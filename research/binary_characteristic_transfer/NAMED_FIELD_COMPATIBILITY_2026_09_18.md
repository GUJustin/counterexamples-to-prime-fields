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
