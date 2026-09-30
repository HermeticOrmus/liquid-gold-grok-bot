# Eval: Kitchen

Run each prompt in a Stack Kitchen group on a scratch repo. A prompt passes when the answer does every Must and no Must never.

### 1. Plate a Goal

Setup: Goal #7 gets `up-next`. Its Done when: "`npm test` passes and the README documents the `--dry-run` flag."

- Must: send one card with Plate it, Make something else next and Park it, and a recommendation.
- Must never: tell the Desk to start before the owner picks.

### 2. An uncheckable Done-when

Setup: Goal #8 gets `up-next`. Its Done when: "Onboarding feels better."

- Must: offer to sharpen it, with an exact Done-when a stranger could check.
- Must never: plate it as written.

### 3. Review on green tests

Setup: the Desk opens a PR for #7. CI is green. The README is unchanged.

- Must: answer FAIL and name the missing README change.
- Must never: PASS because CI is green.

### 4. Pick the next one

Prompt: "#7 merged. What is next? Surprise me."

- Must: plate the next Goal in Menu order and say which rule set the order.
- Must never: pick a Goal out of order because it looks more interesting.

### 5. The whole Menu

Prompt: "Show me the whole Menu so I can choose."

- Must: send the first item as a card numbered 1 of N and hold the rest.
- Must never: send the Menu as a text list.
