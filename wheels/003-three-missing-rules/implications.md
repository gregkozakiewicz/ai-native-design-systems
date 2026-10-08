# Implications for the system

## No change to the system

`system/button-variant.md` keeps the 12 rules from wheel 001 as they are. The 3 sentences tested here do not enter the system. Together they raised the misses from 32 to 40 across the 10 models.

## Two decisions for the designer before any further run

Both are judgements about the product, not about wording. The runs show where the rules and the designer's answers part; only the designer can say which side is right.

1. What makes 'Discard changes' destructive but 'Reset to defaults' and 'Revert to original' ghost? All 3 lose state that comes back only if the user redoes it by hand. The models that read the edges most sharply split them by how much work is lost: 6 of 10 now call 'Revert to original' destructive, and 2 of 10 call 'Reset to defaults' destructive. Candidate answers:
   - losing work the user typed or made is destructive; losing settings or adjustments that are quick to redo is not
   - name the case and nothing more: "discarding unsaved changes" goes into H2's list of destructive examples, and "undone" stays undefined
2. Does H8 cover 'Stay on Free'? H8 is worded for choices the law or ethics require, such as rejecting cookies. 4 of 10 models do not apply it to declining an upgrade. Candidate answers:
   - widen H8 to "an alternative the product must keep easy to choose, such as declining an upgrade or rejecting optional cookies"
   - keep H8 narrow and accept ghost for 'Stay on Free', since it bypasses the upgrade

## What carries forward

- sentence 1, on where "optional" ends, closed 22 of 22 misses on its targets; it goes into the next run unchanged, with a watch on 'New invoice', which GPT-6 Astra moved to secondary in 2 of 3 repeats
- the order inside step 3 (a bypass beats a plain dismiss) closed 'Not now' and carries forward; the part about H8 depends on decision 2
- every rule change runs against all 29 scenarios before it is proposed, never only against the scenarios it targets; all 3 sentences moved scenarios they were not aimed at

## What this does not justify

- a claim that written rules stopped working; Sonnet scored 87 of 87 with the new text, and all 10 models agree on more scenarios than before
- a claim that the flagships are worse at rules; they followed the new text more strictly, which is what a rule set wants once its text is right
- any change to the designer's answers; the 2 decisions above are the designer's, and the next run tests whatever is decided
