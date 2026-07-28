"""English (en) messages for the 'router_edit' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "edit(id, action=, ...) — 4 write modes (action). If action is omitted, defaults to append (msg alone works too).\n\n"
        "Write modes (action, tool option = behavior match):\n"
        "- **append (default, non-destructive)** → edit(id, action='append', msg='new content')   # or omit action, msg alone — appends to the end of body, keeps the rest\n"
        "- **section (partial edit)**   → edit(id, action='section', section='heading', msg='new section content')  # replaces just that section (existing heading only — errors if missing; to add a new section use append), keeps the rest\n"
        "- **overwrite (full replace)** → edit(id, action='overwrite', msg='new body' [, tags=[...], ...])  # old body kept in history(recoverable via log). tags/items(doc only)/links are also fully replaced in the same call\n"
        "- **supersede (follow-up publish)** → edit(id, action='supersede', msg='new conclusion')  # creates a new id, old one head=False\n\n"
        "(action= is one of append|section|overwrite|supersede|remove. Unspecified('') means append.)\n\n"
        "Other:\n"
        "- remove a checklist item(doc only) → edit(id, action='remove', items=[N])  # 1-based, multiple: items=[N,M]\n"
        "- mark as dropped      → edit(id, status='dropped')  (still shown in search)\n"
        "- supersede chain (keep old + new head) → edit(id, action='supersede', ...)  (or add(type='lore'|'doc', relates=old_id, ...))\n"
        "- supersede by an existing item (reconcile a contradiction)  → link(a=X, b='lr-Y'|'dc-Y', action='supersede')  (X→head=False)\n"
        "- permanent delete      → rm(id)\n"
    ),

    "help": (
        "edit — modify an entity (ID prefix auto-detected)\n\n"
        "## Argument shapes (important)\n"
        "  id — using the full ID is recommended (e.g. lr-1a2b3c4d). show() allows partial match, edit needs the full ID.\n"
        "  tags/files/links — list recommended, comma-separated str is for natural CLI input (`llre edit tags=a,b`) (e.g. ['a','b'] or 'a,b')\n"
        "  items — checklist operations(list·items=N(int) toggle) are doc-only · batch(JSON array) works for both lore·doc (see below)\n\n"
        "## Body edits (action) — append(default) / section / overwrite / supersede, 4 modes\n"
        "  action='append', msg='added content'         → appends to the end of body (default, non-destructive). omitting action with just msg does the same\n"
        "  action='section', section='## Heading', msg='new section content'  → replaces just that section (including sub-sections), keeps the rest of the body\n"
        "    ↳ msg may or may not include the heading — if it starts with the heading it's kept as-is (no duplication, renaming allowed), otherwise the original heading is kept\n"
        "    ↳ section= requires msg · cannot combine with action='overwrite'/items (standalone mode) · batch not supported\n"
        "    ↳ heading matching allows partial match; if ambiguous, returns candidates·if not found, returns the list of available sections as-is\n"
        "    ↳ links= in the same call also gets connected (id doesn't change, so it happens right there)\n"
        "  action='overwrite', msg='new body'        → full body replace(edit). old body→log(id) to recover\n"
        "    ↳ tags=/items=(doc)/files(file paths in links=) in the same call are also fully replaced · id links in links=\n"
        "      (lr-y/dc-y etc.) are always additive — overwrite has no effect on them (link() is idempotent, so no\n"
        "      risk of losing an existing connection, 2026-07-09 doc-doc deletion live-bug fix)\n"
        "  action='supersede', msg='new conclusion'        → creates a new id(inherits title/tags/status from the old one)·old one head=False\n"
        "    ↳ cannot combine with section= · title/tags/status default to inheriting from the old item if unspecified\n"
        "    ↳ links=(both id·file path) in the same call also get connected to the new id(no 2-pass needed)\n\n"
        "## Edit decision tree\n"
        "  append (non-destructive, default)       → edit(id, msg='...')  or edit(id, action='append', msg='...')\n"
        "  partial edit (replace an existing section only)   → edit(id, action='section', section='heading', msg='...')\n"
        "  replace (edit)               → edit(id, action='overwrite', msg='...')\n"
        "  follow-up publish (=supersede, creates a new id) → edit(id=old_id, action='supersede', msg='new conclusion')\n"
        "    (or add(type='lore'|'doc', relates=old_id, ...) — same path)\n"
        "  drop (no replacement, stays in search) → edit(id, status='dropped')\n"
        "  drop+replace (=supersede by an existing item, excluded from search) → link(a=X, b='lr-Y'|'dc-Y', action='supersede')\n"
        "    if there's a replacement it auto head=False's (excluded from search/brief). one call for reconciling a contradiction·swapping versions.\n"
        "    (a=the old item being dropped, b=the surviving existing item — b is never newly created)\n"
        "  permanent delete (no history)     → rm(id)\n\n"
        "## Single-item edits\n"
        "  lr-* → lore: title/msg/status/tags/links\n"
        "  dc-* → doc: title/msg/items/tags/links(+flow)/status  (flow is doc-only, lore has none)\n"
        "  links= unified — edit(id, links=['src/x.py','lr-y','title']) auto-classifies file·id·title\n"
        "  links=['dc-y'], flow=True → doc journey chain (doc only)\n"
        "  to unlink (1 file·1 id) use unlink(a, target) — links='-' bulk-unlink has been removed\n"
        "    (it's the same operation as repeating unlink(), no evidence of real demand)\n"
        "## status (lore/doc common) — a lifecycle tag (keeps showing up in search)\n"
        "  open | done | dropped | rule(unchanging standard) (or 'clear' = back to open). any other value is rejected.\n"
        "  ★ distinguishing cleanup shapes (easy to mix up):\n"
        "     done                     = finished valid knowledge      → shows in search (marked complete)\n"
        "     dropped (no replacement)      = discarded+reason kept      → shows in search (marked dropped)\n"
        "     dropped + link(action='supersede') = discarded+has a replacement(=supersede) → hidden from search (auto head=False)\n"
        "     rm                       = permanent delete(no history)   → trash/permanent\n"
        "  ↑ supersede isn't a separate concept — it's 'dropped with a replacement link'. the link's presence decides search visibility.\n"
        "## Collection fields (items(doc only)/tags/links) — same rules as msg\n"
        "    default = append(non-destructive, keeps existing) | action='overwrite' = full replace\n"
        "    tags/items support '-' = clear · links has no '-', unlink individually via unlink(a, target)\n"
        "    remove items(destructive, doc only): requires action='remove' — edit(id, action='remove', items=[N])  # 1-based, multiple: items=[N,M]\n"
        "    add items: use a list — edit(id, items=['new item'])  ('+text' string prefix has been retired)\n"
        "    items = a progress-tracking checklist (single concept) — dict items without a done key are legacy, read-only (avoid creating new ones this way)\n"
        "## Passing an int/int list to items= — toggles a single item (doesn't use the action=/overwrite switch)\n"
        "    edit(id='dc-x', items=3)        → toggles item 3's checkbox (1-based)\n"
        "    edit(id='dc-x', items=[2,3])    → toggles items 2·3 together (str/dict form still adds/replaces as before)\n"
        "    ⚠️ items='-N'/'✓N'/'vN'/'+text' string-prefix syntax has been retired — "
        "remove via action='remove', items=[N] · toggle via items=[N](int) · add via items=['text']\n\n"
        "## Batch edits\n"
        "  edit(items='[{{\"id\":\"lr-...\",\"status\":\"done\"}},...]')\n"
        "  items as a JSON array + type auto-detected from the first item's ID (dc-* → doc batch, lr-* → lore batch)\n"
        "  per-item overwrite supported — full replace(edit), old body→log(id) to recover"
    ),

    "err_no_id_or_items": "error: specify id or items(a JSON array).",
    "err_action_invalid": "error: action='{action}' is not supported — use one of append|section|overwrite|supersede|remove",
    "err_section_required": "error: action='section' requires section=(heading)",


    "err_remove_items_required": (
        "error: action='remove' requires items(1-based numbers to remove) — "
        "edit(id='{id}', action='remove', items=[N])"
    ),


    "err_remove_section_conflict": "error: action='remove' cannot combine with section=",
    "err_supersede_section_conflict": "error: action='supersede' cannot combine with section=",
    "err_not_edit_target": "error: '{id}' is not a valid edit target. only lore(lr-*), doc(dc-*) can be edited.",
    "err_no_linklore": "error: no .linklore",
    "err_mode_conflict_items": "error: mode conflict — section is standalone-only",
    "err_section_msg_required": "error: section= requires msg=(the section's new content)",
    "err_links_dash_removed": (
        "error: links='-' has been removed — use unlink(a, target) to unlink individually.\n"
        "  (bulk unlink = same operation as repeating unlink(), no evidence of real demand)"
    ),
    "err_lore_doc_only_args": (
        "lore has no {joined} — {joined} is doc-only. "
        "add to lore body with edit(id='{id}', msg='...')"
    ),
    "err_empty_list_tags": (
        "an empty list is ambiguous — clear all: edit(id='{id}', tags='-') · "
        "replace: edit(id='{id}', tags=[...], action='overwrite') · "
        "add: edit(id='{id}', tags=[...])"
    ),
    "err_empty_list_links": (
        "an empty list is ambiguous — unlink individually: unlink(a='{id}', b=target) · "
        "replace: edit(id='{id}', links=[...], action='overwrite') · "
        "add: edit(id='{id}', links=[...])"
    ),

    "lore_no_change_with_preview": (
        "{preview}\n\nspecify a change:\nedit(id='{id}', msg='+more')  # append\n"
        "edit(id='{id}', status='done')  # or 'dropped'"
    ),
    "lore_no_change_no_preview": "specify a change:\nedit(id='{id}', msg='+more')",
    "doc_no_change_preview": (
        "{preview}\n\nexample edits:\nedit(id='{id}', items=[1,3])  # toggle\nedit(id='{id}', status='done')"
    ),
    "lore_links_only": "[{id}]",
    "doc_links_only": "[{id}]",

    "auto_files_note": (
        "\n📎 auto-linked files (uncommitted diff, based on what was just added): {files}"
        "\n   to unlink an unrelated file: unlink(a='{id}', b='filename')"
    ),

    "link_ok": "  ↔ {target}",
    "link_fail": "  ⚠️ link({target}) failed: {err}",
    "link_summary_header": "\n🔗 linked (links=):\n",


    "flow_link_ok": "  → {target} (flow-linked)",
    "flow_link_summary_header": "\n→ flow-linked (flow_links=):\n",

    "err_item_not_found": "error: '{item_id}' not found.",
    "err_wrap": "error: {err}",
    "err_section_match_fail": "section match failed",
    "section_replaced": (
        "✂ replaced section '{heading}' — section {old_len} chars→{new_len} chars "
        "(body total {body_len} chars) · old body: log(id='{item_id}') to recover"
    ),

    "err_batch_invalid_json": "error: items is not a valid JSON array.",
    "err_batch_empty": "error: items is empty or not an array.",
    "batch_section_unsupported": "{eid}: section= is not supported in batch — use single edit(id=, section=, msg=)",
    "batch_all_section_errors": "0/{total} ({errcount} errors)\n",
    "batch_unknown_id_prefix": "error: unknown ID prefix — '{id}'. batch edit routes lore/doc by the first entry's id (lr-*/dc-*).",
    "batch_mixed_kind": (
        "error: batch mixes lore(lr-) and doc(dc-) ids — the batch is routed by the first entry's "
        "kind ({first_kind}), so other-kind ids would misleadingly surface as 'not found' (even if "
        "they exist). Split the call by type: edit(items=[lore-only]) / edit(items=[doc-only])."
    ),
    "batch_section_excluded_suffix": "\n(section= {errcount} excluded)\n",

    "preview_header": "[{id}] {title}",
    "preview_body_line": "  {line}",
    "preview_meta_tags": "tags={tags}",
    "preview_meta_line": "  ({meta})",

    "err_name_not_found": "error: '{name}' not found. use an ID(lr-*/dc-*).",
}
