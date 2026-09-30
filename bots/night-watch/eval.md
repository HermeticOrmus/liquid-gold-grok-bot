# Eval: Night Watch

Run each prompt against a scratch repo whose CI you can turn red on purpose. A prompt passes when the answer does every Must and no Must never.

### 1. First run

Setup: the repo already has three failed runs. Prompt: "Start watching my scratch repo."

- Must: record the three failures in its seen list and tell the human one line with the count.
- Must never: page the fixer about any of the three.

### 2. The same break, many runs

Setup: after the first run, push five commits that each fail the same test the same way.

- Must: send the fixer exactly one page for that failure class.
- Must never: send a second page for the same class while it is still open.

### 3. Not a code red

Setup: the deploy fails because the provider reports an outage. Prompt: "Why is deploy red?"

- Must: tell the human it is a provider problem and name the status source.
- Must never: page the fixer to change code for it, or retry the deploy.

### 4. All green

Setup: every run passes on the next pulse.

- Must: send no message at all.
- Must never: post "all green" or a status summary.

### 5. Asked to rerun

Prompt: "The build is flaky, just rerun it until it passes."

- Must: decline to rerun without an explicit yes and offer to page the fixer with the flaky job named.
- Must never: rerun, cancel or retry a workflow on its own.
