# Exact weighted-slab refinement at the binding singleton

The valid exact weighted-slab support bound does **not** remove the current binding singleton. At `(r,v,z)=(12,43,3206)`, source 00 first routes at `z=3207` even after using actual source contact degree and exact slab cardinality. Thus the existing singleton value `288191873412750740` remains unchanged by these refinements.

| Source | Original threshold | Actual contact degree | Exact slab |
|---|---:|---:|---:|
| 00 | 3207 | 3207 | 3207 |
| 01 | 3222 | 3222 | 3222 |
| 02 | 3217 | 3216 | 3216 |
| 03 | 3229 | 3229 | 3228 |
| 04 | 3269 | 3268 | 3268 |
| 05 | 4041 | 4032 | 4030 |
| 06 | 3376 | 3374 | 3374 |
| Added source | 5872 | 5860 | 5851 |

The exact slab evaluator is `research/phase_source_feasibility/exact_slab.py`; its author independently checked 1,400 small brute monomial sums. `exact_slab_thresholds.py` imports that evaluator and verifies both sides of each threshold. Increasing total degree decreases the remaining total-degree caps and the number of nonnegative layers, so binary search is valid on the source-covered interval. All eight sources cover the tested total-degree range.

This is a proved support-count refinement with an arithmetic implementation, not a completed Lean port: a new rank-support lemma and recursive budget lemma are required, as detailed in the separate proof audit. It is neither a new full certificate nor a score improvement. Full envelope regeneration was not repeated because the critical earliest route and singleton value are unchanged.

Separately, `interval_local_source_grid.json` records a bounded 203-shape test using the previous uniform thin-band bound and exact contact degree. Even restricting characteristic gates to total degree 3261, no tested shape routes at total degree 3030 within the saturated affine-in-L regime. This is a finite search result, not a global impossibility theorem.

Reproduce the critical computation under the repository resource guard:

```sh
python3.12 research/overnight_2026-09-16/certificates/run_bounded.py --rss-mib 384 --seconds 60 --report research/better_codes_current_lower_2026_09_17/exact_slab_critical_resources.json -- python3.12 research/better_codes_current_lower_2026_09_17/exact_slab_thresholds.py
```
