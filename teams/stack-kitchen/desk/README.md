---
name: Desk
title: Ships plated Goals for one repo
avatar_shape: tablet
avatar_color: orange
level: assayed
---

# Desk

The Stack Kitchen seat that ships. After the owner plates a Goal, it builds on a branch, proves each Done-when clause, opens a pull request that says `Closes #N`, fixes red CI without weakening checks, and merges only after the owner's OK.

## What it does

- Waits for Plate it. A Goal with `up-next` and no Yes is not its work yet.
- Builds in the project's own checkout, on a branch named for the Goal.
- Pastes an artifact for every clause of the Done-when in the PR body.
- Leaves a Goal an outside contributor claimed to them, and helps if asked.

## Who it is for

Anyone running a [Stack Kitchen](../) for one repo. It works with the [Kitchen](../kitchen/) seat and the group [law](../law.md); on its own, use [Builder](../../../bots/builder/) instead.

## Install

Create it as part of the kitchen (see [the team README](../README.md)):

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh teams/stack-kitchen/desk` prints the command; add `--yes` to run it.
- **By hand:** create a bot named Desk and paste [instructions.md](instructions.md) into the Instructions field.

Files: [instructions.md](instructions.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. Its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds four cracks, each sealed in the text you install: no building before Plate it, every PR closes its Goal, red CI is fixed at the cause, and a claimed Goal is never raced.
