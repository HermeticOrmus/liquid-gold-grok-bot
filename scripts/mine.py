#!/usr/bin/env python3
"""Mine the Grok Bot Marketplace for templates this library has not carded yet.

Usage: python3 scripts/mine.py [--out pantry/YYYY-MM-DD-listing-mine.md]

Reads https://x.ai/bot/marketplace, then every listing page it links, and
takes what each page publishes about its template: name, creator, categories,
description, and the names of its skills, routines, integrations and
memories. Listings that already have a card in community/ are marked carded;
listings missing from the newest earlier listing mine are marked new.

The habits column only names what anyone can see from outside, the same
habits RUBRIC.md looks for: an approval or refusal rule in the description or
a skill ("asks first"), routines, skills, integrations. It is a lead for a
card, never a grade: we cannot read a listing's instructions, so nothing
mined here is marked gold.

No account, no token, no writes to the marketplace. One page at a time, with
a pause between requests.
"""
import argparse
import datetime as dt
import json
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://x.ai/bot/marketplace"
SLUG = re.compile(r"/bot/marketplace/bots/([a-z0-9-]+)")
ASKS_FIRST = re.compile(r"approv|your (exact )?yes|without (you|your)|never (send|spend|sign|post|create|change)|ask(s)? (you )?first|draft", re.I)
log: list[str] = []


def fetch(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (liquid-gold-grok-bot mine)"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def page_text(html: str) -> str:
    chunks = re.findall(r'self\.__next_f\.push\(\[1,"(.*?)"\]\)', html, re.S)
    return "".join(json.loads(f'"{c}"') for c in chunks)


def template(slug: str) -> dict | None:
    text = page_text(fetch(f"{BASE}/bots/{slug}"))
    i = text.find('"template":{')
    if i < 0:
        return None
    obj, _ = json.JSONDecoder().raw_decode(text, i + len('"template":'))
    return obj


def carded() -> dict[str, str]:
    cards = {}
    for card in (ROOT / "community").glob("*.md"):
        if (m := SLUG.search(card.read_text(encoding="utf-8"))):
            cards[m.group(1)] = card.stem
    return cards


def previous_slugs(out: Path) -> tuple[set[str], str]:
    earlier = sorted(p for p in (ROOT / "pantry").glob("*-listing-mine.md") if p.name < out.name)
    if not earlier:
        return set(), ""
    return set(SLUG.findall(earlier[-1].read_text(encoding="utf-8"))), earlier[-1].name


def names(items: list) -> list[str]:
    return [i.get("name", "") for i in items or [] if i.get("name")]


def cell(s: str) -> str:
    return (s or "").replace("|", "/").replace("\n", " ").strip()


def main() -> int:
    ap = argparse.ArgumentParser()
    today = dt.date.today().isoformat()
    ap.add_argument("--out", default=f"pantry/{today}-listing-mine.md")
    args = ap.parse_args()
    out = ROOT / args.out

    try:
        index = fetch(BASE)
    except urllib.error.URLError as e:
        print(f"mine: marketplace not reachable ({e})", file=sys.stderr)
        return 1
    slugs = sorted(set(SLUG.findall(index)))
    log.append(f"{BASE}: {len(slugs)} listings linked")
    cards = carded()
    seen, prev = previous_slugs(out)

    rows = []
    for slug in slugs:
        try:
            t = template(slug)
        except (urllib.error.URLError, ValueError) as e:
            log.append(f"{slug}: not read ({e})")
            continue
        finally:
            time.sleep(0.5)
        if not t:
            log.append(f"{slug}: no template data on the page")
            continue
        skills, routines = names(t.get("skills")), names(t.get("routines"))
        integrations = names(t.get("integrations"))
        text = " ".join([t.get("description", "")] + [s.get("description", "") for s in t.get("skills") or []])
        habits = [h for h, on in (("asks first", bool(ASKS_FIRST.search(text))), (f"routines {len(routines)}", routines),
                                  (f"skills {len(skills)}", skills), (f"integrations {len(integrations)}", integrations)) if on]
        state = f"carded ([{cards[slug]}](../community/{cards[slug]}.md))" if slug in cards else (
            "new" if prev and slug not in seen else "not carded")
        rows.append((slug in cards, -len(habits), -len(skills), slug, t, habits, state))
    rows.sort()

    new = sum(1 for r in rows if r[6] == "new")
    lines = ["# Listing mine: liquid-gold-grok-bot", "",
             f"Read on {today} by `scripts/mine.py` from the [Grok Bot Marketplace]({BASE}). Every row is quoted from "
             "the listing's own page data. Habits are what anyone can see from outside; a row is a lead for a card, "
             "not a grade.", "",
             f"{len(rows)} listings read, {len(cards)} carded, "
             + (f"{new} new since [{prev}]({prev})." if prev else "no earlier listing mine to compare."), "",
             "## Listings", "",
             "| # | Listing | Creator | Categories | Habits | State | Description |",
             "|---|---------|---------|------------|--------|-------|-------------|"]
    for n, (_, _, _, slug, t, habits, state) in enumerate(rows, 1):
        creator = cell(t.get("creatorName", "")) + (f" (@{t['handle']})" if t.get("handle") else "")
        lines.append(f"| {n} | [{cell(t.get('name', slug))}]({BASE}/bots/{slug}) | {creator} | "
                     f"{', '.join(t.get('categories') or [])} | {', '.join(habits) or '-'} | {state} | "
                     f"{cell(t.get('description', ''))[:160]} |")
    lines += ["", "## Search log", ""] + [f"- {line}" for line in log]
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"mine: {len(rows)} listings, {new} new, wrote {out.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
