"""Centralized English-only text for developer-facing log lines (not user-facing i18n)."""
LOG_MESSAGES: dict[str, str] = {
    "json_corrupt_fallback": "corrupt json: %s — falling back to default",
    "project_id_migration_failed": "project_id migration trigger failed (ignored): %s",
    "brief_section_load_failed": "brief section '%s' failed to load: %s",
    "external_sync_trigger_failed": "external source background sync trigger failed: %s",
    "auth_json_corrupt": "auth.json corrupted — treating as logged out: %s",
    "keychain_migration_done": "account token migrated to Keychain — plaintext removed from auth.json",
    "import_provenance_skipped": "import provenance report skipped — exception: %s",
    "lore_embed_incremental_failed": "incremental embedding update failed",
    "lore_embed_remove_failed": "embedding index removal failed (%s) — search may be out of sync, resolve via restore/reindex: %s",
    "lore_reembed_failed": "re-embedding failed (%s) — semantic search may miss this item until next index update: %s",
    "tool_empty_response": "EMPTY %s → None/empty response",
    "embed_backend_missing": "fastembed not installed — semantic search disabled. pip install 'llre[embed]'",
    "embed_model_load_failed": "embedding model load failed (assuming transient, retry in %.0fs): %s",
    "login_stale_session_revoke_failed": "§5 session hygiene: failed to revoke old session — best-effort, login proceeds normally",
}
