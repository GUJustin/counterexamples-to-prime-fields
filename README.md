# Counterexamples to List and Line Decodability Bounds over Prime Fields

Working draft by Justin Thaler, September 18, 2026.

[Read the paper](paper.pdf) · [LaTeX source](paper.tex) · [ZK disclosure summary](reports/stwo-zk-disclosure-summary.pdf)

**Latest verified results (September 18, morning):** the full-page,
one-inch-margin ePrint draft (244 pages) now proves a prime-field line construction
with more than n^(3/2)/4 exceptional challenges, each having a singleton
list, at an error radius covered by the Dao–Kominers–Thaler bounds
and beyond the Johnson radius. Both source words
are outside the tested radius. A collision-averaging variant gives
more than p/36 singleton bad challenges over an infinite sequence of
prime fields with n = Θ(p^(2/3)). Thus singleton lists can coexist with
a constant exceptional probability even over prime fields in this regime.

A further audited random-padding theorem removes the one-coordinate
restriction: the source gap can grow as c log n / log log n, for any fixed
0<c≤1/2, while at least (1/e−o(1))p challenges have singleton lists.
At c=1/2 this gives Ω(n log log n) singleton bad challenges.
In that theorem the dimension is three. A newly audited correlated-cover
construction permits gap and dimension Θ(n^α), for any fixed 0<α≤1/3,
with Θ(n^(3(1−α)/2)) singleton exceptional challenges. For example,
a gap of order n^(1/5) coexists with n^(6/5) exceptions.
Both rate and fractional source gap still tend to zero. This is not fixed-rate tightness
or a better.codes improvement. On the growing-gap examples, the O(n²)
upper comparison exceeds p and is vacuous as a probability bound; constant
bad probability does not establish tightness of that upper bound.
The uniform finite upper comparison is
31000n². A separate extension-field construction gives the same exponent
and an exact two-level spectrum; its affine-witness companion asymptotically
attains a universal triple-count bound.

These results do not supersede the fixed-rate near-capacity counterexamples
of Krachun–Kazanin–Haböck or the capacity-conjecture refutation of
Diamond–Gruen. Our source separation and their gap from capacity are
different quantities. The distinction pursued here is that these exceptional challenges occur
at error rates where the Dao–Kominers–Thaler upper bounds already apply,
even though each exceptional word has only one nearby codeword. This
does not yet show that those upper bounds are close to tight.

An explicit gap-three example has length 4,503,001, dimension three,
and **5,127,684 singleton exceptional challenges**, verified by a separate
implementation. See the [certificate and replay](research/prime_quadratic_line/algebraic_fresh_certificate/README.md).

Reproducible prime-field examples include n=1201 over F_2000003 with
exactly 15,026 singleton exceptions, and an optimized domain over F_20011
with exactly 10,798 singleton bad challenges (more than 53% of the field).
See the [exact certificate](research/binary_characteristic_transfer/prime_L25/README.md)
and [pooled construction](research/binary_characteristic_transfer/pooled_prime_labels/PROOF_AND_JOB.md).

Earlier results include Theorem U.1, which gives an exact
seven-member nearest-codeword list at quarter rate: length28, dimension7,
and fourteen agreements per candidate, over arbitrarily large prime fields.
Two short cyclotomic identities give the construction; its complete-list proof
has independent arithmetic audits. The quarter-rate example works for every
prime p>10^10 with p=1 modulo7. New Theorem V.1 proves the matching universal
maximum seven for cubics on any fourteen-point domain in characteristic zero
and in all sufficiently large characteristics. This upper theorem does not
assert a universal maximum seven for length28, dimension7. Polynomial pullback preserves exact list size
seven at length14m and degree bound3m. This strengthens the earlier six-word
construction, but does not yet give growing lists or a better.codes improvement.
New Appendix W completes the rigidity classification of the seven-cubic banks
and proves that no rational cover of any degree at least two can add an eighth
nearby word by the proper one-extra-pole construction. This excludes a specific
augmentation mechanism, not arbitrary eight-word constructions. Corollary W.3
extends the obstruction to every proper denominator compatible with quarter
rate for cover degrees through nine.
Theorem W.4 constructs the uniform degree-ten Paley norm net exactly
in characteristic zero and proves that it has no integral rational
member. Its proof reconstructs a degree-62 discriminant and gives exact
polynomial identities excluding the required multiplicity. The theorem
concerns this particular net, not arbitrary degree-ten constructions.
Theorem W.5 proves the corresponding exclusion for the orbit-2 uniform net,
using a separately reconstructed degree-62 discriminant and independently
verified projective multiplicity certificates. Both nets also exclude
the possible nonprimitive norm powers under the stated augmentation hypotheses.

