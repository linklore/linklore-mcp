"""English (en) messages for the 'local' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "Use this when you want to view, move, or copy lore/doc items that live in a "
        "different project or folder (workspace) — cross-project / workspace access.\n"
        "local_cross(action, id, to='workspace-path', from_dir='') — directly operate on another "
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
        "⚠️ move always previews first, regardless of item count (it deletes the source, so there's "
        "no low-risk single-item case) — confirm and run it via the forced(...) call the preview "
        "prints, no stored slot. copy is reversible (source kept), so a single item still runs "
        "immediately; only 2+ items preview first, confirmed the same way.\n"
        "cf. sharing across a server/team goes through openbox(), not local_cross() — this tool never talks to a "
        "backend, it only works within your own disk.\n"
        "⚠️ only between projects you own — if the target is genuinely someone else's/another "
        "team's, don't use local_cross() just because you have filesystem access; go through openbox('push') "
        "(the recipient must openbox('pull') — a review gate).\n"
    ),

    "help": (
        "local_cross — directly operate on another LinkLore project on the same disk (move/copy/show)\n\n"
        "  local_cross(action='move', id='lr-x'|'dc-x', to='/path')         move -> preview + a "
        "forced(...) call, paste it back to confirm\n"
        "  local_cross(action='move', id=[...], to='/path')                 move multiple -> same "
        "preview + forced(...) call as a single item\n"
        "  local_cross(action='copy', id='lr-x', to='/path')                copy (source kept, new id, single runs immediately)\n"
        "  local_cross(action='show', from_dir='/other', query='...')       view a sibling workspace\n"
        "  local_cross(action='move'|'copy', ..., from_dir='/src')          set the source workspace "
        "explicitly — applies to move and copy (default: cwd)\n\n"
        "move: preserved fields = id, createdAt, files, tags, level, status, body, items. The "
        "source is soft-deleted (moved to trash, recoverable with restore(id)). Provenance is recorded "
        "(source_location='local', source project, original id).\n"
        "copy: same verdict as move, only the source deletion is skipped. A new id is issued and "
        "the same provenance is recorded. Re-copying the same original is an idempotent skip "
        "(matched by source_id) — no id-collision rejection.\n"
        "move deletes the source, so it's irreversible — it always previews first, regardless of "
        "item count. Execute it by calling the exact forced(action='local_cross', mode='move'|'copy', "
        "id=[...], to=..., from_dir=...) the preview prints (no stored slot, v4 gate). copy is "
        "reversible (source kept), so it's unchanged: a single item runs immediately, only 2+ items "
        "get the same preview + forced() confirmation.\n"
        "show: from_dir is required. query/tag/type/status are passed straight through to the "
        "target workspace — same search logic as show().\n"
        "cross-workspace links (works/supersede/docLink) are not followed by move or copy — "
        "breakage is shown.\n"
        "If the target workspace does not exist (move/copy), the call is rejected — run "
        "init(project_dir=...) first (only init creates stores, no auto-create).\n"
        "Boundary: sharing across a server/team is the openbox (the openbox() tool) — local_cross() only works "
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
    "forced_hint": (
        "To confirm, call exactly:\n"
        "  forced(action='local_cross', mode='{mode}', id={ids}, to='{to}', from_dir='{from_dir}')"
    ),

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
    "note_trash_ghost": "  ℹ️ target already has a trashed copy of this id — it will be purged automatically before the move",
    "moved_lore": '[{id}] "{title}" moved — id/createdAt/files preserved, provenance recorded{warn}',
    "moved_doc": '[{id}] "{title}" moved — id/createdAt/items preserved, provenance recorded{warn}',
    "copied_lore": '[{new_id}] "{title}" copied — new id (source {id}, createdAt/files preserved), provenance recorded{warn}',
    "copied_doc": '[{new_id}] "{title}" copied — new id (source {id}, createdAt/items preserved), provenance recorded{warn}',
    "preview_lore": '[{id}] "{title}" → will be moved (createdAt/files preserved){warn}',
    "preview_doc": '[{id}] "{title}" → will be moved (createdAt/items preserved){warn}',
    "preview_copy_lore": '[{id}] "{title}" → will be copied (source kept, new id + provenance){warn}',
    "preview_copy_doc": '[{id}] "{title}" → will be copied (source kept, new id + provenance){warn}',
}
