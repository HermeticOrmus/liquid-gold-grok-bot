# Grok Ship

| | |
|---|---|
| Author | Kun Chen ([kunchenguid](https://github.com/kunchenguid)) |
| Repository | https://github.com/kunchenguid/grok-ship |
| Read at | [`87825cca5c16c1c5da4f532676bccd5c3342918b`](https://github.com/kunchenguid/grok-ship/commit/87825cca5c16c1c5da4f532676bccd5c3342918b) on 2026-10-04 (committed 2026-09-05) |
| License | MIT. `LICENSE:1` says "MIT License". `LICENSE:3` says "Copyright (c) 2026 Kun Chen". `README.md:99` points at that file. |
| Level | watch |

Citations are `path:line` in that commit. Quotes are short. The jobs below are in our words.

## What it is

This commit marks the repository superseded. Its subject is "Mark grok-ship as superseded by the Firstmate/Grok Bot template (#5)". The README says "This repository has been superseded" by the Firstmate template at https://x.ai/bot/__4FfrkUdvpdMk6-LKg5r (`README.md:22-23`). The quick start on that same page still tells a bot to follow `GROK_SHIP.md` (`README.md:52`).

Under that warning, the files are a pack of charters and skills for a small software factory. The captain talks only to Firstmate. Firstmate files work as scout (a report) or ship (an authorized change), and a crewmate for that project drives a Cursor cloud agent. A fresh review reads the pushed branch before any pull request. The captain's word merges a factory ship.

## Seats

One repo gets one crewmate. Standing triage, when the captain asks for it, is added to that same crewmate. It is not a second bot (`GROK_BOT_FIRSTMATE.md:49`, `GROK_BOT_CREWMATE.md:23`).

| Seat | File | Job |
|------|------|-----|
| Firstmate | `GROK_BOT_FIRSTMATE.md` | The only bot the captain talks to. Files factory work, hands code to the repo's crewmate, and brings one decision at a time. |
| Project crewmate | `GROK_BOT_CREWMATE.md` | Owns one project. Scout ends as a report. Ship pushes a branch, waits for review, then opens the pull request. |
| Triage crewmate | `GROK_BOT_TRIAGE.md` | Optional. When asked, the repo's crewmate also wakes to comment, close stale pull requests, and sometimes merge a narrow class of other people's work. Reports go to Firstmate. |
| Inbox, documents, research | none in the pack | Other roles Firstmate may sign on. The pack gives them a plain role charter and no file of their own (`GROK_BOT_FIRSTMATE.md:5`, `GROK_BOT_FIRSTMATE.md:7`). |
| Starter | `GROK_SHIP.md` | The bot that installs the pack, then steps aside. Firstmate is who the captain keeps. |

## What each may send, publish, spend, or merge

No file at this commit names a payment, a budget, or what a run spends.

### Firstmate

- **Send.** Messages a crewmate and asks for the outcome back against a task id (`GROK_BOT_FIRSTMATE.md:11`, `GROK_BOT_FIRSTMATE.md:17`). May use "a priority send" to interrupt that crewmate (`GROK_BOT_FIRSTMATE.md:21`). Brings the captain one decision per message, with the options on a choice card and a recommendation (`GROK_BOT_FIRSTMATE.md:29`). "Do not paste or forward secrets in chat." (`GROK_BOT_FIRSTMATE.md:9`). The ahoy skill recaps what is already visible in the session: "Do not call GitHub, browsers, fleet snapshots, or file writes. Create no report." (`skills/ahoy/SKILL.md:36`).
- **Publish.** "Do not share/export/publish the lavish artifact for a live loop." (`GROK_BOT_FIRSTMATE.md:43`). The lavish skill Firstmate runs can still publish: its share command puts the artifact on ht-ml.app, public by default (`skills/lavish-session/SKILL.md:76`). The factory addendum says to use that share only when the user asks (`skills/lavish-session/SKILL.md:89`).
- **Spend.** "You never call a cursor cloud agent yourself." (`GROK_BOT_FIRSTMATE.md:13`). Lavish runs on the shared computer, and the captain confirms they can open the session (`skills/lavish-session/SKILL.md:87`). The skill prefers `npx -y lavish-axi@latest` (`skills/lavish-session/SKILL.md:86`). No line names a cost.
- **Merge.** After a factory pull request is green, Firstmate relays the captain's explicit word to the crewmate, which merges. It does not relay that word while checks are red (`GROK_BOT_FIRSTMATE.md:41`). The same line allows a wired triage crewmate to auto-merge corrective or opt-in work when CI is green, VISION is aligned with no cannot-tell, and the change is not default-behavior and not security, and it says that path is not a factory ship.

### Project crewmate

- **Send.** Reports outcomes and blockers to Firstmate against the task id, not to the captain (`GROK_BOT_CREWMATE.md:3`). An ask-user finding goes to Firstmate as a captain decision (`GROK_BOT_CREWMATE.md:15`). A red check goes back to the same cloud agent (`GROK_BOT_CREWMATE.md:17`).
- **Publish.** Scout: "Never open a pull request." (`GROK_BOT_CREWMATE.md:9`). Ship opens the pull request when review findings are empty, or only info, or an ask-user the captain already answered (`GROK_BOT_CREWMATE.md:15`). Error-severity findings do not raise a pull request (`GROK_BOT_CREWMATE.md:15`). The review subagent the crewmate starts "Do not open a pull request until this pass is clean." (`skills/adversarial-review/SKILL.md:8`) and does not open one just to make the branch visible (`skills/adversarial-review/SKILL.md:89`).
- **Spend.** Scout and ship each launch a Cursor cloud agent, "grok 4.6, high reasoning, not fast" (`GROK_BOT_CREWMATE.md:8`, `GROK_BOT_CREWMATE.md:11`). No line asks for a yes first, and no line names a cost.
- **Merge.** "Never merge on your own" (`GROK_BOT_CREWMATE.md:17`). It merges when Firstmate relays the captain's explicit word, never while checks are red, then marks the task row done. If this charter also holds standing triage, those wakes follow the triage rules (`GROK_BOT_CREWMATE.md:23`).

### Triage crewmate

Signed on only when the captain asks (`GROK_SHIP.md:13`, `GROK_BOT_FIRSTMATE.md:47`). Judgment lives in `TRIAGE.md`, which is not an installer (`TRIAGE.md:3`).

- **Send.** "Never message the captain directly." (`GROK_BOT_TRIAGE.md:4`). Every public comment starts with the disclosure line Firstmate recorded (`GROK_BOT_TRIAGE.md:59`). A stale close posts that comment through `gh pr close` (`GROK_BOT_TRIAGE.md:55`, `skills/14-day-stale-pr-close/SKILL.md:51`).
- **Publish.** "Do not open implementation PRs from triage." (`GROK_BOT_TRIAGE.md:57`, `TRIAGE.md:40`).
- **Spend.** Standing wakes do not launch a cloud agent for issue fixes (`GROK_BOT_TRIAGE.md:10`). Firstmate arms a 4-hour wake (`GROK_BOT_FIRSTMATE.md:49`). No line names what a wake spends.
- **Merge.** Auto-merge is allowed only when the class is corrective or opt-in, VISION has no "does not align" and no "cannot tell", CI is green, review is safe, and the change is not default-behavior, not security, not a captain hold, and not waiting on the author (`TRIAGE.md:34`, `GROK_BOT_TRIAGE.md:53`). A cannot-tell on any VISION rule blocks auto-merge (`skills/vision-md-triage-verdict/SKILL.md:24`, `GROK_BOT_TRIAGE.md:45`). Security is flagged to Firstmate and is not auto-merged (`TRIAGE.md:25`). Factory ships still need the captain's word (`TRIAGE.md:30`, `GROK_BOT_TRIAGE.md:10`). Closing a stale pull request "is not a merge" (`skills/14-day-stale-pr-close/SKILL.md:8`). A ready-for-pr ranking is not permission to merge (`skills/triage-eligible-fetch/SKILL.md:44`).

### Inbox, documents, research

`GROK_BOT_FIRSTMATE.md:7` says these crewmates "get a plain role charter instead." This commit has no charter file for them, so it does not say what they may send, publish, spend, or merge.

### Starter

`GROK_SHIP.md:6` calls that file an installer. After setup it tells the user to talk only to Firstmate, and "You cannot delete it yourself." (`GROK_SHIP.md:61`).

- **Send.** Messages Firstmate with a task id and tells it to greet the user (`GROK_SHIP.md:58`). Tells the user the starter is leftover (`GROK_SHIP.md:61`).
- **Publish.** No step publishes a page or opens a pull request.
- **Spend.** If lavish-axi is missing, it may run `npx -y lavish-axi@latest` (`GROK_SHIP.md:55`). No line names a cost. "Do not install extra plugins without a yes from the user." (`GROK_SHIP.md:51`). "Do not ask them to paste a token in chat." (`GROK_SHIP.md:57`).
- **Merge.** No step merges. The installer records the factory rule: factory ships never merge without the captain's word, and a wired triage crewmate may auto-merge only the narrow class above (`GROK_SHIP.md:13`).

## Also in this commit

`.github/workflows/superseded-auto-close.yml` is repository automation, not a Grok Bot seat. It has `issues: write` and `pull-requests: write` (`:9-11`). On an issue or pull request opened or reopened by someone other than the actions bot, the repository owner, or kunchenguid (`:16`), it comments and closes that issue or pull request (`:30-34`) and points at the template in the README warning.

## Why it is gold

Level: **watch**. The charters, skills, workflow, and license were read at `87825cca5c16c1c5da4f532676bccd5c3342918b` on 2026-10-04. The [rubric](../RUBRIC.md) puts a pick on watch when a fracture or a break is still open. This commit marks the repository superseded, and `README.md:52` still tells a bot to follow `GROK_SHIP.md`. That is a fracture: the quick start installs a pack the warning has replaced, and the workaround is the Firstmate template named at `README.md:23`. Gold would need a live eval recorded here. This pack has no eval file.

- Scout stays a report until the captain authorizes the change, and that yes flips the same task row to ship (`GROK_BOT_FIRSTMATE.md:39`, `skills/project-management/SKILL.md:75`).
- A fresh review reads the branch before any pull request. "Severity `error` must not merge." (`skills/adversarial-review/SKILL.md:44`). High risk "should not raise without explicit human approval" (`skills/adversarial-review/SKILL.md:58`).
- A factory merge waits for the captain's explicit word and green checks (`GROK_BOT_CREWMATE.md:17`, `README.md:44`). That is the same shape as [Ship Crew](../teams/ship-crew/) and [Stack Kitchen](../teams/stack-kitchen/): the person is the yes on the factory ship.
- Decisions arrive one at a time, with a recommendation, on a choice card (`GROK_BOT_FIRSTMATE.md:29`). That is the card rule in the rubric.
- Secrets stay on the bot that needs them (`GROK_BOT_FIRSTMATE.md:9`). The same line says the computer and browser logins are shared across the crew.

## Limits seen in the files

- Open fracture, grade from the [rubric](../RUBRIC.md): the commit and `README.md:22-23` mark the repository superseded, and `README.md:52` still installs it. The workaround is the Firstmate template. That open fracture is why the level is watch.
- A triage wake may merge, comment on, and close other people's pull requests under the bar above, without a fresh yes on that pull request (`TRIAGE.md:34`, `GROK_BOT_TRIAGE.md:55`).
- Launching a cloud agent has no ask-first line and no cost line (`GROK_BOT_CREWMATE.md:8`). The 4-hour triage wake has no cost line (`GROK_BOT_FIRSTMATE.md:49`).
- The lavish share command can publish a public page (`skills/lavish-session/SKILL.md:76`). The addendum limits that to a user ask (`skills/lavish-session/SKILL.md:89`).
