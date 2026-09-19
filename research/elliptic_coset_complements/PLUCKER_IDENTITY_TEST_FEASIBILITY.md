# Bounded feasibility ledger: common-pencil Plücker falsification

Status: CANCELLED for this family. No large matrix was allocated and no Plücker experiment was run. The later `TORSION_QUINTIC_SUNFLOWER_BOUND.md` proves at most2n useful labels for arbitrary label assignments under the far-word hypothesis. The initial fixed-H full-rank target was also structurally impossible: the canonical three-dimensional bivector kernel below is always present. Resource numbers are retained only as a design record.

## Exact linear test

Fix ell23, p1657 and one subgroup H in the existing fixture. The syndrome length is r=4ell−1=91. For an admissible parameter point P form the monic support polynomial

`U_P=(N_H-a_P B_H)(N_H-b_P B_H) J_P`,

where a_P=x(phi_H(3P)), b_P=x(phi_H(7P)), and J_P uses multipliers1,2,4,5,6. Its degree is51. The recurrence matrix R(P) has rows0 through39, columns0 through90, with row i equal to the coefficient vector of X^i U_P. It has rank40 by its distinct monic pivots.

A two-dimensional syndrome space spanned by S0,S1 intersects ker R(P) nontrivially exactly when the40×2 matrix [R(P)S0,R(P)S1] has rank at most one. Equivalently the nonzero decomposable bivector w=S0 wedge S1 is killed by all780 pairs of rows of R(P).

For columns a<b and recurrence rows i<j, the corresponding coefficient is

`u_(a-i)u_(b-j)-u_(b-i)u_(a-j)`,

with u outside0..51 defined as zero. There are choose(91,2)=4095 unknown bivector coordinates. Each sample supplies exactly780 linearly independent equations, because the exterior square of a rank40 row map has rank780. The equation count alone requires at least six samples to reach the corrected rank4092 ceiling: five supply only3900 equations.

Full column rank cannot occur for this fixed-H family: its kernel necessarily contains the three-dimensional space described below. The meaningful hypothetical target would have been rank4092 with kernel exactly that canonical space, not rank4095. A larger linear kernel alone would not prove a new decomposable nonzero bivector or a far-source pencil.

## Generic sample scope

For an identity asserted as a rational function of the elliptic parameter, samples may be any points where all rational formulas are defined; they need not be ell-torsion. Reject poles, infinite multiplication images, coincident paired tags, repeated quintic roots, and overlap between the quintic and paired fibers. These checks make the sampled formula agree literally with the intended monic support polynomial.

A canonical-only kernel conclusion obtained from generic points concerns rational-identity candidates, not every pencil that works only on a finite torsion subset. The same kernel conclusion from actual torsion samples would cover all pencils meeting those sampled support spaces. These scopes would need to be distinguished; no such rank result was computed.

## Structure and resources

The Toeplitz structure makes row generation inexpensive relative to elimination: each wedge uses at most two products of shifted52-coefficient vectors, and common simultaneous shifts can be reused. Independently of this Toeplitz structure, the canonical argument below caps the accumulated rank at4092.

As a useful sample diagnostic, the row spaces for two samples consist of degree-at-most90 polynomials divisible by their degree51 support polynomials. If their gcd has degree g, their intersection dimension is max(0,g−11). Choosing samples with low gcd avoids this obvious recurrence-row redundancy, but it neither proves independence of all wedge constraints nor predicts full rank.

A dense six-sample matrix has4680×4095 entries. At eight bytes per entry, typical FLINT nmod storage uses153,316,800 bytes. A4095-square elimination basis uses134,152,200 bytes; one additional780-row block uses25,552,800 bytes. Thus streaming or six-sample-plus-adaptive elimination fits a512MB cap comfortably, provided copies are accounted for. Ten stacked samples use255,528,000 bytes before rank-workspace copies, so a copied ten-sample matrix should not be the default.

The rank elimination is cubic in roughly4095, and can require tens of billions of modular scalar operations. No wall-clock guarantee is inferred from the small row-generation cost. A future authorized run should first time a small representative exact modular rank calculation, then choose a hard wall-clock limit and stop without expanding beyond the budget. A prospective cap is512MB and120 seconds; it has not been exercised here.

## Historical certificate-design requirements (run cancelled)

Preserve the curve/subgroup fixture identifier, sampled points, all support coefficients, row and column ordering, modulus, and pivot-row identifiers. Any rank claim should be independently replayable from these exact inputs. A roughly4092-square rank minor can be stored with16-bit field entries in about33.5MB if desired; its generating sample/row-pair indices are much smaller. Do not equate a probabilistic rank estimate or a decomposability-unchecked kernel with an exact result.


## Forced canonical kernel: corrected algebraic target

Let V_H be the three-dimensional syndrome space of canonical weighted tag functions from the existing fixed-subgroup analysis. For any two actual distinct fiber tags a,b, their support space contains two independent canonical single-fiber syndrome directions in V_H. Thus the degree46 recurrence R_((N−aB)(N−bB)) has rank at most one on V_H.

This holds for arbitrary generic tags as well, not only the finite torsion tags. Each matrix entry on V_H has degree at most one separately in a,b, so each2×2 minor has bidegree at most(2,2). There are t=(ell−1)/2>=5 actual tags. Fixing an actual a gives at least t−1>=4 distinct roots in b, so the minor vanishes identically in b. Repeating for the t values of a proves that it vanishes identically in both variables. This is direct low-degree interpolation in the two tags, not an unjustified interpolation from torsion P-values on the parameter curve.

For any degree-five extra factor J, the recurrence for J(N−aB)(N−bB) factors through the degree46 recurrence by convolution with J. Its restriction to V_H still has rank at most one. Therefore every Plücker constraint kills Lambda^2(V_H), a subspace of dimension choose(3,2)=3. This remains true at every generic parameter where the formulas are defined.

Had the full linear kernel equaled this3-space, all its nonzero bivectors would be decomposable and would describe only lines contained in V_H. This would be a canonical-only classification, not an absence-of-lines result. The elementary sunflower bound now makes this computation unnecessary for the proposed family.

A separate forced kernel arises if P is fixed while H varies: all supports contain the same five extra coordinates. Their syndrome space C has dimension5, so C wedge V is annihilated and has dimension5*91−5*6/2=440. More generally common error-support directions must be accounted for before interpreting a Plücker rank. None of these observations warrants running a new cross-subgroup scan.
