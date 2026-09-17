# Universal cross-coordinate Hermite rank audit

No improved global rank upper bound was found. A genuine universal saturation lemma rules out common cokernel identities supported entirely on the first **34336 local blocks** of the current Source00 map. These comprise **38.24448623%** of its local-rank allowance. This holds for arbitrary received values, not merely generic ones. The remaining blocks are not proved saturated.

## The precise received-word coupling

Write a source polynomial as `Σ_(i,j,z) Q_ijz(X)Y^i R^j Z^z`, with `deg Q_ijz<d_ij=max(D−w*i−(w−1)*j,0)` and `i+j+z≤L`.

At node x, the primary extraction (`LowerFoundation.lean:16185`) sends a monomial to terms

`Hasse_(r−f)(Q_ijz)(x) * binom(i,f) * (u0(x)+u1(x)Z)^(i−f) * a^f b^j Z^z`,

where `f≤i` and `f≤r`. The block then applies the contact jet modulo `(a−b)^(m−r)`. The terms f=i are independent of the received word. Terms f<i mix higher source Y degrees into lower local Y degrees and generally depend on both received values.

It would be invalid to cap each diagonal family by `min(d_ij,n*(m−i))` and add those caps: derivatives beyond that diagonal range can still enter the lower-degree rows through f<i. The safe familywise factorization uses all m Hasse derivatives.

## A valid global rank upper bound

Each fixed `(i,j,z)` coefficient family factors through the simultaneous m-jet map at all n nodes. Therefore

`rank(constraintMap) ≤ min(n*localRankBound, Σ_(i,j,z) min(d_ij,n*m))`.

This requires no assumption about received values. At the target, `d_ij≤D=m*A<n*m`, because A=181275<n=262144. Consequently the familywise sum equals the original source dimension C. Since the source has positive certified nullity, this upper bound reduces to the existing `n*localRankBound`; it saves **zero** constraints.

## Universal initial-block saturation lemma

Assume distinct evaluation nodes, `n≥w`, `L≥R+S`, and

`D−(w−1)S ≥ n(R+1)`.

Then the extraction onto all pre-contact local blocks `0≤r≤R` is surjective, for **every** pair of received-value functions u0,u1.

Proof: use only source Y degrees i≤R, and solve successively in descending i. The coefficient of local `a^i` contributed by source degree i has f=i, hence is the ordinary Hasse jet of `Q_ijz`, independent of u0,u1. Specify its derivatives of orders 0 through R−i at all nodes to correct the desired rows. Simultaneous Hermite interpolation is surjective because

`d_ij ≥ n(R−i+1)`;

indeed subtracting the right side gives at least `D−(w−1)S−n(R+1)+(n−w)i≥0`. Higher source Y degrees already fixed can contribute to lower local degrees, but these contributions are known and corrected at subsequent steps. They preserve total degree, so all necessary correcting coefficients remain in the allowed source box. Distinct-node Chinese remaindering proves this interpolation statement in arbitrary characteristic using Hasse derivatives.

Composing with each contact jet makes the projection onto the corresponding local target ranges surjective as well. In the numerical range used below, `m−r>S`, so the contact jet on every such block is injective: a nonzero multiple of `(a−b)^(m−r)` would have b-degree exceeding S.

## Exact gate

For `m=64000,L=3840000,S=19840,D=11601600000`, choose

`R=floor((D−(w−1)S)/n)−1=34335`.

The saturated local dimension is **44663615153314407616** out of **116784455894414962240**. The corresponding global projection rank is exactly **11708298730750452070088704**. Thus a common cokernel functional supported on these blocks must be zero. This does not rule out mixed dependencies involving later blocks, and does not prove that the full map has maximal rank.

`graded_gate.py/json` records this exact arithmetic. `small_matrix_check.py/json` independently constructs the actual extraction matrix over F101 with 95 rows and 129 source columns; both zero and nonconstant received-value examples have full row rank 95, as the lemma predicts. These are sanity checks for the proof, not a generic-rank assumption.

No numerical scan or full certificate recomputation was performed. The requested cross-coordinate shortcut remains open beyond this saturated projection; a useful new result must control the later mixed blocks rather than discard their received-word coupling.
