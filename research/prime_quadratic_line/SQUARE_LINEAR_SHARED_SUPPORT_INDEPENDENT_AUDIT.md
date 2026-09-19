# Independent audit: shared-support square-linear ceiling

September 19, 2026. PASS for the stated restricted architecture. This is
an upper bound on a constructor family, not a new counterexample or a
bound for arbitrary quadratic witnesses.

The root agent read the full proof independently and checked Theorem 3
on page 2 of Stevens--de Zeeuw, arXiv:1609.06284v4, directly from the
primary PDF. Its two population-range conditions and characteristic
condition are exactly those used in the note.

The square-root reduction is injective on distinct nonzero polynomials
within each square class after choosing one signed root. Including both
roots in the point set preserves every polynomial agreement. Constants
are horizontal lines and cause no exception. Padding to 2n points is
possible since n<=p and p is odd. For large n, taking 2n lines would
force an incidence lower bound of order n^(3/2), contradicting the
n^(22/15) upper bound. The actual smaller line family then lies either
below the (2n)^(7/8) cutoff or within the applicable incidence range.
Solving that bound gives exponent 7/8. The characteristic expression is
at most (2n)^11, safely below a constant times p^15 as n grows.

Subtracting the common quadratic and shifting the line parameter
preserves ordinary common agreement. At any nonzero shifted parameter,
the core matches and fresh matches separately admit simultaneous
polynomial explanations, hence each is at most A. A T=A+d witness
therefore needs at least d matches on each side. This proves membership
in the entire rich core list, including witnesses absent from the named
bank. Each core witness has at most |E| total fresh incidences over all
labels, giving the stated n^(7/8)*n/sqrt(n)=n^(11/8) count. Multiple
witnesses for a label only overcount; no singleton hypothesis is used.

The bounded-n fallback is valid: three matching coordinates determine
an affine quadratic trajectory. If every matching coordinate were
persistent, that trajectory would explain at least T coordinates
jointly, contradicting T>CA. One additional coordinate therefore fixes
the parameter. This avoids claiming a field-independent list bound
from only one or two agreements.

Scope retained: a fixed translated scalar-square cone, proportional
fresh intercept and direction, prime ambient field, and sqrt(n)-scale
loss. The bound leaves smaller superlinear improvements possible and
says nothing about the complementary quadratic witnesses. There is no
new better.codes delta, first-order tightness example, or protocol
security consequence.

Audited source SHA256: `17ecb8c3fc9351dbcb78f18343ff235d805299ccb5dda1f9a6e32a47029920de`.
