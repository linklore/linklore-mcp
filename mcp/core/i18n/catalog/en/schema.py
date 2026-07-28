"""English (en) messages for the 'schema' surface."""
MESSAGES: dict[str, str] = {
    "gen_too_new": (
        "This repository (.linklore) was created by a newer version of LinkLore "
        "(store={db_gen}, this tool={code_gen}) — please update your LinkLore tool "
        "to the latest version."
    ),
    "gen_too_old": (
        "This repository (.linklore) is on an older schema generation "
        "(store={db_gen}, this tool={code_gen}) — an upgrade is required. "
        "No automatic upgrade tool exists yet — let us know via "
        "report(msg='schema upgrade needed: store gen {db_gen}, tool gen {code_gen}') (report always works past this gate, no login required)."
    ),
}
