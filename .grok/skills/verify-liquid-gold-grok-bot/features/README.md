# Liquid Gold for Grok Bot verification map

This directory is the maintained source for verifying what a user of this library touches:
the bot and team folders they read, the create scripts that turn a folder into the exact
`gbot` command, and the library check that keeps every folder complete and public-safe.
Read the index, then use the matching feature file as the recipe.

## Baseline preconditions

- Python 3 with PyYAML, bash and git.
- The head under review is checked out in a scratch clone by `bin/prove --pr N --expect <sha>`,
  or you are in a clean checkout whose `git rev-parse HEAD` is that SHA.
- No gbot CLI and no signed-in Grok Bot account are used. Nothing in this map runs `--yes`.

## Driving conventions

- Run commands from the repo root of the head under review.
- Treat every command and folder name as literal. Bot folders are `bots/<name>/`; team seats
  are `teams/<team>/<seat>/`; teams are `teams/<team>/`.
- Nothing here changes the repo or any account. A recipe that would create a bot or a group is
  a contribution or the owner's click, not a verification.

## Proof and skip reporting

- CLI proof is the command, its output and its exit code, kept in the run's evidence
  directory (`bin/prove` does this for the check).
- Name the head SHA and the folders checked with every artifact.
- A behavior claim that needs a live bot (an eval prompt answered in a chat) is INCONCLUSIVE
  until the owner pastes that chat; do not report it verified from a dry run.

## Feature entry contract

Each feature file starts with an H1 title and one paragraph describing the user-visible
behavior, then exactly four H2 sections in this order: `Sub-features`,
`How to get to it (user POV)`, `Driving it with <harness>` (starting with `Preconditions:`),
and `Gotchas`.

## Features

- [Build a bot from its folder](./create-bot.md) covers the dry run, the fields it reads from
  the folder, the notes for skills, routines and plugins, and the refusal on a broken folder.
- [Build a team group](./create-team.md) covers the member steps, the group command, and the
  placeholder warning before `--yes`.
- [The library check](./library-check.md) covers required files, frontmatter, evals, stage 2
  routine fields, Ask first rules, links, leak patterns, em dashes, and the catalog rows.
