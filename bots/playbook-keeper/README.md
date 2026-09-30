---
name: Playbook Keeper
title: Turns a repeated miss into a rule that holds
avatar_shape: crystal
avatar_color: violet
level: assayed
---

# Playbook Keeper

When a bot makes the same mistake twice, or you ask for a postmortem, it reads what happened, names the root cause, and drafts the smallest change that makes the miss impossible or loud: a rule in a bot's instructions, a skill, or a check in the repo. It does not ship features.

## What it does

- Reads the transcript, the output and the rule that should have held, before it writes a word.
- Finds where the fix belongs, and prefers a check over a sentence, and a sentence over a reminder.
- Shows you the miss, the evidence, the change, and one sentence of what will not recur. Applies it after your yes.
- Tells the bots the rule affects, in one line.

## Who it is for

Anyone running a few bots who is tired of correcting the same thing twice. It fits in the [Ship Crew](../../teams/ship-crew/) and works with any roster.

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/playbook-keeper` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill and the plugins below.

Files: [instructions.md](instructions.md), [skills/encode-the-miss](skills/encode-the-miss/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper; its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds four cracks, each sealed in the text you install:

- A fix that lives only in chat is gone next run: every repeated miss becomes a file change.
- It opens no tickets for work nobody decided on.
- It never ships the feature itself.
- It reads the reasoning before it blames.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/encode-the-miss/SKILL.md](skills/encode-the-miss/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name.

## Credits

Lingxi Li's [Grok Bot for Engineering](https://x.ai/bot/guides/grok-bot-for-engineering) guide describes an operations bot that digs into a mistake's reasoning, updates the playbook and tells the other bots, "so the same mistake doesn’t happen twice". This bot is our version of that job.
