# Routines: Gardener

## Gardener run

| Field | Setting |
|-------|---------|
| Owning bot | Gardener |
| Trigger | Schedule |
| Schedule and time zone | A cron you choose, in the owner's time zone. Pick a quiet time, so the PR is waiting when people start. |
| Input | The repo's base branch, and the pulled and rejected lists. |
| Result | At most one pull request per run. Nothing when no weed is provable. |
| Approval boundary | Never merges; never bundles weeds. |
| Missing source | If the repo cannot be cloned or its checks cannot run, say so once and skip the run. |

Run it by hand twice before you schedule it, and read both PRs. Use **Test run** after any edit to the routine.

Cost: a run that reads a whole repo is a large model run even when it ends in silence. If most runs find nothing, run less often.
