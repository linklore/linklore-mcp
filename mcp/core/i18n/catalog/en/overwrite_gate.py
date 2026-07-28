"""English (en) messages for the 'overwrite_gate' surface."""
MESSAGES = {
    "err_confirm_not_alone": (
        "error: confirm= can only be used alone — extra args given: {params}.\n"
        "  re-call the exact command the warning gave you (with no other args)."
    ),
    "err_plan_not_found": (
        "error: no pending action matches that confirm number (expired after 15 min, "
        "already run/cancelled, or a number from a different tool).\n"
        "  start over — call the original command again (without confirm)."
    ),
    "err_legacy_confirm": (
        "error: the old confirm style (code string / boolean True) is retired — "
        "confirm= is now the number the warning gives you (e.g. confirm=1).\n"
        "  call the original command again (without confirm) to get a fresh warning and number."
    ),
    "pending_multi_header": "⚠️ multiple confirmations are pending — re-call with the exact number:",
    "pending_multi_item": "  {slot}. {desc}{mine_tag}  →  {tool}(confirm={slot})",
    "pending_multi_mine": " (just registered)",
}
