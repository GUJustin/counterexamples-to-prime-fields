# Independent audit: quadratic-13 global coefficient bootstrap

2026-09-19. Outcome: the binding-shape routing proof for a quadratic
factor with NONZERO discriminant passes. The zero-discriminant case
is a linear factor of multiplicity 26 and is not covered.
This is not by itself a complete better.codes certificate.

## Local coefficient constraint

At a good centroid node, translate Y by P_c(X). Although contact support
was originally centered at the fixed received symbol, the difference
P_c(x+t)−word vanishes to order at least one. Translation therefore sends
a term t^iY^j to terms of indices (i+ell,j−ell) or greater t-order;
i+j+min(i,12) cannot decrease. Thus the support condition survives.

Write centered G=Y²−Disc(G)/4 and centered H=sum H_jY^j, and let
delta=ord Disc(G). Use the real convex function
phi(s)=max(0,s/2,s−12); its integer ceiling is
nu(s)=max(0,ceil(s/2),s−12). The endpoints (26,0) and (0,13delta)
of the Newton polygon of G^13, added to any vertex of NP_H, are points
of NP_A by the Minkowski product rule. They need not themselves be
vertices of NP_A. Every such point still satisfies the convex support
lower bound. Convexity extends the resulting bound to all H coefficients;
rounding their integer valuations gives exactly

    ord H_j >= max(0,nu(a−j−26),nu(a−j)−13delta).

This argument uses convexity of phi, not the generally nonconvex ceiling
function. The leading H coefficient is a unit at good nodes, and char!=2
suffices for the centered quadratic formula. Coefficient degree bounds
are deg_X H_j<=(17−j)w+12, because translation by P_c preserves weight.

## Exact initial certificates

Read the finalized proof `QUADRATIC13_CENTERED_COEFFICIENT_ROUTING.md`
and exact certificate `quadratic13_global_coefficient_certificate.py`.
Independently reran the certificate: PASS. Then separately rechecked its
permanent JSON receipt's rational dual inequalities for a=0,...,43 and
all delta values from the required minimum through 100. Recomputed all
twelve upper bounds and K=C−1−12R(67)=6801344498272. For delta>=3 the
coefficient cost stabilizes, so the nonnegative discriminant multiplier
extends the check to every larger delta. This stabilization follows
because nu(a−j)<=31<39; only the delta-independent first term remains.
At a<31, charging coefficient cost zero is a relaxation, not a claim
that the actual coefficient or discriminant valuation is zero.

Every j=0,...,11 has certified rank upper bound strictly below K, assuming
H_j is nonzero and hence obeys its degree budget. Thus all twelve of these
coefficients vanish identically. No stronger vanishing assertion for j>=12 is used. The weakest-looking
end case j=11 already has exact upper bound 6639924735405, below K by
161419762867. The permanent certificate uses explicit rational formulas and no
optimizer; all rational inequalities and exact sums were checked.

Bad-node accounting is valid: at most 12 nodes have nonunit leading H
coefficient; each has contact at most 67. Deducting 12R(67) and padding
the good profile to n states with zero-contact nodes relaxes the system.
It does not count bad nodes as actual centroid nodes.

## Bootstrap and independently derived centroid certificate

The identity H=(Y−P_c)^12 J, deg_Y J<=5, follows. At a noncentroid good
node, G has multiplicity at most one at the received symbol and H at
most five, so A=G^13H has multiplicity at most 18. Therefore contact
at least 19 forces a centroid node. At such a node delta cannot be zero:
G(P_c)=-Disc(G)/4 would be nonzero, leaving multiplicity at most 17
from H. Thus delta>=1 whenever a>=19. The original quadratic argument
still gives delta>=2 whenever a>=43.

Independently derived and checked on all 44 contact states the exact dual

    1[a>=19] >= alpha R(a)−beta (1[a>=19]+1[a>=43])+gamma,
    alpha=1/23273351,
    beta=1557205/23273351,
    gamma=−4730625/23273351.

Using total discriminant budget 2w=262142 and padded state count n gives

    clean centroid count >= 5153030705162/23273351,
    hence clean centroid count >= 221414.

This exceeds 211940=n−181275+w. It also exceeds w+1, so interpolation
on centroid coordinates first proves P_c=P_0+ZP_1 with coefficient
polynomials of degree at most w. Each degree-at-most-w candidate with
181275 agreements then overlaps these coordinates in at least
221414+181275−262144=140545>w points and equals this affine pencil.
The polynomial identity removes potential rational-in-Z denominator
specializations before applying the conclusion to individual labels.

Scope: this closes the stated nonzero-discriminant quadratic-13 repeated-leading-factor
routing subcase. Application to a benchmark score still needs the
surrounding no-large-selected-pencil hypothesis and all other branches.

## Final artifacts audited

SHA256 values after independent replay:

- `QUADRATIC13_CENTERED_COEFFICIENT_ROUTING.md`: `4d3ed77cd300350edbce5bf6b0867e96303a140276b059cf3f42b9010728efb9`
- `quadratic13_global_coefficient_certificate.py`: `f26ac1037460fc4acf147af808b0442d10589b33d57b58716d7dc8a9be27c512`
- `quadratic13_global_coefficient_certificate.json`: `a9f7553198d142112466a3d8c5e596f1a220d0f2ac7e560617ffc982f02f6334`
