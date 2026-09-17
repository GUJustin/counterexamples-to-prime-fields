# Independent audit of weighted support and quotient erosion

2026-09-17. These are valid dimension/routing ingredients, not a better.codes certificate.

Use source monomials X^x Y^i R^j Z^z with i+kappa*j<=H, j<=S, i+j+z<=L and x+w*i+(w-1)*j<D, where kappa>=1.

First-jet extraction replaces Y^i by terms (u0+u1 Z)^(i-f) Y_local^f, f<=i. It preserves j and never increases i+kappa*j or total Y,R,Z degree. Thus the received-word-dependent translations preserve this support bound.

For one enclosing local block, a<=M, b<=S, a+b+z<=L, a+kappa*b<=H. Its dimension is

 B(M,L,S,H)=sum_{b=0}^{min(S,L,floor(H/kappa))}
   [(A_b+1)(L+1-b)-A_b(A_b+1)/2],
 A_b=min(M,L-b,H-kappa*b).

Vanishing to order h along a=b means divisibility by (a-b)^h. In the polynomial integral domain, individual a- and b-degrees, total degree, and positive weighted degree all add under multiplication. The factor has respective degrees h,h,h,kappa*h. Hence the kernel dimension is exactly B(M-h,L-h,S-h,H-kappa*h), with negative caps interpreted as zero. This is the exact rank of the enclosing block map; extraction can have smaller rank.

For the source count at fixed j, write d=D-(w-1)j, c=L+1-j and N=1+min(L-j,H-kappa*j,floor((d-1)/w)). The contribution is sum_{i=0}^{N-1}(d-w*i)(c-i), giving exactly the polynomial in wedge_probe.C. Terms with d<=0 contribute zero.

A factor with deg_(Y,R)=y and deg_R=r has weighted degree at least max(y,kappa*r). This lower bound cannot be increased using those two degrees alone: Y^y+R^r attains it when y>=r. An independent Z^t term can realize total degree t>=y without changing these degrees. In particular, the unsupported replacement y+(kappa-1)r is invalid. Stronger erosion requires additional joint Newton-support information about the actual factor.

The exact weighted X-slab count is C(D,...)-C(max(0,D-width),...). Therefore the routing probe's clipped per-monomial X lengths are correct. This audit verifies formulas and their stated enclosing-space interpretation only; it does not certify a compiled Lean adaptation or a full score ledger.
