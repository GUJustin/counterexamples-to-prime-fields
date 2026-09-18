# Two curvature-linear sources: exact elimination and conditional routing cost

Status: the algebraic elimination, contact, and degree ledger below are proved. The existence of two sources with the required factorwise nonzero determinant is NOT proved. The numerical costs are conditional helper costs, not a benchmark certificate.

Let Q_i=A_i V+B_i, i=1,2, be second-jet sources of local order m≥3, with source weights (1,w,w−1,w−2), weight strictly below B=mA, R-degree≤S, total jet degree≤J, and total jet-plus-challenge degree≤L. Define

    E=A_1 B_2−A_2 B_1.

Every high-agreement candidate satisfies both Q_i as polynomial identities by the ordinary source root count. Consequently it satisfies E(X,P,P′,z)=0. Thus E is an already-known first-order identity if nonzero; no second root-count inference is required.

## Exact degree caps

Since extracting the V coefficient removes one jet and one joint-degree unit, and removes weight w−2,

    deg_R E≤2S,
    deg_(Y,R) E≤2J−1,
    deg_(Y,R,Z) E≤2L−1,
    wt_(1,w,w−1) E≤2B−w.

The final weight bound uses integer source weights: wt A_i≤B−w+1 and wt B_i≤B−1. These caps are valid without assuming generic coefficients or absence of cancellation.

## Exact first-jet contact inherited by the determinant

At a coordinate, set Y=w_x+tR−t²V+t³E3. The source identity is Q_i=0 mod t^m. Differentiating with respect to E3 gives t³(Q_i)_Y=0 mod t^m, hence (Q_i)_Y has order≥m−3 under that substitution. Differentiating with respect to V gives

    A_i−t²(Q_i)_Y=0 mod t^m.

Thus A_i has order≥m−1. Specialize E3=0 and V=−E1, so Y=w_x+tR+t²E1 becomes the first-jet substitution. Each Q_i has order≥m and each A_i has order≥m−1 there. Since

    E=A_1 Q_2−A_2 Q_1,

the determinant has first-jet contact at least 2m−1.

A purely local improvement to 2m is false. The pair

    Q_1=t^(m−3)(Y−tR+t²V),   Q_2=t^m

satisfies the second-jet order-m condition, but its determinant is t^(2m−1). This is a local sharpness example, not a claim that these polynomials fit a useful global source box on every evaluation coordinate.

## The precise missing avoidance theorem

Let R0=k[X,Y,R,Z], let F be an irreducible first-order factor, and let U be the k-linear source kernel. Map every Q=A V+B to its coefficient pair (A,B) over the field Frac(R0/(F)). There exist Q_1,Q_2 in U with F not dividing their determinant if and only if these coefficient pairs span dimension two over this field.

This is stronger than linear independence of Q_1,Q_2 over k and stronger than generic rank two over Frac(R0). A source space can have large dimension but rank one modulo F. A concrete structural mechanism is

    U contained in the V-linear part of the ideal (F,delta F),
    delta F=F_X+R F_Y+2V F_R.

Modulo F, every such source can be proportional to delta F; its coefficient pairs have rank at most one. Every determinant then contains F, although individual sources need not contain F. This is the natural first-order prolongation obstruction. It cannot be replaced by the old dichotomy that a factor divides every source or has a coprime source witness.

Any successful second-jet ledger therefore needs either a dimension theorem forcing rank two modulo each relevant F, or a separate bound for the rank-one/prolongation alternative. Global kernel dimension alone does not establish this.

## Conditional benchmark ledger

Use m=128,S=40,J=177,L=5515, n=262144,w=131071,A=181275. The determinant has

    first-jet contact≥255,
    right helper caps (Y,R,Z)=(353,80,11029),
    inclusive weighted degree≤46,275,329.

The ordinary contact root budget is255*A=46,225,125, so the weight exceeds that budget by50,204. This does not invalidate the known identity established from the two original sources. It does prevent silently using the old source-existence adapter with these parameters.

For a regular left factor at the critical singleton context (Y,R,Z)=(55,12,3261), the existing mixed costs are

    (393228,1757728,8636),

all below the pinned characteristic2130706433. Substitution into the existing asymmetric coprime known-identity helper formula gives

    47,911,200,271,295.

Even the older symmetric helper formula gives255,827,104,666,783. Both are much smaller than the current critical singleton cost288,191,873,412,750,740 (the full target MCA allowance is274,980,720,453,263,170). Exact evaluations at three contexts are in conditional_resultant_cost.json. The source for the formulas is the cached primary UnequalParameters/AsymmetricHelper definitions, not a percentage extrapolation from source rank.

These values demonstrate that proving factorwise rank-two avoidance could be worthwhile; doubling the source's degree does not by itself make the helper cost fatal. They do not establish the avoidance premise, handle every exceptional factor, or constitute a full propagated benchmark receipt.
