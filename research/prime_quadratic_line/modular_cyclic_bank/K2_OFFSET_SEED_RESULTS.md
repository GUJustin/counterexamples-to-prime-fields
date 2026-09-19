# Two prescribed k=2 offset seeds: exact negative result

2026-09-19. This checks only the requested first instances r=2h±3.
It is not an asymptotic exclusion of either parameter family.

| p | n | h | r | m=2h+1 | target T | actual full-coefficient maximum | full maximizers | outside-bank maximum |
|---|---|---|---|---|---|---|---|---|
| 71 | 35 | 5 | 7 | 11 | 8 | 5 | 70 | 5 |
| 131 | 65 | 5 | 13 | 11 | 10 | 5 | 195 | 5 |

Both targets exceed sqrt(3n/2). Neither profile even reaches sqrt(n).
Both full-coefficient maximizer banks have zero separation from other
quadratics: respectively seven and thirteen quadratics with a zero
coefficient also have five agreements. Thus these two cases fail both
the rich-core target and the nonbank-gap requirement of the current
padding route. The full maximizer counts are two and three orbits of
size n; a larger count by itself does not offset their weak agreement.

The exact checker enumerates all p² normalized quadratics P(1)=1,
counts native agreements directly, and recovers each codewide histogram
by n H_A/A. The invariant full-coefficient subfamily uses the same
identity. Zero-agreement counts follow from p³ and (p−1)³ respectively.
Every orbit division is exact, and all three codewide interpolation
moments pass. The JSON receipt retains complete histograms and explicit
full-coefficient maximizers: (a,b,c)=(3,50,19) over F71 and (1,42,89)
over F131.

A separate three-point interpolation verifier is included in the script
and would run if either requested positive target were attained. Neither
was, so it was not run; no independent positive verification is claimed.
No broader prime or parameter sweep was performed. These finite failures
do not justify declaring the nontrivial-character-power route impossible,
but they supply no positive seed for scaling or paid computation.

Files: `check_k2_offset_seeds.py`, `k2_offset_seed_receipt.json`.
