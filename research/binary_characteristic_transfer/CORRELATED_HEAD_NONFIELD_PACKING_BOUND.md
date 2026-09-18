# Universal packing bound for the correlated-head four-space target

September 18, 2026. Independently checked by upper_bound_route. This closes the requested exponent improvement even on non-field additive domains.

Fix a seven-dimensional F_p-linear domain D in any finite coefficient field, fixed correlated heads u,w, and a family of distinct labels represented by admissible four-space locators in `CORRELATED_HEAD_FOURSPACE_TARGET.md`. Choose one representative locator per label, including at most one from the exceptional collapsed label.

For two distinct labels, the difference of their complete multiplied residuals is

    (z_i-z_j)X^(p³)-(alpha_i-alpha_j)X^p-(beta_i-beta_j)X.

Their four-space root supports cannot intersect in dimension four. If they intersect in dimension three, the monic locator of that intersection must be

    J_U=X^(p³)+B X^p+C X,

because the displayed difference has exactly degree p³ and vanishes on all p³ points of the intersection. In particular it has no X^(p²) term.

Every containing four-space locator is J_U^p-gamma J_U and has b=B^p. The admissibility equations force b≠0, so B≠0. Substitution then gives

    u=B^(p³),    w=-C^(p²)/B^p.

Frobenius is injective. Thus for fixed u,w there is at most one possible such locator J_U, and hence at most one three-dimensional core U that can occur as an intersection of supports at distinct labels. This conclusion uses no relation Frobenius^7=identity and applies to non-field domains.

Delete all selected supports containing this one core, if it exists. There are at most [4 choose1]_p=p³+p²+p+1 of them. The remaining four-spaces intersect pairwise in dimension at most two. In the seven-dimensional dual space their annihilators are three-dimensional and intersect in dimension at most one. Packing their two-dimensional subspaces yields

    M≤[7 choose2]_p/[3 choose2]_p+[4 choose1]_p=O(p^8).

For N=p^7 this is O(N^(8/7)), below the uncompressed p^5 example's exponent 6/5, and still further below the new projective-quadratic exponent 3/2.

This also clarifies the shared-core note: a nonconstant-b common three-core (nonzero X^(p²) coefficient) cannot carry two distinct labels. Any multi-locator family through it must lie on the single collapsed-label chart. The earlier kernel reduction was correct but did not use this residual-difference restriction.

Scope: the family must use the stated correlated heads, direction X^(p³-1), degree-<p canonical witnesses, and four-dimensional subspace root supports. This does not exclude unrelated received lines or fresh witnesses with non-subspace supports. It supplies a definitive stopping criterion for the specific designed-non-field-domain route.
