"""English (en) messages for the 'app' surface."""
MESSAGES: dict[str, str] = {


    "instructions": (
        "AI-native structured memory for agents — lore (decisions, pitfalls, journal) "
        "and doc (specs, plans) that you read and write directly, linked to code files. "
        "Built for agents, not humans — every tool here is designed for usability by an "
        "AI, not readability for a person. "
        "Call brief() first in every session for a dashboard of open items and recent "
        "activity. Not set up yet? Call init(). Full self-contained guide: "
        "show(tag='guide')."
    ),


    "err_generic": "error: {name} failed — {err_type}: {err_msg}{hint}",


    "hint_str_attr": "\n💡 argument is a string but was processed as list/dict. Check the list form (e.g. tags=['a','b'])",
    "hint_list_attr": "\n💡 argument is a list but was processed as a string. Check the tool docstring (help=True)",
    "hint_arg_shape": "\n💡 argument shape mismatch or missing. Check the tool docstring (help=True)",
    "hint_keychain": "\n💡 rerun `uvx llre login` or allow Keychain access",

    "err_empty_response": (
        "⚠️ internal error: {name} returned an empty response "
        "(tool bug — please report(msg='{name} empty response: <repro args>'))"
    ),
}
