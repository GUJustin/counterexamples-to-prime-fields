# Bounded primary-source priority check (2026-09-17)

Scope: the particular full-length prime-field Dickson bank, its agreement transition at 3/8 and rate approaching 1/4, and the matching reciprocal-square list dependence above that transition. This is a search record, not a proof of novelty.

## Exact relevant contemporary attribution

Joshua Brakensiek, Yeyuan Chen, Aaron Putterman, Zihan Zhang, and Kai Zhe Zheng, *Algorithmic List Decoding of Reed–Solomon Codes up to Capacity*, arXiv:2609.08005 (2026): [primary PDF](https://arxiv.org/pdf/2609.08005), [metadata](https://arxiv.org/abs/2609.08005).

The PDF's Corollary 5.1 (printed page 22) assumes a prime q >= C(R,delta)n and gives arbitrary-evaluation-set decoding to agreement (R+delta)n, with runtime and list size q^{O_{R,delta}(1)}. This allows polynomial lists. It does not establish a constant list bound, and its field-size hypothesis does not automatically include the full-length quarter-rate bank. The formal q-based bound should be preferred to the introduction's n-based shorthand when q is unrestricted.

Section 3 develops interpolation using hidden Hasse derivatives, backward Taylor constraints, and local-kernel rank savings; root finding uses Kopparty's multiplicity-code machinery. These techniques require explicit attribution. Theorem 4.1 distinguishes runtime exponent O(epsilon^{-12/theta}) from list exponent O(epsilon^{-3/theta}); the following informal-theorem proof uses a weaker list exponent. No Dickson occurrence was found in the searchable HTML. This check verifies statements and method descriptions, not the complete proof.

## Dickson-specific closest primary hit

Matt Keti and Daqing Wan, *Deep Holes in Reed-Solomon Codes Based on Dickson Polynomials*, arXiv:1507.01653: [primary manuscript](https://arxiv.org/html/1507.01653v4).

Their Theorem 12 concerns a Reed–Solomon code whose evaluation set is the **value set** of a Dickson polynomial. It gives sufficient conditions under which a received polynomial of degree k+1 is not a deep hole. This is a different role for Dickson polynomials from a parameterized bank of candidate codewords on the full multiplicative prime-field domain. The inspected theorem does not give our 3/8 transition or the matching reciprocal-square bank-list estimates.

Also inspected the primary author manuscript [Limits to List Decoding Reed–Solomon Codes](https://www.cs.cmu.edu/~venkatg/pubs/papers/rs-limits.pdf). Its subfield/extension-field and low-rate constructions did not yield an exact match in this bounded inspection; no Dickson occurrence was found. This is not an exhaustive theorem-by-theorem priority audit of that literature.

## Search limitations and safe presentation

Queries combined “Dickson”, “Reed–Solomon”, “list size/list decoding”, “prime”, “majority”, “3/8”, and “3n/8”. Primary manuscripts were preferred; search-result snippets, blogs, aggregators, and permutation-polynomial applications were not treated as evidence of an exact prior theorem. A frequent false match is 3/8 as the **unique-decoding error radius** of a rate-1/4 code, rather than the agreement threshold studied here.

No exact prior theorem matching all of the bank, full-length prime-field domain, 3/8 agreement transition, and matching epsilon^{-2} upper/lower dependence was identified in this bounded search. That statement is weaker than a novelty claim. The square-root majority gain and correlation/tensorization tools are classical ingredients; novelty, if claimed after further checking, should attach to their precise Dickson-bank realization and sharp transition, not to those general tools. The new polynomial field-size condition p >= 2^36 L^2 is an internal theorem under audit, not a fact established by the external sources above.
