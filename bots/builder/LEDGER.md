# Ledger: Builder

Each row is a way this bot breaks without its seal. Where the rule came from our own fleet, the evidence names that private charter rule; the history behind it is private, so the row is marked *inferred*. Where we found the crack while writing this bot, the row says so. The eval prompt in the row reproduces the failure, so anyone can check the seal. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | A "should work" change gets reported as done with no proof from the real surface. | Private charter rule "proof against the real surface", *inferred*; repro: [eval](eval.md) prompt 1 | break | new | Proof on the real surface, and "Green unit tests alone are not proof", in [instructions.md](instructions.md) and [skills/proof-bar](skills/proof-bar/SKILL.md). Small. | sealed #2 |
| K-02 | Two writers in one dirty checkout overwrite each other's work. | Private orchestration rule "one writer per dirty worktree", *inferred* | fracture | new | "One writer per dirty checkout: ... stop and say so." Small. | sealed #2 |
| K-03 | A builder that meets two reasonable behaviors picks one on its own. | Private charter rule "if blocked on a product fork, stop and hand back", *inferred*; repro: eval prompt 4 | fracture | new | Stop at a product fork and hand back two options. Small. | sealed #2 |
| K-04 | A failing check gets switched off to turn CI green. | Private charter rule "never weaken a failing check to make it pass", *inferred*; repro: eval prompt 2 | break | new | "Never weaken, skip or delete a check to make it pass." Small. | sealed #2 |
| K-05 | When the machine it proves on is unreachable, a bot reports a proof it never saw. | Private charter rule "if local execution fails, say so and stop; do not fake a proof", *inferred*; repro: eval prompt 3 | break | new | "If you cannot reach the surface you need, say so and stop. Never report a proof you did not see." Small. | sealed #2 |

No eval run yet.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
