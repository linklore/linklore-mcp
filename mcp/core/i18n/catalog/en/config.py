"""English (en) messages for the 'config' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "Project settings (openbox source options) + iam + session pin.\n"
        "\n"
        "WARNING: handle/name/email apply machine-wide, not per-project.\n"
        "\n"
        "Sharing lives in a separate tool: openbox (openbox sharing/members).\n"
        "\n"
        "11 actions:\n"
        "- action='whoami' → your identity (handle/name/email)\n"
        "- action='version' → server code version (git commit)\n"
        "- action='sources' → list registered external sources (openboxes)\n"
        "- action='option' → change an external source's settings (auto_search=/show_prefix=)\n"
        "- action='sync' → force-refresh an external source's cache\n"
        "- action='forget' → deregister an external source\n"
        "- action='pin' → pin this session to a specific project\n"
        "- action='unpin' → unpin the session\n"
        "- action='sessions' → list/revoke your account sessions (revoke=)\n"
        "- action='projects' → list every LinkLore project on this machine\n"
        "- action='delete_project' → permanently delete your personal-server copy of this project (2-step confirm)\n"
        "\n"
        "help=true for details."
    ),

    "help": (
        "config - project settings + external openbox source options + user info\n"
        "\n"
        "Trail model (git concept): home base=local (private), my server=push/pull (mine only), openbox=the openbox() tool (shared, invite-only).\n"
        "push/pull (home base <-> my server) - openbox (openbox sharing/members) are separate tools.\n"
        "\n"
        "## user (global - applies machine-wide, not per-project)\n"
        "  config(action='whoami')                  current iam + this project's iam (read-only)\n"
        "  config(handle='alice')                    change handle (call without action)\n"
        "  config(name='Alice', email='d@e.com')     change name/email\n"
        "  config(name='-')                          clear name - email='-'/handle='-' work the same way\n"
        "\n"
        "## account sessions\n"
        "  config(action='sessions')                list my account's active sessions\n"
        "  config(action='sessions', revoke='<id>') revoke a single session\n"
        "  config(action='sessions', revoke='all')  revoke all but the current session (cleans up ghost sessions)\n"
        "\n"
        "## external openbox source options\n"
        "  config(action='sources')         list registered openboxes\n"
        "  config(action='option', name='team-prj', auto_search=false)  include in search or not\n"
        "  config(action='sync')            summarize openbox changes\n"
        "  config(action='forget', name='team-prj')  fully unregister a source (both registry+openbox)\n"
        "  WARNING: joining/docking an openbox is openbox(action='join'/'docking').\n"
        "\n"
        "## my server (push/pull) / openbox sharing/docking (separate tools)\n"
        "  push(id='lr-xxx')                home base -> my server (mine only)\n"
        "  openbox(name='team-prj', action='docking', url='https://.../api/projects/<pid>')  dock an existing membership\n"
        "  openbox(name='team-prj', action='push', id='lr-xxx')   home base -> openbox share\n"
        "  openbox(name='team-prj', action='show')   browse an openbox (auto-refreshes the cache)\n"
        "  openbox(name='team-prj', action='pull', id='lr-xxx')   item -> absorb into home base\n"
        "\n"
        "## session pin\n"
        "  project_dir was removed from the MCP surface (except init) - use pin when moving between projects.\n"
        "  config(action='pin', dir='/path')  pin this session's base project (an explicit project_dir always wins)\n"
        "  config(action='pin')               show the current pin\n"
        "  config(action='unpin')             clear the pin - restores cwd/CLAUDE_PROJECT_DIR\n"
        "  WARNING: process memory only - not persisted, cleared automatically when the session (server process) ends.\n"
        "\n"
        "## general\n"
        "  config()                   current settings + external source summary\n"
        "  config(action='projects')  list of all LinkLore projects (alias: projects=true)\n"
        "  config(action='version')   check current mcp code version (git commit)\n"
        "  config(action='delete_project', project_id=, confirm='<code>')  permanently delete a personal space (my server) - the first call returns a one-time confirm code - without project_id, targets the pinned/current project - use openbox(name=, action='delete') for openboxes"
    ),

    "err_invalid_action": "error: unknown action '{action}'. valid: {valid} (or leave empty to show current settings). help=True.",

    "version_line": "mcp version: {commit} ({branch}){dirty}",
    "version_dirty_flag": " *(dirty)",

    "unpin_done": "pin cleared - restoring cwd/CLAUDE_PROJECT_DIR as the basis going forward.",
    "pin_none": "no pin set - config(action='pin', dir='/path')",
    "pin_no_store_suffix": " (no .linklore yet - run init() before writing)",
    "pin_store_parent_suffix": " (using the shared store from the parent '{parent}' - call init() for independent storage)",
    "pin_status": "pin: {name} ({path}){store_note}",
    "err_dir_not_found": "error: directory not found - {dir}",
    "store_has": "store exists",
    "store_parent": "using the shared store from the parent '{parent}' - call init() for independent storage",
    "store_none": "no store yet - run init() before writing",
    "pin_set": "pin: {name} ({path}) - {store_note}",

    "whoami_project_identity": "\nthis project: {display} (project iam)",
    "whoami_account_acting": "\nacting as account",
    "err_whoami_readonly": "error: whoami is read-only — to change iam, use config(handle=..., name=..., email=...)",

    "err_login_required": "error: login required - uvx llre login",
    "err_revoke_failed": "error: failed to revoke session ({code}) - {body}",
    "session_revoked": "session {id} revoked",
    "sessions_revoked_all": "{n} revoked - current session kept",
    "err_sessions_list_failed": "error: failed to list sessions ({code}) - {resp}",
    "no_active_sessions": "no active sessions",
    "sessions_header": "# active sessions ({count})",
    "session_current_marker": " (current)",
    "session_line": "- {id}{marker}  created {created}  last used {last_used}  expires {expires}",
    "sessions_footer": "revoke: config(action='sessions', revoke='<id>') (single, immediate) · revoke='all' (all but current, needs confirm)",
    "sessions_revoke_all_desc": "revoke all sessions (except current)",
    "sessions_revoke_all_confirm": (
        "⚠️ this will revoke every active session on my account except the current one — unrecoverable.\n"
        "  1. run it: config(confirm={slot})\n"
        "  2. cancel: do nothing (expires in 15 min)"
    ),

    "no_sources": "no external sources registered",
    "src_list_header": "# external sources ({count})",
    "err_source_not_registered": "error: source '{name}' not registered (check with config(action='sources'))",
    "no_sources_hint": "no external sources registered. connect an openbox with openbox(action='join'/'docking')",

    "sync_counts": "  lore {lore} (new {new_lore}) - doc {docs} (new {new_docs})",
    "sync_new_lore_header": "  new lore (top 3):",
    "sync_new_doc_header": "  new doc (top 3):",
    "no_changes": "no changes.",

    "err_name_required": "error: name is required",
    "option_updated": "[{name}] options updated - auto_search={auto_search}, show_prefix={show_prefix}",

    "forget_done": "[{name}] source unregistered - {where}",

    "settings_header": "# {name} settings",
    "default_sources_summary": "\nexternal sources ({count}): {names}",
    "default_sources_detail_hint": "  details: config(action='sources')",
    "default_projects_hint": "all projects: config(projects=true)",

    "no_projects": "no LinkLore projects found. run init to get started.",
    "projects_header": "# LinkLore projects ({count})",

    "delete_project_personal_label": "personal space",
    "err_delete_project_use_rm_openbox": "error: to delete an openbox, use openbox(name='{name}', action='delete') — config(action='delete_project') is personal-space only",
    "err_delete_project_no_target": "error: no target — pass project_id= directly, or pin this project first with config(action='pin') and retry (deletes the pinned/current project's personal space)",
    "err_delete_project_bad_ref": "error: project_id='{ref}' — pass prj-xxxxxxxx (shown by config(action='projects')) or a full UUID",
    "err_delete_project_ref_not_found": "error: no project matches '{ref}' — not in the address book or my memberships. check: config(action='projects')",
    "delete_project_ambiguous_header": "error: '{ref}' matches multiple projects — which one? (no auto-pick)",
    "delete_project_ambiguous_item": "  {n}. {label} ({prj}) → {cmd}",
    "candidates_more": "  … +{n} more",
    "delete_project_desc": "permanently delete personal space — {label} ({id})",
    "delete_project_confirm_needed": (
        "⚠️ this will permanently delete [{label}] ({id}) on the server — all lore/doc/members/invites gone, no recovery.\n"
        "  1. run it: config(confirm={slot})\n"
        "  2. cancel: do nothing (expires in 15 min)"
    ),
    "err_delete_project_failed": "error: delete failed ({code}) - {body}",
    "delete_project_done": "[{label}] ({id}) permanently deleted on the server.",
}
