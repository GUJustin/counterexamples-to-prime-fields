# Degree-two rational-pencil attribution and manuscript context

## Primary bibliography verified

Hector Pasten and Julie Tzu-Yueh Wang, **Extensions of Büchi's Higher Powers Problem to Positive Characteristic**, *International Mathematics Research Notices* **2015**(11), 3263–3297, DOI [10.1093/imrn/rnu033](https://doi.org/10.1093/imrn/rnu033). The publisher records online publication on 14 March 2014; the journal citation year is 2015. The exact arbitrary-label input is Theorem 3 in the [author manuscript](https://people.math.harvard.edu/~hpasten/preprints/PWposIMRN.pdf), not merely its consecutive-integer formulation.

The characteristic-zero input remains Pasten's Theorem 3.9 in the [primary manuscript](https://people.math.harvard.edu/~hpasten/preprints/pAdicTAMS.pdf). Both results and their exceptional-factor hypotheses should receive explicit attribution. The characteristic-zero eight-value threshold, the positive-characteristic square-value theorem, and factor-height additivity are prior work, not new conclusions of this paper.

## What the bounded priority search establishes

Targeted searches combined rational pencils, Büchi, polynomial sections, coefficient height, Möbius/fractional-linear families, Reed–Solomon lists, and agreement. No primary theorem explicitly giving this exact five-section 10D height bound or this rational-pencil agreement corollary was identified. Most Möbius/coding hits referred to Möbius inversion or evaluation-set transformations, which are unrelated. This is a bounded negative search result, not proof of priority.

The five-section reconstruction is elementary rational interpolation and Cramer's rule. The conic parameterization and degree-one generator characterization are classical. Present the contribution as the **explicit combination and coding consequence**, with its short-characteristic condition, rather than claim any of these ingredients as new. The stated constants 10D and twenty-one labels arise from this specific reduction; do not call them optimal.

## Connection to the existing manuscript and a sharper list bound

The surrounding appendices distinguish ordinary lists from exceptional received-line labels. The existing Riccati appendix already uses a local collision/multiplicity argument giving the sharp ordinary-list bound `L(A−D)<=n`. The Möbius family in the new bridge satisfies the same argument directly, so its provisional `2/eta` estimate can be sharpened.

Indeed let C_x be the sum of vanishing orders of all pairwise differences at x. The local Möbius reduction permits matching multiplicities h only in {0,1,L−1,L}. For L>=2,

`(h−1)(L−1)<=2C_x`.

This is immediate from C_x>=binom(h,2) for the two large matching classes; h<=1 is trivial. Summing over coordinates and using the degree bound on each pairwise difference gives `L A−n<=LD`. The L=1 case follows from A<=n. Therefore the complete finite-characteristic pencil bound is

`L <= max(40, floor(1/eta))`,

for agreement A>=D+eta*n and p>max(2,10D). In characteristic zero, the corresponding threshold-nine-label bound is `max(16,floor(1/eta))`. This sharpening uses an already present counting mechanism, not a new decoding theorem. The pencil-to-Möbius reduction remains the new application to be explained.

## Suggested introduction paragraph

We also restrict a class of algebraic families that could otherwise produce large ordinary lists. Suppose the candidate polynomials are sections of one rational pencil N(X,P)/T(X,P)=c whose numerator and denominator have degree at most two in P. Combining square-value theorems of Pasten and Pasten–Wang with an explicit coefficient-height bound shows that, in characteristic zero or over primes p>10D, only O(1/eta) degree-at-most-D sections can agree with any received word in D+eta*n positions. This concerns candidates in a specified rational-pencil family; it neither bounds all Reed–Solomon lists nor supplies a proximity-gap bound for arbitrary received lines.

The manuscript should retain the explicit constant maximum in the theorem even if the introduction uses O(1/eta). No main manuscript edits were made in this audit.
