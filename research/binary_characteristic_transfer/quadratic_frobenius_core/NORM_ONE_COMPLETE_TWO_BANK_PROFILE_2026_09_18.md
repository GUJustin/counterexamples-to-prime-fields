# Complete norm-one list profile above four agreements

September 18, 2026. An exact completion of one received word's bank. No new codewide upper bound, prime-alphabet construction, or better.codes claim. The independent audit is NORM_ONE_COMPLETE_TWO_BANK_INDEPENDENT_AUDIT.md. Integrated into Theorem N.25.

Let p≥5 be prime, E=F_(p³), L=p²+p+1, and

    D={x in E*: Norm(x)²=1}, |D|=N=2L,
    f(x)=x^(2p+2).

The following is the complete list profile for integer thresholds T≥5:

* 5≤T≤p+1: exactly 3L quadratics;
* p+2≤T≤2p+2: exactly L quadratics;
* T>2p+2: no quadratics.

The two disjoint banks are

    P_a(X)=aX²-a^(p²+1),       Norm(a)=-1,
    Q_u(X)=(uX-u^(p²+1))²,    Norm(u) in {1,-1}.

There are L members P_a, each with exactly 2p+2 matches, and 2L members Q_u, each with exactly p+1 matches. EVERY other quadratic has at most four matches. Nothing is asserted here about the exact counts at thresholds one through four.

## A useful semilinear splitting identity

For any u≠0, the equation

    x^(p+1)=u x-u^(p²+1)

has exactly p+1 distinct nonzero roots in E. Substitution x=u^(p²)z gives z^(p+1)-z+1=0. The map z↦1-1/z has third iterate the identity; neither zero nor one is a root. Iterating z^p=1-1/z shows z^(p³)=z. The derivative z^p-1 has no common root with the polynomial. Moreover z^(p²)=1/(1-z), so Norm(z)=-1 and every root x has

    Norm(x)=-Norm(u).

More generally, for v≠0, the equation y^(p+1)=u y+v has more than two roots in E only when the threefold twisted fractional linear map is the identity. Multiplication of the matrices [[u^(p^i),v^(p^i)],[1,0]], i=2,1,0, gives precisely u≠0 and v=-u^(p²+1). In the nonidentity case it has at most two fixed points. For v=0 there is at most one nonzero root. These are the same semilinear facts used in norm_one_direct_list.tex.

## Even quadratics

For P=aX²+c, put y=x². Then y ranges over the norm-one group and every y has two square roots in D. Unless c=-a^(p²+1) with a≠0, the preceding observation gives at most two y-roots, hence at most four matches. In the exceptional case all y-roots have norm -Norm(a); thus a match in the norm-one group requires Norm(a)=-1. These and only these even quadratics form the P_a bank, with exactly 2p+2 matches.

## Non-even quadratics: the quartic identity is equivalent to the new bank

Write Q=aX²+bX+c with b≠0 and put

    r(X)=1-a^p Q(X)-c^p X².

At any matching x in D, x² Q(x)^p=1. Consequently

    r(x)=b^p x^(p+2),

and the polynomial

    r(X)²-b^(2p)X²Q(X)

vanishes at every match. It has degree at most four. If it is nonzero, Q has at most four matches.

Suppose instead that it is identically zero. Its constant term forces r(0)=0, so

    H(X)=r(X)/(b^p X)

is a polynomial of degree at most one and Q=H². Since b≠0, write H=uX+v with u,v≠0; then a=u²,b=2uv,c=v². The defining identity r=b^p XH becomes

    1-u^(2p)(uX+v)²-v^(2p)X²
        =2u^p v^p X(uX+v).

Its constant coefficient gives (u^p v)²=1. Its linear coefficient, after division by 2u^p v, gives

    v^p=-u^(p+1).

Raising to p² in E yields v=-u^(p²+1), and hence u^p v=-Norm(u). Therefore Norm(u)²=1. The quadratic coefficient then holds automatically: both sides equal -2u^(2p+2). Conversely these conditions give the entire identity, not just necessary coefficients.

Thus the zero-quartic branch is exactly Q_u above. This argument establishes an actual square over E, not just a square over an algebraic closure or a zero discriminant.

At a match the original UNSQUARED identity also gives

    x^(p+1)=H(x).

Conversely every root of that equation lies in D when Norm(u)=±1 and satisfies f(x)=H(x)²=Q_u(x). Hence these are exactly the p+1 matches. The opposite sign H cannot create additional matches; the unsquared identity already fixes the sign.

## Distinctness and counts

The norm map E*→Fp* has fibers of size L. Thus there are 2L allowed u. If Q_u=Q_v then H_v=H_u or H_v=-H_u in E[X]. The first case forces v=u. In the second case v=-u from the linear coefficient, but

    H_(-u)=-uX-u^(p²+1)

is not -H_u, since p²+1 is even, u≠0, and p is odd. Thus all 2L quadratics are distinct. Their nonzero linear coefficients distinguish them from the even bank. This proves the claimed complete profile.

## Small-field validation and scope

The existing exhaustive receipt check_norm_one_lists.json already records:

* p=5: 31 polynomials at agreement 12, 62 at agreement 6, all others at most four;
* p=7: 57 polynomials at agreement 16, 114 at agreement 8, all others at most four.

No exhaustive enumeration is repeated. The new verify_norm_one_two_bank.py/json only constructs the proposed 2L members, checks distinctness and their exact supports, and compares their number with that archived histogram. The p=3 algebra also works, but its second level p+1=4 is indistinguishable from other quartic-bound cases; the stated threshold profile is deliberately for p≥5.

The extra bank appears at thresholds well below the first-order-to-Johnson comparison previously published. It completes the algebraic classification of this particular received word above four matches; it does not strengthen the uniform maximum-list bound or establish a new growing prime-field line construction.
