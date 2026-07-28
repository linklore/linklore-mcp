"""English (en) messages for the 'report' surface."""
MESSAGES: dict[str, str] = {
    "tool_desc": (
        "report(msg) — send feedback/a bug straight to the team. Works whether or not "
        "you're logged in (if logged in, your iam is attached automatically — never forced)."
    ),
    "help": (
        "report(msg)\n"
        "  Send feedback/a bug straight to the team — works anonymously too (no login needed).\n"
        "  - msg: what to send (required)\n"
        "  If you're logged in, your iam is attached automatically for easier "
        "follow-up — never forced."
    ),
    "err_msg_required": "error: msg is required — write what you want to send (e.g. report(msg='...'))",
    "err_failed": "error: send failed ({code}) — {resp}",
    "success": "feedback sent — thanks for letting us know 🙏",
}
