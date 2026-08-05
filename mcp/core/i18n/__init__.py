"""User-facing message catalog with locale detection."""
import importlib
import os
from functools import lru_cache
from pathlib import Path


DEFAULT_LANG = "en"

_CATALOG_DIR = Path(__file__).parent / "catalog"


def _lang() -> str:
    explicit = os.environ.get("LINKLORE_LANG")
    if explicit:
        if (_CATALOG_DIR / explicit).is_dir():
            return explicit
        return DEFAULT_LANG
    for var in ("LC_ALL", "LC_MESSAGES", "LANG"):
        v = os.environ.get(var)
        if v:
            code = v.split(".")[0].split("_")[0].lower()
            if code and (_CATALOG_DIR / code).is_dir():
                return code
            break
    return DEFAULT_LANG


@lru_cache(maxsize=None)
def _load_shard(lang: str, shard: str) -> dict:
    modname = f"core.i18n.catalog.{lang}.{shard}"
    try:
        mod = importlib.import_module(modname)
    except ModuleNotFoundError as e:
        raise KeyError(
            f"i18n: 카탈로그 샤드 없음 — lang={lang!r} shard={shard!r} "
            f"(기대 경로 core/i18n/catalog/{lang}/{shard}.py)"
        ) from e
    messages = getattr(mod, "MESSAGES", None)
    if not isinstance(messages, dict):
        raise KeyError(f"i18n: {modname} 에 MESSAGES: dict 가 없습니다")
    return messages


def msg(key: str, **fmt) -> str:
    if "." not in key:
        raise KeyError(f"i18n: key 형식은 '<샤드>.<슬러그>' 여야 합니다 — got {key!r}")
    shard, _, slug = key.partition(".")
    lang = _lang()
    template = _lookup(lang, shard, slug)
    if template is None and lang != DEFAULT_LANG:
        template = _lookup(DEFAULT_LANG, shard, slug)
    if template is None:
        raise KeyError(f"i18n: 키 없음 — {key!r} (lang={lang!r}, shard={shard!r})")
    return template.format(**fmt)


def _lookup(lang: str, shard: str, slug: str) -> str | None:
    try:
        catalog = _load_shard(lang, shard)
    except KeyError:
        return None
    return catalog.get(slug)


__all__ = ["msg", "DEFAULT_LANG"]
