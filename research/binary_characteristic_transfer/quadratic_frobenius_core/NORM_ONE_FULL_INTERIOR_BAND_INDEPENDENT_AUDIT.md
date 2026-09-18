# Independent audit: uniform linear list bound through the interior band

Verdict: PASS. Independently checked the support from primary Eq. (61)–(63), Proposition 5.10, and Lemma 5.6 Eq. (54),(56) in `tmp/eprint-2056/paper.txt`, together with the exact norm-one classification. No main-paper edits.

Let p>=401, N=2(p²+p+1), K=3, and let the integer threshold satisfy

 ceil(sqrt(3)*p)<=T<=2p+2.

The norm-one received word has exactly N/2 witnesses at every such threshold, since T>p+1 and its only agreements above p+1 are the N/2 bank members at 2p+2.

## Exact finite support

Use multiplicity m=16, derivative cap M=8, total jet cap B=8T and challenge cap H=100B. Message degree is D=2. Thus mT=2B, with strict weighted-degree bound below mT, as required by the primary support. Direct summation of Eq. (61) gives

 G=sum_(t=0)^B sum_(b=0)^min(t,8)(2B−2t+b)
  =9B²−27B=576T²−216T.

Terms are nonnegative; zero contributes nothing. The Eq. (62) rank blocks for s=0,...,15 are exactly

 [9,18,27,36,45,54,63,72,80,84,84,80,72,60,44,24],

whose sum is R=852. The degree cutoff is inactive for these nonzero blocks: t<=s+8 and s<=15, whereas B is already at least 5560. Independently replayed both primary sums at p=401,4099 and both band endpoints, without substituting the claimed formulas into the summation.

Since T²>=3p² and T<=2p+2,

 99G−100NR >=672p²−213168p−213168.

This polynomial is positive at p=401 and increasing thereafter. In particular G>NR. Bounding column challenge budgets below by H−B+1 and row budgets above by H+1 gives the strictly positive finite graded surplus

 (H−B+1)G−(H+1)NR
 =B(99G−100NR)+(G−NR)>0.

Thus the finite primary certificate is valid uniformly over words and domains. Its counting characteristic guard is p>max(D,M)=8, amply satisfied; no restriction p>B or p>H is introduced.

For the smallest tested endpoint p=401,T=695, N=322406, B=5560, G=278072280 and 99G−100NR=60164520. These are exact integers.

## Uniform counting transfer

In Eq. (54), tau=1,u=B,v=9. Hence

 Freg=Bv+8(u−v)=17B−72,
 S=max(B,15B−64)=15B−64.

With lambda=(N−2)/(T−2), Eq. (56) bounds every received word's list by

 floor[lambda(136T−72)+120T−64]
 =floor[136N+200lambda+120T−336].

The lower band endpoint ensures T−2>=p+1, and N−2=2p(p+1), so lambda<=2p. The upper endpoint gives

 list size <=136N+640p−96<=137N,

where N−640p+96=2p²−638p+98>0 for p>=401. This uses the fixed-word part of the counting lemma, not an assumed uniform bound on special fibers of one symbolic interpolant. The challenge certificate is stronger than necessary for fixed words but valid.

Consequently, throughout this integer band,

 N/2 <= maximum quadratic list size at threshold T <=137N.

The lower bound is attained by the specified norm word, whose own list is exactly N/2; the upper bound is uniform over all words and all evaluation sets of size N.

## Interior asymptotics: exact scope

The entire integer band is NOT asserted to lie between the first-order curve and Johnson. Its lowest end can lie below the finite first-order curve, and 2p+2 lies above exact Johnson. These facts do not affect the uniform list statement.

For any FIXED c in (sqrt(3),2), take T=ceil(cp). Eventually this is in the band and above the first-order curve. Indeed the primary low-rate estimate gives

 N a1(3/N)<=sqrt(3N/2)+(3N/8)^(1/4)
           <=sqrt(3)*p+sqrt(3)+sqrt(p)

for sufficiently large p, so the fixed positive coefficient c−sqrt(3) dominates the lower-order terms. Also T<=cp+1 and

 2N−(cp+1)²=(4−c²)p²+(4−2c)p+3>0,

so this fixed-c threshold is below exact Johnson. Both agreement distances are Theta(p)=Theta(sqrt(N)). Equivalently T/sqrt(N) tends to c/sqrt(2), strictly between sqrt(3/2) and sqrt(2).

This establishes matched Theta(N) list size throughout every fixed interior square-root-scale position, with a common explicit factor-274 comparison. It does not establish fixed-rate tightness, a fixed normalized-agreement gap, or a prime-alphabet theorem: K=3, normalized rate and agreement vanish, and the construction uses F_{p³}. The existing far-line theorem is not changed by this audit.
