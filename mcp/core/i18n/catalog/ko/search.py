"""Korean (ko) messages for the 'search' surface."""
MESSAGES: dict[str, str] = {
    "empty": (
        "결과 없음 — 아직 이 프로젝트에 기억이 없습니다.\n"
        "add(type='lore'/'doc', ...) 로 첫 기록을 남기면 발자취가 시작됩니다."
    ),
    "err_no_id": "오류: ID를 입력하세요.",
    "err_not_found_empty": "'{id}'를 찾을 수 없습니다 — 아직 이 프로젝트에 기억이 없습니다.",
    "err_not_found": "오류: '{id}'를 찾을 수 없습니다.",
    "hint_token": "'{term}' {count}건",
    "common_word_hint": "ℹ️ 흔한 단어가 매칭을 채웠습니다 — {parts} 등장. 특징적인 단어를 1–2개 추가하면 좁혀집니다.\n\n",
    "no_exact_match_suggestions": "'{query}' 정확한 매칭 없음. 연관도 순 추천:",
    "no_match": "'{query}' 관련 lore/doc을 찾을 수 없습니다.",
    "err_openbox_not_registered": "오류: openbox '{name}' 미등록",
    "tags_label": "태그: {tags}",
    "copy_hint": "\n→ openbox(name='{openbox}', action='pull', id='{id}') 카피",


    "external_id_hint": (
        "\nℹ️ 이 id는 오픈박스 '{name}'에 있습니다 — "
        "openbox(name='{name}', action='show', query='{id}') 또는 openbox(name='{name}', action='pull', id='{id}')"
    ),
    "err_id_not_found": "[{openbox}] '{query}' ID 없음 (lore {lore_count} / doc {doc_count})",
    "no_match_external": "[{openbox}] '{query}' 매칭 없음 (lore {lore_count} / doc {doc_count})",
    "search_header": "# [{openbox}] '{query}' 검색",
    "lore_section_header": "\n## lore ({count}건)",
    "doc_section_header": "\n## doc ({count}건)",
    "more_items": "  외 {count}건",
    "copy_hint_example": "\n→ openbox(name='{openbox}', action='pull', id='lr-...') 카피",
    "kw_title_fallback": ",#8제목직격",
}
