"""Status value validation shared by lore and doc."""
from core.i18n import msg as _msg


STATUS_OPEN = "open"
STATUS_DONE = "done"
STATUS_DROPPED = "dropped"
STATUS_RULE = "rule"


VALID_STATUSES = {"", STATUS_OPEN, STATUS_DONE, STATUS_DROPPED, STATUS_RULE}


def normalize_status(s: str) -> tuple[str | None, str]:
    if s and s not in VALID_STATUSES:
        return None, _msg("args.status_invalid")
    return s, ""


def is_resolved(status: str) -> bool:
    return status == STATUS_DROPPED
