# Postclick MCP: landing page CRO for Google Ads and Meta ads

Let's make your landing page world class.

Postclick by PPC.io audits the page your ads send traffic to, finds what stops visitors turning into leads and sales, then rewrites the page or builds you a better one. It works inside Claude, ChatGPT, Cursor and any MCP client.

| | |
|---|---|
| Server URL | `https://mcp.ppc.io` |
| Transport | Streamable HTTP, remote. Nothing to install. |
| Sign-in | OAuth to your own Postclick account |
| What it does | Landing page audit, ad match check, buyer objections, competitor check, copy rewrites, A/B test briefs, page designs, page builder |

Ask it things like:

- "What should I fix first on my landing page?"
- "Does my landing page match my Google ad?"
- "What makes buyers hesitate on this page?"
- "Build me a better version of this page."

**[Connect Postclick](https://ppc.io/postclick/mcp?utm_source=github&utm_medium=directory&utm_campaign=postclick-mcp)** · **[Try an example](EXAMPLES.md)** · **[Browse the free skills](skills/)**

## Start here

- **Have page copy?** Give it to your assistant with a [free skill](skills/). No Postclick account needed.
- **Have a saved audit?** Connect Postclick and ask: “What should I fix first? Show me the change.” Saved reads do not use a page.
- **Need a new audit or page?** Your agent checks your balance and the live price with `check_balance`, tells you the price, and asks before it starts paid work. A new account gets its first audit free, with no card.

MCP server URL: **https://mcp.ppc.io**

Use a remote Streamable HTTP connection. OAuth connects the user's own Postclick account. No local server installation is needed.

## Claude plugin

The [plugin](plugin/) adds the five skills and the Postclick server to Claude in one step. In Claude Code, run:

```sh
claude plugin marketplace add agencystew/postclick-mcp
claude plugin install postclick@postclick
```

The skills work on copy you paste in. To use saved audits, run `/mcp` in Claude Code and sign in to Postclick.

## Other assistants

Every client below connects to the same remote server and opens a Postclick sign-in page the first time.

**ChatGPT:** Plugins, then Add, then Add custom MCP server. Paste `https://mcp.ppc.io`, choose OAuth, and connect. Mention `@Postclick` in a message to use it.

**Cursor** (`~/.cursor/mcp.json`):

```json
{ "mcpServers": { "postclick": { "url": "https://mcp.ppc.io" } } }
```

**VS Code** (`.vscode/mcp.json`):

```json
{ "servers": { "postclick": { "type": "http", "url": "https://mcp.ppc.io" } } }
```

**Cline** (`cline_mcp_settings.json`):

```json
{ "mcpServers": { "postclick": { "type": "streamableHttp", "url": "https://mcp.ppc.io" } } }
```

**Windsurf** (`~/.codeium/windsurf/mcp_config.json`):

```json
{ "mcpServers": { "postclick": { "serverUrl": "https://mcp.ppc.io" } } }
```

**Codex:** `codex mcp add postclick --url https://mcp.ppc.io`

## For agents and researchers

[Agent guide](AGENT-GUIDE.md) · [Server metadata](server.json) · [Official MCP Registry](https://registry.modelcontextprotocol.io/?q=postclick-landing-page-cro) · [Glama listing](https://glama.ai/mcp/connectors/io.ppc/postclick-landing-page-cro) · [REST API](https://ppc.io/postclick/docs)

This repository contains public skills, examples and connection documentation. The hosted application source is maintained separately.

Try the public MCP without an account:

```sh
python3 scripts/check-public.py
```

This reads the public catalogue and checks that private audit access requires a connection. It does not create an audit or use a page. The scheduled check runs the same test.

Postclick does not manage ad accounts. Buyer reactions are modelled. Suggested changes need testing; conversion gains are not guaranteed.

Claude Code and OpenAI Responses MCP have been tested. Signed-in consumer Claude and ChatGPT web sessions have not been directly tested. Custom connector access depends on the client and plan.

## Keeping these files current

The public files are generated from Postclick's maintained skill and discovery sources. The daily check compares this copy with the live public catalogue, instructions and manifest. A failed check means the copy or connection needs attention.
