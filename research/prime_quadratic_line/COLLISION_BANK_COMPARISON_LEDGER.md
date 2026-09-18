# Controlled-collision bank: comparison ledger

September 18, 2026. The construction passed two independent proof audits. This ledger derives its parameter comparisons, not historical priority.

For two disjoint complete bipartite graphs K(t,t), let L=2t^2 and A=3t^2+2t-3. Each bank has A core matches, and the core has LA/2 coordinates. With M=floor(L/8), d=floor(M/(64H)), T=A+d and n=floor(T^2/2)+1, the prime-field construction has dimension three and both source agreements and ordinary common agreement A. Here t=Theta(H/log H).

The field is chosen in (4096 LHM,8192 LHM), subject to p=1 mod4. Unlike the earlier C4-free construction, p is chosen to dominate cross-label collisions directly. Since LHM=Theta(H^5/(log H)^4), eventually p>H^4, as required by the integer unique-factorization argument. Existence of primes in this fixed progression over that interval is asymptotic; this is not a practical onset bound.

## Metrics that must stay separate

* Rate: R=3/n.
* Threshold decoding radius: delta=1-T/n.
* Distance below the capacity radius: eta=(1-R)-delta=(T-3)/n=Theta(n^(-1/2)).
* Source decoding radius: 1-A/n.
* Proximity loss: epsilon=(T-A)/n=d/n=Theta(n^(-3/4)/log n).
* Loss relative to the capacity margin: epsilon/eta=d/(T-3)=Theta(n^(-1/4)/log n), tending to zero.
* Prime size: p=Theta(n^(5/4) log n).
* Guaranteed singleton exceptional labels: B>=LHM/32-1>=p/2^18-1, a positive constant fraction asymptotically.

Thus the construction improves the earlier grid's loss n^(-5/6)/log n and turns its vanishing exceptional fraction into a constant fraction, at the cost of reducing the absolute count exponent from 4/3 to 5/4. It does not make the loss comparable to the distance below capacity, provide fixed rate, or improve the benchmark.

Eliminating n gives B=Omega(epsilon^(-5/3)/(log(1/epsilon))^(2/3)). This is a coupled-parameter lower-bound curve only: rate, threshold, and prime size all vary. It does not establish an optimal exponent in a universal proximity-gap theorem.

## Why the change can help

Strictly unique pair products were stronger than needed. Each product has two evaluation roots. If exactly two bank pairs have the same product, each pair can use one root, provided its source value is assigned separately. Disjoint complete bipartite components make the lost matches exactly regular across banks. This permits Theta((H/log H)^2) bank polynomials rather than Theta((H/log H)^(3/2)), while keeping A>L so nonbank quadratics remain excluded. This exact regularity is essential: uncontrolled fluctuations in source agreements could exceed the intended gap d.

The improvement does not remove the integer-slope limitation: d/A remains of order 1/H. A claim of a constant loss-to-capacity-margin ratio would still be false.

## Matched comparison with the inspected prior mechanisms

The bounded source audit TRANSLATED_GRID_MATCHED_PRIOR_COMPARISON.md applies with the following updated exponents. At p=Theta(n^(5/4) log n), T~sqrt(2n), the elementary ambient-mass union bound is

    Pr[agr_3(U)>=T] <= p^3 (e*n/(T*p))^T
                       = exp(-(3/4+o(1))*T*log n).

Even multiplication by p tends to zero. This prevents that ambient-mass certificate from producing the desired number of nearby line points at the matched parameters; it does not exclude structured constructions.

The Crites--Stewart all-label entropy hypothesis would require k at least (3/5+o(1))*T, before its additional nonnegative term, rather than k=3. This follows from log(n/T)/log p tending to 2/5. The strict KKH dimension-three quotient specialization still forces bounded target agreement for r>=3 and only O(n) canonical supports in the enlarged r=2 case.

The repository's iid construction already has a constant exceptional fraction, so that feature alone is not new. Its guaranteed separation is logarithmic, rather than the present polynomial d. The existing growing-dimension full-fiber cover at the new d gives count of order (n/d)^(3/2)=n^(9/8)(log n)^(3/2), whereas the bank gives n^(5/4)log n at dimension three. This compares those constructions only.

As before p=o(n^2), so an O(n^2) exceptional-count upper bound is vacuous for this family. A constant exceptional fraction does not establish tightness of that bound.
