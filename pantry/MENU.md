# Menu: liquid-gold-grok-bot

Queue: 2026-09-30-pantry-queue.md
Counts: open 7, in flight 0, shipped 0, parked 0, dropped 0, needs fixing 0

## Steer

- none

## Up next

**rubric-check**: Check the routine and plugin fields in CI (`rubric-check`) (queue #1, high, repo, since 2026-09-30)

- Done when: `python3 scripts/check.py` fails, naming the file, when a bot's `routines.md` has no table row for any of Owning bot, Trigger, Schedule and time zone, Input, Result, Approval boundary, Missing source; when a routine whose Trigger names a schedule or an event has no `Cost:` line; or when a bot's `plugins.md` has no `## Ask first rules` section. `scripts/fixtures/` holds one broken bot folder per rule, `python3 scripts/check.py --fixtures` shows each one failing, and the library itself still prints `check: ok`
- Verify on: repo
- Evidence: Matrix: "Quality level or score per entry" (Us Y, set by hand; cobus Y, and its CI fails a stable template under 80). RUBRIC.md stage 2 names these fields; check.py checks files, frontmatter and evals, but not these fields
- Issue: none yet (promote after merge)
- Order: rubric-check, publish-proof-judge, proof-judge-eval, catalog-json, assay-engineer-bot, publish-night-watch, stack-kitchen-eval
- Tie: none

## Atoms

| Key | Title | State | Confidence | Class | Since | Queue # | Issue | Because |
|-----|-------|-------|------------|-------|-------|---------|-------|---------|
| assay-engineer-bot | Assay Lingxi's Engineer Bot from its template details (`assay-engineer-bot`) | open | medium | host | 2026-09-30 | 7 | - | - |
| catalog-json | Publish a machine-readable `catalog-json` | open | medium | repo | 2026-09-30 | 2 | - | - |
| proof-judge-eval | Run Proof Judge live against its prompts (`proof-judge-eval`) | open | high | eval | 2026-09-30 | 5 | - | - |
| publish-night-watch | Publish Night Watch as a template (`publish-night-watch`) | open | medium | host | 2026-09-30 | 4 | - | - |
| publish-proof-judge | Publish Proof Judge as a template (`publish-proof-judge`) | open | high | host | 2026-09-30 | 3 | - | - |
| rubric-check | Check the routine and plugin fields in CI (`rubric-check`) | open | high | repo | 2026-09-30 | 1 | - | - |
| stack-kitchen-eval | Run the Stack Kitchen seats live in a group (`stack-kitchen-eval`) | open | medium | eval | 2026-09-30 | 6 | - | - |

## Retired

| Key | Title | State | Since | Issue | Because |
|-----|-------|-------|-------|-------|---------|
| none | | | | | |

## Notes

- none
