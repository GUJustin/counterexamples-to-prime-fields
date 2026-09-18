# Repeated quadratic leading factors: discriminant closes multiplicity 16--21

Status: independently audited proof and exact rank certificates. Binding shape only; this is a subcase of the repeated-leading-factor branch, not a complete benchmark improvement. Characteristic is odd (as at the target).

Use the constants and necessary own-system rank inequality in REPEATED_LINEAR_HELPER_GATE.md. Thus A=lc_R F has deg_Y43, weighted degree at most43w+12, and its leading Y coefficient has X-degree at most12. Assume

    A=G^e H, deg_Y G=2, 13<=e<=21, h=deg_Y H=43-2e.

Weighted additivity and wt(H)>=h w give e(wt(G)-2w)<=12. Hence wt(G)=2w. Its leading Y coefficient is independent of X; normalize it to1 over k(Z). Then G and H belong to k(Z)[X,Y], H's leading Y coefficient has X-degree at most12, and

    deg_X Disc_Y(G)<=2w.

Discard the at most12 nodes where that leading coefficient of H vanishes. At every remaining node the leading coefficient of A is a unit, hence contact a<=43.

## Local discriminant cost

Let delta=ord_x Disc_Y(G), assuming this discriminant is not identically zero. At each good node,

    delta >= 1[a>=44-e] + 1[a>=56-e].             (1)

First threshold: specializing X=x, the received Y-root has multiplicity at least a in A, by the Newton contact lemma at t=0. If G has at most a simple root there, A's multiplicity is at most e+h=43-e. Thus a>=44-e forces both roots of G to specialize to the received symbol, so delta>=1.

Second threshold: suppose delta=1 and translate the received symbol to0. Write G=Y²+b(t)Y+c(t). Both roots specialize to0, so ord b>=1. Since char!=2 and ord(b²-4c)=1, ord c=1. The two root valuations are therefore exactly1/2 (equivalently, the Newton polygon is the single segment from(0,1) to(2,0)). No general pointwise root-slope inference is being made.

In A=G^e H, choose the2e roots supplied by G. Their valuations sum to e. The sum of the smallest2e root valuations is consequently at most e, regardless of the positions of H's roots. As the leading coefficient of A is a unit, this sum is the Newton-polygon ordinate at Y-degree h. But the contact support lemma requires that ordinate to be at least

    max(0,(a-h)/2,a-12-h).

At a>=56-e, its last term is at least e+1, a contradiction. Thus delta cannot equal1, proving (1). The argument uses only a quadratic Newton segment and integral coefficients; it requires no general Puiseux expansion or tameness assumption beyond odd characteristic.

## Global rank contradiction

For a in0,...,43 put c_e(a)=1[a>=44-e]+1[a>=56-e], and

    l=43-e,
    lambda=max(R(55-e)-R(l),(R(43)-R(l))/2).

The script verifies pointwise R(a)<=R(l)+lambda*c_e(a). By (1), the total c_e over good nodes is at most deg DiscG<=2w. The bad nodes contribute at most12R(67). Therefore

    sum_x R(a_x) <= n R(l)+2w lambda+12 R(67).

| e | rank upper bound | required lower bound |
|---:|---:|---:|
|15|6966729152812|6802316684344|
|16|6591448479720|6802316684344|
|17|6227151378396|6802316684344|
|18|5873841256712|6802316684344|
|19|5531521522540|6802316684344|
|20|5200195583752|6802316684344|
|21|5026262663038|6802316684344|

Thus all e=16,...,21 are impossible when DiscG is nonzero. This particular bound does not exclude e15. The script checks every relevant contact value using exact fractions; no optimization library is needed.

If DiscG is identically zero, odd characteristic and monicity give G=(Y-P)² with P in k(Z)[X], deg_X P<=w. Then A has a linear factor of multiplicity2e>=32, and REPEATED_LINEAR_HELPER_GATE.md forces the affine received-word pencil. Thus a quadratic factor of multiplicity at least16 either contradicts own-system universality or yields that pencil. In particular, an irreducible quadratic factor of multiplicity at least16 is excluded outright.

The earlier feasible along-candidate order profile for e21 remains correctly feasible for the inequalities tested there. The new discriminant resource eliminates it: its high-contact nodes demand more discriminant zeros than a degree2w polynomial can possess. No claim is made about e<=15, higher-degree factors, or a replacement of the complete retained normal cost.

Artifacts: repeated_quadratic_discriminant_gate.py/json. The proof is based on the root's two-threshold observation, checked independently here.
