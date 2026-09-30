# Nightly Audit Engineer

| | |
|---|---|
| Author | Lingxi Li |
| Listing | https://x.ai/bot/marketplace/bots/nightly-audit-engineer |
| Add to Grok Bot | https://x.ai/bot/0LLQmzk-yzwHi0zuiV0lC |
| Categories | From Grok Bot Team, Engineering |
| Level | assayed from the page |

## What it does

From the listing: "A nightly engineering auditor that researches a whole codebase, then ships one cleanup PR per area. Defaults to 4am and asks when to run before it starts."

## Why it is gold

- One cleanup PR per area keeps each review small.
- It asks when to run before its first run instead of assuming a schedule.
- It is the model our [Gardener](../bots/gardener/) narrows to one provable weed per run.

## What we could see from outside

- The page data lists 7 memories and 1 routine, "Nightly code-quality audit (4am)", summarized as "Research the whole tree, then one cleanup per area."
- No skills or integrations are listed on the page.

## Check before you add it

A whole-tree audit is a large run each time it fires. Pick a cadence you will actually review.
