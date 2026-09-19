# A multiplicative 3-net: exact quadratic embedding and its richness ceiling

2026-09-18. Bounded construction audit after [PRIME_QUADRATIC_RICH_CORE_INCIDENCE_GATE.md](PRIME_QUADRATIC_RICH_CORE_INCIDENCE_GATE.md). No broad scan, manuscript change, or universal obstruction claim.

**Outcome.** There is a direct ordinary-RS graph embedding of the roots-of-unity configuration using all three quadratic coefficients. However, neither this embedding nor its dense or polylogarithmically punctured versions supplies a bank of size sqrt(n) times a growing factor at agreement c sqrt(n). The obstruction below is specific to this multiplicative-grid candidate. It uses an inspected primary subgroup-intersection theorem, not a general prime-field incidence bound or a characteristic-zero lift.

## 1. The literal multiplicative 3-net

Let P be an odd prime and H⊂F_P^* a subgroup of order t. The t² points H×H support three classes of t-point lines:

    u=a,     v=a,     v=a u,     a∈H.

Every point is on one line from each class. There is no fourth class of complete t-point lines. Indeed, if v=a u+b has t points of H×H and a,b≠0, then aH+b=H. Summing both sides and using sum(H)=0 gives tb=0, impossible because t divides P−1. The other possible affine lines belong to the three displayed classes or miss the grid.

This exact full-class argument alone would not exclude partially retained classes. The subgroup-intersection estimate below gives the stronger fact that every other line has O(t^(2/3)) grid points in the characteristic-size range used here. Thus even a fixed positive fraction of a fourth rich class cannot be obtained merely by weakening complete retention.

For clarity, an elementary line-to-quadratic graph conversion can be made without a silent projective change. Choose κ so that x=u+κv is injective on the selected grid points, and put f(x)=x²+v. The three line classes become

    X²+(X−a)/κ,
    X²+a,
    X²+[a/(1+κa)]X.

The required nonzero denominators are explicit. For the whole grid, excluding all pair-collision values of κ and the displayed denominators is a sufficient finite condition; P greater than the number of excluded values guarantees existence. This construction has only 3t bank words and a common quadratic coefficient. The next embedding is stronger: it does not leave the bank in one affine two-dimensional coefficient plane.

## 2. A direct embedding with all three coefficients

Take any collection of unordered pairs {u,v} from H, with at most one chosen pair for each sum u+v. Define

    D={u+v: {u,v} chosen},      f(u+v)=uv,      n=|D|.

This is a well-defined received word on n distinct coordinates in F_P. It is ordinary RS of message dimension three, with no coordinate multipliers, rational codeword conversion, or projective identification. Pair collisions are resolved by selection before defining the word; different products at the same sum are never treated as separate RS coordinates.

For an arbitrary quadratic Q(X)=aX²+bX+c, agreement at the selected pair is exactly

    F_Q(u,v):=uv−a(u+v)²−b(u+v)−c=0.                 (1)

Three explicit families give many solutions in H×H:

    row family:      Q_r(X)=rX−r²,                r∈H;
    product family:  Q_c(X)=c,                    c∈H;
    ratio family:    Q_ζ(X)=[ζ/(1+ζ)²]X²,         ζ∈H\{−1}.

For the ratio family, ζ and ζ^(−1) give the same polynomial. For odd t this family has exactly (t+1)/2 distinct members: equality of its coefficients is equivalent to (ζ−ξ)(1−ζξ)=0. The complete displayed bank then has (5t+1)/2 members.

Every selected pair is on at most four members of this bank. It lies on only the row words indexed by u and v, exactly one product word, and at most one ratio word. If u+v=0 there is no ratio match. For odd t, every off-diagonal pair has four owners and every diagonal pair has three.

This owner bound is preserved by arbitrary puncturing and by arbitrary choices among colliding sums.

## 3. The precise external bound used

