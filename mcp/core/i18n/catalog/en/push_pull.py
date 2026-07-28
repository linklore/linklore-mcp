"""English (en) messages for the 'push_pull' surface."""
MESSAGES: dict[str, str] = {

    "err_unauthorized": "error: session expired (401) — reauthentication required",
    "err_not_found_on_server": (
        "This project is not on the server (deleted or moved). "
        "The local copy is intact — run push() to upload it."
    ),
    "err_reauth_failed": "error: session expired (401) — reauthentication required\n  log in again: uvx llre login",
    "err_forbidden": (
        "error: my-server auth denied (403) — this project's iam is not the owner on that server.\n"
        "  check: config(action='whoami') · re-login: uvx llre login"
    ),
    "err_snapshot_fetch_failed": "error: backend snapshot fetch failed — {url}{cause}",
    "err_revoked": "error: server-side publication revoked (410) — nothing to restore",
    "err_no_identity": "error: no iam for '{label}' — check with config(action='whoami')",
    "err_backend_unreachable": "backend access failed — {url}{cause}",


    "restore_header": "[{label}] pull restored {count} (lore {lore} + doc {doc})",
    "restore_updated": "  updated {count} (server copy is newer — local replaced)",
    "restore_skipped": "  skipped {count} (local is newer/same)",
    "conflict_prefix": "  ⚠️ conflicts {count} (both server and local changed since the last push — local kept): ",
    "conflict_more": " and more",
    "conflict_suffix": " · to make local the source of truth, run push(id=...)",
    "not_found_header": "  not on server {count}: {ids}",


    "push_desc": (
        "[my server] push(id) — upload the home base to **my server** (visible to me only). Like git push: local → server.\n"
        "Not for sharing — sharing to others (an openbox) is openbox(action='push'), not push"
        " (push has no target argument by design, so it cannot share).\n"
        "\n"
        "- push()            the whole home base → server\n"
        "- push(id='lr-x'|'dc-x')   a single item\n"
        "- push(id=['lr-x','dc-y'])  a batch\n"
        "Take down (inverse): rm(sent='lr-x'|'dc-x') — removes my server copy only, home base untouched.\n"
        "(moving items between local workspaces is local(), not push())\n"
    ),
    "push_help": (
        "[my server] push — home base → my server (visible to me only, like git push)\n"
        "\n"
        "  push()            the whole home base\n"
        "  push(id='lr-x'|'dc-x')   a single item / push(id=['lr-x','dc-y']) a batch\n"
        "  Not sharing (sharing to an openbox = openbox(action='push')). Restore = pull. Take down from my server = rm(sent='lr-x'|'dc-x').\n"
        "  (moving items between local workspaces is local(), not push())"
    ),
    "auto_connect_new_push": "⚠️ no connection found, auto-connected — a new space was created.\n",
    "auto_connect": "⚠️ no connection found, auto-connected.\n",
    "push_empty": "[{label}] home base is empty — nothing to upload",
    "push_up_to_date": "[{label}] already up to date — nothing to push",
    "err_reconnect_failed": "error: the project is not on the server — reconnect attempt failed.\n",
    "err_reconnect_retry_failed": "error: the project is not on the server — reconnected but the retry also failed (404).",
    "healed_new_space": "⚠️ not found on the server — uploaded to a new space.\n",
    "reauth_success": "⚠️ session expired — reauthenticated.\n",


    "push_result_header": "[{label}] {verb} {count} (lore {lore} + doc {doc})",
    "push_not_found_header": "  not in the home base {count}: {ids}",
    "push_errors_header": "  {count} failed:",
    "unpush_header": "[{label}] {verb} {count}",
    "unpush_unknown_header": "  unrecognized id prefix (lr-/dc-) {count}: {ids}",
    "unpush_errors_header": "  {count} failed:",
    "unpush_404_openbox_hint": (
        "  → if '{id}' only exists in an openbox, try: openbox(action='rm', id='{id}')"
    ),


    "pull_desc": (
        "[my server] pull(id) — restore the home base from my server (works across devices too). Like git pull: server → local.\n"
        "Bringing things from an openbox is openbox(action='pull'), not pull — pull is for my server only.\n"
        "If local is newer/same it's skipped; a real conflict (both sides changed) is shown separately (local kept).\n"
        "\n"
        "- pull()            my whole server → home base\n"
        "- pull(id='lr-x'|'dc-x')   restore a selection\n"
        "(moving items between local workspaces is local(), not pull())\n"
    ),
    "pull_help": (
        "[my server] pull — my server → home base restore (like git pull)\n"
        "\n"
        "  pull()            everything / pull(id='lr-x'|'dc-x') a selection\n"
        "  Conflict: if local is newer/same it's skipped (no overwrite).\n"
        "  A real conflict (both sides changed) is shown separately with ⚠️ (local kept) — run push(id=...) to confirm.\n"
        "  Getting openbox footprints = openbox(action='pull').\n"
        "  (moving items between local workspaces is local(), not pull())"
    ),
    "auto_connect_new_pull": (
        "⚠️ no connection found, auto-connected — a new space was created"
        " (there may be nothing to restore on the server).\n"
    ),


    "backup_nudge": "(personal backup to my server — to share to an openbox, use openbox(action='push'))",
}
