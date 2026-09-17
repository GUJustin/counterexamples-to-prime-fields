# Positive sparse-bank attempt: an explicit Reynolds-projected source

This note constructs a sparse bank with a forced growing stabilizer and isolates its exact remaining agreement lemma. The algebraic construction succeeds; the required fixed surplus has not been proved. Generic averaging of the known agreement bound is insufficient.

## Explicit family

Letp=4k+1 be prime, choose a divisord ofk, and writer=k/d. Sete=2k+1. Average the explicit Dickson polynomialH_a overmu_d:

 Pbar_a(X)=(1/d)Σ_{zeta∈mu_d}H_a(zeta X)=V_a(X^d),

where

 V_a(Y)=Σ_{h=0}^{r−1} binom(2k+1,2dh+1) a^{2(k−dh)}Y^h.

ThusdegV_a<r. The leading coefficient is a nonzero constant timesa^(2d), so the projected polynomials remain distinct for distincta^(2d). Restrict toa witha^(2k)=1. Then a^(2d) ranges overmu_r, and

 V_a(Y)=V_1(Y/a^(2d)).

This gives an explicit bank of exactlyr distinct polynomials, invariant under the originalmu_d subgroup before descent, on the prime-field domainmu_(4r). The received word is

 W_r(Y)=(1+Y^(2r))/2−Y^r.

Every bank member has the same agreement count withW_r by itsmu_r symmetry. Unlike merely hoping a nearest polynomial has a large stabilizer, this family has the stabilizer by construction.

## Precise sufficient lemma for a prime-ambient theorem

It would suffice to prove: for an unbounded sequence of prime r and primep=4dr+1, withr→∞ andd→∞, the explicitV_1 agrees withW_r on at least(1+eta)r coordinates, for one fixedeta>0.

Why this alone suffices: a true nearest polynomial ofdegree<r then has agreementM>r. The word takes four distinct constant values on the fourmu_r cosets, each ofsize r; a constant polynomial matches at mostr coordinates. Thus every nearest polynomial is nonconstant. Since r is prime, itsmu_r orbit has exactlyr members. This is a TRUE nearest bank withN=4r,K=r,M−K≥eta r andp/r=4d+1/r→∞. The existing prime-field random-direction compiler then yields exact rate1/8, a capacity gap bounded below byeta/8, and superlinearly many ordinary-CA exceptions. An exactly constant gap would require an additional valid normalization; p/r→infinity alone does not guarantee the field-size hypothesis of the strongest same-field common-zero padding lemma.

This avoids needing to prove thatV_1 itself is nearest. It also does not assume Dirichlet controls the nearest orbit: prime r and the explicit surplus supply the orbit size directly. The missing condition is the displayed agreement estimate along a suitable sequence, not the elementary existence of primes in a progression for each fixedr.

## Exact character identities governing the missing agreement

Choose s withs²=x, and leta=1 for the base candidate. Before subtractingX^k, the averaged polynomial has the root-of-unity-filter expression

 Gbar_a(x)=1/(2d s) Σ_{eta∈mu_(2d)} eta^(-1)(a+eta s)^e.

It agrees with the target exactly whenGbar_a(x)=(1+x^(2k))/2.

For squarex, s∈Fp, Euler's criterion gives the explicit condition

 a Σ_eta eta^(-1)chi(a+eta s)+s Σ_eta chi(a+eta s)=2d s.

For nonsquarex, take s∈Fp² withs^p=−s. PutQ_eta=(a+eta s)^e. Then

 Q_eta²=a²−eta²x,  Q_eta^p=Q_(-eta),

and agreement is exactlyΣ_eta eta^(-1)Q_eta=0. These identities are valid, but they are sums across2d translates, not the two-translate identities used by the original Dickson count. Requiring every paired contribution to vanish gives an intersection of roughlyd quadratic-character conditions; that sufficient event does not provide a constant agreement density asd grows. A useful proof would need substantial structured cancellation beyond those simultaneous individual events.

## Why the old agreement bound does not pass through averaging

There are4r fibers of sized in the original domain. If an original candidate hasM matches, the number of fibers on which it matches everywhere is at least

 max(0,M−4r(d−1)).

Only those complete fibers are automatically preserved by averaging. The known source boundsM≤2k=2dr make this guaranteed count zero for everyd≥2. Averaging may create other matches through cancellation; the exact character identities above describe that additional mechanism. It cannot be justified by the original lower boundM≥3k/2 alone.

## Attempt outcome and stopping condition

The Reynolds family is an actual sparse, rationally compressible bank and escapes the full-bank rational-descent obstruction. It supplies exactly the right list size and field/length tradeoff if the stated surplus lemma holds. No proof of that lemma emerged from the available character identities, and no experiment or prime subsequence is being presented as evidence of it. A next investigation should target these explicit sums, or produce an upper bound excluding their linear surplus, rather than repeat the full-field Dickson calculation.

The companion low-exponent norm-torus family considered independently by the other agent has a related warning: degree-r monic polynomialsG_a splitting on translated root sets yield onlyr matches for candidatesG_a−X^r ofdimensionr. A large bank exactly at capacity is not enough; an additional linear number of matches or a valid dimension reduction remains necessary.
