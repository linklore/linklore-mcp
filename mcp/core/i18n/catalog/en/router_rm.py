"""English (en) messages for the 'router_rm' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "rm — unified delete for my own project. Target is chosen by argument (action= is an explicit "
        "alternative, auto-detected by which argument is present when omitted). "
        "show/rm stay inside my own project — openbox (shared) cleanup lives in the openbox tool.\n\n"
        "## Deleting items (lore/doc) — id is a single value or a list (batch)\n"
        "- **trash (recoverable, default)**         → `rm(id)`  → restore(id) to recover\n"
        "- **permanent delete (unrecoverable)** → `rm(id, force=True)` prints the exact "
        "`forced(action='rm', id=...)` call to run — this call itself deletes nothing\n"
        "- **batch delete**                       → `rm(id=['lr-x','dc-y'], force=True)`\n"
        "- **mark as dropped (stays in search)**        → `edit(id, status='dropped')`\n"
        "- **supersede (keep old + new head)**  → `add(type='lore'|'doc', relates=old_id, ...)`\n\n"
        "## Taking down something you sent — my server only (reverse of push, doesn't touch the source of truth)\n"
        "- `rm(sent='lr-x'|'dc-x')`  take down from my server (or action='sent' explicitly)\n\n"
        "## Openbox things don't live here (moved behind the openbox gate)\n"
        "- remove a shared entry from the box: openbox(action='rm', id=...) · expel a member: openbox(action='rm', member=...) · "
        "delete an openbox: openbox(action='delete')\n"
    ),

    "restore_tool_desc": "restore(id) — recover trashed lore/doc. no id lists the trash.",

    "help": (
        "rm — unified delete for my own project (target by argument, action= is an explicit alternative)\n"
        "show/rm stay inside my own project — openbox (shared) cleanup lives in the openbox tool.\n\n"
        "## Items (lore/doc) — action='' (default)\n"
        "  trash (recoverable, default)        → rm(id)  → restore(id) to recover\n"
        "  permanent delete (unrecoverable) → rm(id, force=True) prints the forced(action='rm', id=...) "
        "call to run — nothing is deleted by this call itself\n"
        "  mark as dropped (stays in search)          → edit(id, status='dropped')\n\n"
        "## Taking down something you sent — my server only (doesn't touch the source of truth) — action='sent'\n"
        "  rm(sent='lr-x'|'dc-x')\n\n"
        "## Openbox things (not here — moved behind the openbox gate)\n"
        "  remove a shared entry from the box (sender only)   openbox(action='rm', id=...)\n"
        "  expel a member (owner)                 openbox(action='rm', member=...)\n"
        "  delete an entire openbox (owner)       openbox(action='delete')\n\n"
        "action='sent' is an explicit, more discoverable alternative to the existing auto-detection\n"
        "by presence of sent= — the value itself is still required, action= alone isn't enough.\n"
    ),

    "restore_help": (
        "restore — recover soft-deleted items from trash\n\n"
        "  restore()      → trash listing (lore + doc, most-recently-trashed first, default 10 — adjust with max=)\n"
        "  restore(id)    → recover that lore/doc (reappears in search/related suggestions)\n\n"
        "rm(id) = move to trash(default), rm(id, force=True) = permanent delete (needs confirm)."
    ),

    "err_action_invalid": "error: action='{action}' is not supported — only 'sent' (or omit it). openbox cleanup lives in the openbox tool",
    "err_sent_required": "error: action='sent' requires sent=(id)",

    "moved_rm_ids": (
        "moved: removing a shared entry from an openbox is the openbox tool now, not rm.\n"
        "  use: openbox(name='{name}', action='rm', id={ids})\n"
        "  (rm(sent=) only takes items down from my own server — show/rm stay inside my own project)"
    ),
    "moved_rm_member": (
        "moved: expelling an openbox member is the openbox tool now, not rm.\n"
        "  use: openbox(name='{name}', action='rm', member='{member}')\n"
        "  (show/rm stay inside my own project)"
    ),
    "moved_delete": (
        "moved: deleting an entire openbox is the openbox tool now, not rm. Nothing was executed.\n"
        "  use: openbox(name='{name}', action='delete')\n"
        "  (show/rm stay inside my own project)"
    ),
    "err_id_required": "error: specify id.",
    "err_not_rm_target": "error: '{id}' is not a valid rm target. only lore(lr-*), doc(dc-*) can be deleted.",

    "err_doc_not_found": "error: doc '{id}' not found.",
    "doc_permanent_deleted": "[{id}]{ts} permanently deleted (unrecoverable)",
    "doc_trashed": "[{id}]{ts} moved to trash — recover: restore('{id}'), permanent delete: rm('{id}', force=True)",

    "predecessor_revived": "predecessor [{id}] revived (successor deleted — now shown in search as dropped)",


    "force_delete_desc": "permanent delete — [{id}] {title}",


    "force_delete_confirm": (
        "⚠️ preparing to permanently delete [{id}] \"{title}\" — unrecoverable. "
        "1. run it: forced(action='rm', id='{id}') · "
        "2. move to trash instead: rm(id='{id}') (kept — restore() to recover)"
    ),


    "force_delete_batch_hint": "run them all at once: forced(action='rm', id={ids})",

    "restore_listing_empty": "trash is empty.",
    "restore_listing_header": "# Trash ({n}/{total}) — restore(id) to recover",
    "restore_listing_line": "- [{id}] {title}  ({when})",

    "restore_listing_truncated": "\n  … {shown} of {total} shown — more: max={total}",
    "restore_not_trash": "[{id}] already active (not in trash).",
    "restore_restored": "[{id}] recovered from trash",


    "restore_batch_summary": "{n} recovered: {ids}",

    "err_sent_no_server": (
        "error: no server of mine (never pushed).\n"
        "  push to a server first (a personal server is set up automatically)."
    ),


    "err_openbox_unregistered_list": "error: openbox '{space}' not registered — check with openbox(action='list')",
    "space_delete_desc": "delete openbox — {space}",
    "space_delete_confirm": (
        "⚠️ deleting openbox '{space}' — unrecoverable.\n"
        "  · all shared entries and member access in that shared space will be permanently deleted.\n"
        "  · everyone's local source of truth stays safe — only the shared copy disappears.\n"
        "  · run: forced(action='openbox', delete='{pid}')\n"
    ),
    "err_openbox_delete_no_auth": "error: openbox delete failed — no auth for '{space}'",
    "err_openbox_delete_failed": "error: openbox delete failed — {detail}",
    "space_deleted": "[{space}] openbox deleted — server-side content cascaded + local cleanup (unrecoverable)",

    "err_name_not_found": "error: '{name}' not found. use an ID.",
}
