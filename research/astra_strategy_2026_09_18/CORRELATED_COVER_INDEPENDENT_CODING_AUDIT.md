# Independent coding audit: correlated-cover construction

Reviewed `strategy_breakthrough_finish_finish.answer.md`. Verdict: **PASS** for the coding, probability, threshold, and common-agreement arguments. The prime-selection step is a standard application of Bombieri–Vinogradov and is separately assigned to the arithmetic auditor; its required modulus range and main/error scales are consistent as detailed below. No manuscript edits.

## Geometry and nonbank union

The condition2s|(p−1) makes the subgroup H of s-th powers have even order, hence−1∈H. Its size>32L² permits the stated integer-Sidon exponent bank and all core/fresh fibers. The degree-2s bank has exactly A=2s(L−1) core matches per incumbent. At each core coordinate exactly two incumbents meet. Thus a nonbank polynomial of degree≤2s has at mostsL core matches, by summing at most2s roots of each of its L nonzero differences from the bank.

A nonbank exceeding A requires at leasts(L−2)+1 fresh coordinate matches, hence at leastL−1 distinct fresh fibers. On each fiber the random value must belong to a set of size≤s, so its probability is at mosts/(p−2L). Values at distinct fibers are independent. There are at mostp^(2s+2) polynomial/label pairs, giving exactly the stated union bound. When p~L³ and s≤L/100 its logarithm is at most(6s−L+o(L))logL, tending to−infinity. Partial matches within a fiber do not create a loophole: each fiber has onlys coordinates.

## Singleton and endpoint assertions

For fixed label outside0,1, desired incumbent values are distinct at every fresh base node. Each incumbent is forbidden at at most6(L−1) nodes by two nonzero cubic equations per other incumbent. Therefore the total bank–fiber hit count is a sum of independent Bernoulli variables with mean1+o(1) and maximum summand probabilityO(L^−2). The standard elementary product formula gives probability of exactly one hit e^−1+o(1), uniformly in the label. Exactly one hit means one incumbent gains exactlys matches, reaches T, and all other incumbents remain at A. On the uniform nonbank-good event all other codewords have at most A agreements. Hence the high list is singleton and the nearest agreement is exactly T.

The endpoint blacklist gives no incumbent fresh matches at labels0 or1; uniform nonbank exclusion then makes both endpoint agreements exactly A. For common agreement, a nonzero direction polynomial of degree≤2s matches g at at most2s core coordinates and3s fresh coordinates because fresh g=x^(3s). Since5s<A eventually, no such direction attains A; zero direction confines simultaneous matches to the core, where a bank polynomial attains A. The common agreement after the invertible endpoint change from(f,g) to(f,f+g) remains A.

## Thresholds and explicit finite DKT support

n=s(2L²−2L+1), k=2s+1, T=s(2L−1), d=s. Exactly
(k−1)n−T²=s²>0.
The Johnson shortfall is asymptotic tos/(4L), so it is Θ(1) when s=Θ(L), and tends to zero for s=Θ(L^b),0<b<1. The normalized threshold is above the first-order curve: k/n~1/L², T/n~1/L, and a_1(rho)~sqrt(rho/2), giving ratio sqrt2.

There is also a direct finite first-order interpolation certificate, avoiding hidden low-rate constants. Use m=4, derivative cap2, message degree D=2s, B=4L−2=2T/s, and challenge cap48B. The exact source count is
G=3sB²−(s−1)(3B−2).
The local degree layers have total rank23; the required specialization cutoffs hold for L≥14. For every s≥1 and L≥14,
G/n≥(48L²−60L+20)/(2L²−2L+1)>47/2.
Thus the same strict graded row inequality as in the earlier certificate holds. Reconstruction requires only p>max(2s,2), which the construction satisfies. This certifies finite first-order admissibility, not a matching exceptional-count upper bound.

## General scaling and prime selection

For any fixed0<b≤1, choose s=Θ(L^b), with the constant sufficiently small at b=1. Bombieri–Vinogradov can be applied to moduli2s in an interval of sizeΘ(X^(b/3)), contained well inside its level-of-distribution range. The sum of reciprocal totients over that interval is bounded below by a positive constant using phi(2s)≤2s; the main count is Ω(X/logX), whereas the total error is o(X/logX). It therefore supplies infinitely many pairs with p~L³ and2s|(p−1). For b<1, the nonbank logarithm is
[6s−(2−b)L+o(L)]logL,
which is negative with a growing margin.

Writing gamma=b/(b+2), the resulting scales are
n=Θ(L^(2+b)), d=Θ(n^gamma),
M=Θ(L³)=Θ(n^(3/(2+b)))=Θ(n^(3(1−gamma)/2)).
Thus0<gamma≤1/3, and M is superlinear when gamma<1/3. At gamma=1/3, p and n have the same order. The normalized gap d/n~1/(2L²) and rate k/n~1/L² are inherited through the cover: neither becomes fixed positive. This is an absolute-scale improvement, not an escape from the normalized-rate/gap limitation.

## Restricted conic-bank comparison

The covered bank is still H0+theta U+theta^−1V, with H0=0,U=1,V=x^(2s), and actual common agreement A. The audited conic-bank theorem gives
#bank-witnessed bad labels≤2n(n−1)/[(T−k+1)d]~4L³.
The construction supplies(1/e−o(1))L³ labels, so it attains this restricted bank bound's order. In the positive-density realization p~L³, the ambient field cap is also Θ(L³); this should be acknowledged if discussing tightness.

One may instead select much larger primes congruent1 mod2s. When p≫L³ and L>2s+4, the same union bound (even after multiplication by p) decreases with p, while the expected total number of isolated bank–fiber hits over all labels is(1−o(1))Lt=Θ(L³). This gives the same restricted-order comparison with an ambient field much larger than the bank bound, but loses positive density. This optional extension requires a separate prime-selection statement and should not be silently conflated with the p~L³ theorem.

## Algebraic fresh-value remark

If fresh values are h(y) for a fixed monic polynomial of degreeD0>3, then for every nonbank Q the fresh residual h(x^s)+lambda x^(3s)−Q(x) is monic degreeD0 s. Hence its total agreement is at mostsL+D0 s<A wheneverL>D0+2. Nonbank exclusion is then deterministic. The limited-independence and endpoint-repair arguments still need to be supplied for selecting h; they are not automatic from the degree bound. This substitution does not improve the scaling exponents, since subgroup capacity still requires s=O(L) when p~L³.