New Theorem W.6 gives a positive construction: over arbitrarily large prime
fields, a length-32, dimension-7 word has exactly eight nearest codewords,
each with 14 agreements. An explicit rational cubic seed and independently replayed interpolation
and quadratic norm certificates prove the result.
Its agreement is above the first-order curve at rate 7/32. This is a finite
seed, not a growing-list construction or a better.codes improvement.

Theorems W.7 and W.8 extend that rational seed by shared intersections:
complete nearest lists of ten cubics on eighteen nodes and eleven cubics on
nineteen nodes, all with seven agreements, over quadratic number fields and
arbitrarily large prime fields. Independent exact interpolation verifies
completeness. Their pullbacks give at least ten candidates at `(n,k,A)=(90,16,35)`
and at least eleven at `(247,40,91)`, both above the first-order curve;
completeness is not asserted for these pullbacks. Theorem X.1 gives a separate
complete nine-quartic list with eight agreements on eighteen nodes by an
incidence exchange. None of these finite constructions establishes growing
lists, intrinsic asymptotic tightness, or a better.codes improvement.
Proposition W.9 further proves that every connected quadratic pullback of
the fixed ten- and eleven-cubic sources, unramified on the selected fibers,
preserves the complete nearest list and leaves a two-match gap to all other
sextics. This characteristic-zero robustness statement has independent
exhaustive norm-system verification; it does not itself amplify list size.
Proposition W.10 gives a complete eight-member list at `(n,k,A)=(48,10,21)`
from a cubic pullback: exactly eight further polynomials have15 matches,
and every other polynomial has at most14. Its six-match gap
is proved by independent complete extension-field interpolation searches and
an exact characteristic-zero transfer. It also lies above the first-order
curve, but remains a fixed-list construction.

A separate ramified-reduction argument bounds the characteristic-zero cyclic
word `W_r` by `r+2` agreements when `r>5` is prime, and by `r+2r/ell`
when `r=ell^a`, `ell>5` prime. Thus growing prime orders cannot supply a fixed
positive capacity gap through this word; fixed-prime powers and general
composite orders remain open. This is a family-specific obstruction, not a
universal list-decoding bound.


Corollary 2.4 sharpens the shrinking-gap and prime-size lower bounds by
an explicit second-order term. The companion method audit now proves
fourth-power inverse-margin cost for every full-prefix monomial support
downward in the value variable, under either current challenge-counting test. This is a limitation of the
specified interpolation ledger, not intrinsic proximity-gap tightness.

Theorem R.5 proves an exact
transition for the complete Dickson cubic-ODE solution family: a linear
list at agreement `3/8`, but at most `ceil(epsilon^-2)` family members for
any word at agreement `3/8 + epsilon`. A matching majority construction
works with `p >= 2^36 L^2` and gives `L` candidates at agreement
`3/8 + 1/(32 sqrt(L))`. The quadratic prime-size bound replaces an earlier
exponential requirement. [Proof and independent review](research/quartic_singular_route/ROOT_SHARP_TRANSITION_AUDIT.md).
These are bounds within the classified family, not upper bounds for the
whole Reed--Solomon code or general proximity-gap tightness.

