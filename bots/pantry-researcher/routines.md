# Routines: Pantry Researcher

Works on request by default. A restock is a large run; start it by hand.

## Restock (optional)

| Field | Setting |
|-------|---------|
| Owning bot | Pantry Researcher |
| Trigger | Schedule, or a message "restock" |
| Schedule and time zone | A cron you choose, in the owner's time zone. |
| Input | The product repo, the previous stock, public sources. |
| Result | One pull request with four dated files, or `none` when nothing changed. |
| Approval boundary | Never posts or contacts anyone; never merges. |
| Missing source | Log it in the search log and keep going; never fill a cell from memory. |

Cost: a restock reads many pages and is one of the larger runs a bot makes. Restock when the queue runs low, not on a clock.
