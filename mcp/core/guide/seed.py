"""Installs and updates the bundled guide as an external source."""
from __future__ import annotations

import hashlib
import importlib
from pathlib import Path

from core.base.dateutil import now_iso
from core.i18n import msg
from core.sync.registry import ensure_entry
from core.sync.remote import (
    _get_remote_doc,
    _get_remote_lore,
    _get_remote_meta,
    _init_remote_dir,
    _save_remote_doc,
    _save_remote_lore,
    _update_remote_meta,
)

SOURCE_NAME = "linklore-guide"
_GUIDE_PID = "linklore-guide"
_GUIDE_PATH = f"local://{_GUIDE_PID}"


def _load_guide_content():
    from core.i18n import _lang
    lang = _lang()
    if lang != "en":
        try:
            mod = importlib.import_module(f"core.guide.content_{lang}")
            return mod.GUIDE_VERSION, mod.ITEMS
        except ModuleNotFoundError:
            pass
    from core.guide.content_en import GUIDE_VERSION, ITEMS
    return GUIDE_VERSION, ITEMS


def _item_id(key: str, kind: str) -> str:
    prefix = "lr" if kind == "lore" else "dc"
    digest = hashlib.sha1(f"linklore-guide:{key}".encode("utf-8")).hexdigest()[:8]
    return f"{prefix}-{digest}"


def _content_sig(item: dict) -> tuple:
    return (
        item.get("title", ""), item.get("body", ""),
        tuple(item.get("tags") or []),
    )


def _build_items(raw_items: list[dict]) -> tuple[list[dict], list[dict]]:
    ts = now_iso()
    lore_out: list[dict] = []
    doc_out: list[dict] = []
    for it in raw_items:
        kind = it.get("kind")
        key = it.get("key", "")
        if not key or kind not in ("lore", "doc"):
            continue
        tags = list(dict.fromkeys([*(it.get("tags") or []), "guide"]))
        base = {
            "id": _item_id(key, kind),
            "title": it.get("title", ""),
            "body": it.get("body", ""),
            "tags": tags,
            "status": "open",
            "head": True,
            "author": SOURCE_NAME,
            "createdAt": ts,
            "updatedAt": ts,
        }
        if kind == "lore":
            base["triggers"] = []
            base["files"] = []
            base["works"] = []
            lore_out.append(base)
        else:
            base["items"] = []
            base["files"] = []
            doc_out.append(base)
    return lore_out, doc_out


def _write_mirror(data_dir: Path, lore_items: list[dict], doc_items: list[dict], version: str) -> None:
    _init_remote_dir(data_dir, _GUIDE_PID, name=SOURCE_NAME, url=_GUIDE_PATH)
    _save_remote_lore(data_dir, _GUIDE_PID, lore_items)
    _save_remote_doc(data_dir, _GUIDE_PID, doc_items)
    _update_remote_meta(data_dir, _GUIDE_PID, guide_version=version)


def _ensure_registry_entry(data_dir: Path) -> None:
    ensure_entry(data_dir, SOURCE_NAME, {
        "path": _GUIDE_PATH,
        "options": {"auto_search": True, "show_prefix": True},
    })


def install_guide_source(data_dir: Path) -> str:
    try:
        GUIDE_VERSION, ITEMS = _load_guide_content()

        lore_items, doc_items = _build_items(ITEMS)
        _write_mirror(data_dir, lore_items, doc_items, GUIDE_VERSION)
        _ensure_registry_entry(data_dir)
        count = len(lore_items) + len(doc_items)
        if count == 0:
            return ""
        return msg("guide.installed", count=count)
    except Exception:
        return ""


def refresh_guide_source(data_dir: Path) -> str | None:
    try:
        meta = _get_remote_meta(data_dir, _GUIDE_PID)
        if not meta:
            return None

        GUIDE_VERSION, ITEMS = _load_guide_content()

        if meta.get("guide_version") == GUIDE_VERSION:
            return None

        old_sig = {
            i.get("id"): _content_sig(i)
            for i in (*_get_remote_lore(data_dir, _GUIDE_PID), *_get_remote_doc(data_dir, _GUIDE_PID))
        }
        lore_items, doc_items = _build_items(ITEMS)
        new_items = [*lore_items, *doc_items]
        changed = sum(1 for i in new_items if old_sig.get(i["id"]) != _content_sig(i))

        _write_mirror(data_dir, lore_items, doc_items, GUIDE_VERSION)
        _ensure_registry_entry(data_dir)

        if changed == 0:
            return None
        return msg("guide.updated", count=changed)
    except Exception:
        return None
