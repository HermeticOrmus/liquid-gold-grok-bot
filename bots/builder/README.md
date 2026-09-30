---
name: Builder
title: Ships the slice with proof, never merges
avatar_shape: hex
avatar_color: orange
level: assayed
---

# Builder

Takes one named piece of work, ships it on a branch, and opens a pull request with proof from the real surface. It does not pick the product and it never merges.

## What it does

- Confirms the outcome, the repo and branch rule, and the proof the owner expects before it starts.
- Makes the smallest change that meets the outcome, on its own branch, one writer per checkout.
- Proves the change where a user would see it, and says so plainly when it cannot reach that surface.
- Stops at a product fork and hands back the two options.

## Who it is for

Anyone who wants a bot to write code for a repo without handing it the merge button. It is the inner loop: a [Chief of Staff](../chief-of-staff/) or a person hands it work, and a [Proof Judge](../proof-judge/) reviews what it opens.

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/builder` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill and the plugins below.

Files: [instructions.md](instructions.md), [skills/proof-bar](skills/proof-bar/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper; its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds five cracks, each sealed in the text you install:

- "Should work" is never reported as done: proof comes from the real surface.
- One writer per checkout, so two agents never overwrite each other.
- Product forks go back to the owner.
- A failing check is fixed, never weakened.
- When it cannot reach the surface, it says so and stops instead of reporting a proof it did not see.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/proof-bar/SKILL.md](skills/proof-bar/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name.

## Credits

"Do not weaken a failing check" and the real-chrome proof bar match rules Lingxi Li published in [Lingxi's Engineer Bot](../../community/engineer-bot.md).
