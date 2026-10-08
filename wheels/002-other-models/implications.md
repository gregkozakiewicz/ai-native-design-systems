# Implications for the system

## Proposed changes

- `system/button-variant.md` keeps its 12 rules unchanged
- 9 models from 4 companies scored 80 to 87 of 87 with them at default reasoning settings
- the rule set therefore belongs to the system, not to a prompt tuned to one model
- the system records which models it has been tested on, with the score for each
- a note such as 'tested on 9 models, 7 October 2026' lets a reader judge the rule set
- a reader with a tenth model then knows to run it
- the system states its scope note as "one component, 9 models" instead of "one model"

- a rule set is checked for gaps by running it on several models and listing the scenarios where they split
- in this wheel, the 6 splits with rules were exactly the 3 open readings
- the method found them without looking at the designer's answers

## Rules to test before they enter the system

Three readings are open, each named in the models' own reasons. Each is a candidate for wheel 003. There it is written, run on the same 9 models, and accepted only if every model then agrees.

1. Where "optional" ends. Precedence step 5 says "secondary if a real choice the user may take, ghost if optional and rarely needed". Six models read archive, log out and export as optional; the Claude models read them as real choices. Candidate: a reversible action the user came to the view to do, or may reasonably do there, is secondary. Ghost is for actions most users never take on that view. Misses it would close: 22 of the 32 across 9 models.
2. What "undone" means. Rule H3 says "can be undone or reversed later". Haiku read redoing work by hand as undoing. Candidate: an action is reversible only if the system can restore the previous state; redoing the work by hand does not count. Misses: 3 of 32.
3. Which rule wins inside a precedence step. 'Not now' is both a dismiss (H5, secondary) and a bypass (H12, ghost). 'Stay on Free' is both an equal alternative (H8, secondary) and a bypass (H12, ghost). Candidate: within step 3, the most specific description of the button's role wins, and H12 is more specific than H5. H8 sits in step 4, so it already loses to H12. Either the designer's answers then change, or H8 moves to step 3 above H12. The designer decides which; the run decides whether models follow it. Misses: 7 of 32.

## What this does not justify

- any claim about effort settings other than each model's default, apart from one Fable 5.1 run at low effort that scored 87 of 87
- any claim about Google's newest model, Gemini 4, which the account cannot reach
- a claim that the rules are complete; 3 readings are open and 32 of 783 answers with rules missed because of them
- a claim about which models behave better when the system is silent, since 5 refuse and 4 guess and the system has not chosen
- a change to the designer's answers, since every miss was a defensible reading of a missing rule
