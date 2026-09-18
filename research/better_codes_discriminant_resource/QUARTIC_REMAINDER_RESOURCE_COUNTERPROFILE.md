# Quartic multiplicity ten: a feasible local resource profile

## Verdict and scope

The branch `A = G^10 H`, with Y-degrees four and three, survives the present own-system rank, Newton, discriminant, resultant, centered-coefficient, and centroid-support tests. The integer profile below satisfies even the stronger monic caps `wt(G)=4w`, `wt(H)=3w`, with no leading-coefficient exceptional nodes. It also satisfies every cross-centroid coefficient budget checked below.

This is a counterprofile to a proposed exclusion using these necessary resources. It is **not** a construction of global polynomials, an actual contact source, or a universal primary factor. In particular, the number called contact below is compatible with the leading-coefficient Newton condition; realization of a complete source F with those contacts is not asserted.

Use `n=262144`, `w=131071`. The required own-system rank sum is `C-1=6802316684344`. The profile gives `6868513256865`, a surplus of `66196572521`.

## Exact profile

Coefficient-order vectors are ascending in Y, omitting the monic leading coefficient. They refer to the local coordinate Y minus the received value. At each row choose generic nonzero leading coefficients of the indicated powers of the local parameter.

| Nodes | Contact | G orders (degrees 0–3) | H orders (degrees 0–2) |
|---:|---:|---|---|
|4|0|(0,0,0,0)|(0,0,0)|
|11|33|(2,1,1,0)|(2,1,1)|
|21847|32|(2,2,1,0)|(1,1,0)|
|43682|33|(2,2,1,0)|(2,1,1)|
|21841|33|(3,1,1,0)|(3,1,1)|
|10923|42|(3,2,1,1)|(1,1,0)|
|65535|43|(3,2,1,1)|(2,2,1)|
|32766|42|(3,2,1,1)|(3,2,0)|
|21845|43|(3,2,3,2)|(2,1,1)|
|43690|43|(3,3,1,2)|(2,1,1)|

The counts sum to n. Tropical convolution gives the generic coefficient orders v_j of G^10 H. Every row satisfies

`min_j (v_j + j + min(v_j,12)) = contact`.

Thus it meets the exact leading-coefficient Newton necessary condition. The independent verifier also recovers both factors' root valuations by taking the lower convex envelope through a different algorithm.

Generic leading coefficients ensure distinct residual roots on each Newton edge, distinct residual roots between G and H when their slopes coincide, and no cancellation in the finitely many invariant expressions used here. These are simultaneous nonempty Zariski-open conditions over characteristic zero (and sufficiently large characteristic). Consequently these resource orders are locally realizable by actual monic coefficient polynomials. This local observation does not glue them into global bounded-degree coefficients.

## All principal resource totals

| Resource | Used | Degree/support bound |
|---|---:|---:|
|Disc G|1572830|1572852|
|Disc H|786415|786426|
|Res(G,H)|1572830|1572852|
|G centered degree-two coefficient|218449|262142|
|G centered degree-three coefficient|393208|393213|
|G centered constant coefficient|524277|524284|
|H centered degree-two coefficient|262139|262142|
|H centered constant coefficient|393208|393213|
|Difference of centroids|131070|131071|
|G centroid equals received word|174759|211940|
|H centroid equals received word|196604|211940|

The centroid-difference row counts its full guaranteed local valuation, not just an indicator of simultaneous support. The centroids are taken in the distinct-centroid branch. Each individual support stays below the helper-forcing threshold. The centered coefficients are tested as nonzero polynomials; allowing an identically zero coefficient cannot invalidate this feasibility conclusion.

For monic degrees d and e, the degree bounds used are `d(d-1)w` for discriminants, `de w` for resultants, and `j w` for centered degree-j coefficients. Generic roots give discriminant order `2 sum_{i<j} min(v_i,v_j)` and resultant order `sum_{i,j} min(v_i,u_j)`.

## Cross-centroid budgets also survive

Let p_G and p_H denote the polynomial centroids. The totals of the orders of `G^[k](p_H)`, for k=0,1,2,3, are

`(524278, 371356, 218449, 131070)`.

They are at most `(4w,3w,2w,w)`. The corresponding totals for `H^[k](p_G)`, k=0,1,2, are

`(338595,240294,131070)`,

at most `(3w,2w,w)`. Here brackets denote Hasse derivatives. In an irreducible-factor application the value polynomials are nonzero; derivatives can in principle vanish identically. The profile satisfies even the stronger nonzero degree budgets for all of them.

## Verification and the remaining mathematical issue

`quartic_remainder_resource_lp.py` discovers the profile with a bounded linear program over 3509 distinct resource states. Its floating-point optimization output is not the certificate. The displayed integer counts are the certificate.

`verify_quartic_remainder_profile.py` independently checks them using exact integer/rational arithmetic, direct monomial rectangle rank sums, tropical coefficient multiplication, and a lower-envelope implementation independent of the discovery hull routine. It imports no optimizer. Its JSON receipt reports PASS. Discovery used 2.806 seconds and 72128 KiB; verification used 0.545 seconds and 5968 KiB, both under the prescribed 60-second/384-MiB bounds.

Several divisor budgets are within 1–22 degrees of saturation. The strongest missing condition is therefore simultaneous **global** realization: the same low-degree coefficient polynomials would have to realize all these nearly saturated local divisors and the received-word relations at the same nodes. Independent divisor inequalities do not express the resulting congruences or algebraic identities among invariants. A useful next theorem should impose such compatibility, or exploit actual full-source contact beyond its leading Newton necessary condition. This profile does not justify more scans of the same scalar-resource relaxation and does not improve the benchmark ledger.
