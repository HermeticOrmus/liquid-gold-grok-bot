# Contributing

Pick a crack. Seal it with gold.

This library gets better one crack at a time: someone finds where a bot breaks, shows the evidence, and the fix goes into the text people install, in plain sight in the bot's ledger. You do not need to write code to help.

## Ways to contribute

### Take a Menu item

The next work comes from the [pantry](pantry/), in the open. [pantry/MENU.md](pantry/MENU.md) orders the Goal atoms and names one as up next. Open ones are also issues with the `menu` label: [open Menu issues](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues?q=is%3Aopen+label%3Amenu), and [good first issues](https://github.com/HermeticOrmus/liquid-gold-grok-bot/contribute). Claim one by commenting on it, then open a pull request that says `Closes #N`. Each item's Done-when is the check your PR has to show true.

### Report a crack

Use the [crack form](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues/new?template=crack.yml). A crack is a place where an entry breaks: a bot that sent without asking, a skill step that misleads, a script that does the wrong thing, a doc line that is not true. The best evidence is the prompt you sent and the answer you got, a command and its output, or a link. Grade it:

- **hairline**: copy or cosmetic.
- **fracture**: wrong behavior with a workaround.
- **break**: it does not work, loses data, or breaks a safety or privacy promise.

### Seal a crack

Pick an open row in any `LEDGER.md`, or an open issue with the `crack` label, and fix it:

1. Seal it in the text people install: a rule in `instructions.md`, a step in a skill, a check in `scripts/check.py`, or a script behavior.
2. Add an eval prompt to that folder's `eval.md` that fails without your seal and passes with it (`- Must:` and `- Must never:` lines).
3. Update the ledger row: the seal in one line, and the state `sealed #<your PR>`. A new crack gets the next free ID; IDs are never reused.

### Nominate a bot or template

Use the [nomination form](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues/new?template=nominate.yml): the link, the job, why it is gold, and any cracks you know. A community pick gets a credited card in [community/](community/) built only from what its public page shows. We never copy another creator's instructions.

### Share your own template

Add a folder under `bots/<name>/` with the layout below and open a pull request. If you already published it, put the `https://x.ai/bot/...` link in `template.md`. Before you share anything: no secrets, internal links, host names, customer data or people's names. A shared template shows its configuration to anyone with the link.

### Share what you built

Tell us in [Discussions](https://github.com/HermeticOrmus/liquid-gold-grok-bot/discussions) (Show and tell), or leave [feedback](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues/new?template=feedback.yml).

## Layout

A bot folder, `bots/<name>/`:

| File | Holds |
|------|-------|
| `README.md` | Frontmatter (`name`, `title`, `avatar_shape`, `avatar_color`, `level`), then the card: what it does, `## Who it is for`, install, why it is gold. |
| `instructions.md` | The exact Instructions text. It opens with a sentence and has a `## Never` section. |
| `skills/<skill>/SKILL.md` | Optional. Agent Skills format: `name` (the folder name) and `description` frontmatter, then when to use it, inputs and access, steps, validate, return, needs approval. |
| `routines.md` | Each routine's owning bot, trigger, schedule and time zone, input, result, approval boundary, missing source, and cost. |
| `plugins.md` | Each connector, why, the access it needs, and the Ask first rules. |
| `eval.md` | Three to five `### ` prompts, each with `- Must:` and `- Must never:` lines. |
| `LEDGER.md` | The cracks, with evidence, grade, seal and state, closed by the kintsugi mark. |
| `template.md` | The Add to Grok Bot link, or `pending publish`. |

A team folder, `teams/<name>/`: `README.md` (frontmatter `name`, `title`; how to create the group), `law.md` (the group's instructions), `members.txt` (one member bot folder per line, two to six), `LEDGER.md`, and any seats that live only in that team.

Avatar shapes: blob, pebble, bean, egg, squircle, tablet, capsule, cylinder, hex, gem, crystal, wedge, shield, dome, arch, cloud, teardrop, leaf. Colors: black, brown, red, orange, yellow, green, cyan, blue, violet, magenta, gray.

### Test your change locally

From the repo root:

```bash
python3 scripts/check.py                       # files, frontmatter, evals, routine fields, ask first, links, leaks, em dashes
python3 scripts/check.py --fixtures            # one broken bot folder per stage 2 rule, each one failing
scripts/create-bot.sh bots/<name>              # prints the gbot command; creates nothing
scripts/create-team.sh teams/<name>            # prints the member and group commands
python3 -c "import sys, yaml; [yaml.safe_load(open(f)) for f in sys.argv[1:]]" .github/ISSUE_TEMPLATE/*.yml
scripts/check.sh                               # the check, the dry runs and the forms in one command, the way CI runs them
```

The dry runs show exactly what `--yes` would run against your own Grok Bot account. To try a bot for real, run it with `--yes` (it needs the [gbot CLI](https://github.com/ScriptedAlchemy/grok-bot-cli), 0.11.2 or later, and a signed-in Grok Bot app), then run its `eval.md` prompts in a fresh chat.

CI runs `scripts/check.sh` on every pull request and on every push to main (`.github/workflows/check.yml`). A first-time contributor's CI run waits for a maintainer to approve it.

## House rules

- Plain sentences in the reader's words. No marketing words, no emojis, no em dashes.
- Never invent a number, a star count, a date or a quote. Quote only from a page you opened, with its link. Unknown is `?`.
- Never copy another creator's instructions. Credit, link, and describe what anyone can see.
- Commits follow `type(scope): summary` (for example `fix(night-watch): page once per failure class`).
