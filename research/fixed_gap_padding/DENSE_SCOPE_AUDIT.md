# Scope audit of the dense-line results

September 17, 2026. The primary whitepaper's Definition24 and Conjecture2
were re-read from the saved ePrint2026/532 source. Definition24 concerns
selected nearby codewords and their concurrency on a codeword line. It
does not require a far point on the received line.

1. No correlated agreement implies concurrency at most n for ANY selection
of witnesses. If an affine codeword graph agrees identically with the
received line on a coordinates, a<A. At each other coordinate it agrees
for at most one parameter. If it contains v selected witnesses, then
v*A<=v*a+n-a, hence v<=n-A+1<=n. Thus the dense-line results really
contradict the stated finite numerical threshold when J exceeds it.

2. The final manuscript uses FAR_POINT_PADDING.md, which DOES guarantee
that parameter zero is exactly one coordinate beyond the nearby radius.
The earlier additive-offset construction did not assert a far point and
remains only a historical alternative. The stronger variant therefore
also provides a distance-profile contrast: one word has maximum agreement
A-1 while a fraction tending to one of the parameters have agreement>=A.
It does not provide a constant separation between these two radii.

3. The shrinking-gap families refute the finite numerical prescription,
and versions with remainders uniform along those families. They do not
by themselves control an unspecified remainder only promised separately
at every fixed gap. The anchored fixed-gap theorem handles that issue
separately, with a linear-in-length lower bound.

4. The density-to-one family is NOT a separation from the code's actual
global maximum list size. In fact its code has an off-line list larger
than p for sufficiently large p. To see this, keep the core N=m-1 and
match s+1 moments for A=t-subsets of it (instead of s moments for the
anchored t-subsets of m points). The numerator changes from
binom(N,h) to binom(N,h-1), losing only log_2(t/h)=O(log b) bits.
Use the same full-m interval moment ranges, valid even if the removed
anchor is internal, and add the (s+1)st range. Its logarithm is
O(s*log m)=O(sqrt(b log b)), which is o(epsilon_b*b).
The box lower bound still has log_2 L'>=b+Omega(epsilon_b*b).
The common locator prefix now gives degree<K candidates agreeing on
A core points with a degree-A word. Extend that word arbitrarily over
the padding: all these candidates remain nearby. Thus the actual
maximum list size exceeds p, and an actual-list-size times n threshold
is vacuous for this family. The separate generic-domain theorem in the
paper remains the result comparing line behavior with actual maximum
list size. This argument is asymptotic; do not infer the same bound for
every small finite table row.

5. The new direction is nonzero on padding, so all p affine parameters
are distinct words. All coordinates, offsets, directions and codeword
coefficients are in F_p. The domain includes an integer core and chosen
padding positions; it is not a prescribed FFT subgroup, so none of these
certificates by itself improves a better.codes instance.

Independent arithmetic audit: all four finite table rows at M31,M61,
M127,M521, plus M2203, pass without importing construction helpers.
A different variance expression and integer square-root rounding replay
the Gram bounds; M2203 is replayed with complement box counts alone;
a smooth (nonintegral) occupancy bound replaces balanced occupancies.
For the older additive-direction argument, all65536 F17 directions are classified by enumerating forbidden vectors
from codewords:5984bad,59552good. The exact bad probability187/2048 is
below the proven union bound30345/32768. This is an independent finite
implementation check, not independent human review of the asymptotic proof.

Far-point update: all displayed density rows were replayed with p-1 in
the multiplicative label universe. The eight-decimal bounds are unchanged,
though some integer count bounds decrease by one. The independent audit
now also uses p-1. A new exhaustive F17 check verifies all65536 directions,
the exact expected union36975/4096, a12-label selected union, and a full
line profile with15nearby nonzero parameters and two farther parameters
(0and11). Its maximum joint agreement is3 at threshold4.

Quantitative far-point refinement: if the far word has at most A-r
agreements, every selected affine codeword graph contains at most
floor((n-A+r)/r) pairs. A degree-e graph contains at most e times
that ratio, rounded down. Count coordinate incidences: coordinates
identical in the parameter number a<=A-r; each other coordinate
contributes at most e roots. Thus m*A<=m*a+e*(n-a).
For the growing-far family r=floor((log_2 p)^(1/6)), this strengthens
concurrency to O(n/(log_2 p)^(1/6))=o(n), uniformly over witness choices.
This is an application of the existing incidence argument, not a new
construction or a fixed-gap result.

Independent headline replay now also verifies the gap-scale far rows
M2203 (>0.93155073), M4423 (>0.99999974), and M9689 (>0.99999970),
with numerical-prescription bounds 2^-126, 2^-619, and 2^-1371.
It imports no construction helpers and separately checks primality.

Cubic-domain update: ../cubic_domain_warp/ now proves complete nonzero
coverage at fixed rate and fixed positive separation fraction eta/u.
It uses cubic images of the interval and a published hypersurface
point-count estimate, unlike the elementary padded-interval results
reviewed above. This closes the former fixed-relative-buffer frontier,
but not fixed-gap superlinear growth, prescribed-domain transfer, or
actual-list-size separation. Local ambiguity is necessary for this
construction: L>p candidates at one padding point map to p-1 labels.
