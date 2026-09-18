# Complete F289 search by nine-anchor pencils

Question: on the48 nodes of T³=x above the16-node original F17 cubic source, can a non-descended polynomial of degree at most9 have17 matches? Here all48 nodes lie in F289=F17(theta), theta²=7. Word values remain in F17. This search permits all F289 coefficients, not only F17 coefficients.

## Complete reduction of the interpolation workload

Partition the16 base fibers into two groups of8; each half has24 cover nodes. Any set of17 matches contains at least9 nodes in one half. For every9-subset S of either half, interpolate its unique degree-at-most8 polynomial Q0 and form its monic degree9 locator L_S. Every degree-at-most9 polynomial matching S is uniquely

    Q_t=Q0+t L_S, t in F289.

For each of the39 remaining nodes x, L_S(x) is nonzero and exactly one scalar

    t_x=(w(x)-Q0(x))/L_S(x)

makes Q_t match there. Counting these scalars therefore finds every Q_t with17 matches: a scalar bucket must contain at least8 nodes. No enumeration of289 pencil parameters is needed, and no ten-node interpolation subsets are enumerated.

The deck action T->zeta*T, zeta=59=8+3theta, and Frobenius T->T^17 preserve both halves and the word. They generate S3, acting on each fiber's root labels by r->a*r+b mod3, a=1,2. Frobenius also conjugates candidate coefficients, so this is a valid semilinear search symmetry over F289. Taking the minimum24-bit anchor mask under these six permutations preserves existence of a candidate; it does not assume candidates are F17-rational.

Burnside gives the exact number of nine-anchor orbits in each half. Identity fixes binom(24,9)=1,307,504 subsets; each of two3-cycles fixes binom(8,3)=56; each of three involutions fixes

    sum_(a+2b=9) binom(8,a)binom(8,b)=5328.

Thus the two halves require exactly

    2*(1307504+2*56+3*5328)/6=441200

pencils, instead of binom(48,10)=6,540,715,896 determining ten-subsets. This is a general two-half pencil strategy whenever the agreement threshold forces D anchors in one half for degree D.

## Result and safeguards

The complete C++ run visits all2,615,008 raw nine-subsets and exactly441,200 canonical pencils. It finds ZERO non-descended candidates with17 or more matches, in0.89seconds under the local384MiB/60-second guard. Field multiplication/inversion uses exact tables for theta²=7; all nonzero inverses, all cubic fibers, and every reported candidate's agreement count are asserted. There are3348 descended-pencil encounters, serving as a positive sanity check. These are encounters, not a count of distinct descended candidates.

No claim is made that only the original eight descended candidates pass17 matches: a residue cubic with6 matches would pull back to18. The result is specifically absence of non-descended candidates. It excludes F289 coefficients on this fixed cover, not algebraic-closure coefficients or all characteristic-zero covers. A separate implementation has not yet replayed all pencils.

Files: `input.hpp`, `search.cpp`, `pilot.json`, `full.json`, `resources.json`. No rental was used.
