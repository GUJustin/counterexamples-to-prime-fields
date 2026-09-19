# Integrated audit: fixed-base extra errors and exact elliptic window

Verdict: PASS on both actual files named below. No source files or manuscript were edited during this audit.

## Fixed-base line lemma

The arbitrary-linear-code proof correctly constructs a linear codeword correction from two qualifying parameter points. Every third qualifying residual belongs to its error pencil because the discrepancy is a codeword of weight at most3d, strictly below minimum distance. The far-point premise forces the pencil's total coordinate support v to exceed d; counting zeros of its active coordinate linear forms yields at most v/(v−d)<=d+1 projective parameters. The argument also covers dependent received vectors, with at most one near point in the degenerate syndrome-image case. It neither assumes disjoint petals nor counts support descriptions as labels.

Puncturing2ell coordinates from RS_(n−4ell+1) leaves distance2ell. Thus the stated fixed-base bound is6 labels for d5 and7 for d6 at ell>=23. The far original agreement premise transfers in the required direction to punctured distance>d.

## Exact five-or-six window

Independently checked the Johnson polynomial and exact first-order sign substitutions for d6,d7; the d5 first-order assertion also follows immediately from alpha5>alpha6 above the unique positive root. The high-branch premise is valid: rho increases from173/264, exceeding11−3sqrt13. The constant term of the quadratic sign is negative, so there is no ambiguity between its two roots. The shift-by23 expansion for the d7 numerator is correct with all coefficients positive. The Johnson inequalities for d5,d6 hold from ell23 onward, while d<=4 fails Johnson and d>=7 fails first order.

Consequently exactly d5 and d6 are allowed at the fixed n,k. The L(6O) normalized form A3+yB1 and its monic norm sextic are correct. This additional parameter is not treated as a native split bank or a common pencil.

## Growing-budget scope

For completeness, the reason a fixed-dimension budget d=delta*ell is not a free gain is quantitative: the existing first-order agreement is n−2ell−13/2+O(1/ell), and finite Johnson is n−2ell−4+O(1/ell), whereas the weakened threshold becomes n−(2+delta)ell. Its agreement margin above k remains(2−delta)ell−1, but it has left the relevant first-order window. Retuning k downward by approximately2d would require a new witness compiler; none is asserted.

The existing canonical-plane pole obstruction also still applies to correction budgets d<=(ell−1)/2: after stripping kernel corrections, its cofactor Q has degree<=d0−1<(ell−1)/2. A zero numerator coefficient still forces Q=0 by the kernel congruence. Corrections confined to the kernel sets have d0=0 and do not weaken the rational identity. This is a statement about that existing compiler, not a general obstruction to all growing-extra models.

## Frozen reviewed hashes

- `FIXED_BASE_MOVING_EXTRA_LINE_BOUND.md`: `f896255aebec24bc527e34635c14b4538478cdd3f7832eff47aad4ebd7f0a14d`
- `FIVE_OR_SIX_EXTRA_WINDOW.md`: `f5a4b50d301af7b6da85d445eb09556e74502904815e2f4e87a452f16c3220e2`
- `NORM_QUINTIC_PADE_ELIMINATION.md`: `55c153a78af281f1cfb1c95e407777f34f06c6321081c8261de612746ee47354`
