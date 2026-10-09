# Implications for the system

This file is not finished. The designer has made one decision so far, recorded below. The proposed rules for `system/`, the choice between run 1's and run 2's rules, and the notes for the wheel 001 and 002 posts are still to be written.

## A reset is destructive when much would be lost

In run 2, GPT-6 Astra called 'Reset to defaults' on a profile settings page secondary in 2 of 3 tries. It would not assume that the reset is "rarely needed", which HR10 requires.

Looking at that miss, the designer found a second problem in HR10. It says the action "cannot cause permanent loss", but not loss of what. A reset does not lose the settings themselves: every switch and slider is still there. It does lose the user's configuration, the values they chose. With a few settings, the user can set them again in a moment. With many switches and sliders, they may not remember what they had, so the loss is permanent in practice. HR2 and HR3 have the same gap.

On 9 October 2026 the designer decided that the answer depends on how much would be lost:

- resetting a few choices the user can easily make again is not destructive, and HR10 can make it ghost
- resetting a large custom configuration that the user would have to rebuild from memory is destructive, under HR2

For the next run, this means:

- HR3 and HR10 say how much may be lost, such as "a few choices the user can easily make again", instead of "cannot cause permanent loss"
- the 'Reset to defaults' scenario says how many settings the page has
- a new scenario resets a large custom configuration, answered destructive

The wording of HR3, HR10 and both scenarios is not yet approved.
