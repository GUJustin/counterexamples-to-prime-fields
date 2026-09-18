# Prime-alphabet variant: primary prime-existence and comparison audit

2026-09-18. **PASS.** No manuscript edits. The prime-existence input supports every sufficiently large power-of-two fiber size, not merely an unspecified infinite subsequence.

## Actual primary theorem and specialization

Thorner–Zaman, *Refinements to the prime number theorem for arithmetic progressions*, Corollary 3.1 and the immediately following discussion / equation (3.2), concern powerful moduli with fixed squarefree radical. Primary: https://arxiv.org/abs/2108.10878 ; published DOI https://doi.org/10.1007/s00209-023-03414-3 . Cached actual PDF/text: `tmp/cs_novelty_audit/tz.pdf`, `.txt`.

Take their modulus to be m=2^a; its radical is 2. The discussion after Corollary 3.1 states that for sufficiently large m relative to this fixed radical, the exceptional zero does not exist, so λ=1. Their estimate then applies when h/φ(m)≥x^(7/12+ε).

For fixed β>12/5 choose 0<ε<5/12−1/β and set x=2m^β, h=m^β. Then

    h/φ(m)=2m^(β−1) ≥ (2m^β)^(7/12+ε)

for sufficiently large m. The error term in (3.2) tends to zero: its exponent grows like a positive constant times (log m)^(1/4)/(log log m)^(3/4). Thus the sum of log p for primes p≡1 mod m in (m^β,2m^β] is asymptotic to 2m^(β−1), in particular positive.

Consequently **for every sufficiently large integer a** there is such a prime p. This gives infinitely many distinct primes and the desired p=Θ(m^β). No assumption such as GRH is used. KKH Appendix A invokes this input, while its headline results assert infinitely many instances. Its extra β>τ+1 restriction serves a separate label/resultant count; it is unnecessary when the new random-tag proof replaces that step.

## Parameter consistency

The image H=(F_p*)^m has size (p−1)/m. Since β>12/5>2,

    |H|/sqrt(p) = Θ(m^(β/2−1)) →∞.

Thus the proposed Jacobi-sum population estimate of size at most sqrt(p), independently audited by the other agent, is small relative to the population. There are nonzero b outside H because m>1. With s=Θ(log p) sampled tags plus one reserved tag, the union of s+1 fibers of X↦X^m has n=(s+1)m=Θ(m log p). Therefore

    p=Θ((n/log n)^β).

In particular this is a PRIME alphabet, with p≫n and hence p>J for fixed rate eventually. Earlier objections based on a required proper extension alphabet no longer apply to this variant. The domain is a union of cosets of μ_m, generally not itself a multiplicative subgroup. The exact source/root-count compiler is unaffected by that distinction.

## Prior comparison

CS Corollary 1 already proves every-affine-label coverage at inverse-logarithmic margin over prime alphabets and arbitrary domains when its entropy condition holds. Thus neither prime alphabet nor almost-all coverage nor logarithmic gap alone is a new regime. The distinction still requiring a novelty assessment is the simultaneous TWO-far exact source/common-agreement profile, with all nonzero combinations near; the prior-direction audit did not find this in the actual CS/DG proofs.

KKH has prime alphabets, subgroup domains and inverse-logarithmic gaps already, and Appendix A already contains the quotient-variable mechanism. This variant changes the domain to a union of cosets and uses Jacobi bounds plus random tags to saturate label coverage. It should be positioned as a structured two-far refinement using existing ingredients, with no priority claim. The exact common-agreement baseline exceeds the code dimension by m−1, so it does not retain the older deep-hole CA=J feature.
