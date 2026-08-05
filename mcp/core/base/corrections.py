"""Single emission path for auto-correcting response messages - delegates to i18n msg()."""
from core.i18n import msg


def correction(key: str, **fmt) -> str:
    return msg(key, **fmt)
