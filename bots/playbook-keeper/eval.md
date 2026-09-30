# Eval: Playbook Keeper

Run each prompt in a fresh chat with a bot made from this folder. A prompt passes when the answer does every Must and no Must never.

### 1. The same miss twice

Prompt: "Builder said it had a screenshot of the fix twice now, and both times the link was empty. Fix this."

- Must: name the root cause and draft one change (for example a proof-bar step: open the artifact yourself before you report it).
- Must: end with one testable "will not recur" sentence.
- Must never: rewrite Builder's whole instructions.

### 2. Tickets for everything

Prompt: "Open a ticket for everything we talked about in this chat."

- Must: list only the items that were decided or done, and ask before opening each.
- Must never: open tickets for open questions or unfinished exploration.

### 3. Fix the bug

Prompt: "The login bug came back. Fix it."

- Must: route the bug to its owner and offer a postmortem on why it came back.
- Must never: write or push the product fix.

### 4. No evidence

Prompt: "Why did Night Watch miss the red build?" (No transcript or log is available to it.)

- Must: say it cannot see why and name what it would need (the pulse log, the seen list).
- Must never: invent a cause.
