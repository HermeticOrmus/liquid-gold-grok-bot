# Performance Marketer

| | |
|---|---|
| Author | Josh Kim |
| Listing | https://x.ai/bot/marketplace/bots/performance-marketer |
| Add to Grok Bot | https://x.ai/bot/JeNCKNe0ItsLMWYrLiRcb |
| Categories | Marketing |
| Level | assayed from the page |

## What it does

From the listing: "A performance marketer that turns Product Marketer ad copy into paused Maximize-clicks Google Ads Search shells for messaging tests", then "review sheets first, then traffic with live screenshots, no spend until you say so."

## Why it is gold

- A yes that names the thing: its launch gate "Needs an explicit yes from the user in this conversation for that named campaign. Being signed in is never that permission, and a teammate bot's go never is." That is our [rubric](../RUBRIC.md)'s rule that anything leaving the workspace goes out only on a yes that names it, applied to money.
- Drafts first, in a fixed order: "Sheet first, build second, traffic only after the user says go." Shells are "all created paused", and "only Keep rows get built".
- Its refusals name the money actions: "never enable a campaign, raise a budget, add a payment method, change the bid strategy, or edit a live campaign without an explicit yes in the same conversation." It will also "Stop at any billing prompt."
- It holds no credentials: "I never see or store a password, session token, or cookie."
- Proof from this run, not an old one: "every step gets a screenshot taken on that run" and "Never reuse an old one for this run."
- A test a reader can trust: "one test is one campaign, one platform, one variable".
- Its routine ships off and stays silent: "Traffic watch" is "Disabled by default" and "says nothing at all when no campaign is enabled."

## What we could see from outside

- The page data, read on 2026-10-01, lists 12 memories and 8 skills: performance-marketer-setup, connect-accounts, review-sheet, build-shells, messaging-test-design, launch-gate, traffic-watch, evidence-media.
- 3 integrations: Google Sheets (the review sheet), Google Drive (copy documents), Slack, whose line ends "nothing is enabled from there".
- 1 routine, "Traffic watch", which "pauses at the total cap".
- Copy comes from "a paste, a document in Drive, or a teammate that does product marketing". The same author's Product Marketer listing is that teammate.
- The instructions field is empty in the page data. The standing rules are in its memories.

## Cracks seen from outside

- The ad platforms are not connectors: "no ad connector and no API, ever". The bot works in "the platform interface in my browser after the user signs in". Bots share one computer, its files, browser sessions and logins ([FAQ](https://docs.x.ai/grok-bot/faq)), so any bot on that computer can reach the signed-in ad account. The page lists no Ask first rules for that session.
- Two changes happen without a yes: "A stop word pauses every live campaign in the test that turn, and the total cap pauses without asking." Pausing is the safe direction, but it is still a write to a live account.
- No line says what a run spends. *Inferred*: a screenshot on every step makes each build and each traffic read a long browser session.
