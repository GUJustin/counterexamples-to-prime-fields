# Local prior check and active-text audit for the RS3 anchor bound

2026-09-19. Bounded local check; no literature-priority claim and no manuscript edits.

## Result

No stale norm-one comparison was found in the active manuscript. A recursive traversal from paper.tex visited all 108 TeX inputs, with no unresolved input/include paths. Searches for the old 22N and 137N bounds, factor 44/274 comparisons, onset p>=401, and the old inverse-cubic dependence produced no remaining relevant active-text claim. Broad searches for the numerical constants and every norm-one reference were also inspected; unrelated occurrences are valid.

The current source is
research/binary_characteristic_transfer/quadratic_frobenius_core/norm_one_direct_list.tex,
SHA256 5ae6570f715de3f18019d2cac265af6bb2d4a59a81bce9487e7215b00821f269.

It consistently states:

- U(N,T)=N(N-1)(T-2)/[T((T-1)^2-(N-1))] for T>=3 and positive denominator, over every field/domain.
- U<=4N/3 at T=ceil(19p/10), p>=53, giving factor 8/3 versus the exhibited N/2 list.
- U<=9N/4 throughout ceil(sqrt(3)p)<=T<=2p+2, p>=53.
- For fixed sqrt(2)<c<2, limsup Lmax(ceil(cp))/N<=2/(c^2-2).

The introduction at paper.tex:1011–1036 matches these statements. The finite full band is correctly distinguished from the strictly above-first-order asymptotic range sqrt(3)<c<2.

The diff in commit 4b841c6 confirms that the complete list classification and its proof were not changed: the first bank has N/2 witnesses with 2p+2 matches, the second has N witnesses with p+1 matches, and all remaining quadratics have at most four matches. Only the universal comparison, its proof, and the associated parameter range changed.

## Local duplicate check

The bounded repository search found no earlier occurrence of the exact global U formula or an earlier improvement of the norm-one 22N/137N comparisons. Git history for the new lemma label first identifies commit 4b841c6, “Sharpen norm-one list comparison to factor 8/3 with elementary universal bound.”

The closest local predecessor is the same-day
research/prime_quadratic_line/DENSE_DOUBLE_INTERSECTION_SIX_ROOT_TRIANGLES.md,
which gives the local anchored multiplicity bound
R=(N-1)(T-2)/[(T-1)^2-(N-1)].
Summing MT=sum_x r_x yields the present global U bound. This is an elementary application of standard shortening/Johnson counting, not a claimed new general method.

Two earlier notes use anchoring in different settings:

- PRIME_NONDEGENERATE_PLANE_LITERATURE_GATE.md, section “One-anchor descent from quadratic witnesses,” concerns varying received-line parameters and a conditional finite-field plane-incidence input. It does not state this fixed-word ordinary-list bound.
- ANCHORED_QUADRATIC_LINE_ARRANGEMENT_GATE.md concerns witnesses sharing two fixed anchors on a received line and its O(N) fixed-anchor-pair / O(N^2) moving-anchor resource bounds. It is not a duplicate of U.

A bounded keyword/formula check of the read-only binary repository sections also found no literal duplicate. This is not an exhaustive mathematical equivalence search or an external literature search.

## Archived weaker comparisons remain

Several dated research records still contain the valid but superseded DKT upper bounds. They are not inputs to the active manuscript:

- quadratic_frobenius_core/NORM_ONE_DIRECT_LIST_AUDIT.md:3 still calls the 22N statement “current”; its later 22N/factor-44 calculations are archival.
- quadratic_frobenius_core/NORM_ONE_DIRECT_LIST_INDEPENDENT_REVIEW.md:49 discusses why ordinary unshortened Johnson and three-coordinate packing alone do not give the former O(N) comparison. The new anchored bound supersedes that comparative emphasis.
- quadratic_frobenius_core/NORM_ONE_GENERAL_FIXED_SUPPORT_2026_09_18.md:98,117 retains the inverse-cubic bound and 137N/p>=401 certificate.
- strategy_review/INTERIOR_LIST_THRESHOLD_REASSESSMENT_2026_09_18.md retains the 22N ledger.
- strategy_review/CURRENT_SIGNIFICANCE_PRIORITIZATION_2026_09_18.md has a correct new update banner but preserves its old 22N/137N discussion in the dated body.

These are weaker valid certificates, not contradictory mathematical upper bounds. If reused as current summaries, their older comparative wording needs the new bound. No archival files were edited in this check.

The independent exact arithmetic certificate remains in
research/rs3_anchor_list_bound_2026_09_19/{README.md,verify.py,receipt.json};
this receipt adds the local prior/active-source check, not a new computation.

