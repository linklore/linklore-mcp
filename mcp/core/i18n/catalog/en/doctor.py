"""English (en) messages for the 'doctor' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "doctor() - checks project data integrity (oldId/newId, files[] paths, link targets).\n"
        "\n"
        "doctor()             read-only diagnostics (default)\n"
        "doctor(action='fix') automatically repairs any issues found\n"
    ),

    "help": (
        "doctor - checks project data integrity + auto-repair\n"
        "\n"
        "  doctor()             read-only diagnostics - oldId/newId supersede chain (lore/doc),\n"
        "                       lore/doc files[] path existence, lore_links/doc_links/lore_works\n"
        "                       reference target existence\n"
        "  doctor(action='fix') automatically repairs found issues (reconnects oldId/newId, clears\n"
        "                       dangling refs, completes half-sealed supersedes, deletes orphaned\n"
        "                       relation rows), then re-verifies and summarizes\n"
        "\n"
        "WARNING: missing files[] paths (stale) and supersede_fork are diagnostic only - the file\n"
        "  can't be restored, and a fork can't be machine-resolved, so neither is auto-fixed.\n"
        "  manual stale cleanup: reconnect with edit(id, links=['new/path']) - remove a dead ref with unlink(id, 'old/path')"
    ),
    "err_action_invalid": "error: action='{action}' is not supported - use '' or 'fix'",
    "ok_no_issues": "OK - no issues found",
    "check_header": "# integrity check - error {error} - warn {warn} - info {info}",
    "auto_fix_hint": "items that can be auto-repaired (oldId/newId, link targets) - doctor(action='fix')",
    "stale_hint": "stale (missing file) is manual cleanup - reconnect: edit(id, links=['new/path']) - remove dead ref: unlink(id, 'old/path')",
    "fix_header": "# doctor(action='fix') results",
    "fixed_header": "fixed items ({count}):",
    "nothing_fixed": "nothing to fix.",
    "remaining_issues": "\nremaining issues (error {remaining}) - run doctor() for details",
    "no_remaining": "\nre-verified: no remaining errors.",
}
