"""Confirmation gate for shrinking overwrites - an identical retry confirms."""
from __future__ import annotations

import json
import time
from pathlib import Path

from core.base.datadir import DATA_DIR_NAME
from core.base.jsonio import _atomic_write_bytes, _load_json_safe

_TTL_SECONDS = 900


def _store_path() -> Path:
    return Path.home() / DATA_DIR_NAME / "confirm_pending.json"


def classify_confirm(confirm) -> tuple[str, int]:
    if confirm is False or confirm == "" or confirm == 0:
        return "none", 0
    if isinstance(confirm, bool):
        return "legacy", 0
    if isinstance(confirm, int):
        return ("slot", confirm) if confirm > 0 else ("legacy", 0)
    if isinstance(confirm, str):
        try:
            n = int(confirm.strip())
        except ValueError:
            return "legacy", 0
        return ("slot", n) if n > 0 else ("legacy", 0)
    return "legacy", 0


def _load() -> dict[str, dict[str, dict]]:
    data = _load_json_safe(_store_path(), {})
    if not isinstance(data, dict):
        return {}
    out: dict[str, dict[str, dict]] = {}
    for tool, plans in data.items():
        if not isinstance(plans, dict):
            continue
        clean: dict[str, dict] = {}
        for slot, p in plans.items():
            if (
                isinstance(slot, str) and slot.isdigit()
                and isinstance(p, dict)
                and isinstance(p.get("ts"), (int, float)) and not isinstance(p.get("ts"), bool)
                and isinstance(p.get("key"), str)
                and isinstance(p.get("kwargs"), dict)
            ):
                clean[slot] = p
        if clean:
            out[str(tool)] = clean
    return out


def _save(data: dict) -> None:
    path = _store_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    content = json.dumps(data, ensure_ascii=False).encode("utf-8")
    _atomic_write_bytes(path, content)


def _purge_expired(plans: dict[str, dict]) -> dict[str, dict]:
    now = time.time()
    return {s: p for s, p in plans.items() if now - p["ts"] <= _TTL_SECONDS}


def _pending_list(plans: dict[str, dict]) -> list[tuple[int, str]]:
    items = sorted(plans.items(), key=lambda kv: kv[1]["ts"])
    return [(int(slot), p.get("desc", "")) for slot, p in items]


def register_plan(
    tool: str, key: str, kwargs: dict, *, action: str = "", desc: str = "", notice: str = "",
) -> tuple[int, list[tuple[int, str]]]:
    data = _load()
    plans = _purge_expired(data.get(tool, {}))
    for slot, p in plans.items():
        if p["key"] == key:
            data[tool] = plans
            _save(data)
            return int(slot), _pending_list(plans)

    used = {int(s) for s in plans}
    slot = 1
    while slot in used:
        slot += 1
    plans[str(slot)] = {
        "ts": time.time(), "key": key, "action": action, "desc": desc, "kwargs": kwargs,
        "notice": notice,
    }
    data[tool] = plans
    _save(data)
    return slot, _pending_list(plans)


def peek_plan(tool: str, slot: int) -> dict | None:
    plans = _purge_expired(_load().get(tool, {}))
    entry = plans.get(str(slot))
    return dict(entry) if entry else None


def resolve_plan(tool: str, slot: int) -> dict | None:
    data = _load()
    plans = _purge_expired(data.get(tool, {}))
    entry = plans.pop(str(slot), None)
    if plans:
        data[tool] = plans
    else:
        data.pop(tool, None)
    _save(data)
    return entry
