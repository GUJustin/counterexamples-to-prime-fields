# Centered coefficients close the separable quadratic13 branch

This is a proved binding-shape subcase, not an all-context ledger or a
better.codes improvement. It uses the root's centered-coefficient observation
and an exact finite certificate checked independently. No manuscript change
or benchmark certificate is asserted.

Work over K=k(Z), with n=262144, w=131071, target agreement A0=181275,
and characteristic p=2130706433. Let F be universal for the full primary
kernel and have the exact own-system caps from OWN_SYSTEM_RIGIDITY.md:
weight55w, joint jet degree55, R-degree12, and total degree3261.
Assume its leading R coefficient A has Y-degree43 and factors as

    A=G^13 H,   deg_Y G=2,   Disc_Y G != 0.

Then every degree-at-most-w polynomial candidate agreeing with the received
line on at least A0 coordinates belongs to one affine codeword pencil.
In particular, the existing no-large-selected-pencil hypothesis bounds
the selected candidates in this branch. The nonzero-discriminant condition
is essential: G=(Y-P)^2 instead gives a linear factor of multiplicity26,
which this argument does not cover.

## 1. Existing numerical and geometric inputs

Weighted additivity, and 13>12, force wt(G)=2w. Normalize G monic in Y;
then G,H belong to K[X,Y], and wt(H)<=17w+12. Its centroid

    Pc=-[Y]G/2

is a polynomial in X of degree at most w. The earlier centroid argument
in CENTROID_DISCRIMINANT_ROUTING.md forces at least193753 good coordinates
where Pc(x,Z)=f_x+Zg_x. Interpolation on w+1 of them gives
Pc=P0(X)+Z P1(X), with P0,P1 in k[X] of degrees at most w. Thus there
are no rational-in-Z specialization exceptions in the resulting pencil.

The leading Y coefficient of H has X-degree at most12. Delete its at most
12 coordinate zeros. At every remaining good coordinate, actual contact
a satisfies0<=a<=43. The deleted coordinates each have contact at most67,
by a<=43+2 ord_x(lc_Y A) and total leading-coefficient order at most12.

Write R(a) for the exact local rank bound in OWN_SYSTEM_RIGIDITY.md.
Its ambient dimension is C=6802316684345. Consequently the good coordinates
satisfy

    sum R(a) >= K0=C-1-12 R(67)=6801344498272.

Pad by zero-contact fictitious coordinates to obtain n terms. Put
delta=ord_x Disc(G). Its total over good coordinates is at most2w=262142.
Initially a>=31 forces a centroid coordinate and delta>=1; a=43 forces
delta>=2. These are the previously proved quadratic Newton/discriminant
inequalities.

## 2. A global resource for each centered coefficient

Use W=Y-Pc(X,Z), and write

    G=W^2-Disc(G)/4,   H=sum_(j=0)^17 H_j(X,Z) W^j.

The degree bounds are deg_X H_j<=(17-j)w+12.
At a centroid coordinate x, set t=X-x. Centering at Pc(X,Z), rather than
the constant received value Pc(x,Z), preserves the required Newton lower
bound: their difference has t-order at least1. Each translated monomial
t^i Y^j contributes terms with exponent pairs(i+l,j-l), and
i+j+min(i,12) cannot decrease.

The required real convex Newton lower function is

    phi(s)=max(0,s/2,s-12).

The two endpoints of the Newton polygon of G^13 are(0,13delta),(26,0).
The Newton polygon of A is the Minkowski sum with that of H. Adding
either endpoint to an H coefficient point must therefore lie above the
required lower bound for A. Since coefficient orders are integers, put
nu(s)=max(0,ceil(s/2),s-12) to obtain

    ord_x H_j >= c_j(a,delta)
      =max(0,nu(a-j-26),nu(a-j)-13delta).          (1)

