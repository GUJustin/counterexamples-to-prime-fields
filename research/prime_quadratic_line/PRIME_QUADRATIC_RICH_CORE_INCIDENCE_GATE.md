# Prime-field quadratic rich cores: incidence-theorem gate

2026-09-18. Bounded primary-source audit. No new construction or exhaustive literature claim.

## Question and budget

Let D⊂F_p have n distinct coordinates, let f:D→F_p, and let L distinct polynomials of degree≤2 each agree with f at at least A=c√n coordinates, with c around1.3. This is precisely incidence counting for the n-point graph P={(x,f(x)):x∈D} and quadratic graphs.

For a fixed bank used on a line f+λg with common-agreement bound A and target A+d, every successful bank witness needs at least d matches on coordinates where g≠0: its matches on g=0 already give common explanations (Q,0) and hence number at most A. Each witness/coordinate with g≠0 determines one λ. Consequently

    B d ≤ L n.

Thus d=Θ(√n) and L=O(√n) force B=O(n). Superlinear B in this framework needs a super-√n rich bank. This is a fixed-bank budget, not a bound on all line counterexamples. It does not imply that the bank is rich on a common zero-direction core: the bank may gain its agreement on label-dependent nonzero-direction blocks.

## Applicable prime-field primary theorem

Mohammadi–Pham–Warren, *A point-conic incidence bound and applications over F_p*, European Journal of Combinatorics107(2023),103596, Theorem1.3:

    I(P,C) ≪ n^(15/19)L^(15/19)+n^(23/19)L^(4/19)+L,

for quadratic graphs y=ax²+bx+c, provided n≪p^(15/13). The p≡3mod4 restriction in that theorem concerns circles, not parabolas. Our n≤p satisfies the size hypothesis asymptotically. The theorem permits arbitrary P, so graph domains qualify; Cartesian-product improvements require additional structure and do not apply automatically.

Primary links: [published paper](https://doi.org/10.1016/j.ejc.2022.103596), [authors' preprint, Theorem1.3 and its proof](https://arxiv.org/html/2111.04072v2).

## Consequence, calculated here

Insert I≥AL and absorb the linear term for A→∞. The first incidence term gives

    L ≪ n^(15/4)/A^(19/4),

and the second gives L≪n^(23/15)/A^(19/15). With A=c√n these are respectively O_c(n^(11/8)) and O_c(n^(9/10)). Therefore

    L=O_c(n^(11/8)).

This is substantially weaker than O(√n). The desired range √n≪L≪n^(11/8) is not excluded. It is stronger than the elementary interpolation bound L≤binom(n,3)/binom(A,3)=O_c(n^(3/2)). Degree≤1 polynomials can be separated: their pairwise overlap is at most1, so for c>1 their count is at most n(A−1)/(A²−n)=O_c(√n), and does not change the exponent.

Combining the incidence upper bound with the fixed-bank budget yields B=O(n^(15/8)) only under the ADDITIONAL assumption that all bank polynomials have Ω(√n) matches to ONE common core graph on at most n coordinates, and d=Ω(√n). This is a conditional ceiling for that rich-core/fresh-match architecture, not for every fixed-bank model. It leaves superlinear populations possible and does not give an actual bank achieving them. For any fixed smaller positive core constant c, the nonlinear-quadratic exponent remains11/8. Degree≤1 witnesses then require a separate bound: triple-free pair interpolation gives at most binom(n,2)/binom(A,2)=O_c(n) distinct lines, sufficient to preserve the combined11/8 exponent. The sharper O(√n) line bound above specifically requires c>1.

## Why the real-plane obstruction does not transfer

The real three-degrees-of-freedom bound of Pach–Sharir gives I≪n^(3/5)L^(4/5)+n+L for quadratic graphs; inserting I≥c√nL yields L=O_c(√n). Its hypotheses are over the real plane. The checked finite-field theorem above is different, even for prime fields and p polynomial in n. A modular incidence pattern need not admit a simultaneous real lift. The fact that each individual polynomial has three coefficients does not provide such a lift.

Primary: [Pach–Sharir, On the Number of Incidences Between Points and Curves (1998)](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/on-the-number-of-incidences-between-points-and-curves/D82C6E430EE5402A3FE18C724A0C14B1).

## The newer polynomial-incidence SVD estimate does not close this window

Tamo, *Points-Polynomials Incidence Theorem with an Application to Reed–Solomon Codes*, Theorem1.2, bounds degree<k incidences over F_p by

    |I−nL/p| ≤ sqrt(nL[p+(k−1)L](1−1/p)).

At k=3 this implies

    A ≤ n/p + sqrt(n[p/L+2](1−1/p)).

For n≤p the limiting square-root term approaches √(2n) as L grows; it is already larger than1.3√n. Thus this result imposes no relevant upper bound on L at the requested constant. This is a direct specialization, not a claim that the paper's coding results are weaker in their intended regime.

Primary: [Tamo, arXiv2312.12962, Theorem1.2](https://arxiv.org/html/2312.12962v1).

Likewise the exact pair-count/Johnson inequality only gives a positive upper bound when A²>2n:

    L ≤ n(A−2)/(A²−2n).

It cannot be used with c=1.3<√2. If a proposed route accidentally raises the *core* agreement above √(2n), it returns immediately to the O(√n) bank regime.

## Concrete next-step target and scope

One particularly strong unresolved target is a graph on n≤p prime-field coordinates with A=c√n for some √(3/2)<c<√2 and L/√n→∞ distinct quadratic graphs. This is sufficient for certain constructions, NOT necessary for a constant source-to-threshold loss. A weaker and potentially more accessible target has core agreement a=c√N for any fixed small c>0 on a core of at most total length N. In the two-ray example the bank core agreement is only2t, whereas the eventual endpoint/common agreement is14t; the fresh blocks supply the difference. A larger bank with only gap-scale common core agreement could therefore be enough. The inspected incidence exponent leaves this lower-core-agreement route open as well. A prospective construction must keep distinct x coordinates and exhibit one common graph value at every coordinate; a Cartesian point set, a subfield plane over an extension, or a multivalued arrangement is not yet such a core.

For an exact regular core model, if every core node belongs to r bank witnesses and every witness has A core matches, then LA=nr. Thus super-√n L forces growing r. Pair overlap≤2 gives n r(r−1)≤2L(L−1), consistent with c<√2. This is a sharply stated combinatorial target, not a classification or existence theorem. Existing real-lifted pair/constant-ray banks have bounded richness and cannot supply it merely by increasing their sizes. No credible prime-field high-richness construction was established in this bounded audit; a specific modular incidence family is needed before a computation is justified.
