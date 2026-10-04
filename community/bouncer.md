# Bouncer

| | |
|---|---|
| Author | Brad Shannon |
| Share page | https://x.ai/bot/cGcG0msqfz7o7J3QMLhbE |
| Add to Grok Bot | https://x.ai/bot/cGcG0msqfz7o7J3QMLhbE |
| Level | assayed from the page |

## What it does

From the share page, read on 2026-10-04: "Reviews a public Grok Bot share link or pasted config before you add it. Quotes findings and returns CLEAN, WARN, or BLOCK-recommended, and does not add, install, spend, or post."

The visible byline is "by Brad". The page data names the sharer "Brad Shannon".

## Why it is gold

- It reviews the share before you add it. The description is a review of a public share link or a pasted config, and it stops at a verdict.
- The verdict is one of three named outcomes: CLEAN, WARN, or BLOCK-recommended. That is the card-shaped decision our [rubric](../RUBRIC.md) asks for, and the shape our [Proof Judge](../bots/proof-judge/) gives a pull request.
- Evidence before the verdict: "Quotes findings".
- The same sentence names the refusals: it does not add, install, spend, or post.

## What we could see from outside

- `curl -sL` on 2026-10-04 returned status `HTTP/2 200`. The title is "Bouncer by Brad". The final URL is the share page above.
- The visible page shows the name, the byline, the description quoted above, the line "This AI bot was created by a third-party user, not by SpaceXAI", and a button labeled "Add to Grok Bot" whose href is `grokbot://app/v1/bot-template?id=cGcG0msqfz7o7J3QMLhbE`.
- The page data in that HTML is one bot-template record: id `cGcG0msqfz7o7J3QMLhbE`, ownerType USER, sharerName Brad Shannon, botName Bouncer, the description quoted above, that add href, color `#FF263C`, shape gem.
- The HTML publishes no skills, no routines, and no integrations. It includes no instructions text and no memory text, so none of that is copied here.

## Cracks seen from outside

- With no skills, routines, or integrations on the page, cadence, cost, connectors, and Ask first rules cannot be checked from this read.
- "BLOCK-recommended" is a recommendation in the description. The description says the bot does not add or install. The page does not show the steps behind a verdict.
- The meta description cuts the refusal clause to "does not...". The visible paragraph and the page data's description field carry the full sentence quoted above.
