---
name: proof-review
description: Use when a pull request needs a PASS or FAIL against its Done-when. Reads the diff fresh, checks the gates and the evidence, and returns a verdict with paths and the missing proof.
---

# Proof review

## When to use it

Someone hands you a pull request and asks whether it is done, or a routine fires because a pull request opened or changed.

## Inputs and access

- The pull request link or number, and read access to the repo (the GitHub plugin).
- The Done-when. Look in the PR body, then the issue it closes, then ask. Stop and ask if none exists.

## Steps

1. Open the diff. List the files it changes. Read each change without reading the PR's own summary.
2. Read the CI status for the head commit. Note any failing or missing check by name.
3. Find the repo's check command (README, CONTRIBUTING, CI config). If you can run it on your computer, run it on the PR head and keep the output.
4. For each clause of the Done-when, find the artifact that shows it true. Open links yourself. Write down which clauses have no artifact.
5. Read the change for working but wrong: behavior the tests do not cover, a path the Done-when names that the diff never touches.
6. Check the owner's hard gates, if they named any.

## Validate

Before you answer, make sure every FAIL finding has a path, every "missing proof" line names a concrete artifact, and you have not quoted the author's summary as evidence.

## Return

```
PASS | FAIL
Findings:
- path/to/file:line  what is wrong
Missing proof:
- the artifact that would settle it
To pass:
- the smallest change
```

## Needs approval

Posting the verdict on GitHub as a comment or review. Merging is never yours.
