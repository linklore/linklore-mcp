"""English (en) messages for the 'app' surface."""
MESSAGES: dict[str, str] = {


    "instructions": (
        "Every tool here is designed solely for agents. "
        "It manages tags, status, and links on top of lore (records that carry across "
        "sessions) and doc (the higher-level unit that groups lore — specs, plans). "
        "Call brief() at the start of every session to save search tokens. "
        "Not set up yet? Call init(). "
        "Data lives in each folder's .linklore/ — one at a parent folder, or one per "
        "subfolder. "
        "ToolSearch matches English only.\n\n"
        "Tools (23) — unsure a name matches? look it up directly: ToolSearch(\"select:<name>\")\n"
        "  add           create a lore/doc record\n"
        "  show          query/search — the main lookup tool\n"
        "  edit          modify an existing record\n"
        "  openbox       share across owners — invite, push, pull, members\n"
        "  local_cross   same-disk, same-owner move/copy/view (no server involved)\n"
        "  report        send feedback/a bug report directly\n"
        "  others: (record) link|unlink|rm|restore  (inspect) brief|log|status|doctor|cleanup\n"
        "          (docs) doc_flow|doc_rollup|doc_map  (server) push|pull|market  (settings) config|init"
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
