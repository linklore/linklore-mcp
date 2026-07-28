"""English (en) messages for the 'cleanup' surface."""
MESSAGES: dict[str, str] = {

    "tool_desc": "[read-only] cleanup(type='lore'|'doc') threshold(=0.85), status(=open), help - duplicate candidates.",

    "help": (
        "cleanup - show strong duplicate lore/doc candidates\n"
        "\n"
        "  cleanup()                  default - type='lore', open only (excludes decided items)\n"
        "  cleanup(type='doc')        doc duplicate candidates (see limitation below)\n"
        "  cleanup(status='')         include all statuses (done/dropped, etc.)\n"
        "  cleanup(status='done')     compare within one specific status\n"
        "  cleanup(threshold=0.80)    looser matching\n"
        "\n"
        "How it works: cosine similarity matrix over head-item (lore or doc) embeddings -> pairs at or above threshold.\n"
        "Defaults to open - decided items (done/dropped) are excluded since they're already resolved.\n"
        "Shown as: new <-> old (duplicate candidate). Suggested command = link(a=old, b=new, action='supersede').\n"
        "WARNING type='doc' limitation: doc embeddings use title+body(first 500 chars)+items+tags -\n"
        "   duplicates that only differ after the 500-char cutoff won't be caught.\n"
        "WARNING no automatic deletion - a human decision is required."
    ),

    "pair_new": "  new: {id} {title}",
    "pair_old": "  old: {id} {title}",
    "pair_confirm": "  -> confirm replace: link(a='{older_id}', b='{newer_id}', action='supersede')",

    "not_enough_lore": "not enough lore to compare (fewer than 2 candidates).",
    "not_enough_doc": "not enough doc to compare (fewer than 2 candidates).",
    "err_no_embed_model": "error: embedding model not installed (fastembed)",
    "not_enough_indexed_lore": "not enough head lore registered in the embedding cache.",
    "not_enough_indexed_doc": "not enough head doc registered in the embedding cache.",
    "no_dup_lore": "no strong duplicate lore found (cos >= {threshold}, {count} head items checked)",
    "no_dup_doc": "no strong duplicate doc found (cos >= {threshold}, {count} head items checked)",
    "dup_candidates_header": "# duplicate candidates (cos >= {threshold}, {pairs} found / {count} head items checked)",
    "warn_manual_lore": "WARNING no automatic close - similar-but-distinct lore exists too, review the body before deciding.",
    "warn_manual_doc": "WARNING no automatic close - similar-but-distinct doc exists too, review the body before deciding.",
    "doc_embed_limit_note": "WARNING doc embeddings are based on title+body(first 500 chars)+items+tags - duplicates that only differ after 500 chars won't be caught.",
}
