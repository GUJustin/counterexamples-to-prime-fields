# Independent OR-tensor audit and low-density boundary

Status: PASS for the full Cartesian theorem and the fixed-density correlated-family closure. The hypotheses concern distinct realized polynomials, a common received word, and the specified carried OR agreements. They are not consequences of having a tuple-label set alone.

## Exact hypotheses and inequalities

For two tuples differing only in coordinate i, the cylinders from the other coordinates are common matches. Their cardinality is N times one minus the product of the other complement densities. Distinct candidate polynomials make their difference nonzero, so the degree root bound applies under any embedding into N distinct field nodes. If the two supports in coordinate i intersect in C_i points, the additional common matches on the complement of the other cylinders have size C_i times the other complement sizes. These give exactly inequalities (1) and (2).

For densities below one, writing odds t_i=a_i/(1-a_i) makes the maximum-minimum optimization immediate; t/(1+t)^B is maximized at 1/(B-1). Degenerate density-one cases also give zero for B>=2 by choosing a different coordinate. Thus the 1/B bound holds even when inner degrees, lengths, and densities vary. Actual dimension rate (D+1)/N is at least the degree rate and only strengthens it.

The bound is on carried threshold a. Extra agreements could increase the true minimum agreement, and are not covered by the full-Cartesian carried-threshold statement alone. Collapsed tuple labels also invalidate the argument unless enough distinct represented pairs remain. Arbitrary realization, moving nodes, and nonlinear coefficient formulas do not invalidate it: the proof is entirely incidence and polynomial root counting.

For arbitrary correlated tuples s,t, put F=product_i(1-a_i) and c_i=|S_(i,s_i) intersect S_(i,t_i)|/n_i. Their common OR set has fraction

    1-2F+product_i(1-2a_i+c_i).

Thus any two distinct realized members force D/N>=1-2F, and carried gap at most F. Even an actual higher threshold has gap at most 2F because its fraction is at most one. Therefore fixed positive inner density with an unbounded number of factors excludes a fixed gap for every correlated family containing two distinct polynomials. The precise sufficient condition is F→0, equivalently sum_i -log(1-a_i)→infinity. No exponential list-size hypothesis is required for this closure.

The CRT product degree formula is also correct when h_i strictly exceeds every inner candidate degree. For a pair realizing the maximum difference degree d_i, the unchanged discrepancy factors have exact degrees h_j N/n_j, so no top cancellation is possible in that pair difference. Reduction modulo the domain locator is a different realization; the incidence bound still applies. A candidate-dependent normalization that destroys the original OR matches is not covered merely by calling it a normalization.

## Low-density correlated families are a real remaining logical exception

If a_i is asymptotic to lambda/B, then F→exp(-lambda), not zero. The full Cartesian family is still excluded by the 1/B theorem, but a correlated family need not contain pairs differing in one coordinate. Neither fixed-density closure nor the general pair-root bound automatically excludes a first-order margin in this regime.

A concrete limiting incidence model makes this distinction quantitative. Give each coordinate q=8 labels with pairwise disjoint inner supports of density a_B, where B*a_B→log 2. Such support data are possible once B is large; the unassigned positions are simply outside all eight supports. For two outer tuples at relative Hamming distance delta, their common OR fraction tends to

    1-2*(1/2)+exp(-(1+delta)*log 2) = 2^(-(1+delta)).

Eight-ary outer codes can have positive rate and relative distance 17/20, since 17/20<7/8 and the Gilbert bound is positive there. Their carried agreement tends to 1/2, and the largest prescribed pair intersection is at most 2^(-37/20), which is less than 7/25. At degree rate rho=7/25, the audited high-branch first-order polynomial evaluates to

    (8-rho)*(1/2)^2-6*rho*(1/2)+rho*(4*rho-5)
      = 9/2500 > 0.

Consequently agreement 1/2 is strictly above the first-order threshold at that rate. The incidence pair bound permits this numerical window; it does not prove polynomial realizability. Rational densities a_B can approximate log(2)/B with error o(1/B), so no irrational finite support sizes are required.

This example is NOT a construction. It specifies the missing algebraic task precisely: realize an exponentially large correlated outer code's overlapping OR sets by distinct degree-at-most-(7/25)N univariate polynomials with one word on N distinct nodes. The ordinary CRT product formula does not supply such a realization, and pair-count feasibility is far weaker than the required simultaneous interpolation identities.

The existing rational eight/ten/eleven banks do not automatically instantiate the disjoint-support model: some inner pairs share three of their seven matches. Merely diluting those fixed banks leaves these relative overlaps, so substituting their density into the disjoint-support computation would be incorrect. A useful next positive direction needs both an appropriate low-overlap inner incidence system and a concrete algebraic realization of its correlated outer code. No new finite scan is warranted by the incidence calculation alone.
