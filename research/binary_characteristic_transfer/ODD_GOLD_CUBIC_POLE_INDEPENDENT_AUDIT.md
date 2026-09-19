# Independent actual-text audit: odd Gold cubic-pole classification

Status: PASS, 2026-09-19. Source inspected in full; no manuscript edits or finite scan.

## Critical checks

1. The derivative is exactly a X^(p^s)+a^(p^(s+1)) X^(p^(s+1)); its p^s-th root is L_a=a^(p^(s+1))X+a^pX^p. A nonzero kernel root η satisfies η^(n−1)=−1 by the norm exponent calculation. Thus η^n=−η and every derivative root lies in B₂. The homogeneous kernel has no nonzero native element, so each affine derivative has a unique native root and all roots are its translate by η Fp.
2. For any Fp-valued polynomial of degree at most d, the identity G^p−G=ΛG′ follows by divisibility and evaluation of the derivative on B: the quotient degree pd−n=p^(s+1) is less than n. At a nonnative root, Λ is nonzero and hence G′ vanishes. Therefore every nonzero Gold-plus-linear-trace polynomial splits over B₂; the purely linear-trace case has constant nonzero derivative and only native roots. Multiplicities do not affect the claim.
3. Since B₂ intersects the cubic extension exactly in B, evaluation at every cubic exterior pole is injective on the entire difference space. The P identity gives G₁(β)/G₂(β) in Fp*, and normalization then forces the same bank member. All P roots lie in B₂ (not all in B), which separately proves nonzero labels at cubic poles. The preliminary parameter audit has been corrected on this point.
4. The good-square-class sign is correct. The Gold power and square power have the same value multiset since both have gcd exponent two with n−1. The trace pairing determinant is square in odd extension degree: the conjugate Vandermonde determinant is Frobenius-fixed because its row cycle has positive sign. Standard odd-rank diagonal counting consequently gives the factor χ_B(a)χ_p((-1)^s t). At t=−1 the selected class is χ_B(a)=χ_p((-1)^(s+1)).
5. The equality factorization and coefficient descent apply to arbitrary extension-valued residuals. The exponent cap permits only single ones or a pair with circular gaps s and s+1: three ones would require 3s≤2s+1, impossible for s≥2. Coefficient cycles give exactly the stated Gold and linear traces. Completion, nonzero level, and derivative normalization recover exactly the normalized bank. Pole injection supplies singleton lists; all other agreements are at most T−1.
6. The source-degree dominance is r(r−p²+1)/p−1, positive already at r=p². This agrees with the corrected preliminary formula. The affine source change loses no bank labels; reciprocal agreement and common agreement remain k. The normalized first-order expression agrees with the even-dimensional formula after Q is replaced by r. Johnson slack is rT−n, giving 1134 at p=3,s=2. All stated finite integers (243,90,162,102,153,135,29403) are consistent.

## Scope

This establishes exact every-cubic-pole injection and exhaustive threshold lists for the inherited odd-dimensional Gold family, with the smaller exact message dimension. Its evaluation and alphabet fields remain nontrivial extensions, its dimension exceeds the characteristic, and no prime-alphabet or prescribed-domain conclusion follows. The prior-work attribution in the source is appropriately limited. The source’s finite example is explicitly algebraic, not represented as an enumerated fixture.

## Frozen source

`ODD_GOLD_CUBIC_POLE_EXACT_CLASSIFICATION.md` SHA256: `564733e7e01e2d83b799d9cd1eb8da244bd4822b64fa71bc47e094b321a73318`.
