"""Korean (ko) messages for the 'doc_edit' surface."""
MESSAGES: dict[str, str] = {

    "err_status": "오류: {err}",
    "err_generic": "오류: {e}",
    "err_link_resolve": "오류: 링크 해결 실패\n{e}",
    "err_flow_link_resolve": "오류: 흐름 링크 해결 실패\n{e}",
    "err_not_found_doc": "오류: doc '{id}'를 찾을 수 없습니다.",


    "rule_tag_removed": (
        "ℹ️ #rule 태그는 폐지됨 — 규칙 지정은 status='rule' 이 정본. "
        "태그에서 제외했습니다."
    ),


    "items_schema_error_skip": (
        "\n⚠️ items 스키마 오류로 스킵됨 (문서는 저장됨) — "
        "수정: edit(id='{id}', items=[...])\n{err}"
    ),


    "status_invalid_default": (
        "⚠️ status '{input}' 무효 — open 으로 저장됨. "
        "수정: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "status_invalid_skip": (
        "status '{input}' 무효 — 스킵, 기존값('{current}') 유지. "
        "재시도: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "err_title_required": "오류: title 필수 — add(type='doc', title='...')",
    "auto_tags_notice": (
        "  태그 자동: #{tags} — "
        "수정: edit(id='{id}', tags=[...], action='overwrite') · 해제: tags='-'"
    ),
    "linked_confirm": "🔗 연결됨 (links=): {ids}",
    "flow_linked_confirm": "→ 흐름 연결됨 (flow_links=): {ids}",
    "link_unresolved_header": "\n⚠️ 일부 링크를 해석하지 못함 (doc 은 저장됨) — id 확인 후 link() 로 재연결:\n",
    "suggestion_header": "관련 후보 (제안 · 연결 안 됨 — 엮으려면 links=/link()):",


    "dup_header": "🚨 매우 비슷한 doc (중복 가능):",
    "dup_line": "  - {title} [{id}]{author}{badge} (cos={cos})",
    "dup_preview": "    ↳ {preview}",
    "dup_judge_header": "   판단 (열지 말고 위 미리보기로 — 같은 결정?):",
    "dup_action_supersede": "   • 방금 게 나음  → link(a='{top_id}', b='{new_id}', action='supersede')",
    "dup_action_keep": "   • 기존 유지     → rm(id='{new_id}', force=True)",
    "dup_action_unrelated": "   • 무관(관련 없음) → link(a='{new_id}', b='{top_id}', action='unrelated')",
    "dup_action_distinct": "   • 중복 아님(별개 확정) → link(a='{new_id}', b='{top_id}', action='distinct')",
    "dup_judge_fallback": "   → 본문 확인 후: link(action='supersede') 또는 rm(force=True) 또는 유지",


    "conflict_header": "⚠️ 상충 후보 (주제 같음 — 결론 반대인지 확인):",
    "conflict_line": "  - {title} [{id}]{badge} (근거: {evidence})",
    "conflict_hint": "   판단: 반대 결정 → 현행 확정 후 link(action='supersede') · 보완 → links=/link() 로 엮기 · 무관 → link(a='{new_id}', b='{top_id}', action='unrelated')",


    "err_no_title_or_msg": "오류: title 또는 msg를 지정하세요.",
    "supersede_result": (
        "[{new_id}] {title}\n"
        "  ↳ supersede: {old_id} → {new_id} "
        "(새 doc 박힘, 옛 doc는 head=False로 보존)\n"
        "  ⚠️ append 아님 — 옛 본문은 검색/브리핑 기본 결과에 안 보임. "
        "같은 ID에 본문만 추가하려면 edit(msg=...) 사용."
    ),


    "collection_cleared": "{label} 해제 — 기존 {n}개 제거",
    "collection_replaced": "{label} 교체 — {old_n}개 → {new_n}개",
    "collection_added": "{label} +{n}개 (총 {total}개)",


    "toggle_parse_failed": "⚠️ 토글 파싱 실패 — 실행 안 함.",
    "bad_tokens": "  이해 못 한 토큰: {tokens}",
    "out_of_range": "  범위 밖 번호: {nums}",
    "no_items_hint": "  이 doc 엔 항목이 없습니다 — 먼저 추가: edit(id='{id}', items=['새 항목'])",
    "current_items_header": "현재 항목:",
    "current_items_more": "  … 외 {n}건 — 전체: show(query='{id}')",
    "retry_hint": "재시도: edit(id='{id}', items=1)  # ← 유효 번호로",


    "err_remove_msg_conflict": (
        "오류: action='remove' 는 msg= 와 동시 사용 불가 — 제거는 단독 호출: "
        "edit(id='{id}', action='remove', items=[N])"
    ),
    "err_remove_items_required": (
        "오류: action='remove' 는 items(제거할 1-based 번호) 필수 — "
        "edit(id='{id}', action='remove', items=[N])"
    ),
    "err_remove_items_type": (
        "오류: action='remove' 의 items 는 int 또는 양의 정수 리스트만 허용 — "
        "edit(id='{id}', action='remove', items=[N])"
    ),


    "err_remove_syntax_retired": (
        "오류: items 문자열('-N')·음수로 제거하는 옛 문법은 은퇴됐습니다 — "
        "edit(id='{id}', action='remove', items=[N])"
    ),
    "err_toggle_syntax_retired": (
        "오류: items='✓N'/'vN' 문자열 토글 문법은 은퇴됐습니다 — "
        "edit(id='{id}', items=[N])  # int 또는 int 리스트"
    ),
    "err_add_syntax_retired": (
        "오류: items='+텍스트' 문자열 추가 문법은 은퇴됐습니다 — "
        "edit(id='{id}', items=['텍스트'])"
    ),


    "err_create_operator_tokens": (
        "생성 시엔 연산 불가 — 일반 텍스트만: {tokens} "
        "(그대로 쓰려면 dict: items=[{{'text': '...'}}])"
    ),


    "list_operator_header": "⚠️ items 리스트 처리 안 함 — 은퇴된 연산자꼴 원소가 있습니다.",
    "list_operator_tokens": "  문제 토큰: {tokens}",
    "list_operator_hint": (
        "제거: edit(id='{id}', action='remove', items=[N]) · "
        "토글: edit(id='{id}', items=[N]) · "
        "이 글자 그대로 추가하려면 dict: items=[{{'text': '...'}}]"
    ),


    "batch_remove_msg_conflict": "{wid}: action='remove' 는 msg 와 동시 사용 불가 — 제거는 단독",
    "batch_remove_items_required": "{wid}: action='remove' 는 items(제거할 번호) 필수",
    "batch_remove_items_type": "{wid}: action='remove' 의 items 는 int 또는 양의 정수 리스트만 허용",
    "batch_remove_syntax_retired": "{wid}: items 문자열/음수 제거 옛 문법 은퇴 — entry에 action:'remove', items:[N]",
    "batch_toggle_syntax_retired": "{wid}: items='✓N'/'vN' 문자열 토글 옛 문법 은퇴 — items:[N](int)",
    "batch_add_syntax_retired": "{wid}: items='+텍스트' 문자열 추가 옛 문법 은퇴 — items:['텍스트']",
    "batch_list_operator_tokens": (
        "{wid}: items 리스트에 은퇴된 연산자꼴 원소 — {tokens} "
        "(dict로 감싸면 리터럴 추가 가능: {{'text': '...'}})"
    ),


    "batch_action_unsupported": "{wid}: action='{action}' 은 배치에서 미지원 — overwrite/remove만 가능(append는 기본값)",


    "toggle_success_header": "[{id}] {title}  ({total}개 중 {done} 완료)",
    "toggle_collapsed_note": "\n  (전체 {total}개 — show(query='{id}')로 상세)",


    "removed_echo": "\n  🗑️ 제거됨: {texts}",
    "removed_echo_more": " 외 {n}건",


    "status_changed_echo": "\n  status: {old} → {new}",


    "err_id_required": "오류: id 필수 — edit(id='dc-xxx', ...)",
    "err_no_changes": "오류: 변경할 내용이 없습니다.",
    "err_not_found_edit": "오류: doc '{id}'를 찾을 수 없습니다.",
    "replace_echo": (
        "\n  body 전체 교체 — 옛 {old_len}자 → 새 {new_len}자 "
        "(옛 본문 doc_history 보존, 복구: log(id='{id}'))\n  ↳ {echo}"
    ),
    "append_echo": "\n  body(append) — 기존 {old_len}자 뒤에 +{appended_len}자\n  ↳ {echo}",
    "auto_checked_echo": "\n  items {n}건 자동 체크 (status=done)",


    "stale_append_notice": (
        "현재 본문이 {length}자이고 마지막 수정 후 {days}일 지났습니다 — "
        "오래된 내용이 있는지 확인하거나 필요시 분리를 고려하세요."
    ),


    "edit_batch_help": (
        "doc_edit_batch — 여러 doc 한 번에 수정\n\n"
        "  edits: JSON 배열 또는 list [{{id, action, items, title, tags, links, flow, status}}, ...]\n"
        '  links: 통합 (파일·dc/lr id·제목 자동분류) · flow:true → 문서 여정 체인 · links:"-" → 연결 전체 해제\n\n'
        "items 문법 (doc_edit과 동일, v4):\n"
        '  ["a", "b", "c"]           → 추가 (append, 기본·비파괴)\n'
        '  ["a","b"] + "overwrite":true → 전체 교체\n'
        '  [1, 3]                   → 토글 (int 리스트, 1-based)\n'
        '  "action":"remove", "items":[3,1]  → 제거 (1-based, 파괴적 — action 필수)\n'
        "  ⚠️ items='-N'/'✓N'/'+텍스트' 문자열 접두 문법은 은퇴됨\n\n"
        "예시:\n"
        '  doc_edit_batch(edits=\'[{{"id":"dc-xxx","items":[1,3]}}, '
        '{{"id":"dc-yyy","action":"remove","items":[2]}}]\')\n'
    ),
    "err_edits_required": "오류: edits 필수 — JSON 배열 또는 list",
    "err_edits_invalid_json": "오류: edits가 유효한 JSON 배열이 아닙니다.",
    "err_edits_not_list": "오류: edits가 JSON 배열이어야 합니다.",
    "batch_bad_tokens": "이해 못 한 토큰: {tokens}",
    "batch_out_of_range": "범위 밖: {nums} (항목 1..{n})",
    "batch_no_items": "이 doc 엔 항목이 없습니다",
    "batch_toggle_error": "{wid}: 토글 번호 오류 — {detail}",
    "result_count": "{success}/{total}건",
    "err_count_suffix": " ({n}건 오류)",


    "add_batch_help": (
        "doc_add_batch — 여러 doc 한 번에 생성\n\n"
        "  docs: list[dict] 권장 — [{{title, items, tags, links, flow}}, ...]\n"
        "  JSON string도 backwards compat\n\n"
        "각 항목의 items/tags/links는 list 또는 쉼표 string\n"
        "links: 통합 (파일·dc/lr id·제목 자동분류) · flow:true → 문서 여정 체인\n\n"
        "예시:\n"
        '  doc_add_batch(docs=[{{"title":"인증","items":["OAuth","JWT"]}}])\n'
    ),
    "title_missing": "title 누락",
    "err_docs_required": "오류: docs 필수 — list[dict] 또는 JSON 배열",
    "err_docs_invalid": "오류: docs가 유효한 JSON/list가 아닙니다.",
    "err_docs_not_list": "오류: docs가 list여야 합니다.",
    "result_created": "{success}/{total}건 생성",
    "errors_section_header": "\n오류:\n",
}
