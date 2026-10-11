# Button variant scenarios for wheel 005

Draft, 11 October 2026. The designer has not decided the answers yet.

These are 24 new scenarios, from products wheel 004's 32 scenarios do not cover. Each one says whether the action can be undone, so the model does not have to assume.

The agent sees only the scenario text and the button label. It answers with exactly one of `primary` (P), `secondary` (S), `ghost` (G), `destructive` (D) or `none`, and one line naming the rule it applied.

The designer fills in the 'Designer's answer' column. Draft answers, read from the rules in order, are in `draft-answers.md`. Open it only after every answer here is filled in.

## Scenarios

| # | Scenario | Button | Tests | Designer's answer |
|---|---|---|---|---|
| 1 | A restaurant's booking page. The user has picked a date, a time and the number of guests. The button at the bottom confirms the booking. | "Book table" | HR1 | |
| 2 | A support desk ticket page. Below the reply box is "Send reply", which the page is for. In the page header is a button that makes the user the owner of the ticket. | "Assign to me" | HR1, P5 | |
| 3 | A password manager. A dialog asks "Delete this vault?" and says the 120 passwords in it will be removed and cannot be recovered. This button confirms. | "Delete vault" | HR2 | |
| 4 | A survey tool's settings page for one survey. A button removes all 340 answers people have sent in so far. The tool keeps no copy. | "Clear responses" | HR2 | |
| 5 | An email inbox where the user has selected 5 emails. The toolbar above the list has "Archive", "Mark as read" and this button, which moves the 5 emails to the bin. Emails stay in the bin for 30 days and can be restored. | "Delete" | HR3, P5 | |
| 6 | A newsletter settings page reached from a link in an email. Apart from the site's footer, the only button on the page stops the weekly newsletter. The user can sign up again at any time on the same page. | "Unsubscribe" | HR3 | |
| 7 | A contract-signing app. A dialog asks "Sign this contract?" with a "Sign" button. Next to it is a button that closes the dialog without signing. | "Go back" | HR4 | |
| 8 | A dialog asking "Cancel your subscription?" with a "Cancel subscription" button. Next to it is a button that closes the dialog and keeps the subscription as it is. | "Keep subscription" | HR4, HR8 | |
| 9 | A fitness app shows a sheet with this week's steps, workouts and sleep. Nothing on it can be changed. The sheet has one button, which closes it. | "Done" | HR5 | |
| 10 | A maps app shows a banner during a journey: "Traffic on your route is heavier than usual." The banner has one button, which hides it. | "Got it" | HR5 | |
| 11 | A list of 20 job adverts. Every advert has the same button, which saves that job to the user's shortlist. | "Save job" | HR6 | |
| 12 | A recipe app's search results show 30 recipe cards. Every card has the same button, which adds that recipe's ingredients to the shopping list. | "Add to shopping list" | HR6 | |
| 13 | A meeting invitation in a calendar app, with 2 buttons of equal importance: "Accept" and "Decline". This button accepts the invitation. | "Accept" | HR7 | |
| 14 | A manager's view of a holiday request in a staff app, with 2 buttons of equal importance: "Approve" and "Decline". This button turns the request down. The employee can send a new request. | "Decline" | HR7 | |
| 15 | A flight booking step that recommends travel insurance for €12, with an "Add insurance" button. Next to it is a button that goes on to payment without insurance. | "Continue without insurance" | HR8, HR12 | |
| 16 | A video call app. The connection dropped, and a full-screen message says "You were disconnected". The message has one button, which joins the call again. | "Rejoin" | HR9 | |
| 17 | A long tax return form. The user selected "Submit", and an error message at the top says one required number is missing. The message has one button, which scrolls to that field. | "Go to field" | HR9 | |
| 18 | A calendar app's event form. The user has changed the event's time and its room. Next to "Save" is a button that puts the event back as it was before editing. The user can make the same changes again. | "Undo changes" | HR10 | |
| 19 | A video player's settings panel with 3 options: playback speed, subtitles and quality. At the bottom is a button that sets all 3 back to their default values. Most people never use it. | "Restore defaults" | HR10 | |
| 20 | A job application form with "Submit application" at the bottom. Next to the cover letter box is a button that opens a page of tips on writing a cover letter. | "Read tips" | HR11 | |
| 21 | A slide editor. In the toolbar under the current slide is a button that opens a box for adding speaker notes to the slide. Most slides have none. | "Add notes" | HR11 | |
| 22 | A language-learning quiz with a "Check answer" button. Next to it is a button that moves on without answering. The question comes back at the end of the lesson. | "Skip question" | HR12 | |
| 23 | A smart home app. The user drags a dial round to set the heating temperature. | "Set temperature" | NR5 | |
| 24 | A taxi app's payment screen. The user slides a handle from left to right across a bar to confirm the payment. | "Slide to pay" | NR5 | |

## How the 24 cover the rules

- HR1 to HR12 are each tested by 2 scenarios, counting the 4 scenarios where 2 rules apply
- the 4 scenarios where 2 rules apply are 'Assign to me', 'Delete', 'Keep subscription' and 'Continue without insurance'
- 'Unsubscribe' tests HR3 and then the part of P4 on the only action in the main area
- 2 scenarios have the answer 'none', both controls that are not a plain click or tap
