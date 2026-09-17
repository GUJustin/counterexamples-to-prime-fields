# Exact boundary-list classes on prime-power subgroups in characteristic zero

September 17, 2026. Search constraint, not a new finite-field upper bound
at practical parameters or a novelty claim.

Let n be a power of a prime ell, 1<=K<A<=n, and s=A-K. On the domain mu_n in
characteristic zero, consider degree-<K polynomials agreeing with a
received polynomial W of degree at most A at A or more coordinates.
If deg W<A, root counting gives at most one candidate. Otherwise scale
W to be monic. Each candidate difference W-P is the locator of an
A-subset, and these subsets have matching power sums of orders 1,...,s.

Let q be the largest power of ell STRICTLY less than n/s, and put h=n/q.
Then h>s. Partition mu_n into its q cosets of mu_h. Every moment class
is described exactly as follows:

* Every partly occupied coset is frozen, including its individual roots.
* Among the remaining cosets, a fixed number b are occupied completely;
  their identities can vary arbitrarily.

If r cosets are partly occupied, the class therefore has exactly
binom(q-r,b) subsets. In particular every displayed list has size at
most binom(q,floor(q/2)) <= 2^(q-1) < 2^(n/s) for q>=2. For q=1 the
list bound is one. This is a reciprocal-gap exponential bound in this
restricted characteristic-zero setting.

## Proof by rational Fourier support

For two A-subsets, let delta in {-1,0,1}^n be the difference of their
incidence vectors, indexed by powers of a primitive n-th root zeta.
Its Fourier coefficients at j=1,...,s vanish, and its coefficient at
j=0 vanishes because the subsets have the same cardinality.

Since delta has rational coefficients, applying every Galois automorphism
zeta -> zeta^u (gcd(u,n)=1) propagates each zero to its full orbit. For a
nonzero frequency j, the least positive member of its orbit is gcd(j,n).
Thus all frequencies with gcd(j,n)<=s vanish. Since n is a prime power,
the only surviving frequencies are multiples of h, where h is
the smallest power of ell exceeding s. Equivalently delta is q-periodic.

On each index class modulo q, delta is therefore constant. On a mixed
0/1 class of the first subset, the only constant change preserving 0/1
entries is zero. Full and empty classes may be swapped; equality of
cardinality fixes the number of full classes. Conversely every such
swap preserves the first s moments, because a full mu_h coset has zero
power sums of orders 1,...,s<h. This proves the exact class description.
Newton identities identify power-sum classes with leading locator
coefficient classes, and hence with the entire decoding list of W.

## Polynomial field-size transfer

The crude norm bound can be sharpened substantially by counting how
many conjugate factors vanish modulo p. Assume p=1 modulo n. For each
power d of ell with d<=s, put N=n/d and

    R_d=floor(s/d)-floor(s/(ell*d)),
    E(n,s)=max_{d<=s, d a power of ell} phi(n/d)/R_d.

Then the ENTIRE class description above holds whenever p>n^{E(n,s)}.
In particular E(n,s)<=2n/s, so p>n^{2/eta}, eta=s/n, suffices.
This is a bound for received polynomials of degree at most A only.

To prove transfer, take the integer difference mask delta of two
subsets having the same first s moments modulo p. If delta(zeta_N)
is nonzero in characteristic zero, its nonzero integer norm has
absolute value at most n^{phi(N)}. But p splits completely, and the
R_d distinct unit indices u with d*u<=s give R_d distinct conjugate
factors vanishing modulo p. Consequently p^{R_d} divides that norm.
For p>n^{phi(N)/R_d}, this is impossible. Thus the full orbit vanishes
in characteristic zero for every such d, giving the same periodicity
and exact class description. Equivalently, the divisibility follows
by lifting the distinct primitive roots to Z_p and taking their product.

For the simple bound, let M=floor(s/d)>=1. Then
R_d=M-floor(M/ell)>=(1-1/ell)M, while phi(n/d)=(1-1/ell)n/d.
Hence phi(n/d)/R_d<=n/(d*M)<=2n/s.

## Limits of the transfer

For fixed n, the statement transfers to all sufficiently large split
primes, but NOT automatically to every p>n. A crude sufficient condition
is p>n^phi(n), in addition to p=1 modulo n. Indeed a nonzero difference
of subset power sums is an algebraic integer in Q(zeta_n), each of its
conjugates has absolute value at most n, and its nonzero norm has
absolute value at most n^phi(n). Such a prime cannot turn it into zero.
One may instead exclude the finite set of prime divisors of all relevant
nonzero norms. Scaling the domain by a nonzero scalar does not change
the argument.

The polynomial threshold above improves this crude norm threshold,
but can still be enormous. The result does not give an
upper bound for better.codes, nor a uniform bound for all growing
short-domain prime-field families. Exceptional finite-characteristic
moment collisions remain a possible route; a characteristic-zero
root-of-unity boundary-list construction cannot evade the stated
periodicity constraint.

The exact checker retains its original power-two filename, but also
checks orders 9 and 25. At n=16,A=8, the characteristic-zero maximum
list sizes for s=1,...,7 are 70,6,6,2,2,2,2. Finite-characteristic
maxima at s=1 are 758,198,120 for p=17,97,113, respectively, exceeding
the characteristic-zero bound70. These are demonstrations of the need
for the transfer qualification, not below-Elias counterexamples.
