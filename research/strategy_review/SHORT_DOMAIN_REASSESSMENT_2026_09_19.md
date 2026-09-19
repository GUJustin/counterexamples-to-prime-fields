# September 19 short-domain research decision

This checkpoint records a change in research direction, not a new lower bound.

The subsequent positive manuscript improvement is a sharper matched list
comparison: elementary shortening replaces the norm-one example's universal
22N bound by 4N/3, so its N/2 list is within a factor 8/3 of the maximum.
The broader band now has upper bound 9N/4 already for p>=53, replacing
137N at p>=401. For T=ceil(cp), sqrt(2)<c<2, the upper bound is
(2/(c^2-2)+o(1))N. This improves the comparison, not the construction;
the example remains an extension-alphabet, vanishing-rate family.
Exact arithmetic is replayable in
[the certificate folder](../rs3_anchor_list_bound_2026_09_19/README.md).

## Keep the actual positive results distinct from the missing target

The manuscript already contains prime-alphabet constructions with superlinear
exception counts and singleton lists. Their rate and normalized margins
vanish. The missing decisive prime-field result is fixed positive rate and
fixed positive margin in the relevant first-order regime, or a comparable
construction on prescribed practical domains. No better.codes improvement
has been established.

The exact odd Gold refinement is an extension-field result. Its characteristic
is smaller than its message degree; it is not an example within the
large-characteristic hypotheses of the current DKT first-order theorem.
Its sharper label count and exhaustive lists do not remove that mismatch.

## Park the Frobenius-twist transfer route

The direct identity G^p-G=Lambda F^p forces p to divide the domain length.
The audited fixed-twist and affine-twist notes close two natural modifications
at short prime-field domains. For the affine family, reversal at infinity
reduces the distinct native locators to a reciprocal pencil; including the
common-locator branch gives a linear displayed-challenge bound under the
explicit residual and common-agreement hypotheses.

The next two-dimensional candidate also fails: the pair-omission family
G_ab=H/((X-a)(X-b)) has quadratically many reciprocal presentations, but
at most 3 deg(H)-6 distinct pairs can lift to an affine plane of twists
when p-n>=3 and the residual degree is below n. This is proved before
imposing a common received line. See
[the pair-plane proof](../binary_characteristic_transfer/PAIR_OMISSION_TWIST_PLANE_GATE.md).

Allowing an unrestricted twist merely defines

    A_i=G_i^(p-1)-(Lambda/G_i)F_i^p.

It does not construct shared high-degree coefficients of the residuals.
Do not resume by increasing the dimension of that tautological parameter
space or by scanning more locators. Resume only with a new explicit identity
that independently supplies a common residual head, native split supports,
and the required agreement inequalities.

## The existing quadratic bank also has a proved resource limit

For P_theta=theta+X^2/theta, arbitrary fresh words satisfy
B(T-CA)<=L n, where L is the number of retained bank members. Each common-core
coordinate belongs to at most two bank graphs, so L a<=2 n_core when each
member has a core agreement. A square-root-scale core therefore restricts
L to O(sqrt(n)); constant relative loss then gives only O(n) challenges.
This is not caused solely by requiring singleton lists.

[The arbitrary-word incidence note](../prime_quadratic_line/ARBITRARY_FRESH_WORD_CONIC_BANK_MAPPING.md)
specifies the possible escape: either abandon the large shared core for most
witnesses or change the coefficient family. A different fresh grid alone
does not suffice.

## Current bounded investigation

For an unrestricted quadratic bank, lift a native prime-field word to
(x,x^2,f(x)). This graph has no three collinear points, and quadratic
agreements are exactly point-plane incidences. The inspected general
incidence theorems retain the n^(3/2) balanced scale; their hidden constants
do not prove a sublinear list above the first-order threshold.

The remaining concrete investigation is the geometry of many quadratics
with c sqrt(n) native agreements for sqrt(3/2)<c<sqrt(2), n<p. Large lists
force many pairs of quadratics to share two agreement coordinates. We are
testing what that condition actually forces, without assuming it yields a
conic or a finite subfield. An applicable graph-specific incidence saving
would be a new upper-bound result; a matching rich prime-field geometry
could instead supply a new construction. Neither has been established.

No cloud rental or broad finite scan is justified by the current state.
