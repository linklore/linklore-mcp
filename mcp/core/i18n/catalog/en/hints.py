"""English (en) messages for the 'hints' surface."""
MESSAGES: dict[str, str] = {


    "sem_label": " (semantically similar {cosine})",


    "weak_candidates": "  {n} weak candidate(s) — run cleanup() to review overlaps",


    "dup_action_unrelated": "   • unrelated (not related) → link(a='{new_id}', b='{top_id}', action='unrelated')",
    "dup_action_distinct": "   • not a duplicate (confirmed separate) → link(a='{new_id}', b='{top_id}', action='distinct')",
    "conflict_action_unrelated": "   • unrelated → link(a='{new_id}', b='{top_id}', action='unrelated')",


    "dup_header": "\n🚨 Very similar lore (possible duplicate):",
    "dup_judge_header": "   Judge (don't open it — use the preview above: same decision?):",
    "dup_action_supersede": "   • the new one wins  → link(a='{top_id}', b='{new_id}', action='supersede')",
    "dup_action_keep": "   • keep existing     → rm(id='{new_id}', force=True)",
    "dup_action_no_id": "   → After checking the content: link(action='supersede') or rm(force=True) or keep",


    "conflict_header": "\n⚠️ Conflicting candidates (same topic — check for opposite conclusions):",
    "evidence_suffix": " (evidence: {evidence})",
    "conflict_judge_header": "   Judge (polarity = conclusion direction — use the preview above):",
    "conflict_action_opposite": "   • opposite decision (conflict)   → confirm the current one, then link(action='supersede') to seal the old decision",
    "conflict_action_reinforce": "   • reinforcement/continuation (complementary) → edit(id='{new_id}', links=['{top_cid}']) to link them",

    "related_header_full": "\nRelated candidates (suggested · not linked — to link, use links=/link()):",
    "related_header_short": "Related candidates (suggested · not linked):",
}
