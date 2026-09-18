# Quadratic-cover augmentation of the ten- and eleven-cubic sources

## Result and scope

Neither the complete ten-cubic source on eighteen coordinates nor the complete eleven-cubic source on nineteen coordinates constructed here admits a fresh degree-six section with at least thirteen agreements after any connected degree-two map from a projective line, provided every selected fiber consists of two distinct points. This is an exact characteristic-zero result for these two fixed sources. It therefore also excludes a fresh fourteen-agreement section. It does not exclude deforming the source, exchanging selected incidences, changing the cover degree, or allowing ramified selected fibers.

The source ten lives over Q(sqrt(17)), with two added conjugate nodes satisfying `358θ²+125θ−25=0`. Source eleven lives over Q(sqrt(39)), with one added node satisfying `θ²+4175θ/3826+4525/15304=0` and two added rational nodes. Their coefficients and original coordinates are those in the previously verified source certificates.

## Complete norm enumeration

For a connected quadratic cover write `Z²=B₂(X,V)` with squarefree binary B₂. Every degree-six section has the form `E₃+Z O₂`. The case O₂=0 is a pulled-back cubic: thirteen matches require at least seven source matches, and source completeness leaves only the existing list.

For O₂ nonzero at most two selected fibers are full. Its monic norm is

`H(X,w)=w²+B₃(X)w+C₆(X)=(w−E₃)²−B₂O₂²`.

Thirteen matches require either at least twelve distinct norm-hit fibers or exactly eleven norm-hit fibers and two full fibers. The latter obey H=H_w=H_X=0 at the two full fibers. All these constraints are linear in the eleven coefficients of B₃,C₆. Thus it suffices to enumerate every twelve-subset, and every eleven-subset with every possible full pair. A full-rank eleven-subset fixes its norm, so it is sufficient to count all nodes satisfying both derivative conditions. Rank-deficient eleven-subsets are refined separately for every pair.

## A specialization-safe screening step

The sources have good, distinct-coordinate reductions at primes 47 and 61 respectively. Linear systems are first solved over these residue fields. Every base subset whose coefficient matrix has rank below eleven is retained for exact replay, **including modularly inconsistent systems**: there are 588 such subsets for the ten-source and 1154 for the eleven-source. This is essential, since a deficient inconsistent reduction can acquire a nonintegral solution in characteristic zero. An inconsistent system with coefficient rank eleven has an augmented rank-twelve minor and is safely impossible in characteristic zero. A consistent system with coefficient rank eleven has a unit coefficient minor and therefore fixes an integral norm. Exact rank-deficient eleven-subset systems are refined at every possible full pair; none remains unresolved.

For systems with a unit rank-eleven coefficient minor, the unique norm is integral. The necessary binary-sextic condition `J=E₃²−C₆=B₂O₂²` is screened using the closed projective image

`P(H⁰(O(2))) × P(H⁰(O(2))) → P(H⁰(O(6))), (B,O) ↦ BO²`.

This image is closed because the domain is projective. Thus specialization preserves membership even when the branch form B acquires a double root. Over an algebraic closure its condition is binary odd-multiplicity degree at most two. The implementation retains both degree zero and degree two, as well as the zero sextic. It counts infinity multiplicity as `6−deg(J)`. It never rejects a scalar square merely because the covering curve would become disconnected in that reduction.

All retained support systems are solved exactly using rational restriction of scalars for the relevant quadratic field. Distinct systems are retained through exact solving before exact norms are deduplicated. The exact binary squarefree part is then computed over that quadratic field.

## Receipts

* Ten source: 412 closed-condition survivors plus 588 coefficient-rank-deficient base subsets, 48 distinct exact norms satisfying the required fiber conditions, and no unresolved affine spaces. All forty-eight have binary odd-multiplicity degree zero.
* Eleven source: 444 closed-condition survivors plus 1154 coefficient-rank-deficient base subsets, 61 distinct exact norms satisfying the required fiber conditions, and no unresolved affine spaces. All sixty-one have binary odd-multiplicity degree zero.

Scripts and receipts are `ten_quadratic_norm_screen.*`, `ten_quadratic_norm_exact.*`, and the corresponding `eleven_` files. Each bounded job completed in under four seconds. All coefficient-rank exceptions are covered by exact replay, rather than an integrality assumption. An independent implementation is being audited separately.
