"""English (en) messages for the 'personal' surface."""
MESSAGES: dict[str, str] = {
    "setup_help": (
        "setup_personal — set up my server space (push/pull target, me only)\n"
        "\n"
        "  setup_personal(project_name='') — leave empty to use the current directory name\n"
        "  - handle: set automatically at login (or config(handle=))\n"
        "  - idempotent: calling again with the same handle+project_name reuses the existing space\n"
        "  - saved: remote/personal/personal.json (gitignore)\n"
        "  - next: push() to upload to the server / pull() to restore"
    ),
    "err_no_handle": (
        "error: iam (handle) is not set.\n"
        "  first: uvx llre login  (or config(handle='your-name'))"
    ),
    "err_login_required": (
        "error: login required — server-connect commands (push/pull/connect) require account login first.\n"
        "  a browser login was attempted but not completed. try again, or: uvx llre login"
    ),
    "err_auth_url_hint": (
        "\n  if the browser didn't open, open it directly: {url}"
        "\n  (once logged in, if a token is shown on screen: uvx llre login and paste it, "
        "or set MCP env LINKLORE_TOKEN)"
    ),


    "login_warning_new": "⚠️ login was required, so a browser login was performed ({email}).\n",


    "err_session_expired": (
        "error: the session has expired (401) — the stored token is no longer valid.\n"
        "  a browser re-login was attempted but not completed.\n"
        "  log in again: uvx llre login"
    ),

    "login_warning_reauth": "⚠️ the session expired, so a browser login was performed ({email}).\n",
    "err_backend_init_failed": "error: backend init failed ({code}) — {resp}",
    "status_reused": "reused (existing project)",


    "status_new": "newly created",
    "setup_success": (
        "[{project_name}] my server space — {status}\n"
        "  handle: {handle}\n"
        "  project_id: {pid}\n"
        "  metadata saved: remote/personal/personal.json (gitignore)\n"
        "next: push() = home base→server / pull() = server→home base restore (works across devices too)"
    ),


    "err_sentinel": "error",


    "err_keychain_read_failed": (
        "error: Keychain access failed (you may still be logged in) — "
        "retry after running `uvx llre login` again in a terminal, or allow Keychain access"
    ),
}
