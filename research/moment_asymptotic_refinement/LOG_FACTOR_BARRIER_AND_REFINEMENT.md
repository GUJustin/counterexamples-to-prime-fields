# Interval moment fibers: logarithmic barrier and a concrete refinement

This review read the existing main proof, the BEK attribution, the optimized gap corollary, and the already-proved growing-moment Gram estimate. It does not repackage those ingredients as new moment theorems.

## Exact reduction to height-one high-order vanishing

For two different equal-cardinality subsets A,B of {0,...,n−1} sharing their first s integer binomial moments, put

    Q(z)=Σ_(a∈A) z^a−Σ_(b∈B) z^b.

Then Q is nonzero, has coefficients in {−1,0,1}, degree<n, and (z−1)^(s+1) divides Q. Conversely those derivative identities give equality of the cardinalities and first s binomial moments of its positive and negative supports. A common padding set may alter their density, but does not itself make a large family.

The primary BEK paper, Theorems2.4 and2.7, gives a universal upper bound floor((16/7)√n)+4 for the order at1 of a nonzero height-one polynomial after removing its initial zero coefficients, and the classical lower construction of order c√(n/log(n+1)). Its real-coefficient Theorem2.5 attains square-root order but does not give coefficients in {−1,0,1}. The primary Borwein–Mossinghoff paper likewise records the minimum-degree bounds m²≪d1(m)≪m²logm for the signed-height-one problem. These checked sources do not provide the missing square-root-order signed construction; this audit is not an exhaustive claim about every paper through2026.

- BEK: https://people.tamu.edu/~terdelyi/papers-online/PLMS.pdf , Theorems2.4–2.7 and the derivative-vector proof of2.7.
- Borwein–Mossinghoff, *Newman polynomials with prescribed vanishing*: https://www.cecm.sfu.ca/~pborwein/PAPERS/P170.pdf .

Suppose the SAME integer-fiber method achieved log2 L≥cη^−2 for fixed c>0, with s≥ηn. Since L≤2^n, n≥cη^−2. Any pair of distinct fiber members would therefore give

    ord_1 Q≥ηn≥√c√n.

Thus removing the logarithm in this way would attain square-root-order height-one vanishing. The BEK upper bound also forces n=O(η^−2), so the target would require an exponentially large fiber at that square-root cancellation scale, not merely one extremal pair. A pair of high-order-vanishing polynomials would be an important ingredient but is insufficient for the desired exponential list.

This implication is explicitly about equal INTEGER moment fibers. Finite-field congruence fibers, unrelated evaluation domains, or a different list construction can evade it; they must supply their own counting theorem.

## Why the immediate alternatives do not remove the loss

Disjoint translated two-choice Prouhet blocks preserve the same moments, but if a block has length m and cancellation order s, BEK gives m=Ω(s²). With n/m disjoint switches their logarithmic family size is only O(n/s²)=O(1/(ηs)), at most O(1/η). Translation and independent switching alone do not amplify one high-order pair into the required exponential-density fiber.

Allowing bounded real coefficients or integer heights greater than1 produces weighted/multiset relations. Repeated evaluation points are not permitted in an ordinary RS domain, and perturbing repeated points does not preserve exact moments. No weight-to-squarefree-support conversion with the needed degree/agreement accounting was found.

A power-map packet domain also supplies no free gain: selecting whole B-point fibers replaces n by M=n/B and the number of canceled coefficients by the corresponding quotient moment count. The relative gap is unchanged, and the list count is the quotient problem's count. This does not improve the known dependence on the gap without a new quotient construction.

The existing Gram, conditional-moment and ellipsoid tools are already in the manuscript. Their growing-moment determinant cost retains (s²/2)log(n/s); they improve its s² term rather than erase log(n/s). A distinct sign-change theorem for many real roots is not a theorem about multiplicity at the single point1 and does not supply equal moments.

## A rigorous positive refinement already available

The manuscript's uniform Gram estimate is

    log2 D_G=(s²/2)[log2(n/s)+γ_G]+O(s log n+s⁴/n²),
    γ_G=3/(2 ln2)−2≈0.16404256.

Let H=H2(ρ), λ=log2(1/η). Taking n nearest the allowed rate denominator to H/[η²(λ+γ_G)], s=ceil(ηn), yields

    log2 L≥H²/[2η²(λ+γ_G)]−O_ρ(1/η).

The earlier complete-range estimate has γ_G+2 in place of γ_G. Thus the optimized Gram guarantee gains

    (1+o(1)) H²/[η² log2²(1/η)]

in logarithmic list size over the corresponding complete-range guarantee, while retaining the leading η^−2/log(1/η) order. This is a second-order sharpening, not logarithm removal.

For every sufficiently large prime, put b=log2p and h=H2'(ρ). Choose η=H/(b−h). Strict concavity gives H2(ρ+η)<H+hη=bη, proving the required strict Elias condition without the old b^−1/2 safety slack. Consequently

    log2 L≥b²/[2(log2b−log2H+γ_G)]−O_ρ(b).

The manuscript-ready one-page proof is `research/growing_m/proposed_gap.tex`. No main manuscript edit or novelty claim was made.
