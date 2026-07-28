"""MCP server entry point - tool registration and runtime wiring."""
import logging
import sys
from pathlib import Path


sys.path.insert(0, str(Path(__file__).parent))

from core.base.datadir import DATA_DIR_NAME


_log_path = Path.home() / DATA_DIR_NAME / "mcp.log"
_log_path.parent.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    filename=str(_log_path), level=logging.DEBUG,
    format="%(asctime)s %(levelname)s %(message)s", datefmt="%H:%M:%S",
)
_log = logging.getLogger("linklore")


import os as _os
_my_pid = _os.getpid()
_my_cwd = Path.cwd()

from core.infra.version import version_label, cleanup_stale_peers
_log.info("server starting — pid=%d, cwd=%s, version=%s",
          _my_pid, _my_cwd, version_label())


_killed = cleanup_stale_peers(_my_pid, _my_cwd)
if _killed:
    _log.info("cleaned %d orphan mcp pid(s): %s", len(_killed), _killed)

from core.infra.app import mcp
import tools


from core.infra.pin_layer import _apply_session_pin_layer

_apply_session_pin_layer(mcp)
_log.info("tools loaded, ready")


from tools.cli import (
    _cli_param_types_from_fn,
    _cli_param_types_from_schema,
    _cli_usage,
    _parse_cli_kwargs,
    _run_cli,
)

__all__ = [
    "main",
    "_cli_param_types_from_fn",
    "_cli_param_types_from_schema",
    "_cli_usage",
    "_parse_cli_kwargs",
    "_run_cli",
]


def main():

    if len(sys.argv) > 1:
        sys.exit(_run_cli(sys.argv[1:]))


    from core.search.embed import warm_embedding_bg
    warm_embedding_bg()
    _log.info("mcp.run() starting")
    mcp.run()


if __name__ == "__main__":
    main()
