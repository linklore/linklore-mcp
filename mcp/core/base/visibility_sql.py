"""Raw-SQL twin of the item visibility predicate."""
from core.base.status import STATUS_DONE, STATUS_DROPPED


VISIBLE_SQL = "deleted_at IS NULL"


LIVE_SQL = "deleted_at IS NULL AND head=1"


SURFACING_EXCLUDED_STATUSES = (STATUS_DROPPED, STATUS_DONE)
