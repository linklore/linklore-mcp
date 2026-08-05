"""Korean (ko) messages for the 'format_search' surface."""
MESSAGES: dict[str, str] = {
    "small_corpus_extra": ' · 폐기본 포함은 status="dropped"',
    "no_match_small_corpus": "'{query}' 매칭 없음 (전체 기록 {corpus}건) — 키워드를 바꾸거나 show()로 전체 목록{extra}",
    "summary_lore": "lore {count}건",
    "summary_doc": "doc {count}건",
    "search_result_header": "'{query}' 검색 결과: {summary}",
    "resolved_part_new_version": '"{title}" → 새 버전 [{new_id}]',
    "resolved_part_dropped": '"{title}"(폐기)',
    "more_suffix": " 외 {count}건",
    "resolved_excluded_with_matches": "(정리됨 {total}건 제외 — 매칭: {titles}{more})",
    "resolved_excluded_plain": "(정리됨 {total}건 제외 · 폐기/대체)",
    "lore_header_start": "## lore ({matches}/{total}건",
    "lore_header_resolved_matched": ", 정리됨 {resolved_total}건 중 매칭 {resolved_matches}건",
    "lore_header_resolved_excluded": ", 정리됨 {resolved_total}건 제외",
    "suggestions_header": "연관도 순 추천:",
    "suggestion_item": "  {id}  {title}  {tags}",


    "snippet_line": '  "{snippet}"',
    "resolved_matches_header": "정리됨 중 매칭 ({count}건) — show(query=) 로 전문:",
    "resolved_item_replaced": "  - [대체됨] {title} → 새 버전: {new_id} [{id}]",
    "resolved_item_dropped": "  - [폐기] {title} [{id}]",
    "resolved_snippet_line": '      "{snippet}"',
    "doc_header": "## doc ({matches}/{total}건)",
    "doc_files_bracket": " [{files}]",
    "no_match_footer": "매칭 결과 없음 — 키워드를 바꿔 다시 검색하세요.",
    "resolved_hint_footer": '정리된(폐기·대체) lore까지 보려면 status="dropped"를 사용하세요.',


    "broad_query_time_hint": "\n  시간순 전개: show(query='{query}', sort='oldest')",
}
