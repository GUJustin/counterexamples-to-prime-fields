# Complete high-rate Hermitian threshold-list classification

2026-09-19. Independent audit: **PASS**. This strengthens the earlier witness-count and source-distance results. No finite scan or manuscript edits.

Fix p≥5, B=Fp²⊂E=Fp4, beta∈E\B, D=p²−p, k=D−p, T=D−2, Λ=X^(p²)−X, and

    f=(X^D−beta^D)/(X−beta), g=1/(X−beta).

Let H be the family of monic polynomials

    G=X^(p+1)+sX^p+s^pX+c,
    s∈B, c∈Fp, c−Norm(s)≠0.

For each G put P_G=(X+s)Λ/G and λ_G=P_G(beta). The earlier injectivity proof gives M=p²(p−1) distinct NONZERO bank labels, denoted B_bank.

## Classification of every threshold witness

For ANY received parameter λ and polynomial q of degree<k, its residual is

    P=(X−beta)(f+λg−q)=X^D+C, deg C≤D−p, P(beta)=λ.

Let V be the monic locator of all its A distinct native roots and write P=VF, e=deg F=D−A. For A≥T one has e∈{0,1,2}. The leading e coefficient comparisons, valid because e<p, force F∈B[X]. Put G=Λ/V, a monic squarefree polynomial of degree p+e whose roots are precisely the native points not in V. As before,

    G=X^p F+A0, deg A0≤e, gcd(F,A0)=1.

The coprimality holds even if P has repeated native roots: G's roots are exactly the native NONroots of P.

If e=0, this gives G=X^p+a, contradicting its squarefreeness. If e=2, the degree-two rational map −A0/F gives p+2 distinct fixed points of its degree-four conjugate composition, whereas at most five are possible. This contradicts p≥5. These arguments do not use P(beta)=0.

Thus e=1. Write F=X+s and G=X^(p+1)+sX^p+aX+c with s,a,c∈B. Reduction modulo Λ gives

    G^p−G ≡ (a^p−s)X^p+(s^p−a)X+(c^p−c).

The right side has degree≤p and vanishes at all p+1 distinct roots of G, since these roots are native. Therefore it is zero, giving a=s^p and c∈Fp. Its radius c−Norm(s) is nonzero, because zero radius would make G=(X+s)^(p+1), contradicting squarefreeness. Hence G belongs to H and P=P_G.

Conversely every G∈H gives a degree<k witness and exactly D−1 matches. Since the map G↦P_G(beta) is injective, each bank label has exactly ONE threshold witness, and all other labels have empty threshold lists. No additional noncanonical polynomial can enter at threshold T. This is a classification of lists at T=D−2, not of all lower-agreement witnesses.

## Uniform stronger bound on every nonbank word

Let r_p=min{e≥2:e²−e+1≥p}. For a nonbank parameter, the cases e=0 and e=1 are excluded by the preceding arguments. Whenever 2≤e<p, the degree-e rational-map argument gives p+e≤e²+1, hence e≥r_p. If e≥p, the same lower bound is automatic. Thus EVERY nonbank word has agreement≤D−r_p<T. The earlier source argument's special use of beta's degree was only to rule out e=1 at λ=0; it is unnecessary after this complete classification.

## Two far affine endpoints without a chart loss

The bank is nonzero, so 0 is outside it. Choose c∈E*\B_bank, which exists because p⁴−1>M. Set r0=f and r1=f+c g. Their affine line is f+ctg, a bijective parameterization of all λ∈E. Both endpoints are outside the bank, so each has agreement≤D−r_p. Their ordinary common agreement is exactly k: the transformation from (f,g) is invertible with determinant c, and the reciprocal source has agreement k while simultaneous interpolation attains k.

Consequently this quartic-alphabet affine line has EXACTLY M singleton threshold lists and all remaining lists empty; both endpoints are individually far. Each exceptional word has exact nearest agreement D−1. No explicit formula for c is required by this existence statement, and no particular simple field-basis element is asserted to work.

The coefficient-descent proof also works if λ and q are taken over a larger coefficient field, so the former degree-eight projection construction keeps its exact source agreement k and now has the same complete singleton profile. The quartic endpoints have only the proved upper agreement bound D−r_p, not necessarily exact agreement k.

Threshold placement remains below finite Johnson AND below first order. This upgrade does not change that scope, the full-subfield domain, or the condition k>p.
