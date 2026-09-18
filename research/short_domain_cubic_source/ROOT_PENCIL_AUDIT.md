# Root audit of the source restrictions

September 17, 2026. These are restrictions on specified source mechanisms,
not general Reed--Solomon list bounds or new proximity-gap counterexamples.

## Split cubic polynomial first integral

Reviewed the complete 33- and 69-section proofs and the independent audit.
The original critical ideal, split seed factorization, and squarefree H
are essential hypotheses. For the 69 bound, the quadratic critical-root
valuation calculation is valid in both cases `2 deg b > deg A` and
`2 deg b <= deg A`. Working in one fixed valued algebraic closure makes
the at-most-two exceptional residues valid. The section-graph quotients
retain multiplicities, and different nonzero labels have disjoint
supports away from H. Verdict: PASS under the stated hypotheses.

## Quadratic rational first integrals

Opened the primary Pasten and Pasten--Wang theorem statements and checked
their hypotheses. The positive-characteristic result requires removing
constant factors, separability, and exclusion of nonconstant factors
whose coefficients are all p-th powers; these conditions cannot simply
be omitted.

Five degree-at-most-D polynomial sections reconstruct a degree-two
rational map: the cross-difference of two possible maps has degree at
most four and five distinct roots. Signed minors then give coefficient
degree bounds `(4D,5D,6D,4D,5D,6D)`, and discriminant height at most
`10D`. Local Gauss valuation additivity bounds every monic factor's
height, excluding the prohibited nonconstant p-th-power factors when
`p>10D`. Constant factors are harmless and removed separately.

Reciprocal normalization at a nonzero square specialization makes the
label polynomial monic without a function-field extension. Twenty other
labels satisfy the exact primary theorem. The resulting constant conic
has rational function field over the algebraically closed constants;
its equality with K(u) implies a degree-one Möbius parametrization.
Using the smooth projective curves handles degree-drop labels as well.

The polynomial members need not form an affine line. The reviewed
Möbius proof correctly uses the primitive local matrix instead: rank two
gives distinct values, and rank one gives one shared value with at most
one exceptional parameter. Pairwise polynomial root counting and total
agreement counting yield

    a <= D + D/(L-2) + n/L,  L>2.

Thus, for `p>max(2,10D)`, `D<n`, and surplus `a-D>=eta*n`, the combined
bound is

    L <= max(40, ceil(2+2/eta)-1).

The fallback forty counts at most twenty labels with two sections each.
Base-field sections may be considered over the algebraic closure without
changing their degrees or agreements. Verdict: PASS. The use of classical
square-value rigidity is explicitly attributed; no novelty claim for that
input is made.

The earlier statement that quadratic denominators require a higher-genus
splitting cover was an unnecessarily restrictive route and has been
corrected in the source notes. Degree at least three remains outside
this rational-map argument.
