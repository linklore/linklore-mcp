"""English (en) messages for the 'setup' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "init(blueprint='') — set up .linklore in this directory (starts local footprint memory).\n"
        "\n"
        "- init()              basic setup\n"
        "- init(blueprint='X') apply a blueprint\n"
        "\n"
        "project_dir: set up .linklore in another folder (creating a boundary is init-only). "
        "setting up there doesn't change this session's base project — to keep working there, "
        "config(action='pin').\n"
    ),

    "help": (
        "init — local .linklore setup\n\n"
        "  init()              basic\n"
        "  init(blueprint='X') apply a blueprint\n"
        "  connect to a server: login → push(my server) / openbox(openbox sharing)"
    ),
    "already_exists": ".linklore/ already exists.",
    "next_steps_hint": (
        "\n\nnext steps:\n"
        "① start every session with `brief` (token-efficient context load) "
        "② create a first doc as a 'feature list', then link per-feature detail docs via links="
    ),
    "err_unknown_blueprint": "error: unknown blueprint '{blueprint}'. available: kickstart",


    "anchor_mismatch_notice": (
        "ℹ️ this session's base project is still '{anchor}' - to work in '{target}', "
        "open a session there or config(action='pin', dir='{dir}')"
    ),

    "empty_done": (
        "done: {data_dir} set up\n"
        "\n"
        "just start using it (nothing to pre-fill):\n"
        "  - brief() — current state (empty for now)\n"
        "  - add(type='lore', ...) — record decisions, pitfalls, lessons\n"
        "  - add(type='doc', ...) — core structure docs (only when needed)"
    ),
    "mcp_status_header": "\n\nMCP registration:",
    "mcp_status_claude_code": "  - Claude Code (.claude/settings.json)",
    "mcp_status_session_hook": "  - SessionStart hook — registered",


    "mcp_status_session_hook_exists": "  - SessionStart hook — already registered",
    "mcp_status_session_hook_failed": (
        "  - SessionStart hook — registration failed "
        "(check write permission on .claude/settings.json, then re-run init())"
    ),


    "mcp_status_mcpjson_done": "  - Claude Code project scope (.mcp.json) — registered",
    "mcp_status_mcpjson_exists": "  - Claude Code project scope (.mcp.json) — already registered",
    "mcp_status_cursor_done": "  - Cursor (.cursor/mcp.json) — registered",
    "mcp_status_cursor_exists": "  - Cursor (.cursor/mcp.json) — already registered",
    "mcp_status_gemini_done": "  - Antigravity (~/.gemini/config/mcp_config.json) — registered",

    "mcp_status_uv_hint": (
        "  - ⚠️ uvx not found — registered with an absolute python path fallback. "
        "Installing uv is recommended: https://docs.astral.sh/uv/ ('uvx llre' is more robust)"
    ),
    "mcp_status_gemini_exists": "  - Antigravity (~/.gemini/config/mcp_config.json) — already registered",


    "claude_md_hint_added": (
        "\n\n📋 Automatically added the block below to your CLAUDE.md "
        "(bootstraps the AI to use LinkLore every session):\n\n"
        "{block}"
    ),
    "claude_md_hint_exists": "\n\n📋 CLAUDE.md already has the bootstrap section (added automatically).",
    "claude_md_hint_failed": (
        "\n\n📋 Add the block below to your CLAUDE.md "
        "(bootstraps the AI to use LinkLore every session):\n\n"
        "{block}"
    ),


    "agents_md_hint_added": "\n📋 Also added the same bootstrap to AGENTS.md (for Codex and similar tools).",
    "agents_md_hint_failed": "\n⚠️ Failed to write AGENTS.md automatically — add the same section as CLAUDE.md by hand.",
    "gemini_md_hint_added": "\n📋 Also added the same bootstrap to GEMINI.md (loaded by Gemini CLI on every prompt).",
    "gemini_md_hint_failed": "\n⚠️ Failed to write GEMINI.md automatically — add the same section as CLAUDE.md by hand.",


    "unknown_agent_hint": (
        "\n\n💡 Not using Claude Code, Cursor, Codex, or Gemini CLI? Check this "
        "project's AGENTS.md, or simply call brief() at the start of every session "
        "and search with show() before editing files."
    ),
}
