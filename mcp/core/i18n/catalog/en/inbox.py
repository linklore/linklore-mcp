"""English (en) messages for the 'inbox' surface."""
MESSAGES: dict[str, str] = {

    "err_source_unregistered": "source '{name}' not registered",

    "err_item_not_found": "'{item_id}' not found in source '{name}'",


    "provenance_report_failed": " (provenance report failed: {err})",

    "skipped_self": "original already present ({id}) — absorption unnecessary (already mine)",

    "deduped": "already imported — {name}/{id} → {new_id}",

    "imported": "[{new_id}] {kind_label} import complete — {name}/{id}",

    "local_source_noop": "remote/{pid}/ local source — remote sync unnecessary (lore {lore_count} / doc {doc_count})",

    "err_session_expired": "session expired (401) — re-login: uvx llre login",


    "err_not_found_on_server": (
        "openbox '{name}' is gone from the server (deleted by the owner, or stale). "
        "The cached copy is left as-is. To clear the local registration, run "
        "openbox(name='{name}', action='undocking')."
    ),

    "revoked": "remote/{pid}/ revoked — publication withdrawn, cleared",
}
