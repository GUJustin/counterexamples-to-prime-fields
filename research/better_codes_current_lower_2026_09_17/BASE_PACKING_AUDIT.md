# Baseline carrier, singleton, base and packing audit

September 17, 2026. Independent arithmetic replay of the remaining
stored moving-fiber baseline receipt layers at the pinned repository
commit cdb451f13fdc6c84f5fe363e77ee13a89bd30974. All checked conditions
pass. This is not a new target certificate or a Lean kernel rebuild.

## Checks completed

Across all 4,970 rows (1<=r<=35, r+v<=159):

* 24,850 Carrier.Correct equalities at z=0,...,4.
* 487,808 SingleValid endpoint inequalities over all eight packing
  sheets, including complete interval coverage, singleton treatment
  below z=3, and every Active side condition.
* 86,460 BaseValid endpoint inequalities, including complete interval
  coverage, valid sheet choices and the base-affinity cell restrictions.
* 47,358,360 direct Bellman convolution inequalities across the eight
  packing sheets, with all row-array lengths checked.

Carrier costs are reconstructed from the primary flagMixed formula,
not trusted from the saved five-value carrier. For the high branch,
the code evaluates the reduced and rational tail flags with the current
moving-fiber normal correction and65539 coefficient. For the low branch,
it evaluates the two padded tails directly. The exact characteristic
Safe predicates are separately reconstructed for each applicable
ordinary-source interval.

The sixteen root-source slope and intercept polynomials are parsed from
the pinned arithmetic definitions, rounded with the exact denominator
and+1 convention, and evaluated at the appropriate shifted indices.
Their source-limit gates use the actual three-source catalog groups.
Phase choices use the current seven source potentials and their stored
thresholds. The full source inequality proofs themselves are not
reproved by these endpoint checks.

The direct Bellman test verifies own(r,u)+packed(R-r,v)<=packed(R,u+v)
for every permitted split and pair of indices. It does not assume that
the stored packed array is a valid closure. Integer arrays are used only
after checking the explicit size bound that prevents signed64-bit
addition overflow. All other arithmetic uses Python integers.

## Reproducibility and limits

base_packing_audit.py records the formulas and full loops;
base_packing_audit.json records the exact check counts. The run completed
in5.03 seconds with sampled process-group RSS below115MiB, under the
384MiB/60-second watchdog. base_packing_audit_sources.json records URLs,
SHA256 hashes and sizes for the additional pinned primary files; those
files remain in the ignored primary cache.

These checks fill the previously missing baseline Carrier.Correct,
SingleValid, BaseValid and Bellman arithmetic layers. Combined with the
other agent's phase/threshold/prefix/ledger replays, they substantially
cover the stored numerical receipt. They do not independently reprove
all upstream algebraic-geometric source-provider theorems, the full
catalog mixed-degree domination identities, or the Lean dependency chain.
Most importantly, they do not transfer unchanged to agreement181275:
that target changes source existence and threshold/provider arithmetic.
No better.codes improvement follows from a successful baseline replay.
