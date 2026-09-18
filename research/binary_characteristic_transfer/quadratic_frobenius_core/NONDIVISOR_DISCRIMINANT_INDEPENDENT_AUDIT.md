# Independent audit: refined nondivisor discriminant gate, Sections 4–5

Verdict: PASS. Read the complete `NONDIVISOR_DISCRIMINANT_GATE.md` to verify the actual-overlap inputs used in Sections 4–5. No construction search, coefficient scan, or duplicate arithmetic checker was run.

## Leading and constant losses

For nonidentity t, the difference polynomial is nonzero because the three nonzero coefficient exponents are consecutive. A vanished leading coefficient gives a genuine linear difference with nonzero linear coefficient. A vanished constant coefficient leaves at most one nonzero root. Both vanish only as a nonzero multiple of X, with zero roots in the nonzero domain. Therefore the two losses add, including their overlap. Each such formal discriminant is a nonzero square.

Let Dplus denote nonzero-square discriminants and let E_tan be total actual overlaps at zero discriminants. The logarithmic-derivative argument gives E_tan<=A: its rational map is nonconstant of degree at most two in odd characteristic, so each matching x has at most one distinct partner in that fiber. This counts actual overlaps, not the potentially large number of vanishing-discriminant parameters. Consequently

 A(A−1)<=2Dplus−L0−C0+E_tan,

which proves 2Dplus>=A(A−2)+L0+C0. Independently, summing the root capacities of every nonzero difference gives A(A−1)<=2(n−1)−L0−C0. Both displayed refined inequalities are valid.

## Exact zero-fiber removal

Under gcd(e−1,n)=1, the denominator t^(e−1)−1 is nonzero on D\{1}. Direct expansion verifies

 (t^(e−1)−1)²−t^(e−2)(t−1)²
 =(t^(e−2)−1)(t^e−1).

Thus the stated two forms of v_t agree and its zero fiber has size L0+C0−B0 by exact inclusion-exclusion. Since gcd(e,e−2,n) divides two, B0 is indeed zero or one.

Writing beta=b²/(ac), one has beta!=0 and chi(ac)=chi(beta). The precise discriminant factorization is

 Delta(t)=ac*(t^(e−1)−1)²*(beta−v_t).

Every zero-fiber term contributes +1 after the chi(beta) prefactor, because beta is nonzero. Therefore sum chi(Delta)=M0+J(beta). Subtraction from the refined inequality gives exactly K=A(A−2)−m+B0; the sign of B0 and the cancellation of L0+C0 are correct. No zero-fiber multiplicity remains in the energy.

Keeping the number Z of zero discriminants in sum chi(Delta)=2Dplus+Z−m gives the stronger J(beta)>=K+M_beta. Here beta!=0 ensures Z=M_beta belongs to the retained nonzero fibers. Beta=4 is excluded by the prior square-family reduction; including it in an upper-bound count is safe.

## Moments and one-sided estimate

For nonzero fiber values v,w, the full-field correlation sum is p−1 if v=w and −1 otherwise. Hence sum H_*²=pE_*−m'². Likewise sum chi(beta)chi(beta−v)=−1 for every retained v!=0, giving sum J=−m'. Finally J(0)=0 while J(beta)²=H_*(beta)² at beta!=0, so

 S2=pE_*−m'²−C_*².

The removal of C_*² is necessary and correct. These identities include arbitrary multiplicities and require neither generic fibers nor a bound on E_*.

For K>0 and c>=0, a qualifying beta contributes at least (K+c)² to sum(J+c)². This gives the bound (S2−2m'c+pc²)/(K+c)². Differentiation gives the nonnegative minimizer

 c=(S2+Km')/(pK+m'),

and substitution yields exactly (pS2−m'²)/(S2+pK²+2Km'). The variance-zero case gives no positive-threshold parameter. The numerator is nonnegative by Cauchy; no assumption of symmetric tails is used.

There is a harmless stronger version if desired: beta=0 is excluded and J(0)=0, so perform the same calculation on F_p* instead. With S2 unchanged, replace sample size p by p−1:

 count <= ((p−1)S2−m'²)/(S2+(p−1)K²+2Km').

It is at least as strong as the displayed source bound and needs no extra hypotheses. Removing beta=4 could further sharpen a concrete computation, but is unnecessary for validity.

## Asymptotic and scope checks

If n is a positive fraction of p, E_*=O(n), and A~c sqrt(n) with c²>3/2, then K~(c²−1)n is positive and linear in n, while S2=O(pn)=O(n²). Either moment bound leaves only O(1) possible shapes. This is conditional on the unproved low-energy input, exactly as the source note says. The reciprocal symmetry v_t=v_(1/t) does not supply a bound on other collisions by itself.

Passing this necessary shape screen does not prove that the difference roots lie in D or that a high-agreement polynomial exists. No uniform low-energy theorem, prime-field construction, or general monomial exclusion follows from the audited algebra alone.
