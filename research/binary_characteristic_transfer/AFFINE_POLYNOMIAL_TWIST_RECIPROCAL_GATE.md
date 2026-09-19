# Affine polynomial twists reduce to a reciprocal pencil

September 19, 2026. Exact reduction for prime-field evaluation domains.
No search, field scan, or manuscript edit.

Let D⊂Fp have size n<p, let Λ=∏_{x∈D}(X−x), and let E be a
finite extension of Fp. Consider monic native locators G_i|Λ of
degrees at most e<n, polynomials F_i∈E[X], and the identities

    G_i^p − A_i G_i = Λ F_i^p,
    P_i = (Λ/G_i)F_i,       deg P_i<n.                      (1)

The zero polynomial is allowed for F_i. Assume that all A_i lie
on one E-affine polynomial line and that

    p−n>2e.                                                 (2)

The fixed-twist result is in FIXED_POLYNOMIAL_TWIST_PRIME_DOMAIN_GATE.md.

## 1. Reversal turns the affine twist into an exact reciprocal pencil

Put e_i=deg G_i, Q_i=Λ/G_i, f_i=deg F_i. If F_i≠0, the residual
degree condition gives f_i≤e_i−1. Rearranging (1) gives

    A_i=G_i^(p−1)−Q_i F_i^p.                                (3)

The second term has degree at most

    n−e_i+p(e_i−1)=(p−1)e_i+n−p<(p−1)e_i.

Thus every A_i is monic of degree (p−1)e_i, including F_i=0.
If e_i=0, residual degree<n forces F_i=0, giving only G_i=A_i=1.

If at least three distinct A_i occur on the affine line, all have
the same degree. Indeed the coefficient at the highest degree
occurring in that line is an affine function of its parameter and
takes values only in {0,1} on these monic polynomials. A nonconstant
affine function cannot do this at three distinct parameters.
Write the common locator degree as e0≥1.

Reverse at infinity:

    g_i(Z)=Z^e0 G_i(1/Z),
    a_i(Z)=Z^((p−1)e0) A_i(1/Z).

All g_i have constant coefficient one. Equation (3) and
g_i(Z)^p=1+O(Z^p) give

    a_i(Z)=1/g_i(Z)+O(Z^(p−n)).                             (4)

Normalize any two distinct twist parameters to 0 and 1. For another
parameter t, affine dependence of the a_i yields

    1/g_t = (1−t)/g_0 + t/g_1 mod Z^(p−n).

After multiplication by g_t g_0 g_1, the numerator has degree at
most 2e0. By (2) it vanishes identically. Undoing reversal gives
the exact relation

    1/G_t = (1−t)/G_0 + t/G_1.                              (5)

If G_0=G_1, all locators are identical. Otherwise (5) makes the
locator injective in the twist parameter.

Repeated twist polynomials cannot hide extra residuals: since
e<p−n, the fixed-twist space has dimension at most one. Its
monic native locator is unique, and (1) then determines F and P.

## 2. A reciprocal pencil has at most e0+1 squarefree locators

Suppose G_0≠G_1 are monic squarefree polynomials of the same
degree e0. Write

    G_0=C U,  G_1=C V,  gcd(U,V)=1,
    deg U=deg V=d≥1,  deg C=e0−d.

For t≠0,1, equation (5) reads

    1/G_t = W_t/(C U V),
    W_t=(1−t)V+tU.

The polynomial W_t is monic of degree d and coprime to UV.
Thus a polynomial G_t exists only if W_t|C. For distinct interior
parameters, the W_t are pairwise coprime: a common root would,
by the two independent linear combinations, be a common root
of U and V. Hence there are at most floor((e0−d)/d) interior
parameters and at most

    2+floor((e0−d)/d) ≤ e0+1                                (6)

locators altogether.

The reciprocal bound is sharp: for a squarefree H of degree e0+1,
the polynomials G_a=H/(X−a), over its roots a, obey
1/G_a=(X−a)/H. This example proves sharpness only for the
reciprocal-pencil lemma. It does not construct F_i satisfying
(1) with the twists on one affine line.

It follows that (1)–(2) allow either a single common locator or
at most e+1 distinct residuals with distinct locators. Cases with
only two distinct twists are already within the latter bound.

## 3. The common-locator branch for an actual received line

A common locator alone does not bound the number of twist parameters:
F may vary. It can nevertheless be bounded when the residuals are the
actual displayed witnesses for a common-far received pencil.

Suppose, in addition to (1)–(2), that a fixed multiplier δ(x)≠0 on D
and a received pair f,g satisfy

    P_i(x)/δ(x)=f(x)+λ_i g(x)−h_i(x)   (x∈D),              (7)

with distinct λ_i, degree(h_i)<k, at least T zeros of each P_i
in D, and ordinary common agreement CA_k(f,g)<T.

**Conclusion.** There are at most e+1 such distinct challenges.

Only the common-locator case needs further proof. Write G_i=G
and Q=Λ/G. Affine dependence of the twists and (3) imply, after
an affine pth-root change of parameter, an exact polynomial pencil

    F_τ=F_0+τF_1,          P_τ=P_0+τP_1.

Let S be the common zero set of P_0 and P_1 in D. It contains Z(Q),
so |S|≥n−deg G≥n−e. Outside S, each coordinate is a zero for at
most one parameter τ.

To compare |S| with common agreement, take the quotient of E^D
by the linear space δ·RS_k(D). If the residual pencil has constant
image there, (7) cannot represent two distinct λ_i: otherwise
g would itself be a codeword, contradicting CA_k(f,g)<T and the
existence of a T-agreement witness. If the image is nonconstant,
(7) makes λ an invertible affine function of τ. The constant
and linear parts of (7), restricted to S, therefore give codeword
explanations for both f and g on S. Hence

    |S|≤CA_k(f,g)<T.

Counting roots outside S now gives, for M displayed parameters,

    M(T−|S|)≤n−|S|≤e,

so M≤e. Together with (6), and the at-most-two-twist case, this
proves the conclusion.

The argument applies to any fixed coordinatewise nonzero multiplier,
including a fixed exterior pole denominator. It does not assume
singleton lists or claim to bound all witnesses not displayed by (1).
It does not cover twists moving in a genuinely higher-dimensional
polynomial space, varying denominators, or residual degree at least n.

For the practical large-characteristic setting, p≥3n is a simple
sufficient condition for (2) for every e<n. Thus a one-dimensional
affine family of twists of this kind cannot yield a superlinear
displayed challenge bank above its common-agreement threshold.

