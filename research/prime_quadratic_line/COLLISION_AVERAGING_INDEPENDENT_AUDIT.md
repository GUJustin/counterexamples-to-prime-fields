# Collision averaging: independent audit

Keep the original core and fresh prescription f=X⁴, g=X³. Write N₀=L(L−1), t=N₀+1, A=2L−2 and T=A+1. Assume p>2Q, so the distinct rational core reduces faithfully. Delete the core, zero, and all points where any incumbent label

    φ_i(x)=(P_i(x)−x⁴)/x³

equals 0 or 1. The remaining set S has size m≥p−N₀−1−8L. Labels at a single allowed coordinate are pairwise distinct, because P_i(x)=P_j(x) only on the core.

For fixed x∈S and indices i,j, the equation φ_j(y)=φ_i(x) has at most four solutions y: after clearing y³ its leading coefficient is −1. Therefore the total number of unordered colliding incidence pairs with distinct coordinates in S is at most 2mL². This bound safely includes some forbidden diagonal solutions before dividing the symmetric ordered count by two.

Choose a uniform t-element subset of S. Each distinct coordinate pair is selected with probability t(t−1)/(m(m−1)). Consequently the expected number C of unordered collisions is at most

    2L²t(t−1)/(m−1).

If m−1≥8Lt, this is strictly less than Lt/4. Some subset therefore has C<Lt/4. A label of incidence multiplicity r≥2 accounts for r≤2 binom(r,2) nonsingleton incidences. Thus this subset has more than Lt−2C>Lt/2 singleton labels.

Each singleton label has precisely one incumbent attaining T and no other candidate attaining T: a nonbank quadratic has at most L core matches and four fresh matches, hence at most A for L≥6. Both endpoint labels 0 and 1 remain at agreement A by the blacklist. The source common-agreement bound and the source change F=f,G=f+g are unchanged. The singleton labels remain distinct nonzero bad challenges under λ↦λ/(1−λ). The infinity challenge adds a singleton list as before. Other finite bad labels may have multiple threshold candidates: the universal-singleton assertion from the collision-free construction must not be retained.

A sufficient explicit field condition is

    p>2Q,  p≥N₀+8L+2+8Lt.

This gives p=Θ(L³) once Q=o(L³). For first-L-prime parameters, the standard estimate a_L=O(L log L) implies this condition eventually. More concretely let R=N₀+8L+2+8Lt. When 2Q≤R, a prime R<p<2R satisfies all conditions. For L≥6, R≤9Lt, so the singleton challenge count is greater than p/36. This is a constant-density prime-field conclusion. It retains the original n=2L(L−1)+1, T²=2n−1 and the previously audited first-order crossing for L≥25.

No numerical pilot is needed for the existence assertion. A pilot can provide explicit small-field instances or derandomize the selection, but it is separate from the averaging proof.

## Stronger density when singleton lists are not required

Let B=Lt. Cauchy on label multiplicities yields, for a subset attaining the collision expectation,

    M_distinct ≥ B²/(B+2C) ≥ B/[1+4L(t−1)/(m−1)].

A sharper bound uses only the degree-four fiber bound. Each label occurs at r_λ≤4L coordinates of S, and Σ_λ r_λ=mL. For m≥4L the probability that a uniform t-subset hits a support of size r is

    h(r)=1−binom(m−r,t)/binom(m,t).

This is discretely concave with h(0)=0, since its successive differences are binom(m−r−1,t−1)/binom(m,t). Consequently h(r)≥r h(4L)/(4L), and some fresh subset has

    M_distinct ≥ (m/4)[1−binom(m−4L,t)/binom(m,t)]
               ≥ (m/4)[1−exp(−4Lt/m)].

The binomial numerator is interpreted as zero if m−4L<t. For p/B→c>0 and m/p→1, this gives bad-label fraction at least (1−exp(−4/c))/4−o(1). In particular c=1 gives approximately 0.24542. For p/B→0 while p≫L², the fraction approaches 1/4. These statements do not guarantee singleton lists, and optimizing them may reduce the absolute number of challenges compared with the p=Θ(L³) regime.
