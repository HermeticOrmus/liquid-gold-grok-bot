# Plugins: Proof Judge

| Plugin | Why | Access it needs |
|--------|-----|-----------------|
| GitHub (first-party) | Read the diff, the PR body, the linked issue and the check runs. | Read. Proof Judge writes nothing to GitHub. |

No other connector is needed. If your previews live on a deploy host, the bot opens the preview link in its browser; no deploy connector is required.

## Ask first rules

Add these in **Settings, General, Auto-review** so the reviewer agent stops the bot before it acts:

- Ask first before posting a comment or review on GitHub.
- Ask first before pushing any commit.
- Ask first before merging a pull request.

Bots share one computer, so a GitHub sign-in made for another bot is visible to this one too. The rules above are the boundary, not the separate bot.
