# Compatibility with the user's named extension fields

The new degree-five theorem applies directly to F_(p^5) for M31 p=2147483647 and BabyBear p=2013265921. The independently checked integer root and irreducible quadratic cofactor in verify_d5_named_fields.py/.json show that H=Z³+2Z²+3Z+1 has exactly one root in each field: 1657462779 for M31 and 952150975 for BabyBear. Thus the fixed-rate internally padded theorem guarantees at least p^5−1 bad native challenges in either quintic extension. Its domain is the FULL extension field, lengthp^5, approximately2^155. Padding may fill the one canonical exclusion, so this is a lower count, not an exact full bad set.

The new five-dimensional domain does not embed in a degree-three or degree-four extension. Earlier separate cubic-extension theorems apply over Goldilocks cubed at length about2p² (approximately2^129). The earlier quartic-extension construction applies over M31/BabyBear quartic extensions at length9p² (approximately2^65), dimensionthree, source/commonagreement2p and threshold4p. These are distinct constructions and parameter regimes.

Matching the alphabet alone is insufficient for a concrete cryptographic conclusion. These evaluation domains and lengths are not the smaller base-field subgroup or circle domains used in a specified practical protocol. No concrete security-bit upper bound or better.codes improvement follows from this field substitution.

The prime moduli agree with their implementation documentation: https://docs.rs/p3-mersenne-31 , https://docs.rs/p3-baby-bear , https://docs.rs/p3-goldilocks/latest/p3_goldilocks/struct.Goldilocks.html . Goldilocks is p=18446744069414584321. Its H is irreducible, but this gives all native labels only for a QUINTIC extension, not for the cubic extension asked about. The cubic case uses the earlier theorem.


## Updated quartic construction at the integer Johnson boundary

The quarter-density theorem supersedes the length-9p² comparison above for
its singleton-list conclusion. It has n=(5p²−1)/2, dimension3, exact
individual and common agreement A=2p, and T=isqrt(5p²−2), the largest integer
strictly below sqrt(2n). There are exactly (p+1)(p²−1) singleton parameters,
one further parameter with list size p+1, and no witnesses elsewhere.
The source agreement itself remains above the first-order curve.
The loss ratio (T−A)/(T−3) tends to 1−2/sqrt(5), about10.56%.

For BabyBear p=2013265921, this applies directly to the quartic extension:
n=10133099171649945602, A=4026531842, T=4501799456,
and B=8160249298611705595853537280 singleton parameters. The exceptional
probability including the further parameter is (B+1)/p⁴, about2^(−30.90689).
These are codes of dimension3 on a selected extension-field domain of
about2^63.14 points. They are not a concrete security ceiling for a short,
prescribed practical domain or for a deployed protocol.

This particular theorem requires F_(p⁴), and therefore does not apply to
the quadratic extension of Goldilocks. It does apply to its quartic
extension. No impossibility for different quadratic-extension constructions
is asserted. The exact threshold proof and finite onset are audited in
quadratic_frobenius_core/QUARTER_DENSITY_EXACT_JOHNSON_THRESHOLD_AUDIT.md.


## Current quartic tradeoffs: message length is not codeword length

For the three rows below the field is F_(p⁴), the codeword length is
n=(5p²−1)/2, and T=isqrt(5p²−2). The exact threshold profile has
B=(p+1)(p²−1) singleton parameters and one additional parameter with p+1
witnesses. Both source words and their ordinary common agreement satisfy
the stated agreement bound. These rows use no neutral padding.

| Message length k | Source/common agreement | Rate | Guaranteed limiting loss divided by T−k | Above first order? |
|---|---|---|---|---|
| 3 | exactly 2p | Θ(p^−2) | 1−2/sqrt(5), about10.56% | Yes, even the sources |
| floor(sqrt(p/2))+1 | exactly 2p | Θ(p^−3/2) | 1−2/sqrt(5) | No |
| floor(p/20)+1, primitive block scale | between2p and2p+2floor(p/20) | Θ(p^−1) | at least(sqrt(5)−2.1)/(sqrt(5)−0.05), about6.22% | No |

Every row still has fractional agreement loss Θ(1/p). In particular, a
constant entry in the loss-ratio column does not mean a constant loss in
relative distance. The last two rows are checked research tradeoffs, not
claims of a practical code rate or tighter first-order bounds.

For BabyBear, the respective message lengths are3,31728,100663297,
all against10133099171649945602 codeword symbols. The final row guarantees
at least273941022 extra agreements beyond either source's maximum, but
still has a rate of about9.93e−12. All these field substitutions are
existence theorems for selected extension-field domains, not explicit
lists of practical evaluation coordinates.

