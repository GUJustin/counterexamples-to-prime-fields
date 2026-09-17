# Can the Dickson seed give ordinary correlated-agreement failure?

Exploratory, September 17. This does not resolve the n=o(p) target.

The manuscript's anchored padding lemma cannot be applied automatically
to the recovered seed. It uses a received polynomial W of degree exactly
t, so every degree-<k candidate has at most t agreements. After removing
an anchor, the old core has maximum agreement t-1, strictly below the
threshold t reached using a new coordinate. That strict boundary is what
excludes the persistent correlated explanation with zero direction.

For the Dickson seed the natural interpolating received polynomial is

    W(X) = (1+X^(n/2))/2-X^(n/4).

Its degree is n/2, not the exhibited agreement t=3n/8. The degree argument
therefore does not show that 3n/8 is the maximum agreement. Using the old
full-set MCA line and declaring its core one point below the threshold
without such a bound would be invalid.

A small exhaustive interpolation calculation at p=17, n=16, k=4 finds
maximum agreement 6, with 22 maximizing polynomials. The eight Dickson
candidates are among these. This finite observation is not a proof for
growing primes. It now has a preserved guarded replay in
`quotient_scan_results.json`. No large-prime maximum-list assertion is
established.

Potential next step: exploit the multiplicative symmetry. W is invariant
under X -> zeta X for zeta in mu_(n/4). A closest polynomial therefore
comes with its orbit, all at the true maximum agreement. An unbounded
orbit of maximizers would give an unbounded boundary list, even if that
maximum exceeds 3n/8. But small orbits are possible: P=Q(X^(k/r)) with
r dividing k has orbit at most r and degree Q<r. Such candidates reduce
to a degree-<r problem on mu_(4r). Their exclusion is NOT proved.

Further obstacles remain even with a boundary list: the construction
must provide enough distinct candidate values on padding coordinates,
and if the evaluation domain must stay in F_p there are only p base-field
coordinates available. Extension-alphabet label separation alone does
not solve either the characteristic/length ratio or the boundary issue.

## Complete finite quotient census

`quotient_scan.cpp` interpolates on every r-subset of mu_(4r), checking
agreement with W(Y)=(1+Y^(2r))/2-Y^r for degree-<r polynomials. Every
maximizer is counted binom(A,r) times, so dividing the number of
maximizing interpolation subsets by that value gives its exact count.
The trivial bound A>=r ensures no maximizer is missed. Memory does not
grow with the number of interpolation subsets.

At the split auxiliary prime 65521 the complete results are:

| r | maximum agreement | maximizing polynomials |
|---|---:|---:|
| 1 | 1 | 4 |
| 2 | 2 | 28 |
| 3 | 4 | 3 |
| 4 | 4 | 1820 |
| 5 | 5 | 15504 |
| 6 | 8 | 9 |
| 7 | 8 | 70 |

All maxima are strictly below 3r/2. These finite upper bounds also hold
in characteristic zero on the same root-of-unity domains: every
interpolation coefficient lies in the cyclotomic field and its
denominators are products of distinct-node differences. Reduction at a
prime above 65521 preserves those denominators and all agreement
equalities. Thus a characteristic-zero counterexample would specialize
to one found by the exhaustive finite-field census. The converse need
not hold; do not claim that every maximizing finite-field configuration
lifts to characteristic zero.

For each fixed r<=7 this also excludes such excessive agreement in all
sufficiently large characteristics. For any support of size A+1, some
(r+1)-row augmented Vandermonde minor is nonzero in characteristic zero.
Its entries in the first r columns have complex absolute value one,
and its final word entry has absolute value at most two. Hadamard bounds
every conjugate determinant by (r+4)^((r+1)/2). Its nonzero integer norm
is therefore at most (r+4)^((r+1)*phi(4r)/2). Primes larger than this
bound cannot annihilate that minor. This uniform bound covers all
supports, since it does not depend on the support or chosen minor.

Consequently, for sufficiently large p, a maximizer of the full Dickson
word cannot have a multiplicative orbit of size at most seven: its
agreement is at least 3n/8, while each such quotient would force less.
This is only a finite lower bound on orbit size, not an unbounded-orbit
theorem. Extending the strict 3r/2 upper bound to all r is an open step.

Reproduction: compile with an available C++17 compiler at -O2 -UNDEBUG,
outputting `tmp/dickson-quotient-scan`, and run `run_quotient_scan.py`
under the repository resource guard. The recorded build used the local
Zig wrapper targeting aarch64-macos.14.0. No compiler-dependent floating
point arithmetic occurs. The scan also independently reproduces the
p=17 maximum6 / 22-maximizer result.
