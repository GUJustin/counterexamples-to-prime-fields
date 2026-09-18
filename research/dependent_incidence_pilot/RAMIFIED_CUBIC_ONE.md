# Cubic Kuranishi check for the same saved pattern

## Result

For saved pattern11, clustered trial3, the cubic correction also fails to absorb the characteristic obstruction. The same normalized Jacobian has rank195 in200 variables and a five-dimensional kernel. After cancelling the quadratic term by a particular quadratic correction, all35 cubic monomial columns lie in the image of that Jacobian. A cokernel vector still sees the nonzero residual18.

Consequently this pattern has no lift over a mixed-characteristic DVR of ramification index three, over any residue-field extension. Combined with the earlier certificates it excludes indices one, two, and three. It is NOT an all-ramification obstruction. No new seed was considered, and the failed span test gives no reason to run a nonlinear root search for an index-three correction.

## Exact calculation

Retain the notation and fourteen-coordinate normalization from RAMIFIED_QUADRATIC_ONE.md. Let

    F(z0+delta)=F(z0)+J delta+Q(delta)+T(delta)+higher terms

modulo41, where Q and T are the homogeneous quadratic and cubic Taylor parts, and let Z be the saved full kernel basis of J. The previous certificate gives Q(Zt) in im J coefficientwise for all t in five variables.

The generator chooses one quadratic polynomial vector w(t) with all free coordinates zero and

    J w(t)=−Q(Zt).

It then expands F(z0+Zt+w(t)) through total degree three. The linear and quadratic coefficients vanish; the cubic coefficient is

    K3(t)=T(Zt)+Q(Zt+w(t))−Q(Zt)−Q(w(t)),

where only the degree-three part of the latter expression contributes. Equivalently, the second summand is the polarized quadratic form evaluated at Zt and w(t). The35 coefficients in five variables are saved exactly modulo41.

The calculation verifies

    rank[J | coefficients(K3)]=195=rank J.

A saved row vector lambda satisfies

    lambda J=0,
    lambda K3(t)=0 identically,
    lambda[-F(z0)/41]=18 mod41.

Changing the chosen second-order correction to w(t)+Z q(t) does not change its cokernel cubic term: the difference is the polarization of Q on two kernel vectors, and the preceding quadratic calculation says that polarization is identically zero in coker J. This also handles an arbitrary individual second-order kernel correction in a hypothetical lift.

## Index-three interpretation

Write 41=u pi³ in a hypothetical DVR, with u a unit. If the least deformation valuation is one, the first-order coefficient belongs to ker J. The second-order coefficient solves the displayed quadratic equation and therefore differs from w(t) by a kernel vector. Projecting order three with lambda annihilates both the third-order linear correction and the full corrected cubic contribution. The projected constant is a nonzero residue times u, a contradiction.

If every deformation coordinate has valuation at least two, the projected constant already has valuation three, strictly smaller than the quadratic and higher terms; the projected linear term has valuation at least five because lambda J vanishes modulo41. This also contradicts the equations. The normalization is legitimate over the DVR by the same unit-valued geometric transformations used in the previous certificate.

At larger ramification the projected equation may first see a quartic or higher term. The vanishing of the quadratic and cubic cokernel maps is not evidence of an actual formal lift; nor does it force the tangent vector to vanish. No all-order conclusion is asserted.

## Independent replay

`ramified_cubic_one.py` generates the particular correction and cubic coefficients; `ramified_cubic_one.json` saves them and the constant-obstruction vector. Its guarded run took about0.56 seconds.

`verify_ramified_cubic_one.py` is a separate stdlib verifier. It independently reconstructs J and the integer residual, checks rankJ=195 and the full kernel basis, and evaluates the corrected Taylor expansion by truncated one-variable arithmetic at all56 points of the lower grid

    t in {0,1,2,3}^5, sum(t)<=3.

That grid is unisolvent for total-degree-at-most-three polynomials over F41: the multivariate falling-factorial basis gives a triangular evaluation matrix with nonzero factorial diagonal. Thus these checks verify every cubic coefficient, rather than sample a polynomial identity. It then checks rank[J|K3]=195 and all entries of the cokernel certificate. The independent run passed in about1.17 seconds under the384MiB/60-second guard. JSON verification and resource reports are stored alongside the scripts.
