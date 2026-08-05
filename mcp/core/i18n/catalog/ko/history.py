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


    "no_history_max_zero": "표시 0건 (max=0 지정됨, 실제 이력 {total}개 존재 — max를 늘리세요).",
    "unified_header": "# 프로젝트 이력 ({n}개)",


    "log_max_clamped_hint": "\n  … 전체 {total}건 중 {shown}건 표시(서버 상한 {cap}) — 더 보려면 log(id=...)로 개별 조회하거나 period=로 좁히세요",
}
