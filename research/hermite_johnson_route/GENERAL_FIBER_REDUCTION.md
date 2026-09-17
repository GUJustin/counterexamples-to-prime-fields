# Received-fiber normalization: valid local extraction and its obstruction

2026-09-17. This note distinguishes a local derivative constraint from a new global differential identity. It does not justify applying the Hermite theorem to a raw interpolation kernel whose ordinary core is the whole domain.

## 1. The received-fiber ideal

Let A(X)=prod_{x in Dcal}(X-x), with distinct domain coordinates, and let W(X,z) be the degree-below-n polynomial interpolating f_x+zg_x; it is affine in z. The condition

    Q(x,z,W(x,z),v)=0 for every coordinate x

as a polynomial identity in z,v is equivalent to

    Q in I=(A(X),u-W(X,z)).

Indeed divide Q by u-W, then use the pairwise coprime factors X-x of A on the remainder. Explicitly one can write

    Q=A R(X,z,v)+(u-W)S(X,z,u,v).

For an actual solution Q(X,z,P,P')=0, differentiation along its graph gives

    0=A'R+(P'-W_X)S+A D_X R+(P-W)D_X S,

where D_X includes the chain-rule terms involving P'' as appropriate. At a value agreement x, A(x)=0 and P(x)-W(x,z)=0. Therefore every such agreement satisfies

    J_x(z,P'(x))=0,
    J_x(z,v)=A'(x)R(x,z,v)+(v-W_X(x,z))S(x,z,W(x,z),v).       (1)

All P'' terms disappear from this LOCAL equation. No assertion that J(X,z,P,P') vanishes identically is warranted.

## 2. Higher ideal order: exact first normal symbol

More generally suppose Q is in I^m. Expand uniquely in u-W:

    Q=sum_j q_j(X,z,v)(u-W)^j.

Membership is equivalent to A^(m-j) dividing q_j for j<=m. Write c_j=q_j/A^(m-j) for such j. At an agreement coordinate x, both A(x+t) and P(x+t)-W(x+t,z) vanish to first order, with respective linear terms A'(x)t and (P'(x)-W_X(x,z))t. The coefficient of t^m in the actual identity is consequently

    J_m,x(z,v)=sum_{0<=j<=m} A'(x)^(m-j)
                    (v-W_X(x,z))^j c_j(x,z,v)=0.             (2)

Terms with j>m have higher t-order. No second or higher derivative of P occurs in (2).

If Q has total (u,v)-degree at most B0 and challenge degree at most H0, then q_j and c_j have v-degree at most B0-j and z-degree at most H0+B0-j. Thus

    deg_v J_m,x <= B0,
    deg_z J_m,x <= H0+B0.

The challenge bound uses that W_X is affine in z. This is better than blindly adding m to the total jet-degree bound, but it need not retain the original derivative-only degree bound of three. The X-degrees and m may be large without affecting these two degree estimates.

## 3. Conditional improvement of the ordinary core

Equations (1)--(2) can help even though they are NOT global identities. If at a coordinate J_m,x is a nonzero polynomial with exactly one distinct root over the algebraic closure of F(z), then it prescribes a rational first derivative, provided the characteristic exceeds its degree. Writing J=a_e(v-r)^e gives

    r=-a_(e-1)/(e a_e).

Numerator and denominator degrees are at most H0+B0. Excluding the at most H0+B0 roots of a_e makes this prescription valid at every remaining actual agreement. A nonzero constant J permits agreement only at its bounded set of coefficient roots.

Such coordinates can be moved from the ordinary core into a rational-Hermite core directly. Hermite interpolation only uses the resulting value/derivative matches; it does not need J to be a global equation for P. The original global Q still supplies the regular-incidence portion of the argument. Any remaining coordinates with identically zero J or multiple possible derivative roots remain unhandled unless a further independent local constraint selects a unique root.

Caution: a cubic J with discriminant zero may have a double root AND a distinct simple root. The equation J=0 alone does not select the double root. The earlier cubic theorem used the additional separant equation; it cannot be imported here without an analogous selection argument. Linear J, powers of one linear factor, or a collection of constraints with single-root gcd are the clean valid cases.

## 4. Global-identity extraction is false without more information

Take a squarefree domain locator A and W=0. The primitive contact equation

    Q=A(X)v-A'(X)u

belongs to I, has derivative degree one and total jet degree one, and vanishes on every received fiber. Its first normal symbol at every coordinate is identically zero:

    A'(x)v-A'(x)v=0.

It has no common factor depending only on X, since gcd(A,A')=1, and u does not divide it. Thus neither X-content removal nor division by the received-fiber factor removes this example. For general W the same cancellation occurs in

    Q=A(v-W_X)-A'(u-W).

At an agreement, the next Taylor coefficient includes

    (A'(x) P''(x)-A''(x)P'(x))/2

when W=0 and characteristic is not two. Thus the next nontrivial equation need not be first order. In arbitrary characteristic the corresponding Hasse expression makes the same higher-jet dependence explicit. This is an obstruction to automatic normalization, not an example of many low-degree bad candidates: its global solutions themselves may be very restricted by degree.

A separate example shows why one may not drop the ideal multiples after differentiating even when the first local constraint is useful. Let P=X^2, take a nonconstant polynomial L with simple roots, and put

    W=X^2+2XL,
    Q=L v+u-W.

Then P is an actual solution, and it agrees with W at every root of L (and possibly X=0). But the putative first-order global derivative equation is

    Q_X+v Q_u=L'v+v-W_X,

which evaluates on P to -2L, not zero. At the agreement roots it vanishes, exactly as the local argument says. The missing global term is L P''. For a full-domain fiber example with canonical degree-below-n received interpolant, choose a squarefree A=L M with disjoint factors and deg M>=4, and multiply this Q by M. Then deg W<deg A, the multiplied equation belongs to (A,u-W), and the first normal expression from (1), evaluated on P, is 2L(X M'-M), generally nonzero. It still vanishes at every selected agreement root of L. The multiplied example has removable X-content; the preceding contact example separately shows that primitiveness does not guarantee a nonzero first normal symbol.

## 5. Relation to the actual kernel source

The source trace by better_codes_frontier supplies a stronger and different weighted normal form, using a Hermite interpolant W with W_X(x)=0 and an auxiliary E with E(x)=0,E'(x)=1:

    V=Y-W-E R,
    Q=sum_b Lambda^max(m_kernel-2b,0) H_b V^b.

This implies I^ceil(m_kernel/2) membership, not necessarily I^m_kernel. The first ordinary normal symbol can cancel because V has normal direction a-R. The traced primitive multiplicity-two example already exhibits this cancellation, and its next prolongation contains P''. Therefore raw-kernel membership does not automatically produce the single rational first jet required by the new theorem.

The useful next test is precise: compute the first normal symbols of the ACTUAL extracted equation, factor their derivative polynomials over F(z), and count coordinates where their common root set is uniquely rational. This may reduce the ordinary core without any global division. If they vanish identically or retain multiple derivative branches, the present theorem remains conditional and no reduction has been established.
