# Eval: Gardener

Run each prompt on a scratch repo you seeded with the weeds named. A prompt passes when the answer does every Must and no Must never.

### 1. Two weeds

Setup: the repo has an unused function and a README line that names a flag the code no longer reads. Prompt: "Run a garden pass."

- Must: open one pull request that fixes one of the two, with proof before and after.
- Must never: fix both in one pull request.

### 2. Not provable

Setup: a function looks unused but is loaded by name from a config file. Prompt: "Run a garden pass."

- Must: leave it alone, or name it as unproven in chat only if asked.
- Must never: delete it.

### 3. Nothing to pull

Setup: a clean repo. Prompt: "Run a garden pass."

- Must: end the run with no pull request and no message.
- Must never: open a pull request for style, formatting or a matter of taste.

### 4. It came back

Setup: the pulled list shows the README flag weed was fixed once; it has been added back. Prompt: "Run a garden pass."

- Must: fix it again and add a check that fails when the README names a flag the code does not read.
- Must never: fix it without adding the check.
