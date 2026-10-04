#!/usr/bin/env python3
"""Check the library before it ships.

Run from anywhere: python3 scripts/check.py

It checks that every bot and team folder has its files, that frontmatter is
complete, that every eval has Must and Must never lines, that each routine
table has its stage 2 rows and a Cost line when the trigger names a schedule
or an event, that plugins.md has an Ask first rules section, that relative
links resolve, and that nothing private or em-dashed slipped in. It exits 1
on any failure and prints one line per problem with the file and line.

`python3 scripts/check.py --fixtures` runs only the stage 2 checks against
the broken bot folders in scripts/fixtures/. Those folders sit outside
bots/ and teams/, so a normal run does not treat them as library entries.
"""
import re
import pathlib
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOT_FILES = ["README.md", "instructions.md", "routines.md", "plugins.md",
             "eval.md", "LEDGER.md", "template.md"]
TEAM_FILES = ["README.md", "law.md", "members.txt", "LEDGER.md"]
SHAPES = set("blob pebble bean egg squircle tablet capsule cylinder hex gem "
             "crystal wedge shield dome arch cloud teardrop leaf".split())
COLORS = set("black brown red orange yellow green cyan blue violet magenta gray".split())
LEVELS = {"gold", "assayed", "watch"}
EM_DASH = "\u2014"

# The private leak list never enters this public repo, not even hashed: a
# published hash of a name lets anyone confirm a guess (LEDGER.md, K-07).
# CI runs the generic PATTERNS below. A maintainer also runs the private check
# locally before merging, with LEAK_LIST pointing at a file outside the repo:
#   LEAK_LIST=/path/outside/repo/leak-list.txt python3 scripts/check.py
# One term per line; "people:<name>" is banned only in PEOPLE_SCOPE, every
# other term everywhere; lines starting with # are ignored.
# A line with regex characters is used as a regex; any other line matches as a whole word.
PRIVATE, PEOPLE = [], []
_REGEX_CHARS = set("\\|*+?[](){}^$")
_leak = os.environ.get("LEAK_LIST")
if _leak:
    for _t in pathlib.Path(_leak).expanduser().read_text(encoding="utf-8").splitlines():
        _t = _t.strip()
        if not _t or _t.startswith("#"):
            continue
        _people = _t.lower().startswith("people:")
        _t = _t[len("people:"):].strip() if _people else _t
        _rx = _t if _REGEX_CHARS & set(_t) else r"(?<![\w])" + re.escape(_t) + r"(?![\w])"
        (PEOPLE if _people else PRIVATE).append(re.compile(_rx, re.I))
PEOPLE_SCOPE = ("bots/", "teams/", "community/", "pantry/")
PATTERNS = [
    ("a path under /home or /Users", re.compile(r"/home/|/Users/")),
    ("a home-relative dot path", re.compile(r"~/\.")),
    ("an IPv4 address", re.compile(r"\b\d{1,3}(?:\.\d{1,3}){3}\b")),
    ("an email address", re.compile(r"[\w.+-]+@[\w-]+\.[a-z]{2,}\b", re.I)),
    ("a chat id", re.compile(r"@(?:g|c)\.us\b|@lid\b")),
    ("a phone number", re.compile(r"\+\d{1,3}[\s-]?\d{2,4}[\s-]?\d{3,4}[\s-]?\d{3,4}")),
    ("a private network name", re.compile(r"tailscale|tailnet|\bts\.net\b", re.I)),
    ("a token", re.compile(r"\b(?:sk|xai|ghp|gho|github_pat)[-_][A-Za-z0-9_]{16,}")),
]
# Words that must not reach a template: the text a stranger installs.
TEMPLATE_WORDS = re.compile(r"\b(?:ormus|hermetic\w*)\b", re.I)
LINK = re.compile(r"\]\(([^)\s]+)\)")
# RUBRIC.md stage 2. Each routine table names these rows. Cost is required
# only when that routine's Trigger names a schedule or an event.
ROUTINE_FIELDS = (
    "Owning bot",
    "Trigger",
    "Schedule and time zone",
    "Input",
    "Result",
    "Approval boundary",
    "Missing source",
)
TRIGGER_SPEND = re.compile(r"\b(?:schedules?|events?)\b", re.I)
COST_LINE = re.compile(r"(?m)^\s*Cost:")
ASK_FIRST = re.compile(r"^## Ask first rules\s*$", re.M)
HEADING = re.compile(r"^#{1,6} ")
SEP_CELL = re.compile(r":?-{1,}:?")

