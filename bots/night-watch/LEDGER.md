# Ledger: Night Watch

Each row is a way this bot breaks without its seal. Where the rule came from our own fleet, the evidence names that private charter rule; the history behind it is private, so the row is marked *inferred*. Where we found the crack while writing this bot, the row says so. The eval prompt in the row reproduces the failure, so anyone can check the seal. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | The first run pages every red that already exists, a flood the fixer cannot use. | Private charter rule "first run records current reds and does not page", *inferred*; repro: [eval](eval.md) prompt 1 | fracture | new | "On the first run, record every current red and page nobody." Small. | sealed #2 |
| K-02 | One broken job pages once per run or deploy id, the same failure again and again. | Private playbook rule "one page per open failure class, not per deploy id", *inferred*; repro: eval prompt 2 | fracture | new | Failure classes: a new key in an open class stays silent ([skills/red-triage](skills/red-triage/SKILL.md) step 4). Small. | sealed #2 |
| K-03 | A host outage goes to the code fixer, who cannot fix it. | Private charter rule "host down goes to the host owner, not the fixer", *inferred*; repro: eval prompt 3 | fracture | new | "A host or service that is down is not a code red. Tell the human." Small. | sealed #2 |
| K-04 | Old failures rotate back into the latest-runs window and page again. | Private playbook rule "a stale filter so window churn cannot re-page", *inferred* | hairline | new | Keys are kept, never pruned by a window, and failures that started before the first run are dropped (Each pulse, step 2). Small. | sealed #2 |
| K-05 | Green beats posted into a team channel bury the real messages. | Private charter rules "silent when green" and "do not post the beat into the team channel", *inferred*; repro: eval prompt 4 | hairline | new | "Nothing new: stay silent." Never posts in a team channel without a yes. Small. | sealed #2 |

No eval run yet.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
