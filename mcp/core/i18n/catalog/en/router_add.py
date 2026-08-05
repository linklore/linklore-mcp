"""English (en) messages for the 'router_add' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "add(type='lore'|'doc', title, msg=) — lore=journal entry/decision, doc=spec/plan.\n"
        "2 linking args: links=unified (code files·dc/lr id·title auto-classified, flow=True for a doc chain) · push_to=send to a box (not a link).\n"
        "items=['a','b']→checklist(0/N, doc only) · items=[{{...}}]→batch creation(both lore·doc — use this for bulk, quieter nudges than N single calls, with status='rule' as the same reserved value in each dict; "
        "each dict may set its own 'type' to mix lore·doc in one call — omitted entries inherit the top-level type=). "
        "details help=True"
    ),

    "help": (
        "add — create an entity (routed by type)\n\n"
        "## Argument shapes\n"
        "  list recommended — tags=['a','b'], items=['todo1','todo2']\n"
        "  comma string — tags='a,b' (for natural CLI input, `llre add tags=a,b`)\n\n"
        "## Linking args — 2 kinds (links is unified, different purposes)\n"
        "  links=['src/x.py','lr-y','decision title']  unified linking — file path·id·title auto-classified\n"
        "                          (files=code link, dc/lr id·exact title=knowledge-graph auto-routing. no need for link())\n"
        "  links=['dc-a','dc-b'], flow=True       doc journey chain (doc only, order=list order)\n"
        "  push_to=['team-prj']    ★not a link★ — send it to that openbox right after creation (send)\n\n"
        "## items — a progress-tracking checklist (single concept). the input shape decides the result UI\n"
        "  items=['a','b','c']           → checklist (0/N, toggle with edit(id, items=N), doc only)\n"
        "  items=[{{'title':'...'}},...]   → catalog (dict cards) = batch creation (lore and doc both)\n"
        "  💡 creating several lore entries? use this batch form instead of N separate add() calls — "
        "quieter (one top-1 related-candidate line per item, vs the full nudge on every single add())\n"
        "  🔀 mixed batch: each dict may include its own 'type':'lore'|'doc' — entries without it "
        "inherit the top-level type= (default 'lore'). an unsupported type value errors out that "
        "entry only, the rest still get created.\n"
        "  ⚠️ dict items without a done key are legacy, read-only — avoid creating new ones this way "
        "(use list[str] or a dict that includes done)\n\n"
        "## Examples\n"
        "  add(type='lore', title='...', msg='...', tags=['lesson'], links=['src/a.py'])\n"
        "  add(type='doc',  title='...', items=['a','b','c'], links=['lr-x'])\n"
        "  add(type='doc',  title='...', links=['dc-a','dc-b'], flow=True)  # doc journey chain\n\n"
        "## type — only lore | doc (any other value is rejected)\n"
        "  lore: msg, tags, status, relates(supersede), items(dict list only=batch)\n"
        "  doc:  items, links(+flow), tags, status, relates(supersede)\n\n"
        "## supersede (keep the old + new head) — relates (lore/doc common)\n"
        "  add(type='lore', relates='lr-old', title='new decision', msg='...')\n"
        "  add(type='doc',  relates='dc-old', title='new version', msg='...')\n"
        "  → old item head=False(excluded from search), new item becomes head. tags/files inherited.\n"
        "  items=(doc)/links=(both id·file path)/flow= in the same call also apply to the new id directly (no 2-pass needed).\n"
        "  cf. to just fold a contradiction into an *existing* item Y = link(a=X, b='lr-Y'|'dc-Y', action='supersede')\n\n"
        "## status (lore/doc common) — lifecycle tag (keeps showing up in search)\n"
        "  open(default) alive · done finished · dropped discarded · rule unchanging standard(stays valid)\n"
        "  ⚠️ done/dropped/rule are 'tags' so they keep showing up in search. any other value isn't rejected — "
        "plain creation corrects it to open(+warning), supersede(relates=) inherits the old item's status(+warning).\n"
        "  cf. dropping while pointing at a 'replacement' auto-excludes from search (=supersede, not a separate concept):\n"
        "     link(a=X, b='lr-Y', action='supersede')  — the replacement link decides search visibility\n"
        "     done=finished valid knowledge(searchable) · dropped=discarded+reason(searchable) · dropped+replacement=old version(hidden)\n\n"
        "## Bulk creation (batch)\n"
        "  add(type='lore', items=[{{...}},{{...}}])  — batch if items is list[dict]\n"
        "  add(type='doc',  items=[{{...}},{{...}}])"
    ),

    "err_title_required": "error: title is required — add(type='...', title='...', ...)",
    "err_lore_items_forbidden": (
        "error: lore has no checklist — a checklist (items=['a','b']) is doc-only.\n"
        "  need a checklist? add(type='doc', title='...', items=['a','b'])\n"
        "  lore body goes in msg=: add(type='lore', title='...', msg='content')\n"
        "  batch creation (items=[{{'title':...}},...] dict) works for both lore·doc"
    ),
    "err_batch_title_conflict": (
        "error: items=[{{...}}] (batch creation) can't be combined with title=/msg= — the intents conflict.\n"
        "  · bulk batch creation: add(type='...', items=[{{'title':...}}, ...])  (drop title/msg)\n"
        "  · one item + checklist: add(type='...', title='...', msg='...', items=['a','b'])  (as a string list)"
    ),
    "err_batch_links_conflict": (
        "error: items=[{{...}}] (batch creation) can't be combined with top-level links=/push_to= — "
        "it's unclear which item they'd apply to.\n"
        "  · per-item links: put links= inside each item dict — items=[{{'title':..., 'links':[...]}}, ...]\n"
        "  · push after creation: add(items=[...]) first, then openbox(name='...', action='push', id='<new-id>') per id"
    ),
    "err_flow_doc_only": "error: flow is doc-only — a doc journey chain (lore has no flow).",
    "err_flow_files_forbidden": "error: flow chain targets must be doc id/title only — file paths not allowed: {files}",
    "err_unknown_type": "error: unknown type '{t}'. doc | lore",
    "err_batch_entry_bad_type": "type '{t}' unsupported — lore|doc",

    "files_more_suffix": " +{n} more",

    "auto_files_note": (
        "\n📎 auto-linked files (uncommitted diff): {files}"
        "\n   to unlink an unrelated file: unlink(a='{id}', b='filename')"
    ),
    "explicit_files_note": "\n📎 files linked: {files}",

    "link_ok": "  ↔ {target}",
    "link_fail": "  ⚠️ link({target}) failed: {err}",
    "link_summary_header": "\n🔗 linked (links=):\n",

    "push_to_fail": "\n  ⚠️ push_to failed: {err}",
    "push_to_unregistered": "  ⚠️ openbox '{name}' not registered — create it first with openbox(name='{name}', action='new')",
    "push_to_line": "  → {result}",

    "batch_streak_hint": (
        "\n💡 {n} single add() calls of the same type in a row — for multiple entries "
        "items=[{{...}}] batch is quieter (you can switch for the rest). Shown once per session."
    ),
}
