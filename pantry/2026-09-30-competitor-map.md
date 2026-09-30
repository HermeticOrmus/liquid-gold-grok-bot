# Competitor map: liquid-gold-grok-bot

Read on 2026-09-30. Star counts come from the GitHub API in this run; entry counts come from each project's own README or page, as quoted. Anything not checked is `?`.

## Product

- Name: Liquid Gold for Grok Bot (`HermeticOrmus/liquid-gold-grok-bot`)
- Flagship: kintsugi-verified bots and teams, each with its instructions, skills, routines, plugins, eval and crack ledger in plain files.
- Our surfaces: `bots/` (7 bots), `teams/` (2 teams, 2 team-only seats), `community/` (10 credited picks), `scripts/create-bot.sh` and `scripts/create-team.sh` (gbot, dry run by default), `scripts/check.py` (CI), `RUBRIC.md`, `CATALOG.md`.
- Note: `main` holds only the README and LICENSE. The "Us" column describes the library as the pull request that adds this pantry ships it.

## Map

| Competitor | What it is | Overlap with us | Watch / differentiator | Source URL |
|------------|------------|-----------------|------------------------|------------|
| Grok Bot Marketplace | xAI's curated shelf of templates: 85 listings across 9 categories (counted from the category pages), a Featured row (Lauren Tan, Lenny Rachitsky, Claire Vo, Eric Zakariasson). | Where a published template is found and added. | No public submission path on the page. Listing pages show each template's memories, skills, integrations and routines; the instructions field is empty in the page data. | https://x.ai/bot/marketplace |
| Grok Bot guides and docs | 15 guides by the Grok Bot team (Templates, How I run multiple teams, Grok Bot for Engineering, and others) and the official docs. | The source of the patterns: teams, templates, routines, approvals. | The docs name what a skill must state and what to confirm for a routine, which our rubric uses. | https://x.ai/bot/guides, https://docs.x.ai/grok-bot/overview |
| cobusgreyling/grok-bot-templates | "Operating contracts for Grok Bot": README says "49 templates · 10 teams · 47 skills · 8 routines", a 100-point Bot Ready score, an npx CLI. 14 stars, MIT. | The closest: templates, teams, skills, routines, a score, CI. | CI fails a stable template under 80; a sanitizer template. `catalog/share-links.json` has an empty `links` object, so no Add links yet. | https://github.com/cobusgreyling/grok-bot-templates |
| kunchenguid/grok-ship | "Turn your Grok Bot into a software factory": scout vs ship, per-project crewmates, adversarial review before any PR, you merge. 178 stars, MIT. | Our Ship Crew and Stack Kitchen. | Superseded by a Firstmate template link per its README; a local sqlite backlog instead of issues. | https://github.com/kunchenguid/grok-ship |
| RongleCat/awesome-grok-bot | A bilingual resource list; its badge says 1866 entries; EN, 中文 and 日本語 READMEs. 353 stars. | Discovery of bots and templates. | A resource list, not verified entries. | https://github.com/RongleCat/awesome-grok-bot |
| majiayu000/awesome-grok-bot | README: "2872 live `x.ai/bot` shares for Grok Bot you can preview and Add", EN and 中文, a `catalog.json`. 55 stars. | Discovery of templates by job. | Live share links only ("not prompt dumps"). | https://github.com/majiayu000/awesome-grok-bot |
| templatesgrokbot.com | README badge: 7,106 templates, searchable by job title, with an MCP connection to the catalog. 32 stars, MIT. | Volume of templates by job. | Breadth over verification. | https://github.com/templatesgrokbot/templatesgrokbot.com |
| elie222/botdirectory.ai | A community directory of agent prompts as markdown files, with an optional `grok_share_url`; CI validates each file. 223 stars, MIT. | Prompts people paste; a PR-based contributor door. | Also serves other agent products; contributors can open a PR by mentioning its bot on X. | https://github.com/elie222/botdirectory.ai |
| divo12/awesome-grok-bot-templates | A curated list of live template share links (badge: 19), with an untrusted-template warning. 3 stars. | A small curated list of templates. | Links only; prompts kept separate and labeled as prompts. | https://github.com/divo12/awesome-grok-bot-templates |
| ZeroPointRepo/GrokBotDev | An agent-run directory of Grok Bot plugins, prompts and use cases with a JSON API, RSS and MCP; PRs are the write API and CI is the gate. 34 stars, MIT. | Community use cases and prompts. | Run by its own bots in the open. | https://github.com/ZeroPointRepo/GrokBotDev |

