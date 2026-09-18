# Independent exhaustive set-equality certificate

This certificate is independent of the enumeration logic in `designs.cpp`. Its executable is `independent_design_set.py`; the result and resource report are recorded separately.

The Python implementation processes vertices in increasing order. When it reaches vertex v, all blocks with least vertex less than v have already been chosen. It chooses exactly 3−current_degree(v) further triples whose least vertex is v, allowing repetition and enforcing vertex degree at most3 and pair multiplicity at most2. Choices within that vertex are nondecreasing to remove permutations of identical block multisets. Every three-regular triple multiset has a unique decomposition by the least vertex of its blocks, so this procedure enumerates every permitted half exactly once.

It independently joins the halves using complementary pair multiplicities, obtaining the set of ordered labelled designs. Separately, it reads only the eight published representatives, applies every one of the5040 permutations of the seven candidate labels, and constructs their ordered labelled orbit sets. It asserts all these orbit sets are disjoint and asserts literal equality between their union and the independently enumerated design set. The test does not merely compare cardinalities and does not quotient by swapping T and C.

The script also records individual orbit sizes and a SHA256 digest of the canonical serialized full ordered-pair set. Completion of this certificate validates the eight-case combinatorial reduction; it does not certify the separate polynomial-realizability arguments for those cases.
