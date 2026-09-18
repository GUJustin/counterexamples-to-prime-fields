# The rigid nine-word branch is obstructed, but an incidence exchange lifts

## Exact reduction of the unrestricted eightfold-node pattern

Suppose eight quartics R_i share the received value v at a distinguished node b, while a ninth quartic R_8 does not agree there. On the open chart where every other node x_j differs from b, define

P_i=(R_i-v)/(X-b), w_j'=(w_j-v)/(x_j-b), N=R_8-v.

Then every P_i is cubic and the new matches are exactly N(x_j)=(x_j-b)w_j'. The condition R_8(b)!=v is precisely N(b)!=0, so the rational candidate N/(X-b) is proper. Conversely R_i=v+(X-b)P_i, R_8=v+N and w_j=v+(x_j-b)w_j' reconstruct every unrestricted configuration in this chart.

Thus the eight common-node equations give an exact chart isomorphism from the unrestricted incidence scheme to the structured scheme times the common-value coordinate v. This is not a restricted deformation ansatz. At the displayed F17 point all relevant differences and the properness value N(0)=2 are units.

## Why the original mod289 obstruction allows no ramified escape

The structured original point has64 equations in70variables and Jacobian rank62. Its old cubic source has56 equations in64variables, rank56. Its eight-dimensional tangent space is exactly the gauge orbit: four common-cubic additions, common scaling, and three projective base changes with the degree-three section action. One can use SL2 together with scaling to avoid any odd-degree global PGL2 linearization issue. These actions preserve proper degree-(4,1) rational sections; near the identity the denominator can still be normalized to X-b.

The determinant of the gauge action on the eight source coordinates complementary to the known unit56minor is11 mod17; see ninth_rigidity_minors.py/json. Hence any source lift over any complete extension valuation ring can be formally normalized to fix those eight coordinates. Hensel uniqueness then identifies its source with the canonical unramified Z17 lift.

For this fixed source, the first six rational-match equations are linear in b,N_0,...,N_4 and have determinant1 mod17. They determine a unique candidate over Z17, also after arbitrary ramified extension. The two remaining equations are incompatible modulo289: ninth_mod289.json supplies left-null certificates with defect pairings11 and7. Therefore there is no mixed-characteristic lift of the original64-equation point, even after ramification. By the chart isomorphism, the same holds for the corresponding unrestricted72-equation nine-quartic point.

This is local at the specified residue configuration. It does not exclude every nine-quartic bank, every pole, or every support pattern.

## Exchange two incidences instead

Take the original finite seed and the numerator

N=2+15X+8X²+5X³+13X⁴.

It matches X times the cubic received word at old coordinate indices0,1,4,5,6,7,8,11. Remove structured row0 (old cubic0 at x=3) and row56 (the new numerator match at x=1). The remaining62 by70 Jacobian has full row rank. Its original62-column minor is8 mod17, independently reconstructed with integer Bareiss elimination in verify_nine_exchange.py/json. Equivalently, the two corresponding columns of the original left-null basis have determinant13.

Consequently the remaining62 equations lift smoothly to a number field embedded in Q17 after fixing the eight complementary variables. This lift is not required to retain either deleted equality.

In fact neither equality survives. Let d=F(z_0)/17 mod17 be the original64-equation defect. The two saved left-null vectors restrict to deleted rows0,56 as (0,14) and (10,15), and pair with d as11 and7. In any first-order lift satisfying the other62 equations, the deleted residuals r_0,r_56 obey

14r_56=11, 10r_0+15r_56=7 (mod17),

so r_0=13 and r_56=2. Both are nonzero. Thus the two deleted equalities genuinely fail in characteristic zero.

Now clear the moving pole: use the eight quartics (X-b)P_i and the ninth N, and append b with received value0. Seven old candidates have eight matches, but old candidate0 and N each have only seven retained matches.

Over F17,

N-X P_0=11(X-5)(X-6)(X²+10).

The quadratic X²+10 is irreducible and separable. Adjoin theta with theta²=7 and append its simple lifted root of N-(X-b)P_0. It remains off all old nodes and off b. Set its received value to N(theta). This adds one agreement to both deficient candidates. The derivative at the finite theta is6+15theta, a unit. Therefore this final root extension is etale and all eighteen nodes remain distinct.

The finite fresh word is15+16theta; only old label0 and the new candidate match there. All nine characteristic-zero quartics now have exactly eight matches. The known finite extra incidences were precisely the two deleted equations, and their nonzero order17 residuals remove them; every other nonmatch was already a residue unit.

## Completeness

The finite F289 specialization has eighteen nodes, with actual agreement counts9,8,8,8,8,8,8,8,9. nine_complete_decode.py/json exhausts all8568 five-point supports, obtaining5628 distinct quartic interpolants. Exactly these nine known quartics have at least eight matches, and no polynomial has more than nine. This also classifies threshold polynomials over the algebraic closure: any such polynomial is determined by five F289 node/value pairs, hence has F289 coefficients.

Any characteristic-zero quartic with at least eight agreements is integral at the chosen place, by five-point interpolation with unit denominators. Its reduction is one of the nine finite candidates, with at most nine matching coordinates. The proposed competitor's at least eight matches and the corresponding known lift's eight selected matches lie inside that residue support, so their intersection has size at least8+8-9=7. Two degree-four polynomials agreeing at seven distinct nodes are equal. Thus the number-field source has maximum agreement eight and complete nearest list exactly nine.

Removing finitely many bad primes preserves this conclusion over arbitrarily large split prime fields, using the finitely many five-point support interpolants to exclude unwanted matches.

## First-order parameters and limitation

The source parameters are n18,D4,k5,A8,L9. They are not themselves in the desired first-order regime. Pull back by a separable degree12 polynomial with all selected fibers split and disjoint. Then

n216,k49,A96,L>=9,
F_(49/216)(4/9)=73/34992>0,
(11-49/216)²-117=-43823/46656<0.

This gives at least nine threshold candidates above the applicable first-order curve. Completeness of the degree12 pullback is not asserted. Neither this single exchange nor polynomial pullback proves a repeatable list-increasing operation or an unbounded list-size family.
