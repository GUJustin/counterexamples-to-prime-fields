# Finite prime-field exponent coefficients

Four half-rate interval-domain Reed--Solomon examples strengthen the
finite comparisons with L <= c1 * 2^(c2 H2(rho)/eta). At c1=1 they
force, respectively:

| Prime | n | k | surplus m | strict log2 L lower bound | forced c2 greater than |
|---|---:|---:|---:|---:|---:|
| 2^31-1 | 154 | 77 | 5 | 61.74656 | 2.00475 |
| 2^61-1 | 548 | 274 | 9 | 242.16447 | 3.97715 |
| 2^127-1 | 2158 | 1079 | 17 | 995.98234 | 7.84601 |
| 2^521-1 | 29176 | 14588 | 56 | 14233.01899 | 27.31865 |

All four radii are strictly below the characteristic-based Elias radius.
These are existence certificates on integer intervals, not examples on
a specified FFT or circle domain. No algorithm to enumerate the enormous
lists is claimed. The discovery scan is not an optimality proof.

## Proof and exact replay

Apply the manuscript's Gram smoothed-ellipsoid bound with m canceled
moments and t=k+m. The variance for the jth Gram moment is

    Vj = t(n-t)/(n-1) * product_(i=1)^j (n^2-i^2)
         / ((2j+1) binom(2j,j)^2 (j!)^2).

The list size is at least ceil(binom(n,t)/D), where

    D = kappa_m (m+2)^(m/2) product_j sqrt(Vj+1/12).

Use pi < 355/113 and a rational upper square-root approximation to
obtain an explicit upper bound on D. The code reuses the exact bound
implementation in ../logarithmic_length_lines/verify.py. It checks

    p^m * t^t * (n-t)^(n-t) > n^n,

which implies the strict sufficient entropy condition for Elias.
Lucas--Lehmer verifies the four Mersenne primes. For decimal comparisons,
the concentration ratio is first normalized into [1,2) and enclosed in
an outward interval with denominator 2^96. Rational arctanh series and
their geometric tail bounds then enclose its logarithm. The verifier
checks that both endpoints imply the same reported five-decimal floor.

At rate one-half, H2(rho)=1, so c2 >= (m/n) log2 L when c1=1.
For general c1 the necessary coefficient is reduced by
(m/n) log2 c1. The last example has m/n=1/521 exactly.

Run `python3 research/prime_exponent_coefficients/verify.py` from the
repository root, sequentially under the 384 MiB watchdog. Standard
library only. `verification.json` records the bounds and hashes of the
large exact integers without printing thousands of decimal digits.

## Field-dependent asymptotic coefficients

The manuscript's all-large-prime list corollary already proves, with
b=log2 p, log2 L >= (1/2-o(1)) b^2/log2 b and eta=(H+o(1))/b.
Consequently even allowing c1(p)<=p^K for fixed K requires

    c2(p) >= (1/2-o(1)) log2(p)/log2(log2(p)).

This is an explicit consequence of the existing corollary, not an
independent construction. The gap still shrinks with p.
