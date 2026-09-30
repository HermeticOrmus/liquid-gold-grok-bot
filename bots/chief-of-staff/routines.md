# Routines: Chief of Staff

Works on request by default. The routine below is optional.

## Open loops check (optional)

| Field | Setting |
|-------|---------|
| Owning bot | Chief of Staff |
| Trigger | Schedule |
| Schedule and time zone | A cron you choose, in the captain's time zone, before they usually start work. |
| Input | The roster note, the decisions file, and what each owner reported since the last check. |
| Result | Only what changed: In flight, Needs you (one card), Ready with evidence. |
| Approval boundary | Never sends outside the workspace; never acts on an unanswered card. |
| Missing source | If an owner has not reported, say "no report from <owner>" rather than guessing their status. |

Silent when nothing changed. Use **Test run** before you enable it.

Cost: every run is a model run. Run it as rarely as still keeps you current; more runs add usage without adding news.