Konyagin--Shparlinski--Vyugin, [Polynomial Equations in Subgroups and Applications](https://arxiv.org/pdf/2005.05315), Theorem 1.2, gives the following specialization (h=1). Let R(U,V) be absolutely irreducible, nonhomogeneous, of bidegree (d_1,d_2), and suppose its lowest nonzero total-degree homogeneous part contains at least two monomials. Let g be the gcd of the nonzero differences between total degrees of its monomials. For a subgroup H of size t, if

    t≥c_0(d_1,d_2),       t≤P^(3/4)/2,

then

    |{(u,v)∈H²: R(u,v)=0}|
       <12 d_1 d_2(d_1+d_2) g t^(2/3).               (2)

The constant c_0 depends only on the two degrees. We only use bidegrees (1,1), (2,1), (2,2), with g≤2. The source allows coefficients in the algebraic closure. The size condition is equivalently 16t^4≤P³. No claim of an explicit finite value for c_0 is made here.

For a nondegenerate affine line αu+βv+γ=0 with αβγ≠0, inversion in both coordinates changes its equation to αv+βu+γuv=0, without changing its number of H² solutions. Its lowest part has two monomials, and (2) gives fewer than 24t^(2/3) points. This proves the partial-class assertion in Section 1 for all sufficiently large t under the displayed size condition. No classification theorem about abstract projective nets is needed.

## 4. All other quadratic witnesses have fewer than 384t^(2/3) matches

There is an absolute t_0 such that, whenever t≥t_0 and 16t^4≤P³, every quadratic outside the three displayed families has fewer than 384t^(2/3) matches to every selected graph in Section 2. Here t_0 can be taken as the maximum of the three constants c_0 appearing in (2), enlarged by a fixed constant. The proof treats all coefficients, not only a proposed bank.

First consider a≠0 and an absolutely irreducible F_Q. Invert both coordinates and clear the denominator:

    u²v² F_Q(1/u,1/v)
       =uv−a(u+v)²−buv(u+v)−cu²v².                 (3)

This has bidegree (2,2). Its lowest homogeneous part is uv−a(u+v)², which has at least two nonzero monomials. Absolute irreducibility is preserved: inversion is an automorphism of the Laurent polynomial ring, and neither cleared polynomial has a coordinate factor. The case b=c=0 is homogeneous and is treated separately below. Otherwise g is 1 or 2, so (2) bounds the ordered solutions by 384t^(2/3).

Next suppose a=0 and b≠0. If c=0, the original irreducible polynomial uv−b(u+v) has bidegree (1,1), two lowest-degree monomials and g=1; the bound is 24t^(2/3). If c≠0, use the invertible monomial change (u,v)↦(u,y=uv). Multiplying the equation by u gives

    uy−bu²−by−cu=0.                                 (4)

Its bidegree is (2,1), its lowest part is −by−cu, and g=1. Unless c=−b², it is absolutely irreducible, so its bound is 72t^(2/3). If c=−b², the original equation factors as (u−b)(v−b)=0 and belongs to the row family when b∈H; when b∉H it has no H² solutions.

The remaining a=b=0 case is uv=c. It belongs to the product family when c∈H and has no solutions otherwise.

It remains to justify that reducible F_Q causes no omitted rich cases. A vertical or horizontal line component forces

    a=0,   c=−b²,

by direct coefficient comparison; this is exactly the row case. A non-coordinate line through the origin, v=ζu, requires

    ζ−a(1+ζ)²=0,   b(1+ζ)=0,   c=0.

The value ζ=−1 cannot satisfy the first equation. Thus this component forces b=c=0, giving precisely the ratio family when ζ∈H. A pure homogeneous quadratic with no such ratio in H has no torus matches. Coordinate-axis components also have no torus points.

Any reducible polynomial not accounted for therefore has at most two line components, each with all three affine coefficients nonzero. Each contributes fewer than 24t^(2/3) points by the line specialization of (2), for a total below 48t^(2/3). This includes line factors defined only over the algebraic closure. All cases are covered by 384t^(2/3), and passing from ordered pairs to selected RS coordinates only reduces the count.

## 5. Consequence for partial retention and logarithmically many classes

Let A>384t^(2/3). Every quadratic with at least A matches belongs to the exceptional bank in Section 2. Since every graph point has at most four owners,

    L A ≤ 4n.                                       (5)

In particular, for A≥c sqrt(n),

    L ≤ (4/c) sqrt(n).                               (6)

The hypothesis A>384t^(2/3) holds eventually whenever n/t^(4/3) tends to infinity and c>0 is fixed. If P≥n, the characteristic-size hypothesis also follows eventually from that same condition, since P³/t^4≥(n/t^(4/3))³ tends to infinity. Thus the obstruction covers any constant-density retained grid and any retention of size t²/(log t)^K for fixed K, even if every retained pair is chosen adaptively to favor agreements.

Consequently this explicit full-coefficient roots-of-unity model cannot supply L≥sqrt(n)log n with fixed positive agreement constant. It also cannot supply the larger fixed bank needed for a superlinear label count at a constant relative gap through the fixed-bank budget in the earlier incidence note.

The scope is important. This is not a bound on arbitrary quadratic graphs over prime fields, arbitrary embeddings of unrelated nets, or arbitrary unions of multiplicative grids. Graphs retaining only n=O(t^(4/3)) points are not excluded by (5) at the square-root agreement scale, because nonexceptional conics may then meet the target. Nor has every rational or algebraic conversion of a projective net been classified. A successful escape needs a different incidence set or a mechanism outside the explicit pullback (1).

## 6. One finite embedding receipt, not an asymptotic construction

The [verifier](multiplicative_net_embedding/verify.py), [fixture](multiplicative_net_embedding/fixture.json), and [receipt](multiplicative_net_embedding/receipt.json) check the single fixed case

    P=131071,   H=<2>,   |H|=17.

All 153 unordered pairs have distinct sums, including the diagonal pairs; binary expansion gives an elementary explanation, and the verifier checks the coordinates directly. The received word f(u+v)=uv therefore uses n=153 genuine distinct prime-field coordinates. Its displayed bank has 43 distinct polynomials: 17 row words, 17 product words, and 9 ratio words. The row and ratio words each have 17 matches; every product word has 9 matches. The point-owner histogram is 17 points with three owners and 136 with four owners. The bank has affine coefficient dimension three.

This checks an exact RS embedding, rather than a geometric picture. It does not certify the asymptotic subgroup bound at t=17 (the external c_0 onset was not made explicit), and it does not enumerate all P³ quadratic witnesses. It exhibits the candidate mechanism and its bounded richness, not the requested growing-ratio construction.