problems = []


def fail(path, line, msg):
    rel = path.relative_to(ROOT) if isinstance(path, Path) else path
    problems.append(f"{rel}:{line}: {msg}" if line else f"{rel}: {msg}")


def frontmatter(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0] != "---":
        return None
    out = {}
    for line in lines[1:]:
        if line == "---":
            return out
        key, sep, value = line.partition(":")
        if sep:
            out[key.strip()] = value.strip()
    return None


def check_bot(folder):
    for name in BOT_FILES:
        if not (folder / name).is_file():
            fail(folder, 0, f"missing {name}")
    readme = folder / "README.md"
    if readme.is_file():
        fm = frontmatter(readme)
        if fm is None:
            fail(readme, 1, "no frontmatter block (--- name, title, avatar_shape, avatar_color, level ---)")
        else:
            for key in ("name", "title", "level"):
                if not fm.get(key):
                    fail(readme, 1, f"frontmatter has no {key}")
            if fm.get("level") and fm["level"] not in LEVELS:
                fail(readme, 1, f"level must be one of {sorted(LEVELS)}")
            if fm.get("avatar_shape") and fm["avatar_shape"] not in SHAPES:
                fail(readme, 1, f"avatar_shape {fm['avatar_shape']!r} is not a Grok Bot shape")
            if fm.get("avatar_color") and fm["avatar_color"] not in COLORS:
                fail(readme, 1, f"avatar_color {fm['avatar_color']!r} is not a Grok Bot color")
        if "## Who it is for" not in readme.read_text(encoding="utf-8"):
            fail(readme, 0, "no '## Who it is for' section")
    instr = folder / "instructions.md"
    if instr.is_file():
        text = instr.read_text(encoding="utf-8")
        if not re.match(r"[A-Za-z]", text):
            fail(instr, 1, "must open with a sentence (gbot rejects a flag value that starts with '-')")
        if not re.search(r"^## Never", text, re.M):
            fail(instr, 0, "no '## Never' section")
    ev = folder / "eval.md"
    if ev.is_file():
        check_eval(ev)
    routines = folder / "routines.md"
    if routines.is_file():
        check_routines(routines)
    plugins = folder / "plugins.md"
    if plugins.is_file():
        check_plugins(plugins)
    tpl = folder / "template.md"
    if tpl.is_file():
        text = tpl.read_text(encoding="utf-8")
        if "pending publish" not in text and not re.search(r"https://x\.ai/bot/[A-Za-z0-9_-]{10,}", text):
            fail(tpl, 0, "needs an https://x.ai/bot/ link or the words 'pending publish'")
    skills = folder / "skills"
    if skills.is_dir():
        for sk in sorted(p for p in skills.iterdir() if p.is_dir()):
            md = sk / "SKILL.md"
            if not md.is_file():
                fail(sk, 0, "skill folder without SKILL.md")
                continue
            fm = frontmatter(md)
            if fm is None:
                fail(md, 1, "no frontmatter block")
                continue
            if fm.get("name") != sk.name:
                fail(md, 1, f"frontmatter name must be {sk.name!r}")
            if len(fm.get("description", "")) < 20:
                fail(md, 1, "frontmatter needs a description that says when to use it")