Theorem R.6 also proves a uniform list bound for every degree-two rational
first-integral family, including quadratic moving denominators. If
`p>max(2,10D)`, agreement `D+eta*n` permits at most
`max(40,floor(1/eta))` degree-at-most-D members. The proof derives a
coefficient-height bound from five sections and applies the classical
Pasten--Wang square-value theorem. It does not apply to arbitrary
first-order equations.

Theorem R.7 extends the finite-critical-locus list bound to every fixed
monic value degree. Corollary R.8 shows that, under its explicit
characteristic bound, exceeding this bound forces a constant fiber with
a repeated factor. This is a necessary structural condition, not a
classification of those remaining families.

Theorem R.9 bounds every weighted monic-cubic first-integral family
with denominator depending only on the evaluation coordinate. For
`p>max(3,2D)`, its list at agreement `D+eta*n` has size at most
`floor(9+(3+108D/n)/eta)`. This includes all prime-field rates below
one half, within the stated family. Repeated denominator roots and
nonconstant Frobenius critical values are covered. In particular, the
complete Dickson bank cannot have such a first integral for admissible
primes at least 521. [Proof](research/short_domain_cubic_source/general_cubic_list.tex)
and [independent audit](research/short_domain_cubic_source/TWO_D_RADICAL_INDEPENDENT_AUDIT.md).

Theorem R.11 extends the cubic cover argument to every constant fiber supported on two roots, with arbitrary multiplicities `r,s`. The section bank is an affine pencil or has at most `2(r+s)/gcd(r,s)+2` members. This does not classify fibers with three or more distinct roots. [Proof](research/short_domain_cubic_source/two_root_fiber.tex).

Appendix S proves, in every characteristic and for arbitrary received words when n≥2w, that contact excess is at least (w−1) times R-degree. Zero excess is exactly a power of a graph matching the received word. This replaces the earlier guarded and uniform-contact statements with stronger results and a shorter proof. These are constraints on factors, not yet a bound on first-tail component costs. [Proofs and scope](research/better_codes_second_jet/contact_resource_appendix.tex).

There is still **no better.codes improvement**. The fully repaired target
certificate exceeds its allowance by 7.65%; earlier conditional estimates
were superseded by the complete audit. The current low-degree derivative
theorem also does not apply directly to the benchmark's raw interpolation
source, whose ordinary core is the full domain.
[Benchmark limitation](research/hermite_johnson_route/BENCHMARK_RELEVANCE.md).

A [reanalysis of the restored second-derivative framework](research/better_codes_second_jet/CLOSED_CURVATURE_RANK.md)
verifies a restricted local-rank saving. In a matched finite comparison at
multiplicity 128, it lowers the sufficient challenge-degree cap from
31,890 to 5,515. The formula is a specialization of the restored exact
rank theorem, independently rederived and checked here; it is not a new
rank theorem. Four broader restored source profiles also meet the critical routing
gate, but their retained-branch bound exceeds the incumbent cost.
[Complete scope and cost audit](research/better_codes_second_jet/RESTORED_ROUTE_COMPATIBILITY.md).
The certified benchmark and score remain unchanged.

The follow-up [source search](research/prime_fixed_gap_new_route/NEXT_SOURCE_STATUS.md)
now records exact obstructions to common-factor Dickson shortening,
primitive squarefree split-cubic pencils, and all degree-two rational
pencils in characteristic `p>max(2,10D)`, together with bounded projection and
second-derivative experiments. These results narrow the search; they do
not supply a new prime-field lower bound.

