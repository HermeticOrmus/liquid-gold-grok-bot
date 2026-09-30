# Routines: Desk

None. The Desk acts on the owner's Plate it and merge OK in the group, and on red CI for its own pull request.

| Field | Setting |
|-------|---------|
| Owning bot | Desk |
| Trigger | A Plate it or a merge OK from the owner in the group; a red CI message about its PR |
| Schedule and time zone | None |
| Input | The plated Goal issue and its Done when section |
| Result | A pull request that says Closes #N with proof; a merge after the OK |
| Approval boundary | Never merges without the owner's OK; never launches a paid agent without "Yes launch it" |
| Missing source | If the repo or the Goal cannot be read, say so in the group and stop |
