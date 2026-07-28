"""English (en) messages for the 'local' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "local(action, id, to='workspace-path', from_dir='') — directly operate on another "
        "LinkLore project on the same disk (works on both lore and doc).\n"
        "\n"
        "action='move'   move to another workspace (source deleted, id preserved; createdAt/files/"
        "tags/level/status/body/items preserved; provenance recorded)\n"
        "action='copy'   copy to another workspace (source kept, a new id is issued + provenance "
        "recorded — re-copying the same original is an idempotent skip)\n"
        "action='show'   view another workspace's content (read-only — query/"
        "tag/type/status passed through)\n"
        "from_dir= applies to all three actions — for move/copy it sets the source workspace "
        "(default: cwd); for show it is the lookup target, hence required.\n"
        "⚠️ For 2+ items, the default is preview only — execute with the local(confirm=<number>) "
        "the preview gives you (a single item runs immediately).\n"
        "cf. sharing across a server/team is the openbox (the openbox() tool) — local() never talks to a "
        "backend, it only works within your own disk.\n"
        "⚠️ only between projects you own — if the target is genuinely someone else's/another "
        "team's, don't use local() just because you have filesystem access; go through openbox('push') "
        "(the recipient must openbox('pull') — a review gate).\n"
    ),

    "help": (
        "local — directly operate on another LinkLore project on the same disk (move/copy/show)\n\n"
        "  local(action='move', id='lr-x'|'dc-x', to='/path')         move (single, runs immediately)\n"
        "  local(action='move', id=[...], to='/path')                 move multiple -> preview + "
        "number, confirm with local(confirm=<number>)\n"
        "  local(action='copy', id='lr-x', to='/path')                copy (source kept, new id)\n"
        "  local(action='show', from_dir='/other', query='...')       view a sibling workspace\n"
        "  local(action='move'|'copy', ..., from_dir='/src')          set the source workspace "
        "explicitly — applies to move and copy (default: cwd)\n\n"
        "move: preserved fields = id, createdAt, files, tags, level, status, body, items. The "
        "source is soft-deleted (moved to trash, recoverable with restore(id)). Provenance is recorded "
        "(source_location='local', source project, original id).\n"
        "copy: same verdict as move, only the source deletion is skipped. A new id is issued and "
        "the same provenance is recorded. Re-copying the same original is an idempotent skip "
        "(matched by source_id) — no id-collision rejection.\n"
        "Multiple (len>1) always previews first and registers a plan — execute only via the "
        "local(confirm=<number>) the preview gives you. A single item is low-risk, so it runs immediately\n"
        "(forcing a preview for a single item is not supported — pass multiple items if you need a "
        "preview).\n"
        "show: from_dir is required. query/tag/type/status are passed straight through to the "
        "target workspace — same search logic as show().\n"
        "cross-workspace links (works/supersede/docLink) are not followed by move or copy — "
        "breakage is shown.\n"
        "If the target workspace does not exist (move/copy), the call is rejected — run "
        "init(project_dir=...) first (only init creates stores, no auto-create).\n"
        "Boundary: sharing across a server/team is the openbox (the openbox() tool) — local() only works "
        "within your own disk."
    ),

    "err_action_invalid": (
        "error: action='{action}' — one of three is required:\n"
        "  action='move'   move (source deleted)\n"
        "  action='copy'   copy (source kept)\n"
        "  action='show'   view a sibling workspace (read-only, from_dir required)"
    ),
    "err_no_to": "error: specify to= (the target workspace path).",


    "err_target_no_store": (
        "error: no store at the target '{to}' — it will not be auto-created. "
        "Run init(project_dir='{to}') in the target folder first, then retry."
    ),
    "note_target_absent": "ℹ️ no store at the target — run init(project_dir='{to}') first to execute.",
    "err_same_workspace": "error: the source and target are the same workspace.",
    "err_same_workspace_walkup": (
        "error: '{to}' has no store of its own and resolved up to the parent '{store}' — "
        "that's the same workspace as the source. To make it an independent project, run "
        "init(project_dir='{to}') first."
    ),
    "err_no_id": "error: specify id.",
    "err_show_no_from_dir": "error: action='show' requires from_dir= (the sibling workspace path to view).",

    "preview_header": "🔍 preview — not executed (source kept)\n",
    "transfer_desc": "{action} {n} items -> {to}",
    "preview_confirm": "\n\n  1. run it: local(confirm={slot})\n  2. cancel: do nothing (expires in 15 min)",

    "err_resolve": "[{id}] error: {rerr}",
    "err_kind": "[{id}] error: only lore(lr-*)/doc(dc-*) can be moved or copied",

    "reason_not_found": "not in source",
    "reason_dup": "already exists in target",
    "reason_self": "the original already lives in the target (same id) — nothing to bring in",
    "reason_already": "already ingested — {existing} in target (source_id idempotency)",
    "err_move_cancel": "[{id}] error: {reason} — move cancelled",
    "err_copy_cancel": "[{id}] error: {reason} — copy cancelled",
    "err_preview_skip": "[{id}] error: {reason} — skipped",

    "skip_self": "[{id}] skipped — the original already lives in the target (nothing to bring in)",
    "skip_already": "[{id}] skipped — already ingested ({existing} in target, source_id idempotency)",
    "warn_dropped": "  ⚠ links {dropped} broken (cross-ws)",
    "moved_lore": '[{id}] "{title}" moved — id/createdAt/files preserved, provenance recorded{warn}',
    "moved_doc": '[{id}] "{title}" moved — id/createdAt/items preserved, provenance recorded{warn}',
    "copied_lore": '[{new_id}] "{title}" copied — new id (source {id}, createdAt/files preserved), provenance recorded{warn}',
    "copied_doc": '[{new_id}] "{title}" copied — new id (source {id}, createdAt/items preserved), provenance recorded{warn}',
    "preview_lore": '[{id}] "{title}" → will be moved (createdAt/files preserved){warn}',
    "preview_doc": '[{id}] "{title}" → will be moved (createdAt/items preserved){warn}',
    "preview_copy_lore": '[{id}] "{title}" → will be copied (source kept, new id + provenance){warn}',
    "preview_copy_doc": '[{id}] "{title}" → will be copied (source kept, new id + provenance){warn}',
}
