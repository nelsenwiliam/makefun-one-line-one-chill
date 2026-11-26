#!/usr/bin/env python3
"""One Line, One Chill - make.fun entry.

Writes a single line of horror to /output/entry.txt (program/v1 harness).
Pure stdlib only. The line was chosen after scoring 10 candidates against
the published judge brief (horror story in one sentence first, then
frightens, then vivid, then original, then crafted; gore for its own sake
does not count; a line may frighten by what it withholds):

  1. "The babysitter called to ask why the children were standing at the
     foot of her bed, and I told her the children were asleep beside me."
     (139) - fright 4, vivid 4, original 2, craft 3 = 13. Known
     creepypasta shape; the twist is telegraphed.
  2. "I taught my parrot to say goodnight, and tonight it whispered it
     back from inside the bedroom wall." (93) - fright 4, vivid 5,
     original 5, craft 4 = 18. Runner-up; the wall detail is fresh,
     but the scare leans on a talking bird doing a spooky thing.
  3. "Every night my daughter waves goodnight to the man in the corner,
     and tonight he waved back." (84) - fright 4, vivid 4, original 2,
     craft 4 = 14. "Man in the corner" is a well-worn image.
  4. "The voicemail from my dead mother ended with her saying she
     finally found where I hid the spare key." (101) - fright 5, vivid 5,
     original 4, craft 4 = 18. Runner-up; the spare-key twist is fresh,
     but a message from the dead is a familiar trope.
  5. "My smart speaker answered a question nobody asked, in my voice,
     from the empty bedroom." (83) - fright 4, vivid 4, original 4,
     craft 3 = 15. Modern and specific, but the last word ("bedroom")
     does not land a blow.
  6. "The ultrasound showed a second heartbeat, and the nurse whispered
     that it wasn't the baby's." (90) - fright 5, vivid 4, original 4,
     craft 4 = 17. Strong, but the nurse whispering is tropey and the
     threat stays vague rather than withheld with precision.
  7. "I stopped setting a place for my late husband at dinner, and this
     morning his chair was pulled out, facing me." (109) - fright 4,
     vivid 5, original 4, craft 4 = 17. Concrete and sad, but the scare
     is gentler than the top lines.
  8. "The new tenant asked why the previous one left, so I showed him
     the closet where she still folds his shirts." (108) - fright 4,
     vivid 5, original 4, craft 3 = 16. The pronoun logic wobbles on
     first read ("she" / "his").
  9. "My son's imaginary friend stopped visiting the day the police
     found the little shoes buried under the porch." (106) - fright 4,
     vivid 4, original 3, craft 3 = 14. "Imaginary friend" is a known
     trope and the shoes edge toward gore-adjacent shock.
 10. "The hospital bracelet on my wrist says my name, my blood type,
     and a date of death: yesterday." (94) - fright 5, vivid 5,
     original 5, craft 5 = 20  <-- WINNER

Why #10 wins: it is a horror story in one sentence with no setup and no
second chance. The scare is earned, not announced: a list of three
ordinary facts (name, blood type, date of death) that builds rhythm and
then detonates on the last word, "yesterday" -- you are already dead and
do not know it, and the dread outlasts the line because the reader is left
asking how, and what comes next. The image is concrete and specific (a
hospital bracelet on your own wrist), the framing is fresh (no mirror, no
doll, no basement, no gore), and it frightens by what it withholds exactly
as the brief allows. 94 characters, one sentence, well inside the 1-200
gate.
"""

import os

LINE = "The hospital bracelet on my wrist says my name, my blood type, and a date of death: yesterday."


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space. Fail loudly instead of submitting
    # an entry the gate would refuse.
    if not (1 <= len(LINE) <= 200):
        raise SystemExit("line is %d chars, outside the 1-200 gate" % len(LINE))
    if not LINE.strip():
        raise SystemExit("line is blank")
    if LINE.count(".") > 1 or "!" in LINE or "?" in LINE:
        raise SystemExit("line is not a single sentence")
    # MAKEFUN_OUTPUT_DIR is what the local grader simulation sets; the
    # sandbox harness mounts /output. Either way the file is entry.txt.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(output_dir):
        # Local run (no sandbox /output): write beside this script instead.
        output_dir = os.path.dirname(os.path.abspath(__file__))
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print("wrote %s (%d chars)" % (path, len(LINE)))


if __name__ == "__main__":
    main()
