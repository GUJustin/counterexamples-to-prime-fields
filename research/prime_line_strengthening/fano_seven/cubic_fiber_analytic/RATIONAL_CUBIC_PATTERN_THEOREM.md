# Rational cubic covers: complete patterns on the squarefree-denominator stratum

Work over an algebraically closed field of characteristic zero or greater than three. Let R,S be coprime binary cubics, S squarefree, ψ=R/S. Pull back the fourteen finite base nodes of one of our exact seven-cubic banks. Assume every selected fiber is unramified, hence consists of three distinct points. The received value at a lifted point is S³ times its base value, interpreted as a section of O(9).

Let ell be a nonzero binary linear form with root b outside these42 points. A degree10 binary form N is a proper candidate if N(b)≠0. Its matches satisfy N=ell S³w. This note proves that the SAME two multiplicity patterns previously classified for polynomial cubic covers exhaust all candidates with at least21 matches. The squarefree-S hypothesis is essential to this proof's scope; the pole may coincide with a root of S, including the chosen affine infinity.

## Full fibers: a homogeneous splitting

The subspace R H⁰(O(1))+S H⁰(O(1)) of binary quartics has dimension4: a relation RL1=SL2 would force R to divide a linear form. Choose a quartic Q outside it. Every degree10 binary form has a unique decomposition

    N=U B3(R,S)+V A3(R,S)+Q C2(R,S),

where A3,B3 are binary cubics in the base variables and C2 is a binary quadratic. Dimensions are4+4+3=11. Independence follows by reducing at the generic cubic fiber: a relation with nonzero C2 would place Q in the scalar extension of the fixed four-dimensional quartic subspace; then the remaining linear form also vanishes. Dimension gives spanning.

On a full fiber R−xS, division by the nonvanishing S² gives

    Q C2(x,1)+S[U(B3(x,1)−d1 w)+V(A3(x,1)−d0 w)]=0 mod(R−xS),

where ell=d1U+d0V. If C2(x,1)≠0 this puts Q in R H1+S H1, contradiction. Thus C2 vanishes at every full fiber, so a nonzero C2 permits at most two.

If C2=0, every nonfull fiber has at most one match: the residual equation is linear in U,V. Full fibers are zeros of d1A3−d0B3, a base cubic. If that cubic vanishes identically, N is divisible by ell and is improper. Otherwise there are at most three full fibers and at most20 total matches. Hence every relevant proper candidate has C2≠0 and f≤2.

## Double fibers: the genus budget, including cancellation

First assume b is outside S=0.

Put g=N/(ell S³). The map (ψ,g) from P¹ to P¹×P¹ is birational onto its image. Indeed its degree divides [k(U/V):k(ψ)]=3. Degree3 would put g in k(ψ). But g has a simple pole at b, and b is the only pole of g in the finite fiber ψ=ψ(b). A pullback of a pole by a degree3 map has total pole multiplicity divisible by3 on that fiber, contradiction.

Let s1,s2,s3 be the distinct roots of S, let vi=min(ord_si N,3), and mi=3−vi. The degree of g is d=10−Σvi, since ell does not cancel. The image has arithmetic genus (3−1)(d−1)=2d−2, and its normalization is P¹. At every si with mi>0 the image meets (∞,∞). Since ψ has a simple pole there, its reciprocal is a local parameter, and the reciprocal of g has order mi. Pairwise intersection multiplicity of these smooth branches is at least min(mi,mj). Branches with mi=0 require no charge. At a double matched finite fiber there are two distinct unramified branches meeting, costing at least1 in the delta invariant; at a full fiber three branches cost at least3. Thus

    d_double+3f ≤18−2Σvi−Σ_(i<j)min(3−vi,3−vj)
                 =9−Σ_(i<j)min(vi,vj) ≤9.

All charges are at distinct image points except the three specified infinity branches, and additional singularities only strengthen the inequality.

If b is a root of S, properness gives pole order4 at b and orders3−v2,3−v3 at the other roots. The degree is10−v2−v3. Birationality still holds: a function in k(ψ) would have equal pole orders at all three simple poles of ψ, impossible for4 versus at most3. Infinity delta is at least9−v2−v3−max(v2,v3), leaving finite budget at most9−min(v2,v3)≤9. Thus the degree-nine budget holds for every ell. In fact it alone forces f≤2 for a21-match witness: f≥4 is impossible, while f=3 forces d=0 and permits at most14+2·3=20 matches. The homogeneous splitting above is therefore supplementary, not needed for this conclusion.

## Two full fibers improve the remaining budget

Suppose x1,x2 are full. Choose the linear base polynomial L interpolating their values. Then

    N−ell S³ L(ψ)=(R−x1S)(R−x2S) M4

for a binary quartic M4, because the two entire fibers divide the left side. Let H(X)=(X−x1)(X−x2). Then

    g=L(ψ)+H(ψ) h,   h=M4/(ell S).

At other finite fibers, equality of g-values is equivalent to equality of h-values. The pole at b remains proper, because b is not in either selected fiber. The same simple-pole argument makes (ψ,h) birational. If V of the three roots of S cancel from h, its degree is4−V; the remaining3−V simple poles give at least binomial(3−V,2) infinity delta. Hence the number of remaining double fibers is at most

    2(4−V)−2−binomial(3−V,2) ≤3   (V=0,1,2,3).

If b is a root of S, the reduced h has pole orders2 at b and1−v2,1−v3 at the other two roots, with vi in {0,1}. Unequal pole orders again prove birationality. Its degree is4−v2−v3; the infinity delta is at least3−v2−v3−max(v2,v3). The finite budget is at most3−min(v2,v3)≤3. Thus f=2 implies d_double≤3 for every ell, exactly the strengthening needed by the earlier incidence classification.

## Consequence and computation interface

The pair bounds with the seven old degree10 sections remain valid: properness prevents equality with an old ell·S³P_i(ψ). Together with the proved f and d bounds, the prior Paley and orbit2 incidence calculations apply without change. Therefore every triple fiber has at least two matches, with precisely the previously listed full/empty exceptions. Choosing one omitted point on each triple fiber and imposing the other fourteen equalities gives a complete homogeneous 14×13 linear gate in the eleven coefficients of N and two coefficients of ell, on this stated stratum. Properness, domain exclusion, and actual quad matches must still be checked. This theorem proves completeness of that search, not existence of a candidate.
