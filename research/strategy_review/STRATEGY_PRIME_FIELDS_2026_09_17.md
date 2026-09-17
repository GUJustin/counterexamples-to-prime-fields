# Strategic review: prime-field fixed-gap ordinary correlated agreement

September 17, 2026. Independent review of the repository, not another
barrier-polishing exercise. No new theorem is claimed here.

## Assessment

The research has explored many variants, but not equally distinct
mechanisms. Cyclic Dickson words, their nearest orbits, composition
lifts, sparse cyclic banks, and deformations of the same incidence bank
occupy a disproportionate share. Several valuable limitations are now
proved, so repeating nearby censuses has low expected value. None of
the currently established source families is demonstrably close to
prime-ambient fixed-gap superlinear ordinary CA.

The compiler is no longer the main problem. A characteristic-zero
nearest bank with M-K>=cN and L growing, over varying number fields,
would suffice: specialize at arbitrarily large completely split primes,
use same-field boundary-preserving padding, and random directions.
CYCLOTOMIC_PRIME_TRANSFER.md proves exact fixed-rate/fixed-gap transfer
for cyclotomic sources, even for slowly growing L=o(N). The same algebraic
specialization argument works in general number fields using completely
split primes. The construction bottleneck is a growing high-margin
nearest bank, not necessarily a linear-size bank or an explicit line.

Two already-proved restrictions should govern resource allocation:

* Generic full-row Jacobian lifting cannot scale L at fixed gap. The
  bound L*eta<=2-rho-O(1/N) means that another larger smooth seed cannot
  solve the problem. A scalable source must have exact dependencies.
* Generic quadratic fiber towers, including varying degree caps, cannot
  amplify a fixed seed into an unbounded fixed-gap list. Ordinary
  tensoring/composition is not a missing easy amplification trick.

The current finite-field orbit argument has a different precise gap:
for rough k=(p-1)/4, a nearest stabilizer is either 1,2 or greater than
R. Only the third branch gives p/r growing after descent. Excluding small
ORBIT sizes does not select that branch. Dirichlet alone cannot help.

## Ranked independent routes

### 1. Deliberately dependent noncyclic incidence varieties

Priority: highest exploratory allocation, but still high risk.

Allow nodes and word values to vary freely over characteristic zero,
and seek exact algebraic dependencies between candidate-agreement
equations. The positive eight- and ten-candidate lifts show the finite
phenomenon is real. The full forty-node Dickson obstruction rules out
one incidence bank, not all incidence patterns or all nearest candidates.
The complete 210-candidate nearest bank is a materially larger design
space than the original twenty Dickson candidates.

Missing object: a parametrized incidence family with dependent equations
whose dependencies are identities over characteristic zero, rather than
identities that hold only in one finite characteristic. A rank-deficient
Jacobian alone is neither success nor obstruction. One needs compatible
higher-order equations or an explicit symbolic parametrization.

Best plausible payoff: an unbounded nearest bank over number fields,
then the prime-field compiler. A finite successful bank above the
full-row threshold would only identify a potentially scalable mechanism;
it would not itself establish growth.

Concrete first experiment: on the complete F41 nearest bank, inspect
24 deliberately varied sixteen-candidate incidence subsets, including
patterns not contained in the twenty-candidate Dickson subbank. Here
N=40,K=10,A=15, so L*eta=2>2-rho=1.75: full-row lifting is impossible.
Remove the standard gauge freedoms, compute the complete first-order
compatibility obstruction, and retain only compatible patterns. For at
most two survivors, test the next obstruction and seek symbolic syzygies
that explain the row dependencies. Preserve the true maximum through
the existing finite-support specialization criterion.

Stop criterion: if all 24 patterns fail, stop that subset-design rule;
do not respond with a larger random census. If a survivor has no
identifiable exact dependency after the bounded second-stage analysis,
do not advertise scalable progress. Continue only after an explicit
relation suggests a family with a varying size parameter. Each numerical
job should respect the existing resource guard.

### 2. Exact moment-collision designs on freely chosen algebraic nodes

Priority: second; analytically distinct from deformation.

Seek many subsets of one domain whose monic locators share a linear
number of leading coefficients. Their differences then give a polynomial
bank under one degree bound, and a received polynomial supplies an exact
agreement ceiling. This packages true nearestness into the construction
instead of proving it after an arbitrary incidence search.

The existing interval concentration argument gives impressive shrinking-
gap examples but does not address a linear number of exact moment
constraints. Bare finite-field pigeonholing is already insufficient
below Elias. Root-of-unity complete fibers and independent product
constructions have specific constant-list obstructions in the repo.
The neglected version is a dependent moment design with freely chosen
algebraic nodes, not another estimate of the same interval class.

