# Independent rational quotient-head CRT audit

PASS, 2026-09-19. Entire frozen source inspected. No finite computation or manuscript edits.

The CRT formulas have the correct powers: multiplying K_H by N_H K_H^(−3) modulo M_H gives N_H/K_H² off the kernel and zero on it. The indicator and arbitrary-kernel-value representatives have degree below n and provide precisely the claimed t-dimensional supported space.

For a nonzero quotient coefficient, αN_H−qK_H² is nonzero by coprimeness and has degree at most k+ell−2. Adding at most t kernel matches yields n−(5ell+3)/2, strictly below both target thresholds. For a supported word, every nonzero codeword agrees at most k−1+t<n−t, so zero is the exact nearest witness with agreement n−wt(u), and is unique at the tested threshold. These arguments also establish the dimension t+1 of W_H.

The cross-subgroup cleared numerator degree is max(2ell−1,k−1+4t)=n−2ell−2, smaller than n−ell+1 off-kernel nodes. Thus the rational equality is exact. Genuine double poles force both quotient coefficients to vanish; minimum distance and disjoint supports then eliminate the remaining kernel corrections. This proves W_H∩W_H′=0, without asserting a bound on arbitrary transversals.

The common-denominator argument correctly uses only the degree bound on S·RS_k, not equality with a larger RS code. Under k+r+4≤L<n, evaluation remains injective, triangular degree flags apply, and the Laurent difference is O(X^(k+r−L+1))=O(X^(−3)). The target root bound correctly forces L≥T whenever T>k+r−1. Therefore r≤2ell−d−5 is sufficient; at ell=23 the bounds 36 and 35 are correct.

For distinct denominators, multiplication by SS′ changes the code degree cap to k+r_H+r_H′ and numerator degrees to L_H+r_H′ and L_H′+r_H. Conditions (9) ensure the required four-degree separation and all degrees below n. Leading coefficients can be normalized by scaling the two source pairs, leaving their rational quotient maps unchanged. The same Laurent proof therefore applies. Denominators remain nonvanishing on D as stipulated by the regularization setup.

The exclusions in the final paragraph are essential and accurate: extra kernel corrections on weighted rational heads, denominator zeros with separately assigned values, degrees reaching n, and arbitrary moving cofactors are not covered. The result closes these specific quotient-head regularizations, not general elliptic received pencils.

Frozen source SHA256: `77444ca164d27013cfc11df5a0f6c13123475116ee3ddb330fed5ef7ebdbb993`.
