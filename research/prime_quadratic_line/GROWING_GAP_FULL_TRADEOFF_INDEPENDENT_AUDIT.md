# Independent audit: full growing-gap tradeoff

Auditor: upper_bound_route. Result: PASS, including the endpoint c=1/2.

Reviewed `growing_gap_random_line.tex` on 2026-09-18. No main-manuscript edits were made.

1. **Core.** For an odd prime q∈[L,2L], b_i=2qi+(i² mod q) is an integer Sidon set. Equality of pair sums first forces the index sums equal because the remainder-sum difference has absolute value<2q. Reduction modulo q then forces the unordered pairs equal. Since b_i<8L², p−1>32L² prevents both ordinary and sign-shifted pair-product collisions for a_i=γ^(b_i), and ensures distinct a_i². Thus the bank has exactly L(L−1) distinct core nodes and each incumbent has exactly2L−2 matches.

2. **Parameters and constants.** For any fixed0<c≤1/2, d=floor(c logp/loglogp), L=floor((p^d d!)^(1/(2d+1))), and n=ceil(((2L−2+d)²+1)/2), Stirling and the negligible floor errors give
   log(p/L²)=logp/(2d)−logd+1+o(1),
   p/n~e/(2c)·(logn)^(1/(2c)−1)loglogn.
   Consequently p/L²→∞, including c=1/2, so the explicit Sidon core fits. Also t=L²+O(Ld+d²), L(t/p)^d/d!→1, and μ=t/p→0.

3. **Factorial lower bound.** For fixed k, at most6L coordinates per incumbent are forbidden. Sequential selection of disjoint d-supports has at least (t−6L−kd)_(kd)/(d!)^k choices. Requiring no extra matches to those k incumbents makes these events disjoint; their additional factor is at least(1−k/(p−2L))^(t−kd). Its limit is1 because μ→0. No dμ condition is used. The falling-factorial losses are O_k(dL/t+d²/t+dL/p), all o(1), including the endpoint. The upper bound and hence all fixed factorial moments→1 follow as stated.

4. **Singleton count.** The pointwise fourth-order Bonferroni inequality is valid for all nonnegative integers Y and yields singleton probability≥1/3−o(1), uniformly over canonical labels other than0,1.

5. **Far sources and common agreement.** The p⁴ union bound excludes EVERY nonbank quadratic with L−1 fresh matches, hence bounds every nonbank at every canonical label by A. This stronger cutoff is sufficient for exact endpoint agreement A. The blacklist prevents incumbent fresh matches at labels0,1. The direction g=X³ has at most5 matches to any nonzero quadratic over core plus fresh domain; zero direction restricts common matches to the core. Common agreement is therefore exactly A.

6. **Final line and thresholds.** Passing to endpoints f and f+g maps counted labels bijectively to nonzero parameters. The extra parameter−1 has singleton list{0}. T²<2n holds by definition, and T/sqrt(n)→sqrt2 exceeds the first-order limit sqrt(3/2). At c=1/2 the gap is asymptotic to logn/(2loglogn), and the singleton population is Ω(nloglogn).

Scope: the rate and relative source separation vanish. The result establishes a growing absolute gap and superlinear singleton bad-challenge population, not fixed-rate or fixed-relative-gap tightness. No computation or prime-gap assumption beyond Bertrand's postulate enters this proof.
