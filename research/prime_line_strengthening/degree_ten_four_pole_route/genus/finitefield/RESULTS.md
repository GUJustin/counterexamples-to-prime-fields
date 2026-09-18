# Complete F29 net: no geometrically integral genus-zero member

All871 projective members of the Paley norm net over F29 fail a necessary condition for being a geometrically integral genus-zero curve. This is a finite-field result only. It does not exclude characteristic-zero rational members that reduce to extension-field parameter points, reducible curves, or other bad reductions. It also does not classify rational components of reducible members.

## First filter

`count.py` enumerates all900 F29-points of F_3 in four disjoint charts:

* affine (X,Y):841 points;
* finite X, negative section:29 points, equation V^10 F(X,1/V) at V=0;
* base infinity, finite fiber coordinate:29 points, equation t^34 F(1/t,Z/t^3) at t=0;
* the remaining corner:one point, equation t^34 V^10 F(1/t,1/(t^3 V)) at t=V=0.

Smooth curve points contribute one normalization point. At a singular point with squarefree homogeneous tangent cone, the number of rational tangent directions equals the number of rational normalization points, including the vertical direction. Nonordinary points are conservatively left unresolved. No rational normalization point can lie over a nonrational curve point.

A geometrically integral genus-zero curve over F29 has a smooth normalization with exactly30 rational points. The871 members split as follows:

* 828 have already more than30 known normalization points;
* 14 have a completely resolved rational-point count different from30;
* 21 have exact count30;
* 8 have unresolved nonordinary points and do not yet exceed30.

The symmetric member (0,1,0) among the last eight is independently excluded by the Kummer genus bound in `../GENUS_BOUNDS.md`. Under the geometric mu7 action, the other28 members comprise four orbits of size seven.

## Quadratic-field filter

`count2.cpp` repeats the point/branch calculation over F841=F29[v]/(v²-2) on the four orbit representatives. A geometrically integral genus-zero normalization would have842 rational points. The results are:

| Parameters | Count or lower bound | Status |
|---|---:|---|
| (1,1,17) | 844 exact | excluded |
| (1,4,1) | 974 exact | excluded |
| (1,8,15) | at least843 | excluded |
| (1,8,20) | 930 exact | excluded |

For the third representative the only unresolved rational singularity is the multiplicity-four point (1,1). Its tangent cone, with slope T=dY/dX, is

    11*(T-9)^2*(T²-6T-9).

The quadratic discriminant is14, a nonsquare overF29. OverF841 it gives two distinct SIMPLE tangent directions and hence two rational normalization points. Adding these to the841 points counted elsewhere gives the rigorous lower bound843. The doubled tangent direction need not be resolved to obtain the exclusion. The revised C++ implementation counts simple rational directions even at a nonordinary point, while continuing to flag its repeated directions as unresolved.

## Records and limitations

`count.json` records all871 members and their singularity data. `count2.in` fixes the three basis polynomials and the four representatives; `count2.json` contains the quadratic-field results. `resolve.py/json` independently factors the remaining tangent cone and checks irreducibility of that member modulo29. Scripts use exact arithmetic only. Bounded runs took about one second and half a second, respectively; shell-wrapper peak-RSS samples for C++ are not reliable memory measurements.

No rental or general-purpose normalization package was needed. The search found no positive rational member over the ground field F29. Extension-field parameter points and characteristic-zero rational loci remain open.
