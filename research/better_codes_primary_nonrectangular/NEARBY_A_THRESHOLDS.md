# Nearby A caps: nonrectangular support does not lower these thresholds

Seven exact min-cut gates and all seven streaming flow/cut replays pass. Every tested maximum is zero. Thus no positive support improvement was found to propagate through the downstream ledger; the tested rectangular minimum challenge caps remain exact for the entire Y-downward full-prefix support class.

All gates use n=262144,w=131071,A=181275. The weighted cutoff is the largest permitted by both contact and declared jet-cap interface:

    D=min(mA,(Q+1)w-Smax).

All tested extractions are saturated, so the local Pascal rank formula is exact.

| Q | m | R cap | D | Gate | Optimum |
|---|---:|---:|---:|---|---:|
|160|116|35|21027900|unweighted slope|0|
|160|116|36|21027900|unweighted slope|0|
|160|117|35|21102396|unweighted slope|0|
|160|117|36|21102395|unweighted slope|0|
|161|117|35|21209175|L=1118297|0|
|161|117|36|21209175|L=613674|0|
|163|118|36|21390450|L=176420|0|

An unweighted-slope optimum zero excludes every L by the diagonal-prefix identity. A zero optimum at a specific L excludes every smaller L by maximum-prefix normalization. Since the archived rectangular witnesses are positive at the next challenge caps, the exact minima for the last three fixed shapes are respectively

    1118298, 613675, 176421.

This means no improvement in A's complement coefficients comes from changing only the downward jet support at those shapes. A ledger rerun using the same caps would not constitute progress.

## Additional q160 consequence

For R cap35, the q160 result extends to every multiplicity at this declared degree interface. If m≤115, the weighted cutoff admits no jet degree160, so the existing all-m q159/r35 theorem applies. Multiplicity116 is checked directly. For m≥117 the maximal permitted D is the constant21102396; the source is fixed and contact conditions are nested as m grows. The m117 zero-slope result therefore dominates every larger m. This all-m consequence fixes D at its maximal permitted value. Smaller deliberately chosen weighted cutoffs are partial X-prefix restrictions and are not excluded by source inclusion alone; they require a separate dimension-test audit.

## Reproducibility and scope

`nearby_a.py` selects precisely the seven rows from the archived `primary_A_small_quotients.json`, invokes `mincut_gate.cpp`, then `verify_receipt.py`. The latter independently checks every edge capacity, flow conservation, minimum-cut equality, support closure, and the direct rank sum. `nearby_a.json`, the seven receipts, sparse flows, and `.verified.json` files preserve all data. Total run and replay time was4.44seconds with41MiB reported peak RSS under the60-second/384-MiB bound.

These conclusions concern the declared fixed shapes, maximal weighted cutoffs, full coefficient prefixes and exact sum of local ranks. They do not exclude nonmonomial supports, partial X/Z prefixes, genuine cross-coordinate dependencies, or other source parameters. No actual full primary-kernel vanishing or global list-size bound is asserted.
