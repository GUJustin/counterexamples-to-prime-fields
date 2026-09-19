# A graph-power helper excludes linear multiplicities at least 17

September 19, 2026. This is an exact binding-shape theorem, not a complete
better.codes improvement. It uses the full-kernel own-system replacement
lemma and an explicit helper, rather than a conjectured rank defect.

Let F be a universal irreducible factor with the exact caps

    wt(F)=55w, deg_R F=12, deg_(Y,R) F=55,
    deg_(Y,R,Z) F=3261,
    n=262144, w=131071, p=2130706433.

Assume A=lc_R F has Y-degree43. Then A has no linear factor over k(Z)[X,Y]
of multiplicity at least17. It has at most one distinct linear factor
of multiplicity at least13. The possible single factor of multiplicity
13--16 remains outside this theorem.

## 1. Graph normalization, affine descent, and rank resource

Suppose A=(Y-P)^e H with e>=13, h=43-e, and the linear factor normalized
monic. Weighted additivity and e>12 force its weight to be w. Thus P is
a polynomial in X over k(Z), with degree at most w, and

    wt(H)<=h w+12.

Call a coordinate a graph coordinate when P(x,Z)=f_x+Zg_x. The leading
Y coefficient B of H has X-degree at most12. At all good coordinates
where B(x,Z) is nonzero, the actual first-jet contact a satisfies a<=43.
A nongraph good coordinate has a<=h: the received root must belong
entirely to H.

Use the exact rank function R from OWN_SYSTEM_RIGIDITY.md. The ambient
own-system dimension is C=6802316684345. There are at most12 bad
coordinates. Writing b_x=ord_x B, one has a_x<=43+2b_x and sum b_x<=12.
Therefore each bad contact is at most67 and

    sum_good R(a) >= K0=C-1-12 R(67)=6801344498272.       (1)

Pad the good profile by zero-contact fictitious coordinates to n terms.
Since e>=13 gives h<=30, all good contacts greater than30 are graph
coordinates. The elementary two-level rank bound gives at least

    ceil((K0-n R(30))/(R(43)-R(30)))
      =ceil(1031235284512/5658289)=182253

such coordinates. This is greater than w+1. Interpolation consequently
gives P=P0(X)+Z P1(X), with P0,P1 in k[X] of degrees at most w. This
affine descent is required before constructing the helper below: it
removes rational-in-Z denominators and controls the total challenge cap.

## 2. The explicit own-system helper

Let a_x be F's actual contact at every coordinate. Set

    b_x = a_x                         at nongraph coordinates,
    b_x = max(a_x-43,0)                at graph coordinates,
    L(X)=product_x (X-x)^b_x,
    Q=(Y-P0(X)-Z P1(X))^43 L(X).

Here b_x denotes a locator exponent, separately from the leading-coefficient
orders used in Section1. The graph factor has contact at least one at
every graph coordinate. Thus Q has contact at least a_x everywhere.
It is nonzero, has R-degree0, joint(Y,R) degree43, and joint(Y,R,Z)
degree43. Its weight is at most43w+deg L.

At good graph coordinates a_x<=43, so they add no locator cost. The total
contribution of every bad coordinate, graph or not, is at most

    sum_bad a_x <= 12*43+2*12=540.                    (2)

If deg L<=12w=1572852, Q belongs to F's entire own interpolation system.
OWN_SYSTEM_RIGIDITY.md proves that system is exactly k F. This is
impossible because deg_R Q=0 whereas deg_R F=12. Therefore a sufficiently
small locator budget excludes the purported universal factor outright.
No candidate agreement set or along-candidate nonvanishing assumption
is used in this helper argument.

## 3. Every multiplicity e>=18 is excluded

Here h<=25, so all nongraph good contacts are at most25. The exact
pointwise inequalities for a=0,...,43 are

    a*1[a<=25] <= (25/21614502)*(R(43)-R(a)).

