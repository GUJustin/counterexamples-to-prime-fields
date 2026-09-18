# Independent audit of constructive positive Eq63 sorting

**PASS.** This audit concerns `EQ63_GROUPED_POSITIVE_SORTING.md` as written after the weighted-excess/maximal-prefix correction. No manuscript changes were made during this audit.

## The previously dangerous step is resolved

Unconditional height sorting can decrease the complete Eq63 margin, as the adjacent-swap counterexamples show. The new lemma does not assert unconditional sorting. It may delete excess monomials, and in the positive case it truncates the EXCESS marginal profile relative to a fixed baseline. Those distinctions are mathematically essential.

The case split uses the weighted excess margin, not its unweighted total. Thus deleting the excess in Case1 cannot decrease the whole margin. In Case2, the excess margin is a sum of its own prefix sums. Selecting a maximal prefix and deleting the later excess makes every later excess prefix equal to that maximum. This both preserves/increases the weighted margin and makes the retained unweighted marginal surplus strictly positive. The baseline can have either sign; the proof does not require it to be a feasible source by itself.

## Exact finite source and rank checks

1. Removing degrees above H changes no Eq63 term. Removing final diagonals Lq<m cannot reduce the margin, because their exact surplus is nonpositive and their row weight is nonnegative. Downward-Y0 closure is preserved.
2. Every remaining diagonal is saturated. Subsequent deletions and left shifts preserve the saturation cutoff and the original characteristic guard.
3. The baseline and excess partition the jet support, hence also their full X-prefix coefficient columns. Source dimensions add. Local ranks do not add, but the definition of d_q is exactly the rank increment relative to the baseline. Equation(1) is therefore an identity with the correct marginal rank.
4. Truncating the excess at total degree k changes no rank increment at smaller degrees, since the saturated rank decomposes by total degree. In each column it removes only a top interval above the baseline height c.

## Rank transport checked at all boundary cases

The baseline decomposes into a coordinatewise order ideal of height at most c, plus earlier-column excess intervals. After clipping at u<=ell, the ideal still has nonincreasing diagonal lengths once q>=c. Every earlier excess interval starts before i+c, so its indicator cannot increase from q to q+1 for q>=i+c. This includes c=0, when the low baseline is empty, and ell<c, when all high excess intervals are empty.

Every shifted excess monomial has u>=c and old v>=i+1, hence new total degree at least i+c. Consequently C(q,ell)>=C(q+1,ell) exactly where needed. Concavity of min(z,m-ell) makes the incremental rank for the same incoming count no larger against the new baseline. This applies to the whole count X(q+1,ell), even when multiple excess monomials occupy a diagonal; no single-monomial approximation is used.

The new excess occupies columns i,...,j-1 at heights u>=c, while the baseline there occupies u<c. Thus there is no overlap or duplicate source monomial after shifting. Also old total degree is at least one, so no negative-degree boundary is introduced.

## Whole-margin and termination checks

Each shifted coefficient prefix grows by exactly D-1, and its challenge weight grows by one. Using the marginal-rank transport inequality gives precisely

  M_new-M_old >= sum_q(g_q-d_q)
    +(D-1)/n sum_E(H-u-v+2).

The first term is strictly positive after the excess-prefix truncation. All terms in the second are positive for retained active degrees. This is a comparison of the complete margin, not of separate first moments.

In both cases column j becomes the new suffix minimum c. All earlier prefix heights remain at least c and the previous suffix heights remain at most c. Thus the suffix invariant survives and its length increases at every step. The algorithm terminates after finitely many columns with a coordinatewise order ideal, positive margin at the same H, and no larger total-degree or derivative cap.

## Consequence and scope

Combining this positive-feasibility reduction with `ORDER_IDEAL_FOURTH_POWER.md` proves the Eq63 fourth-power declared regular-family ledger necessity for every downward-Y0 full-prefix monomial support. The independently established direct Eq64 sorting argument covers the same source class. Hence choosing the better of the two tests does not evade the stated fourth-power necessity in that class.

This supersedes the remaining-open scope sentences in the earlier normalization and adjacent-swap research notes. Their unconditional-monotonicity counterexamples remain correct. The earlier `ORDER_IDEAL_INDEPENDENT_AUDIT.md` was intentionally limited to the then-proved Eq64 extension; its statement that Eq63 was not yet extended is now historical.

The result still depends on the exact saturated-rank characteristic guard and the derivative-weighted full-prefix source model. It does not extend to arbitrary nonmonomial/global kernels, equal-weight cutoffs without a separate argument, or actual list/exception lower bounds.
