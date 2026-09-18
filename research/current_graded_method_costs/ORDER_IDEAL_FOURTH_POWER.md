# Fourth-power ledger necessity for all coordinatewise order ideals

This extends STANDARD_SUPPORT_FOURTH_POWER.md beyond the standard derivative/total-degree caps. It remains a lower bound on the specified declared-degree numerical ledger, not on actual lists, exceptional challenges, or every first-order proof.

## Source class and hypotheses

Use the same n,D,A,m,a*,epsilon*,c0 and characteristic hypotheses as STANDARD_SUPPORT_FOURTH_POWER.md. In particular n>=12 is divisible by4, D=n/4-1, D+1<A<=n, and 0<epsilon*<=1/2000. Let S be any finite monomial order ideal in BOTH jet coordinates (u,v). Retain every X coefficient prefix

    X^x Y0^u Y1^v, (u,v) in S, x+Du+(D-1)v<mA.

The bounds B=max(u+v) and b=max v are declared reconstruction bounds. Empty coefficient prefixes can be deleted; their removal preserves the order ideal.

The following uses the already audited exact finite reduction, critical-support converse, and diagonal-compression lemma. It does not assert that arbitrary downward-Y0 supports are order ideals in both coordinates.

## Mandatory triangle lemma

If this source has positive surplus G/n-R, it contains every jet monomial of degree q<=floor(m/8), with nonempty full coefficient prefix. More strongly, its jet support has no incomplete diagonal of degree at most m/4.

Proof. Apply the exact finite reduction: remove final diagonals with L_q=mA-(D-1)q<m. The remaining order ideal S0 has positive leading benefit-minus-rank at a*, and all its benefits are positive. Let d be its first incomplete diagonal. Diagonal lengths are nonincreasing after that diagonal: the missing monomials' upward shadow grows by at least one at every step. Hence every diagonal has length at most d.

Compress each degree-q diagonal of length k_q to v=0,...,k_q-1. The audited compression preserves benefit, decreases rank, and preserves the order-ideal property. Its maximum derivative exponent is at most d-1. The positive-surplus converse V>m/4-1 therefore gives d>m/4. S0, and thus the original source, contains the claimed triangle. The multiplicity converse also gives m>c0/epsilon* and m>=16.

No height sorting is used here: its effect on degree grading is immaterial. Diagonal compression is used only to force a triangle in the ORIGINAL support, not to compare graded moments of the original and rearranged spaces.

## Eq63: identical fourth-power argument

Let P_j=sum_{q<=j}(G_q/n-R_q). For each prefix, the exact finite reduction and critical-support converse give

    P_j <=3 epsilon* m^3.

If Eq63 holds for an affine received line at challenge cap H, some prefix with j<=H is positive. Apply the mandatory triangle lemma to that prefix. With J=floor(m/8), H>=J and every q<=J has its full q+1 monomials. The existing local calculation gives

    G_q/n-R_q <=-m(q+1)/4,
    -sum_{j=0}^J P_j > m^4/12288.

Thus the constants in STANDARD_SUPPORT_FOURTH_POWER.md remain unchanged:

    H+1>m/(36864 epsilon*),
    H>m/(73728 epsilon*).

Consequently the current Eq55 regular-family declared ledger costs Omega(D^2/(epsilon*)^4), and the Eq56 list ledger costs Omega(D/(epsilon*)^2), for every coordinatewise order ideal satisfying the row test.

## Eq64: column-only test also has the fourth power

Write G_u for the number of coefficients with Y0 exponent u, G=sum G_u, and Delta=G/n-R. The affine-line Eq64 test is exactly

    (H+1)Delta > sum_u min(u,H+1)G_u/n.       (1)

In particular Delta>0, so the mandatory triangle is present and Delta<=3 epsilon* m^3. Also the source truncated to u<=H has positive surplus: (H+1) times its dimension bounds the left side of Eq64, while its local rank is at most R. The finite positive-surplus converse applied to this truncated order ideal gives H>m/4. Thus min(u,H+1)=u on the triangle q<=J.

Every triangle monomial has at least nm/8 coefficients: indeed

    (mA-Du-(D-1)v)/n >= (mA-Dm/8)/n >= m/8.

Since m>=16 gives J>=m/16,

    sum_u min(u,H+1)G_u/n
      >= (m/8) sum_{q=0}^J sum_{u=0}^q u
      = (m/8) J(J+1)(J+2)/6
      >= m^4/196608.

Combining with (1) yields

    H+1>m/(589824 epsilon*),
    H>m/(1179648 epsilon*).

The same reconstruction lower bounds therefore prove fourth-power regular-family ledger necessity when one chooses the better of Eq63 and Eq64. These constants are deliberately conservative.

## Eq64 extension to supports downward only in Y0

The column-only theorem extends further. Write h=H+1 and w_u=(h-u)_+.
Delete final diagonals with L_q<m: each contributes at most
h(G_q-nR_q)<=0 to the test margin. On the remaining saturated support,
write h_v for column heights. Its exact weighted coefficient count is

    sum_v [alpha(h_v)-(D-1)v beta(h_v)],
    alpha(d)=sum_{u<d} w_u(mA-Du), beta(d)=sum_{u<d} w_u.

Sorting heights in decreasing order preserves the alpha sum and decreases
sum v beta(h_v), while the audited saturated height-sorting lemma decreases
rank. Sorting respects every decreasing admissible height bound; hence it
preserves the saturation cutoff, the original total-degree cap, and positive
coefficient prefixes. The derivative cap cannot increase. The same H thus
passes Eq64 for a coordinatewise order ideal with no larger B,b. The proved
lower bounds transfer to the original declared ledger. This does not assert
preservation of a graded row moment. See ORDER_IDEAL_INDEPENDENT_AUDIT.md
for the independent proof and a counterexample to naive moment transfer.

## Scope

This closes the general coordinatewise monomial-downset case for both current tests. The row-test result still requires coordinatewise downward closure. The column-test result also covers supports downward only in Y0 via the preceding sorting argument. Equal-weight coefficient cutoffs, arbitrary nonmonomial spaces, global kernel dependencies, several equations, and actual-degree reconstruction require separate arguments. The characteristic restriction remains the exact local-rank audit's guard, not merely the reconstruction guard.

Primary Eq64 was checked in cached current ePrint2026/2056, Proposition5.10, page51 (`tmp/eprint-2056/paper.txt`). Diagonal compression is the proved lemma in `research/first_order_support_audit/note/main.tex`, and the inverse-margin/degree converse is `GAP_COST_CONVERSE.md` with `FINITE_LENGTH_GAP_COSTS.md`.
