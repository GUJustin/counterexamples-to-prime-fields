# Pooled prime-field challenges and a bounded optimization job

Use the quadratic intersection construction with L bank quadratics, N0=L(L−1) core coordinates, t=N0+1 fresh coordinates, n=2N0+1, and threshold T=2L−1. Let P_i=X²/a_i²+a_i² and let p>2a_L². On fresh coordinates use f=X⁴ and g=X³. Write φ_i(x)=(P_i(x)−x⁴)/x³.

## Averaging theorem

Remove the core, zero, and all roots φ_i(x)∈{0,1}. The allowed domain has m≥p−N0−1−8L elements. Within any allowed coordinate its L labels are distinct. For fixed i,j,x the equation φ_j(y)=φ_i(x) is a nonzero quartic, so it has at most four roots. Thus the full allowed domain has at most 2mL² unordered colliding pairs of incidences at different coordinates.

For a uniform t-subset of allowed coordinates, the expected number C of colliding incidence pairs is at most 2L²t(t−1)/(m−1). There are Lt incidences. A label of multiplicity r≥2 consumes r≤2 binomial(r,2) incidences, so at least Lt−2C labels occur exactly once. If m−1≥8Lt, some subset therefore has more than Lt/2 singleton labels.

Each such label has exactly one quadratic at threshold T: its designated bank polynomial has its 2(L−1) core matches and one fresh match. Any nonbank quadratic has at most L core and four fresh matches, strictly below T for L≥6. Other bank polynomials have no fresh match at a singleton label. The common agreement is A=2(L−1), because any nonzero quadratic direction has at most two core zeros and three fresh matches to X³; zero direction attains A through a bank polynomial. Excluding labels 0 and 1 ensures both f and f+g individually have agreement A. Reparametrizing the line gives singleton bad labels z/(1−z), plus the additional singleton word −g at label −1.

Put R=max(2a_L²,N0+8L+2+8Lt). A prime R<p<2R suffices. For sufficiently large L the first term is dominated by the second (a_L=O(L log L)); the latter is ≤9Lt for L≥6. Consequently more than p/36 prime-field challenges are singleton bad labels. This is a constant exceptional probability at vanishing rate and one-coordinate source gap, not a fixed-rate or fixed-gap theorem. The threshold remains below Johnson (T²=2n−1) and above the stated first-order curve for L≥25.

The independent audit is by /root/audit_random_directions. No characteristic-zero lifting or candidate enumeration is needed for this proof.

## Small pilot

`pilot.py` uses only Python standard library and deterministic seed 20260918. It verifies primality by trial division and core preservation. At L=25, p=20011, n=1201, twenty random allowed fresh sets take 0.24 seconds. The best contains 7188 singleton labels among 15025 incidences, with 10625 distinct labels total. Thus at least 35.9% of the field is singleton-bad. The selected 601 coordinates are in `pilot.json`; this is a pilot receipt, not an independently replayed full certificate.

## One substantive computational job

Target: improve singleton exceptional probability beyond the random occupancy benchmark, without changing the curve or source gap. Fix L=363, n=262813, t=131407, M=47,700,741. Choose a prime p near M, above 2a_L². Optimize the t-element allowed fresh subset for the objective number of labels of occupancy exactly one. Success is a verified density ≥0.40 (random occupancy heuristic near 1/e); failure is reported as optimization failure, not a bound.

Search state: a uint32 occupancy array of length p, fresh coordinates, and their L canonical labels. A swap removes one fresh coordinate and inserts another allowed coordinate. Its objective delta is computed exactly from 2L labels. Use randomized proposals, a cooling schedule, and independent restarts; retain only improvements in a best-state checkpoint. Blacklist core/zero and labels 0/1. Modular inverses can be computed once per proposed coordinate; no GPU-specific operation is necessary.

Cost: one initialization needs M evaluations and about 200 MB for occupancies plus ~191 MB to cache selected labels. One million swaps uses ~726 million label updates; benchmark a 10,000-swap C++ pilot before setting a wall-time budget. A proposed rental would use 16–32 CPU workers, 1 GB per independent restart, and ≤1 hour, with exact replay of the winning coordinate set. A GPU-only rental is inappropriate. Stop if the measured cost or first small optimization runs show no meaningful improvement over random sets.

This computation improves an explicit failure-probability constant; it does not improve the list-size exponent, establish fixed-rate tightness, or solve the better.codes benchmark. Since the mathematical constant-probability result is already unconditional, no rental is required to establish it.
