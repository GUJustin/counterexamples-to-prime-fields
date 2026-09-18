# Bounded high-rate restricted-pair search

2026-09-18. **No hit for primes at most5000.** This is a finite census, not an asymptotic obstruction. The C++ source is `search.cpp`; exact counts are `result.txt` / `result.json`. A measured repeat used0.06 seconds and1.97MB peak RSS, well below the authorized60-second/512MB budget.

For every odd prime p≤5000, every divisor L of p−1 with m=(p−1)/L≥2 was considered. Put s=L−1. Filters were:

- s(s−1)≥2(p−1), the necessary restricted-pair counting condition;
- 2s²<7p, the proposed s²/p<7/2 window;
- 7m>2s, the prospective high-rate first-order-crossing scale.

There are315 admissible shapes. For each, H is the order-L subgroup and b runs through one representative of every nonidentity H-coset. The full-H factors are b−a, a∈H. All products of TWO DISTINCT factors are explicitly counted, with no character estimate. This tests8602 cosets. None covers F_p*.

This full-H prefilter is exhaustive for the requested domain family: if b is multiplied by h∈H, the full factor set scales by h and pair products by h², preserving coverage. Deleting a reserved tag can only remove products, never fill a hole. Hence no reserved-tag variant for any b in these cosets can succeed. The implementation would test every reserved tag after a full-H pass, but there were zero such passes.

The closest case is p31,L10,m3,b3. Independent Python field multiplication confirms the three missing full-H products16,17,25. Since there is no coverage hit, no qualifying RS construction exists in this search and no first-order polynomial sign is asserted for a hit.

The root's proposed larger regime or other populations remain untested. No automatic scale-up is authorized or inferred from this result.

## Authorized extension through65537

`search_extended.cpp` repeats the same exhaustive gate through prime65537. It completed in32.29 seconds (31.42 CPU), with2.95MB peak RSS, before the54-second watchdog cutoff. There were3396 admissible shapes and340732 nontrivial subgroup cosets; again ZERO full-H covers, so ZERO reserve-deleted covers. The smallest absolute deficit remains the independently checked p31,L10,b3 example, with missing products16,17,25 and s²/p=81/31≈2.613. This census does not establish a uniform missing-product character pattern. No250000 extension was performed: the authorized next-size condition of completion within10 seconds was not met.

A separate scope limitation is important even if a future cover is found. The prospective crossing needs m/s>2/7, and all-pair coverage requires M≤binom(s,2). Therefore n=(s+1)m>(2/7)s(s+1)>(4/7)M, so the challenge field has p<(7/4)n+1. All-label coverage would then be only O(n) exceptions, not a near-quadratic lower bound against DKT's exceptional-count bound. A successful instance would be an interesting high-rate threshold example, not the sought superlinear count-tightness breakthrough.
