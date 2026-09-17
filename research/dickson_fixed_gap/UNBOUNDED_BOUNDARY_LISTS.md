# Growing lists at the true nearest-codeword radius

September 17, 2026. New deduction from the recovered seed and the exact
two-orbit certificate. Proof-reviewed locally; not a novelty claim and
not yet a manuscript theorem. The domain remains of length comparable
to the characteristic. No short-domain or line counterexample is claimed.

## Statement

For every integer R>=2 there are arbitrarily large primes p and a
received word on F_p^*, for the exact-rate-1/4 RS code, such that its
list of nearest codewords has more than R members. The maximum agreement
is at least 3(p-1)/8. Thus these are boundary lists, not merely lists at
a radius for which closer codewords might exist.

There is also a three-coset version: on a union of three cosets of
H=mu_((p-1)/4), of length N=3(p-1)/4, the exact-rate-1/3 RS code has
a received word with more than R nearest codewords, and maximum
agreement at least ceil(5(p-1)/16)=ceil(5N/12). Its gap above rate is
at least 1/12. One unused H-coset remains inside F_p^*.

## Proof

Let M_R be the product of odd primes at most R. By the Chinese remainder
theorem and Dirichlet's theorem, there are arbitrarily large primes with

    p = 9 mod 16,     p = -1 mod M_R.

The residue class is coprime to 16 M_R. Put k=(p-1)/4. Then v_2(k)=1,
and no odd prime <=R divides k. Consequently every divisor of k at
most R is either one or two. Take p>17 throughout.

Use the recovered word W(X)=(1+X^(2k))/2-X^k on mu_(4k)=F_p^*.
Its values on the four H-cosets are 0,2,-i,i, all distinct when p>17.
The word and any union of its H-cosets are invariant under X -> zeta X
for zeta in H. This action preserves the RS code and every agreement
count. Therefore the orbit of any nearest polynomial consists entirely
of nearest polynomials.

If such an orbit had at most R members, its size, a divisor of k, would
be one or two. Orbit size one forces a constant polynomial because the
degree is <k. Orbit size two forces

    P(X)=a+b X^(k/2).

Indeed its stabilizer has order k/2, so every nonzero monomial exponent
is a multiple of k/2. On the full domain, Y=X^(k/2) has image mu_8,
with fibers of size k/2; the received word descends to

    w_2(Y)=(1+Y^4)/2-Y^2.

No affine polynomial agrees with this word at three distinct points of
mu_8 when p>17. This is certified exactly by verify_two_orbit.py:
all 56 augmented 3-by-3 Vandermonde determinants are nonzero in
Z[zeta_8], and their integer norms have prime divisors only
2,3,5,7,17. The word column is doubled so all entries are algebraic
integers. Reduction in any characteristic p>17 preserves nonvanishing,
and distinct nodes remain distinct. This also proves the assertion over
any extension alphabet, since an affine polynomial agreeing at two
base-field nodes has base-field coefficients.

Thus an orbit of size at most R can supply at most k agreements on the
full domain or on any three H-cosets. But the Dickson seed has agreement
3k/2 on the full domain, strictly exceeding k. A nearest polynomial
cannot have such a small orbit. Its orbit alone gives more than R
nearest codewords, proving the first assertion.

For the three-coset version, sum the agreements of all 2k Dickson
polynomials. Each has 3k/2 total agreements and k/2 square-coordinate
agreements. The two square H-cosets therefore have total incidence k^2
between them. Delete one whose total incidence is at most k^2/2.
On the remaining three cosets the average agreement per seed polynomial
is at least

    3k/2 - (k^2/2)/(2k) = 5k/4.

Hence the true maximum is at least ceil(5k/4)>k. The same orbit argument
gives more than R nearest polynomials. The dimension is k, length 3k,
and asserted agreement and rate follow.

## What this buys and what remains

This resolves the unbounded-boundary-list step of the full-length
symmetry route along a chosen sequence of primes. It bypasses a general
quotient bound for all r by excluding small odd orbit divisors in the
choice of characteristic. The additional r=3,...,9 census is not needed
for this proof.

It does NOT show n=o(p): the two domain lengths are p-1 and 3(p-1)/4.
It does not yet convert the boundary lists into superlinear numbers of
ordinary correlated-agreement failures. Even with an unused base-field
coset, one must control candidate-value diversity on padding points and
retain the required agreement threshold after any anchor removal.
No growth rate in n or p for the boundary list is asserted beyond its
being unbounded along the chosen sequence. The actual maximum agreement
need not be a fixed fraction; the lower bound is fixed.

## Independent finite boundary example

The complete interpolation census at p=41, k=10 on the three cosets
obtained by deleting mu_10 finds maximum agreement 14, with exactly
20 maximizing polynomials. It checks all binom(30,10)=30,045,015
determining subsets; the candidate count divides the number of
maximizing subsets by binom(14,10). This agrees with, and strengthens
for this instance, the guaranteed agreement ceil(5k/4)=13. The scan
is recorded in three_coset_scan.log and its resource report. It is an
illustration of the theorem, not the proof of the infinite family.

After choosing an anchor agreed by a positive fraction of the boundary
list, dividing (P-P(anchor))/(X-anchor) gives a boundary list of degree
<k-1 with maximum agreement exactly one smaller on the punctured old
domain. This follows directly from maximality: any closer new witness
would lift to a closer old witness after restoring the anchor. Hence
the received-polynomial degree obstruction in BOUNDARY_TRANSFER.md is
resolved for these true boundary lists. The remaining ordinary-CA
padding issue is candidate-value diversity at unused base-field points,
not the lack of a boundary certificate. No superlinear claim follows yet.

## Exact ordinary correlated-agreement line fixture

`verify_boundary_line.py` takes the 20 nearest p=41 polynomials from the
complete census. Ten agree with the word at anchor 2. Dividing their
differences from the anchor value by X-2 gives degree-at-most-8
polynomials on the remaining 29 seed coordinates, each with exactly
13 agreements. No degree-at-most-8 polynomial can have 14 old agreements:
restoring the anchor would contradict the certified old maximum14.
This upper bound holds over extension alphabets as well, since enough
base-field interpolation values force base-field coefficients.

At the five unused points 23,37,1,4,10 these candidates take respectively
10,10,9,9,9 distinct values. Give the direction word value zero on the
old core and one on these five new points. Use intercept theta*x at
the new points, where theta is outside F_41. The labels v-theta*x are
distinct across points and distinct candidate values, giving 47 labels.
Every selected witness has its 13 core agreements and exactly one new
agreement: threshold14 on a length34, dimension9 code.

There is no correlated agreement at threshold14. A nonzero explaining
direction polynomial has at most8 core zeros and can use only5 new
coordinates, for at most13 common agreements. A zero explaining
direction is confined to the old core, where the boundary argument also
limits agreement to13. Thus this is ordinary/subset CA failure, not just
full-set MCA failure. The associated selected-witness concurrency is at
most n-A+1=21. All 47 labels and witnesses are explicitly checked.

Limitation: the radius20/34 is NOT below the characteristic-based Elias
radius at rate9/34 over characteristic41. The verifier checks the entropy
inequality using integers. This fixture validates the transfer mechanism
and exceeds the literal coefficient-one count n, but does not supply a
new below-Elias whitepaper counterexample or an asymptotic superlinear
family. It remains a research note.
