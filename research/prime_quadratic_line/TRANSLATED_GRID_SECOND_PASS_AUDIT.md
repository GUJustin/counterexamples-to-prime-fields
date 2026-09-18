# Adversarial second pass: translated-grid polynomial gap

2026-09-18. Reviewed the complete argument in TRANSLATED_GRID_POLYNOMIAL_GAP_INDEPENDENT_AUDIT.md again, specifically attempting to break the combinatorics and probability coupling. **No fatal error found.** This is a second pass by the same auditor, not an additional independent agent's proof.

## 1. Sidon signs, repetitions, and graph labels

The quartic-class argument needs p≡1 mod4, not necessarily p≡1 mod8. A ratio a/b of two primes in the same quartic class is a fourth power, say t^4. The choice θ=t² is square and satisfies θ²=a/b. The other root is also square because −1 is square, but only one is selected. Arbitrary choices of these signs cannot create a pair-product collision: equality of θ-products implies equality of their squares, to which the integer-factorization argument applies.

For two unordered edge pairs, squared-product equality gives

    a1 a2 b3 b4 = a3 a4 b1 b2 mod p.

Each side is ≤H^4<p, so equality is literal. Since the numerator and denominator vertex sets consist of disjoint primes, their multisets must separately agree. If either vertex multiset repeats a vertex, there is only one possible edge multiset. If both vertex multisets have two distinct elements, different edge pairings require all four edges of a C4. Thus the proof covers repeated pairs, shared vertices, and all sign choices. Distinct edges cannot give θ=±φ because that would give the same rational a/b by the same integer argument.

The point/nonvertical-line incidence graph over a prime field of size q has q² vertices on each side, q³ edges and no C4. Taking q within a constant factor of the square root of the smaller available prime-vertex set gives the claimed Θ((H/log H)^(3/2)) bank. No distribution of small primes among quartic classes is assumed: the largest of four classes suffices by pigeonhole.

## 2. The two random requirements really can occur together

The eligible-square count and cross-label collision count are dependent. The proof does not assume otherwise. Let X be the retained coordinate count after all ratio/core deletions. It proves EX≥(1/2−o(1))M² and X≤M², which gives Pr[X≥M²/4]≥1/3−o(1). Separately, the raw cross-label count C has EC=o(LHM). Markov therefore gives Pr[C>LHM/64]=o(1). Subtracting this bad probability from the first event proves a nonempty simultaneous event.

Ratio equality for two distinct grid positions remains a nontrivial affine equation even if the positions share a row or column. Zero denominators were excluded first; counting the entire affine equation only overestimates collisions. The same applies to core-ratio deletion. Losing k−1 representatives of a k-fold repeated ratio costs at most binom(k,2), so pair counting legitimately bounds deletion loss.

Raw labels are indexed by an integer k=a u+b v and their bank parameter θ. The interval length is <p, so distinct k within one bank cannot alias modulo p. Across banks, the translation coefficients θ−φ and θ^−1−φ^−1 are nonzero. Every pair therefore collides with probability 1/p, regardless of the square-retention rule. Using the whole raw interval, rather than just retained rich labels, is what makes the later singleton assertion valid.

The rich-fiber step is deterministic conditional only on X≥M²/4. Every retained coordinate supplies one incidence to every bank. The common upper bounds K≤3HM and Dmax≤3M/H consequently guarantee ≥HM/16 rich labels separately in every bank. Removing endpoints of all cross-bank raw-label collision edges loses at most twice the edge count, even for collision components containing many banks. This yields the advertised Ω(LHM) distinct labels.

## 3. Singleton lists, exceptional zero label, and padding

The one indispensable exception is the zero polynomial at λ=−c0, which matches the entire grid. It is explicitly discarded. For every other label, every quadratic outside the bank has ≤L core matches, ≤2M grid matches, and ≤3 neutral matches. This is <A for sufficiently large L. Constants are included: a nonzero constant can match only one grid row, while zero matches no grid point except at the discarded label.

