# Independent audit: all q127 doubling-invariant complementary profiles

**PASS: all35,028 characteristic-zero exclusion certificates.**

This audit does not reuse the generator's polynomial coefficients,
remainders, overlap factors, degree witnesses, or Euclidean calculations.
It reconstructs them from the original support sets and the recorded
prime/root/twist. The mathematical transfer lemma is proved separately
in `MODULAR_EXCLUSION_AUDIT.md`.

## Precisely excluded family

Let q=127, r=63, and work in characteristic zero with a primitive qth
root zeta. Let C,T be r-element subsets of Z/q, each invariant under
multiplication by2, and let S=(Z/q)\C. Assume their autocorrelations obey

    |C intersect(C+t)| + |T intersect(T+t)| = 62  (t != 0).

For each h=64,...,126, let P be the unique degree-at-most63 polynomial
with P(zeta^s)=zeta^(hs) for s in S. There are no nonzero alpha with
alpha^127!=1 and no scalar c, over any algebraic extension, such that

    P(alpha*zeta^t)=c*zeta^(ht)  for every t in T.

Independent translations of C and T are also covered by rotation of the
first orbit and rescaling the second orbit parameter. No c!=0 assumption
is needed for this exclusion. For h<=63, P=X^h and the purported cyclic
candidate bank collapses to one polynomial.

This therefore excludes the saturated cyclic two-orbit bank with both
small support/complement patterns doubling-invariant (up to translation)
at q127. It includes every cyclic difference-set pair, by the separate
multiplier theorem. It does **not** exclude arbitrary non-doubling-
invariant supports, noncyclic banks, other q, or all positive
characteristics. The finite exact computation also implies an exclusion
outside a finite set of characteristics, but no explicit exceptional
prime set is computed here.

## Coverage independently checked

The original `cyclic_half_agreement/doubling_profiles127.json` supplies
38 source unit classes and556 relative compatible target pairs. The
preparer expands target orbit masks with that file's own orbit ordering,
checks source S is literally the complement of C, and directly recomputes
all126 nonzero-offset intersection sums for each pair. It independently
forms the expected556*63=35,028 keys (source class,relative target,h).
The certificate file contains exactly that coverage, with no missing or
uncertified key.

The80 difference-set supports occupy only six of these source classes;
the additional32 classes and76 representative pairs are included.
No inference of completeness is drawn merely from testing the six
Singer/Paley-style families.

## Independent arithmetic checks

`verify_modular.cpp` reconstructs each distinct support polynomial from
its linear factors over the recorded finite field. It verifies:

1. q and p are prime and zeta has exact order q;
2. every source/target node exponent is distinct and has the correct size;
3. all monic remainders X^j modulo source and target support polynomials;
4. the pivot v_k is nonzero, and all elimination polynomials
   E_j=v_k R_j−v_j R_k are recomputed coefficient-by-coefficient;
5. the overlap shifts are exactly those with T+t subset S, found directly
   from the actual supports; H is the product of their linear factors;
6. monic division by H has zero remainder for every E_j;
7. some quotient attains the conservative degree bound63−deg H;
8. the quotients generate1 modulo p.

For item8, this verifier uses extended Euclid and checks the polynomial
Bezout identity at **every** update, rather than trusting an unverified
gcd return value. The generator's stored arithmetic is never an input.
All35,028 certificates pass. The independent q7 regression certifies h4
and h6 exclusions but correctly retains the known positive h5 scaling
parameter after removing its overlapping-orbit factor.

The modular DVR lemma now proves the stated characteristic-zero
exclusion: a monic nonconstant common divisor of the integral quotient
polynomials would reduce to a nonconstant common divisor modulo the
recorded prime. The verified full-degree equation prevents loss of such
a divisor at infinity.

## Reproducibility and saved records

* `prepare_modular_verification.py`: independently reconstructs supports,
  checks correlations and coverage, and writes flat verifier input.
* `verify_modular.cpp`: independent finite-field verifier with explicit
  extended-Euclid identity checks; compile with C++17, assertions enabled.
* `modular127_verify.in.summary.json`:194 domains,556 pairs,35,028 rows,
  no missing cases and no uncertified cases.
* `modular127_verify.out`: one independent result per certificate, including
  degree witness, conservative bound, final gcd degree, and overlap degree.
* `modular127_prepare.resources.json` and
  `modular127_verify.resources.json`: both watchdog runs completed
  successfully under384MiB/60s, in0.56s and1.10s respectively.
* `modular_q7_smoke.in/out/resources.json`: positive-regression safeguard.

The source certificate file is
`cyclic_half_agreement/modular_profiles.jsonl`; its two primes are509
and2287. The old partial q127 characteristic-zero CAS checkpoints are
preserved as historical regressions, but are no longer needed to settle
this tested support family.
