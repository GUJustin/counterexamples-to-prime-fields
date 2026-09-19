# Odd-dimensional full-rank Gold compiler: bounded audit

Status: algebraic parameter PASS for s≥2; inherited asymptotic mechanism and population. No manuscript edits.

Let p be odd, s≥1, n=p^(2s+1), B=F_n, d=n/p+p^s, T=n−d, D=n−n/p, and k=(p−1)T/p. Reduce the trace polynomial Tr_{B/Fp}(a X^(p^s+1)) to degree below n.

The polar form is nondegenerate for every a≠0: a nonzero polar-kernel vector would imply an equation whose norm to Fp is simultaneously 1 and −1. Consequently the derivative-root polynomial F has only the translated center as a native root. Odd-rank quadratic-form counts select exactly half of a∈B* for which the level −1 has d points. (Scaling a by a nonsquare in Fp reverses the sign.) Translating by b∈B gives n(n−1)/2 normalized polynomials G=Tr(a(X+b)^(p^s+1))+1, each squarefree and fully split.

The exact reduced polynomial identities are G^p−G=ΛG′ and F^p=G′, where Λ=X^n−X. The leading coefficient of both G and F is a^(p^s); no additional scalar normalization is needed for P=FΛ/G to be monic of degree D. The center belongs to the complement of the roots of G, so P has exactly T distinct native roots. Moreover P^p=Λ^(p−1)−(Λ/G)^(p−1), giving deg(P−X^D)=k whenever pk>n(p−2)+1; the difference is n/p−(p−1)p^s−1>0 for s≥1.

The normalized G family is distinct. Equality of two P polynomials forces (G1/G2)^(p−1)=1 and hence G1=uG2 for u∈Fp*. Derivatives recover their common center and proportional a; evaluation at that center forces u=1. Thus the native residual population is exactly M=n(n−1)/2.

## Pole count and source bound

A simple sufficient pole count needs no stronger collision theorem. Every pair of distinct P has difference degree at most k. Averaging over F_{n^3}\B and applying the energy/Cauchy inequality supplies a pole with at least

    M / (1 + k(M−1)/(n³−n))

distinct evaluations. The residual factor F has nonnative critical roots as well: all its roots lie in the quadratic extension B₂, while Λ/G splits in B. Cubic exterior poles avoid both fields’ root sets, so none of those labels is zero. This corrects the preliminary claim that all P roots are native. Since k<n and M<n²/2, this is greater than 2M/3. This proves an Ω(n²) selected-pole count over the cubic extension of B; it does not prove every-pole injectivity or complete lists.

For the complementary Ω source argument, the exact dominance difference is

    (p+1)k−1 − [D+(p−2)n]
      = n/p² − (p²−1)p^(s−1) − 1.

The exponent in the second term is s−1, not s−2. At s=2 the difference is p−1; it is positive for all s≥2. The same source bound U=floor(((p+1)k−1)/p), and gap T−U=ceil(T/p²+1/p), therefore apply for s≥2. The s=1 instance requires the undominated maximum-degree bound instead and must not be included under this formula without checking it separately.

## Matched primary-source comparison

The read-only binary repository already contains this odd-dimensional mechanism in `sections/constructions/fullfield-elliptic.tex`, the odd-ambient part of the fixed-codimension proof (lines 363–454 in the inspected version). It explicitly uses Ψ_c=Tr(c x^(b^n+1)); proves odd-characteristic nondegeneracy by the same norm argument (lines 400–406); selects the (b−1)/2 full-size nonzero levels and their translations (lines 442–446); and applies the higher-rate compiler and collision averaging (lines 448–454).

To match notation, take its ambient dimension 2s+1, base b=p, radical/shortening parameters zero, and rank parameter t=s. Its level count is n/p+p^s and its native translated normalized population is n(n−1)/2. The prior high-row dimension is k_old=(p−1)²n/p²; the exact correction degree here lowers it by (p−1)p^(s−1). Thus the quadratic population, fixed-characteristic fixed-rate behavior, and collision conversion are inherited. Exact finite dimension, explicit coefficient formulas, or a stronger label/list classification would need separate attribution as refinements. No such stronger classification is established in this note.

The alphabet is F_{n³}, characteristic p is much smaller than k, and the evaluation domain is a full extension field. This does not yield a prime-alphabet or prescribed short-domain counterexample.

## Subsequent exact strengthening

The actual-text audit of `ODD_GOLD_CUBIC_POLE_EXACT_CLASSIFICATION.md` establishes that every nonzero Gold-plus-linear-trace difference splits over B₂. Consequently every cubic exterior pole is injective, and the exact M labels have exhaustive singleton threshold lists. The earlier averaged count above is a valid weaker bound, not the final result.
