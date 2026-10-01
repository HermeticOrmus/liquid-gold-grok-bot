# Catalog

Every entry in the library: its level, its job, and how to install it. Levels are defined in [RUBRIC.md](RUBRIC.md). Every template link here is still pending publish, so the install column gives the other two ways.

## Bots

| Bot | Level | Job | Install |
|-----|-------|-----|---------|
| [Chief of Staff](bots/chief-of-staff/) | assayed | Routes each ask to one owner and brings decisions back as cards, one at a time. | [template](bots/chief-of-staff/template.md) pending; `scripts/create-bot.sh bots/chief-of-staff`; or paste [instructions](bots/chief-of-staff/instructions.md) |
| [Builder](bots/builder/) | assayed | Ships the slice on a branch with proof from the real surface. Never merges. | [template](bots/builder/template.md) pending; `scripts/create-bot.sh bots/builder`; or paste [instructions](bots/builder/instructions.md) |
| [Proof Judge](bots/proof-judge/) | assayed | Reviews a PR as a new context: PASS or FAIL against its Done-when, with paths. | [template](bots/proof-judge/template.md) pending; `scripts/create-bot.sh bots/proof-judge`; or paste [instructions](bots/proof-judge/instructions.md) |
| [Night Watch](bots/night-watch/) | assayed | Pages the fixer once per new CI or deploy red class. Silent when green. | [template](bots/night-watch/template.md) pending; `scripts/create-bot.sh bots/night-watch`; or paste [instructions](bots/night-watch/instructions.md) |
| [Gardener](bots/gardener/) | assayed | Pulls one provable weed per run and opens one small PR with the proof. | [template](bots/gardener/template.md) pending; `scripts/create-bot.sh bots/gardener`; or paste [instructions](bots/gardener/instructions.md) |
| [Playbook Keeper](bots/playbook-keeper/) | assayed | Turns a repeated miss into one rule, skill step or check. | [template](bots/playbook-keeper/template.md) pending; `scripts/create-bot.sh bots/playbook-keeper`; or paste [instructions](bots/playbook-keeper/instructions.md) |
| [Pantry Researcher](bots/pantry-researcher/) | assayed | Stocks cited research and Goal atoms with checkable Done-whens. Contacts nobody. | [template](bots/pantry-researcher/template.md) pending; `scripts/create-bot.sh bots/pantry-researcher`; or paste [instructions](bots/pantry-researcher/instructions.md) |

## Teams

| Team | Level | Job | Install |
|------|-------|-----|---------|
| [Stack Kitchen](teams/stack-kitchen/) | assayed | Ships one repo through Goal issues: plate, build, review, merge on your OK. | Create the two seats, then `scripts/create-team.sh teams/stack-kitchen` |
| [Ship Crew](teams/ship-crew/) | assayed | Five bots from this library in one group for one repo. | Create the five bots, then `scripts/create-team.sh teams/ship-crew` |

Team seats that live only inside a team:

| Seat | Level | Job | Install |
|------|-------|-----|---------|
| [Desk](teams/stack-kitchen/desk/) | assayed | Stack Kitchen: ships plated Goals, merges after your OK. | `scripts/create-bot.sh teams/stack-kitchen/desk` |
| [Kitchen](teams/stack-kitchen/kitchen/) | assayed | Stack Kitchen: plates, reviews against the Done-when, weeds. | `scripts/create-bot.sh teams/stack-kitchen/kitchen` |

## Community picks

Credited, never copied. See [community/README.md](community/README.md) for what "assayed from the page" means.

