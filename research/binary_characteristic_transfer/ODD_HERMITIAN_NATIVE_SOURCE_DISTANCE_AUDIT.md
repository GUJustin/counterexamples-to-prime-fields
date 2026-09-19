# Native quartic-alphabet source distance for the Hermitian compiler

2026-09-19. **PASS**. Pure algebraic audit; no scan or manuscript edits.

Let p be odd, B=Fp²⊂E=Fp4, beta∈E\B, D=p²−p, K=D−p, Λ=X^(p²)−X, and use the shifted source f=(X^D−beta^D)/(X−beta), with g=1/(X−beta), on all B. Define

    r_p=min{e≥2:e²−e+1≥p}.

Then agreement(f,RS_K)≤D−r_p, while agreement(g)=K and ordinary common agreement(f,g)=K.

## Proof of the new upper bound

For an arbitrary q of degree<K, put P=(X−beta)(f−q)=X^D+C. Its remainder satisfies deg C≤K=D−p and P(beta)=0. Let V be the monic locator of ALL distinct native roots of P, of degree A, and write P=VF with F monic of degree e=D−A. If e≥p then e≥r_p and the desired bound already holds.

Suppose e<p. The coefficients of P in degrees D−1 down to D−p+1 vanish. Since V is monic over B, recursively comparing the first e of those coefficients forces every coefficient of F into B. This argument does not assume P itself has coefficients in B. Since V(beta)≠0, F(beta)=0. The minimal polynomial of beta over B has degree two, hence e≥2.

Let G=Λ/V. It is monic, splits into p+e distinct native roots, and none is a root of P. The exact identity PG=ΛF yields

    X^D(G−X^p F)=−XF−CG.

Its right side has degree≤D+e, giving G=X^p F+A0 with deg A0≤e. Both G and F have coefficients in B, so A0 does too. Furthermore gcd(F,G)=1 because every root of G is native but is not a root of P; repeated roots of P cause no exception. Thus gcd(F,A0)=1.

The rational map R=−A0/F consequently has degree exactly e. At each of the p+e roots x of G, F(x)≠0 and x^p=R(x). Applying coefficientwise p-Frobenius gives x=R^sigma(R(x)). Both evaluations are defined there. The composed rational map has degree e², which exceeds one, so it is not the identity. Its fixed-point equation has at most e²+1 solutions on the projective line, and in particular at most that many finite solutions. Therefore

    p+e≤e²+1,

which is precisely e≥r_p. This proves the uniform source bound.

## Consequences and exact scope

At the strict threshold T=D−2, the f-source gap is at least r_p−2 and the g-source gap is p−2. For p≥5, r_p≥3, so both sources are strictly far in the SAME E alphabet. For p=3 the bound supplies no strict f-gap at this threshold. Asymptotically r_p~√p, whereas the capacity margin T−K=p−2; the guaranteed smaller endpoint gap is therefore a vanishing fraction of that margin.

The full Hermitian bank supplies p²(p−1) distinct nonzero values lambda with a displayed degree<K witness matching f+lambda*g on exactly D−1 points. Converting to the literal affine endpoint line (1−z)f+zg uses lambda=z/(1−z), omitting only lambda=−1. Thus at least p²(p−1)−1 distinct interior parameters retain those matches; the endpoint z=1 is g and z=0 is f. This is a certified witness count, not a singleton-list or full nearest-distance classification. The earlier Fp8 coefficient-projection construction remains a separate option with both agreements exactly K; it is no longer needed merely to obtain two far endpoints.

All claims concerning Johnson/first-order placement remain as audited in ODD_HERMITIAN_FULL_FAMILY_INDEPENDENT_AUDIT.md. In particular this refinement does not move the tested threshold above first order.
