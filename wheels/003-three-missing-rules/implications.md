# Implications for the system

## No change to the system

`system/button-variant.md` keeps the 12 rules from wheel 001 as they are. The 3 sentences tested here do not enter the system. Together they raised the misses from 32 to 40 across the 10 models.

## Two decisions for the designer before any further run

Both are judgements about the product, not about wording. The runs show where the rules and the designer's answers part. Only the designer can say which side is right.

### The difference between 'Discard changes' and 'Reset to defaults' needs a rule

'Discard changes', 'Reset to defaults' and 'Revert to original' all lose something the user can get back only by redoing it by hand. The designer calls the first destructive and the other 2 ghost. In this run, 6 of 10 models called 'Revert to original' destructive, and 2 of 10 called 'Reset to defaults' destructive.

The designer can choose one of these answers:

- losing work the user typed or made is destructive, and losing settings or adjustments that are quick to redo is not
- "discarding unsaved changes" goes into the list of destructive examples in H2, and "undone" stays undefined

### The scope of H8 decides 'Stay on Free'

H8 is worded for choices the law or ethics require, such as rejecting cookies. In this run, 4 of 10 models did not apply it to declining an upgrade.

The designer can choose one of these answers:

- widen H8 to "an alternative the product must keep easy to choose, such as declining an upgrade or rejecting optional cookies"
- keep H8 narrow and accept ghost for 'Stay on Free', since it bypasses the upgrade

## What carries forward

- sentence 1, on where "optional" ends, closed 22 of 22 misses on its targets and goes into the next run unchanged
- 'New invoice' needs watching in that run, since GPT-6 Astra moved it to secondary in 2 of 3 repeats
- the order inside step 3, where a bypass beats a plain dismiss, closed 'Not now' and carries forward
- the part about H8 depends on the decision on 'Stay on Free'
- every rule change runs against all 29 scenarios before it is proposed, because all 3 sentences moved scenarios they were not aimed at

## A hierarchy rule for the next run

The designer read wheel 002's wrong answers on 'Archive project' on a project settings page. 13 of them called it optional and chose ghost. The scenario does not say what else is on the page, so the models had nothing to rank the button against. The designer proposed this rule for the next run:

> When an action is the only one in the main area of a view, and no role rule applies, it is primary. Navigation, menus and footers are not the main area.

Before the next run uses it, 3 scenarios need to say what else is in their view:

- 'Archive project' on a project settings page names no other action, so this rule would make it primary
- 'Export CSV' above a data table names no other action in the toolbar
- 'Revert to original' in an image editor toolbar names no other action, and H10 sits in no step of the precedence order

On 8 October 2026 the designer approved these changes to the next run's copy of the scenarios:

- 'Archive project' on a project settings page gets 'Save changes' in its description, and stays secondary
- a new scenario has 'Archive project' alone in the main area of the page, answered primary
- 'Export CSV' above a data table gets 'Delete 3 rows' next to it, as in the delete scenario, and stays secondary

Wheel 001's scenario file stays as it is, because wheels 001 to 003 were scored against it.

## Examples in the rules that match test buttons

Several rules give examples in brackets that are the labels of test buttons, such as "skip, not now, maybe later" in H12. A model can match a label to an example instead of reading the situation. The reworded pairs do not fully check this, because some reworded labels, such as 'Not now', are examples too.

On 8 October 2026 the designer decided to take these examples out of the next run's rules:

- H3: "log out, archive, reset, unsubscribe"
- H4: "cancel, close, go back"
- H11: "attach a file, give feedback, learn more"
- H12: "skip, not now, maybe later"
- the never rules: "cancel, close, dismiss or skip", and "hold, drag, toggle, slider"
- this wheel's amended step 5: "archive, export, log out"

Where a never rule names labels, it will name the role instead, such as a button that backs out, dismisses or skips.

## Names in the next run's rules

On 8 October 2026 the designer decided these names, starting with wheel 004. Wheels 001 to 003 keep the names their models read.

- the hard rules H1 to H12 become HR1 to HR12
- the never rules are numbered NR1 to NR5, in the order they appear
- the precedence steps are P1: Reversibility, P2: Interaction, P3: Role in the view, P4: Recommendation, and P5: Emphasis
- the section keeps the name 'Precedence'

## What this does not justify

- a claim that written rules stopped working, since Sonnet scored 87 of 87 and the 10 models agree more than before
- a claim that the largest models are worse at rules, since they followed the new text more strictly than the others
- any change to the designer's answers; the 2 decisions above are the designer's, and the next run tests whatever is decided
