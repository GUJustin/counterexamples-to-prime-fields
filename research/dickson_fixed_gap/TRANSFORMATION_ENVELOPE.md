# Dickson lists under mixed padding, pullback, and block localization

This combines existing Dickson puncturing bounds with an exact transformation envelope. It is not an upper bound for arbitrary polynomial families or new coincidences over extension-field nodes.

## Input already proved elsewhere

`../binomial_first_order_search/PUNCTURING_LIMIT.md` gives, for arbitrary retained domains and subbanks of the original Dickson bank, in the growing-list limit,

    D=k+o(k),  N<=4k,
    A<=min(N/2,N/4+k/2)+o(k).

The error is uniform for candidate subsets whose size tends to infinity, by the archived Fourier estimate. In particular

    A <= 3D/2+o(k),
    N-A >= (5/6)(N-D)-o(k).

For the second inequality set D=k initially. If N<=2k, N-A>=N/2 >=5(N-k)/6; if2k<=N<=4k, N-A>=3N/4-k/2 >=5(N-k)/6. Replacing k by k-1 only changes a bounded term.

## New mixed-transformation envelope

Consider any interleaving of:

1. unramified degree-e pullback, carrying the original candidates and inherited matches: (N,D,A)->(eN,eD,eA);
2. multiplication by a common polynomial with t distinct fresh zero nodes, carrying the old word multiplied by that polynomial and assigning zero at the new nodes: (N,D,A)->(N+t,D+t,A+t);
3. appending z coordinates without claiming any additional carried matches: (N,D,A)->(N+z,D,A).

Both inequalities above are preserved, with the error scaled only by pullbacks. Indeed A-3D/2 decreases by t/2 under common-zero insertion, and (N-A)-5(N-D)/6 is unchanged; no-match insertion increases the latter by z/6 and leaves the former unchanged. Multiple zeros cost more degree than distinct nodes and cannot improve these upper envelopes. Therefore, with effective degree rate r=D/N and agreement a=A/N,

    a <= min(3r/2,(1+5r)/6)+o(1).                 (E)

This is the exact extremal envelope of mixed zero/no-match padding applied to the full-domain limiting source (4,1,3/2): at fixed r use only no-match padding for r<=1/4 and only common-zero padding for r>=1/4. Arbitrary interleaving cannot improve it. Degree pullbacks preserve the effective rate, while the actual dimension rate is (D+1)/N>=r.

## Comparison with the actual first-order curve

The envelope in(E) lies strictly below the audited first-order threshold a1(r), for every0<r<1.

For r<=2/9, a1(r)>=sqrt(r/2)>=3r/2, with strict inequality at the possible endpoint from the curve formula. For2/9<=r<=1/4 the high-branch quadratic gives

    F_r(3r/2)=-r(9r²-52r+20)/4<0.

For1/4<=r<=8-3sqrt6, evaluate the same quadratic at the other line:

    F_r((1+5r)/6)=-(r-1)(25r²-129r+8)/36<0.

Above8-3sqrt6 the refined high-rate threshold exceeds (1+sqrt(2r-1))/2. This lower bound exceeds (1+5r)/6 because

    (2r-1)-((5r-2)/3)²=-(r-1)(25r-13)/9>0.

The archived first-order curve is nondecreasing, so using dimension rate rather than degree rate only makes the target harder. Hence no such transformed growing Dickson family can have a fixed positive first-order agreement margin. This remains true if the rates tend to an endpoint: the uniform o(1) error cannot produce a fixed positive margin above a curve already dominating the envelope.

## Independent block localization is even more costly

For disjoint blocks of lengths N_i, a standard polynomial direct sum localizes block i by a factor vanishing on every other block. If the maximum degree of a difference within that block's candidate family is D_i, varying only this block forces global degree at least

    D_global >= max_i(N_total-N_i+D_i)
             = N_total-min_i(N_i-D_i).

The Cartesian list's minimum carried agreement is sum_i A_i. For Dickson blocks the deficit inequality gives

    N_total-sum_i A_i >= (5/6)sum_i(N_i-D_i)-o(N_total).

With at least two blocks, this is at least (5/3)min_i(N_i-D_i)-o(N_total). Consequently A_global-D_global<=o(N_total), uniformly even when one block is negligible. Thus the direct sum cannot have a fixed positive margin above capacity, and therefore cannot have a fixed positive first-order margin. The sum of block errors must be o(N_total), as holds when the carried list sizes in the Dickson blocks grow uniformly. Subsequent common-zero insertion and pullback preserve the sign of A-D; no-match padding does not improve it. This concerns the actual block-localized Cartesian construction, not a hypothetical more efficient correlated embedding of product lists into a univariate RS code.

## Precise remaining loophole

Coordinate padding that creates NEW simultaneous matches without a common vanishing factor is not covered. Nor is pullback allowed to silently count additional non-pulled-back candidates. The original Fourier puncturing theorem covers reused coordinates in the original prime-field domain, but not arbitrary new extension-field coordinates. To escape(E), such a step must provide a quantified positive gain either in A-3D/2 or in A-(N+5D)/6, uniformly for a growing subbank. Existing fixed-size ten/eleven-cubic padding examples demonstrate finite coincidence gains; they provide no growing-bank lemma. A coupled construction achieving such a gain is the missing mechanism, not another ordering of the operations above.
