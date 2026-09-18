# Translated grid: matched-parameter comparison with inspected primary results

2026-09-18. **No inspected theorem or immediate transformation establishes the entire conjunction below. This is a bounded non-subsumption audit, not a historical-priority assertion.** No manuscript edits.

## The precise conjunction

The current `translated_grid_polynomial_gap.tex` proves prime-alphabet ordinary RS codes with message dimension 3, two individually far endpoints and exact ordinary common agreement A, and

    A~T~sqrt(2n),  T=A+d<sqrt(2n),
    d=Θ(n^(1/6)/log n),
    B=Ω(n^(4/3)log n) singleton threshold labels,
    p=Θ(n^(4/3)(log n)^4).

Both A and T exceed n*a1(3/n) eventually, with T/(n*a1(3/n))→2/sqrt(3). Successful witnesses need not have exactly T matches. The bad-label fraction is only Θ((log n)^−3) for this construction, not constant. Its rate is 3/n and its normalized source gap is Θ(n^(−5/6)/log n). The relaxed threshold-A list bound L+1=Θ(sqrt n) is local to this received line, not a uniform code-wide list bound.

## Diamond–Gruen: generic mass mechanism does not specialize to these parameters

Primary: [On the Distribution of the Distances of Random Words](https://eprint.iacr.org/2025/2010), Theorem 2.5, Definition 4.1 and Theorem 4.14. The primary theorem/proof was read in `tmp/cs_novelty_audit/dg.txt`; the current ePrint metadata was also checked. The cached-text argument, rather than an assumption about any uninspected editorial revision, supports this comparison.

Theorem 2.5 converts ambient near-word probability into a near-label count on a line through a deep hole. Their displayed family has q=n^(c+1), dimension and target agreement of order n^(1/3), and arbitrarily large fixed polynomial label exponents. Those are stronger counts in a different regime; the dimension is not three, and its agreement lies below the first-order curve.

More decisively, at the grid's actual n,p,T, a uniform random word U obeys the elementary upper bound

    Pr[agr_3(U)≥T] ≤ p³ binom(n,T)p^(−T)
                  ≤ p³ (en/(Tp))^T.

With p=Θ(n^(4/3)(log n)^4) and T~sqrt(2n), the logarithm is at most −(5/6+o(1))T log n. Even multiplying by p still tends to zero. Thus the ambient-mass lower-bound mechanism cannot certify the desired polynomial label count at these matched parameters. This does not rule out a different structured use of their ideas.

## Crites–Stewart: the required entropy window fails quantitatively

Primary: [On Reed–Solomon Proximity Gaps Conjectures](https://eprint.iacr.org/2025/2046), Theorem 1 and Corollary 1, checked in `tmp/cs_novelty_audit/cs.txt`.

Their all-label corollary requires, in its strict-dimension convention, at least

    k ≥ n(1−H_p((n−T)/n))+2

(and an additional nonnegative square-root term). At the grid's parameters,

    n(1−H_p(1−T/n))=(5/8+o(1))T,

since log(n/T)/log p→3/8. This diverges, while k=3. The sufficient hypothesis therefore fails by order sqrt n. Their general random-center mass mechanism is bounded by the same tiny ambient probability as above. These are concrete parameter failures, not merely missing singleton wording. Their prescribed far direction plus near center also does not automatically supply two far projective points.

## Krachun–Kazanin–Haböck: fixed-rate strengths, but dimension-three specialization collapses

Primary: [Failure of proximity gaps close to capacity](https://eprint.iacr.org/2026/782), Theorem 1 and Appendix A, Propositions 3–4. Full text checked in the locally cached `kkh2026_782.txt` under the archived actual-list-literature directory.

Their theorem supplies prime polynomial alphabets, multiplicative-subgroup domains, any fixed rate, arbitrarily large fixed polynomial label exponents, and coordinate gaps Θ(n/log n). A simple polynomial-source shift of their quotient construction already supplies two far endpoints; that feature alone is not a distinction. Their fixed-rate agreement nevertheless tends to the code rate, below first order, and the stated theorem cannot be specialized by replacing its fixed rate with 3/n without a new uniform argument.

The explicit Appendix A compiler permits a sharper direct check. Its strict message dimension is

    J=(r−2)m+1,

and target agreement is rm. Enforcing J=3 gives only (m,r)=(1,4) or (2,3), hence target agreement at most six. This is not the required Θ(sqrt n) threshold. Taking r=2 and enlarging the constant code to dimension three also does not provide the desired population: forcing 2m~sqrt(2n) and n=sm leaves binom(s,2)=Θ(n) canonical supports, hence only O(n) labels. The reserved-fiber padded variant has the same obstruction: J−1=(r−2)m+w=2 forces bounded m for r≥3, while r=2 again yields only O(n) supports at T~sqrt n.

This does not exclude all adaptations of KKH, but it rules out the immediate low-dimension quotient specialization. Their larger fixed-rate coordinate gap is not a matched improvement at dimension three.

## Ben-Sasson–Carmon–Haböck–Kopparty–Saraf: almost-quadratic counts at the opposite rate extreme

Primary: [On Proximity Gaps for Reed–Solomon Codes](https://eprint.iacr.org/2025/2055), Theorems 1.15 and 1.16, checked in the cached `bchks2025_2055.txt`.

Theorem 1.16 already gives prime-alphabet examples with q−1 nearby labels and count Ω(n^(2−8ε)), but its dimension is n−Θ(n^ε), not three, and its tested radius is half the vanishing relative distance. Theorem 1.15 likewise has dimension n−c. These are important stronger count results in a high-rate regime, not the grid's low-rate conjunction. Passing to the dual RS code does not preserve individual Hamming-nearest lists or the received-line profile; it is not a valid automatic conversion to dimension three. No such preserving transformation appears in the inspected proof.

## Closest constructions already in this repository

1. The quadratic intersection bank with one fresh match already gives Θ(n^(3/2)) singleton labels at dimension three and the same above-first-order/below-Johnson placement, but its source gap is one. Therefore neither fixed dimension, singleton labels, nor that placement is newly supplied by the grid in isolation.

2. The iid occupancy family already keeps dimension three and has a positive fraction of native labels singleton, with gap Θ(log n/log log n). At the grid's polynomial gap, its balanced formula forces p<n. For every admissible p≥n its expected qualifying selected-bank label count is at most nL(e t/(dn))^d=o(1), as detailed in TRANSLATED_GRID_SECOND_PASS_AUDIT.md. Thus that existing guarantee does not attain the matched d.

3. Full-fiber covers already give polynomial gaps and singleton labels. At matched n,d their standard fixed-bank count scales as (n/d)^(3/2), or n^(5/4)(log n)^(3/2) at the grid's gap; the grid's count is larger. The cover also raises message dimension with d, whereas the grid keeps it three. This is a comparison of these proved constructions, not a universal cover bound.

4. The norm/quotient entropy-completion constructions supply all interior labels with polynomial prime alphabet at fixed rate and inverse-log gap. Their low-dimension canonical-support specialization has the count obstruction described above; their fixed-rate theorem does not subsume the grid. Conversely, the grid does not subsume their all-label, fixed-rate, or selected-fiber guarantees.

## Meaningful conclusion and remaining gaps

The concrete additional result is **polynomially growing source separation while preserving dimension three, prime alphabet, above-first-order/below-Johnson placement, exact endpoint/common agreement, and a superlinear singleton-label count**. The inspected primary theorems and the obvious origin shifts, parameter specializations, and covers do not yield all of these together.

This does not establish first discovery, optimal exponent, or fixed-rate progress. In particular B=o(p) and p=o(n²). The existing finite DKT O(n²) certificate therefore gives only the trivial field-size upper bound p here; the construction does not match a nonvacuous quadratic DKT count. The first-order excess and the source-to-threshold gap are different quantities and must not be interchanged.

Unresolved questions include a finite onset/explicit prime-and-grid certificate, optimal gap/count tradeoffs at dimension three, and whether a different known low-dimensional incidence construction gives the same asymptotic conjunction. Those require separate work. The present comparison makes no conclusion from the absence of a search hit and no protocol-security claim.
