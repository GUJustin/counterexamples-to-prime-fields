# Two padding orbits: proof audit

This folder strengthens the unique-witness construction. Its two forms
must not be conflated: the splitting-prime form has an efficient decoder,
whereas the logarithmic-length form has a finite existence certificate
and no arbitrary-parameter decoder or polylogarithmic sampler.

## Common geometry

For prime d, use m core orbits a_i mu_d, c single extra coordinates
(0 <= c < d), and padding orbits mu_d and t mu_d. Here
`t^d = q`, `a_i^d = (q^(i+1)-1)/(q^i-1)`,
`n = d(m+2)+c`, and `K = dD-1`.
A locator on D whole orbits is monic of degree K+1 and has zero
coefficient of X^K. Thus subtracting it from a reference locator gives
a codeword of degree below K.

At the two padding orbits, the ratio of its values is `q^(sum I)`.
Selecting one index-sum class makes all its locators fit the same line.
There are at most `D(m-D)+1` classes, so the largest contains at least
`binom(m,D)/(D(m-D)+1)` supports. The padding labels are nonzero.

A nearby codeword requires K+1+2d agreements. The monic difference
from the reference has at most K+1 nonpadding roots. Hence all padding
coordinates must agree, and there must be exactly K+1 nonpadding
roots. Their sum is zero. Root-sum rigidity forces D whole core orbits
and excludes extras; the two padding values force the selected index
sum. Product-label injectivity then proves uniqueness. This classifies
all codewords, rather than merely a constructed bank.

At parameter zero the monic reference has degree K+1, so no degree-<K
codeword has more than K+1 agreements; the zero codeword attains this.
Every nearby parameter has exactly K+1+2d agreements. Thus the far
separation is `2d/n = (2d/(2d+1))*eta`, where `eta=(2d+1)/n`.
The nearby count has logarithm `n H_2(rho)/d + O(log n)`, defeating
`c1*n*2^(c2*H_2(rho)/eta)` for every fixed `c2 < 2+1/d`.

## Integer / splitting-prime form

Write a_i=t+delta_i. Bounds
`t*q^(-i)/(3d) < delta_i <= t*q^(-i)/d`
follow from the difference-of-powers identity, including i=1.
Nonzero cyclotomic subset coefficients have absolute value at least
`d^(-(d-2))`. A nonzero sum of M coefficients has absolute value at
least `(dM)^(-(d-2))`. Choose q and starting index L as stated in
Lemma tou:rigidity. If the coefficients sum nontrivially, the common
leading term dominates all perturbations. Otherwise the first nonzero
perturbation dominates the remaining geometric tail. This proves
rigidity for all independent phases, including singleton extras.

The splitting field has degree at most `(d-1)*d^(M+1)`. Multiplication
by W clears every coordinate denominator, and all conjugates are
bounded in magnitude by W*n*(q+1). Every nonzero cleared difference or
nonpadding subset sum has a nonzero integer norm bounded by B. A
completely split prime p>B cannot annihilate any of them. Existence
uses only infinitude of completely split primes (the already cited
Milne Chebotarev corollary). Arbitrarily chosen finite-field radical
phases are allowed: the characteristic-zero rigidity considered every
phase, not just one compatible choice.

The extra inequality p>q^Smax makes index-sum equality and product
labels lift to integers without wrap. The normalized product of
`(1-q^(-i))` is greater than 1/2, so its bit length gives the sum of
indices when q is a power of two. The existing greedy product decoder
then recovers every support. Dynamic programming finds a largest
index-sum class in polynomial time. Bounds on finding the splitting
prime are deliberately not claimed.

## Function-field / logarithmic-length form

Here i starts at 1 and q varies in F_p. Remove zero and all roots of
Q^i-1 and Q^(i+1)-1. At most U=(M+1)^2 points are removed. Domain
orbits are distinct because R_i(q)=R_j(q) would imply q^(i-j)=1;
none equals zero, 1, or q.

