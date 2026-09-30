#!/usr/bin/env bash
# Build the gbot command that creates a Grok Bot from a bot folder.
#
#   scripts/create-bot.sh bots/<name>          print the command (dry run, the default)
#   scripts/create-bot.sh bots/<name> --yes    run it
#
# The name, title and avatar come from the README.md frontmatter. The
# instructions come from instructions.md, passed as --description, which is the
# Instructions field in the app (gbot 0.2.3 and 0.11.2 both read it). Skills and
# routines are not created here: the printed notes say where they go.
set -euo pipefail

usage() { echo "usage: scripts/create-bot.sh bots/<name> [--yes]" >&2; exit 2; }

dir=""
yes=0
for arg in "$@"; do
  case "$arg" in
    --yes) yes=1 ;;
    -*) usage ;;
    *) [ -z "$dir" ] || usage; dir="${arg%/}" ;;
  esac
done
[ -n "$dir" ] || usage
for f in README.md instructions.md; do
  [ -f "$dir/$f" ] || { echo "not a bot folder (no $f): $dir" >&2; exit 1; }
done

# field FILE KEY: print KEY's value from the file's leading --- frontmatter block.
field() {
  awk -v k="$2" '
    NR == 1 { if ($0 != "---") exit; next }
    $0 == "---" { exit }
    { i = index($0, ":"); if (i && substr($0, 1, i - 1) == k) {
        v = substr($0, i + 1); sub(/^[ \t]+/, "", v); sub(/[ \t]+$/, "", v); print v; exit } }
  ' "$1"
}

name="$(field "$dir/README.md" name)"
title="$(field "$dir/README.md" title)"
shape="$(field "$dir/README.md" avatar_shape)"
color="$(field "$dir/README.md" avatar_color)"
[ -n "$name" ] || { echo "README.md frontmatter has no name: $dir" >&2; exit 1; }

cmd=(gbot bots create --name "$name")
[ -z "$title" ] || cmd+=(--title "$title")
cmd+=(--description "$(cat "$dir/instructions.md")")
[ -z "$shape" ] || cmd+=(--avatar-shape "$shape")
[ -z "$color" ] || cmd+=(--avatar-color "$color")

notes() {
  if [ -d "$dir/skills" ]; then
    for s in "$dir"/skills/*/; do
      [ -f "$s/SKILL.md" ] || continue
      echo "# skill: add ${s%/} in the app (Marketplace, Your plugins, Private skills), or with gbot 0.11.2 or later: gbot skills add ${s%/} (skills are account-wide)"
    done
  fi
  echo "# routines: set them in the app from $dir/routines.md, then use Test run before you enable one"
  echo "# plugins: connect the ones in $dir/plugins.md and add its Ask first rules"
}

if [ "$yes" -eq 1 ]; then
  command -v gbot >/dev/null || { echo "gbot not found: npm install --global grok-bot-cli" >&2; exit 1; }
  "${cmd[@]}"
  notes
else
  printf '%q ' "${cmd[@]}"
  echo
  notes
  echo "# dry run: nothing was created. Add --yes to run it."
fi
