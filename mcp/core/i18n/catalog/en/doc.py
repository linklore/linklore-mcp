"""English (en) messages for the 'doc' surface."""
MESSAGES: dict[str, str] = {

    "show_help": (
        "doc lookup — unified into show(type='doc') (symmetric with lore=show)\n\n"
        "## lookup (show)\n"
        "  show(type='doc')                — full list\n"
        "  show(type='doc', query='auth')  — search\n"
        "  show(type='doc', tag='tech')    — filter by tag\n"
        "  show(type='doc', status='done') — filter by status\n"
        "  show(query='dc-xxx')            — detail view (id doesn't need type)\n\n"
        "## create/edit (add/edit)\n"
        "  add(type='doc', title='Auth', items=['OAuth','JWT'])\n"
        "  add(type='doc', relates='dc-old', title='New version', msg='...')  → supersede (old head=False)\n"
        "  edit(id='dc-xxx', items=['new item'])\n"
        "  edit(id='dc-xxx', items=[1,3])  → toggle done (1-based)\n"
        "  edit(id='dc-xxx', action='remove', items=[2])  → remove an item (destructive, 1-based)\n"
        "  edit(id='dc-xxx', status='done')\n"
        "  link(a=X, b='dc-Y', action='supersede')  → merge into existing dc-Y (reconcile)\n\n"
        "  status: open(default, live) | done(completed) | dropped(retired) | rule(fixed baseline)\n"
        "  show(type='doc', superseded=True) → also include superseded old versions\n"
        "  show(type='doc', source_id='ext-id') → look up by ingested-source original id (openbox('pull') and local copy/move)"
    ),
    "err_no_project": (
        "no docs — this project has no memory yet.\n"
        "add(type='doc', ...) to create the first doc and start the trail."
    ),
    "err_not_found": "error: doc '{query}' not found.",

    "err_not_dc_lr_id": "'{raw}' is not a dc-/lr- id (title→id conversion is classify_links' job upstream)",

    "err_items_schema_item": "  item {i}: keys {keys} — no 'text' or 'key'",
    "err_items_schema_header": "items dict entries need an anchor key ('text' or 'key'):\n",
    "err_items_schema_footer": (
        "\n\nvalid examples:\n"
        "  checklist: {{\"text\": \"a task\"}}\n"
        "  catalog: {{\"key\": \"name\", \"value\": \"value\"}}"
    ),
    "err_no_match": "no doc matches '{label}'",
    "err_sort_invalid": "error: sort='{sort}' is not supported — use one of {valid}",
    "err_empty": "no docs — add(type='doc', title='...') to create one",


    "limit_suffix": "\n  … {shown} of {total} shown — more: max={total}",
    "matched_header": "{n} match(es):",

    "files_label": "files: {files}",
    "related_label": "related: {target}",
    "flow_label": "flow: {target}",
    "link_more": "  … +{n} more",
    "backref_label": "referenced by: {refs}",
    "backref_more": " and {n} more",

    "items_count_suffix": " {n} item(s)",

    "oneline_header": "doc ({m}/{t})",

    "uncategorized": "Uncategorized",
    "grouped_header": "# doc ({n})",
    "grouped_done_footer": "done {done}/{n}",
}
