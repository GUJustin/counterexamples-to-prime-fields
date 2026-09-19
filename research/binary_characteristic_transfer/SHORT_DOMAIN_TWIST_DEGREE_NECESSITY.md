# Necessary degree of a Frobenius twist on a short domain

2026-09-19. A scoped algebraic observation, not a counterexample or a
general obstruction to prime-field proximity gaps.

Let K have characteristic p, let Lambda be a monic polynomial of degree
0<n<p, and suppose nonzero polynomials F,G and a polynomial A satisfy

    G^p - A G = Lambda F^p.

Assume P=Lambda F/G is a polynomial of degree less than n. Write
e=deg G and f=deg F. Then deg P=n+f-e<n, so e>f>=0.

**Claim.** Necessarily

    deg A=(p-1)e,   lc(A)=lc(G)^(p-1).

In particular no twist of degree less than n can work in this model.

**Proof.** The right side has degree n+pf<pe, because n<p and e-f>=1.
The leading term G^p must therefore cancel against AG. This forces both
the asserted degree and leading coefficient. Since e>=1, the degree of
A is at least p-1>=n. This also rules out A=0. No assumption about the
roots of Lambda, the coefficient field being prime, or deg G<n is needed.

## Why a varying twist alone is insufficient

This degree constraint is not a prohibition against high-degree twists.
If G divides Lambda, then for any F with deg F<deg G the polynomial

    A=G^(p-1)-(Lambda/G) F^p

satisfies the identity, and P=(Lambda/G)F has degree below n. In fact its
first term has strictly larger degree than the second, as the proof above
requires. Thus allowing an arbitrary witness-dependent A makes the
identity tautological for split locators. Any useful construction must
add a shared condition that yields a common received line and its claimed
agreement counts; the identity by itself provides neither.

This complements, but does not replace, a bound for a single fixed A
across an entire family. It does not address rational residuals, degree
reduction modulo Lambda, or alternative compiler identities.
