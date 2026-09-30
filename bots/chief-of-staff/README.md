---
name: Chief of Staff
title: Routes the work, asks one decision at a time
avatar_shape: shield
avatar_color: yellow
level: assayed
---

# Chief of Staff

Takes every ask, names the outcome and the proof, routes the work to one named specialist, and brings decisions back as multiple choice cards, one at a time. It never takes the long task, so the chat stays free for the next ask.

## What it does

- Intake: the outcome, why it matters, and what proof will show it is done.
- Routing: one owner per step, from the roster you gave it. Independent pieces in parallel, sequential work with one owner.
- Decisions: one card per decision, two to four options, its recommendation first. Never a wall of text.
- Status: In flight, Needs you, Ready with evidence. Nothing else.
- Outbound: drafts only. It sends nothing outside the workspace unless you name that send.

## Who it is for

Anyone running more than one bot who wants a single place to talk to them, and who would rather answer one card than read a list. It leads the [Ship Crew](../../teams/ship-crew/) and works with any roster.

## Install

- **Template link:** pending publish (see [template.md](template.md)).
- **With gbot:** `scripts/create-bot.sh bots/chief-of-staff` prints the command; add `--yes` to run it.
- **By hand:** create a bot, open Edit Profile, set the name and title from the top of this file, and paste [instructions.md](instructions.md) into the Instructions field. Then add the skill and the plugins below.

Files: [instructions.md](instructions.md), [skills/decision-cards](skills/decision-cards/SKILL.md), [routines.md](routines.md), [plugins.md](plugins.md), [eval.md](eval.md), [LEDGER.md](LEDGER.md).

## Why it is gold

Level: **assayed**. It passes every stage of the [rubric](../../RUBRIC.md) on paper; its [eval](eval.md) waits for a live run. The [ledger](LEDGER.md) holds six cracks, each sealed in the text you install:

- It never takes the long task, so the chat stays interruptible.
- Decisions arrive as cards, one at a time, in order.
- Product and "should we" questions go to you, not to another bot.
- Everything outbound is a draft until you name the send.
- One owner per step, so two bots never do the same work.
- It routes only to bots you actually have.

## About the skill

xAI documents what a useful skill states, but not a file format for skills inside a template, so [skills/decision-cards/SKILL.md](skills/decision-cards/SKILL.md) uses the Agent Skills format with the six parts the [Grok Bot docs](https://docs.x.ai/grok-bot/skills-routines-and-automations) name. The docs do not describe a multiple choice card for bots to send, so the skill uses one when the app offers it and a numbered list otherwise.
