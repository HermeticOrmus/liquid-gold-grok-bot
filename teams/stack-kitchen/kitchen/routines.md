# Routines: Kitchen

## Goal and PR events

| Field | Setting |
|-------|---------|
| Owning bot | Kitchen |
| Trigger | Event: GitHub notifications for the kitchen's repo only: an issue labeled `up-next`; a pull request opened or updated whose body says Closes #N; a pull request merged. Event triggers come from Cursor account integrations and may need their own connection flow. |
| Schedule and time zone | None when events work. Without event triggers, a schedule you choose in the owner's time zone, reading the same three things. |
| Input | The Goal issue, the pull request, CI, the Menu order. |
| Result | A plate card, a PASS or FAIL review, a merge-OK card, or the next plate after a merge. Nothing when nothing changed. |
| Approval boundary | Never merges, never re-picks by taste, never posts outside the group. |
| Missing source | If GitHub cannot be read, say so once in the group and keep the last known Menu state. |

Keep the match narrow: one repo, those three events. A broad listener spends usage on nothing. Use **Test run** on a closed Goal first.

Cost: every run is a model run, whether it starts from an event or from the schedule fallback. The narrow match above keeps that spend on the Menu.
