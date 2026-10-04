#!/usr/bin/env bash
# The one check for this library. CI runs it on every pull request and on every
# push to main (.github/workflows/check.yml). Run it before you open a pull request.
#
#   1. scripts/check.py: files, frontmatter, evals, routine fields, ask first,
#      links, generic leak patterns, em dashes (and the private list when the
#      maintainer sets LEAK_LIST to a file outside the repo).
#   2. Every create script dry-runs: create-bot.sh for every bot and team seat,
#      create-team.sh for every team. Nothing is created.
#   3. The issue forms parse as YAML.
#
# Usage: scripts/check.sh
# Needs Python 3 with PyYAML, and bash. Exits non-zero on the first step that fails.
set -euo pipefail
IFS=$'\n\t'
cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "== library"
python3 scripts/check.py
echo "== create scripts (dry run)"
n=0
for d in bots/*/ teams/*/*/; do
  [ -f "$d/instructions.md" ] || continue
  bash scripts/create-bot.sh "$d" > /dev/null
  n=$((n + 1))
done
t=0
for d in teams/*/; do
  bash scripts/create-team.sh "$d" > /dev/null
  t=$((t + 1))
done
echo "ok: $n bot folders and $t teams dry-run"
echo "== issue forms"
python3 -c "import sys, yaml; [yaml.safe_load(open(f)) for f in sys.argv[1:]]; print('ok: %d forms parse' % len(sys.argv[1:]))" .github/ISSUE_TEMPLATE/*.yml
