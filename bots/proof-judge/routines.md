# Routines: Proof Judge

Proof Judge works on request by default. Hand it a pull request in chat and it judges it. Add the routine below only after a few manual reviews look right.

## PR review on open (optional)

| Field | Setting |
|-------|---------|
| Owning bot | Proof Judge |
| Trigger | Event: a GitHub notification that a pull request opened or got a new commit in the repo you name. Event triggers come from Cursor account integrations and may need their own connection flow. Keep the match narrow: one repo, pull requests only. |
| Schedule and time zone | None (event-driven). If your account has no event trigger, skip the routine and ask in chat. |
| Input | The pull request from the notification and its Done-when. |
| Result | One verdict message in this chat, in the shape of [skills/proof-review](skills/proof-review/SKILL.md). |
| Approval boundary | Never posts on GitHub. Never merges. |
| Missing source | If the PR or its Done-when cannot be opened, say which one and stop. Never judge from memory. |

Use **Test run** on a closed pull request first. A test run does real work.

Cost: every event is a model run. A broad match (every notification) spends usage on nothing; the docs warn against broad listeners.
