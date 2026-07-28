"""Korean (ko) messages for the 'personal' surface."""
MESSAGES: dict[str, str] = {
    "setup_help": (
        "setup_personal — 내 서버 공간 셋업 (push/pull 대상, 나만)\n"
        "\n"
        "  setup_personal(project_name='') — 비우면 현재 디렉토리 이름\n"
        "  - handle: login 시 자동 설정 (또는 config(handle=))\n"
        "  - 멱등: 같은 handle+project_name 재호출 = 기존 공간 재사용\n"
        "  - 저장: remote/personal/personal.json (gitignore)\n"
        "  - 다음 단계: push() 로 서버에 올림 / pull() 로 복원"
    ),
    "err_no_handle": (
        "오류: iam(handle) 미설정.\n"
        "  먼저: uvx llre login  (또는 config(handle='your-name'))"
    ),
    "err_login_required": (
        "오류: 로그인 필요 — 서버 연결 명령(push/pull/connect)은 계정 로그인이 선행됩니다.\n"
        "  브라우저 로그인을 시도했지만 완료되지 않았습니다. 다시 시도하거나: uvx llre login"
    ),
    "err_auth_url_hint": (
        "\n  브라우저가 안 열리면 직접 열기: {url}"
        "\n  (로그인 후 토큰이 화면에 표시되면: uvx llre login 붙여넣기, "
        "또는 MCP 설정 env LINKLORE_TOKEN)"
    ),


    "login_warning_new": "⚠️ 로그인이 필요해 브라우저 로그인을 진행했습니다 ({email}).\n",


    "err_session_expired": (
        "오류: 세션이 만료되었습니다 (401) — 저장된 토큰이 더는 유효하지 않습니다.\n"
        "  브라우저 재로그인을 시도했지만 완료되지 않았습니다.\n"
        "  다시 로그인: uvx llre login"
    ),

    "login_warning_reauth": "⚠️ 세션이 만료되어 브라우저 로그인을 진행했습니다 ({email}).\n",
    "err_backend_init_failed": "오류: backend init 실패 ({code}) — {resp}",
    "status_reused": "재사용 (기존 project)",


    "status_new": "신규 생성",
    "setup_success": (
        "[{project_name}] 내 서버 공간 — {status}\n"
        "  handle: {handle}\n"
        "  project_id: {pid}\n"
        "  메타 저장: remote/personal/personal.json (gitignore)\n"
        "다음: push() = 본진→서버 / pull() = 서버→본진 복원 (다른 기기서도)"
    ),


    "err_sentinel": "오류",


    "err_keychain_read_failed": (
        "오류: Keychain 접근 실패 (로그인 상태는 있을 수 있음) — "
        "터미널에서 `uvx llre login` 재실행 또는 Keychain 접근 허용 후 재시도"
    ),
}
