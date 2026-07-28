"""Argument normalization - accepts str or list unions from tool calls."""
from __future__ import annotations

import json

from core.i18n import msg


def normalize_list(value) -> list:
    if value is None or value == "":
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, str):
        s = value.strip()
        if s.startswith("["):
            try:
                parsed = json.loads(s)
                if isinstance(parsed, list):
                    return parsed
            except (ValueError, TypeError):
                pass
        return [v.strip() for v in s.split(",") if v.strip()]
    return []


def normalize_str_list(value) -> list[str]:
    items = normalize_list(value)
    return [str(x) for x in items if isinstance(x, str)]


def parse_batch_arg(value) -> list:
    if isinstance(value, list):
        return value
    return json.loads(value)


def is_batch_dict_list(value) -> bool:
    return (
        isinstance(value, list)
        and len(value) > 0
        and isinstance(value[0], dict)
    )


def reject_foreign_keys(entry: dict, foreign_keys: tuple, label: str,
                        *, foreign_kind: str, own_kind: str) -> str | None:
    hit = [k for k in foreign_keys if entry.get(k)]
    if not hit:
        return None
    return msg("args.err_foreign_key", label=label, hit=", ".join(hit),
               foreign_kind=foreign_kind, own_kind=own_kind)


def reject_retired_keys(entry: dict, label: str) -> str | None:
    if entry.get("toggle"):
        return msg("args.err_retired_toggle", label=label)
    return None


def coerce_toggle_ints(value):
    if isinstance(value, int) and not isinstance(value, bool):
        if value < 0:
            return value
        return f"✓{value}"
    if (isinstance(value, list) and value
            and all(isinstance(x, int) and not isinstance(x, bool) for x in value)):
        if any(x < 0 for x in value):
            return value
        return ",".join(f"✓{i}" for i in value)
    return value