| Pick | Author | Level | Job | Install |
|------|--------|-------|-----|---------|
| [Lingxi's Engineer Bot](community/engineer-bot.md) | Lingxi Li | assayed from the page | Supervises cloud agents on your repo and asks you only to merge. | [Add to Grok Bot](https://x.ai/bot/SxqbG1NT5qEw7ggmHqQu_) |
| [Nightly Audit Engineer](community/nightly-audit-engineer.md) | Lingxi Li | assayed from the page | Audits the whole codebase and ships one cleanup PR per area. | [Add to Grok Bot](https://x.ai/bot/0LLQmzk-yzwHi0zuiV0lC) |
| [Engineering Lead](community/engineering-lead.md) | Lauren Tan | assayed from the page | Owns the agent loop and pings only when blocked, ready or done. | [Add to Grok Bot](https://x.ai/bot/Ks3X7JpD-6I86s3zkJFRh) |
| [QA bot](community/qa-bot.md) | Ulysses Ng | assayed from the page | Runs the acceptance checklist on the live deploy: pass or fail. | [Add to Grok Bot](https://x.ai/bot/lKQWoQAvYgg_7Bkg2R-m7) |
| [PM bot](community/pm-bot.md) | Ulysses Ng | assayed from the page | Writes the cut, in and out and how you know it is done, before engineering starts. | [Add to Grok Bot](https://x.ai/bot/FeeqMRMJr2jwixCROZcIh) |
| [Alfred](community/alfred.md) | Robin Delta | assayed from the page | Designs and audits your bot organization; creates nothing without your exact yes. | [Add to Grok Bot](https://x.ai/bot/p7Gh6HIrfv4AGzIow6-9X) |
| [dr eggbot](community/dr-eggbot.md) | Lauren Tan | assayed from the page | Designs focused bots: one job, one voice, explicit anti-jobs. | [Add to Grok Bot](https://x.ai/bot/_jOdbfkB16zxu7MRcmReE) |
| [Haggle Bot](community/haggle-bot.md) | Daniel Gartshein | assayed from the page | Finds evidence-backed SaaS savings and drafts counters. Never spends, signs or sends. | [Add to Grok Bot](https://x.ai/bot/pwQ612YrX3R0eACnIMlom) |
| [GTM Loop Closer](community/gtm-loop-closer.md) | Jon Grigull | assayed from the page | Finds promises left open across your tools and drafts what closes each one, with evidence. | [Add to Grok Bot](https://x.ai/bot/gj3IlHOOpzecm6xpmPJOt) |
| [Overheard](community/overheard.md) | Lenny Rachitsky | assayed from the page | Digests third-party mentions of your name and brand; quiet when nothing clears the bar, never posts. | [Add to Grok Bot](https://x.ai/bot/NIEguoGUjA648fUPle8F5) |
| [Deal Inspector](community/deal-inspector.md) | Jon Grigull | assayed from the page | Audits each deal that moved stage against your framework, from timestamped call quotes, and stages CRM updates for your yes. | [Add to Grok Bot](https://x.ai/bot/vZfC76-4UC1XU7qC4m726) |
| [Customer Proof Desk](community/customer-proof-desk.md) | Anoop Baliga | assayed from the page | Turns call notes into case studies and proof points, each quote traced to its source, with consent kept per quote. | [Add to Grok Bot](https://x.ai/bot/AamPlGjd2lIdDv6seEMXR) |
| [Performance Marketer](community/performance-marketer.md) | Josh Kim | assayed from the page | Builds paused Google Ads tests from approved copy and turns traffic on only on your yes for that campaign. | [Add to Grok Bot](https://x.ai/bot/JeNCKNe0ItsLMWYrLiRcb) |
| [Event Request Desk](community/event-request-desk.md) | Emma Weyrauch | assayed from the page | Scores every event, sponsorship and speaking ask against your rubric and drafts the reply for you to send. | [Add to Grok Bot](https://x.ai/bot/hp7QlVUPuYUp09kc6IFAA) |
| [Recruiting Coordinator](community/recruiting-coordinator.md) | Tommy Hansen | assayed from the page | Schedules interview loops and drafts candidate mail. Never sends, books, posts or rejects without your yes. | [Add to Grok Bot](https://x.ai/bot/KDahOjiDbbAvxqx9KaGcq) |
| [Stalk Bot](community/stalk-bot.md) | Shub Gaur | assayed from the page | Watches named competitors across mail, site, pricing, changelog, jobs and X. Never posts, never contacts their people. | [Add to Grok Bot](https://x.ai/bot/Y7iWVNiPdorgu6oFY-PRG) |
