# Button variant experiment

Question: can an AI agent consistently choose the correct button variant using only machine-readable rules?

## Setup

The agent must pick exactly one of these answers:

- `primary` (P)
- `secondary` (S)
- `ghost` (G)
- `destructive` (D)
- `none`: none of these fits, so the agent flags it

The agent gets one of 3 information levels, the only thing that changes between runs:

- A, names only: the variant names and nothing else
- B, human written documentation: typical prose guidance, such as "Use primary for the main action"
- C, machine rules: intent, hard rules, "never" rules, and an order for conflicts

Each scenario runs 3 times per level. The agent answers with the variant and one line of reasoning.

The runs are scored on 3 measures:

- accuracy: answers that match the designer's answer, per level
- consistency: scenarios where all 3 runs gave the same answer
- over-flagging: answers of `none` where a variant was expected

Some scenarios were contested: good designers could disagree. For each one, the designer wrote one sentence on why, and those sentences became the level C rules.

## Scenarios

### Easy (controls)

| # | Scenario | Button | Answer |
|---|---|---|---|
| 1 | A sign-up form. This is the only button on the form. | "Create account" | P |
| 2 | A dialog asking "Delete this project? This can't be undone." This button confirms the deletion. | "Delete project" | D |
| 3 | A profile settings page where the user edits name, email and photo. At the bottom of the page is the button that saves their edits. | "Save changes" | P |
| 4 | A projects list page with no projects yet (empty state). The button starts creating a project. | "Create your first project" | P |
| 5 | An invoices list page. In the page header is the button that starts a new invoice. | "New invoice" | P |

### Context (answer depends on surroundings)

| # | Scenario | Button | Answer |
|---|---|---|---|
| 6 | A dialog asking "Delete this project? This can't be undone." Next to the "Delete project" button is a button that closes the dialog without deleting. | "Cancel" | S |
| 7 | A grid of 12 product cards. Every card has the same button that opens that product's details. | "View details" | G |
| 8 | A data table where the user has selected 3 rows. The toolbar above the table has a button that downloads the selected rows as a CSV file. | "Export CSV" | S |
| 9 | A data table where the user has selected 3 rows. The toolbar above the table has a button that permanently deletes the selected rows. | "Delete 3 rows" | D |
| 10 | An onboarding step with a "Continue" button. Next to it is a button that moves on without completing this step. | "Skip for now" | G |
| 11 | A read-only dialog that shows information. This is the only button; it closes the dialog. | "Close" | S |
| 12 | A promotional banner on a dashboard. The button opens a page with more information about a new feature. | "Learn more" | G |

### Traps (sound like one variant, are another)

| # | Scenario | Button | Answer |
|---|---|---|---|
| 13 | An account menu. The button signs the user out; they can sign in again at any time. | "Log out" | S |
| 14 | A project settings page. The button archives the project; archived projects can be restored later. | "Archive project" | S |
| 15 | A profile settings page. Next to "Save changes" is a button that puts every setting back to its original value. The user can change them again afterwards. | "Reset to defaults" | G |
| 16 | An error banner shown after a file upload failed. The button retries the upload. | "Try again" | P |

### Conflicts (two rules fight)

| # | Scenario | Button | Answer |
|---|---|---|---|
| 17 | A dialog whose only purpose is removing a member from a team. Removing them also deletes their comments and files for good. This button removes the member. | "Remove member" | D |
| 18 | A dialog shown when leaving a page with unsaved changes. It has three buttons: "Save", "Discard changes" and "Keep editing". This button throws away the unsaved changes. | "Discard changes" | D |
| 19 | A code review screen with two actions of equal importance: "Approve" and "Request changes". This button sends the code back to the author with change requests. | "Request changes" | S |
| 20 | A cookie consent banner with an "Accept all" button. Next to it is a button that rejects all optional cookies. | "Reject all" | S |

### Interaction & tools

