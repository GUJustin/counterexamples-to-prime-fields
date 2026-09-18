# Random norm tags: independent logarithmic-gap audit

2026-09-18. **PASS.** This is an existence theorem using the known quotient compiler, Katz's affine-line estimate, and an elementary probabilistic tag choice. It is not a prime-alphabet theorem or an explicit efficient construction.

Fix d≥2 and 0<ρ<1. Put q=p^d, E=F_q, m=(q−1)/(p−1), and choose b generating E/F_p. Let s≤p−1. The following three finite conditions suffice:

1. ((d−1)√p+1)/(p−1)≤1/4.
2. 4(q−2) exp(−s/64)<1.
3. Write n=sm and J=floor(ρn), J−1=(r−2)m+w, 0≤w<m. Require 2≤r<s−1 and, with θ=r/(s−1),
   (q−2)s exp[−θ(1−θ)(s/2−2)]<1.

Then there is a set G⊂F_p* of size s and two received words on D={x∈E:x^m∈G}, |D|=n, such that for the strict-degree-J code,

    agr(f)=agr(g)=CA(f,g)=A=J+m−1,
    agr(f+λg)≥T=J+2m−1 for every λ∈E*.

Thus exactly q−1 affine labels qualify at threshold T, and the projective direction g is far too. No assertion about list uniqueness is needed.

## Simultaneous small character sums

For any nontrivial multiplicative character χ of E*, Katz gives
|Σ_(a∈F_p*)χ(b−a)|≤(d−1)√p+1. The population complex mean therefore has modulus at most 1/4 under condition 1. For a uniformly chosen s-subset G, the expected complex sum has modulus at most s/4.

Each real or imaginary coordinate lies in [−1,1]. The sampling-without-replacement Hoeffding inequality gives

    Pr(|Σ_G χ(b−a)−EΣ_G χ(b−a)|>s/4)≤4exp(−s/64).

Indeed a complex deviation exceeding s/4 forces one coordinate deviation exceeding s/(4√2); each two-sided real tail is at most 2exp(−t²/(2s)). The without-replacement version follows directly by applying Maclaurin's inequality to the positive numbers exp(λx_a): its exponential moment is no larger than sampling with replacement, followed by the usual bounded-variable exponential-moment estimate. Thus no independence assumption on the selected tags is hidden.

Union bound over the q−2 nontrivial characters proves that some single G satisfies |Σ_Gχ(b−a)|≤s/2 for every such χ. The argument applies to every character, including small-order characters; no character-power hypotheses occur.

## Exact dimension and source ledger

Reserve any a0∈G. Choose w points B of its norm fiber and let R be their monic locator. Define Y=X^m and

    f=R(Y^r−b^r)/(Y−b),  g=−R/(Y−b).

Use r-subsets S of G\{a0}. Their product characters have sum at most s/2+1 on s−1 tags. The fixed-cardinality Cauchy lemma therefore gives surjectivity of ∏_(a∈S)(b−a) onto E* under condition 3, since (s−1)−(s/2+1)=s/2−2.

For λ=−V_S(b), the witness R(P_S(Y)−P_S(b))/(Y−b), where P_S=Y^r−V_S, has degree at most J−1. Its residual is R V_S(Y)/(Y−b); the w reserved roots and r full fibers are disjoint, all lie in D, and give exactly T matches. Zero is not in D. The denominator never vanishes on E.

Both source upper bounds follow by nonzero-polynomial root counting at degree A, even on the restricted domain. Their simultaneous lower bound follows by interpolating the two quotient-variable functions on r−1 allowed tags with degree≤r−2, substituting Y and multiplying by R. This yields exactly A common coordinates. Restricting to D does not break either argument. In particular the source words are both far at T, with exact gap m.

## Asymptotics and comparison

For example choose s=ceil(C log q) with any fixed C>max(64,4/[ρ(1−ρ)]). For all sufficiently large primes conditions 1–3 hold: θ→ρ, and the exponent in condition 3 has leading coefficient Cρ(1−ρ)/2>2 against log q+log s. Also s≤p−1 and the r-range eventually hold. This supplies an entirely explicit eventual quantifier through conditions 1–3.

Here n=Θ(p^(d−1)log p), q=Θ((n/log n)^(d/(d−1))), and log q/log n→d/(d−1). Therefore the normalized capacity margin (T−J)/n=2/s−1/n and exact source-to-near gap (T−A)/n=1/s are both Θ(1/log n). Near-label probability is exactly 1−1/q. The rate is exactly floor(ρn)/n. Characteristic grows as Θ((n/log n)^(1/(d−1))); even at d=2, p/J→0. This does not enter the fixed-rate p>J regime.

KKH Appendix A already supplies the quotient-variable mechanism. Its stated main constructions have prime alphabet and a multiplicative-subgroup evaluation domain; this construction has extension alphabet of fixed degree and a union of norm fibers, generally not a subgroup. Thus one may compare almost-complete label coverage at the same logarithmic order of gap, but should not call this a strengthening within their literal prime-domain hypotheses or claim a new quotient idea. Constants in the gap are conservative and have not been optimized. It also does not retain the earlier additive compiler's exact common agreement J: here CA=J+m−1.

Primary inputs: Katz, *An estimate for character sums*, Theorem 1, https://web.math.princeton.edu/~nmk/old/estcharsums.pdf ; Hoeffding, *Probability inequalities for sums of bounded random variables*, finite-population section/Theorem 4, https://doi.org/10.1080/01621459.1963.10500830 . The character-to-subset step is proved in CAUCHY_SUBSET_PRODUCT_LEMMA.md; quotient comparison uses cached KKH ePrint 2026/782 Appendix A, pp.13–16.
