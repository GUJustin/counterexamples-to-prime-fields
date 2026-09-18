# Independent audit: fixed interior square-root-scale list threshold

PASS. This changes only the norm-one direct-list threshold, not any far-source line theorem. Construction and exact list classification are independently proved in `NORM_ONE_DIRECT_LIST_INDEPENDENT_REVIEW.md`.

Let p>=53 be prime, N=2(p²+p+1), and T=ceil(19p/10). Use the same E=Fp³ norm-one doubled domain and received word. The exact list is N/2 because p+1<T<=2p+2, while every outsider has at most p+1 agreements.

## Finite first-order support

Take m=6, derivative cap 3, B=3T and H=40B. The primary Eq. (61) coefficient count is G=4B²−2B and Eq. (62) local rank is R=62. Since 57p/10<=B<=6p,

 39G−40NR >= (2711/25)p²−5428p−4960 >0.

The polynomial is positive at 53 and increasing thereafter (its derivative is 5422p/25−5428>0). This also implies G>NR. Therefore the conservative graded surplus

 (H−B+1)G−(H+1)NR = B(39G−40NR)+(G−NR)

is strictly positive. The finite-characteristic counting guard p>max(2,3) is satisfied. Exact onset replay at p=53 gives N=5726,T=101,B=303,G=366630, NR=355012, inner margin98090 and graded margin29732888. The conservative inner-margin polynomial equals 299099/25 at p=53.

Lemma 5.6, Eq. (56), with D=2,M=3 yields the same all-word list bound

 floor[((N−2)/(T−2))(21T−12)+15T−9].

Here T−2>=p+1, so lambda=(N−2)/(T−2)<=2p, and T<=2p. The bound is at most 21N+90p−51<=22N for p>=53. This is uniform over all received words and all size-N evaluation domains, whereas exact N/2 is specific to the constructed word. No common-agreement or source hypothesis is used.

## Strictly between both agreement boundaries

The primary low-rate curve estimate gives

 N a1(3/N) <= sqrt(3N/2)+(3N/8)^(1/4) < 7p/4+sqrt(p) <19p/10<=T.

For the first strict inequality, sqrt(3N/2)<7p/4 follows from p²/16−3p−3>0, and (3N/8)^(1/4)<sqrt(p) follows from p²−3p−3>0. The second strict inequality uses sqrt(p)>20/3. All hold at p>=53, where the low-rate branch applies.

Also T<=19p/10+1, and

 2N−(19p/10+1)² =39p²/100+p/5+3>0.

Thus T is strictly below exact Johnson agreement sqrt(2N).

As p grows,

 T/sqrt(N) ->19/(10sqrt(2)),
 (N a1(3/N))/sqrt(N) ->sqrt(3/2),
 sqrt(2N)/sqrt(N)=sqrt(2).

The middle threshold constant is strictly between the two boundaries, by fixed positive distances. This is a stronger presentation than a threshold asymptotic to Johnson. It remains a vanishing-rate (K=3) extension-field statement: T/N tends to zero, so it is not fixed normalized agreement or fixed-rate tightness. It establishes the matched finite comparison N/2<=maximum list size at T<=22N with an interior square-root-scale threshold.


## Immediate corollary for the core-punctured far line (N.22)

PASS, with its original onset p>=4099. This is a separate consequence for the existing far-line theorem and does not replace its stronger original threshold. Its retained length satisfies

 2p²−2p−1<=n<=2p²−p−1.

Put T0=ceil(19p/10) and retain the original threshold Tfar=2p−ceil(4sqrt(p))−4. For p>=4099,

 p+2sqrt(p)<T0<=Tfar.

The lower inequality follows from (9/10)p>2sqrt(p). For the upper one, T0<=19p/10+1 and Tfar>=2p−4sqrt(p)−5; it suffices that p/10>=4sqrt(p)+6. This holds at 4099 and remains true thereafter (put y=sqrt(p), so y²/10−4y−6 is increasing for y>20).

The full classification already shows that every outsider and every far-coset word has agreement at most p+2sqrt(p), while every listed near witness retains at least Tfar. Therefore lowering the threshold to T0 changes no list at any parameter. The exact profile remains p³−2p singleton parameters, p parameters with lists of size p, and p empty parameters. Thus the near probability is exactly 1−p^(−2) and singleton probability exactly 1−2p^(−2) for a uniform E-valued affine challenge. The p collinear inputs in the punctured coset remain far, with gap at least (9/10)p−2sqrt(p). The earlier distinction remains: F_p-valued affine weights stay in the far coset and do not have this near probability.

For the actual punctured n, the same first-order estimate is smaller than 7p/4+sqrt(p)<T0. Exact Johnson remains above T0, since

 2n−T0² >=39p²/100−39p/5−3>0

at this onset. Since n~2p², both distances, T0−n a1(3/n) and sqrt(2n)−T0, are positive constant multiples of sqrt(n) asymptotically. This is not a fixed normalized-agreement margin or fixed-rate claim.

The uniform finite certificate also transfers immediately: the norm-one certificate above used the larger length N=2(p²+p+1), and reducing the number of coordinates only reduces its interpolation constraints. Its all-word list bound is still at most 22n when evaluated at n: lambda=(n−2)/(T0−2)<=2p gives 21n+90p−51<=22n for p>=4099, using n>=2p²−2p−1. No received-word-specific interpolation assumption is introduced. No manuscript edit is part of this audit.
