# Ledger: Playbook Keeper

Each row is a way this bot breaks without its seal. Where the rule came from our own fleet, the evidence names that private charter rule; the history behind it is private, so the row is marked *inferred*. Where the rule comes from a public guide or we found the crack while writing this bot, the row says so. The eval prompt in the row reproduces the failure, so anyone can check the seal. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | A fix that lives only in chat is gone next run, so the same miss repeats. | Private charter rule "patch the skill or rule when a worker failed the same way twice", *inferred*; repro: [eval](eval.md) prompt 1 | fracture | new | Every repeated miss becomes a file change with a "will not recur" line ([skills/encode-the-miss](skills/encode-the-miss/SKILL.md)). Small. | sealed #2 |
| K-02 | The keeper opens tickets for exploration nobody finished or decided. | Private charter rule "never invent tickets for unfinished exploration", *inferred*; repro: eval prompt 2 | hairline | new | Never: "Open tickets for exploration that is not done." Small. | sealed #2 |
| K-03 | The keeper starts fixing the product and stops keeping the playbook. | Private charter rule "you do not ship features", *inferred*; repro: eval prompt 3 | hairline | new | Never: "Ship features or fix the product bug yourself." Small. | sealed #2 |
| K-04 | A postmortem written without the reasoning trace blames the wrong step. | Public guide: [Grok Bot for Engineering](https://x.ai/bot/guides/grok-bot-for-engineering), the operations bot "digs into the reasoning that led to the issue"; repro: eval prompt 4 | fracture | new | How you work, step 1: read the transcript and reasoning first; Never: blame without evidence. Small. | sealed #2 |

No eval run yet.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
