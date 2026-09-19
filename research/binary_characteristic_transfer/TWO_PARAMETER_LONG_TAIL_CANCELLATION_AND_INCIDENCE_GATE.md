# Two-parameter long-tail cancellation: exact identity and closure

September 18, 2026. **Closed for a growing bank at fixed length/degree
ratios. No seed scan was run.** The cancellation below is valid in every
odd characteristic and has two independent parameters, but a cubic
incidence count bounds its entire split-locator bank by a constant when
`n/K` and the agreement-loss ratio are fixed.

## Exact compiler

Work over a field `F` of odd characteristic. Fix an integer `K>=1`, a
nonzero polynomial `W(X)` of degree `0<=D<K`, and `theta in F`. Put

```
u = X^K,
F0 = u^8 + theta*u^4,
G = u^3 W,
J = K+3D+1,          A = 3K+D,          T = 4K.
```

The code consists of polynomials of degree `<J` evaluated on a set
`Delta` of `n>=T` distinct field elements. For arbitrary `a!=0,b in F`,
define

```
C_ab = (a²+theta)/2 − (b²/(2a))W²,
L_ab = u^4 + a*u² + b*uW + C_ab,
lambda_ab = −2ab,
h_ab = −(b³/a)uW³ + (b⁴/(4a²))W⁴ − (a²+theta)²/4.
```

Then the following polynomial identity is exact:

```
F0 + lambda_ab*G − h_ab
 = L_ab * (u^4 − a*u² − b*uW + a²+theta−C_ab).       (1)
```

For verification, first multiply
`(u^4+a*u²+b*uW+C)(u^4−a*u²−b*uW+a²+theta−C)`.
The `u²` remainder vanishes because
`b²W²+2aC=a³+theta*a`; the remaining terms are precisely (1).
Equivalently,

```
F0−2ab*u³W mod L_ab
 = −(b³/a)uW³+(b⁴/(4a²))W⁴−(a²+theta)²/4.
```

Since `D<K`, the locator is monic of degree `T=4K`, while
`deg h_ab <= K+3D=J−1`. Thus every `L_ab` that splits into `T` distinct
roots all lying in `Delta` gives a valid affine-line witness at agreement
at least `T`. No division by `X` or zero-root exception is involved.
This does not assert that every parameter splits, or that the witness
has no additional matches.

The direction has degree `A=3K+D>J−1`; consequently

```
agr(G, RS_J(Delta)) <= A,
CA(F0,G) <= A < T.
```

Only upper bounds are asserted here. In particular, farness of the first
source and an exact common-agreement profile have not been established.

## Cubic incidence bound

Let `mathcal B` be any set of distinct parameter pairs `(a,b)`, `a!=0`,
whose locators split as required above. Then

```
|mathcal B| <= 9 n(n−A) / [T(T−A)].                 (2)
```

This bounds parameter pairs, and hence distinct affine labels as well;
no label-injectivity assumption is used.

**Proof.** For each coordinate `x in Delta`, write `u_x=x^K` and
`w_x=W(x)`. Its incident parameter pairs lie on the nonzero cubic

```
P_x(a,b) = 2a L_ab(x)
 = a³+2u_x²a²+(2u_x⁴+theta)a+2u_x w_x ab−w_x²b².
```

Factor these cubics over an algebraic closure and discard the component
`a=0`, which contains no admissible parameter. No remaining component
has constant `ab`. Indeed, restricting `ab=s` and multiplying by `a²`
gives the monic polynomial

```
a⁵+2u_x²a⁴+(2u_x⁴+theta)a³+2s u_x w_x a²−s²w_x².
```

It is not identically zero. This excludes every hyperbola `ab=s!=0`,
and also the remaining component `b=0` when `s=0`.

For a usable irreducible component `C`, let `m_C` be the number of
coordinates whose cubic contains `C`, and let `N_C` be the number of
bank parameter points lying on `C`. We have `m_C<=A`. To see this,
choose two algebraic-closure points on `C` with `a!=0` and different
values of `lambda=−2ab`. Identity (1) gives two strict code witnesses
on all `m_C` coordinates. Subtracting their explanations gives a
polynomial of degree `<J` agreeing there with `G`. Its difference from
`G` is a nonzero degree-`A` polynomial, so it has at most `A` roots.
The argument over the algebraic closure is sufficient for this root
bound and needs no rational-point assumption on `C`.

If a coordinate cubic does not contain `C`, Bezout bounds its number of
intersection points with `C` by `3 deg C`. Each bank point on `C` must
have at least `T−m_C` matches outside the coordinates containing `C`.
Therefore

```
N_C(T−m_C) <= 3 deg(C)(n−m_C).
```

Every bank-coordinate incidence is counted at least once by
`sum_C m_C N_C`, even at intersections of components, while
`sum_C m_C deg C <= 3n`. Since `m_C<=A<T<=n`,

```
T |mathcal B|
 <= sum_C m_C N_C
 <= 3 (n−A)/(T−A) * sum_C m_C deg C
 <= 9n(n−A)/(T−A).
```

This proves (2), including repeated factors or singular cubics.

## Consequence for the proposed transfer

For `n=Theta(K)` and `D/K` bounded away from one, (2) is `O(1)`.
For example, the asymptotic ledger `D=0.3K,n=9K` gives an upper bound
below `165` parameter pairs, regardless of how the domain or `W` is
chosen. At the earlier ledger `D=K/2,n=6.5K`, an even simpler bound
applies: two locators differ in degree at most `2K`, so their `4K`-root
sets intersect in at most `2K`; the ordinary pair-count bound gives at
most four locators.

Thus the longer tail does provide a genuine two-parameter algebraic
cancellation, but its coordinate curves still have bounded degree.
It cannot produce a superlinear label bank with constant relative loss
in the stated regime. Any further transfer must change the actual
parameter variety or allow its coordinate-incidence complexity to grow;
merely reparameterizing `(a,b)` does not change this bound.
