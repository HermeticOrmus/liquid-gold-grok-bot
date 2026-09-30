# Plugins: Builder

| Plugin | Why | Access it needs |
|--------|-----|-----------------|
| GitHub (first-party) | Clone, push a branch, open a pull request, read CI. | Write to branches; merge stays behind Ask first. |
| Cursor cloud agents (if your plan has them) | For work bigger than the bot's own computer. The Builder writes the prompt and the proof bar; the cloud agent writes the code. | Launch agents. Paid runs stay behind a yes. |

## Ask first rules

Add these in **Settings, General, Auto-review**:

- Ask first before merging a pull request.
- Ask first before pushing to the default branch.
- Ask first before any deploy command.
- Ask first before launching a cloud agent.

Start with read and draft access. Widen it after the Builder has shipped a few changes you checked.
