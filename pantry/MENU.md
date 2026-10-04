# Menu: liquid-gold-grok-bot

Queue: 2026-10-04-pantry-queue.md
Counts: open 65, in flight 0, shipped 1, parked 0, dropped 0, needs fixing 0

## Steer

- none

## Up next

**publish-proof-judge**: Publish Proof Judge as a template (`publish-proof-judge`) (queue #2, high, host, since 2026-09-30)

- Done when: `bots/proof-judge/template.md` holds an `https://x.ai/bot/` link in place of "pending publish"; `curl -sL <that link>` returns a page whose title is "Proof Judge" and which shows "Add to Grok Bot"; the Proof Judge row in CATALOG.md links the template; `python3 scripts/check.py` passes
- Verify on: host (the owner's Grok Bot app publishes; the check runs anywhere)
- Evidence: Matrix: "One-click Add to Grok Bot link per entry" (Us N; MP, majiayu000 and divo12 Y; cobus N). X: @bot "You can now share templates of your Bots with others."
- Issue: #9
- Order: bouncer, gotcha-template-import-drops-skills, grok-ship, grokbot-field-notes, import-bot, loops, projects-manager, proto-bot, startup-qa-bot, swe-cursor, tinkabot, publish-proof-judge, proof-judge-eval, catalog-json, account-research-desk, sell-bot, ad-spend-watch, ai-search-visibility, call-follow-ups, copy-humanizer, critiquito, cto, doc-approvals-security-privacy, doc-create-and-manage-bots, doc-grok-bot-overview, doc-skills-and-routines, doc-team-bots, figma-bro, gojiberryai-sales-os, gotcha-bots-not-a-security-boundary, gotcha-custom-connectors-in-chat, gotcha-no-local-mcp, gotcha-weekly-usage-on-demand, grok-bot-coach, grok-bot-templates, guide-flavio-copes-deep-dive, guide-grok-bot-101, guide-grok-bot-for-engineering, guide-multiple-teams-of-grok-bots, guide-templates-for-grok-bot, hub-cursor-forum-grok-bot, hub-grokdex, hub-majiayu000-awesome-grok-bot, hub-ronglecat-awesome-grok-bot, last30days, market-researcher, marketing-project-manager, post-bot-building-software, post-bot-share-templates, post-mattyp-templates-launch, post-team-bots-announcement, pr-reviewer, researcher, researchy, sequencer, signal-prospector, tech-demos, token-efficiency-optimizer, tradbot, website-ops, writing-bot, x-brief, assay-engineer-bot, publish-night-watch, stack-kitchen-eval
- Tie: none

## Atoms

| Key | Title | State | Confidence | Class | Since | Queue # | Issue | Because |
|-----|-------|-------|------------|-------|-------|---------|-------|---------|
| account-research-desk | Card the `account-research-desk` listing from the marketplace | open | medium | repo | 2026-10-03 | 7 | - | - |
| ad-spend-watch | Card the `ad-spend-watch` listing from the marketplace | open | medium | repo | 2026-10-04 | 21 | - | - |
| ai-search-visibility | Card the `ai-search-visibility` listing from the marketplace | open | medium | repo | 2026-10-04 | 29 | - | - |
| assay-engineer-bot | Assay Lingxi's Engineer Bot from its template details (`assay-engineer-bot`) | open | medium | host | 2026-09-30 | 6 | - | - |
| bouncer | Card the shared `bouncer` template | open | high | repo | 2026-10-04 | 15 | - | - |
| call-follow-ups | Card the `call-follow-ups` listing from the marketplace | open | medium | repo | 2026-10-04 | 24 | - | - |
| catalog-json | Publish a machine-readable `catalog-json` | open | medium | repo | 2026-09-30 | 1 | - | - |
| copy-humanizer | Card the `copy-humanizer` listing from the marketplace | open | medium | repo | 2026-10-04 | 23 | - | - |
| critiquito | Card the `critiquito` listing from the marketplace | open | medium | repo | 2026-10-04 | 32 | - | - |
| cto | Card the shared `cto` template | open | medium | repo | 2026-10-04 | 39 | - | - |
| doc-approvals-security-privacy | List `doc-approvals-security-privacy` in GUIDES.md | open | medium | repo | 2026-10-04 | 51 | - | - |
| doc-create-and-manage-bots | List `doc-create-and-manage-bots` in GUIDES.md | open | medium | repo | 2026-10-04 | 49 | - | - |
| doc-grok-bot-overview | List `doc-grok-bot-overview` in GUIDES.md | open | medium | repo | 2026-10-04 | 48 | - | - |
| doc-skills-and-routines | List `doc-skills-and-routines` in GUIDES.md | open | medium | repo | 2026-10-04 | 50 | - | - |
| doc-team-bots | List `doc-team-bots` in GUIDES.md | open | medium | repo | 2026-10-04 | 52 | - | - |
| figma-bro | Card the `figma-bro` listing from the marketplace | open | medium | repo | 2026-10-04 | 30 | - | - |
| gojiberryai-sales-os | Card the public team `gojiberryai-sales-os` | open | medium | repo | 2026-10-04 | 42 | - | - |
| gotcha-bots-not-a-security-boundary | List `gotcha-bots-not-a-security-boundary` in GUIDES.md | open | medium | repo | 2026-10-04 | 54 | - | - |
| gotcha-custom-connectors-in-chat | List `gotcha-custom-connectors-in-chat` in GUIDES.md | open | medium | repo | 2026-10-04 | 56 | - | - |
| gotcha-no-local-mcp | List `gotcha-no-local-mcp` in GUIDES.md | open | medium | repo | 2026-10-04 | 55 | - | - |
| gotcha-template-import-drops-skills | List `gotcha-template-import-drops-skills` in GUIDES.md | open | high | repo | 2026-10-04 | 19 | - | - |
| gotcha-weekly-usage-on-demand | List `gotcha-weekly-usage-on-demand` in GUIDES.md | open | medium | repo | 2026-10-04 | 57 | - | - |
| grok-bot-coach | Card the shared `grok-bot-coach` template | open | medium | repo | 2026-10-04 | 38 | - | - |
| grok-bot-templates | Card the public team `grok-bot-templates` | open | medium | repo | 2026-10-04 | 43 | - | - |
| grok-ship | Card the public team `grok-ship` | open | high | repo | 2026-10-04 | 17 | - | - |
| grokbot-field-notes | Card the public team `grokbot-field-notes` | open | high | repo | 2026-10-04 | 18 | - | - |
| guide-flavio-copes-deep-dive | List `guide-flavio-copes-deep-dive` in GUIDES.md | open | medium | repo | 2026-10-04 | 53 | - | - |
| guide-grok-bot-101 | List `guide-grok-bot-101` in GUIDES.md | open | medium | repo | 2026-10-04 | 45 | - | - |
| guide-grok-bot-for-engineering | List `guide-grok-bot-for-engineering` in GUIDES.md | open | medium | repo | 2026-10-04 | 47 | - | - |
| guide-multiple-teams-of-grok-bots | List `guide-multiple-teams-of-grok-bots` in GUIDES.md | open | medium | repo | 2026-10-04 | 46 | - | - |
| guide-templates-for-grok-bot | List `guide-templates-for-grok-bot` in GUIDES.md | open | medium | repo | 2026-10-04 | 44 | - | - |
| hub-cursor-forum-grok-bot | List `hub-cursor-forum-grok-bot` in GUIDES.md | open | medium | repo | 2026-10-04 | 65 | - | - |
| hub-grokdex | List `hub-grokdex` in GUIDES.md | open | medium | repo | 2026-10-04 | 64 | - | - |
| hub-majiayu000-awesome-grok-bot | List `hub-majiayu000-awesome-grok-bot` in GUIDES.md | open | medium | repo | 2026-10-04 | 63 | - | - |
| hub-ronglecat-awesome-grok-bot | List `hub-ronglecat-awesome-grok-bot` in GUIDES.md | open | medium | repo | 2026-10-04 | 62 | - | - |
| import-bot | Card the `import-bot` listing from the marketplace | open | high | repo | 2026-10-04 | 14 | - | - |
| last30days | Card the `last30days` listing from the marketplace | open | medium | repo | 2026-10-04 | 35 | - | - |
| loops | Card the shared `loops` template | open | high | repo | 2026-10-04 | 16 | - | - |
| market-researcher | Card the `market-researcher` listing from the marketplace | open | medium | repo | 2026-10-04 | 20 | - | - |
| marketing-project-manager | Card the `marketing-project-manager` listing from the marketplace | open | medium | repo | 2026-10-04 | 33 | - | - |
| post-bot-building-software | List `post-bot-building-software` in GUIDES.md | open | medium | repo | 2026-10-04 | 60 | - | - |
| post-bot-share-templates | List `post-bot-share-templates` in GUIDES.md | open | medium | repo | 2026-10-04 | 59 | - | - |
| post-mattyp-templates-launch | List `post-mattyp-templates-launch` in GUIDES.md | open | medium | repo | 2026-10-04 | 58 | - | - |
| post-team-bots-announcement | List `post-team-bots-announcement` in GUIDES.md | open | medium | repo | 2026-10-04 | 61 | - | - |
| pr-reviewer | Card the shared `pr-reviewer` template | open | medium | repo | 2026-10-04 | 37 | - | - |
| projects-manager | Card the `projects-manager` listing from the marketplace | open | high | repo | 2026-10-04 | 13 | - | - |
| proof-judge-eval | Run Proof Judge live against its prompts (`proof-judge-eval`) | open | high | eval | 2026-09-30 | 4 | - | - |
| proto-bot | Card the `proto-bot` listing from the marketplace | open | high | repo | 2026-10-04 | 11 | - | - |
| publish-night-watch | Publish Night Watch as a template (`publish-night-watch`) | open | medium | host | 2026-09-30 | 3 | - | - |
| publish-proof-judge | Publish Proof Judge as a template (`publish-proof-judge`) | open | high | host | 2026-09-30 | 2 | #9 | - |
| researcher | Card the shared `researcher` template | open | medium | repo | 2026-10-04 | 40 | - | - |
| researchy | Card the `researchy` listing from the marketplace | open | medium | repo | 2026-10-04 | 36 | - | - |
| sell-bot | Card the `sell-bot` listing from the marketplace | open | medium | repo | 2026-10-03 | 8 | - | - |
| sequencer | Card the `sequencer` listing from the marketplace | open | medium | repo | 2026-10-04 | 22 | - | - |
| signal-prospector | Card the `signal-prospector` listing from the marketplace | open | medium | repo | 2026-10-04 | 26 | - | - |
| stack-kitchen-eval | Run the Stack Kitchen seats live in a group (`stack-kitchen-eval`) | open | medium | eval | 2026-09-30 | 5 | - | - |
| startup-qa-bot | Card the `startup-qa-bot` listing from the marketplace | open | high | repo | 2026-10-04 | 12 | - | - |
| swe-cursor | Card the `swe-cursor` listing from the marketplace | open | high | repo | 2026-10-04 | 10 | - | - |
| tech-demos | Card the `tech-demos` listing from the marketplace | open | medium | repo | 2026-10-04 | 28 | - | - |
| tinkabot | Card the `tinkabot` listing from the marketplace | open | high | repo | 2026-10-04 | 9 | - | - |
| token-efficiency-optimizer | Card the shared `token-efficiency-optimizer` template | open | medium | repo | 2026-10-04 | 41 | - | - |
| tradbot | Card the `tradbot` listing from the marketplace | open | medium | repo | 2026-10-04 | 27 | - | - |
| website-ops | Card the `website-ops` listing from the marketplace | open | medium | repo | 2026-10-04 | 31 | - | - |
| writing-bot | Card the `writing-bot` listing from the marketplace | open | medium | repo | 2026-10-04 | 34 | - | - |
| x-brief | Card the `x-brief` listing from the marketplace | open | medium | repo | 2026-10-04 | 25 | - | - |

## Retired

| Key | Title | State | Since | Issue | Because |
|-----|-------|-------|-------|-------|---------|
| rubric-check | Check the routine and plugin fields in CI (`rubric-check`) | shipped | 2026-09-30 | #3 | bullet: Check the routine and plugin fields in CI (`rubric-check`): shipped, PR #8 |

## Notes

- none
