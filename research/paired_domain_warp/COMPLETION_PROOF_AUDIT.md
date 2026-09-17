# Completion proof audit — September 17, 2026

This is an internal mathematical audit, supported by independent arithmetic
implementations and small exhaustive fixtures. It is not external peer review
or a formal proof-assistant certificate.

The integrated statement is `completion.tex`, following the character-energy
lemma in `paired.tex`. It strengthens the original multiple-padding-block
construction: a single padding block suffices, the line direction has weight
exactly 2r, and the distance is known exactly on the whole r-dimensional flat.

## Conditional averaging

Fix the padding first. The base-core energy proof is uniform in these fixed
values, not merely an average over padding. Its expected missing fraction is
at most d0. The support pairs with symmetric difference u on each side cannot
collide when 1 <= u <= r: after cancellation, distinct monic degree-u
polynomials in Y differ in degree at most u-1 and cannot agree at r distinct
padding squares. Larger differences use the product-character estimate.

For each extra pair of alternative core orbits, the candidate family chooses
one of the pair. If B is the missing set, the new missing set is the
intersection of its two multiplicative translates. Normalized Parseval gives
expected missing density at most h^2 + C^2 h/p. The character estimate stays
uniform over the entire preceding history: the total excluded set has size
at most n+1 < sqrt(p), so deleting it costs at most sqrt(p), and at least p/2
arguments remain. Requiring the two sampled orbits to differ costs at most
1/(1-4/p). This yields Phi(h), independently of how the old image was chosen.

The existence recurrence uses successive averaging, not Jensen's inequality
on a random density. The randomized guarantee uses conditional Markov at each
step and a union bound; it does not assume independence of successive images.
The sampler computes neither images nor lists.

## Exact geometry

Every chosen locator has degree K+1 after the parity adjustment. Its leading
terms cancel with a reference locator to give a codeword of degree < K.
The reference received word has exactly K+1 roots in the domain, while the
root bound forbids more agreement with any codeword. Its distance is thus
(n-K-1)/n for every generated output, regardless of completion success.

On completion, arbitrary nonzero locator targets can be imposed at all r
padding pairs. To match a parameter vector with j nonzero coordinates,
complete its specified targets arbitrarily on the remaining padding pairs.
The resulting codeword has K+1+2j agreements. Changing 2j received coordinates
can improve distance by at most 2j; hence equality holds. This also excludes
any unaccounted-for closer codeword.

At full support the distance inequality is saturated. Every nearest codeword
must match every padding coordinate and must mismatch its original value at
those coordinates. Therefore different full-support parameter vectors have
disjoint decoding lists. The far point excludes a common agreement set at the
nearby threshold. Direction weight 2r is minimal for a distance decrease 2r/n.

The optional zero coordinate is not a free extra agreement: when K is odd it
is never matched by selected candidates; when K is even multiplication by X
adds exactly one common root and increases locator degree and far agreement
by one. The formulas remain K+1 and K+2r+1 in both cases.

## Growing r and exact rates

For r log(log p) = o(log p), set t=16(r+1) and
n=(2r+4/5) log2(p)/H2(rho)+O_rho(1), choosing the exact-rate parity.
Base support count has logarithm r log2(p)+(2/5)log2(p)+o(log p),
so it exceeds p^(r+1/3). The character constant contribution is p^o(1).
Initial density exceeds p^-1/8 with probability at most 2 p^-5/24.
Each further step reduces it by a factor p^-1/16 except with probability
at most 4 p^-1/16. After t steps its bound is less than p^-r, so the
integer missing count is zero. The total failure is p^-Omega(1).

The strict Elias margin in eta log2(p) is Theta(1/r), larger than the
O(1/log p) entropy change. The prescription's logarithmic ratio is
log2(n)-log2(p)/(5(2r+1))+O(1/r), which tends to minus infinity.
The gap shrinks; no fixed-gap or prescribed-domain conclusion follows.

## Verification artifacts

- `verify_completion.py`: exact dyadic recurrence and finite certificates.
- `audit_completion_independent.py`: independent implementation with weaker
  constants C=4r+4 and conditioning denominator p-8; also Lucas–Lehmer,
  strict Elias, and the numerical prescription.
