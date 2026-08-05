"""English (en) messages for the 'format_search' surface."""
MESSAGES: dict[str, str] = {
    "small_corpus_extra": ' · to include dropped items use status="dropped"',
    "no_match_small_corpus": "no matches for '{query}' ({corpus} total records) — try a different keyword or see the full list with show(){extra}",
    "summary_lore": "{count} lore",
    "summary_doc": "{count} doc",
    "search_result_header": "search results for '{query}': {summary}",
    "resolved_part_new_version": '"{title}" → new version [{new_id}]',
    "resolved_part_dropped": '"{title}" (dropped)',
    "more_suffix": " +{count} more",
    "resolved_excluded_with_matches": "({total} resolved excluded — matches: {titles}{more})",
    "resolved_excluded_plain": "({total} resolved excluded · dropped/replaced)",
    "lore_header_start": "## lore ({matches}/{total}",
    "lore_header_resolved_matched": ", {resolved_matches} matched among {resolved_total} resolved",
    "lore_header_resolved_excluded": ", {resolved_total} resolved excluded",
    "suggestions_header": "top suggestions by relevance:",
    "suggestion_item": "  {id}  {title}  {tags}",


    "snippet_line": '  "{snippet}"',
    "resolved_matches_header": "matches among resolved ({count}) — show(query=) for full text:",
    "resolved_item_replaced": "  - [replaced] {title} → new version: {new_id} [{id}]",
    "resolved_item_dropped": "  - [dropped] {title} [{id}]",
    "resolved_snippet_line": '      "{snippet}"',
    "doc_header": "## doc ({matches}/{total})",
    "doc_files_bracket": " [{files}]",
    "no_match_footer": "no matches — try different keywords.",
    "resolved_hint_footer": 'to include resolved (dropped/replaced) lore, use status="dropped".',


    "broad_query_time_hint": "\n  chronological view: show(query='{query}', sort='oldest')",
}
