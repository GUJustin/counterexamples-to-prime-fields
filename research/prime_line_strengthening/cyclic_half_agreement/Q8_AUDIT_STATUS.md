# Four-orbit cyclic eight-word search: audit status

The proposed family has eight twisted cyclic translates of one polynomial of degree at most7, on four disjoint nonzero μ8 cosets, with at least16 matches on32 coordinates per candidate. This is a scoped family, not arbitrary RS words.

Pair counting forces exactly four matches per orbit. Opposite candidate pairs have at most six nonzero intersections, using the entire four-unit deficit from the naive pair budget. Hence the sum of support autocorrelations is7 at differences1,2,3 and6 at difference4. Exhaustive support enumeration leaves four classes up to independent rotations, permutations and cyclotomic Galois action. Each has one skew support and one antipodal pair in each remaining support. Twists0,3,4,7 are impossible from endpoint-coefficient cancellation; reversal reduces the remaining twists to1,2.

Normalize the skew support to{1,z,z²,z³}, z⁴=−1. Writing P=E(X²)+XB(X²), the appropriate parity cubic is monic with roots a²,b²,c², the three antipodal pair coordinates. The other parity component is determined by interpolation on the first support. The six remaining selected-node equations are recorded in q8_exact.py and the metadata files. Admissibility requires abc(a⁸−1)(b⁸−1)(c⁸−1) times the three pairwise eighth-power differences to be nonzero.

Root independently reconstructed all eight systems using rational arithmetic in Q[z]/(z⁴+1), checked the initial four zeros, and verified every removed factor divides the admissibility guard. It also independently checked exact ideal-membership identities for cases0 and2, twist1, proving a=0 and excluding those two systems. The verifier is verify_q8_certificate.py; receipts are under q8_exact_certificates/.

Sage Groebner calculations return no admissible solution for all eight systems. However independent identity certificates for the other six systems are NOT yet complete: bounded lifting attempts timed out. Consequently this note records a complete algebraic computation and a partial independent certificate audit, not a fully independently certified universal exclusion. No larger positive list was found.

Finite-prime searches at p41 and twelve further primes73 through337 were exhaustive for their stated normalized families and found no hits. These scans alone do not imply characteristic-zero nonexistence.
