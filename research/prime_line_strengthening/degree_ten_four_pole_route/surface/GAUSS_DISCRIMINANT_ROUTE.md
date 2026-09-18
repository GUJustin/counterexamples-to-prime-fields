# A degree-62 residual discriminant cycle

The computations below justify a smaller elimination target than the
degree-1200 subresultant coefficients. They do not yet compute its defining
polynomial or exclude its high-multiplicity points.

Let S be the surface after the sixteen blowups certified in
`RESOLVED_BASE_LOCUS.md`, and L its basepoint-free moving class. Then
L²=14, K.L=14, c2(S)=20, and p_a(L)=15.

## Ramification determinant and rank-one locus

The affine determinant J=det(F_i,partial_X F_i,partial_Y F_i) is a section
of K+3L after the basepoint corrections. Its weighted degree is97 and its
Y degree28. These full degrees show that neither original boundary divisor
is a component. At a multiplicity-m basepoint its expected correction is
3m−1. Direct Hasse calculation gives exactly11 at the fourfold points,
17 at the sixfold points, and2 at each extra simple point. Thus none of
the sixteen exceptional divisors is a ramification component.

Over F29, J is the product of the seven old cubic graph equations and a
single irreducible factor Gamma of weighted degree76, bidegree(73,21),
with135 nonzero terms. Every old factor has exponent one. The gcd of all
nine two-by-two jet minors is one, so the jet matrix has rank at most one
only at finitely many affine points. There is no divisorial rank-one locus
at the boundary or exceptional divisors either, since none is even a
component of the determinant after the prescribed correction. These
facts transfer to characteristic zero using the exact forms, their full
degrees, and the saved nonzero coefficient witnesses.

The exact modular computations and exceptional orders are in
`gauss_determinant.py/json`. No assertion that the residual factor is
absolutely irreducible is needed for the cycle argument below.

## Universal jet incidence has the expected dimension

On S times the projective member plane, the universal first-jet section
has rank three. Basepoint-freeness excludes rank zero. Rank-two jet points
lie on the ramification divisor and have a unique incident member;
rank-one jet points are isolated and have a projective line of incident
members. Hence its zero scheme has dimension one, the expected codimension
three, and its cycle is the top Chern class. Pushing to the member plane
gives an effective discriminant cycle of degree

    c2(J1 L)=c2(S)+2 K.L+3 L²=20+28+42=90.

This is a cycle with multiplicities, not a claim that the reduced
discriminant is a degree-90 curve or that every singular member is nodal.

## Seven certified contributions of degree four

Each old cubic strict transform B is a disjoint(-4) curve with L.B=0.
Its first-order normal sections along the old-factor parameter line have
degree four on B. For the first old curve the two sections, after removing
the27 forced intersection orders, are

```
24+14X+2X²+27X³+12X⁴,
25+27X+28X²+9X³+6X⁴.
```

They have gcd one and no common projective root. Thus their ratio has
degree four and is separable. Equivariance gives the same conclusion for
all seven old curves. The determinant is simple along each B, so the
corresponding incidence component pushes to its old-factor line with
multiplicity exactly four. The saved witness is
`old_curve_gauss_degree.json`; the nonzero resultant also certifies the
degree in characteristic zero.

Subtract these seven known contributions. The remaining effective
parameter discriminant cycle has degree62. It need not be irreducible:
isolated rank-one jet points may contribute additional parameter lines.
They are not detected merely by factoring the ramification determinant.
Accordingly, implicitizing Gamma alone is not automatically the complete
degree-62 polynomial.

If Gamma's image is the sole residual component and is geometrically
irreducible, its Gauss map need not have degree one. Biduality only makes
the branch-curve-to-dual map birational in characteristic zero; several
ramification points may lie over a generic branch value. For a degree14
map with simple ramification, this multiplicity is at most7. Were its
entire pushforward of degree62, the possibilities would be map degree1
or2, and reduced image degree62 or31. These are conditional alternatives,
not a computed generic degree.

## Why this can replace the large subresultant gate

An integral rational member of |L| has total delta15. Choose a generic
pencil through it whose other section avoids its finitely many singular
points; the local total spaces are smoothings. Its discriminant
intersection multiplicity is the sum of the singularities' Milnor numbers,
at least their total delta15. Thus the member parameter has multiplicity
at least15 in the discriminant cycle. It cannot lie on an old-factor line,
since that would make the member reducible. Therefore the residual
degree-62 cycle also has multiplicity at least15 at its parameter.

An actual equation of that cycle would supply degree-at-most48 derivative
conditions for this necessary locus, substantially smaller than the
previous subresultants. The remaining tasks are to account for isolated
rank-one image lines and to implicitize the Gauss image with its correct
degree. The present certificates establish the bounded target, not its
solution or any rational member.
