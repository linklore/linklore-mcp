"""Date parsing helpers - ISO dates and period expressions."""
import re
from datetime import datetime, timezone, timedelta

from core.i18n import msg as _msg


def _parse_iso_only(s: str):
    if not s:
        return None
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    return None


def _parse_period(value: int | str) -> tuple[datetime | None, datetime | None]:
    if value is None or value == "":
        return None, None
    if isinstance(value, int):
        raise ValueError(_msg("dateutil.err_period_int_ambiguous", value=value))
    s = str(value).strip()
    if not s:
        return None, None
    m = re.fullmatch(r"(\d+)([hd])", s)
    if m:
        n, unit = int(m.group(1)), m.group(2)
        delta = timedelta(hours=n) if unit == "h" else timedelta(days=n)
        return now_utc().replace(tzinfo=None) - delta, None
    if ".." in s:
        a, b = s.split("..", 1)
        start, end = _parse_iso_only(a), _parse_iso_only(b)
        if not start or not end:
            raise ValueError(_msg("dateutil.err_period_range_format", value=repr(value)))
        if "T" not in b:
            end = end + timedelta(days=1) - timedelta(seconds=1)
        return start, end
    start = _parse_iso_only(s)
    if not start:
        raise ValueError(_msg("dateutil.err_period_format_unrecognized", value=repr(value)))
    return start, None


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


def parse_iso_dt(s) -> datetime | None:
    if not s:
        return None
    try:
        dt = datetime.fromisoformat(str(s).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def iso(dt: datetime | None) -> str | None:
    if not dt:
        return None
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


def now_iso() -> str:
    return now_utc().strftime("%Y-%m-%dT%H:%M:%S")


def to_local_date(iso_str: str, tz=None) -> str:
    if not iso_str:
        return (iso_str or "")[:10]
    try:
        dt = datetime.fromisoformat(str(iso_str).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return str(iso_str)[:10]
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(tz).strftime("%Y-%m-%d")


def to_local_datetime(iso_str: str, tz=None) -> str:
    if not iso_str:
        return ""
    try:
        dt = datetime.fromisoformat(str(iso_str).replace("Z", "+00:00"))
    except (ValueError, TypeError):
        return str(iso_str)[:16].replace("T", " ")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.astimezone(tz).strftime("%Y-%m-%d %H:%M")
