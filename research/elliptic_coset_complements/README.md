# Elliptic coset-complement route

Current status: **no counterexample; the at-most-two-nonkernel-fiber model has an O(n) label bound with a far endpoint**. The torsion support count is real, but arbitrary within-fiber error values and sparse selections of pairs do not evade this bound. The five-extra-error variant remains outside it.

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
* `TWO_FIBER_LINEAR_RESOURCE_BOUND.md` is the current strongest restriction.
  A three-edge path forces canonical error shapes at its leaves. Thus a
  nonempty graph 3-core forces the received syndrome line into the weighted
  space. At most one subgroup can have such a core; all others are
  2-degenerate. Including one-fiber errors gives at most
  binom(t,2)+ell(2t-3)+(ell+1)=O(n) labels. Arbitrary partial coordinate
  support is allowed, and a far endpoint is an explicit hypothesis.
* `FOUR_CYCLE_FULL_SUPPORT_REDUCTION.md` retains the valid earlier cycle
  proofs and superseded O(n^(5/4)) and O(n^(7/6)) count bounds; they are
  not the current status of the two-fiber route.
* `SYNDROME_TRANSVERSAL_TARGET.md` gives the exact linear Pluecker equations
  plus decomposability condition for a specified support collection. Dimension
  counts or nonzero linear kernels alone do not construct a line.
* `FIXED_EXTRA_QUOTIENT_INTERSECTION_SYSTEM.md` proves that the fixed-extra
  quotient has exactly 3d+3 dimensions and gives an exact pairwise CRT test,
  including the zero-extended kernel values. At d=5 the quotient dimension is
  18. The single curve and fixed extra set in `ell23_fixture/` have zero
  intersection for all 253 clean subgroup pairs after removing the common
  all-far residue space. This is a finite diagnostic, not a general theorem
  about other extra sets or curves.
* `DERIVATIVE_EXTRA_LOCATOR_DISCRIMINATOR.md` gives a degree-at-most-six
  necessary label equation for the explicit Phi',Phi'' pencil with scaled
  logarithmic-derivative error values, followed by an exact polynomial degree
  acceptance test. It is a restricted candidate, not a split locator family
  or a proximity-gap result.

The separate `../elliptic_source_gate/TORSION_COSET_LOCATOR_PREFIX_AUDIT.md`
checks the locator identities and small-order formulas. Its verifier replays
the existing order-five fixture, rather than searching for curves or lines.

The five additional error positions allowed by the corrected threshold and
other support shapes remain outside the linear bound. The exact residual
constraints for the former are recorded in `FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md`.
`FIVE_EXTRA_ERRORS_INDEPENDENT_AUDIT.md` and the finite ordinary-RS replay
verify that reduction, including detection of artificial padding. They do not
construct an elliptic line. For one fixed extra set,
`FIXED_EXTRA_SET_PATH_AUDIT.md` isolates spaces of dimension at most 23.
Those spaces always share a residue subspace whose nonzero words are all far;
its common two-planes cannot be counted as counterexamples.
These routes still require actual source-distance and distinct-label bounds;
a superlinear sparse bank using only two nonkernel fibers is now excluded
under the stated far-endpoint hypothesis.
The current notes do not improve better.codes, establish practical-domain
behavior, or show prime-field proximity-gap tightness. No rentals were used.
