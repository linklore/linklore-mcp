"""English (en) messages for the 'openbox' surface."""
MESSAGES: dict[str, str] = {
    "identity_birth_warning": (
        "⚠️ project iam born — from now on, this project's server backup/sharing belongs to this iam.\n"
        "  saved: remote/iam.json\n"
    ),


    "identity_cleared_warning": (
        "⚠️ project iam cleared — it was issued by this box. This project now acts as the account.\n"
    ),
    "err_openbox_not_registered": (
        "error: openbox '{who}' is not registered.\n"
        "  create: openbox(name='{name_label}', action='new', display_name='me')\n"
        "  join: openbox(action='join', code='<invite-code>', display_name='me')\n"
        "  dock an existing membership: openbox(name='{name_label}', action='docking')"
    ),
    "err_member_id_required": "error: member= is required (nickname or email) — check members: openbox(name='{ob}', action='list')",
    "member_not_found": "error: member '{ref}' not found — check members: openbox(name='{ob}', action='list')",
    "member_hint_close": "\n  did you mean: {items}",
    "member_ambiguous_header": "error: nickname '{ref}' matches multiple members — which one? (no auto-pick)",
    "member_ambiguous_item": "  {n}. {display} ({role}) {detail} → {cmd}",
    "candidates_more": "  … +{n} more",
    "name_auto_placeholder": "(auto)",
    "name_placeholder": "name",
    "openbox_name_placeholder": "<openbox-name>",


    "list_boxes_empty": (
        "no openbox registered — create: openbox(name='<name>', action='new', display_name='me') · "
        "join: openbox(action='join', code='<invite-code>', display_name='me')"
    ),
    "list_boxes_header": "{count} registered openbox(es):",
    "list_boxes_hint": "specify an action: openbox(name='<box>', action='docking'|'show'|'list'|...) · full usage: help=True",


    "init_help": (
        "openbox(name='<name>', action='new', display_name='me')\n"
        "  Create a new openbox — you become owner.\n"
        "  - name: box name (registered as-is — no local alias)\n"
        "  - display_name: your member name (shown to other members)\n"
        "  Access = membership (invite-only) — no public/private flag.\n"
        "  Result: backend project_id + owner registration → remote/openbox/openbox.json"
    ),
    "err_name_required": "error: name is required",
    "err_display_name_required": "error: display_name is required",
    "init_err_backend_failed": "error: backend init failed ({code}) — {resp}",
    "init_success": (
        "[{name}] openbox created — owner={display_name}\n"
        "  project_id: {pid}\n"
        "  access: membership (invite-only)\n"
        "next: openbox(name='{name}', action='invite') to invite members"
    ),


    "edit_err_no_fields": (
        "error: action='edit' requires at least one of description=/title=/display_name= — "
        "supported fields: description(box description, owner/member) · title(box name, owner only) · "
        "display_name(your nickname, anyone)\n"
        "  example: openbox(name='{name}', action='edit', description='...')"
    ),
    "edit_err_failed": "error: edit failed ({code}) — {resp}",
    "edit_done": "[{name}] description updated — \"{description}\"",
    "edit_title_done": "[{name}] box name updated — \"{title}\"",
    "edit_title_err_forbidden": "error: changing the box name (title) requires owner — it's the identity this server matches on docking, so only the owner may change it",
    "edit_display_name_done": "[{name}] your nickname updated — \"{display_name}\"",
    "edit_display_name_err_conflict": "error: nickname '{display_name}' is already taken in [{name}] — retry with a different nickname",


    "invite_help": (
        "openbox(name='<box>', action='invite', role='member', kind='member', expires_h=24)\n"
        "  Issue an invite code. Owner only.\n"
        "  - role='owner' is also possible (transfer is preferred)\n"
        "  - kind='project' — invite a project as a member (the other repo joins)\n"
        "  - member='<nickname>' — reissue invite (targets an existing project iam, rotates the session)\n"
        "  - defaults to 24h, single use"
    ),
    "invite_err_bad_role": "error: role must be one of viewer / member / owner (got: '{role}')",
    "invite_err_bad_kind": "error: kind must be one of member / project (got: '{kind}')",
    "invite_err_failed": "error: invite failed ({code}) — {resp}",
    "invite_join_hint_reissue": "reissued invite — install with openbox(action='join', code='{code}') on the project",
    "invite_join_hint_project": "on the other project: openbox(action='join', code='{code}', display_name='<project-name>')",
    "invite_join_hint_member": "share: send the invite_code to the member → openbox(action='join', code='{code}', display_name='...')",
    "invite_issued_header": "[{name}] invite issued{suffix}\n",
    "invite_project_suffix": " (project member)",
    "invite_owner_role_warning": (
        "⚠️ owner-role invite — once this code is consumed, owner privileges are granted immediately (transfer is preferred).\n"
    ),


    "openbox_join_help": (
        "openbox(action='join', code='<invite-code>', display_name='me')\n"
        "  Join an openbox with an invite code.\n"
        "  - authenticated as iam (env>project iam>account) — no per-box token\n"
        "  - consuming a kind='project' invite may give birth to an iam for this project (loud warning)\n"
        "  - the box name is registered exactly as the backend project name (no local alias)"
    ),
    "err_invite_code_required": "error: code is required (invite code)",
    "err_invite_login_required": (
        "error: this invite requires login — a browser login was attempted but not completed.\n"
        "  try again, or: uvx llre login"
    ),
    "err_auth_url_hint": "\n  if the browser didn't open, open it directly: {url}",
    "join_err_409": "error: join failed (409) — {resp}",
    "join_err_generic": "error: join failed ({code}) — {resp}",
    "openbox_join_success": (
        "[{project_name}] joined openbox — {display_name} ({role})\n"
        "  project_id: {pid}\n"
        "next: openbox(name='{project_name}', action='show') to browse the box\n"
        "  absorb: openbox(name='{project_name}', action='pull', id='...')"
    ),


    "list_help": (
        "openbox(name='<box>', action='list') — member list: nickname + (for people) email + role + last_push_at.\n"
        "  members are referred to by nickname/email as-is — use for the member= argument of "
        "openbox(action='role'/'transfer'/'rm')."
    ),
    "list_err_failed": "error: list failed ({code}) — {resp}",
    "list_header": "[{name}]  ({count} members)",
    "list_project_tag": " [project]",


    "rm_member_help": (
        "openbox(name='<box>', action='rm', member='<nickname or email>')\n"
        "  Owner removes a member. Revokes the token. Unrecoverable — only runs via the\n"
        "  forced(action='openbox', rm_member=..., pid=...) call the first response prints.\n"
        "  The removed member's lore data stays in the box (option a).\n"
        "  member= also accepts a list (batch) — each result is reported separately, no full rollback on partial failure."
    ),
    "rm_member_desc": "remove member(s) — {name}: {members}",
    "rm_member_confirm": (
        "⚠️ [{name}] remove member(s): {members} — revokes their token (lore data stays).\n"
        "  run: forced(action='openbox', rm_member={ids}, pid='{prj_id}')\n"
    ),
    "remove_err_failed": "error: member removal failed ({code}) — {resp}",
    "remove_done": "[{name}] removed member {member_id} — token revoked. lore data remains.",


    "role_help": (
        "openbox(name='<box>', action='role', member='<nickname or email>', role='viewer')\n"
        "  Owner changes a member's role — role='viewer'(read-only) | 'member'(read-write).\n"
        "  Cannot set owner (use transfer instead). Cannot target yourself/owner."
    ),
    "role_err_bad_value": "error: role must be 'viewer'(read-only) or 'member'(read-write)",
    "role_err_failed": "error: role change failed ({code}) — {resp}",
    "role_label_viewer": "viewer (read-only)",
    "role_label_member": "member (read-write)",
    "role_changed": "[{name}] member {member_id} → {label}",


    "docking_help": (
        "openbox(name='team-prj', action='docking')\n"
        "  Dock an openbox you're already a member of to this project **by name** — a box is\n"
        "  only visible from projects it is docked to.\n"
        "  - looks up my memberships with the account token, matches the name → wires it exactly as-is (no local alias)\n"
        "  - if 2+ boxes share the name, shows candidates (name·prj-id·member count) and stops — confirm with project_id='prj-xxxxxxxx'\n"
        "  - auth = account iam (login). Token is not stored. url= is retired.\n"
        "  - project-kind cannot dock (a project iam is bound to the project it was born in via join).\n"
        "  - first join (with an invite code) is openbox(action='join', code=). Undo the wiring: openbox(name='<name>', action='undocking')."
    ),
    "docking_err_url_retired": (
        "error: url= is retired — docking now goes by box **name**:\n"
        "  openbox(name='{name}', action='docking')\n"
        "  if several boxes share the name, candidates plus a project_id='prj-xxxxxxxx' confirm command are shown."
    ),
    "docking_nudge_pid_looks_name": (
        "'{value}' — that landed in project_id= but looks like a name (not prj-xxxxxxxx or a full UUID). is this right?\n"
        "  1. dock by this name: {cmd}\n"
        "  2. to pass a prj-id, check first: config(action='projects') or config(action='sources')"
    ),
    "docking_nudge_name_looks_prj": (
        "'{name}' — that landed in name= but looks like a prj-id. is this right? (nothing was run)\n"
        "  1. dock by this id: {cmd}\n"
        "  2. if this string really is a box name: {results}"
    ),
    "docking_nudge_name_results": "{count} of my memberships share this name — re-calling openbox(action='docking', name=...) will not treat it as a name, use option 1 above",
    "docking_nudge_name_no_results": "no box with this name among my memberships",
    "docking_err_ref_not_found": "error: no project matches '{ref}' — not in the address book or my memberships. check: config(action='projects')",
    "docking_ref_ambiguous_header": "error: '{ref}' matches multiple projects — which one? (no auto-pick)",
    "docking_candidate_ref_item": "  {n}. {label} ({prj}) → {cmd}",
    "docking_err_name_not_found": "error: no box named '{name}' among my memberships — if you have an invite code: openbox(action='join', code='...')",
    "docking_hint_close_names": "\n  did you mean: {items}",
    "docking_err_name_not_box": "error: '{name}' is not an openbox (personal space) — personal backup is push()/pull() (no docking needed)",
    "docking_ambiguous_header": "{count} boxes are named '{name}' — which one? (nothing was wired)",
    "docking_ambiguous_item": "  {n}. {name} ({prj}) {count} members → {cmd}",
    "docking_err_project_kind": (
        "error: a project-kind iam cannot dock — this project acts as a project iam"
        "(remote/iam.json), and an iam is bound to the box it was born into via join.\n"
        "  if you need this box: ask the owner for a kind='project' invite → "
        "openbox(action='join', code='...', display_name='...')"
    ),
    "docking_err_no_url": "error: url is required (openbox address https://.../api/projects/<project_id>)",
    "docking_err_bad_url": "error: url must be a backend openbox address (e.g. https://api.linklore.io/api/projects/<pid>)",
    "docking_err_login_required": "error: login required — retry after `uvx llre login` (docking authenticates as your account iam)",
    "docking_err_connect_failed": "error: could not reach the openbox ({body}) — check the address/network",
    "docking_err_not_member": (
        "error: not a member of this openbox (or the token expired).\n"
        "  if you have an invite code: openbox(action='join', code='...').\n"
        "  if the login expired: `uvx llre login`."
    ),
    "docking_err_not_found": "error: openbox not found — check the project_id in the URL",
    "docking_err_unexpected": "error: unexpected response ({status}) — {body}",
    "err_generic": "error: {error}",


    "err_max": "error: {err}",


    "register_err_url_not_ascii": (
        "error: url contains non-ASCII characters — copy the box address exactly and retry\n"
        "  (a backend address is ASCII only, e.g. https://api.linklore.io/api/projects/<pid>)"
    ),
    "register_err_alias_taken": (
        "error: the name '{name}' is already wired to another box ({pid}) —\n"
        "  use a different name, or unwire it first: openbox(name='{name}', action='undocking')"
    ),
    "docking_success": (
        "[{name}] docked — {prj} ({count} members)\n"
        "  auth: account iam (token not stored, membership verified)\n"
        "  browse: openbox(name='{name}', action='show', query='...') · absorb: openbox(name='{name}', action='pull', id='...')"
    ),


    "docking_rewired": (
        "⚠️ this box was already docked as '{old}' — it is now updated to '{new}'.\n"
    ),


    "undocking_help": (
        "openbox(name='<name>', action='undocking')\n"
        "  Remove only this project's address-book wiring — server membership is untouched\n"
        "  (leaving is openbox(name='<name>', action='leave')).\n"
        "  Cleans up local registrations left by docking/join (registry.json · openbox.json)."
    ),
    "undocking_done": (
        "[{name}] undocked — wiring removed from this project (server membership unchanged).\n"
        "  if you meant to leave: openbox(name='{name}', action='leave')"
    ),


    "transfer_help": (
        "openbox(name='<box>', action='transfer', member='<new owner nickname or email>')\n"
        "  Transfer owner rights. You are demoted to member. Unrecoverable — only runs via the\n"
        "  forced(action='openbox', transfer=..., pid=...) call the first response prints."
    ),
    "transfer_desc": "transfer owner — {name} -> {member}",
    "transfer_confirm": (
        "⚠️ transfer owner of [{name}] to {member_id} — you will be demoted to member and\n"
        "  the new owner must transfer it back to undo this.\n"
        "  run: forced(action='openbox', transfer='{resolved}', pid='{prj_id}')\n"
    ),
    "transfer_err_failed": "error: transfer failed ({code}) — {resp}",
    "transfer_done": "[{name}] owner → member ({member_id})\n  you are now a member.",


    "leave_help": (
        "openbox(name='<box>', action='leave')\n"
        "  Leave an openbox yourself — deletes your membership + cleans up the local\n"
        "  registration (the reverse of join).\n"
        "  Owner cannot leave — transfer ownership first with openbox(name='<box>', action='transfer', member='<id>').\n"
        "  To remove only the wiring (keep membership): openbox(name='<box>', action='undocking')."
    ),
    "leave_desc": "leave — {name}",
    "leave_confirm": (
        "⚠️ leave openbox '{name}'? You can't come back without a new invite.\n"
        "  run: forced(action='openbox', leave='{prj_id}')\n"
    ),
    "leave_confirm_owner_hint": (
        "⚠️ leave openbox '{name}'? You can't come back without a new invite.\n"
        "  ℹ️ Local records suggest you are this box's owner — if so, the server will reject this (owners can't\n"
        "     leave; if you already transferred it, ignore this hint — local records can lag).\n"
        "  1. try anyway: forced(action='openbox', leave='{prj_id}')\n"
        "  2. alternative (this is the real fix if you're owner): "
        "openbox(name='{name}', action='transfer', member='<new owner nickname>')"
    ),
    "leave_err_owner_409": (
        "error: the owner of '{name}' cannot leave — transfer ownership first:\n"
        "  openbox(name='{name}', action='transfer', member='<new owner nickname>')"
    ),
    "leave_err_not_member": "error: not a member of '{name}' — check with openbox(name='{name}', action='list')",
    "leave_err_failed": "error: leave failed ({code}) — {resp}",
    "leave_done": "[{name}] left — local registration cleaned up.",


    "err_name_required_target": "error: name= is required — the target openbox name (e.g. openbox(name='team-prj', action='{action}', ...))",
    "push_err_no_id": "error: id= is required — footprints to share (e.g. id='lr-x' or id=['lr-a', 'dc-b'])",
    "push_verb": "push(shared)",
    "push_preview_header": "[{name}] push preview — {count} items (nothing sent yet)",
    "push_preview_missing": "  ⚠️ not in this project: {ids}",
    "push_desc": "push {count} items — {name}",
    "push_forced_hint": "  run: forced(action='openbox', push={ids}, pid='{pid}')",
    "pull_err_no_id": "error: id= is required — footprint ids to absorb. To browse/refresh the cache only: openbox(name='{name}', action='show')",
    "pull_header": "[{name}] pulled {count} items — absorbed with new ids (provenance kept)",
    "pull_more": "  ... and {count} more",
    "pull_errors_header": "  {count} failed:",
    "rm_ids_err_no_id": "error: id= is required — footprint ids to remove from the openbox (ones I shared to this box)",
    "rm_ids_verb": "removed from openbox",
    "show_refresh_failed": "⚠️ cache refresh failed — showing the last cache ({cause})",

    "show_with_docs": "{lore_part}\n\n{doc_part}",


    "rm_err_no_args": "error: id= or member= is required — id= takes back something you shared, member= removes a member (exactly one)",
    "rm_err_both_args": "error: id= and member= can't both be given — id= takes back something you shared, member= removes a member (exactly one)",


    "tool_desc": (
        "openbox(name, action) — the owner wall: every exchange with other owners (share, absorb, membership) goes through this single gate. "
        "An openbox is an invite-only shared box. Your own server backup is push()/pull() (no target argument — never crosses the wall). "
        "Moving or copying into another LOCAL project you also own (same disk, no server round-trip) goes through local_cross(), not openbox — "
        "lighter and faster when ownership isn't in question.\n"
        "\n"
        "transport:\n"
        "- openbox(name='team-prj', action='push', id='lr-x')     share footprints to the box — sends copies, your project unchanged. 2+ ids: preview first, re-call with forced(action='openbox', push=...)\n"
        "- openbox(name='team-prj', action='pull', id='lr-x')     absorb the box's footprints into your project — new id + provenance\n"
        "- openbox(name='team-prj', action='rm', id='lr-x')       remove what I shared from the box (your project unchanged)\n"
        "browse:\n"
        "- openbox(name='team-prj', action='show', query='auth')  browse the box — cache auto-refreshes on call (filters: query·tag·max·oneline)\n"
        "governance:\n"
        "- openbox(name='team-prj', action='new', display_name='me')          create a box (you = owner)\n"
        "- openbox(name='team-prj', action='edit', description='...')         update the box description (owner/member) · title=box name(owner only) · display_name=your nickname(anyone)\n"
        "- openbox(name='team-prj', action='invite', role='member')           invite code (owner). kind='project' = project member, member='<nickname>' = reissue\n"
        "- openbox(action='join', code='X', display_name='me')   join with an invite code (box name = backend project name, no local alias)\n"
        "- openbox(name='team-prj', action='docking')                         dock a membership to this project by name — 2+ boxes with the name: candidates + project_id='prj-...' confirm. project-kind cannot dock\n"
        "- openbox(name='team-prj', action='undocking')                       remove only this project's wiring — server membership unchanged (leaving is leave)\n"
        "- 'list' members · 'role' member=+role= · 'transfer' member= (double confirm) · 'leave' (double confirm) · 'rm' member='<nickname/email>' to expel a member (owner) · 'delete' whole box (owner, double confirm)\n"
        "(member= refers to members by nickname or email — no ids. action grammar: sustained-connection procedures = -ing (docking/undocking), immediate commands = bare verb. rm(id=)=take back a shared entry, rm(member=)=expel a member — exactly one)\n"
    ),
    "help": (
        "openbox(name, action) — the owner wall (an openbox is an invite-only shared box)\n"
        "transport/browse:\n"
        "  push      openbox(name='team-prj', action='push', id='lr-x')             share to the box (copies, your project unchanged; 2+ ids: preview→forced(action='openbox', push=...))\n"
        "  pull      openbox(name='team-prj', action='pull', id='lr-x')             absorb into your project (new id + provenance)\n"
        "  rm        openbox(name='team-prj', action='rm', id='lr-x')               remove what I shared from the box — or action='rm', member='<nickname/email>' to expel a member (owner). exactly one of id=/member=\n"
        "  show      openbox(name='team-prj', action='show', query='auth')          browse (cache auto-refresh; filters query·tag·max·oneline)\n"
        "governance:\n"
        "  new       openbox(name='team-prj', action='new', display_name='me')      create a box (you = owner)\n"
        "  edit      openbox(name='team-prj', action='edit', description='...')    update description (owner/member) · title=box name(owner only) · display_name=your nickname(anyone)\n"
        "  invite    openbox(name='team-prj', action='invite', role='member')       invite code (kind='project' = project member, member = reissue)\n"
        "  join      openbox(action='join', code='X', display_name='me')  join (box name = backend project name, no local alias)\n"
        "  docking   openbox(name='team-prj', action='docking')                     dock an existing membership by name (2+ with the name: confirm with project_id='prj-...', project-kind cannot)\n"
        "  undocking openbox(name='team-prj', action='undocking')                   remove wiring only (server membership unchanged — leaving is leave)\n"
        "  list      openbox(name='team-prj', action='list')                        member list (nickname·email·role)\n"
        "  role      openbox(name='team-prj', action='role', member='<nickname>', role='viewer')  change role\n"
        "  transfer  openbox(name='team-prj', action='transfer', member='<nickname>')  transfer owner (double confirm)\n"
        "  leave     openbox(name='team-prj', action='leave')                       leave yourself (owner gets 409 — transfer first)\n"
        "  delete    openbox(name='team-prj', action='delete')                      delete the whole box (owner, double confirm)\n"
        "Your own server (backup) is push()/pull() — never crosses the wall. Taking down from your own server is rm(sent=)."
    ),
    "err_invalid_action": "error: action must be one of {valid}. see help=True for usage.",
    "err_param_not_allowed": (
        "error: {params} — not a parameter of the '{action}' action (no silent drop).\n"
        "  '{action}' accepts: {allowed}. see help=True for usage."
    ),
    "err_name_looks_like_action": (
        "error: '{name}' landed in the name= slot (the box name) — the action is the second argument:\n"
        "  openbox(name='<box-name>', action='{name}', ...)\n"
        "  actions that need no name (join) are openbox(action='{name}', ...)."
    ),
}
