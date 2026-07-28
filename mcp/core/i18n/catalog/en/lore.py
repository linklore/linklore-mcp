"""English (en) messages for the 'lore' surface."""
MESSAGES: dict[str, str] = {

    "doc_hint_header": "\nrelated doc candidates (suggested, not linked — use link() to connect):",


    "sem_label": " (semantically similar {cosine})",


    "weak_candidates": "  {n} weak candidate(s) — run cleanup() to review overlaps",


    "connected_line": "connected: {labels}",

    "auto_tags_notice": (
        "\n  tags auto-filled: #{tags} — "
        "edit: edit(id='{id}', tags=[...], action='overwrite') · clear: tags='-'"
    ),

    "err_status": "error: {err}",


    "rule_tag_removed": (
        "ℹ️ the #rule tag is retired — use status='rule' to mark a rule "
        "(strength is level's job). removed it from the tags."
    ),


    "status_invalid_default": (
        "⚠️ status '{input}' is invalid — saved as open. "
        "fix: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "status_invalid_skip": (
        "⚠️ status '{input}' is invalid — skipped, kept the existing value ('{current}'). "
        "retry: edit(id='{id}', status=open|done|dropped|rule)"
    ),

    "err_no_relates": "error: specify relates (the target lore ID).",

    "err_not_found": "error: lore '{id}' not found.",

    "no_changes": "No changes. Specify a field to modify.",

    "overwrite_desc": "full body replace — {id}",
    "overwrite_confirm": (
        "⚠️ [{id}] preparing to fully replace the body — {old_len} existing chars gone.\n"
        "  current first line: {first_line}\n"
        "  1. run it: edit(confirm={slot})\n"
        "  2. append instead (default, re-call without overwrite)"
    ),

    "modify_replace_echo": (
        "\n  body fully replaced — old {old_len} chars → new {new_len} chars "
        "(old body preserved in lore_history, restore: log(id='{id}'))\n  ↳ {echo}"
    ),

    "modify_append_echo": "\n  body(append) — +{appended_len} chars added after the existing {old_len} chars\n  ↳ {echo}",

    "tags_cleared": "tags cleared — removed {n} existing",
    "tags_replaced": "tags replaced — {old_n} → {new_n}",
    "tags_added": "tags +{n} (total {total})",

    "files_cleared": "files cleared — removed {n} existing",
    "files_replaced": "files replaced — {old_n} → {new_n}",
    "files_added": "files +{n} (total {total})",

    "err_no_title_or_msg": "error: specify title or msg.",

    "supersede_result": (
        "[{new_id}] {title}\n"
        "  ↳ supersede: {old_id} → {new_id} "
        "(new lore created, old lore preserved with head=False)\n"
        "  ⚠️ not an append — the old body won't show in brief/show by default. "
        "To append to the same ID's body, use edit(msg=...)."
    ),

    "no_lore": "No lore registered.",
    "no_filtered_lore": "No lore matches the filters ({filters}). {total} total.",

    "oneline_header": "lore ({matched}/{total})",
    "cluster_suffix": "+{n} cluster",
    "detail_header": "# lore ({matched}/{total})",
    "cluster_detail_suffix": "  +{n} cluster (show(query=) for all)",

    "delete_permanent": "[{id}]{title_str} permanently deleted (irreversible)",
    "delete_soft": (
        "[{id}]{title_str} moved to trash — "
        "restore: restore('{id}'), permanent delete: rm('{id}', force=True)"
    ),

    "predecessor_revived": "predecessor [{id}] revived (successor deleted — now shown in search as dropped)",

    "restore_already_active": "[{id}] already active (not in trash).",
    "restored": "[{id}] restored from trash",
}
