# Fifth-root route to a competitor at the second endpoint

Root derivation, 2026-09-19. Subsequently proved in the simplified form recorded in HERMITIAN_CSTAR_FIFTH_ROOT_COMPETITOR_AUDIT.md. The text below preserves the initial derivation; the audited note supplies the final theorem.

The exclusion for p=e^2-e-1 does not extend to all subgroup parameters.
For example p=13,e=8 gives gcd(p^3+e,p^4-1)=105, whereas its gcd with p^2-1 is 21. Thus exterior fifth roots satisfy the second-endpoint condition.

For a growing family, take odd r congruent to 3 modulo 5. In the existing Dirichlet construction impose e=1+rj even and congruent to 2 modulo 5, with j positive odd. Set p=(r-1)e+r. Then p is congruent to 2 modulo 5, and a primitive fifth root t belongs to F_(p^4) but not B=F_(p^2). It satisfies t^(p^3+e)=1.

The extra congruence chooses one class of j modulo 10. The corresponding prime progression has modulus 10r(r-1). The residue is coprime to r and r-1 as before, odd, and 2 modulo 5, so Dirichlet applies. Also m=p+e divides p^2-1 by the existing calculation.

For any prescribed exterior beta and any native a outside mu_m, write u=1/(t-a). The unique native affine map b+gamma*u sending u to beta has gamma nonzero, since both are exterior. Thus M(X)=b+gamma/(X-a) is a B-Mobius transformation with M(t)=beta and no pole on mu_m. Its split transformed locator is finite of degree p+e; the usual conjugated rational map is M^sigma composed with X^(-e) composed with M^(-1).

The second-endpoint condition reduces exactly to t^(p^3+e)=1. If the established transformed-locator identities apply with no additional restriction, this gives a D-e competitor at c_star for every beta. For fixed r, e/p tends to 1/(r-1); taking r to infinity diagonally would rule out a uniform positive fraction of the capacity margin even at the second explicit endpoint.

The independent audit resolved the cofactor normalization, exact distinct native root count, and second-endpoint label identity using the simpler pole choice a=0. This does not address choosing two entirely different line endpoints or different prime subsequences.
