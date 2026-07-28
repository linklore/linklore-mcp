"""English (en) messages for the 'guard' surface."""
MESSAGES: dict[str, str] = {

    "stale_doc_hint": "[stale] doc update recommended: {names}{extra}",
    "stale_doc_tip": "  → review via show(type='doc'), then apply with edit",

    "stale_extra": " and {n} more",

    "stale_lore_header": "[lore] {n} related pitfall(s)/rule(s):",
    "stale_lore_more": "  (+{n} more)",

    "file_surface_header": "⚠️ {n} related decision(s)/pitfall(s) for this file (LinkLore — review before changing):",
    "file_surface_more": "  (+{n} more — see show(file=) for all)",
}
