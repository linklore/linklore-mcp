"""English (en) messages for the 'link' surface."""
MESSAGES: dict[str, str] = {

    "warn_superseded": "⚠ {eid} is superseded — check whether linking to the latest head makes more sense (show(query=))",
    "warn_dropped": "⚠ {eid} is a dropped item — linking to a dropped item",


    "err_entity_not_found": "error: {label} not found — {id}",
    "err_entity_not_found_simple": "error: {label} not found",
    "already_linked": "already linked",
    "not_linked_simple": "not linked (already disconnected)",


    "linked_symmetric": "{a_title} ↔ {b_title}\nlinked ({label}Link, both directions)",
    "unlinked_symmetric": "{a_title} ↮ {b_title}\nunlinked ({label}Link, both directions)",


    "already_linked_flow": "already linked: {a} → {b}",
    "linked_flow": "{a_title} → {b_title}\nflow linked (flowLink)",
    "not_linked_flow": "not linked: {a} → {b} (already disconnected)",
    "unlinked_flow": "{a_title} ↛ {b_title}\nflow unlinked (flowLink)",


    "already_linked_cross": "already linked: {a_id} ↔ {b_id}",
    "linked_cross": "{a_title} ↔ {b_title}\nlinked ({label})",
    "not_linked_cross": "not linked: {a_id} — {b_id} (already disconnected)",
    "unlinked_cross": "{a_title} ↮ {b_title}\nunlinked ({label})",


    "err_supersede_type_mismatch": "error: supersede only works within the same type — lore↔lore or doc↔doc",
    "err_supersede_self": "error: cannot supersede an item with itself",
    "err_supersede_target_missing": "error: the replacement target '{b}' does not exist (prevents a phantom supersede).",
    "supersede_done": (
        "[{a}] dropped + replaced → [{b}]\n"
        "  A dropped item with a replacement is auto-excluded from search (head=False). Visible via show(superseded=True)·show(query=).\n"
        "  cf. a drop with no replacement is just status='dropped' (stays in search)."
    ),


    "err_action_file_incompatible": "error: action='{action}' cannot combine with a file path — files are only supported with related (default)",
    "err_unrecognized": "error: '{raw}' is not recognized — must be an id(lr-*/dc-*), an existing title, or an existing file.",
    "err_flow_file_incompatible": "error: flow=True cannot combine with a file path — files are only supported without flow (default)",
    "err_item_not_found": "error: '{other}' not found.",
    "not_linked_file": "not linked: {other} — {file} (already disconnected)",
    "unlinked_file": "{title} ↮ {file}\nunlinked (file)",


    "link_desc": (
        "link(a, b, action=) — connect two items (dc↔dc / lr↔lr / dc↔lr auto-detected, prefix matching OK).\n"
        "a/b may also be a file path or an existing title — non-id-shaped values are auto-classified (same as links= in add/edit).\n"
        "Undo (inverse) = unlink(a, b) — same arguments.\n"
        "\n"
        "action has 5 modes (extends the member/config(action=) convention):\n"
        "- action='related' (default, same if omitted) → mutual link (symmetric). Same as link(a, b) — dc↔dc/lr↔lr/dc↔lr\n"
        "- action='flow'    → not a mutual link but **document order** (a→b direction, doc↔doc only): read a, then b.\n"
        "- action='supersede' → \"a is replaced by b\" — a=old (dropped, head=False/dropped), b=target (alive,\n"
        "                        must be an existing item — none is created). lore↔lore or doc↔doc only.\n"
        "- action='unrelated' → verdict: not related — this pair stops appearing as related candidates or duplicate alerts (not a link, a stored verdict).\n"
        "- action='distinct'  → verdict: not a duplicate (confirmed separate) — only duplicate alerts are silenced, it still appears as a related candidate.\n"
        "\n"
        "The 4 suggestion verdicts: related-yes=link(a,b) · duplicate-yes=action='supersede' · "
        "related-no=action='unrelated' · duplicate-no=action='distinct'\n"
    ),
    "link_help": (
        "link — connect two items (ID prefix auto-detected)\n"
        "\n"
        "## ID format\n"
        "  prefix matching OK (e.g. 'lr-1a2b3c4' auto-matches dc-1a2b3c4d). Ambiguous matches need the full ID.\n"
        "  non-id-shaped values are auto-classified (reuses the same classifier as links= in add/edit):\n"
        "  link('lr-X', 'existing lore title')  → exact title match links to that id\n"
        "  link('lr-X', 'src/a.py')            → an existing file links as code (X.files, not the link table)\n"
        "    (file paths only work with action='related' (default) — flow/supersede are structural\n"
        "     relations that can't combine with files, both are rejected)\n"
        "\n"
        "## action='related' (default) — mutual link\n"
        "  link('dc-A', 'dc-B')              → docLink on both sides (mutually related)\n"
        "  link('lr-X', 'lr-Y')              → loreLink on both sides (clustering)\n"
        "  link('dc-A', 'lr-X')              → adds A to lore X.works\n"
        "  link('lr-X', 'dc-A')              → same as above (order doesn't matter)\n"
        "\n"
        "## action='flow' — document order (a→b direction, doc↔doc only)\n"
        "  link('dc-A', 'dc-B', action='flow')   → adds B to A.flowLink (read a, then b)\n"
        "\n"
        "## action='supersede' — a is replaced by b (a=old dropped, b=target alive)\n"
        "  link('lr-old', 'lr-new', action='supersede')  → lr-old head=False/dropped, replaced by lr-new\n"
        "  link('dc-old', 'dc-new', action='supersede')  → same as above (doc)\n"
        "  constraint: same type only (lore↔lore/doc↔doc) · b must be an existing item\n"
        "\n"
        "## the 4 suggestion verdicts — responding to related candidates / duplicate alerts (2 yes + 2 no)\n"
        "  related-yes   → link(a, b)                       existing link (linked pairs stop being re-suggested)\n"
        "  duplicate-yes → link(a, b, action='supersede')   existing replace (old item sealed)\n"
        "  related-no    → link(a, b, action='unrelated')   stored verdict — silences related candidates + duplicate alerts\n"
        "  duplicate-no  → link(a, b, action='distinct')    stored verdict — silences duplicate alerts only (stays a related candidate: separate but related)\n"
        "  direction-agnostic (a/b order free) · no type constraint (lr↔lr/dc↔dc/dc↔lr) · repeated calls are idempotent\n"
        "  re-judge (undo) = unlink(a, b, action=same value)\n"
        "\n"
        "limits: dc↔lr + flow/supersede not supported (supersede only works within the same kind (lr↔lr/dc↔dc) · flow is doc↔doc only)\n"
        "\n"
        "Undo (inverse) = unlink(a, b) — same arguments (file links included)"
    ),
    "err_ab_required": "error: both a and b IDs are required",
    "err_self_link": "error: cannot link an item to itself",
    "err_bad_action": "error: action='{action}' is not supported — use one of related|flow|supersede|unrelated|distinct",


    "verdict_unrelated_done": (
        "{a} ✕ {b} verdict saved: unrelated\n"
        "  this pair will no longer appear as a related candidate or duplicate alert. Undo = unlink(a='{a}', b='{b}', action='unrelated')"
    ),
    "verdict_distinct_done": (
        "{a} ≠ {b} verdict saved: not a duplicate (distinct)\n"
        "  only duplicate alerts are silenced — it still appears as a related candidate (separate but related). Undo = unlink(a='{a}', b='{b}', action='distinct')"
    ),
    "verdict_already": "already judged: {a} — {b} ({action}) — repeated calls are idempotent (no change)",
    "verdict_removed": "verdict removed: {a} — {b} ({action}) — candidates/alerts restored",
    "verdict_not_found": "no verdict: {a} — {b} ({action}) (already cleared)",
    "err_unrecognized_id": "error: unrecognized ID — a={a} ({a_col}), b={b} ({b_col})",
    "err_flow_link_only": "error: flow only supports doc↔doc (both dc-*)",


    "unlink_desc": "unlink(a, b, action=) — disconnect two items or clear a verdict. Symmetric with link() (action='' default|'flow'|'unrelated'|'distinct', also accepts file paths the same way).",
    "unlink_help": (
        "unlink — disconnect (symmetric with link)\n"
        "\n"
        "  unlink('dc-A', 'dc-B')                    → removes docLink on both sides\n"
        "  unlink('dc-A', 'lr-X')                    → removes A from X.works\n"
        "  unlink('dc-A', 'dc-B', action='flow')     → removes B from A.flowLink\n"
        "  unlink('lr-X', 'src/a.py')                → removes that file from X.files\n"
        "  unlink('lr-X', 'lr-Y', action='unrelated') → clears the 'unrelated' verdict (candidates/alerts restored)\n"
        "  unlink('lr-X', 'lr-Y', action='distinct')  → clears the 'distinct' verdict (duplicate alerts restored)\n"
        "  (action='flow' combined with a file path is rejected — files are only supported with action='', symmetric with link())"
    ),
    "err_bad_action_unlink": "error: action='{action}' is not supported — use one of flow|unrelated|distinct (or omit it)",
    "err_flow_unlink_only": "error: flow only supports doc↔doc",


    "err_sentinel": "error",
}
