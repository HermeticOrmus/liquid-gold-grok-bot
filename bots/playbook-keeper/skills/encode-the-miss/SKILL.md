---
name: encode-the-miss
description: Use when a bot repeats a mistake or someone asks for a postmortem. Finds the root cause from the transcript and drafts the one rule, skill step or check that stops it recurring.
---

# Encode the miss

## When to use it

A mistake happened twice, or once with a cost high enough that the person asks for a postmortem.

## Inputs and access

- The conversation or transcript where it happened, and the output it produced.
- The instructions, skill or check that should have caught it.
- Write access to the repo when the fix is a check (the GitHub plugin); otherwise nothing but this chat.

## Steps

1. Quote the moment it went wrong, with a link or the message.
2. Find the rule that should have held. If there is none, that is the root cause.
3. If there is one, find why it did not hold: too vague, buried, contradicted by another rule, or unenforceable in words.
4. Choose the home for the fix. Enforceable by a machine: a check. A method: a skill step. A boundary: one line in the bot's instructions.
5. Write the change as a diff or as the exact new line.
6. Write one sentence of what will not recur, in words a stranger can test.

## Validate

The change is one rule, not a rewrite. Replaying the same situation against the changed text would now go right, or fail loudly.

## Return

```
miss: <one line, with the link>
evidence: <the quote or the output>
change: <the new line, the skill step, or the PR>
will not recur: <one testable sentence>
```

## Needs approval

Applying any change to another bot's instructions or skills. Opening a PR in a repo you were asked to maintain is fine; merging it is not yours.
