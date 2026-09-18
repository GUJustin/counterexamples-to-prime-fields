# Pooled elliptic padding: identical collision envelope

The pooled argument applies to any good prime-field realization of the elliptic triple core. Write B for the bank size, t=(B²−10B+30)/6 for the fresh-domain size, and K=Bt for the number of incumbent/fresh incidences (K here is not code dimension). Delete zero, every pairwise bank intersection, and nodes giving any label 0 or 1. The remaining set has

    m ≥ p−B(B−1)−1−8B.

Same-coordinate label collisions are impossible on this set. Every prescribed label equation remains a nonzero quartic. For a uniform t-subset, the collision expectation and resulting incidence-singleton bound are therefore unchanged:

    E[C] ≤ 2B²t(t−1)/(m−1),
    S_single ≥ Bt−4B²t(t−1)/(m−1)

for at least one subset. Each singleton label gives a singleton threshold list by the already proved nonbank exclusion. The source common agreement, far endpoints and infinity conclusions persist.

Conditionally on realizations with p/K→c>4, one has m/p→1 and

    liminf S_single/p ≥ (c−4)/c².

This envelope is maximized at c=8, with value 1/16. It is exactly the same envelope as for the pair core; it is not an improvement due to triples. The simpler sufficient condition m−1≥8Bt yields more than Bt/2 incidence-singleton labels. The previously stated p/36 guarantee for rational pair cores includes a conservative prime-selection loss; comparing it directly with 1/16 would conflate this loss with an improvement in the core.

At fixed n, the triple core increases K/n^(3/2) by 4/3. It also increases the preferred p/n^(3/2) at c=8 by 4/3, so the normalized probability is unchanged. The all-bad-label hypergeometric envelope likewise stays (1−exp(−4/c))/4.

Most importantly, the elliptic proof currently obtains realizations only at sufficiently large completely split primes in a B-dependent number field. It gives no p=Θ(Bt) guarantee. Consequently the conditional constant-probability regimes above are not established elliptic families. The unconditional contribution remains the improved bad-count constant on infinitely many splitting primes. No fixed-rate or growing normalized-gap progress follows from this pooled extension.
