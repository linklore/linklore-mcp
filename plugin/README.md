# LinkLore (Claude Code Plugin)

**AI-native structured memory for agents** — lore (decisions, pitfalls, local rules) and doc (specs, system docs) that AI agents read and write directly, so Claude doesn't have to re-derive context every session.

> **Free tool, paid backend service.** This plugin — and the underlying `llre` MCP server — is free to install and use locally (SQLite-backed, no account required). Team sync, cross-project sharing, and cloud backup are powered by an optional backend subscription at [linklore.io](https://linklore.io). The plugin is just a distribution channel; it does not change the pricing model.

## Install

**Option A — Claude Code Plugin (this package)**

Install from a marketplace once LinkLore is listed, or load it locally for development:

```bash
claude plugin install linklore@<marketplace>
# or, from a local checkout:
claude --plugin-dir /path/to/linklore/plugin
```

This registers the bundled `.mcp.json`, which runs the server via `uvx llre` (same command as the standalone path below — no separate install to maintain).

**Option B — Standalone `uvx` (existing path)**

Register the MCP server directly in your project's `.mcp.json` or `.cursor/mcp.json`:

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

Requires `uv`/`uvx` on PATH. See the [`mcp/` package README](../mcp/README.md) for the source-checkout dev path and optional embedding-search extra.

## First use — 3 steps

1. **`init`** — sets up `.linklore/` in the current project (local memory store, no account needed).
2. **`brief`** — call at the start of every session. Loads open items, recent activity, and hotspots in a few hundred tokens — cheaper than re-reading the whole codebase.
3. **`add`** — after a decision, fix, or pitfall, record it (`type='lore'`) so the next session doesn't repeat the mistake. For new systems/features, prefer `add(type='doc')` over a standalone `.md` file — LinkLore docs get bidirectional links and automatic code context.

Day to day: `show()` to search before changing code, `add()`/`edit()` to record as you go.

## License

Elastic License 2.0 (ELv2) — see [`LICENSE`](../LICENSE). Free to install and use; you may not provide the software as a competing managed service, circumvent license-key functionality, or remove licensing notices (contact support@linklore.io for anything beyond that).
