---
name: Night Watch
title: Pages each new red once, silent when green
avatar_shape: dome
avatar_color: blue
level: assayed
---

# Night Watch

Watches CI and deploys for the repos you name. When something new goes red it tells the fixer once, with the link and the first error line. When nothing is new it says nothing.

## What it does

- Keeps a seen list on its computer. The first run records every red that already exists and pages nobody.
- Groups failures into classes (the same job failing for the same reason), so ten failed runs of one broken test are one page, not ten.
- Sends the fixer a scoped message: repo, link, failing job, first error line, and the standing rules (branch, PR, no merge, no weakened checks).
- Tells the human, not the fixer, when a host or service is down.

## Who it is for

Anyone with CI on GitHub (and optionally deploys on Vercel) who already has someone or something that fixes reds: a person, a [Builder](../builder/), a coding agent. It fits in the [Ship Crew](../../teams/ship-crew/).

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/night-watch` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then connect the plugins and create the pulse routine from [routines.md](routines.md).

Files: [instructions.md](instructions.md), [skills/red-triage](skills/red-triage/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper; its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds five cracks, each sealed in the text you install:

- The first run floods nobody: existing reds are recorded, not paged.
- One page per failure class, not one per run.
- A host that is down goes to the human, not the code fixer.
- Old failures that rotate back into view never page again.
- Green means silence.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/red-triage/SKILL.md](skills/red-triage/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name.
