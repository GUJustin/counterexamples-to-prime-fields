# Independent full zero-chart closure: gap at most two epsilon

The root's proposed circular-path extension is valid and admits the sharper constant 2 instead of 3. Retain the factorization, fixed nonzero label-independent leading coefficients, pairwise coprime inner lengths, and reduced common-H realization from `WRAPPED_CRT_RECTANGLE_BARRIER.md`. Zero constant coefficients are now allowed without restriction. Set epsilon=max_i h_i/n_i and rho=D/N.

**Claim.** If the bank has two different factor vectors, every candidate's actual agreement fraction with H satisfies a<=rho+2epsilon.

Fix a first tuple s, and let ell_j be the smallest exponent with nonzero coefficient in its factor f_(j,s_j). Put delta_j=(h_j-ell_j)/n_j. Since the evaluation roots are nonzero, its inner root count is at most h_j-ell_j. Therefore the actual OR agreement fraction a satisfies a<=sum_j delta_j and a<=1. Every delta_j is between zero and epsilon.

Suppose a>rho+2epsilon, and compare s to any other tuple t in the degree-D bank. Fix coordinate i. In every other coordinate choose initially exponent ell_j, and form the base phase theta=sum_(j!=i) ell_j/n_j modulo one. Successively change each of these exponents from ell_j to h_j, in any fixed order. The prefix phases trace a nondecreasing real lift with increments delta_j<=epsilon and total length

    sum_(j!=i) delta_j >= a-delta_i >= a-epsilon > rho+epsilon.

The open allowed arc is (rho,1-h_i/n_i). Its length is greater than epsilon, since rho<1-2epsilon and h_i/n_i<=epsilon. Its closed complementary arc has length rho+h_i/n_i<=rho+epsilon.

**Circular-path lemma.** A sequence of nondecreasing lifted points with successive increments at most epsilon cannot avoid an open circle arc of length greater than epsilon while traveling farther than the length of its complement. Indeed the inverse image of the complementary closed arc is a disjoint union of closed intervals, separated by open intervals longer than epsilon. No step can pass from one closed component to the next. All sampled points would therefore lie in one component, bounding the total travel by its length. This includes endpoints, zero increments, and arbitrary initial phase.

Consequently some prefix phase u belongs to the allowed arc. Fix its corresponding other-coordinate exponents, each either ell_j or h_j. Every such anchor coefficient is nonzero in the first tuple. Let the i-th exponent range through every integer from 0 to h_i. The normalized residue positions u+e_i/n_i all lie strictly between rho and 1, without wrapping. CRT injectivity ensures these coefficients receive no other monomial contributions.

The pair's product coefficients must agree at these high positions, because their common H cancels and both reduced outputs have degree at most D. At e_i=h_i, the first coefficient is a nonzero anchor product times the shared nonzero leading coefficient. Equality forces the second anchor product to be nonzero and equal to the first. Equality of the other line coefficients identifies f_(i,s_i)=f_(i,t_i), including any zero entries. Repeat for every i to identify the entire factor vectors, a contradiction.

Thus the zero-constant chart is fully closed for this explicit realization. No valuation stripping, change of common received word, or assumption that minimum exponents agree between tuples is needed. The anchor exponents are chosen solely from the first tuple; equality at the high leading coordinate certifies the second tuple's anchors after the fact.

The proof establishes the actual agreement bound because the received word is H and the discrepancy is exactly the product. It does not exclude arbitrary univariate realizations of OR incidence patterns or another received word. It also does not address factors whose leading coefficients vary across labels without an appropriate additional normalization argument.
