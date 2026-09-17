# Counterexamples to List and Line Decodability Bounds over Prime Fields

Working draft by Justin Thaler, September 17, 2026.

[Read the paper](paper.pdf) · [LaTeX source](paper.tex) · [ZK disclosure summary](reports/stwo-zk-disclosure-summary.pdf)

The paper studies quantitative coding statements used in security analyses
of hash-based SNARKs. It proves general list and affine-line separations
over prime fields, gives finite circle-code examples, and treats the S-two
analysis as an application of those results.

The clearest line-level message is that **a line can be close to the code
at every point but one, with that point half the capacity gap beyond the
radius**. At every fixed rational rate, the construction has `n=Theta(log p)`,
all `p-1` nonzero parameters nearby, and a point `eta/2` outside, strictly
below Elias. No common agreement set explains the line. The `c1=c2=1`
numerical prescription predicts a nearby fraction tending to zero;
the actual fraction is `1-1/p`. The gap still shrinks.

The list-size results separately show that the proposed exponent must
grow almost quadratically, rather than linearly, in the reciprocal gap.
Neither result establishes superlinear line counts at one fixed positive
gap on short domains or transfers automatically to a prescribed FFT domain.

## Results

- Exponential lists on integer-interval domains rule out a uniform
  `exp(O(1/eta))` list bound at every fixed rate, with a shrinking gap and
  radii below the characteristic-based Elias bound. Optimizing length rules
  out every bound with logarithm `o(eta^-2/log(1/eta))`. For every sufficiently
  large prime, with `b=log2(p)`, the list has at least
  `2^((1/2-o(1))*b^2/log2(b))` codewords below Elias.
- A cubic change of the seed domain gives **complete nonzero coverage**
  at every fixed rational rate: all `p-1` nonzero parameters are nearby
  while zero is a fixed positive fraction of `eta` outside. For every
  proposed `c2`, any integer `u>c2` permits separation `eta/u` and defeats
  the numerical prescription. An exact half-rate certificate over `2^127-1` has length **214**,
  separation `eta/2`, and prescribed nearby fraction below **1/4096**.
  Larger certificates over `2^1279-1` and `2^9689-1` give prescribed
  fractions below `2^-308` and `2^-593`, respectively.
  The geometry proof and two independent arithmetic implementations support
  these existence certificates. The domains and directions are not enumerated.
- Elementary padded-interval variants give explicit density/separation
  tradeoffs and can make the number of missing coordinates grow while
  the nearby fraction tends to one. Every affine codeword graph then
  contains only `o(n)` selected witnesses, for every choice of witnesses.
  The dense families have large global lists; the generic-domain result
  below addresses the separate actual-list-size question.
- If the rate tends to zero, even the constant code can have **every nonzero
  parameter nearby**, with exactly one far point a fixed fraction of the
  capacity gap outside the radius. The prime field has polynomial size in
  the length, and the statement transfers to any domain of that size.
  This elementary boundary case works on every domain of that size;
  the fixed-rate construction above uses chosen domains. Neither gives
  a separation from the actual maximum list size.
- An anchored lift and padding construction gives genuine failure of
  correlated agreement at an exactly fixed positive rate and gap, for
  arbitrarily large lengths. The necessary coefficient of a linear
  exceptional-count bound has logarithm of order
  `eta^-2/log(1/eta)` at every sufficiently small rational gap. Every
  nearby word on the displayed line can have a unique nearby codeword,
  while the line contains a word one coordinate beyond the decoding radius.
  A concrete family has more than `3.76e17*n` nearby challenges.
  The same count also has polynomial-size prime-field realizations;
  whole-line uniqueness is not asserted for that realization.
- A code can have maximum list size exactly `n-k-1` and nevertheless
  have `binom(n,k+1)` uniquely nearby points on an affine line without
  correlated agreement. Every other point of that line is at the code's
  maximum possible distance. A puncturing bound shows that this parameter
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
  32768 reduces to a power or twisted-inversion quotient. The extension
  to coverage defect `c` requires `n > 6*(B-1+c)` and forces full balance
  if `c < B/2`. On a dyadic domain its divisibility conclusion needs no
  small-defect condition: degrees 513, 514, and 516 require at least
  43,606, 43,180, and 43,360 uncovered points. An exhaustive finite
  theorem also gives exactly **three** as the maximum number of complete
  fibers of any rational cubic on the pinned 256-point subgroup, over
  any extension field. This excludes a proposed composed-cubic bank;
  it does not improve the numerical score.

- For first-order equations of fixed jet and challenge degrees, bad
  labels with a positive fraction of nonsingular agreement coordinates
  number **O(n)** at fixed positive gap. This includes implicit equations
  and actual solution surfaces. For `R(X,z)P'=A(X,z,P)`, it bounds all
  bad labels linearly when `deg_X R` also lies a fixed positive fraction
  below the agreement threshold. A nonlinear two-solution equation has
  exactly **n/2 bad labels** at rate tending to 1/4 and gap 1/4.
  Controlling singular agreements in general remains open.

- A sharp bound limits affine binary support families in every
  characteristic other than two: fixing `s` leading locator coefficients
  forces dimension at most `floor(min(t,n-t)/(s+1))`. A trace family over
  `F_16` violates this bound, identifying a specific barrier to direct
  binary-to-prime transfer. A quantitative corollary allows at most
  `O(N^(3/2))` punctured codimension-two binary subspaces in one
  odd-characteristic prefix class, versus the quadratic full binary family.

[New finite-certificate proofs and replay instructions](research/overnight_2026-09-16/README.md).

