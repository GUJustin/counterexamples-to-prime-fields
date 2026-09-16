# Counterexamples to List and Line Decodability Bounds over Prime Fields

Working draft by Justin Thaler, September 16, 2026.

[Read the paper](paper.pdf) · [LaTeX source](paper.tex) · [ZK disclosure summary](reports/stwo-zk-disclosure-summary.pdf)

The paper studies quantitative coding statements used in security analyses
of hash-based SNARKs. It proves general list and affine-line separations
over prime fields, gives finite circle-code examples, and treats the S-two
analysis as an application of those results.

## Results

- Exponential lists on integer-interval domains rule out a uniform
  `exp(O(1/eta))` list bound at every fixed rate, with a shrinking gap and
  radii below the characteristic-based Elias bound. Optimizing length rules
  out every bound with logarithm `o(eta^-2/log(1/eta))`. For every sufficiently
  large prime, with `b=log2(p)`, the list has at least
  `2^((1/2-o(1))*b^2/log2(b))` codewords below Elias.
- An anchored lift and padding construction gives genuine failure of
  correlated agreement at an exactly fixed positive rate and gap, for
  arbitrarily large lengths. The necessary coefficient of a linear
  exceptional-count bound has logarithm of order
  `eta^-2/log(1/eta)` along a sequence of gaps. A concrete family has more
  than `3.76e17*n` nearby challenges. The prime field grows with length.
- A code can have maximum list size exactly `n-k-1` and nevertheless
  have `binom(n,k+1)` uniquely nearby points on an affine line without
  correlated agreement. A puncturing bound shows that this parameter
  count is optimal at the one-coordinate-gap endpoint.
- Suitable generic domains have an exact list profile at every integer
  radius below the redundancy. The profile persists under field extension
  and finite interleaving measured by column distance. At fixed positive
  rates, the profile follows from published results of Brakensiek, Gopi,
  and Makam and of Roth; the paper supplies an explicit lower construction.
- The puncturing argument also bounds nearby witness pairs whose entire
  agreement sets have no joint explanation, including lines that possess
  some correlated agreement. For degree-`e` polynomial curves, the same
  argument gives a factor of `e`, using the known curve proximity theorem.
  An attributed extension of Jo's incidence argument improves the interior
  bound. The curve endpoint `e*binom(n,k+1)` is attained over suitable fields.
- Exact enumeration certifies **5,552,914,238,035** codewords in
  the length-64, dimension-32 interval example, improving the prior
  polynomial-weight certificate by **5.05%**. A general concentration
  bound improves full-range counting by a factor of order `n^(m/2)`
  for each fixed number `m` of canceled coefficients. Classical Gram coordinates give explicit variances;
  unit-cube smoothing yields a stronger finite concentration constant,
  and the finite-population central limit theorem gives a Gaussian
  constant for the largest class when `m` is fixed and both the subset
  size and its complement grow. A separately verified radial method
  certifies 5,133,798,314,667 without fixing the first moment.

- Over the M31 prime, the interval example with `n=157, k=63, t=68` has
  at least **28,169,451,256,663,519,418** codewords, exceeding the stated
  finite list prescription by more than **2^34.09967**. The corresponding
  quartic-extension line exceeds its finite prescription by **2^50.90955**.
- A line entirely over the M31 prime at `n=82, k=9, t=12` has at least
  **138,752,510** nearby labels. Exact incidences and a next-coefficient
  collision saving strengthen the count.
- The quadratic-circle bank at the existing compact eighth-rate parameters
  increases from **285,003,988,493,147,037** to **365,153,907,657,996,934**.
  A separate native low-rate example gives more than **24.5949 excess bits**.
- A full-fiber classification now removes the Galois assumption for rational
  maps when `p = ell*n +/- 1`, `ell >= 6`, and `n > 6*(B-1)`.
  At the pinned better.codes parameters, every possible degree through
  32768 reduces to a power or twisted-inversion quotient. This concerns
  complete fibers of one fixed map; it does not improve the numerical score.

- A sharp bound limits affine binary support families in every
  characteristic other than two: fixing `s` leading locator coefficients
  forces dimension at most `floor(min(t,n-t)/(s+1))`. A trace family over
  `F_16` violates this bound, identifying a specific barrier to direct
  binary-to-prime transfer.

[New finite-certificate proofs and replay instructions](research/overnight_2026-09-16/README.md).

The statements retain their field, domain, radius, and quantifier
restrictions. They do not establish a complete protocol attack or an
improved better.codes submission.

## Supplementary research notes

[Linear differential constraints and full-support proximity gaps](research/linear_differential_mca/README.md)
gives an elementary `O(n)` bound at fixed positive gap for candidates
satisfying a challenge-dependent linear system of bounded challenge degree
and bounded generic kernel dimension. It covers differential equations
of any fixed order that are affine-linear in the jets, in large
characteristic. General nonlinear first-order constraints remain open here.
The note includes a proof and exact finite checks; it is separate from the
main manuscript and makes no literature-priority claim.

[A linear spectral bound for a nonlinear Riccati family](research/spectral_riccati/README.md)
proves that `R P' - R' P + P^2 - z B P = 0`, with R monic, has at most `D-b-1`
nonzero labels with nonzero degree-D solutions when `deg R=D+1`,
`deg B=b`, and `D>(b+1)(b+2)`, in characteristic greater than `D+1`.
This closes a particular nonlinear construction route. It includes a
sharper constant-weight classification and exact finite checks; it does
not settle the general first-order conjecture or give a quadratic lower bound.

## Build and verify

The standalone source requires a LaTeX installation with `latexmk`,
`pdflatex`, and the packages declared in `paper.tex`.

```sh
make paper
make verify
```

`make verify` runs the general coding-theory checks using Python's standard
library and compiles the rational-fiber enumeration with `clang++` (C++17).
It recomputes the high-moment certificate and its independent
complementary-subset identity. These finite checks supplement the proofs;
they do not replace the cited generic-rank and proximity-gap theorems.

`research/finite_weights/factored40_certificates.json` records the current
degree-40 certificate. The earlier degree-20 certificate remains in
`moment_certificates/weight_certificates.json` for comparison.
The optional discovery script `moment_certificates/search_weights.py`
requires NumPy and SciPy; numerical optimization is unnecessary to verify
the saved integer certificate.

The appendix model scripts and their saved results are also preserved in
`checks/`. They are not native verifier executions. Two historical source
inspection scripts, `verify_scheduled_transfer.py` and
`verify_query_survival.py`, refer to the original local checkout of the
pinned proving source; they are not part of `make verify`.

## Draft provenance

The manuscript incorporates the September 15 consolidated research draft,
its exact certificates, and the subsequent puncturing-bound note. The
title, abstract, introduction, security discussion, and application framing
were revised for this repository. The mathematical development precedes
the S-two application. `provenance.json` records the input hashes and
validation performed for this version.
