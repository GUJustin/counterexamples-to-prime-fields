# Independent audit: quarter-density Frobenius-block puncturing

2026-09-18. **PASS.** Independently read [density_quarter_puncturing.tex](density_quarter_puncturing.tex) and the complete underlying classification in [scaled_fiber_padding.tex](scaled_fiber_padding.tex). No main-text edits. The accompanying [arithmetic verifier](verify_density_quarter_puncturing.py) and [receipt](verify_density_quarter_puncturing.json) check the onset using exact integers and rational numbers.

## Hypergeometric threshold and simultaneous retention

Write N_1=2(p²−1) and m=(p²+3)/2. For any one second-block support S of size k∈{2p−2,2p}, its intersection Z with a uniform m-subset has the same law as the sum of **k draws without replacement** from a population of N_1 bits containing m ones. Thus E[Z]=km/N_1>k/4. Using k, rather than m, as the sample size is valid by this symmetry of the hypergeometric distribution.

For odd p the strict failure event is

    Z<ceil(p/4)  iff  Z≤ceil(p/4)−1,

and ceil(p/4)−1≤(p−1)/4≤k/8. Hence failure entails a lower deviation of at least k/8 from the mean. Hoeffding's without-replacement inequality gives

    Pr[failure]≤exp(−2(k/8)²/k)=exp(−k/32)
               ≤exp(−(p−1)/16).

The without-replacement version is explicitly stated in Bardenet--Maillard, [Concentration inequalities for sampling without replacement](https://arxiv.org/pdf/1309.4029), Proposition 1.2, following their Lemma 1.1 (Hoeffding's convex comparison). Applying it to the negated population gives the lower-tail statement used here. This checks the dependence assumption and the factor in the exponent.

There are p(p+1) canonical supports, since there are p+1 choices of norm-one a and p choices of v∈I_a. Their coordinates depend on (a,v), not on the additional first-block constant b. The union bound therefore uses p(p+1), with no extra factor for b or for the ambient field.

At p=257, the exact inequality

    257·258 < 16^6/6! + 16^7/7! < exp(16)

holds. For x≥257, the logarithm of the union bound has derivative

    1/x+1/(x+1)−1/16 < 2/x−1/16 < 0.

This proves the uniform onset, not merely a check of one prime. The integer rounding in the manuscript is correct.

## Complete classification after puncturing

The underlying block classification is valid over the full coefficient field E=F_(p^4), not merely over B_0=F_(p²). I checked the coefficient-projection and Frobenius arguments in the cited proof, including its sharper bound for quadratics canonical on neither block.

The relevant facts are:

* A quadratic canonical on only one block has **zero** matches on the other block. Its norm-one quadratic coefficient is fixed, while the other block's linearized constant equation fails the required image condition. Its total agreement is at most 2p, before or after puncturing.
* For a quadratic aX²+cX+b with c≠0, coefficientwise B_0-valuedness on a physical line uB_0^* requires c∈uB_0. The four physical lines are distinct. At most one line qualifies; its block contributes at most p for a noncanonical quadratic, and the other block contributes at most four by projection.
* When c=0 and a∈B_0, the noncanonical linearized equations contribute at most two per block. When c=0 and a∉B_0, projection contributes at most four per block. Thus a quadratic canonical on neither block has at most max(p+4,8)=p+4≤2p for p≥257.

Puncturing only removes matches. Consequently every witness above A=2p is canonical on both blocks. Every such witness keeps at least

    2p−2+ceil(p/4) ≥ floor(11p/5)=T.

Indeed the left side minus 11p/5 is at least p/20−2, already positive for p≥257.

For every norm-one a, the nonzero image line I_a can be characterized by z^p=−a^(−1)z, so the p+1 image lines are distinct. Since 1 and η are B_0-linearly independent, the planes I_a+ηI_a intersect pairwise only at zero. Each of their nonzero parameters determines one and only one tuple (a,b,v), hence one quadratic aX²+b. Zero gives precisely b=v=0 for each a, hence exactly p+1 different witnesses. The whole threshold profile is therefore exactly

    B=(p+1)(p²−1) singleton parameters,
    one parameter with p+1 witnesses,
    empty lists at every remaining parameter.

This uses the complete underlying classification, not just preservation of the old theorem's threshold-4p witnesses. The new B correctly includes cases where precisely one of b,v is zero. The actual agreements of nearby words may exceed T and depend on the puncturing; the proposition claims their exact threshold lists, not that their maximum agreement equals T.

## Sources, common agreement, and affine parameterization

The plane union has size 1+B. Its complement has the exact size

    p^4−(1+B)=p(p−1)²(p+1)>1.

Thus distinct α,β outside the union exist. At either source, no doubly canonical quadratic exists; the preceding bounds give agreement at most 2p. A first-block canonical quadratic with b≠0 still agrees on all its 2p first-block coordinates, and g=0 there. The same polynomial therefore explains both sources on the same 2p coordinates. Individual agreement and common agreement are all exactly 2p.

For (1−z)r+zs, the native label is α+z(β−α), a bijection of E. No projective or omitted-label correction is needed; neither endpoint is a nearby parameter.

## First order, Johnson, and scope

With n=(5p²−1)/2,

    sqrt(3n/2) < (31/16)p,
    (3n/8)^(1/4) < sqrt(p).

The first inequality follows from 15/4<(31/16)²; the second from 15/16<1. For p>256, sqrt(p)<p/16. Hence the repository's stated first-order upper bound is strictly below 2p. Also T>2p and

    T² ≤ 121p²/25 < 5p²−1=2n,

the latter strict inequality already holding for p≥3. At the onset prime p=257 the exact values are

    |D_0|=132096, |D'_1|=33026, n=165122,
    A=514, T=565, B=17040384,
    worst retained canonical agreement ≥577,
    2n−T²=11019,
    (T−A)/(T−3)=51/562.

The limiting loss ratio is 1/11 because T−A=floor(p/5). The domain is a selected subset of F_(p^4), and the alphabet is F_(p^4); neither is a prime-alphabet result. Since n∼(5/2)p², this does not retain a fixed practical domain length as a large base characteristic grows. No equivalence to a protocol-specific code or security implication follows from this audit.

No substantive proof issue was found. The minor wording that the domain itself was an extension field was reported; the parent corrected it to a selected subset. The audited TeX files' hashes are recorded in the receipt.
