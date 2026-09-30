# Plugins: Chief of Staff

The core job needs no connector: it routes inside Grok Bot. Connect the tools below only if you want it to read where asks arrive.

| Plugin | Why | Access it needs |
|--------|-----|-----------------|
| Slack (optional) | Read asks in the channels you name and route them. | Read; posting stays behind Ask first. |
| Gmail and Google Calendar (optional) | Read asks and conflicts; draft replies. | Read and draft. Sending stays behind Ask first. |
| GitHub (optional) | See which issues and PRs are open when routing engineering work. | Read. |

## Ask first rules

Add these in **Settings, General, Auto-review**:

- Ask first before sending any external email.
- Ask first before posting in Slack.
- Ask first before any purchase or plan change.

The app shows editable email and Slack drafts with Send and Discard. Those drafts are how outbound work should reach the captain.
