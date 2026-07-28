"""English (en) messages for the 'auth_fallback' surface."""
MESSAGES: dict[str, str] = {


    "box_access_denied": (
        "box '{name}' access denied — you may not be a member, or the iam may have "
        "been revoked. "
        "Check: config(action='whoami') · "
        "Join: openbox(action='join', code=<invite_code>) · "
        "Reissue the project iam: ask the box owner for "
        "openbox(name='{name}', action='invite', member='<member_id>')"
    ),


    "heal_project_reinvite": (
        "error: the project iam was rejected (401) — its session may have been rotated or revoked.\n"
        "  a browser re-login will not fix this (the project iam outranks the account).\n"
        "  ask the box owner for a reissue invite: "
        "openbox(name='<box>', action='invite', member='<nickname>')\n"
        "  then, in this project, use the code: openbox(action='join', code='<invite-code>')"
    ),


    "heal_env_rejected": (
        "error: LINKLORE_TOKEN was rejected (401) — the injected token looks expired/revoked.\n"
        "  replace the token in your MCP config (env LINKLORE_TOKEN) and retry."
    ),

    "heal_login_required": (
        "error: login required — retry after uvx llre login."
    ),
}
