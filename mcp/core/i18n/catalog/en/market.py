"""English (en) messages for the 'market' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": (
        "Browse and pull free lore/doc from LinkLore's public curated catalog — no "
        "account needed.\n"
        "market(query=, id=, filter=, order=, max=) — default (no action=) searches/browses: "
        "id= alone shows a single listing's detail, query=/filter=/order=/max= search the "
        "catalog. action='pull' with id= fetches that listing into this project.\n"
        "Buy lore. Pull it into your project."
    ),

    "help": (
        "market — the public curated catalog (no account, no auth).\n\n"
        "## Search/browse (default, action omitted)\n"
        "  market()                              → curated order, top results\n"
        "  market(query='mcp auth')              → free-text search (title/tags)\n"
        "  market(filter='build')                → category filter\n"
        "  market(order='hot')                   → most-pulled first (falls back to curated "
        "if there isn't enough pull data yet — said so honestly, not silently)\n"
        "  market(order='new')                   → most recently published first\n"
        "  market(id='lr-xxxxxxxx')              → single listing detail (no query=)\n\n"
        "## Pull\n"
        "  market(action='pull', id='lr-xxxxxxxx')  → fetch it into this project (ingest.ingest_item, "
        "same primitive as openbox pull)\n"
        "    - already pulled (same source id)  → idempotent, nothing changes\n"
        "    - curator republished with new content → local copy is replaced (any local edits to "
        "that copy are lost — loud warning)\n"
        "    - no longer offered (removed/retired) → your copy (if any) is unaffected, told plainly, "
        "no did-you-mean (it's a real id, just not offered anymore)\n"
        "    - unknown id                        → did-you-mean against nearby catalog ids\n\n"
        "Everything here is free — no purchase step in v1."
    ),
    "err_invalid_action": "error: market() action must be '' (search/browse) or 'pull'.",
    "err_no_id": "error: action='pull' requires id= (a catalog listing id, lr-*/dc-*).",
    "err_network": "error: market request failed ({code}) — {resp}",
    "err_not_found": "market: no such id '{id}'.",
    "didyoumean_item": "market(action='pull', id='{id}')  # {title}",
    "didyoumean_suffix": " did you mean: {items}",
    "removed_tombstone": "[{id}] no longer available (removed {date}) — your copy is unaffected.",

    "search_header_query": "market — \"{query}\" ({count})",
    "search_header_hot": "market — hot ({count})",
    "search_header_new": "market — new ({count})",
    "search_header_curated": "market — curated ({count})",
    "search_header_category_suffix": " · category={category}",
    "hot_insufficient_banner": "(not enough pulls yet — curated order)",
    "empty_result": "no lore found in the market catalog. try a broader query or drop filter=.",
    "result_tags_suffix": " #{tags}",
    "result_line": "- **{title}** — {category}{tags_suffix} [{id}]",
    "result_summary_line": "  {summary}",

    "detail_header": "# {title} [{id}]",
    "detail_category_line": "**category:** {category}",
    "detail_curator_line": "**curator:** {curator}",
    "detail_tags_line": "**tags:** {tags}",
    "detail_published_line": "**published:** {date}",
    "detail_pulls_line": "**pulls:** {count}",
    "detail_sections_header": "\n## sections ({count})",
    "detail_sections_item": "- {heading}",
    "detail_pull_cta": "\npull: market(action='pull', id='{id}')",

    "pull_success": "[{id}] installed — 1 absorbed ({kind})",
    "pull_success_workspace_own": "workspace: {anchor}",
    "pull_success_workspace_parent": "workspace: {anchor} (stored in parent {store})",
    "pull_success_next": "next: brief()",
    "pull_deduped": "[{id}] already installed — nothing to do.",
    "pull_updated": "[{id}] updated — local copy replaced with the latest version.",
    "pull_updated_warning": "⚠ local copy replaced — any local edits you made to this copy are gone.",
}
