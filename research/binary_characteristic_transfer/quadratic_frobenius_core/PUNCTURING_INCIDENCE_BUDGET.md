# Rich-line budget for structured puncturing

September 18, 2026. Independent elementary counting; a necessary bound, not a new construction.

Identify B=F_(p²) with the affine plane F_p². Retain square-lifted coordinates over a set Y⊂B of size m. A canonical witness's core matches are twice the number of Y-points on one affine F_p-line. Suppose both scaled active blocks use Y, and select only witness-label pairs whose underlying line in EACH block has at least t points. For each direction a let R_a count its t-rich affine lines. Intercepts in the two copies determine the label b−eta*v, so the number of these candidate pairs is at most sum_a R_a². Excluding zero intercepts only reduces the count.

There are p(p+1) affine lines. If r_l=|Y∩l|, exact point and ordered-pair counts give

    sum_l r_l = (p+1)m,
    sum_l r_l² = m²+pm,
    sum_l (r_l−m/p)² = pm−m²/p.

Consequently, when t>m/p,

    sum_a R_a <= (pm−m²/p)/(t−m/p)².

Lines of one direction are disjoint, so R_a<=floor(m/t). Therefore

    sum_a R_a² <= floor(m/t) (pm−m²/p)/(t−m/p)².

For m=o(p²) and t>=c sqrt(m), with fixed c>0, this is O_c(p sqrt(m)). In particular, if m=p^gamma with 1<gamma<2, the candidate population is at most O(m^(1/2+1/gamma)), strictly below m^(3/2). This does not exclude a superlinear population; the displayed exponent is still greater than one. It shows that puncturing cannot retain BOTH the full n^(3/2) population and square-root support on both blocks in this range.

Scope: this bounds only the pairs where BOTH block supports reach t. A total-agreement threshold alone does not imply that condition; a highly unbalanced pair may evade this ledger. A source-to-threshold gap comparable to sqrt(m), together with a matching O(sqrt(m)) upper bound on individual block agreement, can force each block's contribution to be substantial, but that must be checked for the proposed puncture. Likewise, the original noncanonical bound p need not be small enough after puncturing; a new bound for the retained coordinates is required. No generic obstruction to higher characteristic or to arbitrary Reed–Solomon lines is claimed.

The full-plane construction has m≈p² and t≈p, where t−m/p is small; this estimate deliberately provides no competing bound there. Its large rich-line population is consistent with the exact variance identity.