A separate research refinement adjusts the retained block density to attain
a limiting loss ratio1−sqrt(3)/2 at dimension3. Another standard padding
transformation attains rate1/2 but requires alphabetp^(4*2^Θ(p)), retains
only Θ(1/p) fractional loss, and loses first-order placement. Neither
resolves the short-domain, fixed-alphabet, constant-rate target.


## Higher-power variant: a larger relative loss at a longer domain

The new higher-power construction keeps extension degree four and uses
k=h+1 for a proper divisor h of p²+1 satisfying the explicit finite guards
in [the proof](quadratic_frobenius_core/HIGHER_POWER_FULL_FIBER_LIFT.md).
Along a proved prime sequence with h growing slowly, the source agreements
approach the first-order boundary and the tested agreement approaches
Johnson. The loss divided by the capacity margin tends to
1−1/sqrt(2), about29.3%, with n^(3/2−o(1)) singleton challenges.
The rate remains n^(−1+o(1)); this improves the relative-loss conclusion,
not the practical domain or rate.

BabyBear admits h=12241 because 12241 divides p²+1. Keeping a fraction
54/55 of the second full block gives the following exactly checked
parameters over F_(p⁴):

| Quantity | Value |
|---|---:|
| Message length | 12,242 |
| Codeword length | 98,329,309,808,423,281,932,846 |
| Common agreement | 24,644,388,138,961 |
| Each endpoint agreement, exactly | 24,644,388,138,961 |
| Tested agreement | 34,693,646,123,820 |
| Singleton challenges | 8,160,249,298,611,705,595,853,537,280 |
| Exact loss / capacity margin | greater than28.9657% |

The first-order agreement is below24,533,338,196,068, strictly below
common and endpoint agreements. The tested agreement is the largest
integer strictly below Johnson. The complete deterministic finite hypotheses are verified by
[the exact certificate](quadratic_frobenius_core/verify_higher_power_deterministic.json).
The domain consists of explicit multiplicative branches and a fixed prefix
of one more branch; its coordinates are not enumerated by this certificate.
Its rate is approximately1.25e−19. The native challenge count is unchanged
from the dimension-three family, so there is no improved failure-probability
exponent at this fixed alphabet.

This instance does not apply to Goldilocks squared or to a degree-five
extension through field substitution. It gives no better.codes improvement
and no practical SNARK-security ceiling. Direct restriction of the original quadratic sources
to standard multiplicative domains has a separate obstruction, proved in
[PRACTICAL_DOMAIN_DIRECT_RESTRICTION.md](quadratic_frobenius_core/PRACTICAL_DOMAIN_DIRECT_RESTRICTION.md).

The odd-power Kummer refinement proves exact agreement hp at every
nonexceptional parameter when p>=h², including both displayed endpoints.
For the BabyBear instance the noncanonical agreement cap is2,312,937,842,
well below hp=24,644,388,138,961. The exact loss ratio is now
10049257984859/34693646111578. This improves the source statement without
changing the domain, alphabet, code dimension, or native challenge count.

## High-rate Hermitian family (September 19 follow-up)

The new complete norm-family theorem uses the quartic alphabet F_(p^4), the full quadratic subfield domain of length n=p², and dimension k=p²−2p. Its threshold is T=p²−p−2. Exactly p²(p−1) affine labels have singleton lists with nearest agreement T+1; all remaining words have agreement at most p²−p−r_p, where r_p is the least integer r>=2 with r²−r+1>=p. Both explicit endpoints are in this far complement. Common agreement is exactly k. Compact list membership is recovered by two four-dimensional linear algebra operations over F_p.

For BabyBear, this gives n=4053239668659978241, k=4053239664633446399, T=4053239666646712318, and 8160249290505226260546846720 singleton labels. The guaranteed individual source loss is 44868 coordinates; the common-agreement loss is 2013265919 coordinates. These are DIFFERENT losses. The individual guarantee is about 1/sqrt(p) of the capacity margin; the common-agreement loss equals that whole margin.

For M31, n=4611686014132420609, k=4611686009837453315, T=4611686011984936960, and the corresponding guaranteed individual/common losses are 46340 and 2147483645 coordinates.

Thus the alphabet matches degree-four BabyBear or M31, but the domains still have about four quintillion points and the rates are extremely close to one. The threshold is below the full first-order curve, and the code dimension exceeds the characteristic. No actual SNARK domain, better.codes improvement, or prime-alphabet tightness follows. The degree-eight variant makes both individual agreements equal to k; that variant does not preserve a degree-four alphabet. This family does not directly apply to a degree-two Goldilocks alphabet.
