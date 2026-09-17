# Repair propagation after the new phase source

These are successive arithmetic diagnostics at agreement 181275. They are
not a completed score certificate or a Lean proof. The initial three rows
use the incumbent MCA budget 274980720549750805; the repaired scalar arm
reduces it by 96487635 to 274980720453263170. The difference is small compared
with the displayed deficits, but must be included in final propagation.

| Diagnostic | Contexts | Failed contexts | Worst charge | Margin to incumbent budget |
|---|---:|---:|---:|---:|
| New primary A potential, old context slice |4970|0|274712168849822149|268551699928656|
| PrimaryA expanded box `(r<=36,y<=163)` |5238|4|275081844735895895|−101124186145090|
| TCap total 9678, expanded singleton tails and packing |5238|19|275386673467898034|−405952918147229|

Primary A is repaired with `(m,q,s,L)=(118,163,36,176421)`. Its smaller L
reduces the helper/complement cost, partly offsetting the expanded component
box. The old box had 4970 contexts; all 268 added contexts admit at least one
phase source at threshold zero. Their singleton bounds were constructed from
the exact phase envelopes, then all eight Bellman packing sheets were
extended using 5176608 pair checks.

The standard TCap repair `(m,s,L)=(226,70,9682)` permits total degree 9678.
The diagnostic extends all singleton bounds through the extra 403 total
degrees by direct phase envelopes and rebuilds all eight packing sheets
(52534968 pairs). It also recomputes all 32 phase prefixes, the primary A
complement, and the TCap residual-pair overhead 1064173915603138. Its worst
context is `(36,127,9493)`. PrimaryB, the derivative chain, and singleton
bounds below total 9275 were still frozen in that diagnostic.

That frozen-singleton limitation is material: repaired auxiliary source
cutoffs invalidate 4808 old singleton intervals. The next stage therefore
regenerates every singleton envelope using the 27 repaired auxiliary sources,
eight phase sources, and the target-audited carrier bound. Each auxiliary
bound is a maximum of four affine lines; the overall singleton bound is the
minimum over available choices. Exact critical points include activation
boundaries and adjacent integers at line intersections. Two bounded chunks
cover all 5238 contexts and 260809 critical-point checks. Their data are
`regenerated_singletons_1_12.json` and `regenerated_singletons_13_36.json`.

Scripts `extend_A_contexts.py`, `extend_total_cap.py`, and
`regenerate_singletons.py` reproduce the stages; their resource reports
record the 384 MiB/60 second guards. The forthcoming complete regeneration must
also use the repaired primary B, derivative-tail allowance, chain coefficients,
and scalar-list budget before any candidate can be called numerically closed.