The statements retain their field, domain, radius, and quantifier
restrictions. They do not establish a complete protocol attack or an
improved better.codes submission.

## Supplementary research notes

[Nearby density tending to one](research/fixed_gap_padding/NEAR_UNIT_DENSITY.md)
contains the asymptotic parameter calculation.
[Far-point padding](research/fixed_gap_padding/FAR_POINT_PADDING.md) gives
the simpler multiplicative-averaging proof, and the
[scope audit](research/fixed_gap_padding/DENSE_SCOPE_AUDIT.md) distinguishes
numerical prescriptions, actual maximum list size, and far-point premises.
The finite density table has a separate arithmetic replay and a complete
small-field direction count.

[Nonsingular agreement coordinates and first-order MCA](research/quasilinear_first_order/README.md)
contains the local reconstruction proof, its value-independent-separant
corollary, the matching linear lower family, and exact finite checks.
[Exact rational-cubic packet bound](research/structured_domains/general_cubic_packets/README.md)
contains the finite reduction, exhaustive source, all 85 checkpoints,
and independent small-field and witness checks.

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

[Boundedly many roots and full-support MCA](research/bounded_root_mca/README.md)
proves an `O(n)` exceptional-label bound for all candidates with a fixed
bound on their number of distinct roots, at fixed positive rate and
agreement and sufficiently large characteristic relative to length.
Root positions and multiplicities may vary. Appendix G contains the proof
and a third-order equation whose actual solution variety has quadratic
degree but whose bad labels remain linear. The earlier
[fixed-power argument](research/power_family_mca/README.md) is retained.
The general first-order conjecture and quadratic fixed-gap error remain open.

[Actual first-order solution components](research/first_order_actual_components/README.md)
proves that the curve and surface components of the actual regular
polynomial-solution locus have total degree `O(D)` at fixed jet and
challenge degrees, in characteristic zero or greater than message degree D.
Appendix H gives the proof and sharp examples, including a first-order
equation with exactly `binom(D+2,2)` regular isolated solutions and
distinct prime-field labels. That quadratic family nevertheless has only
constantly many nearby labels at a fixed positive gap. The general
contribution of isolated points and persistent affine codeword graphs
remains open; this does not prove the first-order MCA conjecture.

[Sharp isolated-solution counts](research/isolated_solution_sharpness/README.md)
proves matching `O(D^(d+1))` and `Omega(D^(d+1))` bounds for actual
isolated regular polynomial--challenge solutions at every fixed derivative
order d. Appendix I gives an explicit Wronskian family with distinct
prime-field labels, together with a constant fixed-gap nearby-label bound
for that family. Thus the algebraic count is sharp while proximity-gap
sharpness remains open.

[Higher-order actual components](research/actual_higher_order_components/README.md)
sharpens positive-dimensional degrees to `O(D^d)` and positive-dimensional
fixed-challenge degrees to `O(D^(d-1))`. Appendix J gives attaining
families, proves the isolated fixed-fiber count can be `Theta(D^d)`,
and shows that the resulting logarithmic-derivative family still has
only linearly many full-support bad labels at a fixed gap. These
structural sharpness results do not settle quadratic MCA error.

[Inverse Bernoulli equations](research/inverse_bernoulli/README.md)
have at most `2s` polynomial solutions to `P^(s-1) P'=A(X)` for
nonzero A and `p>max(D,s+1)`. Appendix K proves this sharp bound
even when `p<=sD`, classifies nontrivial pairs, and deduces linear
full-support MCA for this nonlinear first-order family.

The binary-transfer analysis also gives a sublinear shared-prefix count
inside every fixed multiplicative orbit at fixed binary codimension.
At codimension two it is `O(N^(15/16))`; see
[the orbit theorem](research/binary_affine_locator/MULTIPLICATIVE_ORBIT_TRANSFER.md).
A linear-sized transfer would have to draw from increasingly many orbits.
Under multiplicative relabeling, a sharper Gauss-sum argument makes all
codimension-two supports distinguishable by just three coefficients
in characteristic greater than three (five in every odd characteristic).
The three-coefficient cutoff is sharp; see
[multiplicative relabeling](research/binary_affine_locator/MULTIPLICATIVE_LABEL_RIGIDITY.md).

## Build and verify

The standalone source requires a LaTeX installation with `latexmk`,
`pdflatex`, and the packages declared in `paper.tex`.

```sh
make paper
make verify
```

`make verify` runs the general coding-theory checks using Python
(with SymPy required by the interpolation-pool checks) and compiles the rational-fiber enumeration with `clang++` (C++17).
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

[Sharp Riccati list bounds](research/riccati_cross_ratio/README.md) proves
`M <= floor(n/(A-D))` for bounded-degree solutions of one Riccati equation
in characteristic zero or `p>D`, and gives prime-field equality families.
A fixed nonlinear equation has at most `C_D` candidates and
`2n(n+C_D)/(A-D)` full-support bad labels, where `C_D=D+2` except
at the boundary `p=D+1`, where `C_D=2D+2`. Appendix M contains the proof.
Challenge-dependent first-order proximity gaps remain open.

[Logarithmic-length prime-field lines](research/logarithmic_length_lines/PROOF.md)
strengthens the field quantifier: every sufficiently large prime admits
a below-Elias example with length `Theta(log p)` and `Omega(p/log p)`
nearby labels, without correlated agreement. For each proposed finite
constant c2 the number of canceled moments is fixed accordingly; the gap
still shrinks. A pure-prime example over `2^127-1` at n257/k72/t78 exceeds
the finite c1=c2=1 line prescription by more than `2^76.40420`.
