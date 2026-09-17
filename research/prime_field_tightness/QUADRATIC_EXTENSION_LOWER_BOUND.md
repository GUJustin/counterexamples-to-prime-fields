# A quadratic fixed-gap MCA lower bound in growing prime characteristic

September 17, 2026. A direct corollary of the already established Dickson
list and anchored averaging compiler. No novelty claim. The ambient field
is a quadratic extension, NOT a prime field.

For every prime p=1 mod 8, p>=17, put N=p-1 and n=2N. There is a
Reed--Solomon code over F_(p^2), with n distinct evaluation points and
dimension k=n/8, and a received affine line with at least

    ceil(n^2/20)

full agreement-set MCA exceptional labels at agreement A=3n/16.
The capacity gap is exactly 1/16, the rate is exactly 1/8, and the
characteristic satisfies p=n/2+1>k-1. In particular, the capacity counting
theorem of ePrint2026/2056 applies for sufficiently large n. The conclusion
is full-support MCA failure; absence of ordinary correlated agreement and
existence of a far point are not asserted.

## Original compiler proof (weaker constant)

The full-length Dickson construction on F_p^* gives L=N/2 distinct
degree-<k polynomials agreeing at A=3N/8 positions with one word, for
k=N/4. These identities and distinctness remain true on passing to
F_(p^2). Additional nearby polynomials in the larger field cause no
problem: the compiler only needs a selected list, not completeness.

The exact-halving compiler in PRIME_BOUNDARY_AMPLIFICATION.md works over
any finite field of cardinality Q>=2N+1. Its proof uses only the root
bound for distinct polynomials, counting unused evaluation points, and
uniform independent translations of subsets of the additive group of the
field. Replace its p by Q throughout. It gives length 2N, dimension k,
agreement A, and at least

    ceil(Q A L/(Q+3 A L))

full-support exceptional labels. Here Q=p^2=(N+1)^2, A L=3N^2/16,
and A>=k+1. Since Q>=N^2,

    Q A L/(Q+3 A L)
      =3Q N^2/(16Q+9N^2) >=3N^2/25=3n^2/100.

The parameter identities and characteristic guard follow immediately.
There are infinitely many such primes, so this is an unbounded-length
family, not a single finite witness. The standard infinitude of primes
1 mod 8 also follows elementarily from prime divisors of X^4+1.

## Improved proof via pairwise splitting

The general proof in `../dickson_difference_splitting/PROOF.md` shows that
all pairwise Dickson differences split over F_p. Anchored quotient values
are consequently distinct at every point of F_(p^2) outside F_p. With
ell=N/4 candidates at any nonsquare anchor and p=N+1 padding coordinates, random
translations have expected union size exactly p^2[1-(1-ell/p^2)^p].
This is at least N^2(1-exp(-1/4))>N^2/5=n^2/20. Thus the current
manuscript uses ceil(n^2/20); the older bound above remains valid.

## What this says about tightness

This gives an intrinsic exponent-two lower bound for the capacity MCA
problem in the full large-characteristic field class of the current
paper. It rules out a universal linear-in-length capacity MCA bound in
that class, even at one fixed positive gap. It complements the intrinsic
linear list lower bound over the prime fields themselves at rate1/4,
agreement3/8, gap1/8.

It does NOT match the paper's capacity exponent, establish an exponent
that grows as the gap shrinks, or prove tightness of its first-order
quadratic bound: the output agreement3/16 is below the first-order
threshold at rate1/8. It also does NOT resolve the target of superlinear
exceptions over prime fields. Indeed that target cannot follow merely
by restricting these challenges to F_p: there are only p=n/2+1 such
labels, and the new evaluation points need not lie in F_p.

The distinction is material. A claim of "no intrinsic superlinear
fixed-gap examples" must specify prime ambient fields; it would be false
for the growing-prime-characteristic extension-field setting above.

## Verification

`check_quadratic_extension_lower_bound.py` independently implements
quadratic finite-field arithmetic and replays the source lists, anchor,
padding, and exceptional witnesses at p17 and p41. The quantified proof
above is by the established compiler; finite replay is corroboration.
