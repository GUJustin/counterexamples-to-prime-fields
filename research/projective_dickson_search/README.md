# Beyond the explicit Dickson bank: projective orbits and sampled lists

September 17, 2026. Intrinsic prime-field exploration. All positive claims
here are finite certificates, not growing-family or tightness theorems.

## Fixed word and projective search

For p=1 mod 8, n=p-1, k=n/4, use the word

    w(x)=(1+chi(x))/2-x^k=(x^k-1)^2/2,  x in F_p^*.

Start from the explicit candidate
P(X)=sum_(j<k) binom(2k+1,2j+1) X^j. With D=k-1, enumerate

    lambda*(cX+d)^D*P((aX+b)/(cX+d)) + beta

for every PGL_2(F_p) matrix and every lambda!=0, first with beta=0
and then with arbitrary beta. The displayed expression is interpreted
as its homogenized polynomial, including at poles of the fraction.
It always has degree at most D.

The matrices are enumerated without projective duplication: c=0,d=1
with a!=0, or c=1 with b!=ad. Their count is p(p^2-1). Value-ratio
histograms exhaust lambda. For the affine-output version, a necessary
test safely discards many polynomials: because w has four values,
the sum of the four largest fibers of the candidate must be at least
the required agreement. All lambda,beta are then exhausted for surviving
polynomials. This filter cannot discard a valid candidate.

| p | length | dimension | agreement | scalar/projective list | with output translations |
|---|---|---|---|---|---|
|17|16|4|6|8|14|
|41|40|10|15|20|20|
|73|72|18|27|36|36|

All candidates in the table have exactly the displayed agreement.
No candidate in the searched families exceeds the first-order curve.
These are complete searches in the specified orbits, not complete RS
list enumerations. At p17 the independently exhausted complete nearest
list has22 candidates, so even the translated projective orbit misses8.

`verify_projective.py` independently expands the homogeneous polynomials
in coefficients and checks134 saved candidate certificates. At p17 it
also exhausts all1820 determining supports, then independently intersects
that complete list with the coefficient-defined projective orbits,
recovering exactly8 and14.

## One million determining-support samples over F_41

To leave the explicit orbit, `sample_lists.py` sampled one million
ten-point determining supports, using seeded NumPy pseudorandom keys.
Vectorized barycentric interpolation evaluates each degree-<10 polynomial
on all40 nodes. It found202 distinct candidates with15 agreements and
none with more. This is not a completeness or maximum-agreement proof.

`verify_samples.py` independently reconstructs all202 polynomials by
Vandermonde elimination. The subgroup H=mu_10 preserves the word, so
P(X)->P(hX) preserves agreement. Closing the certified list under this
symmetry yields **210 distinct degree-nine candidates**, arranged in
21 orbits of size10. Every one has exactly15 agreements. The JSON
certificate gives one polynomial and its15 agreement coordinates per
orbit; multiplying coefficient j by h^j reconstructs the entire list.

This improves the explicit finite witness count from20 to210 at these
parameters. It does not improve the rate, gap, field-size relation, or
first-order regime. No main-paper theorem is based on this search.

## Why this finite count is not yet evidence of a quadratic family

For a uniformly random received word over F_p, the exact expected list
size for any [n,k] code of size p^k at agreement A is

    E L = sum_(j=A)^n binom(n,j)*(p-1)^(n-j)/p^(n-k).

Linearity of expectation proves this without assuming independence
between the agreement events for different codewords. For the parameters
above, the means are about16.56 at p17,194.86 at p41,439.06 at p73,
21.55 at p137, and0.0657 at p193. Exact rational values are saved in
`projective_verification.json`.

These are comparison baselines, not predictions for the structured word.
Nevertheless, a count of210 at p41 alone is weak evidence for an
asymptotically large algebraic family. Finite-length combinatorics already
permits comparable counts on average. At fixed gap eta=(A-k)/n,

    E L <= binom(n,A)*p^(k-A) <= 2^n*p^(-eta*n),

so this random-word mechanism eventually disappears as p grows. The
explicit linear-size Dickson family persists, but the additional sampled
polynomials have no established formula that persists with it.

Sampling is also unsuitable for certifying absence at larger lengths.
A fixed A-agreement candidate is sampled with probability
binom(A,k)/binom(n,k) under ideal uniform independent support sampling.
This is about3.54e-6 at p41 but1.13e-10 at p73. The larger-prime target
requires structural work rather than extrapolating this finite census.

## Fixed cyclotomic lifts are excluded for these 21 support classes

Write the source domain as x=g^i with g=6 primitive in F_41. A very
specific characteristic-zero lift would keep the nodes zeta_40^i and
the word W(X)=(X^10-1)^2/2, while replacing a candidate by a complex
degree-<10 polynomial with the same15 agreement indices.

`cyclic_lift_probe.py` excludes that lift for every one of the21 orbits.
It reduces the same root-of-unity labels at split primes241,281,401,
interpolates on ten specified nodes, and finds nonzero residuals on
the other nodes. One such nonzero residual suffices: a characteristic-zero
solution is uniquely determined by those ten values, and its Vandermonde
denominators and2 are units at these primes. If its extra agreements
were identities in Q(zeta_40), they would survive every such reduction.
The symmetry transports this obstruction to all210 certificates.

This is NOT the earlier general ramified lifting obstruction. It excludes
only the specified cyclotomic nodes and the fixed word formula. Arbitrary
node and word deformations remain untested, as do constructions with
different support patterns or growing length.

## Resource and manuscript scope

Jobs ran sequentially under384MiB/60-second watchdogs. The largest job
was the one-million-support sample, about5.4seconds and45MiB RSS.
All scripts, certificates, and resource reports are retained. The paper
remains159pages; these exploratory findings stay in research notes.
No new asymptotic tightness result or better.codes improvement is claimed.
