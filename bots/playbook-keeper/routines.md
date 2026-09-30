# Routines: Playbook Keeper

None by default. It acts when a miss repeats or someone asks for a postmortem.

## Miss review (optional)

| Field | Setting |
|-------|---------|
| Owning bot | Playbook Keeper |
| Trigger | Schedule, or a message from any bot that says "miss:" |
| Schedule and time zone | A cron you choose, in the owner's time zone. |
| Input | Corrections the owner gave the bots since the last review, from the conversations it can read. |
| Result | For each correction that happened twice: the four-line draft. Nothing when there are none. |
| Approval boundary | Applies nothing without a yes. |
| Missing source | If it cannot read a bot's conversation, say which one and skip it. |

Cost: reading many conversations is a large model run. A message trigger ("miss:") costs less than a schedule.
