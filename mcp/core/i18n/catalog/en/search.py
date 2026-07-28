"""English (en) messages for the 'search' surface."""
MESSAGES: dict[str, str] = {
    "empty": (
        "no results - this project has no memory yet.\n"
        "add(type='lore'/'doc', ...) to leave the first record and start the trail."
    ),
    "err_no_id": "error: enter an ID.",
    "err_not_found_empty": "'{id}' not found - this project has no memory yet.",
    "err_not_found": "error: '{id}' not found.",
    "hint_token": "'{term}' {count} hits",
    "common_word_hint": "note: common words filled up the matches - {parts} appear a lot. Add 1-2 more distinctive words to narrow it down.\n\n",
    "no_exact_match_suggestions": "no exact match for '{query}'. suggestions by relevance:",
    "no_match": "no lore/doc found related to '{query}'.",
    "err_openbox_not_registered": "error: openbox '{name}' not registered",
    "tags_label": "tags: {tags}",
    "copy_hint": "\n-> openbox(name='{openbox}', action='pull', id='{id}') to copy",


    "external_id_hint": (
        "\nnote: this id exists in openbox '{name}' - "
        "openbox(name='{name}', action='show', query='{id}') or openbox(name='{name}', action='pull', id='{id}')"
    ),
    "err_id_not_found": "[{openbox}] ID '{query}' not found (lore {lore_count} / doc {doc_count})",
    "no_match_external": "[{openbox}] no match for '{query}' (lore {lore_count} / doc {doc_count})",
    "search_header": "# [{openbox}] search '{query}'",
    "lore_section_header": "\n## lore ({count})",
    "doc_section_header": "\n## doc ({count})",
    "more_items": "  and {count} more",
    "copy_hint_example": "\n-> openbox(name='{openbox}', action='pull', id='lr-...') to copy",
    "kw_title_fallback": ",#8-title-fallback",
}
