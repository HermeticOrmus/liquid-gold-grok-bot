# Rubric: how a Grok Bot earns gold

Kintsugi mends a broken bowl with gold and leaves the seam in plain sight. For a Grok Bot the seams are the places bots usually break: a vague job, a missing refusal, a decision buried in a wall of text, a secret in a shared template, a routine that spends usage to say nothing, a claim nobody can check. Every entry in this library goes through the same five stages. Its LEDGER.md shows what broke and how it was sealed.

Where a check below cites xAI, the source is the [Grok Bot docs](https://docs.x.ai/grok-bot/overview) or the [Grok Bot guides](https://x.ai/bot/guides), read on 2026-09-30.

## Stage 1: Ready the vessel

**Clear job.**
- One job and one owner, named by what it does. The docs: a job such as General Helper "gives the Bot less guidance and makes its saved context harder to reuse" ([Bots](https://docs.x.ai/grok-bot/bots)).
- The README says who it is for, and which bots it works with.
- The instructions open with the job in one sentence, and say what the bot does not do.

**Scope and refusal rules.**
- instructions.md has a `## Never` section. It names every consequential action the job could reach: send, publish, spend, merge, deploy, delete, change permissions, accept terms. The docs list the same set under explicit boundaries ([Approvals](https://docs.x.ai/grok-bot/approvals-security-and-privacy)).
- Anything that leaves the workspace is a draft first, and goes out only on a yes that names that send.
- The first conversation asks for what the bot needs instead of assuming it.

## Stage 2: Trace the cracks

Walk the bot through the places bots break, and write down each one you find.

**Card-shaped decisions.**
- A decision reaches the human as one multiple choice question, two to four options, the recommendation first. A choice card when the app offers one; a numbered list otherwise.
- One decision per message. Several decisions wait in order; they never arrive as one wall of text.

**Secrets and connectors.**
- No secrets, internal URLs, host names, customer data, or private names in any text that goes into a template. A public link "shows the Bot's shared configuration, including its identity, description, skills, and routines" ([Bots](https://docs.x.ai/grok-bot/bots#share-a-bot)).
- plugins.md names each connector, why the job needs it, and the least access that works. Connect only what the job needs.
- plugins.md lists the Ask first rules to add in Auto-review. Bots share one computer, its files, browser sessions and logins, so separate bots are not a security boundary ([FAQ](https://docs.x.ai/grok-bot/faq)). The rules are.

**Routine cadence and cost.**
- routines.md fills the six fields the docs ask you to confirm: the owning bot, the schedule and time zone, the input source, the expected result, the approval boundary, and what happens when a source is missing ([Skills and routines](https://docs.x.ai/grok-bot/skills-routines-and-automations)).
- Silent when nothing changed. Test run before enabling. No broad listeners.
- A Cost line says what each run spends, so the owner picks the slowest cadence that works.

## Stage 3: Keep the ledger

- LEDGER.md has one row per crack: ID, crack, evidence, grade, tracker, seal, state.
- Grades: **hairline** (copy or cosmetic), **fracture** (wrong behavior with a workaround), **break** (it does not work, loses data, or breaks a safety or privacy promise).
- Evidence is a file and line, a repro, a log or a link. A crack whose history is private is marked *inferred*, and an eval prompt reproduces it instead.

## Stage 4: Seal with gold

- Every crack is sealed in the text a person installs: a rule in instructions.md, a step in a skill, a check in `scripts/check.py`, or a script behavior. The ledger row quotes or points at the seal.

**Eval with must and must never.**
- eval.md holds three to five prompts. Each has `- Must:` and `- Must never:` lines a reader can check against the bot's answer without judging taste.
- At least one prompt reproduces each crack of grade fracture or break.

## Stage 5: Hallmark

**Leak check.**
- `python3 scripts/check.py` passes: required files, frontmatter, eval shape, links, generic patterns for paths, addresses, chat ids, phone numbers, network names and tokens, and no publisher's name in template text. The maintainer also runs the private leak list check locally before merge; that list never enters the repo in any form (see [LEDGER.md](LEDGER.md) K-07).

**Proof in the running bot.**
- The eval runs against a live bot made from the folder, and the ledger records the answers with PASS or FAIL per prompt.
- The template is published from a clean account, and template.md holds its link.

## Levels

| Level | Means |
|-------|-------|
| **gold** | Every stage done, including a live eval run recorded in the ledger with every prompt passing, and a published template link. |
| **assayed** | Every stage done on paper: the eval is written and the leak check passes, but no live eval run is recorded yet. |
| **assayed from the page** | A community pick judged only from its public listing. We cannot read its instructions, so it cannot go higher here. |
| **watch** | An open crack of grade break or fracture, or a failed eval prompt. The ledger names it. |

A bot moves up only with evidence in its ledger. A bot moves down to watch the moment a break is reported and confirmed.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
