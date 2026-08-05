"""English (en) messages for the 'sections' surface."""
MESSAGES: dict[str, str] = {

    "ambiguous": "ambiguous — candidates: [{candidates}]. Be more specific.",


    "not_found": (
        "section not found — available sections: [{sections}]. "
        "to add a new section, use edit(id, action='append')."
    ),


    "not_found_no_headings": (
        "section not found — this document has no section headings. "
        "to add a new section, use edit(id, action='append')."
    ),


    "not_found_read": (
        "section not found — available sections: [{sections}]. "
        "for the full item, use show(query='<id>')."
    ),
    "not_found_no_headings_read": (
        "section not found — this item has no section headings. "
        "for the full item, use show(query='<id>')."
    ),
}
