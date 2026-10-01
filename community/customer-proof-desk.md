# Customer Proof Desk

| | |
|---|---|
| Author | Anoop Baliga |
| Listing | https://x.ai/bot/marketplace/bots/customer-stories |
| Add to Grok Bot | https://x.ai/bot/AamPlGjd2lIdDv6seEMXR |
| Categories | Sales |
| Level | assayed from the page |

## What it does

From the listing: "Turns call notes and transcripts into case studies, testimonials, and proof points. Quotes stay word for word from what you paste, and nothing publishes without your yes."

## Why it is gold

- A rule for what may change inside a quote: "The only changes allowed inside quote marks are an ellipsis marking a cut and square brackets around a word added for context. Anything else is a paraphrase and goes outside the quote marks."
- A refusal that holds: each quote carries an approval state, from "not requested" to "refused", and "Refused means never publish, in every future pull." Consent is kept per quote, not per conversation.
- The record is a file, not the chat: "The proof bank is the record, chat is not." Each row carries "the exact wording, the speaker with their title and company, the source and its date, the claim it supports, and its approval state."
- A clear job with its anti-jobs: "I'm not a copywriter, a CRM, or a research tool."
- Drafts first, with the customer's sign-off named: "Nothing gets published or sent until you say yes, and I flag what still needs the customer's sign-off."
- A check before anything ships: its "Check a draft against the bank" skill runs when the user "wants every quote, number, and customer claim verified before it goes out."
- Routines ship off: "My Monday roundup and monthly freshness check stay off until you turn them on, and they run in your timezone."

## What we could see from outside

- The page data, read on 2026-10-01, lists 5 memories and 11 skills: Getting started, Add sources to the proof bank, Mine a batch of calls, Write a case study, Pull proof for a claim, Testimonials and pull quotes, Build a deal proof one-pager, Get the customer's approval, Check a draft against the bank, Lay out the case study, Run the case study pipeline.
- 7 integrations: notion-workspace, slack, linear, figma, hex, Gmail, Granola. The hex line reads "Check a customer's numbers against your own data before you publish them."
- 2 routines: "Weekly proof roundup" and "Monthly proof refresh".
- The instructions field is empty in the page data. The standing rules are in its memories.

## Cracks seen from outside

- The slack line says it will "drop the Monday roundup there", in a shared channel. The roundup names "which customers are ready for a case study" and "which approvals are still sitting". The page does not say it leaves out customers whose approval is not requested or refused. *Inferred*: a customer's name can reach a team channel before the customer has agreed to anything.
- Neither routine summary states a quiet rule for a run with nothing new.
- Gmail's line is the generic "Search, read, draft, and manage email." The job needs read and draft. The word "manage" is wider, and the page does not say what the bot does with it.
- "Get the customer's approval" is the one skill that writes to someone outside the team. The send rule above covers it; check the first approval request it drafts before you say yes.
