---
name: plate-and-review
description: Use in a Stack Kitchen when a Goal gets up-next (plate it as one card) or a pull request closes a Goal (review it against the Done-when and answer PASS or FAIL with paths).
---

# Plate and review

## When to use it

A Goal issue gets the `up-next` label, a pull request that says Closes #N opens or changes, or the owner asks what is next.

## Inputs and access

- The Goal issue and its Done when section; the pull request and its CI (the GitHub plugin).
- The Menu order: MENU.md at the repo root, or the labels.
- The project's checkout on your computer, if you run its checks.

## Steps

Plate:
1. Read the Done when. Rewrite it in your head as a check someone else runs. If you cannot, it fails the plate.
2. Confirm the evidence cites a source and that no merged PR already does it.
3. Send one card with your recommendation first.

Review:
1. List each Done-when clause.
2. For each, find the artifact in the PR and open it.
3. Run the checks on the PR head, or read their results in CI.
4. Write the verdict.

## Validate

A plate card has three options and one recommendation. A review names a path for every finding and an artifact for every clause marked true.

## Return

Plate:
```
Plate 1 of 1: #<n> <title>
Done when: <one line>
1. Plate it (recommended)
2. Make something else next: #<runner-up>
3. Park it: <reason>
```

Review:
```
PASS | FAIL  #<pr> closes #<n>
- <clause>: <artifact link or "missing">
Findings: <path:line> <what>
```

## Needs approval

Every plate and every merge is the owner's card. The Kitchen never merges.