1. Root-admitting parameters. Expand the product of dth-power character
   indicators for Q,R_1,...,R_M. In a nonprincipal term, the largest
   active R_i has a nonmultiple-d valuation at a primitive (i+1)st
   root; all earlier factors are units there. Separability follows
   from p>M+1. A sole Q exponent is detected at zero. Replacing inverse
   character powers by positive powers modulo d gives a polynomial
   with at most U distinct roots and not a constant times a dth power.
   Weil's bound plus removing at most U arguments gives the stated
   lower count Q0. The primary cited formulation is Sárközy–Sárközy,
   Discrete Mathematics 305 (2005), Lemma 2, author-hosted at
   https://web.cs.wpi.edu/~gsarkozy/Cikkek/23.pdf (printed page 267).

2. Nonzero root-sum functions. In F_p((Q^(-1/d))), the normalized
   branch A_i/Q^(1/d) is `1 + Q^(-i)/d + O(Q^(-i-1))`.
   Any constant linear relation is impossible: either its leading
   coefficient is nonzero or the least active index supplies the
   first nonconstant coefficient. This argument survives positive
   characteristic because d is invertible.

3. Polynomial exclusion. Multiply a root sum over all independent
   root rotations. In formal independent variables, invariance forces
   each exponent to be divisible by d. Substitution Y_i^d=R_i(Q) and
   multiplication by W_U^(d^u) therefore yield a polynomial. Every
   factor is nonzero by step 2. Its degree is at most d^u(T+1).
   No algebraic independence of the radicals is assumed.

4. Rotation count. Every proper nonempty subset of mu_d has a rotation
   orbit of size d, since d is prime. There are (2^d-2)/d classes.
   Its coefficient is nonzero: a cyclotomic norm has absolute value
   at most d^(d-1)<p. Distinct subsets can share coefficients; this
   only makes the upper bound more conservative. Empty/full subsets
   give zero. Summing polynomial degrees over nonzero coefficient
   patterns gives `(T+1)*((2^d-1)^M-1)`. Singleton extras are covered
   by the same patterns. Quotienting by rotations is essential for
   this sharper bound; each polynomial already includes all phases.

5. Product labels. Distinct D-support products of (Q^i-1) differ as
   polynomials over every characteristic. Different sums give different
   degrees. Equal sums allow common factors to be canceled; the least
   index in the symmetric difference has coefficient +/-1 at infinity
   and cannot be produced by larger indices. Each collision costs at
   most Smax roots. Excluding Q^h=1 for 1<=h<=D(m-D) makes equality of
   powers equivalent to equality of the two index sums.

6. Probability and complexity. At n=(log_2 p)/8+O(1), root-admitting
   parameters number at least p^(7/8+o(1)); bad parameters number at
   most p^(1/8+o(1)). Their conditional ratio is at most p^(-3/4+o(1)).
   Rejection sampling takes expected d^(M+1)(1+o(1)) trials, which is
   not polynomial in log p. No witness recovery is claimed. Finite
   integer certificates establish existence only, not a particular
   domain or a deterministic sampler.

## Scope

The gap shrinks, the nearby bank is sparse, and no global list-size
upper bound is proved. This is not the complete-coverage construction,
not a fixed-positive-gap superlinear lower bound, and not a construction
on the prescribed better.codes domain. It does not improve better.codes.

## Subsequent refinements

The logarithmic-length theorem permits any alpha below
`d/(log_2(d)+max(log_2(2^d-1),2H_2(rho)))`, rather than just1/8.
The root-admitting main term still dominates the character error, since
`log_2(2^d-1)>log_2(d)`. The conditional failure exponent is exactly
the difference between the main root count and the largest exclusion
exponent. The old1/8 statement remains a uniform special case.

Reducing K from dD-1 to dD-s,1<=s<d, retains every constructed codeword:
its degree is at most dD-d. It cannot introduce new nearby codewords,
and the monic root bound still supplies exact far/near distances.
This gives c2<2+s/d and separation2d/(2d+s), hence any fixed c2<3
with separation>2/3. The integer witness decoder is unchanged.

The variance concentration lemma strengthens the largest sum class.
If J/A is the largest atom of the subset-sum distribution, smoothing
by an independent uniform[-1/2,1/2] gives density bounded by J/A and
variance(V+1)/12. The elementary density/variance inequality yields
J^2(V+1)>=A^2. This is checked against all2,097,110 supports in190
small fixtures, including the sharp D=1 and D=m-1 cases.
