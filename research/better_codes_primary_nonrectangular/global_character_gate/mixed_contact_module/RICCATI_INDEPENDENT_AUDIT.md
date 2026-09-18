# Independent common-Riccati audit and polynomial-bank parametrization

Status: PASS for the fixed-word theorem in `WEIGHTED_REES_PADE_TARGET.md`. Characteristic zero or p>2w is essential to the stated constant-cross-ratio argument. No assertion about candidates at different received-line labels is made.

## Contact transfer and collision inequality

For an actual candidate P, substitute Y=P(X), R=P'(X). At a matching node a, the polynomial P(a+t)-P(a)-tP'(a+t) is divisible by t^2, in every characteristic. Thus this is a specialization of the free-E contact substitution, and the restricted helper has order at least m at each matching node. The original weights (1,w,w-1) give restricted degree below mA. Therefore F(X,P,P') vanishes identically.

If the R coefficient is zero, a nonzero polynomial quadratic in Y cannot have three distinct roots in k(X). Otherwise division by the R coefficient gives a common rational Riccati equation. For any four solutions, logarithmic differentiation of their differences makes the derivative of their cross-ratio zero. Its numerator and denominator each have degree at most 2w. In characteristic p>2w, a nonconstant rational function of X^p has rational-map degree at least p; hence this cross-ratio is a true constant. This also works over a nonperfect constant field: the derivative kernel is k(X^p), and the degree argument forces degree zero.

The constant cross-ratio is not 0,1, or infinity for four distinct functions. If two specialize to the same value and two others specialize outside that value, choose cross-ratio ((P1-P3)(P2-P4))/((P1-P4)(P2-P3)). Its denominator is nonzero at this coordinate and its value is 1, a contradiction. Consequently every received-value bucket is of size 0,1,L-1, or L. This remains valid at poles of the Riccati coefficients: the proof uses polynomial values and a cross-ratio with nonvanishing denominator, not local ODE uniqueness.

The stated pair inequality holds for all four allowed bucket sizes, including the harmless negative right side at size zero. Summing it and the pairwise degree-w intersection bound gives L(A-w)<=n. The archived fixed-word scope is necessary.

## Explicit parametrization

Choose any three distinct polynomial solutions and write them as

    P0,  P0+G*u,  P0+G*v,

where G is the monic gcd of their two differences and gcd(u,v)=1. Every further solution in a degree-at-most-w bank, under the same characteristic assumption, has the form

    P_t = P0 + G*u*v / ((1-t)*u+t*v),       t in k,

together with P_infinity=P0. Parameters for which the denominator is the zero polynomial are excluded. The parameters t=0,1 give the two chosen nonbase solutions. This follows directly by solving the constant cross-ratio identity; coefficients may be taken in the common constant field or its algebraic closure as appropriate.

For t different from 0 and 1, the denominator D_t is coprime to both u and v. Therefore P_t is polynomial if and only if D_t divides G in k[X]. Distinct finite parameters give pairwise coprime denominators, because a common divisor would divide u and v. Constant nonzero denominators impose no divisibility restriction; if u,v are nonconstant there is at most one such parameter. If both are constants, the family is simply the polynomial affine pencil P0+cG. For a prescribed degree cap one must additionally retain only parameters whose resulting polynomial has that degree bound.

This is also a converse parametrization: any three distinct rational functions define a moving fractional-linear coordinate on the dependent variable. Differentiating its constant parameter yields a rational Riccati equation, satisfied by the full displayed family. Thus the divisibility condition describes precisely its polynomial members. In positive characteristic it parametrizes the bounded-degree bank under p>2w; unrestricted high-degree solutions may have nonconstant parameters in k(X^p) and are not covered by the assertion.

## The rational eight, ten, and eleven sources escape this subclass

The original rational eight-cubic source has, for example, old coordinate index 1 with received-value bucket exactly {6,7}; six other candidates lie outside that bucket. A common Riccati equation for these eight distinct functions would force a size-two bucket to have size at least seven, impossible. Equivalently, use candidates 6,7 and any two of the other six in the cross-ratio argument above.

The complete ten- and eleven-cubic sources retain these same eight polynomials and this coordinate/value, so they likewise admit no common rational Riccati equation. This conclusion is independent of the contact helper's weight and does not require enumeration or a genericity assumption. The exact rational incidence table is already certified in `research/relaxed_eight_cubic_route/rational_seed.json`; candidate indices refer to that table.

This is an exclusion of the common-Riccati subclass, not an obstruction to the successful finite lists themselves or to higher Y/R contact helpers.
