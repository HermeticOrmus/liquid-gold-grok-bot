---
name: red-triage
description: Use on each pulse to decide whether a failed CI run or deploy is new, belongs to a failure class that is already open, or is not a code red at all.
---

# Red triage

## When to use it

On every pulse of the watch routine, and when someone asks "is this red new?".

## Inputs and access

- The seen list file on your computer.
- Read access to the repo's workflow runs (GitHub plugin), and to deploys if a deploy connector is connected.

## Steps

1. For each failed run or errored deploy, build its key: repo, workflow or project, run or deploy id.
2. Skip it if the key is in the seen list, the run was canceled, it is a rerun of a commit already seen, or it started before the watch's first run.
3. Read the first error line of the failing job.
4. Compare with open classes: same job, same first error (ignoring ids, paths under temp folders, timestamps). A match joins that class.
5. No match: open a new class named after the job and the error, for example `build: module not found`.
6. If the error says the provider, runner or host is down (a status page outage, a 5xx from the platform, no runner available), mark it `not code` and route it to the human.
7. Write every key you looked at into the seen list, paged or not.

## Validate

Each new class produces exactly one page. No key is paged twice. A class closes only when a later run of that job passes.

## Return

For a new class, four lines to the fixer:

```
red: <repo> <workflow or project>
link: <run or deploy link>
error: <first error line>
rules: branch, PR, no merge to the default branch, do not weaken the check
```

Otherwise nothing.

## Needs approval

Any rerun, restart, redeploy, rollback, merge or post in a team channel.
