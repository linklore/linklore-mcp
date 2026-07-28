"""English (en) messages for the 'doc_rollup' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": "[read-only] doc_rollup(id) — collects lore linked to a doc into an AI-summary draft.",

    "help": (
        "doc_rollup — collect linked lore → markdown for AI summarization\n\n"
        "  doc_rollup(id='dc-xxx')\n\n"
        "behavior: MCP gathers related lore (explicit works links + tag matches).\n"
        "MCP does not edit anything itself. The AI reads it, proposes a summary draft → user confirms →\n"
        "the AI calls edit(id, items='...').\n\n"
        "⚠️ never auto-overwrite the doc. User judgment required."
    ),
    "err_no_id": (
        "error: id is required — doc_rollup(id='dc-xxx') (rollup targets a single doc, so there's "
        "no list mode — find candidates with show(type='doc') or doc_flow())"
    ),
    "not_found": "error: doc '{id}' not found.",
    "tags_label": "tags: {tags}",
    "items_header_progress": "## current items ({done}/{n})",
    "items_header_plain": "## current items ({n})",
    "items_none": "(none)",
    "explicit_header": "## explicitly linked lore ({n})",
    "explicit_none": "(none — lore with this doc in lore.works)",
    "tag_header_base": "## tag-matched lore ({n}",
    "tag_header_omitted": " / {total} total — top {limit} by most recent, {omitted} omitted",
    "tag_header_footer": " · matched on: {tags})",
    "tag_none": "(none — generic tags (design/decision, etc.) are noise and excluded from matching. only specific tags match)",
    "tag_omitted_notice": (
        "  ⚠️ {omitted} omitted (showing top {limit}) — check the full set before rolling up: "
        "show(tag='{tag}')"
    ),


    "rollup_insufficient_stub": "(not enough material to roll up — {n} linked lore. once more lore accumulates, an items draft can be proposed)",
    "ai_guide_header": "## 📌 AI processing guide",
    "ai_guide_1": "1. Read the lore above and draft a **reorganized items proposal**",
    "ai_guide_2": "2. **Propose it to the user**: which items are new/changed/completed",
    "ai_guide_3": "3. Only after user confirmation, call `edit(id='{id}', items='...')`",
    "ai_guide_warn": "⚠️ **never auto-overwrite the doc**. It's the project's source of truth — user judgment required.",
    "ai_guide_tip": "You can also propose `edit(id='{id}', tags='+new-tag')` etc. at the same time.",

    "more_lines_suffix": "  ... (+{n} more line(s))",
}
