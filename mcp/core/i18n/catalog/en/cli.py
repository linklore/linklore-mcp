"""English (en) messages for the 'cli' surface."""
MESSAGES: dict[str, str] = {
    "usage": (
        "LinkLore MCP — usage:\n"
        "  uvx llre init       set up .linklore in this directory (start the trail memory)\n"
        "  uvx llre            MCP server for AI tools (stdio, no args)\n"
        "  uvx llre login      log in with Google (browser)\n"
        "  uvx llre logout     remove the local token (log out)\n"
        "  uvx llre connect    connect this project to your account (personal backup)\n"
        "  uvx llre whoami     show my iam\n"
        "  uvx llre doctor     check project data integrity\n"
        "  uvx llre report <message>   send feedback/a bug directly (no login needed)\n"
        "  uvx llre <tool> [key=value ...]   call any tool directly (e.g. llre brief / llre show query=lr-x / llre add help=true)\n"
    ),
    "err_run_failed": "error: llre {sub} failed — {err}",
    "err_flag_help": (
        "for help, use help=true — e.g., llre {sub} help=true\n"
        "(help=true, not -h/--help, is the single canonical syntax across surfaces (MCP and CLI))"
    ),
    "err_kv_format": (
        "error: arguments must be key=value — '{arg}'\n"
        "example: llre show query=lr-x / llre add type=lore title=title msg=body"
    ),

    "login_already": "already logged in ({email}) — to re-login: llre login --force",
    "err_login_keychain_read_failed": (
        "error: Keychain access failed — can't check login status ({err})\n"
        "allow Keychain access and retry, or force re-login: llre login --force"
    ),


    "err_login_start_failed": "error: couldn't start login (backend connection) — please try again shortly.",

    "login_callback_success": "✅ CLI authentication complete — this window will redirect shortly.",
    "login_callback_failed": "Authentication failed — run <code>uvx llre login</code> again in your terminal.",

    "logout_already": "already logged out (no saved token).",
    "logout_server_revoked": "   server session revoked too.",
    "logout_server_revoke_failed": "   server session remains valid until it expires (revoke failed — network/token).",
    "err_logout_unlink": "logout failed (removing token file): {err}",
    "logout_done": "✅ logged out — local token removed (~/.linklore/auth.json).",
    "logout_reconnect_hint": "   to reconnect: uvx llre login",

    "paste_token_prompt": "if the browser showed a token, paste it here (Enter = skip): ",
    "err_paste_token_verify": "token verification failed: {err}",

    "login_done": "✅ login complete ({email}) — token saved (~/.linklore/auth.json).",
    "login_identity_handle": "   iam: @{handle} (user.json)",
    "login_browser_prompt": "Complete Google login in your browser. (If it doesn't open, use the URL below.)",
    "login_timeout": "timed out ({timeout}s).",
    "login_retry_hint": "please try again: uvx llre login",
    "login_cancelled": "login cancelled — again: uvx llre login",
    "login_mcp_auto_auth": "   now 'uvx llre' (the AI-tool MCP) will authenticate automatically with this account.",
    "login_connect_hint": "   connect a project: uvx llre connect",

    "telemetry_consent_prompt": (
        "Would you like to help improve LinkLore by sending tool-usage stats "
        "(tool name + count)? No personally identifiable information is included. [y/N] "
    ),
    "telemetry_result_opt_in": "   stats sent: opted in — change via re-login or LINKLORE_TELEMETRY=off",
    "telemetry_result_opt_out": "   stats sent: opted out — change via re-login or LINKLORE_TELEMETRY=off",
}
