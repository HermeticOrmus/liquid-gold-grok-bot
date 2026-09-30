---
name: Pantry Researcher
title: Stocks cited research and checkable Goal atoms
avatar_shape: cylinder
avatar_color: cyan
level: assayed
---

# Pantry Researcher

Stocks the pantry for one product: a competitor map, a public mine of what people said, a people mine of what the product's own users said, and a queue of Goal atoms, each with a Done-when someone else can check. Every row cites a source it actually opened. It decides nothing and contacts nobody.

## What it does

- Reads the product as it is now, then writes four dated files.
- Fills a capabilities matrix with Y, N, P and ?, and a source for every claimed cell.
- Logs every search, including the empty ones, and every source it could not reach.
- Proposes five to eight Goal atoms, each checkable on the product itself.
- Opens the stock as a pull request or a draft for a person to review.

## Who it is for

Maintainers and product owners who want the next work to come from evidence instead of a hunch, and anyone running a [Stack Kitchen](../../teams/stack-kitchen/), whose Menu reads this pantry. This repo's own [pantry](../../pantry/) was stocked this way.

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/pantry-researcher` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill and the plugins below.

Files: [instructions.md](instructions.md), [skills/stock-the-pantry](skills/stock-the-pantry/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper; its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds five cracks, each sealed in the text you install:

- No invented numbers, stars, dates, quotes or links. Unknown is `?`.
- Every search is logged, the empty ones too, so a reader can judge coverage.
- A person's words are evidence, never a target.
- Every atom's Done-when can be checked by someone who did not build it.
- `none` is an honest answer.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/stock-the-pantry/SKILL.md](skills/stock-the-pantry/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name.
