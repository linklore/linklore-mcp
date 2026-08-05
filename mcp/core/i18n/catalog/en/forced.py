"""English (en) messages for the 'forced' surface."""
MESSAGES: dict[str, str] = {


    "tool_desc": (
        "Executes the exact destructive action described in a warning printed by "
        "rm(), local_cross(), config(), or openbox() — copy the values from that "
        "warning verbatim. Do not call this on your own initiative; only call it "
        "after seeing a warning that names it and tells you exactly what to pass."
    ),
    "help": (
        "forced — the sole execution point for a destructive-action warning from "
        "rm() / local_cross() / config() / openbox(). Copy the values printed in "
        "that warning verbatim — do not decide to call this yourself.\n\n"
        "action='rm'           id=<item(s) to permanently delete>\n"
        "  -> the id from rm(force=True)'s warning, unchanged.\n\n"
        "action='local_cross'  mode='move'|'copy', id=<item(s)>, to=<target path>, from_dir=<source path>\n"
        "  -> the values from local_cross()'s multi-item warning, unchanged. mode= "
        "is local_cross()'s own action= renamed (to avoid clashing with forced's "
        "own action=).\n\n"
        "action='config'       delete_project=<prj_id>  OR  sessions_revoke_all=True\n"
        "  -> the value from config()'s warning, unchanged. Exactly one of the two.\n\n"
        "action='openbox'      delete=<pid> | leave=<pid> | transfer=<member id>(+pid=) | "
        "rm_member=<member id(s)>(+pid=) | push=<item id(s)>(+pid=, name= optional)\n"
        "  -> the value from openbox()'s warning, unchanged. Exactly one of the "
        "five — transfer=/rm_member=/push= also need pid= naming the target box "
        "(delete=/leave= don't, their own value already is the pid).\n\n"
        "the 9 combinations:\n"
        "  rm            id=\n"
        "  local_cross   mode= id= to= from_dir=\n"
        "  config        delete_project=\n"
        "  config        sessions_revoke_all=True\n"
        "  openbox       delete=\n"
        "  openbox       leave=\n"
        "  openbox       transfer= pid=\n"
        "  openbox       rm_member= pid=\n"
        "  openbox       push= pid= (name= optional)"
    ),
    "err_action_invalid": "error: action='{action}' not supported — one of {valid}",
    "err_fields_missing": "error: could not determine which operation — valid fields for {action}: {fields}",
    "err_pid_required": "error: action='openbox', {field}= also needs pid= (the target box)",
    "err_box_not_found": "error: no box in the address book matches pid='{pid}' — it may have been unregistered since the warning was shown",
}
