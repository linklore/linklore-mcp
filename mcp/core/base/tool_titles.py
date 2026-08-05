"""Single source for each MCP tool's ToolAnnotations.title display label."""
TOOL_TITLES: dict[str, str] = {
    "add": "Create Lore or Doc",
    "brief": "Project Dashboard",
    "cleanup": "Find Duplicate Candidates",
    "config": "Settings, Identity & Session Pin",
    "doc_flow": "Doc Chain Viewer",
    "doc_map": "Doc Link Network Map",
    "doc_rollup": "Summarize Linked Lore",
    "doctor": "Data Integrity Check",
    "edit": "Edit Lore or Doc",
    "forced": "Execute Confirmed Action",
    "init": "Initialize Project",
    "link": "Link Two Items",
    "local_cross": "Cross-Workspace Move/Copy",
    "log": "Change History",
    "market": "Public Catalog Search",
    "openbox": "Shared Box (Cross-Owner)",
    "pull": "Restore From My Server",
    "push": "Backup To My Server",
    "report": "Send Feedback to Team",
    "restore": "Restore From Trash",
    "rm": "Delete Lore or Doc",
    "show": "Search & Read",
    "status": "Code-Doc Drift Check",
    "unlink": "Remove Link",
}


UNADVERTISED_TOOLS: frozenset[str] = frozenset({"forced"})
