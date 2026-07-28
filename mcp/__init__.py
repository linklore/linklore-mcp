"""LinkLore MCP server package - long-term project memory for AI agents."""
import sys as _sys
from pathlib import Path as _Path


_pkg_dir = str(_Path(__file__).parent)
if _pkg_dir not in _sys.path:
    _sys.path.insert(0, _pkg_dir)


try:
    from importlib.metadata import PackageNotFoundError as _PNF, version as _version

    try:
        __version__ = _version("llre")
    except _PNF:
        __version__ = "0.1.0+source"
except Exception:
    __version__ = "0.1.0+source"
