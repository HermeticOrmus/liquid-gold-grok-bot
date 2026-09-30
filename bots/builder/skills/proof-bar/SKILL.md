---
name: proof-bar
description: Use before you report any code change as done. Picks the proof that fits the change, captures it from the real surface, and writes the PR body around it.
---

# Proof bar

## When to use it

You finished a change and are about to open a pull request or say it is done.

## Inputs and access

- The outcome and the proof the owner asked for.
- Your checkout of the repo on your computer, and a way to run it (a test command, a dev server, a preview link).

## Steps

1. Match the proof to the change. Logic: the test that fails before and passes after. Command line: the command and its output. Screen: a screenshot or short recording of the running product showing the change. Deploy: the preview link, opened by you.
2. Capture it from the real surface. Open the screenshot or the link yourself and check it shows the change.
3. Run the repo's own checks and keep the output.
4. Write the PR body: What changed, How I proved it (the artifact inline or linked), Risk left, and `Closes #N` when an issue exists.

## Validate

The artifact shows the outcome the owner named, not a neighbor of it. If you could not produce it, the PR says "Not proven:" and why, and you do not call it done.

## Return

The PR link and one line: what changed and the proof type.

## Needs approval

Merging, deploying, force-pushing, and any paid agent launch.
