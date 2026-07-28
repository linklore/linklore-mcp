"""English (en) messages for the 'nodes' surface."""
MESSAGES: dict[str, str] = {

    "err_multi_id_match": "'{query}' — matched multiple IDs: {names}",

    "err_multi_name_match_header": "'{query}' — matched multiple items (closest first):",

    "hint_specify_by_id": "→ specify by ID.",

    "dead_note": "\n(search dropped items: show(superseded=True))",

    "not_found_with_suggestions": "error: '{query}' not found. Did you mean:\n",

    "not_found_plain": "error: '{query}' not found. Try show(query='{query}').",
}
