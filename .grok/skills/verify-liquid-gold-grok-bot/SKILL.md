---
name: verify-liquid-gold-grok-bot
description: Prove a head of the Liquid Gold for Grok Bot library (Grok Bot templates and teams as readable folders, with kintsugi ledgers) on its user surface, the create scripts that build gbot commands from a folder. Checks one exact commit in a scratch clone, runs the library check, dry-runs every create script, parses the issue forms, and keeps the log. Use when proving a pull request's Done-when, reproducing a check failure, or showing that main is green.
---

# Verify Liquid Gold for Grok Bot

This repo has no server. What a user touches is a bot or team folder: they read its card,
then build the bot with `scripts/create-bot.sh` (or a group with `scripts/create-team.sh`),
which prints the exact `gbot` command and creates nothing until `--yes`. So the proof is the
library check plus a dry run of every create script, at the exact commit under review.

The one check command is `scripts/check.sh`: `scripts/check.py` (files, frontmatter, evals,
routine fields, Ask first rules, links, generic leak patterns, em dashes), a dry run of every
create script, and a YAML parse of the issue forms. CI runs the same command
(`.github/workflows/check.yml`).

Helper (executable, bash): `.grok/skills/verify-liquid-gold-grok-bot/bin/prove`

```bash
P=.grok/skills/verify-liquid-gold-grok-bot/bin/prove
$P --help
$P --pr 9 --expect <head sha>      # the head under review
$P --ref main                      # what main holds now
$P                                 # this checkout at HEAD (reports dirty: true if edited)
```

One JSON line on stdout (`head`, `source`, `dirty`, `exit`, `evidence`), the check's own
output on stderr. Exit is the check's exit code, 3 when the head is not the expected one.

## Launch

- **Needs:** Python 3 with PyYAML, bash, git, and network access to GitHub for `--pr` and
  `--ref`. No gbot CLI and no Grok Bot account: nothing here runs `--yes`.
- **Head.** `--pr N` clones the public repo into a scratch directory and checks out
  `pull/N/head`; `--ref REF` does the same for a branch or tag. `--expect SHA` refuses any
  other head, so pass the head SHA the review names.
- **Private list.** A maintainer sets `LEAK_LIST` (and `LEAK_ALLOW`) to files outside the
  repo before running `prove`; `check.py` then also fails on private terms. CI never has
  that list. The check's last line says whether the list was loaded.
- **Ready.** There is nothing to wait for. A run is ready to judge when the JSON line prints.
- **Teardown.** `prove` removes its scratch clone on exit. Nothing else is started.

## Doctor

```bash
python3 -c "import yaml" && echo yaml ok       # PyYAML is present
git rev-parse HEAD                             # the head you think you are on
python3 scripts/check.py | tail -1             # the library check alone
```

Run these first when anything looks off. A `ModuleNotFoundError: yaml` is a missing package
on the machine, not a broken issue form.

## Drive

The feature map in [features/README.md](features/README.md) has one recipe per feature.
For a pull request:

1. Read which folders changed: a bot under `bots/`, a team under `teams/`, a page under
   `community/`, or the scripts.
2. Run `prove --pr N --expect <head sha>`. The three sections end in `check: ok: ...`,
   `ok: <n> bot folders and <t> teams dry-run` and `ok: <f> forms parse`.
3. For each bot or team the pull request touched, run its create script dry run from the
   recipe and read the printed command against the folder: the name and title from the
   README frontmatter, the instructions from `instructions.md`, the avatar.
4. A Done-when about how a bot behaves needs that bot's `eval.md` prompts run in a fresh
   chat by the owner; say so and mark the verdict INCONCLUSIVE until that evidence is
   pasted. Never create the bot yourself to get it.

## Evidence

- Each run writes `<evidence>/head.txt` (the head and its subject, the source, dirty or not,
  the Python version), `<evidence>/check.log` (the full check output) and
  `<evidence>/result.json`.
- Evidence lives under `$VERIFY_LIQUID_GOLD_GROK_BOT_HOME`, default
  `${XDG_STATE_HOME:-$HOME/.local/state}/verify-liquid-gold-grok-bot/evidence/<head12>-<stamp>/`.
- Save a dry run you read in step 3 next to it: `scripts/create-bot.sh bots/<name> > <evidence>/create-<name>.txt`.
- A verdict cites the head SHA and pastes the three ok lines. `dirty: true` means the run
  judged a checkout with local edits; never post a verdict from a dirty run.

## Cleanup

`prove` removes what it created. The evidence directory stays. To clear old evidence,
delete directories under `.../verify-liquid-gold-grok-bot/evidence/` by name.

## Maintain

When a folder shape, a script or a rubric rule changes, update its file under `features/`
in the same pull request. A recipe that no longer matches the repo is a crack in this skill:
fix the recipe, not the check.
