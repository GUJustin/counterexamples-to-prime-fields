# Full quadratic banks: a precise cone target

For P_i(X)=a_iX²+b_iX+c_i, regard [a_i:b_i:c_i:1] as coefficient points in P³. Evaluation planes have dual coordinates [α:β:γ:δ]=[x²:x:1:−f(x)], and therefore lie on the rank-three quadric cone

    β²=αγ.

A positive projective realization must admit such a dual cone after change of coefficient chart, avoid its vertex and degenerate normal chart, and use distinct cone rulings so that no two selected planes prescribe different values at the same evaluation x. Generic coplanarity is insufficient.

## What incidence theory currently supplies

Quadratic graphs have three degrees of freedom and pair intersection multiplicity at most two. For real coefficients and real evaluation points the Pach–Sharir bound gives J=O(n₀^(3/5)L^(4/5)+n₀+L). After absorbing linear terms when average agreement S=J/L and richness R=J/n₀ are large, it yields n₀=Ω(sqrt(R) S²). Thus growing richness is impossible at Johnson-scale n₀=O(A²) even for full real quadratic banks. See the primary [Pach–Sharir paper](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/on-the-number-of-incidences-between-points-and-curves/D82C6E430EE5402A3FE18C724A0C14B1).

For complex coefficients, [Sheffer–Szabó–Zahl, Theorem 1.3](https://arxiv.org/html/1502.07003v4) gives J=O_ε(n₀^(3/5+ε)L^(4/5)+n₀+L), without transversality assumptions. Algebraically this implies R S⁴=O_ε(n₀^(2+5ε)). At n₀=Θ(A²), all fixed-power richness R≥n₀^δ is excluded, by choosing ε<δ/5. This bound alone leaves logarithmic or other subpolynomial growing richness unresolved. These are characteristic-zero/realization statements, not finite-field incidence bounds.

## Elliptic quartics and the natural quadric construction

An elliptic normal quartic in coefficient P³ has at most four points in a plane. It could improve a constant-richness core, but cannot itself give growing richness. Four torsion points with the correct group sum are coplanar; their planes need additionally to satisfy a rank-three dual quadratic equation.

One standard construction uses an elliptic quartic on a fixed smooth quadric Q. Each tangent plane to Q cuts it into one line from each ruling; intersecting these with the elliptic curve gives two pairs, hence four points. The tangent planes form the smooth rank-four dual quadric Q*. The evaluation cone is rank three, so cannot equal Q*. Its restriction to Q* is a nonzero bidegree-(2,2) equation on the two ruling parameters.

If U and V are the ruling fibers whose two distinct elliptic intersection points lie in a bank of L points, each has at most L/2 members. A nonzero bidegree-(2,2) polynomial has at most 2|U|+2|V| zeros on U×V: at most two exceptional first coordinates make it identically zero in the second coordinate, and all other fibers have at most two zeros. Thus this fixed-quadric mechanism supplies only O(L) admissible planes, not the Θ(L²) needed for agreement Θ(L). Varying the containing quadric is not excluded by this argument.

## Bounded necessary identity gate, completed

The concrete possible-positive target is a torsion-compatible two-parameter family

    R=mP+nQ+τ,  S=−P−Q−R

on E:y²=x³−x, embedded as [1:x:y:x²]. Its coplanar-plane image would be useful if it lies on a rank-three dual quadric. This is a ten-coefficient linear identity question before any torsion enumeration.

`elliptic_quadruple_cone_gate.py/json` tests τ=O and all m,n∈[−3,3], using 100 distinct valid planes per nondegenerate branch at primes 1009 and 1013. Both primes give the same result:

* 41 branches have quadratic evaluation rank ten, so no sampled dual quadratic relation.
* Four branches force duplicate points: (m,n)=(-2,-1),(-1,-2),(0,1),(1,0).
* Four branches have image in a fixed dual plane and quadratic rank six. For (-1,-1),(0,0), the coefficient of x² vanishes because one point is O. For (-1,0),(0,-1), the coefficient of y vanishes because the pairs are P,−P and Q,−Q. Every quadratic relation is divisible by the fixed linear equation and hence has matrix rank at most two.

There is no rank-three positive lead in this bounded target. An independent integer Bareiss verifier (`elliptic_quadruple_cone_verify.py`, `elliptic_quadruple_cone_verified.json`) replays all 82 original 10×10 unit minors, the eight six-dimensional plane-image minors, all point-on-curve checks, and coplanarity witnesses. Runtime was 1.38 seconds for generation and 0.026 seconds for replay.

This does not classify arbitrary elliptic quartic embeddings, nonzero τ, other curves, or unrelated full quadratic banks. No further scan or rental is justified solely by these negative cases.
