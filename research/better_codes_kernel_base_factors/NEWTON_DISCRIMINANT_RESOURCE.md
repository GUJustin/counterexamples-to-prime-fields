# Newton contact and a global leading-coefficient resource

Status: the local standard-basis lemma and exact numerical inequalities are checked independently. The discriminant lemma is undergoing independent audit. This is not a replacement for the retained normal term.

Work over K=k(Z). At a coordinate x write t=X-x and Y'=Y-w_x. Put N=Y'-tR. The standard monomials

    t^i Y'^k N^j R^l, with i*l=0,

form a basis: the only rewriting relation is tR=Y'-N. Their highest physical R terms are distinct, and their leading first-jet terms are t^(i+k+2j) R^(k+l) E^j. For fixed j, the pair (i+k,k+l) determines i,k,l uniquely under i*l=0. Thus contact is diagonal in this basis. If deg_R F=r and F has contact a, every term t^u Y'^k of its leading R coefficient satisfies

    u+k+min(u,r) >= a.                    (1)

Indeed j+l=r and u=i+j force j=min(u,r). This is valid in every characteristic.

For A=lc_R F of Y-degree q, the lower Newton polygon therefore lies above the convex envelope with coefficient ordinates

    max(0, ceil((a-k)/2), a-r-k).

The discriminant consequence, including nonunit leading coefficient, is

    ord_x Disc_Y(A) >= Phi(q,r,a)
    Phi(q,r,a)=sum_{j=1}^{q-1} max(0,a-j,2(a-j-r)),

provided the discriminant is nonzero. The identity behind this is the root-valuation bound ord Disc >= 2 sum_{j=1}^{q-1} NP(j); the leading-coefficient contributions cancel. This avoids deleting zeros of lc_Y A. When q>=a the bound is

    D_r(a)=a(a-1)/2                         (a<=2r),
    D_r(a)=a(a-1)-r(2a-2r-1)               (a>=2r).

If wt F<=v, then with Delta=v-r(w-1)-qw, weighted homogeneity of the discriminant gives

    deg_X Disc_Y A <= q(q-1)w+(2q-2)Delta.

Delta cannot be replaced by the actual X-degree of lc_Y A without additional coefficient information.

## Nonuniform own-system consequence at the binding shape

Assume the exact own-system caps v=55w,y=55,r=12,t=3261, n=262144,w=131071, and q=43. Its ambient dimension is C=6802316684345. Universality implies sum R(a_x)>=C-1, with R the explicit local rank bound in OWN_SYSTEM_RIGIDITY.md. Write b_x=ord_x lc_Y A. Then a_x<=43+2b_x and sum b_x<=12; hence 0<=a_x<=67.

The exact rational inequality, checked at all 68 possible integer contact orders, is

    Phi(43,12,a) >= (27/715793)R(a)
                     -5633856/55061 - (640622/55061)b,

whenever b>=max(0,ceil((a-43)/2)). Summing proves

    deg Disc >= ceil(164462990425824/715793)=229763340.

The weighted upper bound is 236715234, leaving at most 6951894 degree after the forced node contributions. The executable certificate is newton_discriminant_gate.py/json. This uses the full nonuniform profile; assuming average contact at least 40 is unnecessary and unjustified by the rank inequality alone.

## Exact scope and missing bridge

This is a dichotomy: either Disc_Y A is identically zero, or the stated finite divisor budget holds. Irreducibility of F does not imply squarefreeness of its leading R coefficient. No proper helper follows merely from the zero-discriminant alternative.

The retained normal term is a mixed flag intersection of F, its first-tail cut, and a rational-coordinate pole budget over k(X), in variables Y,R,Z. The new divisor instead belongs to the projection of A(X,Y,Z)=0 onto X over k(Z). The existing normal proof has no discriminant summand that can simply be replaced by 6951894. A required new theorem would charge the active tail components or their pole budget to this residual X-divisor, while treating repeated A and points at infinity. No such charge has been proved here.

Nor is residual polynomial-discriminant degree itself a genus/different bound: normalization can remove large index contributions, while some local discriminant contribution remains actual ramification. Any conductor argument must explicitly use the index-discriminant identity and account for the nonmonic model and infinity.
