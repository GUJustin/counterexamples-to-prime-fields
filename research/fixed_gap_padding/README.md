# Fixed-gap correlated-agreement failure

This package supports Lemma 4.5 and Theorem 4.6 in the September 16, 2026
manuscript. The anchored quotient removes one common agreement point;
padding then gives many nearby challenges with no correlated agreement.
The rate and positive capacity gap stay exactly fixed as length grows.

The coefficient of the resulting linear count has logarithm at least
(H_2(rho)^2/2-o(1))/(eta^2 log_2(1/eta)) along a sequence of gaps.
A concrete family at rate 31/81 and gap 1/27 has more than 3.76e17*n
nearby challenges. Its prime field grows with length.

## Verification

Run from the repository root:

```sh
python3 research/fixed_gap_padding/verify_anchored_padding.py
```

The standard-library checker constructs six full finite-field fixtures
at lengths 10, 20, 40 and 11, 22, 44. It checks the anchored quotient,
exact agreement counts, disjoint challenge labels, and the global degree
bound against every possible pair of common witnesses. It also scans all
field challenges for the exhibited candidates and checks that their full
agreement supports have no degree-bounded direction witness. Seventy
small anchored moment counts, 378 integer affine transforms, and the two
concrete coefficient calculations pass.

`PROOF.md` gives the proof and quantifiers. `anchored_padding_verification.json`
contains the domains, received lines, candidates, labels, and exact results.
Resource reports record sequential execution under a 384 MiB watchdog.

The finite fixtures supplement the written proof; they do not prove
splitting-prime infinitude or the asymptotic moment estimate. The proof
has been self-reviewed, with no independent review or novelty claim.
This result does not establish quadratic growth at one fixed positive
gap, a prescribed-alphabet counterexample, or an improved better.codes score.
