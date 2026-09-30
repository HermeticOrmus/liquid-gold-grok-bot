# Routines: Night Watch

## Pulse

| Field | Setting |
|-------|---------|
| Owning bot | Night Watch |
| Trigger | Schedule |
| Schedule and time zone | A cron you choose, in the owner's time zone. We run `*/15 * * * *`. |
| Input | Failed workflow runs on the watched repos (default branch and open PRs), and errored deploys if a deploy connector is on. |
| Result | One page per new failure class to the fixer. Nothing when nothing is new. |
| Approval boundary | Never reruns, restarts, redeploys, merges or posts in a team channel. |
| Missing source | If GitHub or the deploy host cannot be read, say so once to the human and keep the seen list as it is. Do not page from old data. |

Create it from the first conversation, after GitHub is connected, and only if no pulse exists yet. Use **Test run** once before you enable it: the first run should record the current reds and page nobody.

Cost: every pulse is a model run, even a silent one. Pick the slowest cadence that still catches a red before the people who would notice it. The owner can pause the routine from the bot's conversation details.

## Event trigger (optional)

If your account has GitHub event triggers, a narrow match (workflow run failed, watched repos only) can replace the schedule. Avoid broad listeners such as every notification.
