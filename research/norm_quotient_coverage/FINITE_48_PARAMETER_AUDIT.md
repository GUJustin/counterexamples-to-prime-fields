# Conditional 48-coordinate prime-field parameter audit

2026-09-18. Algebra and exact below-Elias inequality **PASS**. Existence of the required23-tag product-covering set is still a separate condition; this receipt does not assert that its search has succeeded.

Assume p=65537, m=2, b=3, a0=1, and23 distinct nonzero square tags G excluding1, with every nonzero field element represented as ∏_(a∈S)(3−a) for some13-subset S⊂G. Let D be the square roots of G∪{1}; then |D|=48. The strict code dimension is J=24. Division gives

    J−1=23=(13−2)*2+1,

so r=13, w=1. Reserve the coordinate1, giving R=X−1. The pole X²−3 has no roots in F65537 because3 is primitive and hence nonsquare. Define

    f=(X−1)(X^26−3^13)/(X²−3),
    g=−(X−1)/(X²−3).

The audited compiler gives exact individual/common agreement A=J+m−1=25 and exact agreement T=J+2m−1=27 for every nonzero pencil label. Every witness has degree at most23. The complete normalized mixture profile is exact agreement25 for the two endpoints and exact agreement27 for all65535 other affine parameters.

Thus rate=1/2, endpoint normalized distance=23/48, interior decoding radius=(48−27)/48=7/16, and source-to-interior gap=2/48=1/24.

For rate1/2, the q-ary Elias radius is the increasing-branch solution of H_p(R)=1/2. Since7/16<1−1/p, the proposed radius is strictly below Elias iff H_p(7/16)<1/2. Multiplying the entropy inequality by16 log p and exponentiating gives EXACTLY

    (p−1)^7 *16^16 < p^8 *7^7 *9^9.

Independent integer arithmetic at p65537 gives

    left  =95780971304118053647396689196894323976171195136475136,
    right =108582871902291753903353686974292588554886020758912367.

The inequality is strict. No decimal entropy approximation or asymptotic assertion is involved. Coverage remains the only missing premise of this particular finite construction; the argument does not enumerate or claim uniqueness of the maximizing witnesses.

## Paragraph audit after the root's successful coverage search

The added48-coordinate paragraph in `prime_random_fiber_log_gap.tex` was read. Its23 printed tags exactly match `/tmp/prime48-root-dp.json`; independent integer checks confirm they are distinct squares and exclude1. All displayed formulas, distances, the1/16 capacity margin, the1/24 source loss, and the exact entropy inequality agree with this audit. The producer reports zero missing products on its first sample. Independent support enumeration is assigned to another agent; this paragraph audit does not replace that remaining coverage receipt. Final source hashing will follow the stable certificate-path insertion.

## Final coverage closure and source hash

Coverage is now **FULL PASS**, no longer conditional: the producer receipt records bitset DP coverage65536, meet-in-the-middle enumeration of all1144066 subsets, and direct field multiplication of65536 saved supports. The separate root-owned `below_elias_prime_fixture/independent_direct.py` enumerates all subsets without discrete logs and its `independent_direct.verified.json` reports the same full count array. Minimum product multiplicity is3, maximum36. This audit inspected those receipts; the independent enumeration itself was performed by the root, not re-attributed to this agent. All remaining algebra/entropy checks were independently established above.

The final paragraph includes the correct certificate path. SHA256 of reviewed `prime_random_fiber_log_gap.tex`: `9e43f03cc96e1fd2881b68e7da9abc60c41c6944f5ffd8c449396538af3854cd`.
