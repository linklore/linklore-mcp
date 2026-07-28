"""English (en) messages for the 'update' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "status() — detects code↔doc sync drift (git-diff based). Not for reading lore/doc content → use show()/brief().\n"
        "\n"
        "since, action(''|'ack'|'reset'), ack, reset, help.\n"
        "(2026-07-09: the dead params auto=/sync= and ack_all= were removed — ack='all' does the same job, matching the reset='all' convention)"
    ),

    "help": (
        "status — code↔doc sync status (git-diff based stale detection)\n"
        "  ⚠️ not for reading lore/doc content or progress — that's show() · brief() · show(type='doc').\n"
        "  This tool finds files where 'the code changed but the doc didn't follow'.\n\n"
        "(no args) → list of stale docs (doc not updated after a code change)\n"
        "since: git comparison base ('HEAD~3', a commit hash)\n"
        "action='ack', ack=name|'all' → mark as acknowledged (omitting action= with ack= set works the same)\n"
        "action='reset', reset=name|'all' → clear ack (omitting action= with reset= set works the same)\n"
    ),
    "err_action_invalid": "error: action='{action}' is not supported — use one of ack|reset (or omit it)",
    "err_invalid_since": (
        "error: since='{since}' is not a valid git ref (commit hash, HEAD~N, tag, branch). "
        "since= expects a git rev-spec — for a date/day-count filter use show()/log()'s period= instead."
    ),
    "err_reset_requires_name": "error: action='reset' requires reset=(a name or 'all')",
    "reset_all_done": "All acks have been reset.",
    "reset_names": "ack reset: {names}",
    "reset_none": "No acks to reset.",
    "no_changes": (
        "code↔doc sync OK — no changed code files detected (no doc updates needed).\n"
        "(if you meant to check lore/doc content or progress → show() · brief() · show(type='doc'))"
    ),
    "err_ack_requires_name": "error: action='ack' requires ack=(a name or 'all')",
    "names_not_found": "⚠️ names not found: {names}",
    "ack_done": "acknowledged: {names}",
    "ack_remaining": "\nremaining stale: {count}",
    "ack_all_resolved": "\nall stale items resolved.",
    "ack_no_match": "No matching stale docs.",
    "header_changed": "# code changes detected: {count} file(s)",
    "all_silent": (
        "{count} code change(s) detected — all of them only scope-match a doc (not tightly coupled), "
        "so no notice is shown (no action needed).\n"
        "(if a tightly-coupled doc appears, this will show up here — link a file directly to a doc with file= to tightly couple it)"
    ),
    "section_affected_header": "## doc updates needed ({count}) — judge each doc",
    "item_header": "### {name} [{id}]",
    "item_files": "  changed code: {files}",
    "item_judge1": "  judgment: • needs update  → edit(id='{id}', msg='summary of the change')",
    "item_judge2": "        • unrelated/already seen → status(ack='{id}')",
    "item_judge3": "        • later          → leave as is (will resurface on the next commit)",
    "acked_summary": "acknowledged {count} — restore with status(reset=...)",
    "section_unmatched_header": "## unmatched files ({count})",
    "unmatched_item": "  - `{file}`",
    "unmatched_footer": "  → if a related doc exists, edit(id, links=['path']); otherwise ignore (code-doc unrelated)",
}
