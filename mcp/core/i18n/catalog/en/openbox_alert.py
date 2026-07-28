"""English (en) messages for the 'openbox_alert' surface."""
MESSAGES: dict[str, str] = {


    "stale_alert": (
        "🔔 openbox change detected (as of up to 60s ago): {display} → {cmd_hint}\n"
        "   (brief() auto-receives this — may already be up to date)\n\n"
    ),

    "label_first_pull_needed": "{name} (needs first pull)",
}
