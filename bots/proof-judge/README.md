---
name: Proof Judge
title: PASS or FAIL against the Done-when, with paths
avatar_shape: gem
avatar_color: green
level: assayed
---

# Proof Judge

Reviews a pull request as a new pair of eyes and answers PASS or FAIL against its Done-when, with file paths and the exact proof that is missing. It never writes the feature it judges.

## What it does

- Reads the diff from the start, without leaning on the author's summary.
- Checks the repo's own gates on the PR head, then the Done-when against real evidence: a log, a command's output, a file path, a screenshot of the running product, a hosted preview.
- Catches working but wrong: code that passes its tests and still misses the Done-when.
- Answers in one word first, then findings with paths, then the missing proof, then the smallest change that would turn a FAIL into a PASS.

## Who it is for

Anyone who ships through pull requests and has a builder (a person, a coding agent, another bot) whose work needs a second look before a human merges. It pairs with [Builder](../builder/) and sits in the [Ship Crew](../../teams/ship-crew/).

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/proof-judge` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill, the routine and the plugins below.

Files: [instructions.md](instructions.md), [skills/proof-review](skills/proof-review/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper, and its [eval](eval.md) is written and waits for a live run. The [ledger](LEDGER.md) holds five cracks, each sealed in the text you install:

- It never passes the author's report through as its verdict.
- Green unit tests alone never earn a PASS.
- It never writes the fix, so it stays independent.
- A FAIL always names paths and the missing artifact.
- A hard gate the owner named is a FAIL, never a warning.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template. So [skills/proof-review/SKILL.md](skills/proof-review/SKILL.md) uses the Agent Skills format (a `SKILL.md` with `name` and `description` frontmatter) and carries the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name: when to use it, inputs and access, the steps, how to validate, what to return, and what needs approval.

## Credits

The proof bar (real product chrome; captions and mocks are not proof) follows the one Lingxi Li published in [Lingxi's Engineer Bot](../../community/engineer-bot.md).
