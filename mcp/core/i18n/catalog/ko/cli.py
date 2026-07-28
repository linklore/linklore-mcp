"""Korean (ko) messages for the 'cli' surface."""
MESSAGES: dict[str, str] = {
    "usage": (
        "LinkLore MCP — 사용법:\n"
        "  uvx llre init       이 디렉토리에 .linklore 셋업 (발자취 메모리 시작)\n"
        "  uvx llre            AI 도구용 MCP 서버 (stdio, 무인자)\n"
        "  uvx llre login      Google 로그인 (브라우저)\n"
        "  uvx llre logout     로컬 토큰 제거 (로그아웃)\n"
        "  uvx llre connect    이 프로젝트를 내 계정에 연결 (개인 백업)\n"
        "  uvx llre whoami     지금 iam 확인\n"
        "  uvx llre doctor     프로젝트 데이터 정합성 점검\n"
        "  uvx llre report <메시지>   피드백/버그 바로 전송 (로그인 불필요)\n"
        "  uvx llre <도구> [키=값 ...]   모든 도구 직접 호출 (예: llre brief / llre show query=lr-x / llre add help=true)\n"
    ),
    "err_run_failed": "오류: llre {sub} 실패 — {err}",
    "err_flag_help": (
        "도움말은 help=true 로 — 예: llre {sub} help=true\n"
        "(-h/--help 대신 help=true 가 전 표면(MCP·CLI) 공통 정문 문법입니다)"
    ),
    "err_kv_format": (
        "오류: 인자는 키=값 형식이어야 합니다 — '{arg}'\n"
        "예시: llre show query=lr-x / llre add type=lore title=제목 msg=내용"
    ),

    "login_already": "이미 로그인됨 ({email}) — 재로그인: llre login --force",
    "err_login_keychain_read_failed": (
        "오류: Keychain 접근 실패 — 로그인 상태를 확인할 수 없습니다 ({err})\n"
        "Keychain 접근을 허용한 뒤 다시 시도하거나, 강제 재로그인: llre login --force"
    ),


    "err_login_start_failed": "오류: 로그인 시작 실패 (백엔드 연결) — 잠시 후 다시 시도하세요.",

    "login_callback_success": "✅ CLI 인증 완료 — 이 창은 곧 이동합니다.",
    "login_callback_failed": "인증 실패 — 터미널에서 <code>uvx llre login</code>을 다시 실행하세요.",

    "logout_already": "이미 로그아웃 상태입니다 (저장된 토큰 없음).",
    "logout_server_revoked": "   서버 세션도 폐기됨.",
    "logout_server_revoke_failed": "   서버 세션은 만료까지 유효 (폐기 실패 — 네트워크/토큰).",
    "err_logout_unlink": "로그아웃 실패 (토큰 파일 제거): {err}",
    "logout_done": "✅ 로그아웃 완료 — 로컬 토큰 제거됨 (~/.linklore/auth.json).",
    "logout_reconnect_hint": "   다시 연결하려면: uvx llre login",

    "paste_token_prompt": "브라우저에 토큰이 표시됐다면 붙여넣으세요 (Enter = 건너뜀): ",
    "err_paste_token_verify": "토큰 검증 실패: {err}",

    "login_done": "✅ 로그인 완료 ({email}) — 토큰 저장됨 (~/.linklore/auth.json).",
    "login_identity_handle": "   신원: @{handle} (user.json)",
    "login_browser_prompt": "브라우저에서 Google 로그인을 완료하세요. (안 열리면 아래 URL 직접 열기)",
    "login_timeout": "시간 초과({timeout}s).",
    "login_retry_hint": "다시 시도하세요: uvx llre login",
    "login_cancelled": "로그인 취소됨 — 다시: uvx llre login",
    "login_mcp_auto_auth": "   이제 'uvx llre' (AI 도구 MCP) 가 이 계정으로 자동 인증됩니다.",
    "login_connect_hint": "   프로젝트 연결: uvx llre connect",

    "telemetry_consent_prompt": (
        "도구 사용 통계(도구 이름·횟수)를 전송해 개선에 참여하시겠어요? "
        "개인 식별 정보는 포함되지 않습니다. [y/N] "
    ),
    "telemetry_result_opt_in": "   통계 전송: 동의 — 변경은 재로그인 또는 LINKLORE_TELEMETRY=off",
    "telemetry_result_opt_out": "   통계 전송: 거부 — 변경은 재로그인 또는 LINKLORE_TELEMETRY=off",
}
