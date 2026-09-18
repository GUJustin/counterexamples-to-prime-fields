# Split monomial/constant bank: bounded prior comparison

2026-09-18. Independent comparison of the c=14 construction. This is not a novelty or priority certificate. No manuscript changes.

## Matched statement and its limitations

The independently checked construction has strict message dimension 3,

    n=128t²+1, A=CA=14t, T=16t,

with two endpoints of exact agreement A, exactly t²+1 nearby normalized affine parameters, and singleton lists at threshold T. The nonzero product labels have exact agreement T; the additional zero label has larger agreement. Both A and T exceed the first-order curve eventually, while T²<2n. The source gap is 2t, and its ratio to T−3 tends to 1/8.

It works over any sufficiently large odd field with q>n+6t+1 and enough square-group order; choosing prime p=Θ(n) makes the exceptional fraction constant. Over arbitrarily large prime fields its guarantee is Θ(n/p), not Θ(n²/p). Thus it is not intrinsically a prime-field separation, not a superlinear count result, and not tightness of a nonvacuous quadratic DKT upper bound. The useful conjunction is a constant fraction of the capacity margin separating two equally far endpoints from singleton near words, at dimension three and above the first-order curve.

## The serious nearby baseline: KKH with r=2 and code enlargement

Primary: Krachun–Kazanin–Haböck, [Failure of proximity gaps close to capacity](https://eprint.iacr.org/2026/782), Appendix A, equations (5)–(6), Propositions 3–4. Read from the archived primary `kkh2026_782.txt`, pp. 15–16. Their degree convention is degree at most k, so dimension is k+1.

Write Y=X^m, take s tag fibers, n=sm, and b outside the tags. The r=2 quotient construction, after the elementary origin shift, has

    f=Y+b, g=−1/(Y−b).

For a pair of distinct tags S, put V_S(Y)=∏_{a∈S}(Y−a). At λ=−V_S(b), a constant witness agrees with f+λg on 2m coordinates. Enlarging the constant code to degree at most two preserves these witnesses. For m>2 the polynomial source has exact agreement m, and clearing the denominator gives agr(g)≤m+2 (with lower bound m). There are binom(s,2) canonical supports.

**The count objection used for the superlinear grid theorem does not distinguish the present result.** If s,m are both Θ(sqrt n), the available pair count is Θ(n), exactly the scale now sought. Also, two-far origin shifting is already available; it is not new in isolation.

At the *canonical* threshold 2m, demanding 2m<sqrt(2n) gives s>2m. The source m is then below the first-order threshold. This does prevent a literal matching of canonical nearest agreement and source ratio with 14t versus16t.

However, merely lowering the tested threshold invalidates that simple obstruction. Formally take s/m→c with 1/2<c<2/3. Then

    sqrt(3n/2) ~ sqrt(3c/2)m < m < sqrt(2c)m ~ sqrt(2n).

One can test between m+2 and sqrt(2n), while the canonical constants still have 2m matches. Thus placement above first order and below Johnson, plus a linear support count, is not by itself a separation from this adaptation.

The original inspected proof did **not** give the following conjunction after enlargement. The new local proof in `KKH_R2_QUADRATIC_ENLARGEMENT.md` resolves the first two gaps and gives a finite comparable-prime-size example; the list below records the original missing steps, not the current state:

* It does not exclude additional nonconstant quadratic witnesses or prove singleton lists. Its immediate per-fiber bound is 2s for each nonconstant quadratic. For c>1/2, 2s≥sqrt(2sm), so this bound cannot exclude outsiders at a below-Johnson threshold.
* It does not make both enlarged-code endpoints have the same exact agreement m, nor identify all near parameters or their exact agreement at the lowered threshold.
* It does not certify Θ(n) distinct singleton pair labels with p=Θ(n) in this balanced-fiber regime. Proposition 4 supplies p/(2n) labels in its stated fixed-rate, p=Θ(n^β), β>12/5 regime; the fixed-rate asymptotic theorem cannot simply be specialized to dimension three. Its prescribed-power subgroup prime theorem is also not a p=Θ(n) theorem.

These are missing arguments, not impossibility claims. A sharper analysis of this r=2 family is the most concrete possible source of subsumption. In particular, absence of a singleton assertion in the theorem statement alone would not suffice; the explicit available root bound above explains what the inspected proof currently fails to certify.

## Existing constructions in this repository

The original quadratic pair-intersection bank already has dimension three, prime alphabets, singleton near lists, above-first-order/below-Johnson placement and Θ(n^(3/2)) labels. Its source gap is one. Random occupancy increases this to logarithmic scale; the translated-grid and collision-bank families give polynomial gaps, but their gap divided by sqrt n tends to zero. Those results are stronger in count and weaker in the constant relative source separation now considered. Simply lowering their threshold cannot increase their source-to-threshold gap.

The deterministic full-fiber cover (`DETERMINISTIC_CORRELATED_COVER.md`) has dimension 2s+1 and gap s. Holding dimension three forces s=1. It therefore does not transfer its growing separation into the present dimension-three conjunction.

The projective quadratic example (`binary_characteristic_transfer/projective_quadratic_line.tex`) already gives dimension three, Θ(n^(3/2)) singleton labels, a Θ(sqrt n) source gap, and a below-Johnson/above-first-order tested threshold. Its exact source agreement is only 2(p+1), whereas n=2(p⁴+p³+p²+p+1); the sources themselves are below first order, and the construction uses an extension alphabet. The scaled Frobenius example (`quadratic_frobenius_core/scaled_fiber_padding.tex`) likewise gives n=9p², exact sources/common agreement 2p and threshold4p, with Θ(p³) singleton labels over F_(p⁴). Its sources are below the first-order scale sqrt(13.5)p. Consequently neither constant-order normalized loss nor dimension-three singleton examples are new features individually. Ordinary neutral padding does not raise their endpoint agreements, and standard common-zero padding raises message degree; no checked automatic transformation gives the present conjunction.

## Other inspected primary mechanisms

Crites–Stewart ([2025/2046](https://eprint.iacr.org/2025/2046), Theorem 1/Corollary 1) and Diamond–Gruen ([2025/2010](https://eprint.iacr.org/2025/2010), Theorem 2.5) do not directly certify these matched low-dimensional parameters. For p≥cn and T=Θ(sqrt n), the elementary ambient near-word bound is

    Pr[agr_3(U)≥T] ≤ p³(en/(Tp))^T,

and even p times this tends to zero. This explains the failure of a generic ambient-mass line guarantee here, rather than merely noting missing endpoint or singleton wording. Their other parameter regimes remain incomparable. BCHKS ([2025/2055](https://eprint.iacr.org/2025/2055), Theorems 1.15–1.16) gives stronger counts near rate one; duality does not preserve received-line nearest-list profiles and is not an immediate dimension-three transfer.

## Updated verdict after the odd-fiber enlargement proof

The proof in `KKH_R2_QUADRATIC_ENLARGEMENT.md` now establishes a finite KKH-derived example with dimension three, exact equal endpoint/common agreement, sources above first order, a tested threshold below Johnson, constant relative loss, and linearly many singleton labels. Its exact integer verifier passed independently. At n=33513480 and p=2147483647, A=7161, tested T=8184, and at least10893038 labels are singleton. Thus that conjunction alone is no longer a justified distinction for the split bank.

The comparison does not establish complete subsumption: its actual nearby agreement is2m=14322, not T; additional nearby labels may be nonsingleton; and no infinite balanced-divisor family with p=Theta(n) is established. The split bank retains its exact all-label profile and elementary prime-size guarantee. These distinctions do not improve the exceptional-count exponent. No priority or overall-strength claim follows.
