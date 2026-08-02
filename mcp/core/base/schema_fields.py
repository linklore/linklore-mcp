"""Shared Field description aliases for repeated MCP tool parameters."""
from typing import Annotated

from pydantic import Field

HelpArg = Annotated[
    bool,
    Field(description="Return this tool's full help text instead of executing."),
]

ProjectDirArg = Annotated[
    str,
    Field(
        description=(
            "Run against another LinkLore project directory instead of the "
            "pinned/current one. Rare — most sessions never need this."
        )
    ),
]

ConfirmArg = Annotated[
    int | str,
    Field(
        description=(
            "Confirmation slot number echoed back from a prior 2-step "
            "destructive-action warning. Pass this alone, with no other arguments."
        )
    ),
]
