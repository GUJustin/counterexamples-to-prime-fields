# Positive-dimensional critical components have constant value in the short-characteristic regime

**Later strengthening:** the final list theorem uses `p>max(3,2D)`; see `TWO_D_RADICAL_BUDGET.md`, its independent audit, and `general_cubic_list.tex`. The stronger characteristic assumptions in this earlier argument remain valid sufficient conditions.

This supplies the algebraic reduction needed before the separate three-label cubic-cover lemma. It does not assume every rational fibration is isotrivial.

Let k be algebraically closed of characteristic zero or characteristic p>max(3,6D), K=k(X), and

    F=u³+a2(X)u²+a1(X)u+a0(X),
    deg a2≤D, deg a1≤2D, deg a0≤3D.

Let H be nonzero. Assume at least one nonzero-label polynomial section of degree≤D exists, so N=deg H≤3D. If the ideal (F_u, H F_X−H′F) has a positive-dimensional component, then for some constant c0,

    F−c0 H=(u−R)²(u−S),   R,S in k[X], deg R,deg S≤D.       (1)

R=S is permitted.

## Critical value and its height

The polynomial F_u has nonzero constant leading u-coefficient 3, so a positive-dimensional common component cannot be vertical. Choose its root r over K, and let L=K(r). The extension has degree d≤2 and is separable. The common-component equation gives

    H F_X(X,r)−H′ F(X,r)=0,   F_u(X,r)=0.

Extend d/dX to L and set v=F(X,r)/H. Differentiation gives v′=0.

In characteristic zero the constants of L are k, hence v=c0. In positive characteristic the kernel of this nonzero derivation is L^p: L is a one-variable separable function field over the perfect constant field k. It remains to exclude a nonconstant p-th power by height.

The critical equation 3r²+2a2 r+a1=0 shows r is integral at every finite place above X. At an infinity place of ramification index e, its pole order is at most De: otherwise the r² term would have strictly smallest valuation. Therefore F(X,r) has pole order at most 3De above infinity and no finite poles.

At finite places v has poles only above zeros of H, whose total degree is at most dN. At infinity its pole order is at most (3D−N)e, with zero used if this is negative. Since N≤3D and the sum of infinity ramification indices is d (the constants are algebraically closed),

    h_L(v)≤dN+d(3D−N)=3dD≤6D<p.

A nonconstant p-th power in L has height at least p. Thus v must again be constant. This argument explicitly controls the Frobenius escape; merely having zero derivative would not suffice.

## Repeated root descends to a polynomial

The cubic F−c0H has repeated root r. In characteristic different from two and three, a cubic with a repeated root has that root in K: in the double-plus-simple case its gcd with its derivative is linear, and in the triple case the root is read from its u² coefficient. Thus r=R belongs to K. Monic integrality over k[X] gives R in k[X]. The coefficient degree caps, including deg(c0H)≤3D, imply deg R≤D by the leading-term valuation comparison. The remaining root S=−a2−2R is polynomial of degree≤D. This proves (1).

## Exact reduction of the remaining sections

For every other label set lambda=c−c0. Equation (1) becomes

    (P−R)²(P−S)=lambda H.

If R=S, any nonzero-label section makes H a constant times a polynomial cube; all sections belong to the affine family R+t h, and arbitrary-word lists at surplus eta*n have size≤floor(1/eta).

If h=R−S is nonzero, set Y=(P−R)/h and q=H/h³. Then

    Y²(Y+1)=lambda q(X).                         (2)

If q is constant, Y is constant and again the bank is an affine family R+t h. If q is nonconstant, the independently audited cubic-cover lemma rules out three distinct nonzero lambda values with rational Y solutions. Therefore there are at most six sections in nonzero lambda fibers and at most the two repeated-fiber sections R,S: at most eight total.

The cover lemma is separate: three degree-three covers of the q-line have shared branch points 0 and infinity and distinct third branch points +4/(27lambda_i). Their fiber product has full S3^3 monodromy and genus three. A rational function field cannot contain that function field. No negative sign is present in the third branch value.

This reduction closes the positive-dimensional critical-ideal case once that cover lemma is included. It concerns the weighted monic-cubic polynomial first integral F/H; it does not extend to general rational cubic denominators or nonintegrable equations.
