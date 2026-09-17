# Primary A repair: bounded exact audit

Target agreement is 181275, n=262144, w=131071. This is an interpolation-dimension audit, not a completed benchmark certificate.

## Fixed quotient cap

`primary_A_repair.py` checks 9,283 pairs with 1<=m<=115 and 0<=s<=floor(mA/w), using the one-residue coefficient formula and the general rectangular local rank sum. Unlike the earlier audit, this includes 2s>m. For every pair the surplus is affine in L throughout L>=max(m+s-1,floor(mA/w)); checking its value at this lower endpoint and its slope decides feasibility for every L in this range. None is feasible.

For m115 (quotient159), the original L274277 gives:

| s | surplus | slope per extra L |
|---|---:|---:|
|35|−1455824819235|−3164760|
|36|−2181178198995|−5790130|
|37|−4309317795497|−13533434|

The script also checks the truncated-weight escape: m116 with D=160w−s for every 0<=s<=159, retaining the standard quotient-cap shape D+s<=160w. None is feasible in the affine-L regime. Larger m with this same maximal D and s have nested, stronger contact conditions, hence cannot improve the dimension surplus. This does not cover arbitrary nonstandard supports or small-L regimes outside the stated affine range.

The existing `primary_tradeoff.json` identifies positive expanded-quotient examples: m117,s36,q161 needs L613675; m118,s36,q163 needs L176421. These change the geometric ranges, and cannot be substituted into a frozen old receipt without rebuilding affected rows. Positivity alone does not preserve every downstream nullity requirement.

## There is no uniform one-point rank saving for the unchanged source

For the actual RCN119 coefficient box B(M,L,s), the contact map kernel consists exactly of polynomials divisible by (Y−V)^h. If a nonzero f=(Y−V)^h g belongs to B(M,L,s), degree additivity in Y, in V, and in total degree forces g into B(M−h,L−h,s−h). Conversely every such g works. Therefore the subtraction used by `contactRankBound` is the exact rank of the full-box contact map over every field, rather than merely a possibly loose kernel estimate. If h>M the kernel is zero; replacing h by min(M+1,h) preserves this rank.

For primary A's unchanged full weighted source, its extraction onto the direct sum of local coefficient boxes is also surjective. At x=u0=u1=0, the global monomial X^(r−i) Y^i V^j Z^z maps to exactly the local monomial Y^i V^j Z^z in block r, and zero in every other block. Its weighted degree is r+(w−1)(i+j), whose maximum for r<m, i<=r, j<=s is

    (m−1)+(w−1)(m−1+s).

For m115,s35 this is 19529544, strictly below target weighted cutoff 20846625. Thus every local box monomial is present, simultaneously across all blocks. The source support is preserved by invertible translations of X and by Y -> Y + u0 + u1 Z: these decrease weighted degree, preserve the total Y,V,Z cap, and preserve the V cap. Translating therefore proves the same surjectivity at every local point and received value.

Consequently the **one-point** rank is exactly 50068355280 for the unchanged primary A support, also at the target. No improvement obtained solely by lowering that uniform local rank number is available. This does NOT assert independence between constraints at different domain points. New global dependencies, or a genuinely different support whose restricted local images are smaller, remain possible.

At the unchanged shape, dimension positivity needs a saving of at least 1455824819236 in the global rank upper bound (and more if a prescribed positive nullity is required). Hypothetically distributed uniformly, this would require at least 5553531 saved constraints per point, but the exact local-rank result rules out that particular mechanism.

## Validation and limitations

The count formulas were previously matched to all three authoritative baseline kernel counts. The expanded audit ran in under two seconds and below 22 MiB under the 384 MiB / 60 second watchdog. Exact results and the resource record are saved beside this note. No Lean rebuild, source-provider port, geometric receipt regeneration, or improved score is claimed.

## Small quotient follow-up

`primary_A_small_quotients.py` checks qcap160–163, m115–119, all s<=qcap, choosing maximal D=min(mA,(qcap+1)w−s). qcap160 has no feasible choice, including deliberate weighted-degree truncation at higher m. qcap161 first works at (117,35,1118298) or (117,36,613675); qcap162 brings no better choice. qcap163 works at (118,35,380088) or (118,36,176421). These are minima within the enumerated scope and affine-L regime, not arbitrary-support lower bounds.

## Actual downstream role of A

Pinned primary `MovingFiberSelection6811.lean` shows the selected pair is drawn from TCap and B, not A. A is used to separate factors that divide its entire kernel from the complementary factors. The universal-factor aggregate inherits r<=s_A and y<=q_A. Its total cap comes from TCap, not A.L. On a retained total cap9275, the old4970 (r,v) rows become5040 for (s_A,q_A)=(35,161), or5238 for (36,163).

For complementary factors, `MovingFiberInitialCore6811.lean` uses A as the right helper with caps (L_A,q_A,s_A). The generic linear-majorant theorem yields coefficients

    cT=ceil((n−w)(ay*s_A+ar*q_A)/gap),
    cY=ceil((n−w)(ar*L_A+az*s_A)/gap)+(errors+1)*s_A,
    cR=ceil((n−w)(ay*L_A+az*q_A)/gap)+(errors+1)*q_A,

where ay=1+2w*185, ar=w*(2*40−1), az=1+2w*9275 and gap=A−w. These reproduce all three old potential coefficients exactly. The complement greedily maximizes cT*t+cY*y+cR*r in the remaining wide box (9275−t_p,185−y_p,40−r_p), with 0<=r<=y<=t. All coefficients are nonnegative, so the same greedy formula remains valid.

`primary_A_potential.json` records resulting coefficients and exact comparisons. At the old binding aggregate (r,y,t)=(35,159,9249):

| A-source choice | complement change versus baseline |
|---|---:|
|q161,s35,L1118298|+1127705357818597|
|q161,s36,L613675|+453720828166349|
|q163,s36,L176421|−130365302389024|
|q163,s35,L380088|+141556003128757|

Thus q163,s36 has a genuine favorable direct-helper contribution. This does not establish its full ledger: expanded phase potentials/domain, source B/TCap repairs, and corresponding base receipts remain necessary. Conversely the q161 increases defeat the currently frozen best phase margin at that row, but are not impossibility proofs against different phases or sharper complements.

A's current use requires only positive nullity. TCap is different: its cap9275 is proved by nullity exceeding the coefficient count of the quotient box of total degree L−9276. Merely finding positive nullity after increasing TCap.L does not preserve this total cap. This distinction is explicit in Selection's `common_TCap_total_le`.
