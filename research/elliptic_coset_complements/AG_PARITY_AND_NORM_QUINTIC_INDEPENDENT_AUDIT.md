# Independent audit of AG parity and norm-quintic reduction

Verdict: PASS. Reviewed the actual `AG_PARITY_AND_NORM_QUINTIC_REDUCTION.md`; no changes to the source note or manuscript.

## Parity and divisor checks

The L(mO) degree bounds, exclusion of y=0 on nonzero odd torsion, paired-agreement subtraction, and division by an x-locator all hold with the stated pole budgets. In particular the odd cofactor at five extra errors has degree at most three and does not enlarge the even degree-five cofactor. This says nothing about unpaired AG agreements.

For the displayed Miller product, the three line divisors sum to the desired five points plus the two intermediate opposite pairs. The two vertical denominators cancel precisely those pairs, leaving the divisor sum[P_i]−5[O]. The last point is −S4=P5. The qualification on degenerate additions is appropriate; the signed divisor itself, rather than that particular ordering, guarantees existence in all cases.

Normalizing the coefficient of X in B1 to one is possible because a function with precisely five finite zeros has exact pole order five. The norm sign in J=f_c(X)(X+b)^2−A2(X)^2 makes it monic. The five displayed coefficient identities agree with direct expansion. Conversely squarefreeness prevents a simultaneous root of X+b and A2, so each root selects one signed point, and the function's principal divisor gives their zero sum.

Signed-choice uniqueness holds exactly as claimed: the difference of two choices gives twice the sum of a subset of the first signed divisor. Odd torsion permits cancellation of two. Both that subset and its complement sum to zero; for a proper nonempty subset one of the two has size at most two, impossible for nonzero points with distinct x-coordinates. Thus only global reversal remains.

## Fixed affine norm-pencil test

Divisibility by Phi at three distinct parameter values forces coefficientwise divisibility of the degree-two parameter polynomial. The quotient heads modulo the code therefore obey the three-column rank test. Passing to a projective syndrome line is correctly handled by quotienting by its two-dimensional vector space; scaling is not confused with literal affine collinearity.

If the span of the three residual polynomials contains a nonzero codeword, its common zero set has size v<=k−1. Each remaining coordinate contributes at most two parameter incidences, even if some exceptional parameter gives the zero polynomial. Thus B(T−v)<=2(n−v), and monotonicity in v gives the stated bound floor(8ell/(2ell−5))=4 for ell>=23.

If the span contains no nonzero codeword, its projection is injective. In dimension two, distinct projective residuals have disjoint zero sets outside the common zero set. The far-point premise implies v<T because every syndrome in the same projective line has a representative in this residual span agreeing with zero on those v coordinates. Consequently B<=n−T+1=2ell+6. A one-dimensional span supplies at most one projective label and is correctly treated separately. These are counts of distinct projective labels in the second case, not counts of parameter descriptions of the same label.

## Positive component and scope

The norm-quintic family and its torsion-multiple specialization are valid constructive components. The separate `TORSION_MULTIPLE_QUINTIC_SUPPORT_COUNT_AUDIT.md` strengthens their count: for every prime ell>14, the complete two-fiber-plus-five supports number exactly ell*(ell^2−1)/2, including6072 atell23. Quintics themselves number only (ell^2−1)/2 globally.

Neither this support count nor the affine norm-pencil exclusion decides the general Phi/(L0 J_P) Padé family. Its moving denominators, subgroup dependence, shared-syndrome compatibility, challenge injectivity, and source farness remain separate obligations. The actual note maintains this distinction throughout.

Reviewed source SHA256: `e7b0a339e404b9280a73f00f1bc9592b3f59ca9e41267c72bd6193f4d4366274`.
