---
name: Ship Crew
title: Routes, builds, judges and watches one repo
---

# Ship Crew

Five bots from this library in one group for one repo: a Chief of Staff who routes and asks decisions as cards, a Builder who ships with proof, a Proof Judge who reviews every PR as a new context, a Night Watch who pages new reds once, and a Playbook Keeper who turns a repeated miss into a rule. You are the captain and the only Yes.

## Members

| Seat | Folder | Job |
|------|--------|-----|
| Chief of Staff | [bots/chief-of-staff](../../bots/chief-of-staff/) | Intake, routing, one decision card at a time. |
| Builder | [bots/builder](../../bots/builder/) | Ships the slice on a branch, opens a PR with proof. |
| Proof Judge | [bots/proof-judge](../../bots/proof-judge/) | PASS or FAIL against the Done-when, with paths. |
| Night Watch | [bots/night-watch](../../bots/night-watch/) | Pages the Builder once per new red class. |
| Playbook Keeper | [bots/playbook-keeper](../../bots/playbook-keeper/) | Turns a repeated miss into a rule. |

Five members leave one seat free: a group holds two to six bots.

## How it flows

```
You ask            ->  Chief of Staff names outcome and proof, routes to one owner
Builder ships      ->  PR with proof  ->  Proof Judge: PASS or FAIL with paths
PASS               ->  Chief of Staff: one card to you (Merge it / Hold / Send it back)
CI goes red        ->  Night Watch pages the Builder once for the new class
A miss repeats     ->  Playbook Keeper drafts the one rule; you say yes or no
```

## Create the group

1. **Fill the law.** Replace `<owner/repo>` in [law.md](law.md).
2. **Create the five bots** from their folders: `scripts/create-bot.sh bots/<name>` for each (add `--yes` to run), or by hand. If you already have one of them, reuse it.
3. **Create the group.** `scripts/create-team.sh teams/ship-crew` prints the command; `--yes` checks that all five exist and refuses while the law has placeholders. By hand: New, New chat, select the five bots, then paste [law.md](law.md) into the group's instructions.
4. **Routines.** Night Watch's pulse from [its routines.md](../../bots/night-watch/routines.md). The others work on request.

One crew, one project. For a second repo, create a second crew with its own bots.

## Why it is gold

Level: **assayed**. Every member is assayed on its own, and the [team ledger](LEDGER.md) holds four cracks about how they meet, each sealed in [law.md](law.md).
