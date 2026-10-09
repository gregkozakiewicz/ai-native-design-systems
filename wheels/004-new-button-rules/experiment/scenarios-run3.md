# Button variant scenarios for wheel 004, run 3

These are wheel 001's 29 scenarios, with 5 descriptions changed and 2 scenarios added, as the designer approved in wheel 003's `implications.md`. The check run does not use this file: it uses wheel 001's scenarios unchanged.

The agent sees only the scenario text and the button label. It answers with exactly one of `primary` (P), `secondary` (S), `ghost` (G), `destructive` (D) or `none`, and one line naming the rule it applied.

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
| 8 | A data table where the user has selected 3 rows. The toolbar above the table has a "Delete 3 rows" button. Next to it is a button that downloads the selected rows as a CSV file. | "Export CSV" | S |
| 9 | A data table where the user has selected 3 rows. The toolbar above the table has a button that permanently deletes the selected rows. | "Delete 3 rows" | D |
| 10 | An onboarding step with a "Continue" button. Next to it is a button that moves on without completing this step. | "Skip for now" | G |
| 11 | A read-only dialog that shows information. This is the only button; it closes the dialog. | "Close" | S |
| 12 | A promotional banner on a dashboard. The button opens a page with more information about a new feature. | "Learn more" | G |

### Traps (sound like one variant, are another)

| # | Scenario | Button | Answer |
|---|---|---|---|
| 13 | An account menu. The button signs the user out; they can sign in again at any time. | "Log out" | S |
| 14 | A project settings page with a form for the project's name and description, and a "Save changes" button below the form. Further down the page is a button that archives the project; archived projects can be restored later. | "Archive project" | S |
| 15 | A profile settings page with 4 settings. Next to "Save changes" is a button that puts all 4 back to their original values. Most people never use it, and the user can set them again afterwards. | "Reset to defaults" | G |
| 16 | An error banner shown after a file upload failed. The button retries the upload. | "Try again" | P |

### Conflicts (two rules fight)

| # | Scenario | Button | Answer |
|---|---|---|---|
| 17 | A dialog whose only purpose is removing a member from a team. Removing them also deletes their comments and files for good. This button removes the member. | "Remove member" | D |
| 18 | A dialog shown when leaving a page with unsaved changes to a written report. It has three buttons: "Save", "Discard changes" and "Keep editing". This button throws away the unsaved changes. | "Discard changes" | D |
| 19 | A code review screen with two actions of equal importance: "Approve" and "Request changes". This button sends the code back to the author with change requests. | "Request changes" | S |
| 20 | A cookie consent banner with an "Accept all" button. Next to it is a button that rejects all optional cookies. | "Reject all" | S |

### Interaction & tools

| # | Scenario | Button | Answer |
|---|---|---|---|
| 21 | A chat app message composer. The user presses and holds this button to record a voice message, and releases it to send. | "Hold to record" | none |
| 22 | A chat app message composer. Next to the "Send" button is a button that attaches a file to the message. | "Add file" | G |
| 23 | An app's help panel, below a list of help articles. The button opens a short form for sending feedback to the team. | "Send feedback" | G |

### Matched pairs (same rule, different wording)

| # | Scenario | Button | Answer | Pairs with |
|---|---|---|---|---|
| 24 | A billing page. A notice says the monthly payment was declined because the card has expired. The notice has one button, which opens the form for entering a new card. | "Update card" | P | #16 (HR9) |
| 25 | A pricing screen shown to a user on the free plan. It has two buttons: "Upgrade to Pro" and a button that keeps the user on the free plan and closes the screen. | "Stay on Free" | S | #20 (HR8) |
| 26 | An image editor. The user has applied several crops and filters. The top bar has a "Save" button. In the toolbar, next to the "Crop" and "Filters" buttons, is a button that removes all the edits and shows the original photo again. The user can apply edits again afterwards. | "Revert to original" | G | #15 (HR10) |
| 27 | A notification toast at the top of the screen says "Your report is ready". It has one button, which hides the toast. | "Dismiss" | S | #11 (HR5) |
| 28 | A prompt asking the user to turn on notifications, with an "Enable notifications" button. Next to it is a button that closes the prompt and leaves notifications off; the app will ask again next week. | "Not now" | G | #10 (HR12) |
| 29 | A checkout payment step with a "Pay with card" button. Next to it is a button that lets the user pay by bank transfer instead. | "Pay by bank transfer" | S | #13 (HR12) |

### New in wheel 004 (pairs that test the new rules)

Each tests one new rule against an existing scenario. 'Archive project' changes only its surroundings. 'No thanks' changes the consequence and the label.

| # | Scenario | Button | Answer | Pairs with |
|---|---|---|---|---|
| 30 | A project settings page whose settings are read-only, so the page has no "Save changes" button. Apart from the site's navigation, the only button on the page archives the project; archived projects can be restored later. | "Archive project" | P | #14 (P4) |
| 31 | A prompt asking the user to turn on notifications, with an "Enable notifications" button. Next to it is a button that turns notifications down and closes the prompt. The app will not ask again, but the user can turn notifications on in settings at any time. | "No thanks" | S | #28 (HR8, HR12) |
| 32 | An app's automation settings, where the user has set up 40 custom rules with switches and sliders. Next to "Save changes" is a button that puts every setting back to its factory value. The app keeps no copy of the old rules. | "Reset to defaults" | D | #15 (HR2, HR3) |

## Changes in run 3

The designer approved both on 9 October 2026, recorded in `implications.md`.

- 'Reset to defaults' now says the page has 4 settings and that most people never use the button. The answer stays G.
- New scenario 32: 'Reset to defaults' on an app's automation settings with 40 custom rules, answered D.

## Changes from wheel 001's scenarios

The designer approved each change on 8 October 2026. They are recorded in wheel 003's `implications.md`.

- 'Export CSV' now names the "Delete 3 rows" button beside it, so it is not the only action in the toolbar. The answer stays S.
- 'Archive project' now names the form and its "Save changes" button, so the page has a primary action. The answer stays S.
- 'Discard changes' now says the unsaved changes are to a written report, so the lost work is typed content. The answer stays D.
- 'Revert to original' now names the "Save" button in the top bar and the "Crop" and "Filters" buttons beside it. The answer stays G.
- 'Not now' now says the app will ask again next week, so the button postpones the decision. The answer stays G.
- New scenario 30: 'Archive project' as the only button in the main area of the page, answered P.
- New scenario 31: 'No thanks', which declines notifications and is not asked again, answered S. The user can still turn notifications on in settings, so the button is not destructive.
- The "Pairs with" column uses the new names HR and P.
