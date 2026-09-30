---
name: Kitchen
title: Plates, reviews and weeds for one repo
avatar_shape: arch
avatar_color: yellow
level: assayed
---

# Kitchen

The Stack Kitchen seat that plates, reviews and weeds. It checks each up-next Goal before any work starts, sends the owner one card per decision, reviews every Goal PR against its Done-when with PASS or FAIL and paths, and turns a weed that returns twice into a Goal for a check. It never writes the feature and never merges.

## What it does

- **Plate:** checks the Goal's Done-when is checkable, its evidence cited, and nothing merged covers it, then sends one card: Plate it, Make something else next, Park it.
- **Review:** runs the repo's checks on the PR head, reads CI, and checks each Done-when clause against an artifact. PASS or FAIL with paths.
- **Merge OK:** on PASS, one card to the owner: Merge it, Hold, Send it back.
- **Menu order:** follows MENU.md or the owner's labels. Never re-picks by taste.

## Who it is for

Anyone running a [Stack Kitchen](../) for one repo, with the [Desk](../desk/) seat and the group [law](../law.md). On its own, use [Proof Judge](../../../bots/proof-judge/) and [Chief of Staff](../../../bots/chief-of-staff/) instead.

## Install

Create it as part of the kitchen (see [the team README](../README.md)):

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh teams/stack-kitchen/kitchen` prints the command; add `--yes` to run it.
- **By hand:** create a bot named Kitchen and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill and the routines.

Files: [instructions.md](instructions.md), [skills/plate-and-review](skills/plate-and-review/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. Its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds four cracks, each sealed in the text you install: no PASS on green tests alone, no plate with an uncheckable Done-when, no picking by taste, no Menu as a text list.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/plate-and-review/SKILL.md](skills/plate-and-review/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name.
