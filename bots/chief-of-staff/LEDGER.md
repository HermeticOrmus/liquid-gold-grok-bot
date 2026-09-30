# Ledger: Chief of Staff

Each row is a way this bot breaks without its seal. Where the rule came from our own fleet, the evidence names that private charter rule; the history behind it is private, so the row is marked *inferred*. Where we found the crack while writing this bot, or in public docs, the row says so. The eval prompt in the row reproduces the failure, so anyone can check the seal. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | A chief of staff that takes the long task goes dark, and the next ask has nobody to take it. | Private charter rule "keep this chat interruptible; if you take the long task, the captain has no liaison", *inferred*; repro: [eval](eval.md) prompt 5 | fracture | new | "You do not take the long task" and "Keep this chat free" in [instructions.md](instructions.md). Small. | sealed #2 |
| K-02 | A menu of choices sent as a text list gets skimmed and answered wrong. | Private kitchen rule "never send a Menu as a text list; multiple choice cards", *inferred*; repro: eval prompt 2 | fracture | new | Decisions as cards, one at a time ([skills/decision-cards](skills/decision-cards/SKILL.md)). Small. | sealed #2 |
| K-03 | Several decisions in one message get one answer meant for only one of them. | Private charter rule "one decision at a time", *inferred*; repro: eval prompt 2 | fracture | new | "If there are five, send the first and hold the rest in order." Small. | sealed #2 |
| K-04 | An outbound message leaves the workspace without the captain seeing it. | Private kitchen law "draft-only for any outside send", *inferred*; repro: eval prompt 3 | break | new | Never without a yes: send anything outside the workspace. Draft first. Small. | sealed #2 |
| K-05 | Two bots get the same step and do duplicate work. | [Grok Bot docs](https://docs.x.ai/grok-bot/chat-and-collaboration): "Ask for a single owner at each stage. Too many parallel handoffs can create duplicate work and noisy updates." | hairline | new | "Never two owners on one step." Small. | sealed #2 |
| K-06 | A routing table copied from someone else's fleet names bots the new owner does not have. | Found while writing this bot: our private route table named our own seats | fracture | new | The roster is built in the first conversation and read before every routing call. Small. | sealed #2 |

No eval run yet.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
