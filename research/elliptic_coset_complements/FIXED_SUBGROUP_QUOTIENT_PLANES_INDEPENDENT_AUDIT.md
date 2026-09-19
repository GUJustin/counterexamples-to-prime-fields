# Independent audit: fixed-subgroup quotient planes

Date: 2026-09-18. Verdict: **PASS**, with the scope below. This is an algebraic audit of the saved proof, not an elliptic fixture or a claim of source farness.

## Compiler and degree check

Write t=(ell-1)/2, r=t-2, n=(ell²-1)/2. The quotient x-map N/B has B=K², deg K=t, deg N=ell, and gcd(N,K)=1. The pole parameter must avoid ALL nonkernel torsion image tags. This guarantees L=N-bB is nonzero on the entire evaluation domain; choosing it outside only the selected tags would not suffice.

With C=K B^(r-2), the displayed rational formulas are exactly f=N^r/(K L) and g=-B^r/(K L). The word f is defined separately as zero at kernel coordinates. For p_S of degree at most r-2, C p_S(N/B) is polynomial, divisible by K, and has degree at most t+(r-2)ell=n-4ell. Its residual off the kernel is prod_(a in S)(N-aB)/(K L). Hence the canonical agreement is exactly r ell+t=n-2ell, including the kernel coordinates. Distinct omitted pairs give distinct supports, but pole choices are still needed for distinct labels.

## Disjointness check

For two different subgroups, removing both kernel coordinate sets leaves n-ell+1 nodes. Clearing both denominators gives degree at most n-ell for the received terms and at most n-ell-1 for a codeword term. Thus equality on these nodes forces an exact rational identity.

At a kernel root for H, the f_H term has a genuine simple pole, while the other subgroup's expression is regular by the all-tags pole exclusion. This forces its coefficient to vanish, and symmetrically eliminates both f terms. The remaining g terms have reduced denominators L_H and L_H'. Equality modulo a polynomial with both coefficients nonzero forces their complete finite pole divisors, including multiplicities, to agree. Monicity then gives L_H=L_H'.

Pullback by x gives a nonempty effective divisor of degree 2ell, invariant under both H and H', hence under E[ell]. Translation acts freely on geometric points, so every orbit has ell² points; invariance forces degree at least ell². This contradicts ell>2. The reasoning remains valid when b is a branch value, because divisor multiplicities are retained. The one-subgroup version also proves that each received plane has dimension two modulo the code.

## An additional exact canonical-count ceiling

Let P_H be these two-dimensional syndrome planes and let L be ANY two-dimensional syndrome plane of a proposed global received pencil. Count only projective syndrome classes of the displayed canonical witnesses, allowing nonzero scalar rescaling and addition of codewords.

If L=P_H for some H, pairwise zero intersection excludes every other subgroup plane, leaving at most binom(t,2) canonical classes. Otherwise dim(L intersect P_H)<=1 for each of the ell+1 subgroups, leaving at most ell+1 classes. Consequently the union of these particular canonical banks contributes at most

    max{binom((ell-1)/2,2), ell+1} = O(n)

distinct projective challenge classes on any genuine syndrome pencil. An affine chart cannot increase this count. This remains an upper bound when canonical labels within one subgroup collide.

This is NOT an upper bound for all words near the pencil, or for all errors supported on the two-coset omissions. Different error cofactors may occupy other points of the much larger support syndrome spaces S_U. This paragraph records the scope of the fixed-compiler proof only. The later TWO_FIBER_LINEAR_RESOURCE_BOUND.md proves an O(n) bound for arbitrary at-most-two-nonkernel-fiber errors with a far endpoint; only enlarged or different support models remain outside that closure. A received pencil whose syndrome span has dimension less than two is outside the stated count argument and cannot be substituted silently.

No finite Pluecker computation is needed to close this fixed-subgroup compiler. The unslacked agreement is above Johnson; testing it at the separately checked slack-five threshold does not itself prove source/common-agreement separation.

## Reviewed source

SHA-256 of FIXED_SUBGROUP_QUOTIENT_PLANES.md:

    dc6753efe2f21cdd5c88965cdd4647d399cf61d55f4262984c07f6375cb3db35


