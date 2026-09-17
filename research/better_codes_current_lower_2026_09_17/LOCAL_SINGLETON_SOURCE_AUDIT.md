# Context-local singleton interpolation sources: proof audit

**Conclusion:** a source used only for a fixed singleton context may use the actual factor degrees in its mixed-characteristic gates. It need not satisfy the global phase-box gates. This is supported by the pinned generic theorem, but requires a new local singleton adapter: the existing `PhaseSourceSound` wrapper deliberately quantifies over the entire global box and cannot be reused unchanged.

## Primary theorem and specialization

Pinned `MovingFiberRouting6811.lean`, theorem `BatchPowerRoute.exists_strict_helper_split_of_batch_source_thin` (line980), takes an arbitrary finite set A of regular irreducible factors. Its helper gates and stage-charge hypotheses quantify only over F∈A. Take A={F}. The conclusion supplies a proper subset U⊊{F}, hence U=∅, and directly bounds the seeds on F by its supplied charge. The field-size requirement becomes1<|K|. There is no requirement to choose the same source across different singleton contexts, and no global phase potential is needed.

The existing proof of `MovingFiberSingletonGeometry6811.source_count` uses this same singleton principle through the more restrictive `routeable_exists_strict_helper_split`/`PhaseSourceSound` wrapper. The new adapter should instead invoke the generic theorem directly, or parameterize that wrapper by a context predicate. The receipt choice/cover soundness theorem must include this additional local choice and its activation interval. It is not already available merely by inserting a row into the old seven-source catalog.

## Exact sufficient hypotheses at target181275

Write n=262144, w=131071, A=181275, p=2130706433; agreement gap is50204, and the power-band decrement is50205. For source (m,L,s,Y), let D=mA and let g>0 be a proved lower bound on its kernel dimension.

Required source conditions include D+s≤w(Y+1), s≤m, m<p, and the exact interpolation coefficient-minus-local-rank lower bound g. For a regular factor with actual weights (r,y,t), require1≤r, t≤L, y≤Y, r≤s. Set fuel=min(floor(L/t),floor(Y/y),floor(s/r)). The usual thick or contact-thinned band budget must be strictly below g. The standard contact bound wy−r and shape inequality justify the conservative thin-band test exactly as in the existing route adapter.

Fuel≥1, fuel≤s≤m<p, terminal remainder, and capacity/positivity conditions follow from these hypotheses. In particular D−j·50205≤(m−j)A+j(w−1), with equality before natural subtraction, for j≤fuel≤m. The factor is already a regular irreducible factor of the selected carrier; helper polynomials need not be irreducible. No extra requirement D<p appears in this generic source-routing theorem.

The stage-zero characteristic conditions are:

- r≥1 and y,r,t<p;
- rL+ts<p;
- yL+tY<p;
- ys+rY<p.

At stage j the source caps become (L−jt,Y−jy,s−jr), so all three mixed costs weakly decrease. Thus stage-zero gates imply all required stage gates. This uses actual factor weights, not the global maxima36,163.

For fixed r=12,y=55 and all t≤9678, sufficient endpoint conditions are

`L <= min((p-1-9678*s)//12, (p-1-9678*Y)//55)`

and `55*s+12*Y<p`, together with nonnegative numerators and the elementary degree gates. A shorter permitted t-interval can relax these caps further, provided the choice is disabled outside that interval.

## Exact cost and affine envelope

Let My=rL+ts, Mr=yL+tY, Mz=ys+rY. The exact stage-zero helper bound is floor(N/50204), where

N=(n−w)[(1+2wy)My+w(2r−1)Mr+(1+2wt)Mz]+80870·50204·Mz.

This is exactly `AsymmetricHelper.leftRegularCountCap(helperPair L Y s y r t)` after the target parameter substitution, matching `pair_numerator`. The denominator is the agreement gap50204, **not** the interpolation nullityg. Monotonicity in the three right caps makes this stage-zero charge dominate every power-stage charge. At fixed r,y and t=r+v+z, N is affine in z with nonnegative coefficients. Ceiling its slope and intercept separately gives a valid integer affine majorant usable in the singleton envelope.

The routing test must hold at each enabled z. A threshold proof may establish this over a tail; otherwise use explicit certified intervals. Characteristic validity alone does not establish routing. Choices may differ between contexts and intervals because each proves a pointwise bound for that factor; subsequent singleton/packing summation needs only those pointwise bounds.

## Status and provenance

This audit establishes applicability of the generic mathematical proof and identifies the target port obligations. It is not a compiled Lean adapter or a completed benchmark certificate. Primary files are pinned at cdb451f13fdc6c84f5fe363e77ee13a89bd30974. Newly fetched dependencies and SHA256 hashes are recorded in `local_singleton_source_inputs.json`.