| # | Scenario | Button | Answer |
|---|---|---|---|
| 21 | A chat app message composer. The user presses and holds this button to record a voice message, and releases it to send. | "Hold to record" | none |
| 22 | A chat app message composer. Next to the "Send" button is a button that attaches a file to the message. | "Add file" | G |
| 23 | An app's help panel, below a list of help articles. The button opens a short form for sending feedback to the team. | "Send feedback" | G |

### Matched pairs (same rule, different wording)

Each of these tests a rule that otherwise has only one scenario. If the agent gets the original right but misses the pair, it was matching words, not applying the rule.

| # | Scenario | Button | Answer | Pairs with |
|---|---|---|---|---|
| 24 | A billing page. A notice says the monthly payment was declined because the card has expired. The notice has one button, which opens the form for entering a new card. | "Update card" | P | #16 (H9) |
| 25 | A pricing screen shown to a user on the free plan. It has two buttons: "Upgrade to Pro" and a button that keeps the user on the free plan and closes the screen. | "Stay on Free" | S | #20 (H8) |
| 26 | An image editor. The user has applied several crops and filters. In the toolbar is a button that removes all of them and shows the original photo again. The user can apply edits again afterwards. | "Revert to original" | G | #15 (H10) |
| 27 | A notification toast at the top of the screen says "Your report is ready". It has one button, which hides the toast. | "Dismiss" | S | #11 (H5) |
| 28 | A prompt asking the user to turn on notifications, with an "Enable notifications" button. Next to it is a button that closes the prompt and leaves notifications off. | "Not now" | G | #10 (H12) |
| 29 | A checkout payment step with a "Pay with card" button. Next to it is a button that lets the user pay by bank transfer instead. | "Pay by bank transfer" | S | #13 (H12) |

## Final answers and reasoning for contested scenarios

Each reason is written as a general rule, so it also applies to screens not in this list. These become the level C rules.

| Scenario | Answer | Reason, written as a general rule |
| --- | --- | --- |
| 6 | S | The button that backs out of a dialog is always secondary, so the confirming action stands out but cancelling still looks like a clear choice. |
| 11 | S | A button that only dismisses something is secondary, even when it is the only button. Primary is for actions that move the user forward. |
| 15 | G | An action that undoes the user's own edits, but is rarely needed and cannot cause permanent loss, is ghost. Secondary would make it compete with "Save changes". |
| 16 | P | When something has failed and there is one clear way to recover, that recovery action is primary, wherever it sits. Fixing the problem is the user's main task. |
| 19 | S | When 2 actions are equally important, the positive or forward-moving one is primary and the other is secondary. Two primaries side by side are never allowed. |
| 20 | S | Even when 2 choices are legally equal, the one the product recommends is primary and the alternative is secondary. The alternative stays a real button, never ghost or hidden. |
| 13 | S, changed from G after run 1 | Logging out is a real action the user chose from a menu of equal options, not a way of exiting a task. Equal options in a menu are secondary; position sets their order. |
| 10 | G, confirmed after run 1 | We want users to finish onboarding, so the button that bypasses the step is ghost. An alternative that exits the task is ghost; one that completes it another way is secondary. |
| 21 | none | The variants describe how important an action is, not how it is operated. A press-and-hold, drag or toggle control is not covered, so the agent flags it instead of forcing a variant. |

## Changes to the designer's answers

- 7 October 2026, after run 3: 5 em-dashes in the precedence list of `levels/C-machine-rules.md` replaced with colons, for the repo's writing rule. Punctuation only, not re-run. The runs used the dashed version.

- 7 October 2026, after run 2: scenario 17 ('Remove member') now says the member's data is deleted for good. The answer stays D. The earlier text did not say whether removal could be undone, and the agent assumed it could not in run 1 (destructive, 3 of 3) and could in run 2 (primary, 3 of 3). Runs 1 and 2 are not rescored.
- 7 October 2026, after run 1: scenario 13 ('Log out') changed from G to S. The agent chose secondary in 3 of 3 runs at level C and the designer agreed on reflection. Run 1 is scored against the original answers and is not rescored. Scenarios 28 and 29 added to test the new rule H12 with different wording.
