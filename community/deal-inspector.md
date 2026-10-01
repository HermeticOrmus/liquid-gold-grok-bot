# Deal Inspector

| | |
|---|---|
| Author | Jon Grigull |
| Listing | https://x.ai/bot/marketplace/bots/deal-qualification |
| Add to Grok Bot | https://x.ai/bot/vZfC76-4UC1XU7qC4m726 |
| Categories | From Grok Bot Team, Sales |
| Level | assayed from the page |

## What it does

From the listing: "Checks every deal that moved stage against your qualification criteria using the actual call transcripts. Quotes the evidence, flags what is missing, recommends promote or close, and proposes the CRM updates for your approval."

## Why it is gold

- A decision with fixed options: "Verdicts are Promote, Close, or Insufficient Data, never a maybe." That is the card-shaped decision our [rubric](../RUBRIC.md) asks for, and the shape our [Proof Judge](../bots/proof-judge/) gives a pull request.
- Evidence before any claim: "Every criterion in an audit is scored from a transcript quote with a timestamp, or marked as missing."
- A bar a reader can check: "A recommendation to move a deal to the next stage names the champion, the economic buyer, the pain in the customer's words, and an estimated size, or it is not a recommendation."
- Writes are drafts first: "This bot writes nothing to the CRM without the owner's approval in the same conversation. Unattended runs stage audits; the owner applies them." Its crm-writeback skill shows "a before/after diff" and "applies it only after the owner approves".
- Least access in its own words: the Salesforce line says "Connect the one CRM you use."
- The first conversation ends in a real result: getting-started "audits one live deal as a demo".

## What we could see from outside

- The page data, read on 2026-10-01, lists 3 memories and 4 skills: crm-writeback, getting-started, qualification-frameworks, stage-gate-audit.
- 9 integrations: Gong, Granola, Salesforce, HubSpot, Attio, Slack, Gmail, Notion, Google Sheets. HubSpot and Attio are listed as alternatives to Salesforce.
- 1 routine, "Friday stage audit": "Every Friday afternoon, audit each of the owner's opportunities that was created or moved stage this week against the qualification framework and stage the CRM updates."
- The instructions field is empty in the page data. The standing rules are in its memories.

## Cracks seen from outside

- The routine's summary does not say it ships disabled, and getting-started "sets up the weekly audit" in the first conversation. Whether it asks before it turns the routine on is not visible.
- No quiet rule is stated for a run where no deal moved stage. *Inferred*: an empty audit may still arrive.
- Gmail's line, "Checks whether we did what we promised on the last call", is a read. Only CRM writes carry a stated approval rule; no line on the page says it never sends mail.
- Slack delivers "the weekly audit as a DM". The page does not say whose DM, or that transcript quotes stay out of shared channels.
