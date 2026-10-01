# Event Request Desk

| | |
|---|---|
| Author | Emma Weyrauch |
| Listing | https://x.ai/bot/marketplace/bots/event-request-desk |
| Add to Grok Bot | https://x.ai/bot/hp7QlVUPuYUp09kc6IFAA |
| Categories | From Grok Bot Team, Operations |
| Level | assayed from the page |

## What it does

From the listing: "Scores every event, sponsorship, and speaking ask, then drafts your yes or no. Works from a Slack channel or a paste, and never sends without you."

## Why it is gold

- One call per ask, from a short fixed list: it will "recommend yes, no, not now, or needs info". Four options and a recommendation, the decision card our [Chief of Staff](../bots/chief-of-staff/) brings back.
- A score you can argue with: "Each rubric criterion scores 0 to 3", and its rubric skill runs "when a call they made disagrees with your score."
- A clear job with its anti-jobs: "I don't produce the events you say yes to, own a budget, or act as a general chatbot."
- Drafts first, and a state only the human can close: "every reply is a draft", and "a request only reaches replied after the user confirms they sent it."
- The record is a file: "The queue is the record, chat is not."
- No invented facts: "I never invent a request, an organizer, a date, or a fee".
- A yes has a tail: "After a yes, track what the team owes the organizer until it is delivered."

## What we could see from outside

- The page data, read on 2026-10-01, lists 5 memories and 8 skills: Getting started, Log a new event request, Score an event request, Tune the decision rubric, Draft the reply, Track what you owe after a yes, Event spend and yes rate, Queue review.
- 9 integrations: slack, notion-workspace, linear, figma, hex, Gmail, Google Calendar, Google Drive, Google Sheets. The slack line reads "Read new event and sponsorship asks out of the channel where people already ask."
- 3 routines: "Weekday intake sweep", "Weekly queue review", "Weekly commitment check". Its first memory says "My routines stay off until you say yes, and they run in your timezone."
- The instructions field is empty in the page data. The standing rules are in its memories.

## Cracks seen from outside

- Nine integrations for a queue job, and three lines are the generic connector text: Gmail "Search, read, draft, and manage email.", Google Calendar "Search events and schedule meetings.", Google Sheets "Read and write Google Sheets." The least access the job needs is not stated for those three.
- The scope widens at the edge: "Non-event asks that need the same call go in the same queue under other." The page does not say where that stops.
- No routine summary states a quiet rule for a morning with no new asks.
- It saves a "spend cap" and a "period budget", but the page does not say what happens to a yes that would cross the cap.
