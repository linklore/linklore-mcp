"""English (en) messages for the 'doc_flow' surface."""
MESSAGES: dict[str, str] = {

    "flow_tool_desc": "[read-only] doc_flow(id) — renders a doc's flowLink chain in order (journey view).",

    "flow_help": (
        "doc_flow — doc journey view (flowLink chain)\n\n"
        "  doc_flow()            — list all flow start points\n"
        "  doc_flow(id='dc-xxx') — expand the flowLink chain from a start point\n\n"
        "edit: edit(id='dc-xxx', links=['dc-yyy'], flow=True)\n"
        "flowLink is one-directional — if there are multiple branches, only the first target is shown.\n"
        "cleaning up (broken link) entries = doctor(action='fix') — auto-deletes links with missing targets."
    ),
    "no_flow_links": "no flow links\nedit(id='dc-xxx', links=['dc-yyy'], flow=True) to create a flow",
    "no_clear_start": "no clear start point — {n} doc(s) with flowLink",
    "starts_header": "# doc_flow — {n} start point(s)",
    "start_line": "- **{title}** [{id}] → {n}-step chain",
    "starts_footer": "expand a chain with `doc_flow(id='dc-xxx')`",
    "flow_not_found": "error: doc '{id}' not found.",
    "chain_header": "# doc_flow({id}) — {n} step(s)",
    "current_suffix": "  (current)",
    "branch_suffix": "  (+{n} branch(es))",
    "branches_header": "## branches ({n} — following the first one only)",
    "branch_item": "- {title} [{id}]",
    "branch_item_broken": "- (broken link) [{id}]",


    "map_tool_desc": "[read-only] doc_map(oneline) — overview of the full doc link network.",

    "map_help": (
        "doc_map — doc link network overview\n\n"
        "  doc_map(oneline=True)  — per-cluster representative title + count summary (start here for large projects)\n"
        "  doc_map()              — full doc + link detail per cluster\n\n"
        "↔ docLink (related) / → flowLink (flow)\n"
        "cleaning up broken links = doctor(action='fix') — auto-deletes links with missing targets."
    ),
    "no_docs": "no docs",
    "map_header_body": " ({n} total: {conn} connected cluster(s), {iso} unconnected",
    "map_header_dangling": ", {n} broken link(s)",
    "map_header_empty_note": "\nno connections yet (normal — link items together as they accumulate)",
    "more_suffix": " +{n} more",
    "chunk_oneline_line": "## cluster {i} ({n}): {preview}{more}",
    "isolated_oneline_footer": "\n{n} unconnected — detail: doc_map()",
    "chunk_header": "## cluster {i} ({n})",
    "external_label": "(external)",
    "isolated_header": "## unconnected ({n})",
    "truncated_suffix": "  ... +{n} more",
    "dangling_header": "## broken links ({n})",
    "dangling_item": "- **{title}** [{id}] {field} → {target} (target not found)",
}
