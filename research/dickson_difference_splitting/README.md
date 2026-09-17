# Pairwise splitting probe for the Dickson bank

September 17, 2026. Finite evidence only; a general proof remains open in
this investigation. This is not a prime-field tightness result.

For p=1 mod8, k=(p-1)/4, the source polynomials are

    P_a(X)=sum_{j=0}^{k-1} binom(2k+1,2j+1) a^(2k-2j) X^j,
    1 <= a <= (p-1)/2.

We factored every pairwise difference at p=17,41,73,89,97. All 2,922
nonzero differences split into linear factors over F_p; every observed
root multiplicity is one or two. Each factorization was multiplied back
and checked against the original polynomial. The degree of each difference
is k-1. Exact totals and multiplicity counts are in probe.json.

This is stronger finite evidence than checking just the selected anchored
subfamily. It does not prove splitting for other primes.

## Why the pattern could help

If all differences in a source bank split over F_p, then evaluation at
ANY point of F_(p^2) outside F_p separates the entire bank. The same is
true for anchored quotients: their pairwise differences are the original
differences divided by the common linear anchor factor.

Consequently, if the observed splitting property holds at a prime p,
choose any N+1 distinct padding points outside F_p, where N=p-1. For an
anchored subfamily of size ell, every padding value set has exactly ell
members. Independent uniform translations give a union of expected size

    p^2 * (1 - (1 - ell/p^2)^(N+1)).

An anchor with ell >= A*L/N = 3N/16 exists for the full Dickson bank.
The existing full-support MCA root-count argument then applies without
any collision loss. If a general splitting theorem is established, this
would asymptotically improve the quadratic coefficient at output length
n=2N from 3/100 to (1-exp(-3/16))/4, approximately 0.04274.
This would improve a constant, not the exponent or the field-class scope.

The proof obligation is substantial: establish the splitting property for
all p=1 mod8 and all distinct a,b modulo sign. Neither a finite census nor
the expectation calculation discharges it. No manuscript claim has been
changed on the basis of this probe.
