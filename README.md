# LinkLore

**AI-native structured memory for agents** — a project memory that AI agents read and write directly (lore/doc), via [MCP](https://modelcontextprotocol.io).

AI agents record decisions, pitfalls, and specs as they work — and recall them next session with code context attached (file links, stale detection, bidirectional links). Local-first: everything lives in a `.linklore/` SQLite store in your project.

- **[`mcp/`](./mcp)** — the readable portion of the MCP server source (PyPI: [`llre`](https://pypi.org/project/llre/), run with `uvx llre`)
- **[`plugin/`](./plugin)** — Claude Code plugin wrapper

## Quick start — tell your agent

This is an MCP server, meant to be set up by an AI agent rather than typed in by hand. Paste this as your first message to Claude Code, Cursor, or any other MCP-capable agent:

> Set up LinkLore (an MCP server for project memory) in this repo. It's the PyPI package `llre`, run via `uvx llre` — no install or clone needed. Register it as an MCP server for whichever client you are (Claude Code: `claude mcp add llre -- uvx llre`; otherwise add `{"mcpServers": {"llre": {"command": "uvx", "args": ["llre"]}}}` to this project's `.mcp.json`), then run `uvx llre init` here. Ask me first before running `uvx llre login` — it opens a browser for Google login and is only needed for personal backup or team sharing.

Prefer to do it by hand?

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

Or with Claude Code:

```bash
claude mcp add llre -- uvx llre
```

The official guide ships **inside the product, as lore** — LinkLore documents itself with itself. After `init()`, your project carries the guide as a read-only source:

```
show(tag='guide')
```

It updates with the package: upgrade `llre` and `brief()` tells you what changed.

## Source model

Mostly readable, core compiled. This repository publishes the MCP server's source in the clear — the entry point, i18n catalogs, base utilities, and the onboarding guide — under the Elastic License 2.0. The core modules (search, ranking, contradiction detection, the tool logic) ship as compiled extensions in the published wheel rather than plaintext source, so "read every line and fork it" isn't 100% true — but the majority is readable, and you can run it, self-host it, and use it commercially inside your own org. We'd rather be upfront that the crown-jewel logic is compiled than pretend it's fully open.

This tree is not buildable on its own (the compiled modules are not here) — install the published package instead: `uvx llre`.

## Research

LinkLore is the case study of the paper **"When the Agent Is the User: Agent-Driven Evolution of AI-Native Tools"** — defining the *AI-Native Tools* category, where the AI agent is the primary operator.

DOI: [10.5281/zenodo.21216858](https://doi.org/10.5281/zenodo.21216858) · citation: [`CITATION.cff`](./CITATION.cff)

## License

[Elastic License 2.0](./LICENSE). Free to install and use; you may not provide the software as a competing managed service, circumvent license-key functionality, or remove licensing notices.

Team sync, cross-project sharing, and cloud backup are provided by the backend service at [linklore.io](https://linklore.io) (not part of this repository).
