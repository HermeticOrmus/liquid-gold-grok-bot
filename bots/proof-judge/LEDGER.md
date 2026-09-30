# Ledger: Proof Judge

Each row is a way this bot breaks without its seal. Where the rule came from our own fleet, the evidence names that private charter rule; the history behind it is private, so the row is marked *inferred*. Where we found the crack while writing this bot, the row says so. The eval prompt in the row reproduces the failure, so anyone can check the seal. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | A reviewer that reads the author's summary first passes it through as its verdict. | Private charter rule "no pass-through of the author's report as your verdict", *inferred*; repro: [eval](eval.md) prompt 2 | fracture | new | "Read the diff yourself... never pass it through as your verdict" in [instructions.md](instructions.md), How you judge, step 1. Small. | sealed #2 |
| K-02 | Green unit tests earn a PASS on a change that is wrong on the real surface. | Private charter rule "never approve on green unit tests alone", *inferred*; repro: eval prompt 1 | break | new | "Green tests alone are not proof", and PASS needs an artifact (How you judge step 3, Verdict). Small. | sealed #2 |
| K-03 | A reviewer that starts fixing the feature stops being independent of it. | Private charter rule "never write the feature yourself", *inferred*; repro: eval prompt 5 | fracture | new | Never: "Write or push the fix yourself." Small. | sealed #2 |
| K-04 | A FAIL without paths cannot be acted on and comes back for a second round. | Private charter rule "concrete findings with paths, and what proof is missing", *inferred* | hairline | new | Verdict shape: findings with paths, missing proof by name, the smallest change to pass. Small. | sealed #2 |
| K-05 | A gate the owner said never to cross gets reported as a concern, and the change merges. | Private charter rule "FAIL, do not soften" on a named gate, *inferred*; repro: eval prompt 4 | break | new | How you judge step 5: a named hard gate is a FAIL, never a warning. Small. | sealed #2 |

No eval run yet. The first live run lands here as an "Eval run" section; see the [pantry queue](../../pantry/2026-09-30-pantry-queue.md).

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
