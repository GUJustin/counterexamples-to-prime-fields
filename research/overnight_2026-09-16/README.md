# Integrated finite coding-theory improvements — September 16, 2026

This package updates the official `GUJustin/counterexamples-to-prime-fields`
manuscript. It was assembled in an isolated worktree from the existing
canonical working tree, preserving the other session's uncommitted work.
`baseline.json` identifies that source. The manuscript also retains the
previously staged balanced-fiber and growing-moment refinements, whose
proof reviews and checkers are included in their respective research
directories. Those earlier results are not attributed to the overnight work.

## What changed

| Result | Prior paper | Integrated result |
|---|---:|---:|
| Interval list, n64/k32/t34 | 5,285,900,426,578 | 5,552,914,238,035 (+5.05%) |
| Quadratic circle, n2048/K256/T302 | 285,003,988,493,147,037 | 365,153,907,657,996,934 (+28.1%) |
| M31 interval list, n157/k63/t68 | New finite instance | 28,169,451,256,663,519,418; >34.09967 excess bits |
| M31 interval line, n82/k9/t12 | New finite instance | 138,752,510 labels; >7.04613 excess bits |
| Quartic-extension interval line, n157/k63/t68 | New finite instance | 508,108,952,659,354,448,051,620,618 labels; >50.90955 excess bits |

The stronger native-circle comparisons retain the precise circle code
spaces. The interval examples use prime-field evaluation points; only the
last row uses an extension alphabet. Finite comparisons use c1=c2=1.
The pinned better.codes display remains 116.13. These are coding-theory
results, not a revised security level for a complete deployed protocol.

## Verification

Run `make verify-overnight` from the repository root. It requires Python,
NumPy, SymPy, and a C++17 compiler named `clang++`. Each step runs alone,
with numerical threads set to one and its subprocess-group RSS monitored
at a 384 MiB ceiling. The half-second sampling interval can miss short peaks.

The suite recounts the n64 class by complementary subsets, rechecks the
saved 4D/3D projection identities and raw-moment transformations, and
independently integrates both displaced weights. It recounts the selected
n82 incidences by formal division, recomputes its source size, and replays
the stored rational duals without calling an optimizer. A separate
coefficient-sum implementation verifies the native-circle class counts and
collision arithmetic. The original expensive directional subset counts
are preserved inputs; the suite does not rerun all of them.

The n82 incidence check uses a different recurrence identity and item order
with the same histogram engine, not an independent full engine. The
general proofs are self-reviewed and supported by exact checks; this
package does not assert independent peer review or novelty.

`finite_updates.tex` is included directly by `paper.tex`. The numerical
inputs are under `certificates/`, with paths made relative to that directory.
The old weight bounds remain in their original propositions as valid
method-specific results. The introduction and finite-example summary now
point to the stronger exact certificate.

## Publication checks

The revision builds cleanly to 71 pages. All twelve commands in the
finite-certificate replay suite passed; `verification.json` records their
results and sampled memory use. The publication pass additionally runs
the complete `make verify` target, including the earlier mathematical
refinements. Its result is recorded in `publication_suite_resources.json`.
The separate `beyond_johnson_tightness` notes are exploratory follow-up
and are not included in this manuscript.