The convex argument uses phi, not the nonconvex integer ceiling function.
Rounding is applied only to the resulting coefficient-order inequalities.
Cancellation in a polynomial product does not invalidate the Minkowski
identity for Newton polygons over the valued coefficient field.

If H_j is nonzero, (1) supplies the global constraint

    sum_(good a>=31) c_j(a,delta) <= (17-j)w+12. (2)

This constraint couples different coordinates; the earlier local profile
test and along-candidate G(P),H(P) budgets did not include it.

## 3. Exact certificate: H_0 through H_11 vanish

For each j=0,...,11, the accompanying pure-Python certificate constructs
nonnegative rational lambda_j,mu_j and an intercept b_j satisfying

    R(a) <= b_j+lambda_j delta+mu_j c_j(a,delta)

on all allowable good-coordinate states, interpreting c_j as zero when
a<=30. It checks every a=0,...,43 and all necessary delta values exactly.
For delta>=3 the coefficient cost stabilizes, so lambda_j>=0 extends the
finite check to arbitrarily large delta; no upper bound delta<=3 is assumed.

Combining this inequality with (2) gives a rank upper bound below K0 for
every j<=11. The largest of these twelve certified upper bounds is
6639924735405, still161419762867 below K0. Thus every H_j with j<=11
must be identically zero:

    H=W^12 J,   deg_W J<=5.                       (3)

The certificate needs no optimizer and records each rational dual and sum.
The separate exploratory optimization is not an input to this verification.

## 4. Bootstrap to enough centroid coordinates

At a good noncentroid coordinate, W is a unit at the received value. The
factor G cannot have a double root there, since a double quadratic root is
its centroid. Hence G^13 contributes received-root multiplicity at most13,
and J contributes at most5. Equation(3) therefore gives a<=18. Thus every
good coordinate with a>=19 is now a centroid coordinate. It has delta>=1:
if delta=0, G is nonzero at its centroid, so the received-root multiplicity
of A would be at most deg_Y H=17. The a=43 state still requires delta>=2.

The exact pointwise inequality for all a=0,...,43 is

    1[a>=19] >= (R(a)-1557205 delta-4730625)/23273351,

where it suffices to check delta=1[a>=19]+1[a>=43], because larger delta
only decreases the right side. Summation yields at least

    ceil((K0-1557205*(2w)-4730625*n)/23273351)
      =ceil(5153030705162/23273351)=221414

good centroid coordinates. Every candidate's A0 agreement set meets this
fixed coordinate set in at least140545 positions, exceeding w by9474.
The root bound therefore forces the candidate to equal P0+zP1. This holds
at every label z because the centroid identity is polynomial in Z.

## Scope and verification

Files quadratic13_global_coefficient_certificate.py/json contain the exact
certificate. The guarded run completes in under one second and uses less
than10 MiB. An independent audit checks both the Newton coefficient lemma
and the finite rational inequalities.

This closes the separable quadratic factor of multiplicity13 at the stated
exact factor shape; together with the prior results, separable quadratics
of multiplicity at least13 route or are excluded there. It does not cover
the linear multiplicities13--26, other exact factor weights or caps, or
the squarefree and smaller-multiplicity branches. It supplies no replacement
for the full normal-cost inequality and no regenerated passing ledger.

The subsequent [linear own-system helper](LINEAR17_OWN_SYSTEM_EXCLUSION.md)
separately excludes every linear leading factor of multiplicity at least17
at these exact caps. In particular it closes the zero-discriminant
quadratic13 case, which is linear multiplicity26. The quadratic proof
above retains its nonzero-discriminant hypothesis. The combined remaining
high-linear case is at most one distinct graph of multiplicity13--16;
the other shape and ledger limitations remain unchanged.
The same helper also upgrades the separable quadratic13 branch from
pencil routing to an outright contradiction: its proved nongraph contact
bound18 is below the helper's certified threshold25. This corollary is
proved in the linked note and does not alter the scope of the original
quadratic coefficient certificate.
