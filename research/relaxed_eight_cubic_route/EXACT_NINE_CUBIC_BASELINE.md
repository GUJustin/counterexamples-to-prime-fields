# Complete nine-cubic rational baseline

Independent verification uses stdlib Fraction arithmetic and Newton divided differences, not the source generator's formulas. The stable source chart is U=1/(X−3).

`rational_nine.py/json` verifies the projective-to-affine coefficient transform, all56 source incidences, and all1820 four-node interpolation subsets. The16-node source has exactly8 nearest cubics with7 matches; its1516 distinct four-point interpolants have agreement histogram {4:1500,5:8,7:8}.

The fresh cubic is

    Q(U)=−9U−34U²−32U³.

It matches source indices0,1,3,8,10. Append U=1,2 with received values−75,−410. Both new nodes avoid every other source four-point interpolant's intersections with Q. Exact exhaustive enumeration of3060 four-node subsets on the18-node word gives2726 distinct interpolants, with histogram

    {4:2710,5:7,7:9}.

Thus maximum agreement is exactly7 and the complete nearest list consists of the eight archived cubics and Q. There are no six-match cubics. All rational nodes, word values, and coefficients are in `rational_nine.json`.

`rational_nine_modular.py/json` independently performs modular Vandermonde elimination: reduction modulo103 has18 distinct nodes, nine distinct cubics, maximum agreement7, and exactly9 nearest cubics. Its histogram is {4:2520,5:45,7:9}. This supplies a compact explicit prime-field baseline as well as a good reduction certificate. Completeness over Q is already established independently by exact enumeration.

## First-order pullback

A degree-e simple-fiber pullback carries9 polynomials of degree3e on18e nodes with7e agreements. Dimension is3e+1. The smallest integer e entering the audited first-order region is5.

For e=1,2,3 the rate lies on the high-rate branch; e=2,3 give boundary-polynomial values−1099/11664 and−341/8748, respectively, and e=1 also fails. For e=4,5 the rate is below11−3sqrt13. Let a=7/18, rho=(3e+1)/(18e), t²=rho/2, and K=t⁴+3at²−a³. The low-rate boundary is a1=t(1+u), where u>0 satisfies u²(u+3)=t. Here a>t and K>0, so a>a1 is equivalent to

    4t⁶−K²>0.

For e=4 this rational expression is−1557169/34828517376; for e=5 it is475871/21257640000>0. Thus e=5 gives

    n=90, degree15, k=16, rate8/45, agreement7/18,

with first-order agreement margin approximately0.00113940394.

One explicit algebraic pullback is U=T⁵+3. None of the18 rational nodes equals3; therefore all90 roots are simple and distinct in a finite splitting number field. The nine compositions are distinct and retain35 matches each. After specialization at infinitely many completely split good primes, the same prime-field parameters hold. This asserts at least9 carried candidates, not completeness or maximum agreement of the pulled-back word.

This remains a finite baseline, not a growing-list construction or a better.codes improvement.
