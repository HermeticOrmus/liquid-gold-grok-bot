---
name: Stack Kitchen
title: Ships one repo through Goal issues
---

# Stack Kitchen

Two bots and one group law that ship one repo through Goal issues. Every Goal carries a Done-when someone else can check, every decision reaches you as a card, and nothing merges without your OK.

## The loop

```
Goal issue gets up-next  ->  Kitchen plates it: one card to you (Plate it / Make something else next / Park it)
You pick Plate it        ->  Desk ships on a branch, opens a PR that says "Closes #N" with proof
PR opens                 ->  Kitchen reviews: checks, CI, each Done-when clause -> PASS or FAIL with paths
PASS                     ->  one card to you (Merge it / Hold / Send it back)
You pick Merge it        ->  Desk merges; Kitchen plates the next Goal in Menu order
CI goes red on the PR    ->  Desk fixes it on that branch, never by weakening the check
```

## Members

| Seat | Folder | Job |
|------|--------|-----|
| Desk | [desk/](desk/) | Ships a plated Goal: branch, proof, PR, merge after your OK. |
| Kitchen | [kitchen/](kitchen/) | Plates, reviews against the Done-when, weeds. Never writes the feature. |
| You | | The only Yes: plate, paid agent launch, merge, park. |

The group law is [law.md](law.md). It goes into the group's instructions.

## Create the group

1. **Fill the law.** Replace `<owner/repo>` and `<base branch>` in [law.md](law.md) with your repo.
2. **Create the two seats.** `scripts/create-bot.sh teams/stack-kitchen/desk` and `scripts/create-bot.sh teams/stack-kitchen/kitchen` print the commands; add `--yes` to run them. Or create each bot by hand and paste its `instructions.md`.
3. **Create the group.** `scripts/create-team.sh teams/stack-kitchen` prints the command. With `--yes` it checks that both seats exist and refuses while the law still has placeholders. By hand: New, New chat, select Desk and Kitchen, then paste [law.md](law.md) into the group's instructions.
4. **Add the labels** to your repo: `goal`, `up-next`, `pin`, `parked`. With the GitHub CLI: `gh label create goal`, and the same for the other three.
5. **Write the first Goal** as an issue with the `goal` label and a `## Done when` section, and give it `up-next`. The Kitchen plates it.
6. **Routines.** Set the Kitchen's triggers from [kitchen/routines.md](kitchen/routines.md).

One kitchen, one project. For a second repo, create a second pair of seats with their own names (for example "Desk: api" and "Kitchen: api") and a second group. Never put one seat in two kitchens.

## Why it is gold

Level: **assayed**. The law and both seats pass every stage of the [rubric](../../RUBRIC.md) on paper; their evals wait for a live run. The [team ledger](LEDGER.md) holds nine cracks, each sealed in the law or a seat's instructions, and each seat has its own ledger.