- `verify_translate_identity.py`: exact finite-group translate averages.
- `check_small_completion.py`: all 1369 parameters over F37, including the
  three exact distance levels. Toy fixtures are not below-Elias claims.
- `verify_completed_sample.py`: independent root-product replay of every
  coordinate in the stored M521 sample. Distances at zero and one are
  deterministic; whole-flat coverage is a guarantee over generator randomness,
  not a deterministic certificate of that particular sample.

No arbitrary-parameter witness recovery, global list upper bound, FFT-domain
transfer, or better.codes improvement is established.

## Witness degree and extension fields

The existing incidence lemma bounds every degree-e polynomial codeword graph
by floor(e(n-K-1)/(2r)) nearby parameters; thus selecting all p-1 witnesses
requires degree Omega(p/log p). This does not imply computational hardness.

Over an extension field, any word at the tested radius must match all padding
and at least K+1 base-valued core coordinates. Interpolation forces its
coefficients into the base field, so the nearby torus and its lists remain
exactly the base-field torus and lists. For a scalar line parameter outside
Fp, a base-linear functional taking 1 to 1 and z to 0 projects every agreement
to one with f. This bounds agreement by K+1; the zero codeword attains it on
the reference core roots. Thus every nonbase line parameter is exactly as far
as f. `verify_extension_profile.py` exhausts all 4368 interpolation subsets
for the F17 fixture, determining all potential nearby witnesses over F17^2.
All 272 nonbase parameters have distance 10; the 16 nonzero base parameters
have distance 8 and disjoint lists, with 35 codewords total.


## Two far endpoints and multiple far inputs

The exact affine profile immediately supplies a line with exactly two far parameters: split an even number r of padding directions into equal groups and take the two endpoint coefficient vectors to be complementary indicator vectors. At z=0 and z=1 the weight is r/2; elsewhere it is r. Thus both endpoints have distance theta+r/n, all p-2 remaining parameters have distance theta, and the relative endpoint separation tends to half the capacity gap. No new sampling hypothesis is used.

For the r words f+e_j, each has distance theta+2(r-1)/n. Uniform affine coefficients give nearby probability ((p-1)^r-(-1)^r)/p^r, by counting nonzero coordinates summing to one. This tends to one while every input lies almost the whole capacity gap outside the radius. These are coding statements on the constructed domains, not an implementation-level soundness claim.

`check_far_inputs.py` verified explicit witnesses for all 37 parameters of a complete r=2 product-image fixture (n=36,K=15), with endpoint distances 18 and all 35 other distances 16. The degree/direction lower bound proves exactness. It also exhausted coefficient counts for 16 small (p,r) cases. The toy fixture itself is not claimed below Elias; that qualification comes from the asymptotic completion theorem and separately certified finite parameters.

## Fixed batch sizes, multilinear mixtures, and curve profiles

The multi-input statement now allows any t>=2 dividing r, with no parity
restriction on r (only the two-equal-endpoint statement requires even r).
Partition directions into t groups of r/t. Each displayed input has
weight r/t and hence excess distance (1-1/t)*2r/n. Every fixed t can
approach that fraction of the gap by taking r large through multiples.

For unrestricted linear coefficients, condition on their sum s. If s is
nonzero, normalization gives the previously counted affine distribution.
If s=0, the reference word cancels and the combination has support at most
2r; n-K>=4r+1 puts it within theta of zero. This condition is automatic
in the stated growing-field regime. The exact probability is therefore
1/p+(1-1/p)*[(1-1/p)^t-(-1)^t/p^t]. For tensor-product multilinear weights,
all coefficients are nonzero iff each coordinate avoids0and1, giving
(1-2/p)^ell for t=2^ell. These are pure coding consequences, not a
full-protocol soundness conclusion.

The zero-coordinate profile also gives a degree-e distance budget:
sum_z(dist(f_z,C)-theta)<=2er/n for any curve in this affine space with
at least one nearby point. No coordinate polynomial is identicallyzero;
each has at most e roots. Any desired multiplicities a_i<=r with total
<=er can be realized by cyclically allocating their roots to r degree-e
coordinate polynomials. This is a statement about the constructed space,
not a universal distance budget. Lagrange interpolation of t displayed
far inputs attains it at degree t-1: only those t parameters are far,
with equal excess2r(t-1)/(nt); all other p-t parameters are nearby.
