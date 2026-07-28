"""Korean (ko) messages for the 'report' surface."""
MESSAGES: dict[str, str] = {
    "tool_desc": (
        "report(msg) — 피드백/버그를 팀에 바로 전송. 로그인 여부와 무관하게 항상 동작 "
        "(로그인돼 있으면 자동으로 iam이 함께 첨부됨, 강제 아님)."
    ),
    "help": (
        "report(msg)\n"
        "  피드백/버그를 팀에 바로 전송 — 익명도 가능(로그인 불요).\n"
        "  - msg: 보낼 내용 (필수)\n"
        "  로그인돼 있으면 iam 이 자동 첨부돼 후속 확인이 쉬워짐 — 강제 아님."
    ),
    "err_msg_required": "오류: msg 필수 — 보낼 내용을 적어 주세요 (예: report(msg='...'))",
    "err_failed": "오류: 전송 실패 ({code}) — {resp}",
    "success": "피드백 전송 완료 — 보내주셔서 고마워요 🙏",
}
