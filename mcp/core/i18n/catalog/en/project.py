"""English (en) messages for the 'project' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "[read-only] project dashboard — call at the start of every session.\n"
        "\n"
        "external source 🔔 = a new push has arrived. receive it with openbox(action='show').\n"
        "options: dismiss(turn off a nudge), undismiss(restore it), help."
    ),

    "help": (
        "brief — project dashboard\n\n"
        "Call at session start. Feature list + lore stats + stale detection + recent activity.\n"
        "dismiss: turn off a nudge (comma-separated keys)\n"
        "undismiss: restore a nudge"
    ),


    "identity_name_part": " ({name})",
    "identity_connected": "iam: @{handle}{name_part} ✓ account linked",


    "identity_project_acting": "iam: @{handle}{name_part} ✓ acting as project iam",
    "identity_local_only": "iam: @{handle}{name_part} · local only (link account: login)",


    "location_counts": "doc {doc_count} lore {lore_count} (total, incl. superseded/dropped)",
    "location_own_store": "here: {anchor} · own store · {counts}",
    "location_parent_store": (
        "here: {anchor} · belongs to parent workspace '{store}' "
        "(this folder has no store of its own) · {counts}\n"
        "   independent memory for this folder: init()"
    ),
    "location_pin_suffix": "\n📌 pin: {name} ({path}) — unpin: config(action='unpin')",
    "location_identity_suffix": "\n🪪 project iam: {display} — details: config(action='whoami')",


    "brief_empty": (
        "# {name}\n\n"
        "here: {name} · unregistered (.linklore missing)\n\n"
        "get started:\n"
        "- already have a project elsewhere? `config(action='projects')` to list it, "
        "then `config(action='pin', dir='/path/to/project')` to attach here instead of "
        "starting a new one\n"
        "- starting fresh: `init()`            start independent footprint memory in this folder\n"
        "- `add(type='lore'/'doc', ...)`  leave your first record (after init, lore-first)\n"
        "- `show(file='path')` / `show(query=...)`  (once registered) search related memory"
    ),


    "doc_flow_header": "**doc flow ({count}):**",
    "doc_flow_item": "- {title} → {steps} step(s) [doc_flow(id='{id}')]",
    "doc_flow_more": "  +{count} more — doc_flow()",


    "cleanup_header": "**cleanup candidates:**",
    "cleanup_extra_suffix": " +{count} more",
    "cleanup_stale_item": "- #{tag} {count} lore accumulated — candidate doc: {titles}{extra} — consider distributing/updating",
    "cleanup_pending_item": "- #{tag} {count} lore accumulated, no related doc — consider doc_rollup/manual doc cleanup",


    "external_sources_header": "**external source ({count}):**",
    "auto_search_flag": "auto_search ",
    "external_source_local": "- [{name}] {auto}— local link (always current)",
    "external_source_no_access": "- [{name}] {auto}— ⚠️ not accessible (login required/expired or not a member) → login",
    "external_source_first_pull": "- [{name}] {auto}— 🔔 first pull needed (rev {rev}) → openbox(name='{name}', action='show')",
    "external_source_changed": "- [{name}] {auto}— 🔔 changed (rev {last} → {current}) → openbox(name='{name}', action='show')",
    "external_source_latest": "- [{name}] {auto}— up to date (rev {rev})",
    "external_sources_footer": "  → openbox(name=, action='pull', id=) to copy",


    "stale_header": "doc not updated after code changes ({count}) — check with status",
    "stale_file_extra": " +{count} more",
    "stale_item": "  - {name}: {files}",


    "hotspot_tag": "  {warn}{title} [{id}]",
    "hotspot_line": "    {path} ·{age}{tag}",


    "codemap_stale_suffix": " · map refreshing",
    "codemap_header": "## code map (auto-derived{stale})",
    "codemap_head_bits_line": "  {bits}",
    "codemap_run_line": "  run: {bits}",
    "codemap_structure_line": "  structure: {mods}",
    "codemap_landmarks_line": "  → {items}",
    "codemap_entities_more": " +{count}",
    "codemap_entities_line": "  entities: {entities}{more}",
    "codemap_hotspot_legend": " · ⚠=unresolved",
    "codemap_hotspot_header": "  hotspots (recent+decisions{legend}):",


    "title_header": "# {name}",
    "legend_doc": "doc = design·features·tech docs·checklists → show(type='doc')",
    "legend_lore": "lore = decisions·lessons·pitfalls·rules → show()",
    "doc_summary": "doc: {total} (done {done}) — list show(type='doc') · filter show(type='doc', tag='...')",
    "tag_hint_more": " +{count} more",
    "tag_hint_line": "  tags (by frequency): {tags}",


    "lore_summary": "lore: {count} (excl. superseded/dropped) — list show() · filter show(tag='...')",
    "lore_summary_zero": "lore: 0",
    "rule_doc_note": " · doc {count}",
    "rule_header": "**rule ({count}{doc_note}):**",
    "rule_item": "- {title} [{id}]",
    "rule_tail_more": "  +{count} more → show(status='rule')",
    "rule_tail_default": "  → show(status='rule')",
    "rule_tail_doc_suffix": " · doc: show(type='doc', status='rule')",
    "unresolved_header": "**unresolved:**",
    "unresolved_tags_paren": " ({tags})",
    "unresolved_item": "- {title}{tags_suffix} [{id}]",
    "recent_activity_header": "**recent activity:**",
    "recent_activity_item": "- [{kind}] {title} ({date}){author} [{id}]",
    "nudge_no_doc": "no docs yet → capture core structural docs with add(type='doc')",
    "nudge_no_lore": "no lore yet — recommended to start recording lessons (add)",
    "recommend_header": "recommended:",
    "recommend_item": "  - [{nudge_key}] {msg}",
    "section_failed": "  (⚠ failed to display {name}: {error})",


    "section_name_doc_flow": "doc flow",
    "section_name_cleanup": "cleanup candidates",
    "section_name_external_sources": "external source",
    "section_name_stale": "stale detection",
    "section_name_codemap": "code map",
}
