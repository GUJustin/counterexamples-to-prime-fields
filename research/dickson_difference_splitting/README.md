# Pairwise splitting of Dickson differences

September 17, 2026. The observed splitting pattern is now proved for all
primes p=1 mod4 in [PROOF.md](PROOF.md). No novelty claim is made.
This strengthens the extension-field quadratic MCA constant; it is not
a prime-field tightness result.

For k=(p-1)/4 the source candidates are

    P_a(X)=sum_{j=0}^{k-1} binom(2k+1,2j+1) a^(2k-2j) X^j,
    1 <= a <= (p-1)/2.

Every root of P_a-P_b belongs to F_p when a^2!=b^2. The proof writes
X=t^2 and uses 2e=p+1 for e=(p+1)/2. Equality of the two polynomial
values forces t^p=t or t^p=-t, and either condition puts X in F_p.
The argument takes place in an algebraic closure, so it accounts for
all roots rather than only roots in one extension field.

Anchored quotients inherit the splitting property. Thus their evaluations
are pairwise distinct at every point outside F_p. With ell anchored
candidates and p padding points, independent translations have expected
union size p^2[1-(1-ell/p^2)^p]. This yields at least ceil(n^2/20)
full-support exceptional challenges over F_(p^2), at rate1/8 and gap1/16.
The sharper uniform coefficient is (1-exp(-1/4))/4, about0.05530.
Neither the exponent nor the ambient-field class changes.

## Independent finite checks

`probe.py` factors every pairwise difference at p=17,41,73,89,97:
2,922 differences in total. Every factorization was multiplied back
and checked against the original polynomial, and all factors were linear.
All observed multiplicities are one or two; the proof does not require
or assert a general multiplicity classification.

The separate stdlib verifier
`../prime_field_tightness/check_quadratic_extension_lower_bound.py`
checks pairwise separation at ALL points outside F_p in F_(p^2) for
the anchored banks at p17 and p41, then constructs and checks the full
exceptional-label witnesses. It certifies63 and370 labels respectively,
exceeding the new uniform bounds52 and320. Its occupancy targets are
computed exactly with rational arithmetic.
