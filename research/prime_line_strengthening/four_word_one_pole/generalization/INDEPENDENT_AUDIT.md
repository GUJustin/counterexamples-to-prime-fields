# Independent audit: generic four-parameter one-pole operation

**PASS.** The displayed rational formula, properness guards, and exhaustive
balanced/antibalanced support classification in GENERIC_ONE_POLE.md are correct
in characteristic different from two, subject to the stated domain and pole
guards. No main-source changes are needed.

## Formula and explicit rational example

For a=a_i, the quartic equation for a gives exactly

 A_i=X^3+(a^2-e1*a)X^2+(e3*a-e4)X-a^2*e4,
 k_i=e1+e3/a^2.

Direct coefficient comparison verifies N-DH_i=k_i A_i. Independently,
`independent_formula.py` expands all FOUR identities after multiplying by a_i^2
in the polynomial ring Q[a,b,c,d,X]; all residuals are identically zero.
This is a symbolic identity test, not evaluation at sampled parameter tuples.

The same script uses exact Fraction arithmetic at (1,2,5,13), obtaining
(e1,e2,e3,e4)=(21,121,231,130), pole130/11, and

    N(130/11)=-26535600/1331 !=0.

The twelve signed pair nodes are distinct and avoid the pole. The rational
function matches precisely the positive pair nodes2,5,13,10,26,65. The bounded
independent run and exact results are saved beside the proof.

Since a_i^2 are distinct, every a_i+a_j and hence every k_i is nonzero.
With e3!=0, D is genuinely linear. Its off-domain root cannot be a root of
A_i, so N cannot vanish there. Properness follows without an additional
hidden resultant guard. The claimed formula

    D(a_i*a_j)=-a_i*a_j*(a_k+a_l)*(a_i*a_j-a_k*a_l)

also follows by expanding e1,e3,e4; it checks the signs and confirms automatic
avoidance of the six selected nodes. Avoidance of the negative nodes remains
an explicit condition, as the note correctly states.

## Saturation and all sign supports

A proper one-pole function has at most three intersections with each old
quadratic. Six received-word agreements already account for twelve old-word
incidences, so each of the four vertex degrees is exactly three. Solving these
four degree equations makes opposite-edge multiplicities equal, and their
three values are either(1,1,1) or a permutation of(2,1,0).

The latter patterns have TWO distinct doubled edges. Writing
N=N_e(X^2)+X N_o(X^2) and denominator X-alpha, matching both signs implies
N_e(q)+alpha N_o(q)=0 at the associated squared node q. This polynomial has
degree at most one. Two distinct roots force it to vanish identically, giving
N=(X-alpha)N_o(X^2), contrary to properness. This argument uses only that the
characteristic is not two and the signed pair nodes are distinct.

Every remaining support has one sign on each of the six edges. Switching
vertices normalizes the three edges incident to the first vertex, leaving
exactly eight classes. I checked `determinant.py` against the six-point
homogeneous interpolation matrix: its exponent accumulation, row entries,
permutation parity, and all720-term expansion are correct. The saved six
nonzero factorizations consist only of a nonzero sign times2abcd and factors
a_i-a_j or a_i+a_j. Thus they are nonzero under the stated assumptions over
EVERY allowed characteristic, not only at the rational verification tuple.
The two zero classes are precisely all-plus and the class with all three
remaining signs negative. Their vertex-switch orbits are the eight balanced
and eight antibalanced supports. The explicit formula, switched and optionally
composed with X -> -X, realizes them whenever their pole guards hold.

## Scope

This is a generic positive algebraic first step, stronger than the isolated
cyclotomic witness. It still constructs only a fixed five-word bank after
pullback; no repeatable induction, nearest-list certificate, or superlinear
bad-label conclusion follows. A square pullback T^2 requires a nonzero pole;
this holds in the explicit rational example and on the relevant generic open
set. If applying the operation outside that open set, one can instead choose
a quadratic map whose critical value avoids the finite domain and pole.
