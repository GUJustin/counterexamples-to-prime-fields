# Depressed cubic cover: fiber patterns and a five-by-three gate

Use the Paley base word and matrices in SHIFT_ZERO_NO_GO.md. Let ψ(U)=U³+aU+γ. Assume all fourteen fibers are separable and have three distinct points. A proposed witness N(U)/(U-b) has deg N≤10, b off the domain, and N(b)≠0. Work in characteristic zero; the algebra also holds in finite characteristics where these hypotheses and the Paley incidence data hold.

Uniquely write N=A(X)+UB(X)+U²C(X), X=ψ(U), with deg A,B≤3 and deg C≤2. Put L=A+bB. If two fiber roots are matched and t is the omitted root, the selected-root quadratic is U²+tU+t²+a. Therefore

    B(x)−w(x)=C(x)t,
    A(x)+bw(x)=C(x)(t²+a),
    L(x)=C(x)(t²+bt+a).

A full fiber forces C(x)=L(x)=0 and B(x)=w(x).

If C=0 and L≠0 there are at most three full fibers and all other fibers have at most one match: at most 20 total. If C=L=0 the witness is improper. Thus C≠0 and the number f of full fibers is at most two.

The norm of L−C(t²+bt+a) under t³+at=X−γ is, writing z=X−γ,

    F=L³−aCL²+(ab²−3bz)C²L
      −C³[z²+(b³−2ab)z+a²b²].

Its degree is at most nine. It is nonzero: over the rational function field the cubic extension has basis 1,t,t², and C≠0 makes the normed element nonzero. It vanishes at each double fiber and has multiplicity at least three at every full fiber. Consequently d+3f≤9, where d counts double fibers.

If f=2, C=cH and L=Hℓ for a monic quadratic H and deg ℓ≤1. The norm is H³ times a nonzero polynomial of degree at most three. If ℓ is nonconstant its cubic leading coefficient is nonzero; if constant, the quadratic leading coefficient is −c³. Hence d≤3.

## Complete counting reduction

Let m be the number of matches, T the number above the seven triple-bucket base nodes, and Bq the number above the quad bucket. Every original cleared polynomial has degree≤10 and differs from N by properness. Summing its root bound over the seven candidates gives

    3T+4Bq=4m−T≤70.

But T≤14+f≤16, so m≥22 is impossible. We consider m=21. If f,d,s,e count full,double,single,empty fibers, then m=14+2f+d−e.

For f=2, d≤3 forces d=3,e=0. The bound T≥14 forces both full and all three double fibers into the triple bucket. All quad fibers are single. Let v be the extra triple multiplicities over baseline one; its entries are 2,2,1,1,1,0,0. The total pair bound is saturated, giving Mv=3·1. Since M is invertible and M1=3·1, v=1, contradiction.

For f=0, T≥14 forces all triple fibers double. Saturation gives Qb=4·1 for the quad multiplicity vector b. Since QQᵀ=2I+2J, Q is invertible and b=1.

For f=1, the full fiber must be triple: otherwise the norm bound d≤6 contradicts seven double triple fibers. There is no empty triple fiber and at most one single triple fiber. If all other triple fibers are double, the quad bucket has one empty and six single fibers. The pair inequalities give M e_i≤Q e_j, where i is full and j is empty. A Fano triple T_i is contained in {j}∪T_j only when i=j, since distinct triples intersect once. Thus they are paired.

If instead one triple fiber k is single, the norm bound and total count allow either all quad fibers single, or one double quad fiber j and one empty quad fiber l. The all-single case gives M(e_i−e_k)=0 by pair saturation, contradicting invertibility of M. In the remaining case pair saturation gives M(e_i−e_k)+Q(e_j−e_l)=0. With v=e_i−e_k+e_j−e_l, this says Mv=e_l−e_j. Multiplying by Mᵀ gives 2v=Mᵀ(e_l−e_j), since sum v=0. The right side has entries −1,0,1, so it must vanish, implying j=l, impossible.

Therefore the only patterns are:

1. Every triple fiber double; every quad fiber single.
2. One full triple fiber and its paired empty quad fiber; all other triple fibers double and all other quad fibers single.

The argument is integer incidence counting, not division in the coefficient field. In particular every triple fiber has at least two matches. The norm is divisible by X⁷−α⁷; in the second pattern it is a nonzero scalar times (X−αζ^i)²(X⁷−α⁷).

## Linear gate, including arbitrary a and γ

Choose an omitted root t_j on each triple fiber x_j=αζ^j, choosing arbitrarily for a full fiber. Let T and R be the unique degree≤6 interpolants of C(x_j)t_j and C(x_j)t_j². Put W=λ α^−5 X⁵. Then

    B=W+T,
    b=R5/(λ α^−5),
    A=R+aC−bW.

Thus precisely five linear equations in the three coefficients of C impose the degree caps:

    T4=0, T5=−λ α^−5, T6=0, R4=0, R6=0.

The aC term is degree≤2 and changes no equation. For a specified full fiber add C(x_i)=0. Its other two full-fiber conditions then follow. A singular linear system must be retained as an affine solution space, not discarded: numerator coefficients and b depend affinely on its free parameters. Quad-fiber matching constraints are unions of three affine hyperplanes in those parameters. Properness, pole exclusion, and exact agreements are final explicit checks. This gives a complete algebraic gate for general depressed cubic covers, but does not assert a no-go for a or γ nonzero.
