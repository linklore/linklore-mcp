"""Korean (ko) messages for the 'auth_fallback' surface."""
MESSAGES: dict[str, str] = {


    "box_access_denied": (
        "박스 '{name}' 접근 거부 — 멤버가 아니거나 iam이 폐기됐을 수 있습니다. "
        "확인: config(action='whoami') · "
        "가입: openbox(action='join', code=<초대코드>) · "
        "프로젝트 iam 재발급: 박스 owner에게 openbox(name='{name}', action='invite', member='<member_id>') 요청"
    ),


    "heal_project_reinvite": (
        "오류: 프로젝트 iam이 거부되었습니다 (401) — 세션이 회전됐거나 폐기됐을 수 있습니다.\n"
        "  브라우저 재로그인으로는 복구되지 않습니다 (프로젝트 iam이 계정보다 우선).\n"
        "  박스 owner에게 재발급 초대를 요청하세요: "
        "openbox(name='<박스>', action='invite', member='<닉네임>')\n"
        "  받은 코드로 이 프로젝트에서: openbox(action='join', code='<초대코드>')"
    ),


    "heal_env_rejected": (
        "오류: LINKLORE_TOKEN이 거부되었습니다 (401) — 주입된 토큰이 만료/폐기된 것 같습니다.\n"
        "  MCP 설정(env LINKLORE_TOKEN)의 토큰을 새 것으로 교체한 뒤 재시도하세요."
    ),

    "heal_login_required": (
        "오류: 로그인이 필요합니다 — uvx llre login 후 재시도하세요."
    ),
}
