# Strategic reset: intrinsic DKT tightness

September17,2026. Independent review after the user's request to step back.
This is a research allocation proposal, not a claim of new mathematical
results. Current repository proofs and the cached current ePrint are the
sources; no new literature-priority claim is made.

## Assessment

The project has a substantive intrinsic capacity result: quadratic many
ordinary-CA failures over quadratic extensions at an exact fixed rate/gap.
It also has prime-field linear-size fixed-gap lists. It has not produced
an unbounded first-order-regime list, superlinear first-order MCA family,
or prime-ambient fixed-gap superlinear MCA family. More method-cost
converses do not fill these gaps.

The strongest negative evidence is structural, not the volume of finite
searches. The full and short-domain Dickson words are now below the
first-order threshold; arbitrary puncturing of the original bank is also
controlled. Explicit Wronskian equations have quadratically/higher-degree
many actual isolated solutions, but the corresponding nearby-label counts
are bounded at fixed gap. This makes it reasonable to investigate whether
the first-order quadratic upper bound is genuinely loose, rather than
continuing to assume that a quadratic lower example must exist.

Current-file anchors:

- `../prime_field_tightness/STATUS.md` and `EPRINT_2056_COMPARISON.md`;
- `../first_order_actual_components/README.md`;
- `../isolated_solution_sharpness/README.md`;
- `../riccati_cross_ratio/TWO_BRANCH_FRONTIER.md`;
- `../ordinary_ca_superlinear/RANDOM_DIRECTION_QUADRATIC.md`;
- `../dickson_domain_deformation/{README,SMOOTHNESS_METHOD_LIMIT,RAMIFIED_OBSTRUCTION}.md`.

## Five genuinely different routes

### 1. Agreement-first isolated solutions, with willingness to prove a stronger upper theorem

**Highest immediate expected payoff.** Revisit the unnormalized two-branch
Riccati equation

    T(X)P'=(P-F_z)(P-G_z),

where T is the squarefree domain locator and F_z,G_z are affine received
branches. At every domain coordinate a candidate automatically meets one
branch. Thus many isolated labels would already have substantial actual
agreement with a branch; this avoids the central failure of the previous
Wronskian construction. The zero-branch normalization is closed, but the
fully unnormalized family is explicitly still open in the repository.

A promising upper-bound mechanism appears before any enumeration. For
more than two isolated labels, the coefficients of X above n+D-1 in
F_zG_z must vanish identically as quadratics in z. If both generic branch
degrees exceed D, their sum is therefore at most n+D-1 and each degree is
at most n-2. In the top D coefficient equations, T P' then dominates the
terms involving the constant coefficient of P. A triangular recurrence,
dividing only by1,...,D, expresses all nonconstant coefficients of P as
polynomials in z. Only its constant term remains. Substituting back gives
polynomial equations of z-degree O(D) and constant-term degree at most2.
Their isolated intersection should have only O(D) points by a bidegree
resultant/Bezout argument. This is a lead, not yet a proved theorem.

Positive-dimensional components must be retained and treated using the
existing actual-component/incidence theorem; persistent affine codeword
graphs and branch-degree-drop labels must be handled explicitly. Branches
of degree<=D have a separate high-agreement restriction. No conclusion
about arbitrary first-order equations follows automatically.

**Why worth doing:** a genuine linearly bounded agreement-bearing family
would test the conjectured looseness at exactly the singular domain
coordinates where naive ODE counting misses the issue. The recurrence may
extend to a wider class of equations whose leading X coefficients force
polynomial parameter dependence. Merely adding another narrow excluded
ansatz would not justify a long project.

**Concrete next test:** one algebraic proof pass deriving the recurrence
with its exact z-degree; construct a degree-(2,O(D)) eliminant or a pair of
coprime residuals; verify on small symbolic fixtures with n>4D and both
branches of degree>D. Include positive-dimensional and disappearing-leading-
coefficient fixtures. Test actual agreement on roots of T, not only the
number of algebraic solutions.

**Stop criterion:** after that pass, stop if the residual degree in the
remaining coefficient grows with D, or if singular branches prevent an
O(D) count and cannot be classified. If it works, spend one further pass
seeking a general leading-coefficient criterion. If it does not generalize,
record a concise lemma and do not launch another large family census.

### 2. Prime-field capacity transfer through a truly short-domain nearest list

The precise missing source is a growing true nearest list over F_p with
p/n sufficiently large. A prime field with p=O(n) cannot even contain
quadratically many distinct labels. The current descent theorem does not
control the orbit size r relative to p; r may remain comparable to p.
This is the obstacle, not the padding-direction choice, which has already
been improved substantially.

