# Independent constructive audit: full-domain padding while characteristic grows

Verdict: PASS as a common-agreement/native-label theorem, with explicit individual-source limitations. The binary repository was read only: `AGENTS.md`, the strategy/status documents, the final corollary and fixed-characteristic remark of `sections/constructions/quadratic-near-johnson.tex`, and the Artin–Schreier comparison in `research/frontier/characteristic-and-domains.md`. Nothing in that repository was edited.

This is a uniform growing-p consequence of the archived p-linear locator compiler plus a different padding choice; it should not be presented as a newly invented locator compiler.

## Parameters and compiler input

Fix integers s>=2, d>=s+2 and a rate 0<rho<1. Let D be an F_p-linear domain of size N=p^d in a field F of size q, let t=p^(d−s), K0=t/p², and J=floor(rho N). The existing elimination uses every codimension-s subspace W of D. Its fixed seed pair has direction g0=X^(pK0−1), and at affine label z_W it has a witness of degree at most K0−1, agreeing on W\{0}.

The label functions of the s−1 free head parameters are distinct affine functions. The archived triangular recovery still applies with d,s fixed and p varying: it recovers the first s locator coefficients; if these already exhaust the locator there is nothing more to prove, and otherwise their difference degree is smaller than the minimum intersection size of two codimension-s subspaces. Missing lower coefficients may be read as zero. Thus two different subspaces collide with probability at most 1/q. No hidden constant depending exponentially on p is needed in this algebraic assertion.

The number of subspaces is M=[d choose s]_p. For fixed d,s,

 p^(s(d−s)) < M <=2^s p^(s(d−s)).

Each factor in the Gaussian product is strictly larger than its leading power, proving the lower inequality; bounding each denominator factor below by 1/2 proves the upper one.

## One padding set for every subspace

Put w=J−pK0+1. For sufficiently large p, 0<=w<=N. In fact w<=rho N because pK0>=1. Choose B uniformly from all w-subsets of D. For each fixed W, |B intersect W| is hypergeometric with mean wt/N<=rho t. A standard without-replacement Chernoff bound gives

 Pr[|B intersect W|>(rho+epsilon)t] <= exp(−2epsilon² t).

One elementary justification is that its binomial moments satisfy E binom(X,k)=binom(t,k)(w)_k/(N)_k<=binom(t,k)(w/N)^k, so its exponential moment is bounded by the corresponding binomial moment; the usual Bernoulli Chernoff/Hoeffding calculation then applies.

Hence it suffices that

 2^s p^(s(d−s)) exp(−2epsilon² p^(d−s)) <1.

This holds for all sufficiently large p because d−s>=2. Thus there exists one B of the exact required size with |B intersect W|<=(rho+epsilon)t for ALL W simultaneously. B can be chosen before the head parameters are selected, since this condition depends only on subspaces, not on labels or extra seed agreements.

## Degrees, zero coordinate and agreement

Multiply both seed sources and every witness by the monic locator L_B. The new direction is monic of degree exactly J. Every witness has degree at most

 w+K0−1=J−(p−1)K0<J,

so the original strict code dimension J is preserved.

The guaranteed matching set is B union (W\{0}). Its size is exactly

 w+t−1−|B intersect W|+1_{0 in B}
 >=J+t−pK0−|B intersect W|.

Therefore zero causes no loss beyond the stated formula; including it in B only improves the estimate. Extra old matches likewise help. Every retained label has agreement at least

 J+(1−rho−epsilon−1/p)t.

Taking epsilon=(1−rho)/4 and p>=4/(1−rho) gives a gap at least (1−rho)t/2. Integer thresholds can be obtained by flooring this last positive margin.

Since the direction is monic of degree J, its agreement with every strict degree-<J codeword is at most J. Interpolation on any J domain coordinates attains J both individually for the direction and simultaneously for the pair. Thus agr_J(g)=CA_J(f,g)=J exactly. This does NOT prove agr_J(f)=J. In the all-native-label specialization, lambda=0 is near, so f must itself be close at the advertised larger threshold. No both-far native statement is possible for that same all-label pair.

## Pooling and native specializations

The fixed padding does not change the affine label functions. Pairwise collision probability at most 1/q and the usual second-moment pooling give a parameter choice with at least ceil(qM/(q+M−1)) distinct labels. Each label has at least one strict witness; no distinctness of witnesses across colliding labels is needed. Zero is allowed. For a nonzero-label statement subtract at most one. If M>(q−1)², the ceiling equals q and every label, including zero, occurs.

For D=F_{p^8}, d=8,s=4, q=N=p^8 and M=[8 choose4]_p>p^16=q². Thus every native challenge is near; characteristic is N^(1/8), and the guaranteed common-agreement gap is Theta(p^4)=Theta(sqrt(N)).

For D=F_{p^4}, d=4,s=2, q=N=p^4 and

 M=(p²+1)(p²+p+1)>q.

The native label count is strictly larger than q/2 and asymptotic to q/2 under this pooling bound. Characteristic is N^(1/4), with the same Theta(sqrt(N)) common-agreement gap. No claim of completeness or an upper bound on other labels is made.

Both statements hold at every fixed rho in (0,1), for sufficiently large p depending on rho,d,s, on the full native field domain. More generally the same padding and harmonic count work on any size-p^d linear domain in a containing field, with q retained in the count.

## Matched significance and limitations

This supplies fixed-rate examples with growing characteristic and constant or perfect native failure probability. The normalized gap is Theta(p^−s), not a fixed positive number. It remains below the fixed-rate first-order boundary asymptotically, and p<J for large p; it therefore does not contradict the DKT large-characteristic guard or its above-curve theorem.

The archived packet result has p=Theta(n/log n), gap Theta(n/log n), challenge field p^4, and only an Omega(1/n) guaranteed bad fraction. It is not dominated: it has much faster characteristic growth and a larger coordinate gap. The present transfer instead gives native q=N and constant/perfect failure, at characteristic N^(1/4) or N^(1/8). These are distinct matched tradeoffs; the old packet count q/(4n) alone does not subsume the new native-probability guarantees.

Proper-extension source conversion could restore two individually far sources using the archived theorem, but changes the alphabet/probability contract. It is not part of the native statements above. No protocol consequence, explicit deterministic padding algorithm, or independent novelty priority is asserted.
