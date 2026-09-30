#!/usr/bin/env bash
# Build the gbot command that creates a Grok Bot group from a team folder.
#
#   scripts/create-team.sh teams/<name>          print the commands (dry run, the default)
#   scripts/create-team.sh teams/<name> --yes    create the group
#
# members.txt lists the member bot folders. Create each member first with
# scripts/create-bot.sh; --yes checks that every member exists (read-only) and
# refuses while law.md still holds <placeholders>.
set -euo pipefail

usage() { echo "usage: scripts/create-team.sh teams/<name> [--yes]" >&2; exit 2; }

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
for f in README.md law.md members.txt; do
  [ -f "$dir/$f" ] || { echo "not a team folder (no $f): $dir" >&2; exit 1; }
done
root="$(cd "$(dirname "$0")/.." && pwd)"

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
[ -n "$name" ] || { echo "README.md frontmatter has no name: $dir" >&2; exit 1; }

folders=()
members=()
while IFS= read -r line || [ -n "$line" ]; do
  line="${line%%#*}"
  line="${line//[[:space:]]/}"
  [ -n "$line" ] || continue
  [ -f "$root/$line/README.md" ] || { echo "member folder not found: $line" >&2; exit 1; }
  m="$(field "$root/$line/README.md" name)"
  [ -n "$m" ] || { echo "member has no name in its README.md frontmatter: $line" >&2; exit 1; }
  folders+=("$line")
  members+=("$m")
done < "$dir/members.txt"

n=${#members[@]}
if [ "$n" -lt 2 ] || [ "$n" -gt 6 ]; then
  echo "a group holds two to six bots; $dir/members.txt lists $n" >&2
  exit 1
fi

cmd=(gbot groups create --name "$name")
[ -z "$title" ] || cmd+=(--title "$title")
for m in "${members[@]}"; do cmd+=(--member "$m"); done
cmd+=(--description "$(cat "$dir/law.md")")

placeholders="$(grep -o '<[a-z][a-z /-]*>' "$dir/law.md" | sort -u | tr '\n' ' ' || true)"

if [ "$yes" -eq 1 ]; then
  [ -z "$placeholders" ] || { echo "fill these in $dir/law.md first: $placeholders" >&2; exit 1; }
  command -v gbot >/dev/null || { echo "gbot not found: npm install --global grok-bot-cli" >&2; exit 1; }
  for i in "${!members[@]}"; do
    gbot bots get "${members[$i]}" >/dev/null 2>&1 || {
      echo "member bot not found: ${members[$i]}; create it first: scripts/create-bot.sh ${folders[$i]} --yes" >&2
      exit 1
    }
  done
  "${cmd[@]}"
else
  echo "# 1. Create each member first:"
  for f in "${folders[@]}"; do echo "#    scripts/create-bot.sh $f"; done
  echo "# 2. Then the group:"
  printf '%q ' "${cmd[@]}"
  echo
  [ -z "$placeholders" ] || echo "# fill these in $dir/law.md before --yes: $placeholders"
  echo "# dry run: nothing was created. Add --yes to run it."
fi
