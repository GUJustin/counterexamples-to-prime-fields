# Boundary locator lists on cyclic domains of arbitrary order

September 17, 2026. Proposed extension of the existing prime-power
boundary theorem; proof under local audit, no novelty claim.

## Characteristic-zero bound

Let n>=2, 1<=K<A<=n, s=A-K, and use the domain mu_n in characteristic
zero. Let the received polynomial W have degree at most A. If deg W<A,
there is at most one polynomial of degree<K with at least A agreements.
Otherwise scale W to be monic. Each difference W-P is exactly the monic
locator of an A-subset, and all these locators have the same first s
non-leading coefficients. Their first s power sums therefore agree.

For two supports, let delta in{-1,0,1}^n be their incidence difference.
The Fourier coefficients at0,1,...,s vanish. Since delta has rational
coefficients, each zero propagates to its Galois orbit. The orbit of
frequency j contains gcd(j,n), so every frequency whose gcd with n is
at most s vanishes.

The only possible surviving characters have orders q dividing n with
q<n/s. Define

    M(n,s)=sum_{q|n, q<n/s} phi(q),
    Q(n,s)=lcm{q:q|n, q<n/s}.

There are M-1 surviving nonconstant characters, and the constant Fourier
coefficient is also zero by equal support size. Thus the affine space of
all real incidence vectors in one moment class has dimension at most M-1.
An affine d-dimensional subspace has at most2^d vertices of the Boolean
cube: some d coordinate functionals give an injective projection on it.
Consequently the complete decoding list has size at most

    2^{M(n,s)-1}.

Also every incidence difference is Q-periodic. Q divides n and is at most
lcm(1,...,ceil(n/s)-1). This is only a necessary periodicity constraint in
general; unlike the prime-power case, arbitrary swaps of full cosets need
not preserve the moments.

For fixed eta=s/n>0, M<=sum_{q<1/eta}phi(q), independently of n.
In particular log_2 L <= B(B+1)/2-1 for B=ceil(1/eta)-1. Thus the list is
constant in n at every fixed gap, for arbitrary cyclic order, not just
prime powers. This is a restricted boundary-word theorem, not a bound for
arbitrary received words.

## Transfer to sufficiently large split prime fields

For every divisor d of n with d<=s, write N=n/d and

    R(N)=#{1<=u<=floor(s/d): gcd(u,N)=1},
    E(n,s)=max_{d|n,d<=s} phi(n/d)/R(n/d).

Every R is positive because u1 qualifies. If p=1 modulo n is prime and
p>n^{E(n,s)}, the same characteristic-zero moment relations hold for
any pair of finite-field supports with matching first s moments.

Indeed evaluate their integer difference mask at a primitive Nth root.
If it is nonzero in characteristic zero, its nonzero integer norm has
absolute value at most n^{phi(N)}. Since p splits completely and the R
indices u give distinct primitive Nth roots modulo p at which the mask
vanishes, at least R distinct primes above p divide it. Its norm is
therefore divisible by p^R, contradicting the size bound. Each orbit with
d<=s vanishes in characteristic zero. Applying this to every pair of
supports places the whole finite-field list inside one characteristic-zero
moment class, so the bound2^{M-1} applies even when W has arbitrary F_p
coefficients and no chosen integer lift.

## A uniform polynomial threshold at a fixed gap

An elementary bound is E(n,s)<=125/eta^3, eta=s/n. For N>1,
Mobius inversion gives

    R(N)=sum_{e|N} mu(e) floor(eta*N/e)
        >=eta*phi(N)-2^{omega(N)-1}.

There are2^{omega(N)-1} positive Mobius terms; the negative terms only
increase the lower estimate. The product inequalities

    phi(N) >= [2/6^{2/3}] N^{2/3},
    2^{omega(N)} <= [16/210^{1/3}] N^{1/3}

follow by isolating the primes2,3 in the first product and2,3,5,7 in the
second. For all other primes the respective factors are at least one or
at most one, and higher prime powers improve the inequalities. Hence

    2^{omega(N)-1}/phi(N) < (9/4) N^{-1/3}.

If N>=(5/eta)^3, then R(N)>=(eta/2)phi(N), so phi/R<=2/eta.
Otherwise phi/R<=phi(N)<=N<125/eta^3. This proves the claimed threshold.

Therefore p>n^{125/eta^3}, p=1 mod n, suffices uniformly in n. In
particular every superpolynomial-prime sequence eventually meets the
threshold at each separately fixed eta. Changing the number or pattern
of prime factors of n cannot rescue a growing fixed-gap boundary-locator
list along such a sequence.

## Limits

- The received word must be represented by a polynomial of degree<=A.
  General words or locators with variable cofactors are not covered.
- The evaluation domain is a multiplicative subgroup (or a nonzero scaled
  coset), not an arbitrary chosen prime-field domain.
- The fixed-gap list is bounded here; this alone does not bound the number
  of nearby points on an arbitrary received line.
- The field threshold is sufficient and very large, not a practical
  better.codes certificate or a claim for every p>n.
- The general-order class bound is an upper bound, not the exact
  prime-power class description or a claim that every Boolean vector in
  the Fourier subspace occurs in the chosen decoding list.
