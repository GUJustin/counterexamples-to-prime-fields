# Exact product classes throughout the native dyadic circle family

September 16, 2026. Exact comparison certificate and separate arithmetic
audit passed. This replaces the global-comparison limitation in the older
joint-count note, within the precise one-anchor family below.

## Results

Let p=2^31-1. Both winning parameter sets remain unchanged.

| Alphabet | n | K | T | M | B | r | h | Guaranteed labels J | Excess bits, greater than |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| F_(p^2) | 4096 | 64 | 86 | 512 | 8 | 0 | 11 | 334185312123996677 | 24.5949101010 |
| F_(p^4) | 8192 | 1024 | 1182 | 256 | 32 | 1 | 37 | 73497635817388704528460 | 34.7773316358 |

The excess compares J with n*2^(H2(K/n)/((T-K)/n)). Both strict
characteristic-p Elias conditions pass rational checks. The quartic bank
is fourteen labels larger than the previous value; its relative numerical
effect is negligible. The selected-graph concurrency upper bounds are251
and55, respectively. Attainability was previously verified for the
quadratic example only.

## Optimized family and limitations

The certificate covers every M=2^m>=4, B=2^b>=2, MB<=2^30,
d=2^a<M, K=dB, and every reserve r>=0 with h=d+2r+3<M for which
T=hB-2 lies strictly below the characteristic Elias radius. One support
point is fixed as an anchor. Every possible product exponent is covered.

For r=0, use each complete anchored product class and its exact support
incidences. For r>0, use the guaranteed class size

    N = ceil(C_(h-1)(c)/p^(2r))

and balanced incidence lower bounds. These are the largest guaranteed
banks from this specified formula over the stated parameter family.
Actual leading-coefficient classes can be larger; arbitrary subclasses,
additional anchors, other support constructions, and other dimensions
are outside the optimization claim. No pinned better.codes improvement
or unrestricted coding-theory upper bound is asserted.

## Product classes need only logarithmically many representatives

C_k(c) counts k-subsets of {1,...,M-1} whose sum is c modulo M. The
character generating function from CIRCLE_JOINT_VALUES.md gives

    C_k(c) = (1/M) sum_(L|M) R_L(c) F_L,
    F_L = (-1)^(k+floor(k/L)) binom(M/L-1,floor(k/L)).

Here F_1=binom(M-1,k). For dyadic L>1, R_L(c) is L/2 if L divides c,
-L/2 if L/2 divides c but L does not, and0 otherwise. Hence the count
depends only on v_2(c), with c=0 treated as the final class. Odd-unit
multiplication acts transitively on each such class and permutes all
nonanchor support positions. It preserves incidence histograms. Thus
one representative for each valuation covers every product exponent,
including the possible effect of a smaller population with a better
incidence histogram.

The exact incidence at nonanchor exponent a is

    I_a = sum_(j=0)^(h-2) (-1)^j C_(h-2-j)(c-(j+1)a).

The anchor incidence is N. For r>0, the actual coefficient subclass
incidences are unknown, so the balanced bound is used instead.

## A uniform two-average bound makes the whole grid certifiable

For 1<=k<=M-2, put K0=binom(M/2-1,floor(k/2)). Then

    |F_L| <= K0  for every L>=2,
    (M-1)K0 <= binom(M-1,k).

For the first inequality, successively halve L. If q=M/L and a=floor(k/L),
the next binomial coefficient is binom(2q-1,2a) or binom(2q-1,2a+1).
Map an a-subset of q-1 pairs to its union, adding a distinguished extra
point in the odd case. This injects the previous subsets into the next.

For the second inequality, write M-1=2A+1. If k=2s, Vandermonde gives

    binom(2A+1,2s)
      = (2A+1)/(2s) * binom(2A,2s-1)
      >= (2A+1)/s * binom(A,s) * binom(A,s-1)
      >= (2A+1) * binom(A,s),

using binom(A,s-1)>=s for 1<=s<=A. Odd k follows by replacing k with
M-1-k; this preserves K0 and the total binomial coefficient.

Since the sum of the nontrivial character multiplicities is M-1,

    max_c C_k(c) <= 2*binom(M-1,k)/M.

Consequently, if u is the existing rigorous upper bound for
log2[binom(M-1,h-1)/(M*p^(2r))], every guaranteed N is at most
2^max(0,ceil(u)+1). This excludes uncomputed rows. The average count
decreases with r because its successive ratio is

    (M-h)(M-h-1)/(h(h+1)*p^2) < 1.

The same two-average bound therefore excludes every omitted reserve tail;
no monotonicity of an individual product class is assumed.

## Verification

- Complete coverage:4410 admissible parameter groups,56 empty groups,
  4383 reserve tails,5309 rows excluded by rational upper bounds.
- Exact contenders:66 rows and1406 alphabet/product-class comparisons.
- Independent coefficient-sum arithmetic rechecks every computed product
  population and collision certificate, and every raw-row exclusion.
- Exhaustive supports for M<=16 verify all count and incidence orbits.
  Five earlier dynamic-program certificates independently match larger
  counts and incidences. The two-average inequality is also checked at
  2026 finite parameter pairs.

Files: `certify_circle_product_dyadic.py`,
`circle_product_dyadic_verification.json`, `verify_circle_product_orbits.py`,
`circle_product_orbits_verification.json`,
`verify_circle_product_dyadic_output.py`,
`circle_product_dyadic_output_verification.json`.

The full grid certificate took15.17 seconds and sampled51,312KiB RSS.
The long moment-counting process was paused while these checks ran and
resumed in a finally block.