## Capabilities matrix

Y / N / P (partial) / ?. "MP" is the Grok Bot Marketplace.

| Capability | Us | MP | cobus | grok-ship | majiayu000 | divo12 | botdirectory | Source notes |
|------------|----|----|-------|-----------|------------|--------|--------------|--------------|
| One-click Add to Grok Bot link per entry | N | Y | N | P | Y | Y | P | Us: every `template.md` says pending publish. MP: each listing has an Add link. cobus: `catalog/share-links.json` `links` is empty. grok-ship: one template link in its README. majiayu000, divo12: READMEs list live share links. botdirectory: `grok_share_url` is optional. |
| Full instructions readable before install | Y | P | Y | Y | N | P | Y | Us: `instructions.md` per bot. MP: memories, skill names and routines shown; instructions field empty in page data. cobus: `PROFILE.md` per template. grok-ship: `GROK_SHIP.md`. majiayu000: links only. divo12: a separate `prompts/` folder. botdirectory: the prompt is the file body. |
| Refusal and approval rules stated per entry | Y | P | Y | Y | ? | ? | ? | Us: a `## Never` section in every `instructions.md`. MP: some listings state them in the description (Haggle Bot: "Never spends, signs, or sends without you"). cobus: `approval_never` in each `template.yaml`. grok-ship README: "factory ships never merge without your word". |
| Connectors named per entry, with why | Y | Y | Y | ? | ? | ? | P | Us: `plugins.md` per bot. MP: integrations listed on each listing page. cobus: `plugins` in each `template.yaml`. botdirectory: an `integrations` field. |
| Create a bot from files with a CLI | Y | N | Y | ? | ? | ? | ? | Us: `scripts/create-bot.sh` builds the gbot command. cobus: `npx ... init <id> --print`. |
| Teams with a written group law | Y | P | Y | Y | P | P | ? | Us: `teams/*/law.md`. MP: the Projects Manager listing staffs project channels. cobus: 10 teams. grok-ship: the factory and its crewmates. majiayu000: a "Team packs" section. divo12: its description names team operating systems. |
| Per-entry eval with Must and Must never | P | ? | P | ? | ? | ? | ? | Us: `eval.md` per bot, no live run recorded yet. cobus: `examples/first-run.md` per template and a static score. |
| Crack ledger with evidence per entry | Y | ? | P | ? | ? | ? | ? | Us: `LEDGER.md` per bot and team. cobus: a `patterns/` folder (for example `share-sanitizer-before-link`). |
| Leak or secret scan in CI | Y | ? | Y | ? | ? | ? | P | Us: `scripts/check.py`. cobus README: "share-safe by construction and scanned in CI". botdirectory README: "CI validates the file". |
| Quality level or score per entry | Y | P | Y | ? | ? | ? | ? | Us: levels in `RUBRIC.md`. MP: Featured and From Grok Bot Team rows. cobus: the Bot Ready score. |
| Credits outside creators by name | Y | Y | ? | ? | ? | ? | Y | Us: `community/`. MP: a creator on every listing. botdirectory: a `contributor` field. |
| Contributor door (forms or a PR path) | Y | N | Y | ? | Y | ? | Y | Us: issue forms and CONTRIBUTING.md. MP: no submission path on the page. cobus: CONTRIBUTING and good first issues. majiayu000: a PRs welcome badge and CONTRIBUTING.md. botdirectory: fork and PR, or an X mention. |
| Machine-readable catalog | N | ? | Y | ? | Y | ? | ? | cobus: `catalog.json` and an API. majiayu000: `catalog.json`. |
| Translations | N | ? | ? | ? | Y | ? | ? | majiayu000: EN and 中文. RongleCat (not a column): EN, 中文, 日本語. |
| Entries | 7 bots, 2 teams, 10 picks | 85 | 49 templates, 10 teams | 1 factory | 2872 shares | 19 | ? | Counts as each source states them. |
