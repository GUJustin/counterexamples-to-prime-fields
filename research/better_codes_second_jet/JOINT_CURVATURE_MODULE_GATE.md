# Two curvature-linear equations: exact module gate

**Scope correction:** the restored primary `SecondJetRefinements.lean` already proves a second-jet proper/prolongation alternative. See `RESTORED_ROUTE_COMPATIBILITY.md`. Statements below identifying a wholly missing route are superseded by that primary-source audit; standalone algebraic lemmas remain valid.

Work in the UFD k[X,Y,R,Z,V]. Write Q_i=A_i V+B_i. A nonzero resultant A_1 B_2−A_2 B_1 gives a first-order identity for every common polynomial solution. Nonzero scalar linear independence of Q_1,Q_2 does not imply this resultant is nonzero: the necessary condition is independence over the fraction field k(X,Y,R,Z).

If every nonzero element of a kernel subspace has the same ratio B/A, clear denominators to a primitive V-linear factor F. Gauss's lemma implies that every source in the subspace is F G with G independent of V. Conversely such a subspace has vanishing pairwise resultants. A purely V-free kernel is a separate rank-at-most-one case with no useful V elimination.

For any fixed F, all nonnegative weighted degrees, total jet degree, slope degree, and jet-plus-challenge degree are additive under multiplication. Thus the space of admissible multipliers is exactly the intersection of the original degree caps shifted by the corresponding degrees of F. This gives a rigorous ambient common-factor dimension bound. It uses no independence assumption about coordinate constraints.

At the audited source m128,S40,J177,L5515,Vcap1, the particular factor F=V already has an ambient multiplier space of dimension360473415909375. The proved source-kernel dimension lower bound is only53746080, over6.7million times smaller. Therefore comparison with the maximum ambient common-factor space cannot force a nonzero pairwise resultant here. This does not demonstrate that the actual source kernel has a common factor; it demonstrates that the proposed raw dimension certificate is insufficient.

Even the special factor V exposes what extra information is needed. For Q=V G, the second-jet local condition is equivalent to the ordinary first-jet condition on G at the same order m: cancel the independent V and substitute E_first=−V+tE; conversely specialize E=0,V=−E_first. Thus improving the bound on the actual constrained multiples requires a global upper bound on a first-jet interpolation kernel with a shifted source budget, not merely the coefficient count or the known local-rank upper bound. Existing source-existence estimates give kernel lower bounds and cannot be reversed to supply this missing upper bound.

Finally, existence of a nonzero resultant alone would not finish the benchmark. The resultant may have roughly doubled source degrees, and trivial pairs such as H,VH merely yield H², reproducing a preexisting first-order equation. A useful joint-source theorem must certify both a nonzero resultant and a favorable first-order degree/factor profile. Neither follows from the present curvature source dimension certificate.

The tiny exact arithmetic receipt is joint_module_gate.py/json. No matrix scan was used, and no score improvement is claimed.

## Stronger contact of a nonzero resultant (root's subsequent lemma)

The doubled degree has a compensating doubled contact order, so it is not by itself a reason to discard elimination. Suppose Q=A V+B has curvature contact order m, with m>=3. Substitute V=−E1 and E3=0, making Y=w+tR+t²E1. Differentiating the full curvature identity in E3 gives t³Q_Y=0 mod t^m, hence Q_Y has order at least m−3 on this first-jet substitution. Differentiating the specialized identity in E1 gives t²Q_Y−A=0 mod t^m. Thus A has first-jet contact order at least m−1.

For two such sources, their resultant equals A1 Q2−A2 Q1 on the same substitution, so its first-jet contact order is at least2m−1. If each source has strict weighted degree<mA, then wt(A_i)<=mA−w+1 and wt(B_i)<=mA−1, giving

    wt(resultant)<=2mA−w.

Equivalently its strict degree budget is2mA−w+1, only A−w+1=50205 above the ordinary budget(2m−1)A at the pinned parameters. Every candidate satisfies the resultant identically because it satisfies the original two equations; no new root-count argument is required for that identity. This makes elimination substantially more plausible than a naive degree-doubling objection suggests. The rational independence gate remains unresolved, as does a favorable factor/counting receipt for the resulting first-order equation.