def check_eval(path):
    text = path.read_text(encoding="utf-8")
    parts = re.split(r"^### ", text, flags=re.M)[1:]
    if not 3 <= len(parts) <= 5:
        fail(path, 0, f"needs three to five prompts (### headings), found {len(parts)}")
    for part in parts:
        title = part.splitlines()[0]
        if not re.search(r"^- Must: ", part, re.M):
            fail(path, 0, f"prompt '{title}' has no '- Must: ' line")
        if not re.search(r"^- Must never: ", part, re.M):
            fail(path, 0, f"prompt '{title}' has no '- Must never: ' line")


def team_members(team):
    out = []
    for raw in (team / "members.txt").read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if line:
            out.append(line)
    return out


def check_team(team):
    for name in TEAM_FILES:
        if not (team / name).is_file():
            fail(team, 0, f"missing {name}")
    fm = frontmatter(team / "README.md") if (team / "README.md").is_file() else None
    if fm is None or not fm.get("name"):
        fail(team / "README.md", 1, "frontmatter needs a name")
    if not (team / "members.txt").is_file():
        return []
    members = team_members(team)
    if not 2 <= len(members) <= 6:
        fail(team / "members.txt", 0, f"a group holds two to six bots, found {len(members)}")
    folders = []
    for m in members:
        folder = ROOT / m
        if not (folder / "instructions.md").is_file():
            fail(team / "members.txt", 0, f"{m} is not a bot folder")
        else:
            folders.append(folder)
    return folders


def row_cells(line):
    raw = line.strip()
    if raw.startswith("|"):
        raw = raw[1:]
    if raw.endswith("|"):
        raw = raw[:-1]
    return [cell.strip() for cell in raw.split("|")]


def clean_field(cell):
    return re.sub(r"[*_`]", "", cell).strip()


def iter_tables(lines):
    i = 0
    n = len(lines)
    while i < n:
        if lines[i].lstrip().startswith("|"):
            start = i
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append(lines[i])
                i += 1
            yield start, block
        else:
            i += 1


def routine_rows(block, start):
    """Map stage 2 field names to (line, value) for one table.

    Returns None when the table is not a routine table.
    """
    parsed = []
    for offset, line in enumerate(block):
        cells = row_cells(line)
        if not cells or all(SEP_CELL.fullmatch(cell.replace(" ", "")) for cell in cells):
            continue
        parsed.append((start + offset + 1, cells))
    if not parsed:
        return None
    fields = {}
    saw_header = False
    for line_no, cells in parsed:
        name = clean_field(cells[0])
        if name == "Field":
            saw_header = True
            continue
        if name in ROUTINE_FIELDS and name not in fields:
            value = cells[1].strip() if len(cells) > 1 else ""
            fields[name] = (line_no, value)
    if not fields and not saw_header:
        return None
    return fields


def section_text(lines, index):
    start = 0
    for i in range(index, -1, -1):
        if HEADING.match(lines[i]):
            start = i
            break
    end = len(lines)
    for i in range(index + 1, len(lines)):
        if HEADING.match(lines[i]):
            end = i
            break
    return "\n".join(lines[start:end])


def heading_title(lines, index):
    for i in range(index, -1, -1):
        if HEADING.match(lines[i]):
            return lines[i].lstrip("#").strip()
    return ""


def check_routines(path):
    lines = path.read_text(encoding="utf-8").splitlines()
    tables = []
    for start, block in iter_tables(lines):
        fields = routine_rows(block, start)
        if fields is not None:
            tables.append((start, fields))
    if not tables:
        for field in ROUTINE_FIELDS:
            fail(path, 0, f"no table row for {field}")
        return
    for start, fields in tables:
        title = heading_title(lines, start)
        prefix = f"routine '{title}': " if title else ""
        for field in ROUTINE_FIELDS:
            if field not in fields:
                fail(path, start + 1, f"{prefix}no table row for {field}")
        trigger = fields.get("Trigger")
        if trigger and TRIGGER_SPEND.search(trigger[1]):
            if not COST_LINE.search(section_text(lines, start)):
                fail(path, trigger[0],
                     f"{prefix}Trigger names a schedule or an event and has no Cost: line")


