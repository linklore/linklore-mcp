"""Korean (ko) messages for the 'history' surface."""
MESSAGES: dict[str, str] = {

    "err_not_found": "오류: '{id}'를 찾을 수 없습니다.",

    "lore_no_history": "lore/{id} 이력 없음.",
    "lore_history_header": "# lore/{id} 변경 이력 ({n}개)",


    "body_history_header": "## 본문 수정 이력 ({n}개 — append/overwrite/section 변경)",


    "body_history_append_line": "- {when}  [append +{delta}자]  {preview}",


    "body_history_section_line": "- {when}  [section {delta}자 교체]  {preview}",

    "doc_no_history": "doc/{id} 이력 없음.",
    "doc_history_header": "# doc/{id} 변경 이력 ({n}개)",

    "no_history_at_all": "이력 없음.",
    "unified_header": "# 프로젝트 이력 ({n}개)",
}
