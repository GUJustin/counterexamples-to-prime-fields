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
growing primes and will need a preserved guarded replay before use as a
certificate. No large-prime maximum-list assertion is established.

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
