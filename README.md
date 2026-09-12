# Postclick MCP: landing page optimization

Let's make your landing page world class.

Postclick by PPC.io helps you find what to fix, rewrite copy, answer buyer objections and turn audit findings into designs and finished pages.

**[Connect Postclick](https://ppc.io/postclick/mcp?utm_source=github&utm_medium=directory&utm_campaign=postclick-mcp)** · **[Try an example](EXAMPLES.md)** · **[Browse the free skills](skills/)**

## Start here

- **Have page copy?** Give it to your assistant with a [free skill](skills/). No Postclick account needed.
- **Have a saved audit?** Connect Postclick and ask: “What should I fix first? Show me the change.” Saved reads use no credits.
- **Need a new audit or design?** Your agent checks the price and asks before spending credits.

MCP server URL: **https://mcp.ppc.io**

Use a remote Streamable HTTP connection. OAuth connects the user's own Postclick account. No local server installation is needed.

## For agents and researchers

[Agent guide](AGENT-GUIDE.md) · [Server metadata](server.json) · [Official MCP Registry](https://registry.modelcontextprotocol.io/?q=postclick-landing-page-cro) · [REST API](https://ppc.io/postclick/docs)

This repository contains public skills, examples and connection documentation. The hosted application source is maintained separately.

Try the public MCP without an account:

```sh
python3 scripts/check-public.py
```

This reads the public catalogue and checks that private audit access requires a connection. It does not create an audit or spend credits. The scheduled check runs the same test.

Postclick does not manage ad accounts. Buyer reactions are modelled. Suggested changes need testing; conversion gains are not guaranteed.

Claude Code and OpenAI Responses MCP have been tested. Signed-in consumer Claude and ChatGPT web sessions have not been directly tested. Custom connector access depends on the client and plan.

## Keeping these files current

The public files are generated from Postclick's maintained skill and discovery sources. The daily check compares this copy with the live public catalogue, instructions and manifest. A failed check means the copy or connection needs attention.
