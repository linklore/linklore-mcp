"""Korean (ko) messages for the 'update' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "status — 코드↔doc 동기화 상태 (git diff 기반 stale 감지)\n"
        "  ⚠️ lore/doc 내용·진행 상태 조회가 아님 — 그건 show() · brief() · show(type='doc').\n"
        "  이 도구는 '코드는 바뀌었는데 doc 이 안 따라온' 파일을 찾아줌.\n\n"
        "(없음) → stale doc 목록 (코드 변경 후 doc 미갱신)\n"
        "since: git 비교 기준 ('HEAD~3', 커밋해시)\n"
        "action='ack', ack=이름|'all' → 확인 처리 (action= 생략하고 ack= 만 줘도 동일)\n"
        "action='reset', reset=이름|'all' → ack 초기화 (action= 생략하고 reset= 만 줘도 동일)\n"
    ),
    "err_action_invalid": "오류: action='{action}' 미지원 — ack|reset 중 하나 (또는 미지정)",
    "err_invalid_since": (
        "오류: since='{since}' 는 유효한 git ref 가 아님 (커밋해시, HEAD~N, 태그, 브랜치). "
        "since= 는 git rev-spec 전용 — 기간(일수) 필터는 show()/log() 의 period= 사용."
    ),
    "err_reset_requires_name": "오류: action='reset' 은 reset=(이름 또는 'all') 필수",
    "reset_all_done": "모든 ack가 초기화되었습니다.",
    "reset_names": "ack 초기화: {names}",
    "reset_none": "초기화할 ack가 없습니다.",
    "no_changes": (
        "코드↔doc 동기화 OK — git 변경 코드 파일 없음 (doc 갱신 필요 없음).\n"
        "(lore/doc 내용·진행 상태를 보려던 거면 → show() · brief() · show(type='doc'))"
    ),
    "err_ack_requires_name": "오류: action='ack' 은 ack=(이름 또는 'all') 필수",
    "names_not_found": "⚠️ 찾지 못한 이름: {names}",
    "ack_done": "확인 완료: {names}",
    "ack_remaining": "\n남은 stale: {count}건",
    "ack_all_resolved": "\n모든 stale이 해소되었습니다.",
    "ack_no_match": "매칭되는 stale doc가 없습니다.",
    "header_changed": "# 코드 변경 감지: {count}개 파일",
    "all_silent": (
        "코드 변경 {count}건 감지 — 전부 관할 문서(scope)만 있어 안내 생략(강결합 아님, 조치 불요).\n"
        "(강결합 doc이 생기면 여기 다시 뜸 — file= 로 파일을 doc에 직접 연결하면 강결합)"
    ),
    "section_affected_header": "## doc 업데이트 필요 ({count}건) — 각 doc 판단",
    "item_header": "### {name} [{id}]",
    "item_files": "  변경된 코드: {files}",
    "item_judge1": "  판단: • 반영 필요   → edit(id='{id}', msg='변경 요약')",
    "item_judge2": "        • 무관/이미봄 → status(ack='{id}')",
    "item_judge3": "        • 나중에      → 그대로 (다음 커밋에 또 뜸)",
    "acked_summary": "확인 완료 {count}건 — status(reset=...)로 복원 가능",
    "section_unmatched_header": "## 매칭 안 되는 파일 ({count}건)",
    "unmatched_item": "  - `{file}`",
    "unmatched_footer": "  → 관련 doc 있으면 edit(id, links=['경로']), 없으면 무시 (코드-doc 무관)",
}
