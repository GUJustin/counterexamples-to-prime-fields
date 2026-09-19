# Elliptic coset-complement route

Current status: **no counterexample**. The torsion support count is real, but
the natural received-line compiler does not combine across subgroups.

For torsion prime ell, n=(ell^2-1)/2 and k=n-4ell+1. The corrected tested
agreement T=n-2ell-5 lies above the full first-order curve and below Johnson
for ell>=23. `PARAMETER_WINDOW.md` and its exact verifier establish this
numerical window, not source farness or a construction.

The substantive findings are:

* `FIXED_SUBGROUP_QUOTIENT_PLANES.md` constructs each fixed-subgroup bank
  and proves its received plane is disjoint modulo the code from every
  different subgroup's plane, even with different external poles.
* `FIXED_SUBGROUP_QUOTIENT_PLANES_INDEPENDENT_AUDIT.md` verifies that proof
  and extends it to the full three-dimensional space of weighted quotient-tag
  words. Those spaces intersect pairwise in dimension at most one. On a
  received line with a far endpoint, their two-fiber errors give only O(n)
  distinct labels.
* `FULL_PAIR_TRANSVERSAL_CLASSIFICATION_INDEPENDENT_AUDIT.md` shows why
  realizing every pair with full-support errors forces this weighted space.
* `FOUR_CYCLE_FULL_SUPPORT_REDUCTION.md` strengthens the restriction to
  arbitrary partial selections and arbitrary values inside two fibers.
  Despite its historical filename, the final statement does not assume
  coordinatewise full support. A four-cycle forces the weighted space;
  extremal graph counting bounds all such labels by O(n^(5/4)). This still
  leaves superlinear partial banks possible.
* `SYNDROME_TRANSVERSAL_TARGET.md` gives the exact linear Pluecker equations
  plus decomposability condition for a specified support collection. Dimension
  counts or nonzero linear kernels alone do not construct a line.

The separate `../elliptic_source_gate/TORSION_COSET_LOCATOR_PREFIX_AUDIT.md`
checks the locator identities and small-order formulas. Its verifier replays
the existing order-five fixture, rather than searching for curves or lines.

Still open are a constructive sparse pair bank on one common line, the five
additional error positions allowed by the corrected threshold, and other
support shapes. All require actual source-distance and distinct-label bounds.
The current notes do not improve better.codes, establish practical-domain
behavior, or show prime-field proximity-gap tightness. No rentals were used.
