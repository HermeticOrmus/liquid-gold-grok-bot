<p align="center">
  <img src="https://ormus.solutions/mascot/pixellab_liquid_to_swan.gif" alt="Liquid Gold for Grok Bot" width="128" style="image-rendering: pixelated;" />
</p>

<h1 align="center">Liquid Gold for Grok Bot</h1>

<p align="center">
  <em>The best Grok Bot templates and teams, each one kintsugi-verified: its cracks traced with evidence and sealed in plain sight</em>
</p>

<p align="center">
  <a href="https://github.com/HermeticOrmus/liquid-gold-grok-bot/stargazers"><img src="https://img.shields.io/github/stars/HermeticOrmus/liquid-gold-grok-bot?style=flat-square&color=aa8142" alt="Stars" /></a>
  <a href="https://github.com/HermeticOrmus/liquid-gold-grok-bot/blob/main/LICENSE"><img src="https://img.shields.io/github/license/HermeticOrmus/liquid-gold-grok-bot?style=flat-square&color=aa8142" alt="License" /></a>
  <a href="https://github.com/HermeticOrmus/liquid-gold-grok-bot/commits"><img src="https://img.shields.io/github/last-commit/HermeticOrmus/liquid-gold-grok-bot?style=flat-square&color=aa8142" alt="Last Commit" /></a>
  <img src="https://img.shields.io/badge/Kintsugi-aa8142?style=flat-square" alt="Kintsugi" />
  <img src="https://img.shields.io/badge/Grok_Bot-aa8142?style=flat-square&logo=x&logoColor=white" alt="Grok Bot" />
</p>

---

> A living library of Grok Bot templates and teams: instructions, skills, routines, plugins and an eval for every bot, with the cracks found and sealed in its ledger.

## Why kintsugi

Kintsugi mends a broken bowl with gold, and the repair becomes the part people look at. The cracks are where the gold goes.

Every bot here was taken apart the same way. We traced the places bots like it break: a vague job, a missing refusal, a decision buried in a wall of text, a secret left in a shared template, a routine that spends usage to say nothing, a claim nobody can check. We wrote each crack down with its evidence, and sealed it in the text you install. The seals are not hidden. Each bot's `LEDGER.md` shows what was broken and the line that now holds, for example:

| ID | Crack | Seal |
|----|-------|------|
| [Night Watch K-02](bots/night-watch/LEDGER.md) | One broken job pages once per run, the same failure again and again. | Failures group into classes; a new run of an open class stays silent. |
| [Proof Judge K-02](bots/proof-judge/LEDGER.md) | Green unit tests earn a PASS on a change that is wrong on the real surface. | PASS needs an artifact from the real surface. Green tests alone are not proof. |
| [Stack Kitchen K-01](teams/stack-kitchen/LEDGER.md) | A seat sitting in two project rooms carries notes between projects. | One kitchen, one project. A second repo gets its own seats. |

The library's own tools went through it too: the [library ledger](LEDGER.md) records the gbot CLI crack we hit while building this, and why the private leak list never lives in this repo, not even as hashes.

## Install a bot

A Grok Bot template packages a bot's instructions, relevant memories and skills (never personal or private ones), first-party plugins and routines. It leaves out secrets, custom code and scripts, and non-standard plugins such as MCP servers. So each folder here holds everything a template would, in files you can read first. Three ways in:

1. **The template link.** When a bot's `template.md` holds an `https://x.ai/bot/...` link, open it and choose **Add to Grok Bot**, then review the details before **Add Bot**. Every template here is pending publish.
2. **With gbot.** Install the community CLI ([grok-bot-cli](https://github.com/ScriptedAlchemy/grok-bot-cli)) and build the bot from its folder. The script prints the command and creates nothing until you add `--yes`:

   ```bash
   npm install --global grok-bot-cli
   scripts/create-bot.sh bots/proof-judge          # dry run: prints the gbot command
   scripts/create-bot.sh bots/proof-judge --yes    # creates the bot
   scripts/create-team.sh teams/stack-kitchen      # dry run for a group
   ```

   Use gbot 0.11.2 or later. Version 0.2.3 sends a create request when you type `gbot bots create --help` ([K-01](LEDGER.md)).
3. **Paste it.** Create a bot, open **Edit Profile**, set the name and title from the top of its `README.md`, and paste its `instructions.md` into the Instructions field. Then add the skills, routines and plugins its folder lists.

Each folder: `README.md` (the card), `instructions.md`, `skills/`, `routines.md`, `plugins.md`, `eval.md`, `LEDGER.md`, `template.md`. The skill files use the Agent Skills format, since xAI does not document a skill file format for templates ([K-08](LEDGER.md)).

This library is independent and not affiliated with xAI or Cursor.

## The catalog

| Entry | Level | Job |
|-------|-------|-----|
| [Chief of Staff](bots/chief-of-staff/) | assayed | Routes each ask to one owner; decisions as cards, one at a time |
| [Builder](bots/builder/) | assayed | Ships the slice with proof; never merges |
| [Proof Judge](bots/proof-judge/) | assayed | PASS or FAIL against the Done-when, with paths |
| [Night Watch](bots/night-watch/) | assayed | Pages each new red class once; silent when green |
| [Gardener](bots/gardener/) | assayed | One provable weed per run, one small PR |
| [Playbook Keeper](bots/playbook-keeper/) | assayed | Turns a repeated miss into a rule |
| [Pantry Researcher](bots/pantry-researcher/) | assayed | Stocks cited research and checkable Goal atoms |
| [Stack Kitchen](teams/stack-kitchen/) (team) | assayed | Desk and Kitchen ship one repo through Goal issues |
| [Ship Crew](teams/ship-crew/) (team) | assayed | Five of the bots above in one group for one repo |

Plus ten credited [community picks](community/) from the [Grok Bot Marketplace](https://x.ai/bot/marketplace), by Lingxi Li, Lauren Tan, Ulysses Ng, Robin Delta, Daniel Gartshein, Jon Grigull and Lenny Rachitsky. Every entry, with install links: [CATALOG.md](CATALOG.md).

## How a bot earns gold

Every entry goes through five stages: ready the vessel (a clear job, scope and refusal rules), trace the cracks (card-shaped decisions, secrets and connectors, routine cadence and cost), keep the ledger, seal with gold (every crack sealed in the installed text, an eval with Must and Must never lines), and hallmark (the leak check passes, the eval runs on a live bot, the template is published). A bot is **gold** only when its live eval run is in its ledger. Everything here is **assayed**: every stage done on paper, and no live eval run recorded yet. The full rubric: [RUBRIC.md](RUBRIC.md).

## Feedback

Tried a bot? [Tell us what worked and what did not](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues/new?template=feedback.yml).

## Contribute

Pick a crack. Seal it with gold.

- [Report a crack](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues/new?template=crack.yml) in any bot, team or script, with the evidence.
- [Nominate a bot or template](https://github.com/HermeticOrmus/liquid-gold-grok-bot/issues/new?template=nominate.yml) that deserves a place here.
- Take an item from the [Menu](pantry/MENU.md) or a [good first issue](https://github.com/HermeticOrmus/liquid-gold-grok-bot/contribute), or share your own template as a folder.
- Questions and show and tell: [Discussions](https://github.com/HermeticOrmus/liquid-gold-grok-bot/discussions).

See [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT © 2026 [Diego Bodart](https://github.com/HermeticOrmus). See [LICENSE](LICENSE). Community picks belong to their creators and are linked, never copied.

<p align="center"><img src="https://brand.ormus.solutions/assets/marks/kintsugi-mark.svg" alt="Kintsugi mark" width="48" /></p>
