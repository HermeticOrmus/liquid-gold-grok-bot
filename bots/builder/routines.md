# Routines: Builder

None. The Builder works when someone hands it a task. A routine here would start work nobody asked for.

If you want red CI fixed without asking, pair it with [Night Watch](../night-watch/), which pages the Builder once per new failure class. The page is the trigger, not a schedule.

| Field | Setting |
|-------|---------|
| Owning bot | Builder |
| Trigger | A message from you, a Chief of Staff, or Night Watch |
| Schedule and time zone | None |
| Input | The outcome, the repo, the proof expected |
| Result | A pull request with proof, and one line in chat |
| Approval boundary | Never merges, deploys or spends |
| Missing source | If the repo or the surface cannot be reached, say so and stop |
