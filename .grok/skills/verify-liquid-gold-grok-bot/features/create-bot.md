# Build a bot from its folder

A user picks a bot folder and runs `scripts/create-bot.sh` on it. The script prints the one
`gbot bots create` command that would build the bot (name, title and avatar from the README
frontmatter, instructions from `instructions.md`), then notes where the skills, routines and
plugins go, and says that nothing was created. Only `--yes` runs it.

## Sub-features

- `bot-dry-run` prints the command and creates nothing by default.
- `bot-fields` reads `name`, `title`, `avatar_shape` and `avatar_color` from the `README.md`
  frontmatter and the instructions from `instructions.md`.
- `bot-notes` prints one note each for skills, routines and plugins.
- `bot-refuse` refuses a folder with no `README.md` or `instructions.md`, and any unknown flag.

## How to get to it (user POV)

- README.md, "Install a bot", way 2: `scripts/create-bot.sh bots/<name>`.
- A team seat: `scripts/create-bot.sh teams/<team>/<seat>`, as `create-team.sh` tells the user.

## Driving it with scripts/create-bot.sh

Preconditions:

- The baseline in [README.md](./README.md) holds.
- You know which bot folders the change touched.

- **Dry run.** Run `scripts/create-bot.sh bots/<name>`. Exit code `0`. The first line starts
  with `gbot bots create --name`, and the last line reads
  `# dry run: nothing was created. Add --yes to run it.`
- **Fields.** Compare the printed `--name`, `--title`, `--avatar-shape` and `--avatar-color`
  with the `name`, `title` and avatar lines at the top of `bots/<name>/README.md`, and the
  `--description` text with `bots/<name>/instructions.md`.
- **Notes.** The output has lines starting `# skill:` (one per skill folder), `# routines:` and
  `# plugins:` that name files inside that folder.
- **Refusal.** Run `scripts/create-bot.sh community`. Exit code `1` and
  `not a bot folder (no instructions.md): community` on stderr. Run
  `scripts/create-bot.sh bots/<name> --help`. Exit code `2` and the usage line.
- **Every folder.** `scripts/check.sh` dry-runs every bot and seat; its line
  `ok: <n> bot folders and <t> teams dry-run` covers them all.
- **Proof.** Save the dry run: `scripts/create-bot.sh bots/<name> > <evidence>/create-<name>.txt`,
  with the head SHA.

## Gotchas

- Never run `--yes` to verify. It creates a real bot on whatever account gbot is signed in to.
- gbot 0.2.3 sent a create request on `gbot bots create --help` (LEDGER.md K-01); the script
  never passes `--help` to gbot, and that must stay true.
- Instructions must open with a letter: gbot rejects a flag value that starts with a dash
  (K-03). `check.py` fails such a folder before the dry run would show it.
