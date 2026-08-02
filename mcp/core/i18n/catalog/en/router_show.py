"""English (en) messages for the 'router_show' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "[read-only] show() — target/scope: query·type / filters: tag·status·file·period('Nh' hours|'Nd' days|'YYYY-MM-DD' UTC)·source_id / "
        "result shape: sort·max·oneline·superseded / mode: action / plumbing: help. "
        "Before editing code, check file=path for related lore/doc — a direct Edit/Write auto-surfaces this via a PreToolUse hook, but check it yourself before delegating. "
        "show/rm stay inside my own project — to browse an openbox, use openbox(action='show')"
    ),

    "log_tool_desc": (
        "[read-only] log(id) — shows the edit-history timeline (who changed what, when). "
        "No id = project-wide history. For current content use show(); for code<->doc "
        "drift use status(). "
        "period('Nh' hours|'Nd' days|'YYYY-MM-DD' UTC), sort=oldest, max, plumbing: help"
    ),

    "help": (
        "show — unified query (my own project only — to browse an openbox, use openbox(action='show'))\n\n"
        "## Target/scope (query, type)\n"
        "  query=ID  → detail (lr-*/dc-*)\n"
        "  query=ID+words mixed → ID match pinned on top + keyword results (a typo'd ID only gets a hint, never pollutes the keywords)\n"
        "  query=text → unified search (lore+doc)\n"
        "  type=collection → listing (lore/doc)\n"
        "  (none) → lore listing (self + auto_search external openbox merged)\n\n"
        "## Filters (tag, status, file, period, source_id)\n"
        "  tag, status(open/done/dropped/rule)\n"
        "  file(path match, against the files[] index) — check before editing code. A direct Edit/Write auto-surfaces\n"
        "    this via a PreToolUse hook, but delegating or investigating first still needs an explicit call. Lore never\n"
        "    added to files[] gets missed — pair with query=text for broader recall\n"
        "  source_id — reverse-lookup an ingested item's original id (openbox('pull') and local copy/move — 'have I already brought this in?')\n"
        "  range: period='24h'(last 24 hours) · period='7d'(last 7 days) · period='2026-07-01'(from that date, UTC) · period='2026-07-01..2026-07-08'(between, UTC)\n\n"
        "## Result shape (sort, max, oneline, superseded)\n"
        "  sort: sort(newest/oldest/alpha), max(N items), oneline(one line each)\n"
        "  for a detail view, max= caps how many clusters are shown (default 10, in listing mode it's the item-count cap as before)\n"
        "  other: superseded=True → include old lore and doc versions\n\n"
        "## Mode (action)\n"
        "  action='graph' → corpus audit aggregation (status/tag/body-length/link-graph distribution, exhaustive counts)\n"
        "  action='tags'  → tag list\n"
        "  (none) → listing/detail/search per the target/scope·filter·result-shape combo above\n\n"
        "## Plumbing (help)\n"
        "  help=True → this guide"
    ),

    "log_help": (
        "log — history query (SQL: lore/doc supersede chain + body edit history + unified timeline)\n\n"
        "id → lore change history (supersede chain + body edit history) or doc change history "
        "(supersede chain + body edit history) — body edit history lists every append/overwrite/section change, "
        "in order\n"
        "(none) → unified timeline (lore/doc changes in order)\n\n"
        "filters: period='24h'(last 24 hours) · period='7d'(last 7 days) · period='2026-07-01'(from that date, UTC) · period='2026-07-01..2026-07-08'(between, UTC), "
        "sort(oldest), max(default 20)"
    ),

    "err_action_invalid": "error: action='{action}' is not supported — use one of graph|tags",

    "err_sort_invalid": "error: sort='{sort}' is not supported — use one of {valid}",

    "err_period": "error: {err}",

    "empty_project": (
        "no results — this project has no memory yet.\n"
        "add(type='lore'/'doc', ...) to leave your first entry and start the trail."
    ),

    "overview": (
        "{lore_part}\n"
        "  ↳ narrow down: show(tag='...') · show(status='done') · show(query='search text')\n\n"
        "{doc_part}\n"
        "  ↳ narrow down: show(type='doc', tag='...')"
    ),

    "graph_title": "# Corpus stats (audit)",
    "graph_lore_summary": "lore: {live} live / {total} total (including superseded)",
    "graph_status_label": "  status: ",
    "graph_tags_label": "  top tags: ",
    "graph_tag_item": "#{t} {c}",
    "graph_body_len_line": "  body length: median {median} chars · mean {mean} chars · 1500+ chars {over}({pct}%)",
    "graph_linkgraph_line": "  link graph: {nodes} nodes, {edges} edges, {components} components (largest {top})",
    "graph_doc_summary": "doc: {total} live (excl. superseded/trash)",
    "graph_footer": "→ detail: show(tag=, status=, sort=, max=) · use a large max for everything",

    "tags_none_no_store": "no tags (no memory yet)",
    "tags_none": "no tags",
    "tags_header": "# Tags ({n})",
    "tags_count_lore": "lore {n}",
    "tags_count_doc": "doc {n}",
    "tags_line": "- #{tag} ({counts})",

    "lore_none": "no lore registered.",
    "lore_filtered_none": "no lore matches the filter. {total} total.",
    "lore_oneline_header": "lore ({shown}/{total})",
    "lore_cluster_suffix_oneline": "+{n} clustered",
    "lore_header": "# lore ({shown}/{total})",
    "lore_cluster_suffix_full": "  +{n} clustered (show(query=) for all)",

    "lore_cluster_suffix_full_openbox": "  +{n} clustered (openbox(action='show', query=...) for all)",

    "list_truncated_hint": "\n  … {shown} of {total} shown — more: max={total}",

    "log_no_history": (
        "'{id}' has no change history — history tracking is lore(supersede chain + body edit history)·"
        "doc(supersede chain + body edit history) only. check the current state with show."
    ),


    "mixed_id_hits_header": "# ID matches ({n})",


    "mixed_id_miss": "note: {hint}",
}
