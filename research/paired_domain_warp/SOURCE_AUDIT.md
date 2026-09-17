# Character-sum input and comparison

Primary source read September17,2026:
Bourgain, Garaev, Konyagin, Shparlinski, On the hidden shifted power problem,
arXiv1110.0812v2, Lemma17 on printedpage10/PDFpage10.
https://arxiv.org/pdf/1110.0812
The existing paper bibkey is bgks-shifted.

The lemma bounds a product of characters evaluated at distinct shifts,
with at least one nonprincipal character, times an additive polynomial
phase. With2r shifts and constant phase, its bound is2r sqrtp.
Here each chi_j(x_j²-a²) splits into chi_j(a-x_j)chi_j(a+x_j)
times a constant. The2r shifts are distinct because the x_j are nonzero
and their squares are distinct. Deleting0 andthe±x_j costs at most2r+1.
This yields the conservative lambda used in paired.tex.

No use is made of the cryptanalytic algorithms elsewhere in that paper.
The cited character-sum theorem is the only external analytic input in
the multiblock proof. The simpler single-pair curve argument instead
uses Cafure–Matera Cor5.6, already audited in cubic_domain_warp.

Comparison checked against Kambire, arXiv2604.09724v1, Theorem1 and
construction on pages1–3. That result uses multiplicative subgroups,
subset sums, and quantitative Linnik, with polynomial-size fields and
many nearby labels. The paired-block argument here uses random paired
short domains, joint product images, and covers every nonzero label.
This comparison does not claim an exhaustive novelty search.


Completion strategy attribution (2026-09-17): Erdős–Rényi, Probabilistic
methods in group theory, Journal d'Analyse Mathématique 14 (1965),127–138.
Primary PDF https://renyi.hu/~p_erdos/1965-15.pdf read, especially Theorem2,
printed pages132–136. Its proof completes a dense subset-sum image by random
translates and iterates a conditional missing-set estimate. Our completion
uses that strategy with a nonuniform character-controlled distribution,
exclusions from previous choices, and paired alternatives preserving degree.
The manuscript credits the strategy; it does not assert this general
probabilistic method is new. The institute's publication list independently
confirms bibliographic metadata: https://renyi.hu/en/node/4094.