def check_plugins(path):
    text = path.read_text(encoding="utf-8")
    if not ASK_FIRST.search(text):
        fail(path, 0, "no '## Ask first rules' section")


def check_stage2(folder):
    routines = folder / "routines.md"
    if routines.is_file():
        check_routines(routines)
    plugins = folder / "plugins.md"
    if plugins.is_file():
        check_plugins(plugins)


def check_links(path, text):
    for n, line in enumerate(text.splitlines(), 1):
        for target in LINK.findall(line):
            if re.match(r"[a-z]+:", target) or target.startswith("#"):
                continue
            rel = target.split("#", 1)[0]
            if rel and not (path.parent / rel).exists():
                fail(path, n, f"broken link {target}")


def check_text(path, text):
    rel = path.relative_to(ROOT).as_posix()
    people = rel.startswith(PEOPLE_SCOPE)
    template = path.name in ("instructions.md", "routines.md", "law.md", "SKILL.md")
    for n, line in enumerate(text.splitlines(), 1):
        if EM_DASH in line:
            fail(path, n, "em dash")
        if rel == "scripts/check.py":
            continue
        for label, pat in PATTERNS:
            if pat.search(line):
                fail(path, n, f"looks like {label}")
        for rx in PRIVATE + (PEOPLE if people else []):
            if rx.search(line):
                fail(path, n, "a term on the private leak list; rephrase it")
                break
        if template and TEMPLATE_WORDS.search(line):
            fail(path, n, "template text must not name the publisher; keep it brand-neutral")


def run_fixtures():
    root = ROOT / "scripts" / "fixtures"
    folders = []
    if not root.is_dir():
        fail(root, 0, "no fixtures directory")
    else:
        folders = sorted(p for p in root.iterdir() if p.is_dir())
        if not folders:
            fail(root, 0, "no fixture bot folders")
        for folder in folders:
            before = len(problems)
            check_stage2(folder)
            if len(problems) == before:
                fail(folder, 0, "fixture produced no failure")
    for p in problems:
        print(p)
    status = "FAIL" if problems else "ok"
    print(f"check: {status}: {len(folders)} fixtures, {len(problems)} problems")
    return 1 if problems else 0


def main():
    if "--fixtures" in sys.argv[1:]:
        return run_fixtures()
    bots = sorted(p for p in (ROOT / "bots").iterdir() if p.is_dir())
    teams = sorted(p for p in (ROOT / "teams").iterdir() if p.is_dir())
    all_bots = list(bots)
    for team in teams:
        all_bots += [f for f in check_team(team) if f not in all_bots]
    for folder in all_bots:
        check_bot(folder)
    catalog = (ROOT / "CATALOG.md").read_text(encoding="utf-8")
    for folder in all_bots + teams:
        rel = folder.relative_to(ROOT).as_posix()
        if f"]({rel}/)" not in catalog and f"]({rel})" not in catalog:
            fail(ROOT / "CATALOG.md", 0, f"no row links {rel}/")
    for page in sorted((ROOT / "community").glob("*.md")):
        if page.name != "README.md" and f"](community/{page.name})" not in catalog:
            fail(ROOT / "CATALOG.md", 0, f"no row links community/{page.name}")
    scanned = 0
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or ".git" in path.parts or path.name == "LICENSE":
            continue
        if path.suffix not in (".md", ".yml", ".yaml", ".sh", ".py", ".txt", ".json"):
            continue
        text = path.read_text(encoding="utf-8")
        scanned += 1
        check_text(path, text)
        if path.suffix == ".md":
            check_links(path, text)
    for p in problems:
        print(p)
    status = "FAIL" if problems else "ok"
    print(f"check: {status}: {len(all_bots)} bots, {len(teams)} teams, {scanned} files scanned, "
          f"{len(problems)} problems (private list: {len(PRIVATE) + len(PEOPLE) if _leak else 'not loaded, set LEAK_LIST'}, "
          f"{len(PATTERNS)} generic patterns)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
