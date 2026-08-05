"""English (en) messages for the 'history' surface."""
MESSAGES: dict[str, str] = {

    "err_not_found": "error: '{id}' not found.",

    "lore_no_history": "lore/{id} — no history.",
    "lore_history_header": "# lore/{id} change history ({n})",


    "body_history_header": "## body edit history ({n} — append/overwrite/section changes)",


    "body_history_append_line": "- {when}  [append +{delta} chars]  {preview}",


    "body_history_section_line": "- {when}  [section {delta} chars replaced]  {preview}",

    "doc_no_history": "doc/{id} — no history.",
    "doc_history_header": "# doc/{id} change history ({n})",

    "no_history_at_all": "No history.",


    "no_history_max_zero": "0 shown (max=0 was requested — {total} entries exist, increase max).",
    "unified_header": "# project history ({n})",


    "log_max_clamped_hint": "\n  … {shown} of {total} shown (server cap {cap}) — narrow with period=, or use log(id=...) for a single item's full history",
}
