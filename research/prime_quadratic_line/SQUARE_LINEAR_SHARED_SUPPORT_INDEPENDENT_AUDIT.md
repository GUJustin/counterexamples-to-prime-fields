# Independent audit: shared-support square-linear ceiling

September 19, 2026. PASS for the stated restricted architecture. This is
an upper bound on a constructor family, not a new counterexample or a
bound for arbitrary quadratic witnesses.

The root agent read the full proof independently and checked Theorem 3
on page 2 of Stevens--de Zeeuw, arXiv:1609.06284v4, directly from the
primary PDF. Its two population-range conditions and characteristic
condition are exactly those used in the note.

The updated square-root reduction works in an algebraic closure of the
coefficient field. Choosing one signed linear square root per nonzero
scalar-square polynomial is injective on distinct polynomials. Including
both roots in the point set preserves every agreement. Constants give
horizontal lines and cause no exception. The algebraic closure has
enough points to pad to 2n, while its characteristic is unchanged. For large n, taking 2n lines would
force an incidence lower bound of order n^(3/2), contradicting the
n^(22/15) upper bound. The actual smaller line family then lies either
below the (2n)^(7/8) cutoff or within the applicable incidence range.
Solving that bound gives exponent 7/8. The characteristic expression is
at most (2n)^11, safely below a constant times p^15 as n grows with
n<=p. In characteristic zero no characteristic condition is required.

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
fresh intercept and direction, characteristic zero or odd characteristic
p>=n (with arbitrary extension degree), and sqrt(n)-scale loss. The bound leaves smaller superlinear improvements possible and
says nothing about the complementary quadratic witnesses. There is no
new better.codes delta, first-order tightness example, or protocol
security consequence.

Audited source SHA256: `24ce7d740573696ca09be592c632620fbc2c982df1b8e12165335074021e6a8d`.
