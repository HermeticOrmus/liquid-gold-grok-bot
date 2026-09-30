---
name: Gardener
title: Pulls one provable weed per run, one small PR
avatar_shape: leaf
avatar_color: green
level: assayed
---

# Gardener

Each run it pulls one weed from the repo it tends and opens one small pull request with the proof pasted. A weed is something provably wrong or dead: a rule written down but not enforced, a workaround whose cause is gone, code nothing calls, a doc line the code contradicts, a test that can never fail.

## What it does

- Reads the repo's own rules first, then looks for weeds it can prove with a file, a line and a command.
- Fixes exactly one weed per run on its own branch, and shows the proof before and after.
- Turns a weed that comes back twice into a check, so it cannot come back a third time.
- Stays silent when it finds nothing it can prove.

## Who it is for

Maintainers who want the repo to get a little cleaner on its own without a flood of cleanup PRs to review. It works alone or next to a [Builder](../builder/) and a [Proof Judge](../proof-judge/).

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/gardener` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill, the routine and the plugins below.

Files: [instructions.md](instructions.md), [skills/pull-one-weed](skills/pull-one-weed/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper; its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds five cracks, each sealed in the text you install:

- One weed per PR, so review stays small.
- No weed without proof: taste is not a weed.
- A weed that returns twice becomes a check.
- Rules come only from the repo or a named, linked source.
- Nothing provable means no PR and no message.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/pull-one-weed/SKILL.md](skills/pull-one-weed/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name.

## Credits

The one-cleanup-per-area rhythm is close to Lingxi Li's [Nightly Audit Engineer](../../community/nightly-audit-engineer.md). This bot narrows it to one provable weed per run.
