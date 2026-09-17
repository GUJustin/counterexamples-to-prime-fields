# The rigidity proof on arbitrary cyclic domains

September 17, 2026. This strengthens the hypotheses in NEAR_RIGIDITY.md;
its prime-field statement and proof remain valid special cases.

Let F contain all 4kth roots of unity, and suppose its characteristic is
zero or a prime p>8k/3. On mu_(4k), put w=(1+X^(2k))/2. The same six
degree-at-most-k polynomials are the entire list above 5k/3 agreements.
Except in characteristic five, the Dickson word W=(X^k-1)^2/2 has
maximum agreement at most floor(5k/3) for degree-<k polynomials.
Both statements persist over extension coefficient fields.

The proof needs only these properties of the original full prime field:

1. The two zero/one coordinate classes are the roots of X^(2k)+1
   and X^(2k)-1, each with 2k distinct elements. These properties hold
   on mu_(4k) under the stated characteristic assumption.
2. The polynomial abc identity has all degrees at most 2k+2h, where
   h=2k-A<k/3. Thus all degrees are strictly less than 8k/3 and,
   in positive characteristic, less than p. In characteristic zero
   the Wronskian condition is automatic.
3. F contains a square root of -1, supplied by its fourth roots of unity.

The locator identities, primitive-pair cancellation, and abc radical
count are otherwise unchanged. The six classified candidates each have
2k agreements. For the Dickson corollary, a monic classified candidate
would force 4*1^4+1=0, which happens only in characteristic five.

Every prime-field subgroup mu_(4k) satisfies p>=4k+1>8k/3, so this
includes every such short domain, not only p=4k+1. It also includes
the characteristic-zero cyclic word and certain extension-field domains.
It does not apply in arbitrary small characteristic, to arbitrary
puncturings of the cyclic domain, or to different received words.

The main paper now states this more general form. The nearest-source
descent used in the quadratic ordinary-CA construction satisfies these
hypotheses directly, since its prime p is at least 4r+1.
