---
name: pull-one-weed
description: Use on each Gardener run to find one provable weed in a repo, prove it, fix it on a branch, and open one pull request with the proof before and after.
---

# Pull one weed

## When to use it

On each Gardener run, or when the owner asks for a cleanup.

## Inputs and access

- The repo and its base branch; a checkout on your computer.
- Your pulled and rejected lists.
- The GitHub plugin to push a branch and open a pull request.

## Steps

1. Update the checkout to the base branch.
2. Read the repo's rules and CI config.
3. Look in this order and stop at the first weed you can prove: a rule in the docs that no check enforces; code with no callers; a doc line the code contradicts; a workaround whose reason is gone (its comment names a bug that is fixed); a test with no assertion that can fail.
4. Write the proof before you change anything: the file and line, the command, its output.
5. Fix it on a branch named `garden/<short-weed-name>`. Run the repo's checks.
6. If the pulled list shows the same weed once before, add a check that fails when the weed returns, and show it failing on the old code.
7. Open the pull request and add the weed to the pulled list.

## Validate

The PR changes one weed. The proof before and after are both in the body. The repo's checks pass.

## Return

```
weed: <one line>
proof before: <command> -> <output>
proof after: <command> -> <output>
checks: <command> -> pass
```

Or nothing, when no weed could be proven.

## Needs approval

Merging; deleting anything whose use you could not rule out; any change a user would see.
