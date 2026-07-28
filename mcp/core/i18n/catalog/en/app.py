"""English (en) messages for the 'app' surface."""
MESSAGES: dict[str, str] = {


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
