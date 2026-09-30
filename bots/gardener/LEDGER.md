# Ledger: Gardener

Each row is a way this bot breaks without its seal. Where the rule came from our own fleet, the evidence names that private charter rule; the history behind it is private, so the row is marked *inferred*. Where we found the crack while writing this bot, the row says so. The eval prompt in the row reproduces the failure, so anyone can check the seal. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | A cleanup PR that bundles many weeds is hard to review and waits. | Private kitchen law "a provable weed, proof pasted" (one per PR), *inferred*; repro: [eval](eval.md) prompt 1 | hairline | new | "Pick exactly one weed"; Never: "Put two weeds in one pull request." Small. | sealed #2 |
| K-02 | A "weed" that is a matter of taste has no proof, and review turns into an argument. | Private kitchen law "provable weed, proof pasted", *inferred*; repro: eval prompt 3 | hairline | new | Proof means a file, a line and a command's output ([skills/pull-one-weed](skills/pull-one-weed/SKILL.md) step 4). Small. | sealed #2 |
| K-03 | A weed that was pulled comes back. | Private kitchen law "a weed that returns twice becomes a check", *inferred*; repro: eval prompt 4 | fracture | new | The second pull adds a check that fails when the weed returns, in the same PR. Small. | sealed #2 |
| K-04 | A rule gets imported from an unnamed video, a source nobody can check. | Private charter rule "never treat unnamed clip videos as sources", *inferred* | fracture | new | Sources: only the repo, its maintainers, or a named, linked public source. Small. | sealed #2 |
| K-05 | A "no callers" search is fooled by code loaded by name, so a live path passes as dead. | Found while writing this bot: step 3's proof would accept it; repro: eval prompt 2 | break | new | Never: "Delete anything you cannot prove is unused." Small. | sealed #2 |

No eval run yet.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
