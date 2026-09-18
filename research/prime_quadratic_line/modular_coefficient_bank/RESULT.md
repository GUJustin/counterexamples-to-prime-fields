# One modular coefficient-bank capacity gate

September 18, 2026. One fixed prime, no prime enlargement or asymptotic exclusion. The exact C++ gate verifies p=4801 is prime, verifies a primitive generator 7, and uses 4096 distinct coefficient points in each bank:

1. additive box {0,...,15}³;
2. multiplicative box H16³;
3. modular paraboloid {(u,v,uv):u,v in H64}.

For every x in F_p, it computes the largest bucket B_x of a*x²+b*x+c. The sum of the largest n=4096 such buckets is the exact maximal TOTAL bank incidence achievable by any choice of n distinct coordinates and received values. It does not assert that this maximizing word distributes incidences evenly across candidates.

| Bank | Capacity | Average per coordinate/candidate | Average / sqrt(n) | Maximum bucket |
|---|---:|---:|---:|---:|
| Additive box | 14322 | 3.49658 | 0.05463 | 256 |
| Multiplicative box | 22765 | 5.55786 | 0.08684 | 256 |
| Modular paraboloid | 32187 | 7.85815 | 0.12278 | 127 |

The descending-rank buckets at ranks 1,16,64,256,1024,2048,4096 are respectively:

- additive: 256,16,8,5,4,3,2;
- multiplicative: 256,45,16,16,5,4,3;
- paraboloid: 127,127,127,8,6,6,5.

The complete histograms over all 4801 coordinates are retained in `gate.json`; `summary.json` adds ranks and ratios and checks histogram cardinality and the reported top-n sum. The code is `gate.cpp`; runtime was 0.078 seconds internally, with the OS receipt in `resources.txt`.

For these EXACT banks, no word/domain can give all 4096 candidates even agreement 4,6,8, respectively. In particular they fail the specified sqrt(n)-scale regular-bank target, and also fail uniform agreement 32 in this finite fixture. This does not exclude a smaller selected bank, another box aspect ratio, another field, another received-line construction, or a weaker core followed by fresh padding. Being below the unpadded DKT scale is not itself a padding obstruction.

The paraboloid's conspicuous buckets have a direct explanation: evaluation factors as

    u*x²+v*x+uv = (u+x)(v+x²)−x³.

For x in H64, the value −x³ gives the union u=−x or v=−x², of size 127. But this mechanism supplies only 64 rich coordinates, not 4096. Thus its large maximum is not a growing regular-incidence mechanism at this size. No new viable formula was found, and this isolated gate does not justify enlarging the prime or launching a bank search.
