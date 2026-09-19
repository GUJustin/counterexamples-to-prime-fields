# Independent audit of sextic trace-head pullback gate

PASS, 2026-09-19. Actual source inspected in full. No finite computation or manuscript edits.

The normalized separable Vélu map preserves the invariant differential, giving F(X)(Y′)²=Y³+A_HY+B_H. Expanding Y=X+u/X+v/X² gives 5u=A−A_H and 7v=B−B_H. If the targets agree but the maps first differ by cX^(−m), subtraction gives (2m+3)c=0. The denominator-degree bound m≤2ell−2 and the explicitly stated p≥n>4ell−1 make the coefficient nonzero. Thus equal first two Laurent coefficients do determine the subgroup in this parameter range; no small-characteristic uniqueness assumption is hidden.

For monic polynomial weights clearing the denominator, F_H and G_H have distinct degrees L and L−1 below n. Evaluation below n is injective, so equality of their two-dimensional syndrome planes forces the same L and triangular relations G_H′=G_H+Q and F_H′=F_H+aG_H+P with degP,degQ<k. The absence of a constant Laurent term gives a=0. The resulting ratio difference is O(X^(k−L+1)); L≥k+4 fixes both inverse-power coefficients and hence forces identical subgroups. Arbitrary invertible source recombinations and codeword shifts are already included by plane equality.

The target step is correctly restricted to nonzero syndromes: a polynomial representative of degree at most L<n cannot have more than L agreements with a strict-degree-<k codeword. For ell≥23 and d∈{5,6}, T_d−k=2ell−d−1≥39, so a plane reaching the stated target is within the proved degree range. The kernel-value discussion correctly separates polynomial evaluations from independently prescribed pole values. A common weight divisible by all K_H² makes the second word zero and cannot supply two independent heads.

Scope is essential and correctly stated: this excludes identification of these two polynomial-weighted quotient-head planes below the domain length. It does not exclude a global pencil meeting multiple unequal planes, rational weights with prescribed kernel values, additional heads, representatives of degree at least n, or arbitrary moving omission locators. No broader elliptic proximity obstruction follows.

Frozen source SHA256: `2e4e8e78fb657c4e5847778456893dd4d160d337e12c43c3a48ec90e9a9d1a5f`.
