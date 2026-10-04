# Build a team group

A user picks a team folder and runs `scripts/create-team.sh` on it. The script prints the
create-bot step for each member seat, then the one `gbot groups create` command for the
group with the law as its description, warns about any `<placeholder>` left in `law.md`, and
says that nothing was created.

## Sub-features

- `team-members` lists one `scripts/create-bot.sh` line per member in `members.txt`.
- `team-group` prints the `gbot groups create` command with name and title from the README
  frontmatter, one `--member` per member, and `law.md` as the description.
- `team-placeholders` names every `<placeholder>` still in `law.md`; `--yes` refuses while any
  remain.

## How to get to it (user POV)

- README.md, "Install a bot", way 2: `scripts/create-team.sh teams/<name>`.

## Driving it with scripts/create-team.sh

Preconditions:

- The baseline in [README.md](./README.md) holds.

- **Dry run.** Run `scripts/create-team.sh teams/<team>`. Exit code `0`. The output starts with
  `# 1. Create each member first:`, lists `scripts/create-bot.sh teams/<team>/<seat>` for each
  seat, then `# 2. Then the group:` and a line starting with `gbot groups create --name`. The
  last line reads `# dry run: nothing was created. Add --yes to run it.`
- **Members.** Compare the `--member` flags with `teams/<team>/members.txt`.
- **Placeholders.** For a template team, a line starting `# fill these in teams/<team>/law.md before --yes:`
  names each placeholder. `teams/stack-kitchen` names `<base branch>` and `<owner/repo>`.
- **Proof.** Save the dry run to `<evidence>/team-<team>.txt`, with the head SHA.

## Gotchas

- Never run `--yes` to verify. It checks the members exist on the signed-in account and then
  creates a real group.
- A seat that lives only in a team is a bot folder under `teams/<team>/`; it is dry-run by
  `create-bot.sh`, not by `create-team.sh`.
