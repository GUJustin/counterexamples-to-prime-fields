# All doubling-invariant complementary profiles at q=127

We exhaust all 48620 subsets C of F127 of size63 invariant under multiplication by2. Such C cannot contain0, because each nonzero doubling orbit has size7. With primitive root3, the18 orbits are {3^j 2^k:0<=k<7}, indexed j=0,...,17. Each C is a union of9 of them.

For cyclic two-coset candidates of degree63, first support S=F127\C and second support T of size63, pair-root saturation requires lambda_C(d)+lambda_T(d)=62 for every d!=0. For doubling-invariant sets lambda is constant on the nine orbits of <−1,2>; representatives used here are1,3,5,7,9,11,13,19,21. All profiles are computed exactly by127-bit rotation and intersection popcount, and hash-joined against62 minus the profile.

Results:
-48620 supports,23326 distinct profiles;
-656 supports have at least one compatible doubling-invariant partner;
-7768 ordered compatible(C,T) pairs;
-38 classes under unit multiplication, including the6 difference-set classes and32 further classes.

Unit multiplication is cyclic rotation of the18 orbit indices, so classification is exhaustive without expensive general isomorphism testing. The JSON stores every representative C, its first support S, and every compatible T orbit mask. CSV first-support files are in doubling127_supports/class0.support throughclass37.support.

Independent verifier uses ordinary sets and direct intersection counts, checks all126 nonzero differences for each of556 representative pairs, and confirms the unit orbits expand to exactly656 retained supports. This validates the positive compatibility data; exhaustive absence of other retained supports follows from the original48620-case loop.

Scope: this is an exact combinatorial necessary-condition census, not a polynomial-existence theorem. It includes all doubling-invariant C and T, but does not assert arbitrary cyclic constructions have doubling-invariant supports. A finite-field or characteristic-zero interpolation/gcd test remains necessary for each retained family.
