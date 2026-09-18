# Universal one-pole cover genus bound

Characteristic zero throughout. This is a proof, not a numerical search. It supersedes separate pole-partition arguments for cubic covers.

## Excess-one birationality, including composite covers

Let psi:P1_U -> P1_X have degree e. Suppose a nonconstant rational v satisfies

    pole(v) <= m psi^*(infinity) + [b],

and its pole excess at b is exactly one: ord_b(pole v)-m ord_b(pole psi)=1. At every other point the excess is nonpositive. Then k(psi,v)=k(U).

Indeed let phi:P1 -> C be the map to the normalization of the image of (psi,v), of degree t. Both functions descend to C, so their pole excess at any point is its ramification index times the excess downstairs. The positive excess at b forces positive excess at every point in phi^-1(phi(b)). Hence this fiber consists only of b. Its ramification index is t, so 1=t times an integer and t=1. No primality assumption on e is used.

A proper one-pole witness N/(ell S^3), psi=R/S, has this property with m=3. After subtracting the base interpolant at f fully matched fibers and dividing by their degree-f locator, it has the property with m=3-f. The extra pole lies outside those fibers; at infinity the interpolant has pole order at most f-1, and division by the locator removes exactly f times the psi-pole order. Thus the positive excess remains exactly one.

## Norm equation and compactification

The primitive minimal relation is

    H(X,V)=sum_{j=0}^e A_j(X) V^(e-j),  A_0 != 0,
    deg A_j <= mj+1.

At any finite place except psi(b) the conjugates are integral. At psi(b) their extra total negative valuation is at most one, so all elementary symmetric coefficients have poles of order at most one. At infinity the jth coefficient has pole order at most mj, plus at most one if b is above infinity. Clearing the possible finite linear denominator proves the degree flags. Birationality proves that the minimal degree is exactly e.

Compactify the total space of O(m) to the Hirzebruch surface F_m. Let C0 be the negative section, F a fiber. Then

    C0^2=-m, C0.F=1, F^2=0, K=-2C0-(m+2)F.

The irreducible closure of H=0 has divisor class

    D=e C0+(me+c)F,
    c=max_j(deg A_j-mj) in {0,1}.

This is the coefficient transition rule for the fiber coordinate of O(m). Use the actual maximum c, rather than artificially homogenizing all coefficients to the larger cap; this removes any extra infinity-fiber component. Primitivity excludes finite vertical components. A_0 nonzero and deg A_0>=0 ensure c>=0. The degree flags ensure c<=1.

Adjunction gives

    p_a(D)=1+(D^2+D.K)/2
          =(e-1)(me/2+c-1) <= m e(e-1)/2.

The normalization is P1 by the excess-one lemma. Therefore the sum of delta invariants at ANY subset of affine image points is at most m e(e-1)/2. Boundary singularities can only consume the budget. Neither Newton nondegeneracy nor squarefree S is required. If k distinct preimages in a selected separable fiber have the same v-value, their k normalization branches contribute at least binom(k,2) to delta. In fact they are smooth because X is unramified on each branch, but the weaker distinct-branch estimate suffices.

## Consequence for every degree e>=4

Take any seven-cubic bank on fourteen nodes with seven matches per candidate. Saturation makes seven base columns triples and seven quadruples. A proper one-pole witness on an e-cover with at least 7e matches differs from each old cleared section by a nonzero binary form of degree 3e+1.

Select exactly 7e matches. Let T,Q be their totals above the seven triple and seven quadruple nodes. Then

    T+Q=7e, 3T+4Q<=7(3e+1), hence T>=7(e-1).

On the seven triple fibers convexity forces delta cost at least 7 binom(e-1,2). The m=3 genus bound gives at most 3e(e-1)/2. Thus

    7(e-1)(e-2) <= 3e(e-1),

which fails for every e>=4. This conclusion needs no geometric classification of the bank beyond the saturated incidence counts.

For e=3 the same lemma gives d+3f<=9. If f=2, removing the full fibers gives m=1 and d<=3. Consequently the already certified cubic support reduction and norm matrices apply without any pole-partition caveat. For e=2 the existing quadratic matrices apply unchanged. Combined with the complete orbit2/orbit7 realization classification and those exact matrices, all proper one-pole rational-cover augmentations of seven-cubic banks are excluded for every degree e>=2.

## Scope

The selected fourteen fibers have e distinct preimages; the extra pole is outside them and is proper. The statement is characteristic zero and concerns this augmentation operation. It neither excludes arbitrary eight-word banks nor bounds all list sizes. Higher pole order would replace excess one by a larger divisor and can permit an intermediate factorization; that is a different construction problem.