At a surviving rich label, no second bank word can have any grid agreement, because all cross-bank raw-label collisions were removed. Its total agreement is therefore just A. The owner has ≥A+d. Thus the complete degree-≤2 threshold list is a singleton; it is not merely a singleton within the selected bank.

Neutral coordinates can be chosen outside all old points, zero, and the roots of X³−Pθ for all banks. There are at most 3L such extra roots and p≫n. They preserve each bank's exact A baseline while adding at most three matches to any outsider.

For CA, a nonzero explaining direction has at most two zeros across the entire zero-direction block and at most 2M matches to 1/U on the grid. A nonzero constant direction satisfies the stronger one-row bound. The zero explaining direction restricts the intercept to core and neutral matches, whose maximum is exactly A. Therefore CA=A without a genericity or independence assumption on the two explaining quadratics. An invertible change to two far finite endpoints preserves this value.

Choosing both endpoints outside the union of raw bank labels and the exceptional zero label is possible because LK=o(p). Each such word has exact agreement A, including against all outsider quadratics. For normalized affine mixtures the resulting parameter map is an affine bijection, so there is no loss in the retained-label count; a different unnormalized-pencil convention can require the usual one-label adjustment.

## 4. Matched comparison with iid random occupancy

Use B_old for the number of labels, to avoid confusing it with the translated-grid side length M. In the earlier iid fresh-word construction, a fixed bank and fixed label get a binomial occupancy of mean μ=t/p, with t~n/2, L~sqrt(n/2), and threshold d additional matches. The balanced rare-event prescription is

    L μ^d/d! ~ 1,
    p ~ t (L/d!)^(1/d).

Stirling gives

    log p = log n + (log n)/(2d) − log d
            + O(1 + (log d)/d),

and when log L/d→0 the sharper ratio is p/n~e/(2d). The number of labels certified by that balanced regime is Θ(p), so the same logarithmic scale applies to B_old. These formulas assume the usual rare-occupancy approximation and explain its parameter choice; the next bound gives a rigorous obstruction to using that mechanism at the proposed polynomial gap.

For any actual alphabet size p≥n, the expected number of labels with at least d matches for some selected bank member is bounded directly by a union bound over bank, label and d fresh coordinates:

    E B_old ≤ p L binom(t,d) p^(−d)
            ≤ n L (e t/(dn))^d,

where the second step uses d>1 and p≥n. At d=Θ(n^(1/6)/log n), its logarithm tends to minus infinity: d log d dominates log(nL). Thus E B_old=o(1). The endpoint-exclusion variant, with at most O(L) forbidden values per coordinate, changes the bound by a factor exp(O(dL/p))=1+o(1) in this regime and has the same conclusion.

In particular the old balanced choice would require p<n and is inadmissible. For admissible fields, a uniformly random fresh word has no qualifying selected-bank label with probability tending to one. This does **not** prove that specially structured words cannot exist; the new translated grid is exactly such a structure. It excludes the old typical-random occupancy certificate at the same polynomial gap, not all possible probabilistic arguments or all rare sample outcomes.

The earlier deterministic full-fiber cover also already supplied polynomial gaps. Its label count at matched n,d scales as (n/d)^(3/2), which at the present d is n^(5/4)(log n)^(3/2), smaller than the new n^(4/3)log n. This comparison does not match message dimension: the cover raises it with d, while the grid retains dimension three. No claim that polynomial gaps themselves are new is justified.

## 5. Final scope

The audited scale is Ω(n^(4/3)log n) singleton labels and additive gap Θ(n^(1/6)/log n), or normalized source-to-threshold separation Θ(n^(−5/6)/log n). It is not n² count tightness, not fixed rate, and not a practical finite-parameter certificate. The neutral-padded threshold lies just below Johnson and asymptotically a fixed multiple of sqrt(n) above the first-order boundary. Further manuscript use should retain all of these qualifications.
