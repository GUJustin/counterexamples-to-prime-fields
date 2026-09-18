# Restored second-jet route: compatibility and corrected scope

The pinned primary repository already contains the second-jet interpolation and geometric alternative needed for this experiment. The earlier notes in this directory overstated the absence of a routing theorem because they did not inspect these restored definitions. Their standalone algebraic observations remain valid, but the route must now be assessed through the existing proof framework.

Primary repository: https://github.com/proximity-prize/proximity-prize at commit cdb451f13fdc6c84f5fe363e77ee13a89bd30974. Exact URLs, SHA256 hashes and local locations are in restored_primary_sources.json. Re-fetching confirmed that the cached LowerGeometry.lean and SecondJetRefinements.lean match this commit byte for byte.

## Exact interface

LowerGeometry.lean defines SecondJetRelaxedInterpolation.Interpolant around line24595. Its source variables are X, curvature V=P^[2], value Y=P, slope R=P', challenge Z. Its flags are

    2 deg_V + deg_R <= B,
    deg_V <= s,
    deg_V+deg_Y+deg_R <= U,
    deg_V+deg_Y+deg_R+deg_Z <= L.

The localize/substitute maps compose to Y -> w_x(Z)+tR−t²V+t³E, exactly the contact map used in our independent rank experiments.

For curvature exponent h the strict weighted cutoff is

    m*A − reserve(k,n0,h)*(A−(w−2)),
    reserve(k,n0,h)=h if h<n0, otherwise k.

At target A181275,w131071 the reserve cost is50206, not50204 (the latter is the regular counting denominator). The old source was pinned at A181353 with reserve50284.

The interface includes nonzero source, flags, local contact order m, and vanishing of every curvature derivative through order k on sufficiently agreeing codewords. These derivative vanishings are essential to the proper-helper/prolongation alternative; a positive unreserved source count alone is not generally sufficient.

For the curvature-linear rectangle previously tested, choose s1,B=S+2,U=J. With k0,n01 both h0 andh1 have reserve zero, so that rectangle genuinely fits the full interface after changing the target constants and proving source existence using the recovered rank bound. The larger old flag space permits slope degree S+2 in the curvature-free part and S in the curvature-linear part.

SecondJetRefinements.lean provides helper_or_divisibility (line51), count_of_interpolant_total (line203), and the retained_scaled alternative. Thus the prolongation branch is already addressed by the old theorem, not an entirely missing mathematical mechanism. The total-degree avoidance hypothesis is L<t for the target factor. Proper and retained branches, characteristic pair gates, and target-dependent arithmetic must all be checked.

## Independent arithmetic replay and target repair

restored_flag_gate.py first reproduces the original profile114 coefficient count1521555139747342 and local rank5804271999 exactly. It then evaluates the curvature-linear flag family; its bounded5115-shape check has minimum sufficient L5108 and does not activate at critical total degree3261. This limited scan is not a global impossibility theorem.

The more relevant general second-jet sources repair successfully at target181275:

| m | B | s | U | k | n0 | Required L | Certified nullity |
|---|---|---|---|---|---|---|---|
|114|47|21|155|5|7|2777|2602706530|
|116|47|21|157|5|7|2721|1863810977|
|96|38|17|130|4|5|2698|313386875|
|108|41|19|146|4|7|2557|2092909271|

Every row satisfies the closed-rank hypotheses B<=m, m+s<=U, L>=m+B+s, and all curvature-dependent cutoff caps dominate U. All four have L<3261. The script restored_general_gate.py computes source dimensions and local ranks as exact affine functions of L and solves the strict positive-nullity gate. It does not claim a target Lean rebuild or a complete geometric receipt.

The next decisive test is the maximum of the proper-helper and retained-branch counts at the actual binding contexts, followed by all relevant factor domains and full packing propagation. Positive interpolation and activation do not establish that the numerical bound beats the incumbent envelope.

## Priority correction

The rectangular curvature-linear rank formula and its degree-graded refinement are specializations of the primary SecondJetCounts formulas already present in LowerGeometry.lean. Our explicit kernel proof is an independent recovery, not a new theorem. The useful new work here is the audited target repair and the opportunity to test an existing second-jet route against the full target receipt.

## Decisive downstream check

The upper-bound-route agent independently reproduced the original profile114 binding value268923679246212987, then evaluated the target proper and retained branches. At the actual critical factor (r,v,z)=(12,43,3206), the retained normal term alone is352613725068219795, already larger than the repaired incumbent singleton288191873412750740. The best of the four repaired source profiles gives509590929180880563; the proper branch is much smaller, and all evaluated characteristic gates pass. Exact arithmetic is in restored_route_cost.py/json.

Consequently these repaired sources do not improve this binding contact. Further source-parameter optimization alone cannot overcome the unchanged normal-term floor at this contact. A useful next step would have to force the proper-helper branch or improve the retained geometry. The recovered source activation is real, but it does not close the full ledger deficit.
