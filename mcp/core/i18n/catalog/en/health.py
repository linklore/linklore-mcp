"""English (en) messages for the 'health' surface."""
MESSAGES: dict[str, str] = {
    "dangling_cleared": (
        "{label} [{item_id}] {field} dangling ref cleared "
        "(item stays dropped - restore to bring it back)"
    ),
    "old_new_sealed": "{label} [{target_id}] → [{item_id}] oldId/newId seal completed",
    "resealed": "{label} [{item_id}] head=False/status=dropped resealed",
    "orphan_seal_revived": "{label} [{item_id}] head=True restored (orphaned seal resolved, status=dropped kept)",
    "orphan_link_deleted": "{collection} [{item_id}]→[{target_id}] {count} orphaned link(s) deleted",
    "orphan_ref_deleted": "lore_works [{item_id}]→[{target_id}] orphaned reference deleted",
    "dangling_supersede": "{label} [{item_id}] {field}={target_id} — target not found (dangling, corruption)",
    "half_sealed": "{label} [{item_id}] has no newId (half-written) — [{ref_id}] points to it via oldId",
    "supersede_fork": "{label} [{item_id}] newId={new_id}, but [{ref_id}] also points to it via oldId (fork)",
    "superseded_but_head": "{label} [{item_id}] has newId={new_id} set but head=True (half-sealed)",
    "orphaned_seal": "{label} [{item_id}] has head=False but no newId — orphaned seal (replacement deleted, reference lost)",
    "supersede_convergence": "{n} convergence group(s) — normal (multiple items converging on the same new_id)",
    "trash_reference": "{n} trash reference(s) — restored via restore, cleared on permanent delete",
    "stale_file": "{label} [{item_id}] — file {path} not found (deleted/moved)",
    "broken_link_src": "{collection} [{src}]→[{dst}] ({kind}) — src {entity_word} [{src}] not found",
    "broken_link_dst": "{collection} [{src}]→[{dst}] ({kind}) — dst {entity_word} [{dst}] not found",
    "broken_ref_lore": "lore_works [{lore_id}]→[{doc_id}] — lore [{lore_id}] not found",
    "broken_ref_doc": "lore_works [{lore_id}]→[{doc_id}] — doc [{doc_id}] not found",
}
