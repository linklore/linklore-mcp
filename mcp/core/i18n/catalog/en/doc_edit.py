"""English (en) messages for the 'doc_edit' surface."""
MESSAGES: dict[str, str] = {

    "err_status": "error: {err}",
    "err_generic": "error: {e}",
    "err_link_resolve": "error: failed to resolve links\n{e}",
    "err_flow_link_resolve": "error: failed to resolve flow links\n{e}",
    "err_not_found_doc": "error: doc '{id}' not found.",


    "rule_tag_removed": (
        "ℹ️ the #rule tag is retired — use status='rule' to mark a rule. "
        "removed it from the tags."
    ),


    "items_schema_error_skip": (
        "\n⚠️ items skipped due to a schema error (the doc was saved anyway) — "
        "fix: edit(id='{id}', items=[...])\n{err}"
    ),


    "status_invalid_default": (
        "⚠️ status '{input}' is invalid — saved as open. "
        "fix: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "status_invalid_skip": (
        "status '{input}' is invalid — skipped, kept the existing value ('{current}'). "
        "retry: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "err_title_required": "error: title is required — add(type='doc', title='...')",
    "auto_tags_notice": (
        "  tags auto-assigned: #{tags} — "
        "edit: edit(id='{id}', tags=[...], action='overwrite') · clear: tags='-'"
    ),
    "linked_confirm": "🔗 linked (links=): {ids}",
    "flow_linked_confirm": "→ flow-linked (flow_links=): {ids}",
    "link_unresolved_header": (
        "\n⚠️ some links could not be resolved (doc saved anyway) — "
        "verify the ID then reconnect via link():\n"
    ),
    "suggestion_header": "related candidates (suggested · not linked — use links=/link() to connect):",


    "dup_header": "🚨 very similar doc found (possible duplicate):",
    "dup_line": "  - {title} [{id}]{author}{badge} (cos={cos})",
    "dup_preview": "    ↳ {preview}",
    "dup_judge_header": "   judge (from the preview above, no need to open it — same decision?):",
    "dup_action_supersede": "   • the new one is better → link(a='{top_id}', b='{new_id}', action='supersede')",
    "dup_action_keep": "   • keep the existing one  → rm(id='{new_id}', force=True)",
    "dup_action_unrelated": "   • unrelated (not related) → link(a='{new_id}', b='{top_id}', action='unrelated')",
    "dup_action_distinct": "   • not a duplicate (confirmed separate) → link(a='{new_id}', b='{top_id}', action='distinct')",
    "dup_judge_fallback": "   → after checking the body: link(action='supersede') or rm(force=True) or keep both",


    "conflict_header": "⚠️ conflict candidates (same subject — check if the conclusion is opposite):",
    "conflict_line": "  - {title} [{id}]{badge} (evidence: {evidence})",
    "conflict_hint": "   judge: opposite decision → confirm current then link(action='supersede') · complementary → connect via links=/link() · unrelated → link(a='{new_id}', b='{top_id}', action='unrelated')",


    "err_no_title_or_msg": "error: specify title or msg.",
    "supersede_result": (
        "[{new_id}] {title}\n"
        "  ↳ supersede: {old_id} → {new_id} "
        "(new doc created, old doc preserved with head=False)\n"
        "  ⚠️ not an append — the old body no longer shows up in default search/brief results. "
        "to append to the same ID's body instead, use edit(msg=...)."
    ),


    "collection_cleared": "{label} cleared — removed {n} existing",
    "collection_replaced": "{label} replaced — {old_n} → {new_n}",
    "collection_added": "{label} +{n} (total {total})",


    "toggle_parse_failed": "⚠️ toggle parse failed — not executed.",
    "bad_tokens": "  unrecognized tokens: {tokens}",
    "out_of_range": "  out-of-range numbers: {nums}",
    "no_items_hint": "  this doc has no items — add one first: edit(id='{id}', items=['new item'])",
    "current_items_header": "current items:",
    "current_items_more": "  … +{n} more — full list: show(query='{id}')",
    "retry_hint": "retry: edit(id='{id}', items=1)  # ← with a valid number",


    "err_remove_msg_conflict": (
        "error: action='remove' cannot combine with msg= — remove is a standalone call: "
        "edit(id='{id}', action='remove', items=[N])"
    ),
    "err_remove_items_required": (
        "error: action='remove' requires items(1-based numbers to remove) — "
        "edit(id='{id}', action='remove', items=[N])"
    ),
    "err_remove_items_type": (
        "error: action='remove' items must be an int or a list of positive ints — "
        "edit(id='{id}', action='remove', items=[N])"
    ),


    "err_remove_syntax_retired": (
        "error: the old items string('-N')/negative-int remove syntax has been retired — "
        "edit(id='{id}', action='remove', items=[N])"
    ),
    "err_toggle_syntax_retired": (
        "error: the items='✓N'/'vN' string toggle syntax has been retired — "
        "edit(id='{id}', items=[N])  # int or a list of ints"
    ),
    "err_add_syntax_retired": (
        "error: the items='+text' string add syntax has been retired — "
        "edit(id='{id}', items=['text'])"
    ),


    "err_create_operator_tokens": (
        "operators aren't valid at creation — plain text only: {tokens} "
        "(to use it literally, use a dict: items=[{{'text': '...'}}])"
    ),


    "list_operator_header": "⚠️ items list not processed — it contains retired operator-shaped elements.",
    "list_operator_tokens": "  offending tokens: {tokens}",
    "list_operator_hint": (
        "remove: edit(id='{id}', action='remove', items=[N]) · "
        "toggle: edit(id='{id}', items=[N]) · "
        "to add it literally, use a dict: items=[{{'text': '...'}}]"
    ),


    "batch_remove_msg_conflict": "{wid}: action='remove' cannot combine with msg — remove is standalone",
    "batch_remove_items_required": "{wid}: action='remove' requires items(numbers to remove)",
    "batch_remove_items_type": "{wid}: action='remove' items must be an int or a list of positive ints",
    "batch_remove_syntax_retired": "{wid}: old items string/negative-int remove syntax retired — use action:'remove', items:[N]",
    "batch_toggle_syntax_retired": "{wid}: old items='✓N'/'vN' string toggle syntax retired — use items:[N](int)",
    "batch_add_syntax_retired": "{wid}: old items='+text' string add syntax retired — use items:['text']",
    "batch_list_operator_tokens": (
        "{wid}: items list has retired operator-shaped elements — {tokens} "
        "(wrap in a dict to add literally: {{'text': '...'}})"
    ),


    "batch_action_unsupported": "{wid}: action='{action}' is not supported in batch — only overwrite/remove (append is the default)",


    "toggle_success_header": "[{id}] {title}  ({done} of {total} done)",
    "toggle_collapsed_note": "\n  ({total} total — show(query='{id}') for detail)",


    "removed_echo": "\n  🗑️ Removed: {texts}",
    "removed_echo_more": " and {n} more",


    "status_changed_echo": "\n  status: {old} → {new}",


    "err_id_required": "error: id is required — edit(id='dc-xxx', ...)",
    "err_no_changes": "error: nothing to change.",
    "err_not_found_edit": "error: doc '{id}' not found.",
    "replace_echo": (
        "\n  body fully replaced — old {old_len} chars → new {new_len} chars "
        "(old body preserved in doc_history, recover: log(id='{id}'))\n  ↳ {echo}"
    ),
    "append_echo": "\n  body(append) — appended +{appended_len} chars after existing {old_len} chars\n  ↳ {echo}",
    "auto_checked_echo": "\n  {n} item(s) auto-checked (status=done)",


    "stale_append_notice": (
        "the body is now {length} chars and it's been {days} day(s) since the last edit — "
        "check for stale content or consider splitting it up."
    ),


    "edit_batch_help": (
        "doc_edit_batch — edit multiple docs at once\n\n"
        "  edits: JSON array or list [{{id, action, items, title, tags, links, flow, status}}, ...]\n"
        '  links: unified (files·dc/lr id·title auto-classified) · flow:true → doc journey chain · links:"-" → clear all links\n\n'
        "items syntax (same as doc_edit, v4):\n"
        '  ["a", "b", "c"]           → append (default, non-destructive)\n'
        '  ["a","b"] + "overwrite":true → full replace\n'
        '  [1, 3]                   → toggle (int list, 1-based)\n'
        '  "action":"remove", "items":[3,1]  → remove (1-based, destructive — action required)\n'
        "  ⚠️ items='-N'/'✓N'/'+text' string-prefix syntax has been retired\n\n"
        "example:\n"
        '  doc_edit_batch(edits=\'[{{"id":"dc-xxx","items":[1,3]}}, '
        '{{"id":"dc-yyy","action":"remove","items":[2]}}]\')\n'
    ),
    "err_edits_required": "error: edits is required — JSON array or list",
    "err_edits_invalid_json": "error: edits is not a valid JSON array.",
    "err_edits_not_list": "error: edits must be a JSON array.",
    "batch_bad_tokens": "unrecognized tokens: {tokens}",
    "batch_out_of_range": "out of range: {nums} (items 1..{n})",
    "batch_no_items": "this doc has no items",
    "batch_toggle_error": "{wid}: toggle number error — {detail}",
    "result_count": "{success}/{total}",
    "err_count_suffix": " ({n} error(s))",


    "add_batch_help": (
        "doc_add_batch — create multiple docs at once\n\n"
        "  docs: list[dict] recommended — [{{title, items, tags, links, flow}}, ...]\n"
        "  a JSON string is also backwards compatible\n\n"
        "each entry's items/tags/links can be a list or a comma-separated string\n"
        "links: unified (files·dc/lr id·title auto-classified) · flow:true → doc journey chain\n\n"
        "example:\n"
        '  doc_add_batch(docs=[{{"title":"Auth","items":["OAuth","JWT"]}}])\n'
    ),
    "title_missing": "title missing",
    "err_docs_required": "error: docs is required — list[dict] or JSON array",
    "err_docs_invalid": "error: docs is not valid JSON/list.",
    "err_docs_not_list": "error: docs must be a list.",
    "result_created": "{success}/{total} created",
    "errors_section_header": "\nerrors:\n",
}
