# Independent small-set quadratic graph incidence audit

2026-09-19. PASS after the final source clarification. Primary Rudnev, Milojevic–Sudakov–Tomon and the author VC preprint checked directly. The source now uses only the accessible author-preprint Theorem 1.4 and makes no claim about the unavailable published theorem numbering. No source gap remains; no manuscript edits.

The graph lift has no three collinear points by its Vandermonde projection. Pairwise distinct quadratic planes share at most two graph points, so the stated forbidden-subgraph hypotheses apply. Rudnev gives only O(L√n) in the relevant range. In Milojevic–Sudakov–Tomon Theorems 1.1–1.2, substituting dimension three gives balanced exponent 3/2 and L√n for n≤L≤n^(3/2); their varying-field sharpness assertions do not supply prime-field graph examples at n<p. The author VC preprint’s unrestricted pair-intersection estimate is as quoted; optimizing yields nL^(2/3), not a saving. Normalization outside fewer than p planes is legitimate because their union has fewer than p³ points. The final replacement explicitly records the hypotheses 0<α<1 and n≥6p^α. The balanced choice p^α=n^(1/3) satisfies both for sufficiently large n<p, yielding O(n^(5/3)). The independent VC-dimension-three example is retained only as a caution about any added hypothesis, without invoking an unverified published theorem.

## Conditional saving and examples

The sufficient balanced estimate is correctly formulated for arbitrary n distinct quadratic planes. If there were at least n planes each meeting the graph in c√n points, choosing n of them would contradict O(n^(3/2−ε)) for sufficiently large n. For a smaller list, pad it with arbitrary distinct quadratic planes (there are p³ available and n<p); the total incidence bound gives Lc√n≤C n^(3/2−ε), hence L=O_c(n^(1−ε)). This padding would not be justified by a theorem restricted to specially rich plane families, but the proposed statement has no such restriction.

The eight-polynomial VC example is valid: interpolation at three distinct coordinates gives eight distinct value patterns, and disjoint blocks of T other coordinates make every polynomial T-rich without altering the shattered triple. It refutes automatic VC dimension two, not the proposed power saving.

The anisotropic norm quadric example is also exact in odd characteristic. No projected nonzero line direction is isotropic, so each spatial line meets the graph at most twice. Completing the norm gives p+1 points on each nonzero-level plane and one at zero level, yielding p²(p−1) rich planes. Its p²-point size and repeated first coordinates violate the target n<p graph-lift hypotheses.

## Existing repository constructions: no demonstrated contradiction

The actual prime-alphabet examples must be distinguished from large ordinary lists at ONE received word. The square-linear/two-ray construction has many challenge labels but singleton threshold lists, so its linear challenge count does not contradict a sublinear list conclusion. The translated/collision/asymmetric conic constructions explicitly retain only O(√n) bank polynomials; their superlinear counts are again counts of different challenge words. They do not exhibit n planes each with Θ(√n) incidences against one fixed quadratic graph. The KKH quadratic enlargement likewise counts many different line parameters, while the finite-rate prime constructions use growing message dimension rather than degree-two explanations. Odd Gold and trace–norm examples use extension-field domains and growing code dimension, so also fall outside this graph-specific statement.

This establishes that none of those displayed constructions demonstrates a contradiction. It is NOT a proof that every undisplayed quadratic plane in their graphs obeys the proposed estimate, nor an exhaustive theorem about all repository configurations. A verified balanced graph-incidence lower bound of order n^(3/2) would be a genuinely different object and would falsify the proposed sufficient saving.

Primary sources inspected:
- https://arxiv.org/pdf/1407.0426v5
- https://aleksa-milojevic.github.io/publications/PointHyperplaneIncidences.pdf
- https://arxiv.org/html/2303.00330

Frozen source SHA256: `ca03ea858da7201bd855bad90289439ee6e6a54c32baef58f1628fae1b118b98`.
