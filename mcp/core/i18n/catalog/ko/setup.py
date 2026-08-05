"""Korean (ko) messages for the 'setup' surface."""
MESSAGES: dict[str, str] = {

    "help": (
        "init — .linklore 로컬 셋업\n\n"
        "  init()              기본\n"
        "  init(blueprint='X') 블루프린트 적용\n"
        "  서버 연결: login → push(내 서버) / openbox(오픈박스 공유)"
    ),
    "already_exists": ".linklore/ 이미 존재합니다.",
    "next_steps_hint": (
        "\n\n다음 걸음:\n"
        "① 매 세션 `brief` 로 시작 (토큰 절약형 컨텍스트 로드) "
        "② 첫 doc 으로 '기능리스트'를 만들고 기능별 상세 doc 을 links= 로 연결"
    ),
    "err_unknown_blueprint": "오류: 알 수 없는 blueprint '{blueprint}'. 사용 가능: kickstart",


    "anchor_mismatch_notice": (
        "ℹ️ 이 세션의 기준 프로젝트는 여전히 '{anchor}'입니다 — '{target}'에서 작업하려면 "
        "그 폴더에서 세션을 열거나 config(action='pin', dir='{dir}')"
    ),

    "empty_done": (
        "완료: {data_dir} 셋업 완료\n"
        "\n"
        "이제 그냥 쓰면 됩니다 (미리 채울 것 없음):\n"
        "  - brief() — 현재 상태 (지금은 비어 있음)\n"
        "  - add(type='lore', ...) — 결정·삽질·교훈 기록\n"
        "  - add(type='doc', ...) — 핵심 구조 문서 (필요할 때만)"
    ),
    "mcp_status_header": "\n\nMCP 등록:",
    "mcp_status_claude_code": "  - Claude Code (.claude/settings.json)",
    "mcp_status_session_hook": "  - SessionStart 훅 — 등록 완료",


    "mcp_status_session_hook_exists": "  - SessionStart 훅 — 이미 등록됨",
    "mcp_status_session_hook_failed": (
        "  - SessionStart 훅 — 등록 실패 (.claude/settings.json 쓰기 권한 확인 후 init() 재실행)"
    ),


    "mcp_status_mcpjson_done": "  - Claude Code 프로젝트 스코프 (.mcp.json) — 등록 완료",
    "mcp_status_mcpjson_exists": "  - Claude Code 프로젝트 스코프 (.mcp.json) — 이미 등록됨",
    "mcp_status_cursor_done": "  - Cursor (.cursor/mcp.json) — 등록 완료",
    "mcp_status_cursor_exists": "  - Cursor (.cursor/mcp.json) — 이미 등록됨",
    "mcp_status_gemini_done": "  - Antigravity (~/.gemini/config/mcp_config.json) — 등록 완료",
    "mcp_status_gemini_exists": "  - Antigravity (~/.gemini/config/mcp_config.json) — 이미 등록됨",

    "mcp_status_uv_hint": (
        "  - ⚠️ uvx 미발견 — python 절대경로 폴백으로 등록됨. "
        "uv 설치 권장: https://docs.astral.sh/uv/ ('uvx llre' 실행이 더 안정적)"
    ),


    "claude_md_hint_added": (
        "\n\n📋 CLAUDE.md에 아래 블록을 자동으로 기입했습니다 "
        "(AI가 매 세션 LinkLore를 쓰게 하는 부트스트랩):\n\n"
        "{block}"
    ),
    "claude_md_hint_exists": "\n\n📋 CLAUDE.md에 부트스트랩이 기입돼 있습니다 (자동).",
    "claude_md_hint_failed": (
        "\n\n📋 CLAUDE.md에 아래 블록을 추가하세요 "
        "(AI가 매 세션 LinkLore를 쓰게 하는 부트스트랩):\n\n"
        "{block}"
    ),


    "agents_md_hint_added": "\n📋 AGENTS.md도 함께 기입했습니다 (Codex 등 발견성용).",
    "agents_md_hint_failed": "\n⚠️ AGENTS.md 자동기입 실패 — CLAUDE.md와 같은 섹션을 수동으로 추가하세요.",
    "gemini_md_hint_added": "\n📋 GEMINI.md도 함께 기입했습니다 (Gemini CLI가 매 프롬프트 로드).",
    "gemini_md_hint_failed": "\n⚠️ GEMINI.md 자동기입 실패 — CLAUDE.md와 같은 섹션을 수동으로 추가하세요.",


    "unknown_agent_hint": (
        "\n\n💡 Claude Code·Cursor·Codex·Gemini CLI가 아닌 도구를 쓰고 있다면 — "
        "이 프로젝트 루트의 AGENTS.md를 참고하거나, 매 세션 brief() 먼저 부르고 "
        "파일 수정 전 show()로 검색하세요."
    ),
}
