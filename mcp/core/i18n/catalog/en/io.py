"""English (en) messages for the 'io' surface."""
MESSAGES: dict[str, str] = {
    "err_no_store": "no memory yet (.linklore/ not found). run init() to start. (searched from: {start})",


    "err_store_missing_init": "no LinkLore store in this folder — run init() first. (searched from: {start})",
    "warn_boundary": "WARNING: this folder ({anchor}) has no .linklore - using the shared store from the parent '{store}'. call init() if you want independent memory.",

    "warn_pin_write_divergence": "WARNING: this write targets the pin ({target}), not {base} — unpin: config(action='unpin')",


    "warn_pin_export_divergence": "WARNING: this send exports data from the pin ({target}), not {base} — unpin: config(action='unpin')",


    "parent_independent": "ℹ️ starting as an independent store, separate from the parent '{parent}' store.",


    "parent_referenced": (
        "⚠️ the parent '{parent}' store has {n} item(s) referencing this folder — "
        "they will no longer show up from this project.\n"
        "   to bring them over: local(action='move', id=[...], from_dir='{parent_dir}', to='{child_dir}')"
    ),
}
