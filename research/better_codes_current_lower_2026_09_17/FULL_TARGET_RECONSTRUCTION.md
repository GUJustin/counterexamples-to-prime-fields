# Full numerical reconstruction of the next-centibit candidate

There is no better.codes improvement yet. The reconstructed agreement 181275
candidate misses the repaired MCA allowance by **21042194961366305**, about
**7.65%**. Earlier sub-percent deficits held the incumbent singleton/packing
allowances fixed; they were conditional diagnostics, not near-complete
certificates. Rebuilding those allowances from repaired target sources is
the material extra cost.

The primary repository is
<https://github.com/proximity-prize/proximity-prize>, pinned at
`cdb451f13fdc6c84f5fe363e77ee13a89bd30974`. All primary input paths, URLs,
and hashes are tracked in the input manifests. `fetch_primary_sources.py`
restores and verifies the unified `source_inputs.json` inputs.

## Reconstructed candidate

* Agreement 181275, corresponding to the next possible integer score 6812.
* Primary A `(m,q,s,L)=(118,163,36,176421)`.
* TCap `(m,s,L)=(226,70,9682)`, with total cap 9678.
* All 27 auxiliary sources repaired; all 16 triple root envelopes regenerated.
* Target carrier identity/tangency gates audited.
* All 5238 component contexts, eight rebuilt Bellman packing sheets, and
  32 explicit phases. The final phase is the new source
  `(m,L,s,Y)=(350,31116,107,484)`.
* Primary B alternatives `(m,q,s,L)=(134,185,40,22192)` and
  `(137,189,42,18812)`, with repaired residual-pair/derivative-chain arithmetic.
* Scalar-list budget 7658131917, giving MCA allowance 274980720453263170.

The second B alternative is slightly better. Its worst context is
`(r,v,z)=(36,127,9489)`, with charge 296022915414629475. There are 2841 failing
contexts. The empty-factor context passes. The binding source is phase 32;
its charge is 289199318507669466, including the inherited prefix
288491475171905068. The earliest ancestor creating that prefix is `(17,45)`.
Thus the dominant cost already occurs well inside the component box.

The other B alternative has worst charge 296073051328227109. Both complete
per-context numerical ledgers are saved in `target_B_*_all_rows.json`; their
summaries and prefix origins are in `target_repaired_B_ledger.json`.

## Baseline control

The new singleton generator was rerun at the exact incumbent parameters.
It reproduces or improves **all 4970×8 stored singleton allowances**, with
zero positive differences and 276175 critical-point checks. Separately,
64 coefficientwise polynomial comparisons show that its generic helper/
retained-root alternatives are bounded by the incumbent root envelopes.
Consequently the 7.65% failure is not a failure to reproduce the baseline
allowances or an unexplained max-of-four transcription penalty.

The target singleton reconstruction checks 260809 critical points across all
5238 contexts. Each singleton bound is the minimum of eligible carrier,
root, and phase bounds; each root bound is the maximum of four affine
majorants. Activation boundaries and the neighboring integers at all line
intersections are included. The eight packing sheets process 52534968 exact
integer Bellman pairs. Phase prefixes are recomputed in increasing `(r,v)`
order, using only earlier phases and valid ancestor rows.

## Reproduction and limitations

Use the repository watchdog for every numerical job, with 384 MiB and 60 seconds.
After restoring primary inputs and running the baseline/target source,
threshold, and repair scripts documented in adjacent notes:

1. `regenerate_singletons.py 1 12`
2. `regenerate_singletons.py 13 36`
3. `replay_regenerated.py`
4. `finish_target_ledger.py`
5. `baseline_singleton_control.py`

The regeneration consumes the repaired-source manifests and evaluators;
the latter have their own exact count, graph, identity, and characteristic
audits. `replay_regenerated.py` creates the ignored intermediate state used
by the final ledger script. That state is a reconstructible derived cache,
not an external research input.

This is an independently replayed numerical pipeline, not a completed Lean
port or a prize submission. The upstream code contains agreement/error
literals, ten-phase lookup defaults, finite row bounds, source definitions,
and protocol closure constants that must all be updated consistently and
proved. A final independent all-gates review is also required. Since the
numerical ledger itself currently fails, no security score or theorem is
claimed from this candidate.

The next constructive target is the auxiliary/packing or phase-source cost
at the ancestor `(17,45)`. The new phase source is useful, but it does not
yet compensate for the full cost of repairing the other sources.
