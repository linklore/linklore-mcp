"""Korean (ko) messages for the 'lore_batch' surface."""
MESSAGES: dict[str, str] = {

    "err_no_edits": "오류: edits 필수 — JSON 배열 또는 list",
    "err_edits_invalid_json": "오류: batch가 유효한 JSON 배열이 아닙니다.",
    "err_edits_not_array": "오류: batch가 JSON 배열이어야 합니다.",

    "link_post_failed": "  ⚠️ link({a}↔{b}) 실패: {res}",

    "batch_summary": "{success}/{total}건",

    "batch_edit_errors_suffix": " ({n}건 오류)\n{errors}",

    "link_post_header": "🔗 링크 후처리:",

    "err_no_items": "오류: items 필수 — list[dict] 또는 JSON 배열",
    "err_items_invalid_json": "오류: items가 유효한 JSON/list가 아닙니다.",
    "err_items_not_list": "오류: items가 list여야 합니다.",

    "err_entry_not_object": "항목이 객체가 아닙니다.",
    "err_title_missing": "title 누락",

    "batch_add_errors_suffix": " ({n}건 오류: {errors})",


    "status_invalid_default": (
        "⚠️ status '{input}' 무효 — open 으로 저장됨. "
        "수정: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "rule_tag_removed": (
        "ℹ️ #rule 태그는 폐지됨 — 규칙 지정은 status='rule' 이 정본 (강/약은 level). "
        "태그에서 제외했습니다."
    ),
}
