# QA bot

| | |
|---|---|
| Author | Ulysses Ng |
| Listing | https://x.ai/bot/marketplace/bots/qa-bot |
| Add to Grok Bot | https://x.ai/bot/lKQWoQAvYgg_7Bkg2R-m7 |
| Categories | Engineering |
| Level | assayed from the page |

## What it does

From the listing: "Acts as your QA on the live deploy: runs the acceptance checklist and says pass or fail before you ship."

## Why it is gold

- A binary verdict on the live deploy, the same shape as our [Proof Judge](../bots/proof-judge/), but aimed at production after merge.
- Its routine stays quiet when a PASS has not changed.
- It pairs with the same author's [PM bot](pm-bot.md), whose cut defines what QA checks.

## What we could see from outside

- The page data lists 7 memories, 3 skills (enterprise AC fail-gate, ADHD-friendly agent responses, getting-started-ac-fail-gate-qa), 1 integration (Vercel) and 1 routine, "Post-merge AC fail-gate": "When a PR merges in the watched product repo, verify Production SHA and re-run the BLOCK AC pack; stay quiet on unchanged PASS."
