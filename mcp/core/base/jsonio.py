"""JSON file I/O primitives with file locking and atomic writes."""
import json
import logging
import os
import subprocess
import sys
import tempfile
from contextlib import contextmanager
from pathlib import Path
from typing import Callable, Iterable

from core.base.log_messages import LOG_MESSAGES


if sys.platform == "win32":
    import msvcrt

    def _flock_ex(lock_fd):
        lock_fd.seek(0)
        msvcrt.locking(lock_fd.fileno(), msvcrt.LK_LOCK, 1)

    def _flock_un(lock_fd):
        lock_fd.seek(0)
        msvcrt.locking(lock_fd.fileno(), msvcrt.LK_UNLCK, 1)
else:
    import fcntl

    def _flock_ex(lock_fd):
        fcntl.flock(lock_fd, fcntl.LOCK_EX)

    def _flock_un(lock_fd):
        fcntl.flock(lock_fd, fcntl.LOCK_UN)


def _restrict_to_owner(path: Path) -> None:
    if sys.platform == "win32":
        user = os.environ.get("USERNAME", "")
        if not user:
            return
        try:
            subprocess.run(
                ["icacls", str(path), "/inheritance:r", "/grant:r", f"{user}:F"],
                capture_output=True, timeout=5, check=False,
            )
        except (OSError, subprocess.SubprocessError):
            pass
        return
    try:
        os.chmod(path, 0o600)
    except OSError:
        pass


def _load_json(path: Path, default=None) -> dict | list:
    if not path.exists():
        return default if default is not None else {}
    return json.loads(path.read_text(encoding="utf-8"))


def _load_json_safe(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except OSError:
        return default
    except json.JSONDecodeError:
        logging.getLogger("linklore").warning(LOG_MESSAGES["json_corrupt_fallback"], path)
        return default


def _atomic_write_bytes(path: Path, content: bytes) -> None:
    fd, tmp = tempfile.mkstemp(dir=str(path.parent))
    try:
        os.write(fd, content)
    finally:
        os.close(fd)
    os.replace(tmp, str(path))


def _save_json(path: Path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = str(path) + ".lock"
    with open(lock_path, "w", encoding="utf-8") as lock_fd:
        _flock_ex(lock_fd)
        try:
            content = json.dumps(data, ensure_ascii=False, indent=2).encode("utf-8")
            _atomic_write_bytes(path, content)
        finally:
            _flock_un(lock_fd)
    try:
        os.remove(lock_path)
    except OSError:
        pass


@contextmanager
def _rmw_lock(path: Path, lock_path: Path | None = None):
    target = Path(lock_path) if lock_path is not None else Path(str(path) + ".rmw.lock")
    target.parent.mkdir(parents=True, exist_ok=True)
    with open(str(target), "w", encoding="utf-8") as lock_fd:
        _flock_ex(lock_fd)
        try:
            yield
        finally:
            _flock_un(lock_fd)


def _self_heal_field(items: Iterable[dict], key: str, normalize: Callable[[str], str]) -> bool:
    changed = False
    for entry in items:
        if isinstance(entry, dict) and isinstance(entry.get(key), str):
            new_val = normalize(entry[key])
            if new_val != entry[key]:
                entry[key] = new_val
                changed = True
    return changed
