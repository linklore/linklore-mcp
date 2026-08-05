"""Normalizes max/limit parameters shared by result-capping tool logic."""
from core.i18n import msg


def normalize_max(value: int, *, default: int, hard_cap: int = 0) -> int:
    if value < 0:
        raise ValueError(msg("limits.err_negative", value=value))
    if value == 0:
        return default
    if hard_cap and value > hard_cap:
        return hard_cap
    return value
