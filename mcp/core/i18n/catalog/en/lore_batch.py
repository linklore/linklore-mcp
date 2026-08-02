"""English (en) messages for the 'lore_batch' surface."""
MESSAGES: dict[str, str] = {

    "err_no_edits": "error: edits is required — a JSON array or list",
    "err_edits_invalid_json": "error: batch is not a valid JSON array.",
    "err_edits_not_array": "error: batch must be a JSON array.",

    "link_post_failed": "  ⚠️ link({a}↔{b}) failed: {res}",

    "batch_summary": "{success}/{total}",

    "batch_edit_errors_suffix": " ({n} errors)\n{errors}",

    "link_post_header": "🔗 link post-processing:",

    "err_no_items": "error: items is required — list[dict] or a JSON array",
    "err_items_invalid_json": "error: items is not valid JSON/list.",
    "err_items_not_list": "error: items must be a list.",

    "err_entry_not_object": "Entry is not an object.",
    "err_title_missing": "title missing",

    "batch_add_errors_suffix": " ({n} errors: {errors})",


    "status_invalid_default": (
        "⚠️ status '{input}' is invalid — saved as open. "
        "fix: edit(id='{id}', status=open|done|dropped|rule)"
    ),


    "rule_tag_removed": (
        "ℹ️ the #rule tag is retired — use status='rule' to mark a rule. "
        "removed it from the tags."
    ),
}
