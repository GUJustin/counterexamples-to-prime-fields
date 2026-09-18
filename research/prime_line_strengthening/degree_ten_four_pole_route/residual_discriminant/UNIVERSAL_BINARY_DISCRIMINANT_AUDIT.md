# Binary discriminant removes the boundary guards

Independent audit: the parent's proposed homogeneous replacement is valid
for a geometrically integral member of the actual class
`10 C0+34 f` on F3, in characteristic zero or 29. It supplies a necessary
condition for rationality on the entire parameter plane, including the
exceptional curves omitted by the earlier affine-chart proposal.

## Local identity at every fiber

An integral nonvertical member maps finitely to the base with degree ten.
Its binary defining form has nonzero reduction at every base point; a
zero binary reduction would give a vertical component. Work over the
algebraic closure and the local DVR of a base point. Choose a constant
PGL2 change of the fiber coordinate whose point at infinity avoids the
finitely many reduction roots. Its determinant is a unit, and the new
leading coefficient is a unit. Dividing by that unit gives a monic order.
The discriminant-index identity then gives

    ord(Delta) = local different + 2 * sum(local delta invariants).

The coordinate change and unit division do not change the valuation of
the binary discriminant. This proves the identity also at branches that
were Y-infinite in the original chart, repeated pole images, and singular
or ramified fibers over base infinity. No squarefreeness of the original
leading coefficient, or coprimality with its next coefficient, is needed.

In characteristic29 the degree-ten map is separable and tame: an
inseparable degree would be divisible by29, and every ramification index
is at most ten. The same discriminant-index identity applies.

## Global residual index

The binary discriminant is a section of O(342) on the base. This follows
either from the F3 transition, or from
`3*10*9 + 2*4*9 = 342`. Adjunction gives arithmetic genus162.
The seven multiplicity-four and seven multiplicity-six prescribed plane
points force delta at least

    7*binom(4,2)+7*binom(6,2)=147.

The fixed discriminant factor T has degree294. Its divisibility follows
at each point from the local identity and the standard plane-multiplicity
delta bound, or from the dense ordinary locus followed by polynomial
identity. The homogeneous residual discriminant D_h is a binary form of
degree48.

For rational normalization, total different is18 and total delta is162.
After subtracting the147 forced delta units, exactly15 residual delta
units remain. At a base point with residual delta k and different r,
the residual discriminant multiplicity is 2k+r. If k>0 then
`2k+r-1>=k`. Consequently the sum of multiplicities minus one over
distinct roots of D_h is at least15.

In characteristic zero this is exactly

    deg gcd(D(X), D'(X)) + max(47-deg D(X),0) >= 15,

where D(X)=D_h(X,1). The second term includes base infinity. The displayed
inequality is still necessary in characteristic29: differentiating a
multiplicity divisible by29 only increases the finite gcd contribution.
Equivalently, a convenient necessary condition in both characteristics is

    deg gcd(partial_X D_h, partial_V D_h) >= 15.

Here 48 is invertible in characteristic29, so Euler's identity ensures
that every common factor of the two partials also divides D_h. The binary
partial condition can be weaker at multiplicities divisible by29, but
never excludes a rational member for that reason. An identically zero
discriminant is not evidence of rationality: it is incompatible with an
integral separable degree-ten member and must be screened separately.

## Actual class and parameter chart

For the recorded Paley basis the weighted-infinity restrictions are

    F0: 23 Z^8+10 Z,
    F1: 15 Z^9+7 Z^2,
    F2: 20 Z^10+2 Z^3.

Their supports are disjoint. Thus every nonzero linear combination has
actual weighted class c=4; none acquires an artificial whole infinity
fiber through a drop in this class. This directly verifies the class
hypothesis for the whole modular net. The degree-ten Y leading projection
is also injective, as separately certified in the net rank computation.

Each discriminant coefficient is homogeneous of parameter degree18.
Therefore the existing reconstruction on a=1 determines the full
parameter plane: homogenize each saved coefficient to degree18 in
(a,b,c), and homogenize the residual in (X,V) to degree48. This recovers
the a=0 chart exactly, rather than treating it as absent data.

## What the discarded guards actually meant

The conditions a=0, c=0, Disc(B)=0, Res(B,C9)=0, and repeated weighted
infinity roots are not forbidden by proper four-pole augmentation and
separability only at the fourteen selected fibers. They can express
repeated poles, coincident pole images, or ramification/singularities at
unselected fibers. They must not be removed from a complete rationality
calculation. The homogeneous condition above includes them automatically.

By contrast B(x_selected)=0 is incompatible with the proposed realization:
the entire selected fiber lies in the evaluation domain and off the pole
divisor, so no branch there can have infinite received ordinate. Likewise
additional branches agreeing with the selected received ordinate would
exceed the prescribed6/4 counts; the old-candidate intersection sum is
already saturated at238=7*34. These are legitimate realization screens,
but neither is needed to justify the universal discriminant condition.

All finite-field claims above concern the recorded modular net. A
characteristic-zero exclusion still requires an appropriate integral
certificate and specialization argument; an empty modular parameter locus
alone does not provide that transfer.
