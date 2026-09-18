# Crites–Stewart subsumes the existential native d5 exact-CA guarantee

2026-09-18. **Definitive verdict: yes, asymptotically at matched full domain, alphabet, dimension, exact common agreement, and direction agreement.** The explicit algebraic witnesses and the old theorem's particular finite onset are not supplied by this application.

## Exact application

Let E=F_(p^5), q=p^5, D=E, n=q, 0<ρ<1 fixed, and J=floor(ρq). Use the strict-degree-J RS code. Choose the prescribed direction g(X)=X^J. For every h of degree<J, g−h is monic degree J, so agr(g)≤J; interpolation on any J distinct coordinates gives the reverse inequality. Therefore agr(g)=J.

For ANY first word u, CA(u,g)≤agr(g)=J. Interpolate u and g separately on an arbitrary common set of J coordinates to obtain CA(u,g)≥J. Hence CA(u,g)=J independently of how u is chosen.

Fix 0<c<h(ρ), where h is binary entropy with natural logarithms. Define

    T = J + floor(c q/log q),     f_rad=q−T.

For all sufficiently large p, Crites–Stewart Corollary 1 applies with k=J, n=q and this prescribed g. It gives a first word u such that

    agr(u+λg)≥T for EVERY λ∈E,
    agr(g)=CA(u,g)=J.

The far-direction hypothesis holds strictly: distance(g,C)=q−J>q−T=f_rad. The lower entropy condition follows from

    q(1−H_q(f_rad/q))
      =J−(h(ρ)−c+o(1))q/log q,

while its extra term 2+sqrt(qH_q(f_rad/q)−f_rad) is O(sqrt(q/log q)). The upper condition J≤q−f_rad−2 is T−J≥2, which also holds eventually.

Thus at the exact same q=p^5, D=E and J, this gives all q near labels with gap Θ(q/log q), larger than the old internally padded d5 native guarantee Θ(p^3)=Θ(q^(3/5)). It preserves exact common agreement J and exact direction agreement J. Its first source is near (λ=0), just as the old native guarantee. The old result should be positioned as an explicit algebraic realization with specified witnesses/finite hypotheses, not a new existential count or parameter regime. Comparison of a particular small prime still needs the explicit entropy inequality; this is not a blanket finite-onset domination claim.

## Primary conventions and proof caveats

Primary source: Crites–Stewart, ePrint 2025/2046, Section 2 defines RS(F,D,k) using polynomials of degree at most k−1 and unnormalized Hamming distance. Corollary 1 explicitly permits any prescribed u1 farther than the chosen radius. Local files: `tmp/cs_novelty_audit/cs.pdf` and `.txt`; strict-degree definitions at extracted lines 200–207, corollary at 671–685.

Their subsequent proof contains an incorrect/loose minimum-separation expression for RS(k+1), and the extracted Theorem 1 also has apparent count/probability typographical issues. Neither affects the application: the exact far-direction hypothesis is proved directly above, and the underlying random-word argument is independent of the direction. If the fraction of near words exceeds 1−1/q, then for fixed g a uniformly random u has expected fewer than one failing affine label. Some u has none. This is precisely the corollary's use of its preceding random-word bound.

## What this does not subsume

Theorem 1 fixes the far direction and randomizes the affine center. It does not fix a far center, and Corollary 1 actually makes that center near. The exact all-near affine line has only its projective direction far at that threshold, so an invertible line reparametrization cannot supply two far sources. No direct two-far conclusion follows from this result. Conditioning the random center to be far would invalidate the unconditional random-word argument unless separately analyzed.

Accordingly the norm compiler's two-far profile remains a distinct feature not obtained by this immediate application. Its novelty is not established merely by this distinction; its ordinary CA is also larger, J+m−1.
