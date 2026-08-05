"""Official guide content - source for seed packs and GUIDE.md."""
GUIDE_VERSION = "2026.08.03.1"

ITEMS = [

    {
        "kind": "doc",
        "key": "getting-started",
        "title": "Getting Started",
        "body": (
            "## Install\n\n"
            "LinkLore ships as the PyPI package `llre` — no separate clone needed.\n\n"
            "```bash\n"
            "uvx llre               # MCP server for AI tools (stdio, no args)\n"
            "uvx llre login         # Google login (browser) — needed for personal backup/team sharing\n"
            "```\n\n"
            "Embedding search is an optional extra: `uvx --from 'llre[embed]' llre` (fastembed + numpy).\n\n"
            "Register with an MCP client via `.mcp.json` (or `.cursor/mcp.json`):\n\n"
            "```json\n"
            "{\n"
            '  "mcpServers": {\n'
            '    "llre": { "command": "uvx", "args": ["llre"] }\n'
            "  }\n"
            "}\n"
            "```\n\n"
            "## First session\n\n"
            "1. **`init()`** — if the project has no `.linklore/` yet, this creates the local store. "
            "No login or paid backend required.\n"
            "2. **`brief()`** — call this first, every session. It returns open items, recent activity, "
            "and hotspots in a few hundred tokens — cheaper than reading the codebase cold.\n"
            "3. **`show(file='path')`** — before touching a file, search for decisions or pitfalls "
            "already tied to it.\n"
            "4. **`add(type='lore', ...)` / `add(type='doc', ...)`** — record what you did. After a "
            "decision, fix, or pitfall: `add(type='lore', status='done')`. For a new system "
            "or feature: `add(type='doc', ...)` instead of a standalone `.md` file.\n\n"
            "Logs live at `~/.linklore/mcp.log`."
        ),
        "tags": ["guide", "reference"],
    },
    {
        "kind": "doc",
        "key": "mental-model",
        "title": "Mental Model: lore vs. doc",
        "body": (
            "LinkLore stores two kinds of items in a local `.linklore/` store (SQLite, no account "
            "required).\n\n"
            "## lore (`lr-` ids)\n\n"
            "Decisions, pitfalls, fixes, local rules — a journal entry, not a spec. One field carries "
            "meaning beyond the body:\n\n"
            "**status** (lifecycle tag, lore and doc share this):\n"
            "- `open` (default) — alive\n"
            "- `done` — finished, still searchable\n"
            "- `dropped` — discarded, reason kept, still searchable\n"
            "- `rule` — a fixed baseline that doesn't expire\n\n"
            "None of these delete anything — `done`/`dropped`/`rule` keep showing up in search. A "
            "\"dropped with a replacement\" (superseded) is the one case that's auto-hidden from "
            "default search, and only because a `link(action='supersede')` points at what replaced "
            "it.\n\n"
            "## doc (`dc-` ids)\n\n"
            "Specs and system documentation — a living reference, not a snapshot. Progress is "
            "tracked with checklist items and `status` instead.\n\n"
            "## The link\n\n"
            "lore and doc link bidirectionally (`link()`), and both can attach to files. "
            "`show(file='path')` surfaces whichever lore and docs are tied to the file you're about "
            "to edit — that's the mechanism that turns memory into code context instead of a drawer "
            "of notes."
        ),
        "tags": ["guide", "reference"],
    },
    {
        "kind": "doc",
        "key": "team-flow",
        "title": "The Three Zones: Home Base, My Server, and Openboxes",
        "body": (
            "Every tool that touches data lives in exactly one of three zones, split by who owns "
            "the data. Three rules cover all of it: home-base tools never reach outside. Someone "
            "else's world is always behind the `openbox()` gate. Moving things is push/pull (my "
            "server) or openbox (sharing).\n\n"
            "In tool descriptions the zones are marked `[my server]` (push/pull) and `[openbox]` "
            "(openbox); home-base tools carry no marker.\n\n"
            "## 🏠 Home base — this project's own store\n\n"
            "`add`, `edit`, `show`, `rm`, `link`, `log`, ... operate only on the local "
            "`.linklore/` store of the current project. None of them takes a cross-owner "
            "argument — `show()` has no `openbox=` parameter; browsing a shared box is "
            "`openbox(name='team-prj', action='show')`.\n\n"
            "## 🧭 My server — personal backup ([my server])\n\n"
            "Like `git push`/`git pull` against a remote only you can see. There's no target "
            "argument, so sharing this way is structurally impossible.\n\n"
            "- `push()` — upload the home base to your own server space (visible to you only)\n"
            "- `push(id='lr-x')` / `push(id=[...])` — a single item or a batch\n"
            "- `pull()` — restore from your server (works across devices too)\n"
            "- `rm(sent='lr-x')` — take an item down from your server copy (the local original "
            "stays)\n"
            "- If local is newer/same, `pull` skips it; a real conflict (both sides changed) is "
            "shown separately and local is kept — run `push(id=...)` to make local the source of "
            "truth.\n\n"
            "## 🌐 Other owners — one gate: openbox(name, action)\n\n"
            "An openbox is a project's shared, invite-only space (not \"public\"). Every operation "
            "that crosses into someone else's world goes through `openbox(name=..., action=...)` — "
            "the box name is the namespace, so the same verb can never land in the wrong world.\n\n"
            "**Transport**\n\n"
            "- `openbox(name='team-prj', action='push', id='lr-x')` — share a copy into the box "
            "(the original never changes). A batch (`id=[...]`) previews by default — call again "
            "with `confirm=True` to execute; a single item runs immediately.\n"
            "- `openbox(name='team-prj', action='pull', id='lr-x')` — bring a box item into the "
            "home base (new local id, provenance tracked).\n"
            "- `openbox(name='team-prj', action='rm', id='lr-x')` — take back an item you "
            "shared earlier (exactly one of `id=`/`member=` — `member=` on this same action "
            "expels a member instead, see Governance below).\n\n"
            "`push()`/`pull()` and `openbox('push')`/`openbox('pull')` share verbs on purpose — "
            "like `git push origin` vs. `git push fork`, you name the remote, you don't change "
            "the verb.\n\n"
            "**Browse**\n\n"
            "- `openbox(name='team-prj', action='show', query=...)` — look around a box (filters: "
            "`query`, `tag`, `max`, `oneline`; the local cache refreshes automatically). Skim, "
            "pick, `pull` — deep analysis belongs in the home base after pulling.\n\n"
            "**Governance** — `new`, `invite`, `join`, `docking`, `undocking`, `list`, `role`, "
            "`transfer`, `leave`, `rm` (member=), `delete`:\n\n"
            "- `openbox(name='team-prj', action='new')` creates a box, `action='invite'` issues a "
            "code (`expires_h=` optional), `openbox(action='join', code=...)` joins with one.\n"
            "- `docking` wires a membership you already hold to *this* project "
            "(`openbox(name='team-prj', action='docking', url=...)`) — a box is only visible from "
            "projects it's docked to. `undocking` removes just that wiring; quitting the box "
            "itself is `leave`. Naming rule: actions that create or remove a standing connection "
            "are -ing forms (docking/undocking, like Bluetooth pairing); one-shot commands stay "
            "bare verbs (push, join, leave, rm).\n"
            "- `role` (`member=`, `role=`) switches someone between `viewer` and `member` "
            "(owner-only), `transfer` (`member=`) hands off ownership, `rm` (`member=`) removes a "
            "member (the same action as taking back a shared item — argument picks the branch), "
            "`delete` removes the whole box. `transfer` and `delete` are permanent — both "
            "ask for a second, identical call to confirm.\n\n"
            "## local_cross — operating on another local workspace directly\n\n"
            "`local_cross(action, id, to='workspace-path')` operates on a sibling local `.linklore/` "
            "store on the same disk — three actions:\n\n"
            "- `local_cross(action='move', id='lr-x', to='/path')` — relocate an item, preserving fields "
            "like `createdAt`, `files`, `tags`, `status`, and body. The source is "
            "force-deleted, so it's a move, not a copy. For 2+ items it previews by default; call "
            "again with `confirm=True` to execute.\n"
            "- `local_cross(action='copy', id='lr-x', to='/path')` — same fields preserved, but the "
            "source is kept and a new id is issued with provenance recorded (source project + "
            "original id); re-copying the same original is an idempotent skip.\n"
            "- `local_cross(action='show', from_dir='/other', query=...)` — read-only lookup into a "
            "sibling workspace, same filters as `show()`; `from_dir` is required.\n\n"
            "**Boundary**: crossing to a server or an openbox is push/pull or `openbox()` — "
            "`local_cross()` never talks to a backend, it only moves data between `.linklore/` stores on "
            "your own disk.\n\n"
            "## config(action='pin') — switching your whole session to another project\n\n"
            "If you want every subsequent tool call in this session (not a single item) to default "
            "to a different project directory, `config(action='pin', dir='/path')` pins it for the "
            "rest of the process (session-only, not written to disk); `config(action='unpin')` "
            "clears it. Reach for `local_cross()` instead when you're moving, copying, or viewing one "
            "specific item rather than switching your whole working context."
        ),
        "tags": ["guide", "reference"],
    },
    {
        "kind": "doc",
        "key": "tool-reference-map",
        "title": "Tool Reference Map",
        "body": (
            "22 tools, grouped by what they do. Call any tool with `help=True` for full usage.\n\n"
            "| Category | Tool | What it does |\n"
            "| --- | --- | --- |\n"
            "| Setup | `init` | Set up `.linklore/` in this directory (optionally from a blueprint) |\n"
            "| Project | `brief` | Project dashboard — call at the start of every session |\n"
            "| Project | `status` | Code↔doc sync drift detection (git-diff based), with acknowledge/reset |\n"
            "| Project | `config` | Project settings, external source options, iam, session pin, "
            "`action='delete_project'` (permanent, `confirm=True` required) |\n"
            "| Diagnostics | `doctor` | Data integrity check; `action='fix'` auto-repairs what it can |\n"
            "| Feedback | `report` | Send feedback/a bug straight to the team — works whether or "
            "not you're logged in |\n"
            "| Record | `add` | Create lore or doc (`type='lore'\\|'doc'`); `items=[{...}]` batch-creates |\n"
            "| Record | `edit` | Modify an item — `action=`: `append`(default, never overwrites)/"
            "`section`(replace one heading)/`overwrite`(full replace)/`supersede`(new id, old head=False) |\n"
            "| Record | `rm` | Delete — trash (recoverable) by default, `force=True` for permanent; "
            "`sent='lr-x'` takes an item down from your server copy |\n"
            "| Record | `restore` | Recover from trash; no `id` lists the trash |\n"
            "| Record | `local_cross` | Operate on a sibling local workspace — `action='move'\\|'copy'\\|'show'` "
            "(move/copy preserve fields; copy keeps the source) |\n"
            "| Search | `show` | Query by id/query-text/tag/status/file/period/`source_id=`; "
            "`action='graph'`(corpus stats) or `action='tags'`(tag list) |\n"
            "| Search | `log` | Change history |\n"
            "| Link | `link` | Connect two items (lore↔lore, doc↔doc, doc↔lore) |\n"
            "| Link | `unlink` | Disconnect (symmetric with `link`) |\n"
            "| Doc view | `doc_flow` | Render a doc's flow chain in order (journey view) |\n"
            "| Doc view | `doc_map` | Overview of the full doc link network |\n"
            "| Doc view | `doc_rollup` | Collect lore linked to a doc into an AI-summary draft — never auto-applied |\n"
            "| Cleanup | `cleanup` | Detect duplicate lore/doc candidates by similarity |\n"
            "| My server | `push` | `[my server]` Back up the home base to your own server space |\n"
            "| My server | `pull` | `[my server]` Restore from your own server space |\n"
            "| Openbox | `openbox` | `[openbox]` Every cross-owner operation behind one gate — "
            "`action=` transport (`push`/`pull`), browse (`show`), governance "
            "(`new`/`invite`/`join`/`docking`/`undocking`/`list`/`role`/`transfer`/`leave`/"
            "`delete`), `rm` (`id=` takes back a shared item, `member=` expels a member — exactly "
            "one) |\n\n"
            "Arguments generally prefer lists (`tags=['a','b']`) — a comma-separated string is "
            "accepted for backwards compatibility."
        ),
        "tags": ["guide", "reference"],
    },

    {
        "kind": "lore",
        "key": "session-start-brief",
        "title": "Call brief() first, every session",
        "body": (
            "`brief()` is a project dashboard: open items, recent activity, and hotspots in a few "
            "hundred tokens. Call it before reading the codebase at large — it's the cheapest way to "
            "load context, and it's meant to run at the start of every session, not just the first "
            "one."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "show-before-touch",
        "title": "Check show(file=...) before touching a file",
        "body": (
            "Before changing code, search `show(file='path')` (or `tag=`/`query=`/`status=`) for "
            "decisions or pitfalls already tied to the area you're about to edit. Reading this first "
            "avoids repeating a mistake someone — or a previous session — already made and recorded."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "capture-decisions-fixes",
        "title": "After a decision or fix, add a lore entry",
        "body": (
            "Once you've made a decision, fixed a bug, or hit a pitfall, "
            "`add(type='lore', status='done')` leaves a regression guard for future sessions — "
            "future search (and `brief`'s recency-ranked picks) surfaces it without you needing "
            "to remember it happened."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "record-the-reason",
        "title": "A dropped item keeps its reason, not just its outcome",
        "body": (
            "`status='dropped'` means discarded, with the reason still visible in search — it's not "
            "the same as silently deleting something. That only works if the reason actually got "
            "written into the entry. A lore item that records the conclusion but not why tends to get "
            "re-litigated later, because nothing about it explains itself on a second read."
        ),
        "tags": ["guide", "lesson"],
    },
    {
        "kind": "lore",
        "key": "doc-not-markdown",
        "title": "New systems get a doc, not a standalone .md file",
        "body": (
            "When documenting a new system or feature, prefer `add(type='doc', ...)` over writing a "
            "plain markdown file. LinkLore docs get automatic bidirectional links and code context "
            "(via `show(file=...)`) that a file sitting in the repo doesn't."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "link-at-creation",
        "title": "Connect related items at creation time",
        "body": (
            "Pass `links=['dc-x', 'lr-y']` in the same `add()` or `edit()` call instead of following "
            "up with a separate `link()` call. Links aren't decoration — a mutual lore↔lore link is "
            "what clustering and the link-graph stats are built from, so a well-linked corpus "
            "searches and clusters better than an unlinked one."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "scope-creep-open",
        "title": "\"That's separate, later\" becomes add(status='open') now",
        "body": (
            "Scope creep during a task — \"that's separate, follow-up\" — should become "
            "`add(type='lore', status='open')` immediately, in the moment you notice it. A commit "
            "message is not a backlog; it won't resurface on its own."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "doc-rollup-is-a-draft",
        "title": "doc_rollup drafts, it doesn't overwrite",
        "body": (
            "`doc_rollup(id='dc-xxx')` collects the lore linked to a doc into a markdown draft for "
            "summarization. It never edits the doc itself. The expected loop is: the AI reads the "
            "draft, proposes a reorganized items list to the user, the user confirms, and only then "
            "does the AI call `edit(id, items=...)`. Never auto-overwrite a doc — it's the project's "
            "source of truth and needs a human judgment call."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "edit-overwrite-is-footgun",
        "title": "edit(action='overwrite') is a full replace, not a patch",
        "body": (
            "The default write mode for `edit()` is append — `msg='...'` alone (or "
            "`action='append'`) adds to the end of the body and keeps everything else. "
            "`action='overwrite'` is different: it fully replaces the body, and tags/items/links "
            "passed in the same call are also fully replaced, not merged. The old body isn't lost "
            "(it's recoverable via `log(id)`), but it's easy to reach for overwrite out of habit and "
            "clobber more than intended. Default to append; reach for overwrite deliberately."
        ),
        "tags": ["guide", "lesson"],
    },
    {
        "kind": "lore",
        "key": "rm-is-soft-by-default",
        "title": "rm() trashes by default — force=True is what's permanent",
        "body": (
            "`rm(id)` moves an item to trash; nothing is actually lost, and `restore(id)` brings it "
            "back. Only `rm(id, force=True)` is unrecoverable. If you're unsure whether something is "
            "still needed, the default (soft) delete is the safe call — you can always clean it up "
            "permanently later."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "push-pull-vs-openbox",
        "title": "push/pull backs up — openbox('push') shares",
        "body": (
            "push/pull moves items between your local home base and your own server space; nobody "
            "else can see it, and there's no target argument on `push`, so sharing that way is "
            "structurally impossible. Sharing goes through the openbox gate: "
            "`openbox(name='team-prj', action='push', id='lr-x')` copies an item into a shared, "
            "invite-only box, and `openbox(name='team-prj', action='pull', id='lr-x')` brings a box "
            "item into your home base (new local id, provenance tracked). Same verbs, different "
            "world — the `name=` is what routes the call, like `git push origin` vs. "
            "`git push fork`. A call that doesn't name a box can't touch one."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "move-is-not-sync",
        "title": "local_cross() relocates/copies locally — it isn't push or openbox('push') in disguise",
        "body": (
            "`local_cross(action='move'|'copy', id, to='workspace-path')` moves or copies a lore/doc "
            "between your own local `.linklore/` stores, preserving fields like `createdAt`, "
            "`files`, `tags`, `status`, and body. `action='move'` force-deletes the "
            "source and preserves the id; `action='copy'` keeps the source and issues a new id — "
            "both record provenance (source project + original id), and re-copying the same "
            "original is an idempotent skip. Neither talks to a server "
            "or an openbox. Getting a copy onto another machine is push/pull; getting it into a "
            "team space is `openbox(action='push')` — neither is local_cross()."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "multi-item-move-previews",
        "title": "Moving or copying 2+ items previews by default",
        "body": (
            "`local_cross(action='move'|'copy', ...)` runs immediately for a single item (low risk), but "
            "for two or more items it defaults to a preview only — nothing executes until you call "
            "it again with `confirm=True`. That asymmetry exists specifically to prevent an "
            "accidental bulk relocation-and-delete."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "irreversible-deletes-confirm-twice",
        "title": "Permanent operations need a deliberate second step",
        "body": (
            "`config(action='delete_project', confirm=True)` permanently deletes your personal "
            "space on the server (all lore/doc/members/invites gone) — the first call, without "
            "`confirm=True`, only shows what would be deleted. `openbox(name='...', "
            "action='delete')` removes an entire shared box, and `openbox(name='...', "
            "action='transfer', member=...)` permanently hands off ownership — for both, the safety "
            "step is calling a second, identical time; the first call only warns. None of these is "
            "the everyday `rm(id)`, which just trashes an item and is recoverable via "
            "`restore(id)`."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "edit-section-and-supersede",
        "title": "edit() has two more write modes: section (partial replace) and supersede (new id)",
        "body": (
            "Beyond append and overwrite, `edit()` has two more `action=` modes. "
            "`action='section', section='heading', msg='...'` replaces just that section and keeps "
            "the rest of the body — the heading must already exist, or it errors (to add a "
            "brand-new section, use the default append instead). `action='supersede', "
            "msg='new conclusion'` creates a new id that inherits title/tags/status from the "
            "old one, and sets the old item's `head` to `False` — the same mechanism "
            "`link(action='supersede')` uses to reconcile a contradiction with an *existing* item, "
            "but here the new item doesn't exist yet."
        ),
        "tags": ["guide", "workflow"],
    },
    {
        "kind": "lore",
        "key": "show-period-and-modes",
        "title": "show() period filter, plus action='graph' and action='tags'",
        "body": (
            "`period=` on `show()`/`log()` takes `'Nh'` (hours), `'Nd'` (days), or `'YYYY-MM-DD'` "
            "(from that date, UTC) — and two dates joined by `..` for a range "
            "(`'2026-07-01..2026-07-08'`). `source_id=` reverse-looks-up an item that came in via "
            "`openbox(action='pull')` by its original external id, for checking whether you "
            "already pulled something. "
            "`action='graph'` returns corpus-wide audit stats (status/tag/body-length/"
            "link-graph distribution), and `action='tags'` lists every tag in use — both read the "
            "whole corpus, not a filtered slice."
        ),
        "tags": ["guide", "reference"],
    },
    {
        "kind": "lore",
        "key": "surfacing-badges-meaning",
        "title": "What the auto-surfaced badges in add()/edit() responses mean",
        "body": (
            "`add()`/`edit()` responses can carry several automatic sections beyond the write "
            "itself — none of them block anything, they're judgment aids attached after the "
            "fact.\n\n"
            "- 🚨 very similar (cos=X.XX) — cosine similarity crossed a high threshold, likely a "
            "duplicate. Check the inline preview instead of opening the item; if it's the same "
            "call, `link(action='supersede')` the older one or `rm(force=True)` it.\n"
            "- ⚠️ conflicting candidates — same topic, but evidence the conclusion points the "
            "opposite way. If it's a real reversal, finalize the new one and "
            "`link(action='supersede')` the old; if both stand, connect them with `links=`/"
            "`link()` instead.\n"
            "- related candidates — suggested only, nothing is connected automatically; use "
            "`links=`/`link()` for the ones worth keeping.\n"
            "- weak candidates — count only (titles aren't listed), since their hit rate is low "
            "and reading them out doesn't pay off; run `cleanup()` to review actual overlaps.\n"
            "- 💡 related doc — a doc overlapping with the lore you just added exists; `link()` it "
            "so `show(file=...)` surfaces both together.\n"
            "- 🔗 linked (links=) — confirms which of the `links=` you passed actually connected; "
            "one that failed shows `⚠️ link(...) failed` next to it instead."
        ),
        "tags": ["guide", "workflow"],
    },
]
