# Independent audit of the centered subgroup-twist estimate

2026-09-18. Verdict: **PASS**, as a derivation from Katz's proof, not as a quotation of his displayed theorem. Read `PRACTICAL_SUBGROUP_TWIST_AUDIT.md` and the actual cached primary `/tmp/katz1989.pdf`, especially pp.198–199.

Let E/F_p have degree six, b generate E, χ≠1 a character of E*, ψ a character of F_p*, and ρ=χ|F_p*. Set S=Σ_(a≠0)χ(b−a)ψ(a), δ0=1_(ψ=1), δ∞=1_(ρψ=1). Then

    |S+δ0χ(b)+δ∞χ(−1)|≤(6−δ0−δ∞)√p.

## Independent geometric derivation

Apply Katz's Lang-character construction to E×F_p, regular element (b,0), and χ×ψ, with the harmless constant adjustment making its trace χ(b−a)ψ(a). Over the algebraic closure the six finite b-conjugate punctures are distinct and nonzero. Their local characters are Frobenius conjugates of χ and are each nontrivial: the relevant exponent multipliers are powers of p, which are units modulo the character order. In particular the pulled-back rank-one sheaf is geometrically nontrivial.

At zero the inertia character is ψ. At infinity it is the inverse of the product of the finite inertia characters. The product of the six E-factor characters is precisely χ restricted to scalar F_p*: for character exponent k modulo p^6−1, the geometric exponent sum multiplies by 1+p+...+p^5, yielding k modulo p−1. Thus the infinity triviality test is ρψ=1, not a norm-triviality condition imposed on all χ.

The endpoint trace at zero, when removable, is χ(b). For infinity use u=1/a and

    (b−a,a)= (−1,1) · (u^(−1),u^(−1)) · (1−bu,1).

When ρψ=1, the scalar-factor character sheaf is trivial and the last factor specializes to the identity; hence the removable trace is χ(−1). This verifies both phases, not only their absolute values.

For the bound, extend across these removable endpoints and let U be P1 minus the actual nontrivial-monodromy punctures. Their number is 8−δ0−δ∞. The tame rank-one Euler characteristic is 2−(8−δ0−δ∞). Compactly supported H0 vanishes because U is nonproper; H2 vanishes by geometric nontriviality. Therefore Hc1 has dimension 6−δ0−δ∞. Its Frobenius weights are at most one, exactly the bound used in Katz's proof. The trace formula gives the displayed inequality. A stronger purity assertion via projective covers is unnecessary for this proof, so no extra purity citation is needed.

## Averaging and scope

For H of size I=8128 annihilating D=μ262144, exactly one ψ is trivial. A removable infinity occurs among the twists iff χ|D=1, and then for exactly one ψ. It can coincide with the trivial twist, but still saves just two dimensions in that one summand. Hence

    |S_D+[χ(b)+εχ(−1)]/I|≤[6−(1+ε)/I]√p.

The uncentered triangle bound is 6√p−(1+ε)(√p−1)/I. At p=2130706433 even ε=1 gives approximately 276946.10>262144, so the argument supplies no nontrivial bias bound on D. It does not justify a uniform 5√p bound, nor exclude stronger cancellation across twists.

The independent one-pole degree cap in the audited note is also correct: for strict dimension k=131072 its residual numerator is a nonzero polynomial of degree k+1, giving at most 131073 matches. Thus product coverage by itself would not reach 139782 agreements. The degree and character-sum gates are logically separate.

Primary: Katz, *An Estimate for Character Sums*, JAMS 2 (1989), 197–200, https://web.math.princeton.edu/~nmk/old/estcharsums.pdf . This receipt certifies the stated restricted estimate, not a new construction or a general impossibility theorem.
