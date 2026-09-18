# Random fresh words: growing gap at fixed dimension three

Independent audit: PASS with the endpoint-tail strengthening below. The advance is an unbounded absolute source/common-agreement gap while retaining degree two; it is not a fixed-rate or fixed-normalized-gap result.

## Construction and exact probability bounds

Retain the rational pair core with L quadratics, N₀=L(L−1), and A=2L−2. For an integer d≥2 put

    T=A+d, n=floor(T²/2)+1,
    t=n−N₀=L²+(2d−3)L+floor((d−2)²/2)+1.

Choose any t fresh field elements outside the core and zero. Set g=x³ there. Independently at each fresh x choose f(x) uniformly from the field after deleting every P_i(x) and P_i(x)−x³. There are between p−2L and p permitted values. Keep the original core f and g=0. Same-coordinate incumbent values are distinct because every pair intersection belongs to the core.

For λ≠0,1, the desired value P_i(x)−λx³ is disallowed on at most 6L fresh coordinates. Indeed, equality with P_j or P_j−x³ is a nonzero cubic equation, with respective nonzero cubic coefficients −λ and 1−λ. Put u=t−6L and

    q_−=binom(u,d) p^(−d) (1−1/(p−2L))^(t−d),
    q_+=binom(t,d) (p−2L)^(−d).

The probability incumbent i has at least d fresh matches is at least q_−: count disjoint events of exactly d matches supported on admissible coordinates. It is at most q_+ by the d-th factorial moment. For two different incumbents, their desired values differ at every fresh coordinate; any two selected d-match supports must be disjoint. Independence across coordinates therefore gives joint probability at most q_+².

If E_i denotes the qualifying event, the indicator of exactly one event is at least Σ_i 1[E_i]−2Σ_{i<j}1[E_i∩E_j]. Consequently, uniformly for λ≠0,1,

    Pr(exactly one qualifying incumbent) ≥ Lq_−−L(L−1)q_+².

No assumption of identical categorical distributions is needed.

## Excluding all fresh nonbank candidates and preserving endpoints

A nonbank quadratic has at most L core matches. For any fixed λ and such quadratic, its chance of at least s fresh matches is at most binom(t,s)/(p−2L)^s. Union-bound over at most p⁴ choices of λ and quadratic. Use **s=L−1**, not merely s=T−L: this rules out every nonbank having agreement above A, including at endpoint labels 0 and 1. The failure probability is at most

    p⁴ [ e t / ((p−2L)(L−1)) ]^(L−1).

It tends to zero in the regime below. Incumbents have exactly A endpoint matches by the blacklist, so both f and f+g have exact agreement A. Common agreement is A: a nonzero quadratic explanation of g has at most two core and three fresh matches, while the zero explanation reduces to the original core. The source change F=f,G=f+g preserves common agreement; λ↦λ/(1−λ) transfers finite bad labels to distinct nonzero challenges. The infinity word −g has zero as its unique qualifying candidate, since N₀≥T and every nonzero quadratic has at most five matches.

## Prime choice without short-interval prime estimates

Fix growing integers d and let L₀=ceil(exp(d²)). Define the increasing real function on integers

    P₀(L)=t(L,d) (8L/d!)^(1/d).

Choose a Bertrand prime between ceil(P₀(L₀)) and twice this integer. Choose L with P₀(L)≤p<P₀(L+1). Such L lies between L₀ and 2L₀ for all sufficiently large d. Adjacent P₀ values have ratio 1+O(1/L), so p/P₀(L)=1+O(1/L). In particular

    δ=Lq_+ → 1/8,  q_−/q_+ → 1.

Here d²/t→0, dL/t→0, and t/p→0. Also p≫L² log²L, so p>2a_L² for the first-L-prime core and there is ample room for all fresh nodes. The nonbank failure bound above tends to zero faster than any fixed reciprocal power of p.

The unique-incumbent probability has limit inferior at least 7/64; in particular it exceeds 1/16 eventually. Linearity of expectation and removal of the vanishing-probability nonbank failure event show that some allowed fresh word has at least p/32 singleton qualifying finite labels. No independence across different labels is asserted or needed.

Finally d~sqrt(log L), n~2L², and

    log(p/n)=d−log d+O(1)
             =(1/sqrt(2)+o(1))sqrt(log n).

Thus this yields at least n exp((1/sqrt(2)+o(1))sqrt(log n)) singleton bad challenges (with a harmless constant absorbed in the o(1)), fixed code dimension three, and source/common gap d~sqrt(log n/2). The tested threshold is strictly below Johnson because T²<2n, and above first order for all sufficiently large d because T/sqrt(n)→sqrt(2)>sqrt(3/2). The rate and normalized gap still tend to zero. This uses a nonconstructive choice of the fresh received word; it is not an explicit efficient sampler or an all-prescribed-L prime theorem.
