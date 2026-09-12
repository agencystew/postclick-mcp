# Make your landing page clearer

Start with one job. Use your own page copy or connect a saved Postclick audit.
These are starter requests, not customer results.

## Improve the opening without an account

Give your assistant your headline, opening paragraph and button text, then ask:

> Use Postclick's copy rewrite skill on the copy below. Tell me who this page is for, what it offers and what happens after I click. If any of those are unclear, rewrite the headline, opening and button. Keep the facts. Ask before adding a claim.

[Get the copy rewrite skill](https://ppc.io/free-tools/postclick-copy-rewrite).
No Postclick account or audit is needed. Your assistant uses the copy you supply.
A useful answer gives you replacement copy, explains the change briefly and names any missing facts.

## Make the page match the ad

Give your assistant the ad and the page opening, then ask:

> Use Postclick's message match skill. Compare this ad with this page. What does the ad promise that the page does not explain? Rewrite the opening so they agree. Do not invent prices, guarantees or reviews.

[Get the message match skill](https://ppc.io/free-tools/postclick-message-match).
No Postclick account is needed when you supply both pieces of copy. A useful answer shows the missing promise and the replacement opening.

## Know what to fix first in a saved audit

[Connect Postclick](https://postclick.ppc.io/connections), then ask:

> Use my latest Postclick audit. What should I fix first? Show me the exact change and link to the finding. Keep it short.

The agent uses `run_cro_skill` with `skill: "postclick-fix-first"` and `latest: true`.
This reads your saved audit without spending credits. If there is no saved audit, it should say so and offer the portable skill or a new audit with a price check first.

## For agents: try the public connection

Run `python3 scripts/check-public.py` from this repository. It reads public tools and skills and verifies that a private audit request is refused. It needs no packages, account or API key. It starts no paid work.

Connection URL: `https://mcp.ppc.io`. [Full account and credit rules](https://ppc.io/postclick/mcp.md).
Suggested changes need testing. Buyer reactions are modelled, not customer interviews or measured sales results.