The accompanying certificate checks all44 states. Summing with(1), and
adding(2), gives

    deg L <= (25/21614502)*(n R(43)-K0)+540
          =5652585643980/3602417.

Since deg L is integral, it is at most1569109, which is3743 below12w.
The explicit helper therefore excludes all e>=18, including linear26
arising from a zero-discriminant quadratic factor repeated13 times.

## 4. Multiplicity17: split on one centered coefficient

For e=17, center at W=Y-P and write H=sum_(j=0)^26 H_j W^j. Its leading
coefficient H_26=B is a unit at every good coordinate, and
deg_X H_25<=w+12.

If H_25 is identically zero, a nongraph good coordinate cannot have
contact26. Indeed its received offset s=f_x+Zg_x-P(x,Z) is nonzero. A
degree26 polynomial with root s of multiplicity26 is B(W-s)^26, whose
W^25 coefficient is -26 B s, nonzero at the benchmark characteristic.
Thus nongraph contact is at most25, and Section3 applies unchanged.

If H_25 is nonzero, every good contact43 coordinate is a graph coordinate
and forces H_25(x,Z)=0. For example, the leading-coefficient contact
extraction gives received-root multiplicity43 in A(x,Y,Z); after centering,
the W^42 coefficient must vanish, and that coefficient is H_25.
Consequently the number N43 of good contact43 coordinates is at most
w+12=131083.

Put dR=R(43)-R(42)=1557205. The exact pointwise inequalities are

    a*1[a<=26]
      <= (R(42)-R(a)+dR*1[a=43])/738980.

For a<=42 the rank deficit is nonnegative; the displayed correction
handles precisely a=43. Summing, using N43<=w+12, and adding540 yields

    deg L <= (n R(42)-K0+(w+12)dR)/738980+540
          =1152463886007/738980.

Its integer upper bound1559533 is13319 below12w. The helper also excludes
this case, completing the e>=17 theorem.

## 5. Two distinct highly repeated graphs cannot occur

Suppose A has two distinct monic linear factors Y-P and Y-Q, each of
multiplicity at least13. At every good coordinate with contact>30,
the received symbol must be a root of both factors: otherwise the remaining
Y-degree is at most30. There are at least182253 such coordinates by
Section1. The polynomial P-Q has X-degree at most w, so it is identically
zero. This contradicts distinctness. This argument does not require the
two graph factors to be defined by different received-support subsets.

## Corollary: the separable quadratic13 branch is excluded outright

QUADRATIC13_CENTERED_COEFFICIENT_ROUTING.md proves that its centroid
Pc is affine in Z and that the centered remainder has the form
H=(Y-Pc)^12 J with deg_Y J<=5. Its good noncentroid coordinates therefore
have contact at most18. Apply the same graph-power helper centered at Pc:
the pointwise h25 inequality in Section3 already covers all these
contacts. The helper belongs to the own system and has R-degree zero,
again a contradiction. Thus the separable quadratic13 universal-factor
branch is actually impossible at the exact stated caps; a selected-list
or no-large-pencil hypothesis is not needed for this stronger conclusion.

## Exact verification and remaining work

The pure-Python linear17_own_system_certificate.py/json checks every finite
rank inequality, the exact locator costs, and the own-system degree caps.
It uses no optimizer and passes the384 MiB/60-second resource guard in
under one second. The independent audit also checks the actual helper's
contact and challenge-degree interface.

The remaining high-linear case is one graph repeated13--16 times.
LINEAR13_16_RESOURCE_LIMIT.md gives an exact profile showing that the
current rank, centered-coefficient budgets, centroid-overlap test, and
graph-power locator family do not exclude those four cases. The profile
is not asserted to glue to global polynomials. Smaller multiplicities,
squarefree leading coefficients, other exact factor shapes, and the
geometric-to-ledger adapter remain separate. No reduction of the complete
7.65% benchmark deficit is claimed here.