Missing lemma: a sequence of non-composition subset designs with an
unbounded number of equal first Theta(N) moments. Parameter counting is
unfavorable generically, so exact dependencies must be part of the design.
First gate: construct a symbolic three-way identity with a varying size
parameter and verify that it extends the NUMBER of subsets, not merely
replicates their roots. Stop any proposed recursion immediately if its
list count stays constant or its moment depth divided by N tends to zero.

### 3. Elliptic or higher-genus symmetry with an explicit RS degree budget

Priority: a short symbolic feasibility gate; no numerical search yet.

Growing torsion translation groups on an elliptic curve provide symmetry
that is not available from growing noncyclic automorphism groups of the
projective line in characteristic zero. This is genuinely different
from cyclic Dickson symmetry. But an AG-code construction is not an RS
construction, and descent to an x-coordinate can be expensive.

Concrete candidate from the team: symmetrized functions
x(P+a)+x(P-a), viewed as rational functions of x(P), and an isogeny-based
received word. Their poles vary with a. Clearing the union of those
poles may increase the common RS degree by as much as the size of the
candidate bank, or worse when a two-dimensional torsion set is used.

First task: compute pole divisors and the exact common-denominator degree
symbolically, together with the number of surviving distinct x-nodes
and predicted agreements. Require A-K>=cN and growing L after every
conversion. Stop before enumeration if the denominator consumes the
entire proposed margin. A shared-pole subspace or cancellation identity
that avoids this cost would justify further effort. Without that, this
is an interesting AG example with no payoff for the requested RS problem.

### 4. Prime-order cyclic domains: CLOSED by a general obstruction

Priority: no further search allocation.

The independent audit in
../cyclotomic_dickson_word/PRIME_ORDER_COSET_WORD_OBSTRUCTION.md proves
that, for prime r coprime to fixed s, any NONINVARIANT polynomial of
degree at most D agrees with ANY word constant on the mu_r cosets of
mu_(sr) at at most D+s-1 points in characteristic zero. In degree <r
this gives at most r+s-2 agreements for every nonconstant candidate. The proof reduces a normalized
cyclotomic solution at a prime above r, collapses each coset to a distinct
s-th root, and counts zeros of the nonzero reduced derivative.

In particular the arbitrary-four-value proposal has maximum nonconstant
agreement at most r+2. Its normalized surplus cannot remain positive.
This closes the proposed broader cyclic branch before another census.
Changing to degree >=r does not help: strip the entire invariant part
Q(X^r) before reduction, and the same derivative argument applies.
Above this bound only invariant candidates remain, descending to the
fixed s-point quotient domain. The geometric kernel's r+1 result is within one point
of this bound, but proximity to that extremum is not progress toward the
fixed-gap target.

### 5. Native exceptional-prime short-domain sources

Priority: reserve exploratory slot, lower immediate confidence.

A source need not lift to characteristic zero. Nonzero integer or
cyclotomic incidence determinants may vanish modulo special large
primes, potentially producing short-domain lists only in those
characteristics. This differs from choosing ordinary split primes,
where all incidence ranks eventually stabilize to characteristic zero.

Missing lemma: a controlled sequence of large exceptional prime factors
that annihilates enough mutually compatible minors to create a whole
nearest bank while retaining distinct nodes and a positive margin.
A large factor of one determinant does not establish this. Merely using
Frobenius again generally costs degree comparable to p and loses the
short-domain ratio.

First gate: identify a symbolic family of incidence ideals with a
nonconstant common characteristic obstruction, then ask whether its
prime factors are provably unbounded relative to the domain size.
Do not factor unrelated numerical minors hoping for a shared bank.
This route has high upside but no current credible scalable seed.

## Recommended allocation and honest likelihood

Use distinct agents for (1) dependent incidence compatibility, (3) the
elliptic pole-budget gate, and (2) the moment-design question;
keep the root on synthesis and the user-facing decision about priorities.
The moment-design agent should begin with a concrete identity rather than
an unconstrained numerical search. The cyclic slot is now closed by proof. Maintain the practical better.codes optimization
track separately: a mathematical lower bound is not a direct route to
an improved security ledger.

I would allocate no new time to generic fiber amplification, all-row
smooth Hensel scans, larger fixed Dickson nearest-bank censuses, or
routine sharpening of already-established barriers without a new lemma
that changes feasibility. These tasks can generate publishable detail
while leaving the principal target unchanged.

There is currently no route here that merits a confident prediction of
a prime-field breakthrough before the deadline. The most useful change
is to run explicit feasibility gates across distinct mechanisms and
terminate failed branches, rather than interpreting the growing count
of restricted negative results as convergence toward the desired source.
