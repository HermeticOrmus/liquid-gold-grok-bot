# Plugins: Night Watch

| Plugin | Why | Access it needs |
|--------|-----|-----------------|
| GitHub (first-party) | Read workflow runs and their logs on the watched repos. | Read only. |
| Vercel (optional) | Read deployments in an error state for the team you name. | Read only. |

Night Watch needs no write access anywhere. Its only outputs are messages in this workspace.

## Ask first rules

Add these in **Settings, General, Auto-review**:

- Ask first before rerunning or canceling a workflow.
- Ask first before any deploy, redeploy or rollback.
- Ask first before posting in Slack or any team channel.
