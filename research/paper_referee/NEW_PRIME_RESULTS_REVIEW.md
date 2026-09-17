# Self-review of the new prime-field results

September 16 evening continuation. This is a direct proof review, not
independent peer review. The current sources, rather than the exploratory
notes, were checked.

## Logarithmic-length lines

For target dimension k and surplus r, the source dimension is k+1 and
the canceled moment count is r-1. Thus the source polynomials have
degree at most k, and division by X-tau gives degree strictly less than
k, as required. Their supports have exactly t=k+r roots on the interval.
The moment-range exponent is sum_(j=1)^(r-1)(j+1)=(r-1)(r+2)/2.
With the chosen n, the bank lower bound is Omega(p log p), so N/p tends
to infinity. This is stronger than needed for the limiting label count.

For each pair of distinct source polynomials, shared support roots
consume part of its at-most-k root budget. Summing yields the displayed
pair budget and, after Cauchy--Schwarz, exactly

    N(p-n) / [(p-n)+N(k-t^2/n)+(t-k)].

The denominator's dominant term is N*rho(1-rho)*n. This gives the stated
constant H2(rho)/(rho(1-rho)) multiplying p/log2 p. All signs and the
source/target dimension shift agree. The direction 1/(X-tau) alone
precludes correlated agreement above k. The existing incidence proof
gives the stated concurrency bound for selected witnesses.

The Elias check fixes r>=2 and uses eta log2 p -> r H2(rho)>H2(rho).
Choosing r>c2 produces a strictly positive leading gap between the
logarithms of the actual count and the proposed finite threshold.
Every sufficiently large prime is covered. The gap shrinks; the theorem
does not control a remainder asserted only after fixing a positive gap.

## Riccati characteristic refinement

Taylor reconstruction at a transcendental center distinguishes all
polynomial candidates. When p>D+1, the (D+1)st derivative has a
nonzero leading term (D+1)! gamma^(D+1) U^(D+2). At p=D+1 this
derivative cannot be used; the residual of the degree-D Taylor
polynomial instead has the stated nonzero U^(2D+2) term. This establishes
the candidate bound without assuming constant cross ratios.

For the list bound, zeros of a nonzero derivative-zero rational function
have orders divisible by p. Applying this to a cross ratio minus one
rules out three value classes whenever one class contains a collision.
In the only additional case (two classes of sizes h,b>=2), the minimum
internal intersection orders have sum at least p. The inequality for
h>=b reduces to (b-1)(p*b-M+1)>=0; the proved total count M<=2p
justifies its last sign. Summing all pair intersection multiplicities,
including pairs not matching the received word, gives M(A-D)<=n.
The linear equation is handled separately and does not need a finite
total candidate count.

The full-support label proof requires a single fixed equation. Nothing
in this argument controls a union of candidate sets over challenge-
dependent equations. The sharp list family and the new p+2 boundary
family meet their characteristic and degree guards. For the latter,
evaluation on F_p determines every degree-<p polynomial even over an
extension, so its classification also rules out extra extension-field
solutions. The small-field maximum scan does not imply a general p+2
upper bound.

## New finite exponent coefficients

The source moment count is m, with k=n/2 and t=k+m. The variance product
uses m dimensions, unlike the rational-line certificates, which use
surplus minus one. The independent binomial expression for each variance
matches the product formula. Pi and square-root approximations enlarge
the denominator, so the concentration ratio is a lower bound. Outward
96-bit mantissa intervals precede the rational logarithm evaluation;
no floating-point discovery value enters the exact verification.

The Elias integer inequality uses t, not k. This matters for the
521-bit example: n=521*m, so the crude p^m>2^n condition fails, but
the sharper entropy inequality holds strictly. The gap is exactly
1/521. With c1=1 and H2(1/2)=1, the required c2 is eta log2 L.
For other prefactors the correction is minus eta log2 c1. These are
interval-domain claims, not claims for the native circle domain.

Finally the all-large-prime corollary forces c2(p)>=(1/2-o(1))*
log2(p)/log2(log2(p)) even if c1(p)<=p^K for fixed K. The prefactor's
logarithm is O(log p), negligible against (log p)^2/loglog p. The
rate is fixed throughout; the gap is not.
