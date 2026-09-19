# Independent audit: residual discriminant for linear multiplicities 13–16

September 19, 2026. **PASS**, within the stated binding-shape and nonzero-discriminant assumptions. This audit checks the proof and independently replays the exact arithmetic certificate; it does not assert existence of a global polynomial with the displayed profiles.

## Local and global inequalities

The real convex function phi(s)=max(0,s/2,s−12), rather than the rounded coefficient bound, is the correct Newton-polygon lower envelope. Graph translation by a t-divisible series preserves the contact filtration. At nongraph coordinates the graph factor has a unit constant term, so its Newton polygon contains (0,0); the product polygon therefore contains the residual polygon. These give NP_H(j)≥phi(b−j), with b=max(a−e,0) on the graph and b=a off it.

At a good coordinate the leading coefficient is a unit, and all root valuations are nonnegative. The root-difference inequality and Newton slopes give ord Disc(H)≥2 sum_{j=1}^{h−1} NP_H(j). Consequently the exact lower cost is D(b)=binom(b,2)+binom(max(b−24,0),2). This does not assume cancellation is absent: cancellation can only increase discriminant valuation. Squarefreeness is required to obtain a finite global discriminant budget.

Weighted homogeneity gives deg_X Disc(H)≤h(h−1)w+24(h−1): the discriminant has coefficient degree 2h−2 and weighted degree h(h−1), and each H_j has degree at most (h−j)w+12. Global monicity is unnecessary. Only the retained good nodes need a unit leading coefficient. Translation in Y preserves the discriminant.

The explicit local models have exactly the claimed costs. For s=b−24, their discriminant valuation is 12+4 binom(12,2)+24s+2 binom(s,2)=D(b). The benchmark characteristic is odd and exceeds all constants in these factors, so they are distinct and separable. Adding the unit root for contact h−1 adds no discriminant valuation. The unit leading term establishes exact contact even in the finite characteristic. These models establish local sharpness, not global compatibility with coefficient degree bounds.

## Exact replay and scope

Replayed `python3 research/better_codes_kernel_base_factors/linear13_16_residual_discriminant.py` successfully. Moving respectively 44584 and 10852 graph nodes from contact 43 to 42 repairs the e=13 and e=14 discriminant overruns. The four discriminant slacks are 4, 20, 559218, and 1203534. Every profile has 262144 nodes, no bad nodes, and passes the stronger full own-system rank requirement C−1=6802316684344.

All centered-coefficient budgets and the full graph-power helper range q=0,...,55 pass. The minimum helper excesses above the own-system cap are respectively 182564, 156296, 107148, and 47148. The common graph count 202144 stays below the routing threshold 211941.

Thus the original e=13,14 profiles are rejected under squarefreeness, but this additional resource does not exclude either multiplicity. None of these computations improves the certified benchmark ledger. Repeated residual factors remain outside this discriminant argument. The final note states these limitations accurately.

## Audited artifact SHA-256

- `LINEAR13_16_SQUAREFREE_RESIDUAL_LIMIT.md`: `cdb859ccd0abb52aff3f88fe44d3c101d4136fb01fcafb267ed98ce94b43d65b`
- `linear13_16_residual_discriminant.py`: `3a97110e8abd91f3b56c3fe528c514acc8dcd1e369aff0f99d1d0950abc8c4cc`
- `linear13_16_residual_discriminant.json`: `f5395e180f71743c12fc70992afc90f326ea75ae278477eef7e5e981f76d25f1`
- `linear13_16_residual_discriminant.resources.json`: `17971bd1be50633774e0c5e0b535230edb71b1a5e0441805bb3a548804c1691f`
