# Complete small-q cyclic exclusion over characteristic zero

The complete autocorrelation-profile census and modular unit-leading certificate apply to arbitrary odd q, not only primes. The cyclotomic integer argument uses primes p congruent1 moduloq and an element of full orderq; the generator explicitly tests every proper divisor ofq. The first/second support sizes(q+1)/2 and(q−1)/2 are both coprime toq, so their translation orbits have full sizeq and rotation normalization remains valid.

New exhaustive support counts:

q | canonical r-subsets | retained C | ordered canonical(C,T) pairs
9 |14|9|12
15|429|82|172
21|16796|408|984

For each compatible ordered pair all h=r+1,...,q−1 were tested. Results:

q | cases | certified excluded
9|48|48
13|252|252
15|1204|1204
17|2576|2576
19|4032|4032
21|9840|9840
23|25696|25696

The already completed q11 exact cyclotomic calculation excludes all120 cases. Thus every odd q from9 through23 is excluded for the degree(q−1)/2 cyclic two-coset mechanism with h>(q−1)/2, over characteristic zero. This covers arbitrary supports, not just difference sets or doubling-invariant supports.

Positive regression guards remain unresolved, as required: all4 q5 cases and precisely2 of12 q7 cases. A modular failure is not itself a positive construction; the q7 survivors agree with the independently verified compact Paley identity.

The generator is modular_general.cpp, the manifest converter is run_modular_general.py, and every case records its source/target IDs, h, prime, full-order root and pass status in modular_q{q}.jsonl. Exact input supports and ID-to-mask mappings are also saved. The conservative characteristic-zero quotient-degree bound is always r−degH; no observed modular source degree is substituted. Independent verification is separately assigned to the audit agent.

Scope excludes only this cyclic two-coset ansatz with the stated degree and high twist. It is not a universal list-size upper bound and does not exclude exceptional positive characteristics, other rates, or noncyclic constructions.
