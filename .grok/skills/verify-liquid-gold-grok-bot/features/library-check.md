# The library check

A reader trusts that every bot and team folder is complete, safe to install and listed in the
catalog. `scripts/check.py` is that promise in code, and `scripts/check.sh` runs it with the
create script dry runs and the issue form parse, the same way CI does.

## Sub-features

- `check-files` every bot folder has its seven files and every team its four.
- `check-frontmatter` `name`, `title` and `level` present, a known level, and a known Grok Bot
  avatar shape and color; a `## Who it is for` section in the card and `## Never` in the
  instructions.
- `check-evals` every eval has Must and Must never lines.
- `check-stage2` every routine table has the stage 2 rows, a Cost line for a schedule or event
  trigger, and plugins.md has `## Ask first rules`.
- `check-links` every relative link in a Markdown file resolves.
- `check-leaks` generic patterns (paths, addresses, emails, chat ids, phone numbers, network
  names, tokens) everywhere; the private list only when `LEAK_LIST` is set.
- `check-style` no em dash anywhere, and no publisher name in template text.
- `check-catalog` CATALOG.md has a row for every bot, team and community page.

## How to get to it (user POV)

- CONTRIBUTING.md, "Test your change locally".

## Driving it with scripts/check.sh

Preconditions:

- The baseline in [README.md](./README.md) holds.

- **Whole check.** Run `bin/prove --pr N --expect <sha>`, or `scripts/check.sh` in a clean
  checkout. Exit code `0`. `check.log` holds `check: ok: <b> bots, <t> teams, <f> files scanned, 0 problems (...)`,
  `ok: <n> bot folders and <t> teams dry-run` and `ok: <k> forms parse`.
- **Read a failure.** `check.py` prints one `path:line: problem` line per finding and exits `1`.
  Each is a FAIL with rung `check`.
- **Stage 2 rules still bite.** Run `python3 scripts/check.py --fixtures`. It prints one or more
  problems for each folder under `scripts/fixtures/` and ends `check: FAIL: 3 fixtures, <n> problems`.
  The exit code is `1` by design; the proof is that no line reads `fixture produced no failure`.
- **Private list.** With `LEAK_LIST` set, the summary reads `private list: <n>` instead of
  `not loaded, set LEAK_LIST`. Without it, say the private list was not checked.
- **Proof.** The command, `check.log` and the exit code, with the head SHA.

## Gotchas

- `--fixtures` always exits `1` because the fixtures are broken on purpose. It is not part of
  `check.sh`; never wire it into CI as a pass or fail gate.
- Any file named `SKILL.md`, `instructions.md`, `routines.md` or `law.md` counts as template
  text, so it must not name the publisher.
- CI cannot run the private list. A green CI run means the generic patterns passed, not the
  private terms.