**Other results and research history:** A separate
[20-page first-order tightness note](research/first_order_support_audit/note/main.pdf)
proves the sharp quarter-rate threshold for the specified interpolation
framework. A new independently audited converse also proves that the
current [ePrint 2026/2056](https://eprint.iacr.org/2026/2056)'s **standard
supports and graded row test necessarily incur inverse-margin powers two
and four** in its list and regular-MCA degree budgets. This assumes
characteristic zero or characteristic larger than every retained jet degree;
it does not cover arbitrary supports, the alternative column test, or
stronger component counts. [Proof and scope](research/current_graded_method_costs/STANDARD_SUPPORT_FOURTH_POWER.md).
The older cubic/fifth-power converse concerns only the September 10 formulas.
The separate support-threshold limitations include translation-stable nonmonomial
jet spaces. For full-coefficient monomial sources, an exact finite-length
extension uses an explicit corrected margin, uniformly in multiplicity.
The audited high-rate shape also yields a strict agreement-curve
refinement at every rate above `8-3*sqrt(6)`, already acknowledged by the
current ePrint. [Current-paper comparison](research/prime_field_tightness/EPRINT_2056_COMPARISON.md) records these distinctions. These are not intrinsic
list-size or exception-count lower bounds.
[Research status](research/prime_field_tightness/STATUS.md) distinguishes
proved results from open targets. No better.codes improvement is claimed.

There is also an intrinsic partial tightness result: at fixed rate `1/8`
and capacity gap `1/16`, a line over `F_(p^2)` has at least `ceil(n^2/20)`
full-support MCA exceptional challenges. Thus a universal linear capacity
bound fails in the large-characteristic field class. A short splitting
lemma for Dickson polynomial differences proves the improved constant.
This is **not** prime-ambient-field or first-order-regime tightness.
[Proof and exact checks](research/prime_field_tightness/QUADRATIC_EXTENSION_LOWER_BOUND.md).

Appendix N strengthens the logical conclusion by a separate construction:
`ceil(n^2/4096)` nearby labels with **no ordinary correlated
agreement**, over quadratic extensions at exact rate `3/13` and capacity
gaps greater than `3/26`. The gap is bounded below, not fixed exactly.
Orbit descent gives a linear-size true nearest list on its own domain;
Dirichlet prime selection and at most two anchors suffice, without a sieve estimate.
[Full proof and verification](research/ordinary_ca_superlinear/PROOF.md).

Corollary N.3 fixes both rate and gap. Proposition N.4 now strengthens
it to **exact rate `1/8`, gap `1/16`, and `ceil(n^2/192)` nearby labels
with no ordinary correlated agreement over `F_(p^2)`**. Conjugate-avoiding
common-zero blocks normalize the parameters; random nonzero padding
directions exclude every nonzero explaining polynomial. The proof has
an independent subagent audit and exact finite checks.
[Quadratic-extension proof](research/ordinary_ca_superlinear/RANDOM_DIRECTION_QUADRATIC.md).

The exact family gives rate `b/d`, gap `1/d`, and at least
`ceil((b+1)n^2/(4(b+6)d^2))` ordinary-CA exceptions over
`F_(p^(2^(b-1)))`, for `b=2,3,4,5` and `d>=b+7`.
These are capacity-regime lower bounds, not prime-ambient-field or
first-order tightness, and they do not improve better.codes.

A fresh [exact better.codes frontier audit](research/better_codes_revisit_2026_09_17/README.md)
confirms no new score: the closest alternative fixed-domain construction
still needs just over a fourfold increase in certified family count.
This numerical target is not a proof that such an increase is possible.

A [strategic review](research/strategy_review/README.md) now prioritizes the
actual incumbent's three-source moving-component certificate for better.codes,
with independent agreement-based and new-source construction work alongside it.
The earlier 1100-fold deficit applies to weaker single-equation bounds, not
the current incumbent. An [exact replay and sensitivity audit](research/better_codes_current_lower_2026_09_17/README.md)
now reproduces the 27 auxiliary interpolation counts, 10 primary/phase
kernel counts, and the stored ledger and threshold arithmetic. Upstream
packing validation and the target certificate remain incomplete. No new
benchmark score is claimed.

The paper studies quantitative coding statements used in security analyses
of hash-based SNARKs. It proves general list and affine-line separations
over prime fields, gives finite circle-code examples, and treats the S-two
analysis as an application of those results.

The clearest line-level message is that **even below Elias, two far words
can have every affine combination other than the endpoints close to the
code**. Both endpoints can lie almost half a gap outside the radius, while
a random mixture is nearby with probability `1-2/p`. For any fixed batch
size `t`, all inputs can be almost `(1-1/t)*eta` outside the radius while
a random affine combination is nearby with probability `1-O(t/p)`.
Unrestricted linear combinations and multilinear mixtures have the same
failure; for `2^ell` inputs, the multilinear nearby probability is exactly
`(1-2/p)^ell`. The nearby polynomial changes with the mixing coefficient.

The underlying construction also gives a line close to the code at every
point but one, with that point only one coordinate short of maximally far. At every fixed rational rate, all `p-1` nonzero
parameters are nearby while zero has distance `1-rho-1/n`. Its separation
from the radius is `(1-o(1))*eta`, almost the entire capacity gap. The
radius remains strictly below Elias. The `c1=c2=1` numerical prescription
predicts a nearby fraction tending to zero; the actual fraction is `1-1/p`.
The gap still shrinks, and this strongest relative separation approaches
the Elias boundary. Every nonzero point has exactly the tested distance,
and its decoding list is disjoint from the lists at all other nonzero
parameters. The direction changes the minimum number of coordinates
needed for the distance improvement. No common agreement set explains the line.

A separate deterministic construction uses powers of two as its core
coordinates. **Every nearby point has a unique, efficiently recoverable
codeword**, while the proposed nearby-count bound is exponentially too small.
At half rate the entire line can have just two distance levels, with every
parameter outside the nearby bank at the far level. This failure does not
require decoding ambiguity or difficulty finding witnesses. An extension
using scaled prime-order orbits makes the separation at least
`(1-epsilon)*eta` for any fixed positive `epsilon`, on suitable infinite
progressions of prime fields, with the same unique-witness and recovery
guarantees. These examples have sparse nearby sets; the full-coverage
result is a separate construction.

**Two padding orbits strengthen the unique-witness result even after
raising the exponent constant to `c2=2`.** The far point can remain
arbitrarily close to a whole gap outside the radius. Over sufficiently
large splitting primes, every nearby witness is efficiently recoverable;
a separate character-sum argument gives logarithmic-length existence
without that decoder. Reducing the dimension further defeats every fixed
`c2<3` while retaining more than two-thirds-gap separation and uniqueness.
The near-full-gap and two-thirds-gap statements are different tradeoffs.
Finite existence certificates reach separation `86/87` of the gap. A
length-226 half-rate certificate over an explicit 338-bit prime exceeds
the original prescription by `2^45` and the doubled-exponent version by
more than `1.19`. It specifies the field and support class, not a sampled
evaluation domain. A length-220, dimension-95 certificate over the
327-bit prime `121*2^320+1` gives a further shorter example.

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
- Random paired domains give **complete nonzero coverage with almost the
  entire capacity gap as separation**, and an exact distance formula on an
  affine space. Their exceptional point has distance `1-rho-1/n`; length
  can be `Theta(log p * log log p)` and `eta~H(rho)/log2(p)`. A character
  estimate and successive pairs of extra roots complete the joint product
  image. The sampler runs in expected polynomial time in `log p` and
  succeeds with probability `1-p^-Omega(1)`. Exact finite certificates
  include length **158** over `2^61-1`, changing only two coordinates;
  length **2518** over `2^521-1`, changing four coordinates with generator
  failure below `2^-88`; and length **26218** over `2^1279-1`, changing
  twenty coordinates with failure below `2^-123`. The last example's
  separation is **20/21 of the gap**. Independent integer replays support
  these bounds. Coverage of the stored sample has a probability guarantee
  over the generator, not an individual deterministic certificate.
  Optimized certificates give full coverage at length 2142 over `2^521-1`
  while the prescribed fraction is below `2^-81`, and length 8014 over
  `2^1279-1` with generator failure below `2^-64` and prescribed fraction
  below `2^-121`. These results defeat the `c1=c2=1` prescription; the next
  construction handles arbitrary fixed numerical constants.
- Deterministic paired-domain banks over `2^31-1` are checked by two
  independent exhaustive enumerators. At exact half rate and length **62**,
  there are **140,916,078** certified nearby parameters, against a prescribed
  bound below **103,199,661**. Its full list distribution is also certified:
  **136,494,714** parameters are uniquely nearby, and every point on this
  line has at most **five** nearby codewords. A length-68 instance also beats twice the
  proposed prefactor. All four stored instances are strictly below Elias;
  their directions change only two coordinates and their exceptional points
  are one coordinate short of maximum distance. These are concrete chosen
  domains, including a length-64 instance, with no prescribed FFT-domain claim.
- A cubic change of the seed domain gives **complete nonzero coverage**
  at every fixed rational rate: all `p-1` nonzero parameters are nearby
  while zero is a fixed positive fraction of `eta` outside. For every
  proposed `c2`, any integer `u>c2` permits separation `eta/u` and defeats
  the numerical prescription. An exact half-rate certificate over `2^127-1` has length **214**,
  separation `eta/2`, and prescribed nearby fraction below **1/4096**.
  Larger certificates over `2^1279-1` and `2^9689-1` give prescribed
  fractions below `2^-308` and `2^-593`, respectively.
  The geometry proof and two independent arithmetic implementations support
  these existence certificates. A separate randomized procedure outputs
  the code and line in expected polynomial time in `log p`, with success
  probability `1-p^-Omega(1)`, without finding the large moment class.
  A stored length-990 sample over `2^521-1` has an independently checked
  generator failure bound below `2^-128`; its structural properties are
  replayed exactly. This is a probability guarantee over sampling, not a
  deterministic complete-coverage certificate for that individual sample.
  Nearby-witness recovery remains a separate question.
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
The general first-order conjecture and quadratic fixed-gap error over prime
ambient fields remain open.

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
structural sharpness results do not settle quadratic MCA error over prime
ambient fields.

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
(with SymPy required by the interpolation-pool checks; optional `gmpy2`
substantially accelerates the large-prime checks) and compiles the rational-fiber enumeration with `clang++` (C++17).
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

Corollary N.5 gives rate `b/d` and gap `1/d`, for `b` in `{2,3,4,5}`
and `d>=b+7`, over `F_(p^(2^(b-1)))`. In particular, rate `2/9`
and gap `1/9` admit at least `ceil(n^2/864)` nearby challenges with no
ordinary CA over `F_(p^2)`, in characteristic greater than message degree.
[Parameter-family proof](research/ordinary_ca_superlinear/RANDOM_DIRECTION_QUADRATIC.md).

[Leading-degree separation](research/two_branch_recurrence/NEWTON_DEGREE_CRITERION.md)
now gives a characteristic-free sufficient condition for linear full-support
exception counts among actual solutions of a challenge-dependent first-order
identity. Appendix P includes the proof and the unnormalized two-branch
Riccati corollary. The condition allows singular agreement coordinates but
requires nonzero coefficient pivots and separation of the nonlinear terms.
It is not a general first-order proximity-gap theorem.

Appendix T verifies a second one-pole extension: six distinct polynomials of degree at most 14 each agree with one word on 30 of 60 coordinates over arbitrarily large prime fields. An exact F97 witness has two independent nonsingular lifting certificates. This is a fixed-size construction, not unbounded iteration or a leaderboard improvement. [Proof and certificates](research/prime_line_strengthening/four_word_one_pole/transversal_search/SIX_WORD_LIFT.md).
