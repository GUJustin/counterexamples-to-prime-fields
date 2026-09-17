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

2. These results do not assert a far point on the line. They should not
be described as a counterexample to a differently formulated distance
profile dichotomy requiring a far-point premise. The asserted property
is failure of correlated agreement and selected-witness line decodability.

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
All65536 F17 directions are classified by enumerating forbidden vectors
from codewords:5984bad,59552good. The exact bad probability187/2048 is
below the proven union bound30345/32768. This is an independent finite
implementation check, not independent human review of the asymptotic proof.
