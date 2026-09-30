# Ledger: Stack Kitchen

Cracks that belong to the kitchen as a whole: the group law and how the two seats meet. Each seat's own cracks are in [desk/LEDGER.md](desk/LEDGER.md) and [kitchen/LEDGER.md](kitchen/LEDGER.md). Where the rule came from our own fleet, the evidence names that private law and the row is marked *inferred*. IDs are never reused.

| ID | Crack | Evidence | Grade | Tracker | Seal | State |
|----|-------|----------|-------|---------|------|-------|
| K-01 | A seat sitting in two project rooms carries notes between projects. | Private ship law "no seat sits in two kitchens; a seat reads, writes and talks only about its own project", *inferred* | break | new | [law.md](law.md): "One kitchen, one project"; the README says a second repo gets a second pair of seats. Small. | sealed #2 |
| K-02 | Separate groups do not keep projects apart on disk: every bot on an account shares one computer, its files, browser sessions and logins. | [Grok Bot FAQ](https://docs.x.ai/grok-bot/faq): "They share its files, browser sessions, and logins"; "Do not use separate Bots as a security boundary." | fracture | new | law.md: "work only inside this project's own checkout folder"; each seat's instructions repeat it. Small. | sealed #2 |
| K-03 | A Goal PR merges on green CI without the owner's OK. | Private ship law "merge only after the explicit OK", *inferred* | break | new | law.md and the Desk: merge only after the owner's OK and the Kitchen's PASS. Small. | sealed #2 |
| K-04 | The next Goal gets picked by taste. | Private ship law "nobody picks the next atom by taste", *inferred* | fracture | new | law.md: the Menu order lives in MENU.md or the labels. Small. | sealed #2 |
| K-05 | A paid cloud agent launches without a yes. | Private ship law "Cloud Agent launch or spend: the explicit 'Yes launch it'", *inferred* | break | new | law.md and the Desk: a paid agent only after "Yes launch it". Small. | sealed #2 |
| K-06 | Both seats answer every message and the group fills with noise. | Private kitchen law "act on the tag addressed to you, once; silent when nothing is yours", *inferred* | hairline | new | law.md: "Act once on a message addressed to you... Silent when nothing is yours." Small. | sealed #2 |
| K-07 | The Desk races an outside contributor who claimed a Goal. | Private kitchen law "a Goal an outside contributor has claimed is theirs", *inferred* | fracture | new | law.md and the Desk's Claimed Goals section. Small. | sealed #2 |
| K-08 | A group created straight from law.md points both seats at the literal text `<owner/repo>`. | Found while writing this team; law.md ships with placeholders | fracture | new | `scripts/create-team.sh --yes` refuses while law.md has placeholders; the dry run lists them. Small. | sealed #2 |
| K-09 | The Menu reaches the owner as a text list. | Private kitchen rule "never send a Menu as a text list", *inferred* | fracture | new | law.md: "Cards to the owner: one decision per card, in pick order." Small. | sealed #2 |

No eval run yet. Running both seats' evals in a real group is a [pantry atom](../../pantry/2026-09-30-pantry-queue.md).

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
