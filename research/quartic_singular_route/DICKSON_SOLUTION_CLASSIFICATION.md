# Exact polynomial-solution classification for the Dickson cubic ODE

2026-09-17. Independent algebraic check of DICKSON_CUBIC_ORDINARY_CORE.md. This is an actual-solution classification, not a new RS agreement bound.

## Theorem

Let p=4k+1 be prime, k>=1, and let K be ANY extension field of F_p. Put e=2k+1 and

    G_t(X)=sum_{j=0}^k binom(e,2j+1)t^(k-j)X^j.

The monic degree-k polynomial solutions over K of

    4X(2G^2-1-X^(2k))G' + G(4G^2-1-3X^(2k))=0          (1)

are exactly G_t for

    t=0 or t^(2k)=1.

All these t lie in F_p; they are zero and the nonzero squares. Thus there are exactly 2k+1 solutions, even over an algebraic closure. Equivalently the shifted equation in the existing note has exactly 2k+1 polynomial solutions P=G-X^k of degree at most k-1, and all are defined over F_p.

More generally, all solutions G of degree at most k are

    G=0, and G=+G_t or -G_t for those same parameters.

There are exactly 4k+3=p+2 such solutions.

## 1. The triangular high-degree recurrence

Write a monic degree-k polynomial as

    G=X^k+sum_{r=1}^k c_r X^(k-r).

The left side of (1) is

    8X G^2 G' -4X G' -4X^(2k+1)G' +4G^3-G-3X^(2k)G.

Its leading coefficient is 4k+1=0 in F_p. For 1<=r<=k, the coefficient of X^(3k-r) has the form

    4(1-r)c_r + F_r(c_1,...,c_(r-1)).                   (2)

Indeed the coefficient linear in a perturbation c_r X^(k-r) around X^k is

    8(3k-r)-4(k-r)+12-3 = 20k-4r+9 = 4(1-r) mod p.

The lower-degree terms -4XG'-G have degree at most k, while 3k-r>=2k>k, so they do not contribute. In every nonlinear term involving c_r and some other positive-deficit coefficient, the total deficit exceeds r; c_r occurring twice also has deficit at least 2r>r. Therefore no hidden nonlinear dependence on c_r remains in (2).

At r=1, F_1=0 and the multiplier is zero, so c_1 is free. For 2<=r<=k the multiplier is nonzero because 1<=r-1<p. Thus c_1 determines all remaining coefficients uniquely. For k=1 there are no further recurrence equations, which is consistent with the same argument.

## 2. Identifying the universal recurrence solution

The coefficient of X^(k-1) in G_t is

    binom(e,2)t = -t/8 in F_p.

Thus every desired c_1 corresponds to the unique t=-8c_1 in K.

For each r<=k, the coefficient of X^(3k-r) in the residual of G_t has degree at most r in t: every contribution has total coefficient deficit r, and the coefficient of deficit j in G_t is a constant times t^j. This residual coefficient vanishes for every t which is zero or a nonzero square in F_p. There are 2k+1 distinct such values, because for t=a^2 the polynomial G_t is exactly the previously verified binomial G_a satisfying (1).

Since r<=k<2k+1, the residual coefficient is identically zero as a polynomial in t. Hence G_t satisfies all the triangular high-degree equations for every t in K, whether or not it satisfies the full ODE. The uniqueness from (2) now forces every monic degree-k solution to equal G_t for its parameter t. This step only uses polynomial identities verified at enough base-field parameters; it does not assume the Frobenius derivation works for arbitrary extension-field a.

## 3. The constant term eliminates every extra parameter

At X=0, equation (1) reads

    G(0)(4G(0)^2-1)=0.

For G_t, its constant term is e t^k=(1/2)t^k. Therefore any solution must satisfy

    (1/2)t^k(t^(2k)-1)=0.

The polynomial T^(2k)-1 has 2k distinct roots, all already in F_p, since 2k divides p-1. They are precisely the nonzero squares. No extension field contributes additional parameters. Conversely all these parameters, including t=0, give the known solutions. Their c_1 coefficients distinguish them, proving the exact count.

## 4. Lower degrees and nonmonic solutions

If a nonzero solution has degree j<k and leading coefficient a, the unique highest-degree contribution has coefficient

    -(4j+3)a at X^(2k+j).

Here 0<4j+3<p, so it cannot vanish. Hence no nonzero lower-degree solution exists.

If G has degree k and leading coefficient a!=0, the leading ODE coefficient is

    (8k+4)a^3-(4k+3)a=2a(a^2-1).

Thus a=+1 or -1. The equation is odd under G->-G, so the monic classification applies after changing sign. This proves the full degree-at-most-k statement.

## Scope

The exact count is over every extension field in the SAME characteristic p=4k+1. It is not a lift to larger characteristics. For the received word and agreement claims, retain the separate hypotheses in DICKSON_CUBIC_ORDINARY_CORE.md, including p=1 mod8 for the cited 3k/2 agreement count. Those estimates are not proved by this ODE classification.

The equation supplies a genuine growing solution bank inside the full ordinary core. Its exact solution set is finite and entirely prime-field defined. This reinforces that eliminating the ordinary core must deal with actual solutions, while giving no superlinear scalar-label construction by itself.
