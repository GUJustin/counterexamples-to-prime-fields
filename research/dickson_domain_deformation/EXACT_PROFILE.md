# A characteristic-zero deformation with exactly eight above-capacity candidates

September 17, 2026. Strengthening of the finite p17 lift. The p41
obstruction and all growing-family limitations remain unchanged.

There is an algebraic-number received word on16 distinct nodes for the
dimension4 Reed–Solomon code whose complete list above4 agreements
consists of exactly8 polynomials, each with exactly6 agreements. Every
other polynomial has at most4 agreements. Arbitrarily large completely
split primes preserve this entire profile.

## Finite certificate

The original F17 word has22 polynomials with6 agreements and124 with5.
Eight of the22 are the selected Dickson bank already used in the smooth
32-equation,48-variable incidence lift. All16 nodes are covered; their
selected-bank incidence counts are

    2,2,4,2,4,4,4,2,2,4,4,4,2,4,2,2.

Among all binom(16,5)=4368 five-node subsets:

* 4112 do not interpolate to a degree-at-most3 polynomial modulo17.
* 48 are five-subsets of the selected bank's six-node agreement sets.
* 208 are unwanted consistent supports (14*6+124).

The probe saves16 tangent vectors for the selected incidence locus.
Every one of the208 unwanted support conditions has a nonzero derivative
on at least one of these vectors. `verify_extra_supports.py` independently
checks this by exhausting ALL4368 five-subsets, solving Vandermonde
systems, and differentiating the last-node interpolation residual.
It checks each supplied tangent vector directly against all selected
candidate incidences. The generator instead uses Lagrange coefficients
and the derivative of the top interpolant coefficient; the two derivative
vectors match after their independently computed nonzero scaling factor.

## Why the tangent certificate gives simultaneous avoidance

The previously certified invertible32-column Jacobian minor gives a
smooth Hensel chart for the selected incidence equations over Z_17.
The16 remaining variables are free local parameters. For each unwanted
five-support S, let F_S be the residual obtained by interpolating on
four nodes and evaluating at the fifth. Its denominators are units on
this chart, since the node residues are distinct.

The certificate shows that the differential of F_S on the chart is
nonzero modulo17. Therefore F_S is not the zero function on its
characteristic-zero local branch. This can also be seen analytically:
choose any Hensel lift; the derivative with respect to a free coordinate
is a17-adic unit in some direction. Restricting to residue-preserving
parameter variations scales that derivative by17 but does not make it
zero in Q_17. Thus the zero set of F_S has empty interior in the local
17-adic parameter ball. Avoid the finite union of these208 zero sets.

The4112 initially inconsistent supports remain inconsistent throughout
the residue-preserving ball: their interpolation residuals are units.
The48 intended supports remain consistent because they belong to the
selected polynomials. Distinct selected polynomials and their original
nonagreements also persist modulo17. Consequently any polynomial with
five agreements must coincide with a selected polynomial, and each
selected polynomial has exactly its six intended agreements.

This is one simultaneous choice of parameters, not separate deformations
chosen for separate supports. Equivalently, the product of the208
nonzero residual functions is nonzero in the smooth formal local domain.

## Algebraic and prime-field realizations

Encode all selected incidences as polynomial equations and all node,
candidate, nonagreement, and unwanted-support exclusions as finitely
many polynomial inequations. The Q_17 point proves this finite-type
Q-locus nonempty, hence it has an algebraic-number point. All coordinates
lie in one number field. At sufficiently large completely split primes
of its normal closure, preserve the finitely many nonzero determinants
and denominators. This preserves the complete above4 agreement profile.
There is no assertion that the original extra14 nearest polynomials
lift; this construction deliberately removes all their five-supports.
No explicit small-height algebraic coordinates are produced here.

## Quadratic-tower consequence

Combine with ../generic_fiber_nearest_lists/QUADRATIC_TOWER_PROFILE.md.
For every B=2^s, s>=1, there are prime-field instances of length16B and
dimension4B whose complete above4B list consists of exactly8 polynomials,
each with6B agreements. Every other polynomial has at most4B agreements.
Rate1/4, gap1/8, and list size8 are all exact. The prime may be arbitrarily
large along a suitable splitting sequence, with no polynomial-size
field guarantee. List size remains8 as length grows.

One may anchor at a lifted node over the third source node, where exactly
four of the selected polynomials agree. Restrict first to degree cap3B
(which still contains all selected compositions), then subtract the
anchor value, divide by X-x_*, and delete the anchor. The resulting word
on16B-1 nodes for dimension3B has exactly4 nearest polynomials with6B-1
agreements. Every other polynomial has at most4B-1 agreements: restoring
the anchor would otherwise give an unselected original candidate with
more than4B agreements.

The general unique-nearby compiler can therefore use pool threshold4B
and pool size U=4, with no external capacity-list theorem. Take q=8B+1
new nodes. The resulting line has

    n=24B, dimension3B, threshold6B,
    rate=gap=1/8,
    exactly32B+4=(4/3)n+4 uniquely nearby labels.

Every other label, including zero, has maximum agreement6B-1; nearby
labels have maximum agreement6B. Ordinary correlated agreement fails.
The compiler's explicit sufficient inequalities hold, for example,
when p>=32(8B+1)^2: the collision term is below1/4, the node-exclusion
bound is42B-6, and the outside-pool term is at most

    binom(24B,6B)/p^(2B) <= (4096/p)^(2B) < 1/16.

This field cutoff is ONLY for the compiler after a good source
specialization. The entire algebraic configuration may require a much
larger splitting prime. There is no polynomial-field construction claim.
The count is linear in n and the far/near separation is one coordinate;
this is not a superlinear fixed-gap result or a global list-size bound.