## Independent extension: the entire weighted-tag three-space

The following algebra extends the checked result beyond one pole choice. Put C_H=K_H B_H^(t-4), and define e_j=C_H Y_H^(t-3+j), j=0,1,2, extended by zero on the kernel. As rational functions,

    e_j=N_H^(t-3+j)/K_H^(2j+1).

Let V_H be their syndrome span. It has dimension three: a code relation, cleared by K_H^5, vanishes at all n-t nonkernel nodes, while its numerator has degree at most ell(t-1)<n-t. Thus it is a rational identity. Successive pole orders 5,3,1 at a kernel coordinate force all three coefficients to vanish.

For H distinct from H', e_0,H does not belong to V_H'. Indeed, clear K_H K_H'^5 in a proposed relation modulo a codeword. The first numerator has degree n-ell-2, the other received numerators have degree at most n-ell, and the codeword numerator has degree n-ell-3. The n-ell+1 off-kernel nodes force a rational identity, contradicted by the simple pole of e_0,H at a kernel root of H. This is an assertion about syndrome classes, with the separate zero extensions already accounted for by omitting kernel nodes.

Here is also a direct check of the asserted pencil of planes. Write the tag locator as F(Y)=Y^t+c1 Y^(t-1)+c2 Y^(t-2)+.... Modulo codewords, the inverse function C/(Y-b), for F(b) nonzero, is proportional to

    (b²+c1 b+c2)e0+(b+c1)e1+e2.

This follows by dividing F(Y)-F(b) by Y-b. Also f_b+b^(t-2)g_b is e0 modulo codewords. Therefore P_H(b) is precisely span(e0,(b+c1)e1+e2). These are all planes through e0 except the infinity plane span(e0,e1) and the finitely many forbidden tag parameters.

If dim(V_H intersect V_H')>=2, its intersection with each forbidden plane is proper: otherwise that two-plane, and hence e0,H, would lie in V_H', contradicting the preceding paragraph. The same holds on the other side. Over the algebraic closure choose a nonzero common vector outside this finite union of proper subspaces. It belongs to good P_H(b) and P_H'(b'), contradicting the pole/divisor argument, which is valid over this extension as well. Consequently

    dim(V_H intersect V_H') <= 1.

There is no finite-field-size assumption hidden in the generic-vector step: the contradiction is taken over the algebraic closure, and the earlier rational-function proof is field independent.

### Weighted-tag errors and the precise count consequence

Restrict errors to be zero on the kernel and, on each nonkernel quotient fiber, a scalar multiple of C_H. Their syndromes lie in V_H: interpolate the tag scalars by a polynomial of degree at most t-1; terms of degree at most t-4 give codewords. The syndrome of a single-tag error at a is proportional to

    v(a)=(a²+c1 a+c2, a+c1, 1).

The proportionality factor is nonzero, since tag roots are simple. Thus two-tag error supports give exactly the secant planes span(v(a),v(a')) in the three-dimensional vector space V_H. Each such error is supported on at most 2ell coordinates.

Let L be a genuine two-dimensional received syndrome space with at least one endpoint whose maximum codeword agreement is strictly less than n-2ell (in particular, endpoints far at the tested lower threshold suffice). It cannot equal a two-tag secant: equality would make every received word on that pencil within 2ell errors of the code. If L is contained in one V_H, it therefore obtains at most binom(t,2) projective points from its secants, and at most one point from each of the other ell subgroup spaces. If it lies in none, it obtains at most ell+1 points altogether. Hence the total is at most

    max{binom(t,2)+ell, ell+1} = O(n).

This extension covers all displayed weighted-tag errors, not arbitrary coordinate-dependent error cofactors within a fiber, five additional omissions, or a different shared-line compiler. The later TWO_FIBER_LINEAR_RESOURCE_BOUND.md extends the O(n) conclusion to arbitrary errors confined to at most two nonkernel fibers, with a far endpoint; extra-error and different-support transversals remain outside it. No source farness is inferred from these algebraic identities; it is an explicit premise of the secant count.

Current-status crosslinks and the reviewed source SHA-256 were refreshed after the three-edge-path linear bound. The underlying fixed-compiler algebra is unchanged.
