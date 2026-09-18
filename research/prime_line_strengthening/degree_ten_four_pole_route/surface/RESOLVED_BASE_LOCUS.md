# The Paley net has exactly sixteen resolved basepoints

The fourteen prescribed points are not the entire base locus. There are
two further simple points: (X,Y)=(0,0), and (t,Z)=(0,0) in the chart
`t=1/X, Z=Y/X³`. After blowing up these sixteen points once, with the
prescribed multiplicities4/6 at the first fourteen and multiplicity1 at
the last two, the net is basepoint-free.

## Exhaustive modular certificate

`base_locus.py/json` computes two independent eliminants modulo29:
Res_Y(F0,F1) and Res_Y(F0,F2), of degrees373 and379. Both divide exactly by
the prescribed factor of degree364, whose local exponents are16 and36.
The gcd of the two residual eliminants is exactly X. Thus no additional
finite base coordinate is possible away from the fourteen prescribed
coordinates and zero.

At each of those fifteen finite coordinates, the gcd of all three
specialized Y polynomials has only the designated received ordinate as
a root. This prevents removal of the known X factors from concealing
other basepoints in those same fibers. F0 has constant Y-leading
coefficient25, so there are no finite-X, Y-infinite basepoints.

At X infinity, the three restrictions are

    23Z8+10Z, 15Z9+7Z2, 20Z10+2Z3.

Their gcd is Z. The third restriction has nonzero degree-ten coefficient,
so the corner Z=infinity is not a basepoint. At the new affine point,
the linear parts of F0,F2 are19X,25Y; at the new infinity point they are
10Z,t. These independent pairs show that each new basepoint is simple
and has no infinitely-near successor.

At the prescribed points the three tangent-cone sections have no common
projective zero. This is checked at the two orbit representatives, with
the direction at infinity checked as well; equivariance covers all
fourteen points. Thus those points have no infinitely-near basepoints
after their prescribed blowups either. The entire check took0.54seconds
and under8MiB, with full resultants and exact residual divisions saved.

## Exact characteristic-zero transfer

The exact Q(eta) forms reduce to this basis at eta=7 above29. Their
vanishing orders at the fourteen sections hold exactly, by the independent
Hasse-jet certificates. Equivariance forces the two additional points to
be basepoints exactly as well; their independent linear coefficients
remain units. Blow up these sixteen disjoint sections over the DVR,
extending it to split the seventh roots if needed. The three transformed
sections define a closed base locus on this proper relative surface.
Its geometric special fiber is empty by the exhaustive modular check.
Properness therefore makes its geometric generic fiber empty. This
proves the claimed characteristic-zero basepoint-freeness.

## Correct intersection numbers and remaining discriminant guard

On the resolved surface, the moving class L has

    L²=14, K L=14, c2=20, p_a(L)=15.

Consequently `c2(J1 L)=c2+2 K L+3L²=90`. The generic pencil has fourteen
further simple basepoints if transverse, rather than sixteen. Its total
space then has Euler characteristic34, consistent with a genus15 pencil
and total singular-fiber defect90.

The Chern number alone is not an unchecked claim that the reduced plane
discriminant has degree90. One must identify the pushed jet-incidence
cycle, including its multiplicities, and rule out excess-dimensional
jet incidence. Generic nodality gives the familiar interpretation as
ninety nodes in a pencil; it cannot be assumed solely from basepoint-
freeness of an arbitrary three-dimensional subsystem.

Each old cubic strict transform B_i remains a disjoint(-4) curve and
L.B_i=0. It has no net basepoint. A generic member containing it has
residual intersection number4 with it. Four distinct transverse
intersections would account for multiplicity4 of its old-factor line
in the discriminant cycle. Equality, and hence a residual cycle of
degree62 after subtracting seven such lines, still requires the indicated
transversality and incidence checks.
