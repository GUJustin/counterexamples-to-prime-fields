# Finite necessary locus and a sevenfold quotient

This is a scoped consequence of the corrected complete projective-line test over F29, not a claim that the remaining locus is empty or contains a rational curve.

Let Z in P² be the closed scheme defined by the 80-minors of the 94×94 homogeneous Sylvester matrix of the two degree47 base partials of D48. Parameter entries are homogeneous of degree18. Thus its geometric points are precisely the parameters with binary-gradient gcd degree at least15, including D=0.

## Projective finiteness

The line c=a has no geometric point in Z according to the exact subresultant computation and its algebraic-residue-field checks. Its endpoint [0:1:0] must be evaluated by proper exponent lookup: its residual degree is45, finite derivative gcd degree2, and infinity contribution2, giving total4. The initial zero-discriminant endpoint report was a dictionary-key lookup error, independently detected by direct FLINT resultant and reconstruction checks.

Every positive-dimensional closed projective subset of P² meets every line. Therefore Z is zero-dimensional or empty. This argument requires the complete projective line, including all leading-degree drops and its endpoint. It is not valid for a sampled affine line. It does not assert reducedness.

The same conclusion transfers to the characteristic-zero kernel family over the chosen integral model: the determinantal locus is projective over the localization at the good prime, so a positive-dimensional generic component would have a positive-dimensional special fiber. This requires the already proved kernel base-change and integral discriminant construction, not merely unrelated modular interpolation data.

Each defining minor has degree80*18=1440. As the common projective locus is finite, two generic linear combinations of the minors have no common curve. Bezout therefore bounds the number of distinct geometric candidate points by1440²=2,073,600. This is deliberately coarse; it is an upper bound, not an estimate of practical elimination size.

The affine chart c-a=1 contains all Z. Restrict the homogeneous minors there; the resulting affine ideal has finite quotient. Thus a finite multiplication-matrix/rational-univariate-representation computation is a complete target, with no missing infinity points. Computing a few principal subresultants first can produce a larger finite candidate set, but must retain leading-degree-drop strata and confirm the homogeneous gradient criterion afterward. A positive-dimensional intermediate ideal is not evidence that Z has a curve.

## Exact mu7 quotient on a*b nonzero

In chart a=1 write parameters (b,c). The audited sparsity identity is

    k-2i-4j = 2 mod7

for a term d_ijk X^k b^i c^j of D. Consequently define

    U=c/b², V=b⁷, X=b³ Z.

Then, exactly,

    D(b³ Z; b, U b²) = b⁶ E(Z,U,b⁷).

The sparse polynomial E is recorded by invariant_quotient.py/json. It has1278 terms and degrees Z48,U18,V24. Each coefficient is obtained by the integral exponent map

    (k,i,j) -> (k,j,(3k+i+2j-6)/7).

All resulting V exponents are nonnegative. The script independently reverses this map term by term against the reconstructed D. On V nonzero, scalar multiplication and the invertible base-coordinate change preserve the homogeneous gradient-gcd degree. Hence solving the corresponding condition for E and lifting b⁷=V gives exactly the candidates on this chart.

This is the quotient by (b,c)->(zeta² b,zeta⁴ c). It reduces sevenfold orbits, but raises one parameter degree to24; no speedup is promised. The a=0 and b=0 lines must be treated separately. All three coordinate-axis points have gradient gcd degree4 (basis residual degrees44,45,46 and finite gcd degrees1,2,3 respectively), so none is a candidate. Every remaining candidate orbit has size7.

## Old-graph lines and positive search

The seven old-graph divisibility lines are known reducible strata. For seeking a geometrically integral positive member, one may first solve away from their product, then recover and inspect the omitted finite set separately. They must not be discarded when proving emptiness of an integral characteristic-zero locus: a characteristic-zero integral member can specialize to a reducible member on one of these lines.

A point surviving the discriminant condition is only a candidate. It still requires geometric integrality, normalization genus zero, and the required distinct matching branches/pole divisors. Conversely, failure of those final guards at a modular point does not exclude a characteristic-zero deformation without further specialization arguments.
