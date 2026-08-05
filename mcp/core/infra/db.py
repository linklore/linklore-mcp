"""Database engine and session management for the local store."""
import contextvars
import os
from contextlib import contextmanager
from pathlib import Path

from sqlalchemy import Engine, create_engine, event
from sqlalchemy import text as _sql_text
from sqlalchemy.orm import Session, sessionmaker
from core.infra.db_models import Base

from core.infra.schema_gate import (
    CODE_SCHEMA_GENERATION,
    SchemaGenerationError,
    _db_path,
    _run_schema_gate,
)


_engines: dict[str, Engine] = {}
_initialized: set[str] = set()


_active_uow_dirs: contextvars.ContextVar[frozenset[str]] = contextvars.ContextVar(
    "_active_uow_dirs", default=frozenset()
)


def _enable_sqlite_fk(engine: Engine) -> None:
    if engine.dialect.name != "sqlite":
        return

    @event.listens_for(engine, "connect")
    def _set_sqlite_pragma(dbapi_conn, _connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.execute("PRAGMA journal_mode=WAL")
        cursor.execute("PRAGMA busy_timeout=5000")
        cursor.close()


def _db_url(data_dir: Path) -> str:
    url = os.environ.get("LINKLORE_DB_URL")
    if url:
        return url
    p = _db_path(data_dir)
    return f"sqlite:///{p}"


def get_engine(data_dir: Path) -> Engine:
    key = str(data_dir.resolve())
    if key not in _engines:
        engine = create_engine(_db_url(data_dir), echo=False)
        _enable_sqlite_fk(engine)
        _engines[key] = engine

    if key not in _initialized:
        (data_dir / "system").mkdir(parents=True, exist_ok=True)
        Base.metadata.create_all(_engines[key])
        _run_schema_gate(_engines[key], data_dir)
        _initialized.add(key)
    return _engines[key]


def get_session(data_dir: Path) -> Session:
    engine = get_engine(data_dir)
    SessionLocal = sessionmaker(bind=engine, expire_on_commit=False)
    return SessionLocal()


@contextmanager
def uow(data_dir: Path):
    key = str(Path(data_dir).resolve())
    active = _active_uow_dirs.get()
    if key in active:
        raise RuntimeError(f"중첩 uow() — 같은 data_dir({data_dir})에 이미 열린 트랜잭션 안에서 또 uow() — 자기교착 위험")
    token = _active_uow_dirs.set(active | {key})
    try:
        s = get_session(data_dir)
        try:
            if s.get_bind().dialect.name == "sqlite":
                s.execute(_sql_text("BEGIN IMMEDIATE"))
            yield s
            s.commit()
        except Exception:
            s.rollback()
            raise
        finally:
            s.close()
    finally:
        _active_uow_dirs.reset(token)


def init_db(data_dir: Path) -> None:
    get_engine(data_dir)


def reset_engine_cache() -> None:
    global _engines, _initialized
    for engine in _engines.values():
        engine.dispose()
    _engines = {}
    _initialized = set()
