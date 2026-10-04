# Menu: liquid-gold-grok-bot

Queue: 2026-10-03-pantry-queue.md
Counts: open 8, in flight 0, shipped 1, parked 0, dropped 0, needs fixing 0

## Steer

- none

## Up next

**publish-proof-judge**: Publish Proof Judge as a template (`publish-proof-judge`) (queue #2, high, host, since 2026-09-30)

- Done when: `bots/proof-judge/template.md` holds an `https://x.ai/bot/` link in place of "pending publish"; `curl -sL <that link>` returns a page whose title is "Proof Judge" and which shows "Add to Grok Bot"; the Proof Judge row in CATALOG.md links the template; `python3 scripts/check.py` passes
- Verify on: host (the owner's Grok Bot app publishes; the check runs anywhere)
- Evidence: Matrix: "One-click Add to Grok Bot link per entry" (Us N; MP, majiayu000 and divo12 Y; cobus N). X: @bot "You can now share templates of your Bots with others."
- Issue: #9
- Order: publish-proof-judge, proof-judge-eval, catalog-json, account-research-desk, sell-bot, assay-engineer-bot, publish-night-watch, stack-kitchen-eval
- Tie: none

## Atoms

| Key | Title | State | Confidence | Class | Since | Queue # | Issue | Because |
|-----|-------|-------|------------|-------|-------|---------|-------|---------|
| account-research-desk | Card the `account-research-desk` listing from the marketplace | open | medium | repo | 2026-10-03 | 7 | - | - |
| assay-engineer-bot | Assay Lingxi's Engineer Bot from its template details (`assay-engineer-bot`) | open | medium | host | 2026-09-30 | 6 | - | - |
| catalog-json | Publish a machine-readable `catalog-json` | open | medium | repo | 2026-09-30 | 1 | - | - |
| proof-judge-eval | Run Proof Judge live against its prompts (`proof-judge-eval`) | open | high | eval | 2026-09-30 | 4 | - | - |
| publish-night-watch | Publish Night Watch as a template (`publish-night-watch`) | open | medium | host | 2026-09-30 | 3 | - | - |
| publish-proof-judge | Publish Proof Judge as a template (`publish-proof-judge`) | open | high | host | 2026-09-30 | 2 | #9 | - |
| sell-bot | Card the `sell-bot` listing from the marketplace | open | medium | repo | 2026-10-03 | 8 | - | - |
| stack-kitchen-eval | Run the Stack Kitchen seats live in a group (`stack-kitchen-eval`) | open | medium | eval | 2026-09-30 | 5 | - | - |

## Retired

| Key | Title | State | Since | Issue | Because |
|-----|-------|-------|-------|-------|---------|
| rubric-check | Check the routine and plugin fields in CI (`rubric-check`) | shipped | 2026-09-30 | #3 | bullet: Check the routine and plugin fields in CI (`rubric-check`): shipped, PR #8 |

## Notes

- none
