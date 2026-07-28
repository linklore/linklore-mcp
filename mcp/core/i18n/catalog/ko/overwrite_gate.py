"""Korean (ko) messages for the 'overwrite_gate' surface."""
MESSAGES = {
    "err_confirm_not_alone": (
        "오류: confirm= 은 단독 인자로만 사용할 수 있습니다 — 함께 온 인자: {params}.\n"
        "  위 경고가 준 완성된 명령을 그대로(다른 인자 없이) 재호출하세요."
    ),
    "err_plan_not_found": (
        "오류: 그 확인 번호에 해당하는 대기 중인 실행이 없습니다 (15분 경과로 만료됐거나, "
        "이미 실행/취소됐거나, 다른 도구의 번호일 수 있습니다).\n"
        "  처음부터 다시 시도하세요(확인 없이 원래 명령 재호출)."
    ),
    "err_legacy_confirm": (
        "오류: 옛 확인 방식(코드 문자열/불리언 True)은 폐지됐습니다 — "
        "이제 confirm= 은 경고가 알려주는 번호(예: confirm=1) 입니다.\n"
        "  확인 없이 원래 명령을 다시 호출해 새 경고와 번호를 받으세요."
    ),
    "pending_multi_header": "⚠️ 대기 중인 확인이 여러 건입니다 — 번호를 정확히 지정해 재호출하세요:",
    "pending_multi_item": "  {slot}. {desc}{mine_tag}  →  {tool}(confirm={slot})",
    "pending_multi_mine": " (방금 등록됨)",
}
