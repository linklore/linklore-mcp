# LinkLore

[![PyPI](https://img.shields.io/pypi/v/llre)](https://pypi.org/project/llre/)
[![Python](https://img.shields.io/pypi/pyversions/llre)](https://pypi.org/project/llre/)
[![License: Elastic 2.0](https://img.shields.io/badge/license-Elastic%202.0-blue)](./LICENSE)
[![MCP](https://img.shields.io/badge/MCP-server-blueviolet)](https://modelcontextprotocol.io)

**MCP server for project memory — lets AI agents record decisions, pitfalls, and specs as they work, and recall them next session with code context attached.**

Built for agents, not humans: every tool here is designed for usability by an AI, not readability for a person.

## Why LinkLore

Every new session, an AI agent starts from zero — decisions get re-litigated, pitfalls get rediscovered, and "why is it done this way?" gets answered by guessing. Markdown notes don't fix this: they're written for people, they drift from the code, and no agent reads them reliably.

LinkLore is structured memory that the agent itself reads and writes through MCP tools:

- **Two record types** — *lore* (decisions, pitfalls, journal) and *doc* (specs, plans), bidirectionally linked to each other and to code files.
- **Local-first** — everything lives in a `.linklore/` SQLite store inside your project. No account needed to start.
- **Code context** — records link to source files; git-diff-based stale detection flags memory that the code has outrun.
- **Cheap recall** — query by meaning, tag, file, status, or period; a session-start `brief()` returns open items and hotspots in a few hundred tokens.

## Quick Start

Runs straight from PyPI — no install or clone (`uvx llre`).

**Claude Code**

```bash
claude mcp add llre -- uvx llre
```

**Any other MCP client** (Cursor, Codex, Windsurf, …) — add to the project's MCP config (e.g. `.mcp.json`):

```json
{
  "mcpServers": {
    "llre": {
      "command": "uvx",
      "args": ["llre"]
    }
  }
}
```

Then initialize, once, in the project root:

```bash
uvx llre init
```

**Or let your agent do all of it** — this is a server meant to be set up by an AI agent rather than typed in by hand. Paste this as your first message to Claude Code, Cursor, Codex, or any other MCP-capable agent:

> Set up LinkLore (an MCP server for project memory) in this repo. It's the PyPI package `llre`, run via `uvx llre` — no install or clone needed. Register it as an MCP server for whichever client you are (Claude Code: `claude mcp add llre -- uvx llre`; otherwise add `{"mcpServers": {"llre": {"command": "uvx", "args": ["llre"]}}}` to this project's `.mcp.json`), then run `uvx llre init` here. Ask me first before running `uvx llre login` — it opens a browser for Google login and is only needed for personal backup or team sharing.

## The Loop

How an agent actually uses it, in order:

```
start a session       →  brief()                  open items, recent activity, hotspots
about to touch code   →  show(file=..., query=…)  decisions & pitfalls tied to that area
decided / got burned  →  add(type='lore', …)      record it, linked to the files involved
spec or plan          →  add(type='doc', …)       instead of a standalone .md
something changed     →  edit(id=..., …)          append, replace a section, or supersede
memory getting messy  →  doctor() · cleanup()     integrity check, duplicate detection
back up / share       →  push() · openbox(…)      your server space · invite-only shared boxes
```

## Available Tools

22 tools. Call any of them with `help=True` for full usage.

| Category | Tool | What it does |
| --- | --- | --- |
| Setup | `init` | Set up `.linklore/` in the current directory |
| Project | `brief` | Session-start dashboard — open items, recent activity, hotspots |
| Project | `status` | Code↔doc sync drift detection (git-diff based) |
| Project | `config` | Project settings, external sources, session pin |
| Diagnostics | `doctor` | Data integrity check; `action='fix'` auto-repairs |
| Record | `add` | Create lore or doc; `items=[{...}]` batch-creates |
| Record | `edit` | Modify an item — append (default), replace a section, overwrite, or supersede |
| Record | `rm` | Delete — recoverable trash by default, `force=True` for permanent |
| Record | `restore` | Recover from trash; without `id` lists the trash |
| Record | `local` | Move/copy/view items across sibling local workspaces |
| Search | `show` | Query by id, text, tag, status, file, or period; graph and tag views |
| Search | `log` | Change history |
| Link | `link` | Connect two items (lore↔lore, doc↔doc, doc↔lore) |
| Link | `unlink` | Disconnect two items |
| Doc view | `doc_flow` | Render a doc's flow chain in order |
| Doc view | `doc_map` | Overview of the full doc link network |
| Doc view | `doc_rollup` | Collect lore linked to a doc into an AI-summary draft |
| Cleanup | `cleanup` | Detect near-duplicate lore/doc candidates |
| My server | `push` | Back up the local store to your own server space |
| My server | `pull` | Restore from your own server space |
| Openbox | `openbox` | All cross-owner sharing behind one gate — push/pull, browse, invite/join, roles |
| Feedback | `report` | Send feedback or a bug report straight to the team |

The full guide ships **inside the product, as lore** — LinkLore documents itself with itself. After `init()`, your project carries it as a read-only source:

```
show(tag='guide')
```

It updates with the package: upgrade `llre` and `brief()` tells you what changed.

## Repository Layout

- **[`mcp/`](./mcp)** — the readable portion of the MCP server source (PyPI: [`llre`](https://pypi.org/project/llre/))
- **[`plugin/`](./plugin)** — Claude Code plugin wrapper

## Source Model

Mostly readable, core compiled. This repository publishes the MCP server's source in the clear — the entry point, i18n catalogs, base utilities, and the onboarding guide — under the Elastic License 2.0. The core modules (search, ranking, contradiction detection, the tool logic) ship as compiled extensions in the published wheel rather than plaintext source, so "read every line and fork it" isn't 100% true — but the majority is readable, and you can run it, self-host it, and use it commercially inside your own org. We'd rather be upfront that the crown-jewel logic is compiled than pretend it's fully open.

This tree is not buildable on its own (the compiled modules are not here) — install the published package instead: `uvx llre`.

## Research

LinkLore is the case study of the paper **"When the Agent Is the User: Agent-Driven Evolution of AI-Native Tools"** — defining the *AI-Native Tools* category, where the AI agent is the primary operator.

DOI: [10.5281/zenodo.21216858](https://doi.org/10.5281/zenodo.21216858) · citation: [`CITATION.cff`](./CITATION.cff)

## License

[Elastic License 2.0](./LICENSE). Free to install and use; you may not provide the software as a competing managed service, circumvent license-key functionality, or remove licensing notices.

Team sync, cross-project sharing, and cloud backup are provided by the backend service at [linklore.io](https://linklore.io) (not part of this repository).
