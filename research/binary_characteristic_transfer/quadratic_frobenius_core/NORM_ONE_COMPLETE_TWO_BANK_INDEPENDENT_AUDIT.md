# Independent audit of the complete two-bank norm-one profile

September 18, 2026. **PASS.** Independently checked the algebra in `NORM_ONE_COMPLETE_TWO_BANK_PROFILE_2026_09_18.md` against the classification in `norm_one_direct_list.tex`. No main-fragment edits or exhaustive computations were made for this audit.

Let p>=5, E=F_(p^3), L=p^2+p+1, D={x!=0:Norm(x)^2=1}, and f(x)=x^(2p+2). The complete list at every integer threshold T>=5 is

    3L when 5<=T<=p+1;
     L when p+2<=T<=2p+2;
     0 when T>2p+2.

The L-member even bank is P_a=aX^2-a^(p^2+1), Norm(a)=-1. The additional 2L-member bank is

    Q_u=(uX-u^(p^2+1))^2, Norm(u)=1 or -1.

Every P_a has exactly 2p+2 matches, every Q_u exactly p+1, and every other polynomial of degree at most two has at most four.

## Necessity and coefficient comparison

For Q=aX^2+bX+c with b!=0, put r=1-a^p Q-c^p X^2. At a match x, the domain condition and f(x)=Q(x) imply x^2 Q(x)^p=1 and therefore r(x)=b^p x^(p+2). The degree-at-most-four polynomial r^2-b^(2p)X^2 Q vanishes at every match. Unless it is identically zero, the four-match bound follows directly.

In the identity case, X divides r and H=r/(b^p X) is an actual polynomial over E with H^2=Q. In particular this is a square over E, with its sign fixed by r, not merely a zero-discriminant assertion. Since b!=0, write H=uX+v with u,v!=0. Then a=u^2, b=2uv, c=v^2. The constant and linear coefficients of

    1-u^(2p)(uX+v)^2-v^(2p)X^2
      =2u^p v^p X(uX+v)

give, respectively,

    (u^p v)^2=1,
    v^p=-u^(p+1).

The second equation gives v=-u^(p^2+1), by raising to p^2 and using u^(p^3)=u. Thus u^p v=-Norm(u), and the first equation is exactly Norm(u)^2=1. Conversely these conditions satisfy every coefficient: the quadratic coefficients on both sides are -2u^(2p+2). This proves both directions of the zero-quartic classification, including the norm constraint.

## Exact roots and the sign issue

For any u!=0, substitute x=u^(p^2)z in

    x^(p+1)=u x-u^(p^2+1).

The equation becomes z^(p+1)-z+1=0. Its roots are nonzero and different from 1. The identity z^p=1-1/z and the third iterate of this fractional linear map show that all roots lie in E. The derivative z^p-1 has no common root with the polynomial, so there are exactly p+1 distinct roots. Also z^(p^2)=1/(1-z), giving Norm(z)=-1 and Norm(x)=-Norm(u). For either allowed norm of u, every root therefore lies in D.

These roots are matches for Q_u. Conversely, every match must satisfy the original unsquared identity r(x)=b^p x^(p+2). Since r=b^p XH and b,x!=0, this forces H(x)=x^(p+1). Squaring introduces no additional minus-branch matches. Hence the agreement count is exactly p+1.

## Exhaustion, distinctness, and finite guards

The even case is also exhaustive. Writing y=x^2 reduces it to y^(p+1)=a y+c. If c!=0, the threefold Frobenius-twisted fractional linear map is the identity precisely when a!=0 and c=-a^(p^2+1); otherwise it has at most two fixed points. One can check necessity from the lower-left matrix-product entry a^(p+1)+c^p. In the identity case its y-roots all have norm -Norm(a). Thus a root in the norm-one group requires Norm(a)=-1, giving exactly the original bank. If c=0 there is at most one nonzero y-root. Every other even quadratic consequently has at most four x-matches.

There are L elements of each nonzero norm, so the proposed new bank has 2L parameters. Equality Q_u=Q_(u') implies H_(u')=H_u or H_(u')=-H_u in E[X]. The first case gives u'=u. The second would require u'=-u, but H_(-u)=-uX-u^(p^2+1) differs from -H_u because p is odd and u!=0. Thus the parametrization is injective. Its linear coefficient -2u^(p^2+2) is nonzero, proving disjointness from the even bank.

All guards are satisfied for p>=5. In particular p+1>4 separates the new bank from the remaining quartic cases. The algebra remains valid at p=3, but does not classify the entire four-match stratum there. Degree(f-Q)=2p+2 gives the empty list above the top threshold.

The archived complete census agrees: p=5 has 62 quadratics at agreement 6 and 31 at agreement 12; p=7 has 114 at agreement 8 and 57 at agreement 16, with every other quadratic at agreement at most four. The new targeted receipt `verify_norm_one_two_bank.json` independently constructs these 62 and 114 distinct proposed members and checks their exact supports. No full census was repeated.

This is an exact classification for one received word over the cubic extension field. The additional bank occurs below the previously analyzed first-order/Johnson interval; it does not improve the uniform maximum-list bound, establish prime-alphabet transfer, or change the better.codes benchmark.
