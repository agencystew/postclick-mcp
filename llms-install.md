# Installing the Postclick MCP server

Postclick is a hosted remote MCP server. There is nothing to download, build or run locally.

1. Add this server to the MCP settings, using the Streamable HTTP transport:

   ```json
   { "mcpServers": { "postclick": { "type": "streamableHttp", "url": "https://mcp.ppc.io" } } }
   ```

2. Connect. The server answers tools that need an account with HTTP 401 and OAuth metadata, so the client opens a Postclick sign-in page. The user signs in at postclick.ppc.io and approves access. No API key is needed.
3. Check the connection: call `list_cro_skills`. It works before sign-in and returns the five landing page skills.
4. After sign-in, call `check_balance` before any paid step. Only `audit_page`, `generate_concepts` and `build_page` start paid work. Tell the user the price and get their yes first.

Help: https://ppc.io/postclick/mcp
