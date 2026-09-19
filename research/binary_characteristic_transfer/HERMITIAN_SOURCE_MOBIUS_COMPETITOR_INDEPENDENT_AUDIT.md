# Independent audit of the Möbius source competitor

2026-09-19. **PASS** for the actual proof note hashed below. No manuscript edits, PGL census, or polynomial scan.

## Constructor and exact agreement

For even e and a trace-zero exterior t, t^e lies in B and a=t^(−ep) lies in B, with a^p t^e=1. If both choices t=w and w*zeta gave a in mu_m, then L=(p²−1)/m would divide ep, hence e, contradicting L>e. Thus the claimed two-choice rule is valid. The conjugation formulas for gamma and b are native and gamma≠0, since t and beta are exterior. They produce a B-Möbius transformation mapping t to the prescribed beta and with its pole outside mu_m.

The inverse-coordinate locator G=(U^(p+e)−q^(p+e))/(a^(p+e)−1) is monic, squarefree, fully native-split and has degree p+e. The displayed Frobenius expansion gives monic F of degree e and A of degree≤e. The two coefficient rows have determinant gamma^p, so gcd(F,A)=1. This proves gcd(F,G)=1 without assuming all roots of F are native. Evaluating at beta gives F(beta)=0.

For P=FΛ/G, all native roots of F already lie in the complementary root set because F and G are coprime. Therefore the number of distinct native roots of P is EXACTLY D−e. The polynomial identity (P−Y^D)G=−YF−Y^D A proves the head gap deg(P−Y^D)≤D−p. Its value P(beta)=0 makes the displayed divided difference a polynomial of degree<k. Thus it is an actual competing codeword for the zero endpoint, for every exterior beta, rather than only a candidate split locator.

## Saturation and unconditional asymptotic limitation

If even e≥4 has p=e²−e−1 prime, then p+e=e²−1 divides p²−1 and L=e(e−2)>e. The preceding integer below e fails the inequality j²−j+1≥p while e satisfies it, so r_p=e. Combining the constructor with the proved source upper bound gives exact source agreement D−r_p. The note correctly treats these as conditional prime-quadratic parameters and finite examples, not an infinite-primes theorem.

For the unconditional family, fixed odd r≥3 and positive odd j give even e=1+rj and p=(r−1)e+r. The arithmetic progression has modulus 2r(r−1) and residue r²+r−1, coprime to that modulus. Dirichlet therefore gives infinitely many primes for each fixed r. The identities p−1=(r−1)(e+1), r|(p+1), and m=r(e+1) prove divisibility and the stated L>e. Also e<p. Consequently the zero-endpoint loss divided by p−2 is at most (e−2)/(p−2), tending to 1/(r−1). Varying r along a diagonal disproves a uniform positive fractional zero-source gap across all primes. No unproved uniform prime bound is used: one may choose arbitrarily large primes separately from each progression.

This is also a genuine obstruction to the contemplated uniform e=Omega(p) claim for these split cofactor polynomials. It does not imply that every prime admits e=o(p), that the universal sqrt(p) bound is always attained, or that a different pair of endpoints cannot have stronger distances.

The final paragraph's separate c* condition also checks: P(beta)=c* implies G(beta)^p=Λ(beta)F(beta)^p, hence A(beta)^p=−beta F(beta)^p and (−A/F)(beta)=beta^(p³). The present construction imposes F(beta)=0 instead, so it does not solve that different endpoint constraint.

This audit checks the proof, not the forthcoming p=11 implementation receipt.

Source SHA256: `d1321d73364a95d955a9b7068dee0f0fad9ac58fbeb7f315144f98c2bfa07159`.