Potential new input is an arithmetic characterization of stabilizers of
nearest polynomials, forcing a subsequence with r=o(p), or an entirely
new short-domain source with L growing. Search should target this ratio
explicitly. Enlarging a field to F_(p²) does not solve the prime-ambient
problem.

**Test/stop:** first prove a structural implication relating nearest-orbit
stabilizer size to congruence conditions or word symmetry. Without such an
implication, stop the Dirichlet-prime search: congruence conditions alone
currently give no useful bound on r/p. Additional short-subgroup scans of
the same Dickson word are low-value because its rigidity theorem already
blocks the first-order target, though capacity transfer is a distinct issue.

### 3. New incidence geometries rather than another deformation of the same bank

A characteristic-zero nearest-list source with growing L and fixed positive
gap would specialize at arbitrarily large split primes and could supply
route2. The p17 seed already lifts, but its list stays bounded. Generic
fiber expansion preserves the list rather than amplifying it. The full
p41 seed has a certified obstruction even to ramified mixed-characteristic
lifting. Smooth full-row lifting has its own list-size barrier.

The neglected possibility is a deliberately singular, explicitly
parameterized characteristic-zero incidence variety: for example a family
built from divisor identities or group laws on algebraic curves, then
realized as ordinary polynomial evaluations. This is a different object
from varying all coordinates of a rigid finite-field bank. A high-genus
construction is not automatically an RS construction: the reduction to
polynomials on one affine line and its degree cost must be established.

**Test/stop:** demand an explicit identity producing at least two
independent parameters of candidate polynomials, together with a provable
shared received word and positive agreement excess. Stop before symbolic
elimination if the identity merely produces rational functions of bounded
denominator degree, a family already covered by the bounded-envelope
barriers. Do not reopen the exact p41 incidence mask.

### 4. Capacity exponent growth via genuinely superlinear nearest lists

The current quadratic exception theorem is powered by a linear nearest
list and one additional incidence coordinate. Matching a capacity exponent
larger than two requires a qualitatively stronger source or amplifier,
not better constants in the same compiler. A natural intermediate target
is a true nearest list L=n^(1+c) at one fixed rate/gap in the allowed
large-characteristic field class. It would already be a meaningful
intrinsic strengthening even without a prime ambient field or first-order
agreement.

Potential routes are coupled divisor constraints or multistage algebraic
incidence constructions where constraints are shared rather than paid
independently. Independent Cartesian products and generic power-fiber
expansion have documented degree/agreement or list-preservation barriers.

**Test/stop:** write the exact resulting RS degree, evaluation length,
agreement and number of distinct candidates before proving any auxiliary
algebra. Discard immediately if the list is constant under length scaling,
if positive gap vanishes, or if characteristic falls below message degree.
This route is high upside but lower near-term probability than route1.

### 5. Parameter-varying intrinsic lower bounds as a separate, explicitly weaker goal

A lower bound with shrinking gap or varying rate can be informative even
when fixed-rate first-order length-exponent tightness remains out of
reach. The existing interval constructions already demonstrate strong
inverse-gap list growth below characteristic Elias. Their parameter ledger
should be compared directly against the current theorem's hypothesis and
constants, rather than described as evidence for a fixed-rate exponent.

A useful target would separate dependence on characteristic, gap and
length in one explicit regime, or force a lower bound on a uniform
all-rate prefactor. Allowing rho to approach0 or1 does not establish
fixed-rho tightness, because the theorem's hidden constant may depend on
rho. Merely moving a known capacity source toward high rate with common
zeros must not be treated as crossing the first-order curve.

**Test/stop:** solve the exact parameter inequalities symbolically first.
If no regime lies inside the current first-order hypothesis with controlled
rate constants, label it a capacity/parameter-dependence result and stop
selling it as first-order tightness. No new search is justified without a
specific stronger quantified statement.

## Work to stop or sharply limit

1. Further refinements of standard-support method-cost converses. They are
   now a useful completed secondary result, not the main intrinsic target.
2. Larger sparse split/nonsplit torus scans absent a mechanism that scales
   list size and crosses the actual affine first-order threshold.
3. New Wronskian solution counts without an agreement mechanism. Candidate
   count sharpness is already established; it did not yield proximity
   sharpness.
4. Padding/fiber compositions that preserve a fixed source list, and
   resweeps of independent product constructions already bounded in the repo.
5. Repeated lifting of the exact obstructed p41 bank, or treating a smooth
   finite seed lift as a growing-list construction.

## Suggested allocation

One agent should pursue route1's triangular recurrence and actual-agreement
classification, while a second independently audits it and looks for the
broadest valid hypothesis. A separate agent can work on the benchmark's
actual incumbent certificate; that is a different objective from intrinsic
DKT tightness. The root should synthesize the resulting mathematical
claims and decide whether route1 merits expansion. Do not use every agent
on variations of the same already-bounded family.
