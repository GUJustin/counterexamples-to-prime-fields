# Independent audit of the three principal results

**Priority update:** The deeper focused search in
[INTERVAL_PRIORITY_AUDIT.md](INTERVAL_PRIORITY_AUDIT.md) locates the exact
classical integer-moment pigeonhole mechanism. A fixed-weight, large-fiber
adaptation of Borwein--Erdelyi--Kos, Theorem 2.7 proof, plus the standard
locator bridge already gives the interval asymptotic exponent and the
below-Elias huge-prime corollary. The earlier section 2 assessment below
is superseded on that point: the interval result is a useful quantitative
coding consequence/refinement, not a new counting mechanism.

This is a bounded assessment against the primary sources below, not an
exhaustive priority search or a prediction of conference acceptance.
The current manuscript and its audited constructive proofs contain
substantial theorem statements. Their strongest case is the sharp
prime-field line geometry plus the stronger reciprocal-gap dependence,
not the quantity of appendices or the number of refuted numerical
variants. A better.codes improvement is neither established nor needed
to state these contributions.

## 1. Almost-complete prime-field coverage with genuinely far inputs

**Audited claim.** At every fixed rational rate, over every sufficiently
large prime, a constructed short domain has an exact affine-space distance
profile. Choosing r growing slowly gives n=Theta(log p log log p),
eta asymptotic to H_2(rho)/log_2 p, all p-1 nonzero parameters nearby,
and the exceptional point at distance1-rho-1/n. A derived line has TWO
endpoints almost eta/2 outside the tested radius and every other point
at exactly that radius. The radius is below characteristic-based Elias.

**Actual advance.** This is not just a larger constant in a known list
lower bound. It makes mixing almost surely nearby even when both input
words have quantified separation, and determines the full distance
profile. Pairwise disjoint decoding lists explain why witness switching
can defeat the inference from random mixtures to fixed common witnesses.
The efficient randomized domain sampler strengthens the existence story;
it should not be confused with efficient recovery of every witness.

**Closest checked comparison.** Krachun--Kazanin--Habock, Theorem1,
already give prime-field subgroup line/list obstructions with
eta=Theta(1/log n) and exp(Omega(1/eta)) nearby points. Their stated
polynomial-field parameters have p=Theta(n^beta), beta>tau+1, while the
certified number is n^(tau-o(1)); that fraction tends to zero. Their
multiplicative-subgroup domain and polynomial alphabet are advantages
our paired-domain construction does not retain. Thus our coverage and
separation are stronger, while its domain/field-size tradeoff differs;
we should not advertise “the first prime-field proximity-gap failure.”
Source: https://eprint.iacr.org/2026/782, PDF Theorem1 and Sections2--3.

**Classical ingredients versus theorem novelty.** Locator cancellation,
character estimates, Fourier energy, and random-translate completion are
classical ingredients (the manuscript properly credits Erdos--Renyi for
the completion strategy). The proposed new content is their quantitative
combination producing the exact distance profile, nearly maximal far
point, and almost-certain mixing of separated inputs. The elementary
far-input corollaries follow from that profile; they are not independent
technical breakthroughs.

**Scope that must remain prominent.** eta tends to zero. The theorem does
not invalidate established Johnson-regime guarantees, prove fixed-gap
prime-field superlinear exceptions, or give the same behavior on the
prescribed Circle STARK domain. It is a coding obstruction, not a full
protocol attack or an improved numerical security certificate.

## 2. Interval lists with almost-quadratic reciprocal-gap exponent

**Audited claim.** Integer intervals give exponential-in-n lists with
eta=Theta(1/sqrt(n log n)) and log p=Theta(sqrt(n log n)). Equivalently,
log L=Omega_rho(eta^(-2)/log(1/eta)); this rules out every uniform
exp(O_rho(1/eta)) prescription even when n=o(p), below Elias.

**Actual advance.** The exponent's dependence on the gap changes from
linear to almost quadratic. This is the cleanest quantitative separation
from the compared prescriptions. The particularly simple interval domain
and finite certificates make the statement easy to verify and explain.
It does not claim a matching upper bound, so “almost quadratic is
necessary” is justified; “the exponent is characterized” is not.

**Classical ingredients.** Equal subset moments, Newton identities,
leading locator coefficients, and conversion to Reed--Solomon lists are
old. Gandikota--Ghazi--Grigorescu explicitly develop the moments/decoding
connection for hardness. Rudra thesis Section6.4.3, Theorem6.10, constructs
prime-field lists by unions of multiplicative cosets: with p=aL+1, its
bank is binom(a,b), agreement bL, and dimension (b-1)L+1. At fixed rate,
its log bank is O(a)=O(1/eta). Neither checked theorem supplies the
interval exponent above. The likely contribution here is quantitative
integer moment counting and parameter optimization, not a new algebraic
connection between moments and decoding.
Sources:
https://arxiv.org/abs/1611.03069
https://cse.buffalo.edu/faculty/atri/papers/coding/thesis-chaps/chap6.pdf

**Scope and novelty risk.** This is a simple powerful counting proof,
which is a strength in exposition but warrants careful priority checking
in coding theory and additive combinatorics. Our bounded source check
supports a distinct parameter theorem; it does not certify that no older
interval moment-counting argument implies it. The gap shrinks and p is
superpolynomial in n. It is not a fixed-gap exponential-list theorem or
a theorem for polynomial-size alphabets. The hardness theorem cited above
is not itself a list-size lower bound and should not be described as one.

## 3. Quadratically many ordinary-CA exceptions at fixed gap over F_(p^2)

**Audited claim.** At exact rate1/8 and gap1/16, an unbounded family over
F_(p^2) has at least ceil(n^2/192) nearby labels and NO ordinary common
agreement at that threshold. The characteristic exceeds message degree
and the radius is below characteristic-based Elias. The extension degree
is fixed at two, while p grows.

**Actual advance.** This settles a qualitative intrinsic question in
this field class: no uniform o(n^2) ordinary-CA exception count can hold
at those fixed parameters. Ordinary CA is stronger than merely failing
full-support common witnesses, so the nearest-boundary argument matters.
Orbit descent turns an unbounded nearest orbit into a list linear in its
own domain length; exact-boundary preservation and the padding compiler
then turn it into quadratic exceptions. Random nonzero directions remove
the need for an additional extension. This is more than relabeling the
older full-support MCA construction.

**Classical ingredients versus new assembly.** The Dickson/character
source, root counting, orbit-stabilizer, interpolation, and probabilistic
padding are established tools. The proposed contribution is the true
nearest-source descent and ordinary-CA-preserving amplification at fixed
rate/gap and degree-two extension. Priority for the specific Dickson
list source is not established; the paper should avoid absorbing that
source into an unqualified novelty claim.

**Scope that changes the headline.** This is not a prime-ambient-field
result, not tightness of the current DKT first-order bound, and not a
lower bound forcing a gap-dependent polynomial exponent. Its agreement
is in the capacity regime; the first-order curve is a different target.
The conclusion is that a quadratic length dependence is necessary in
a large-characteristic class including quadratic extensions, not that
the known upper bounds are tight in all parameters.

## Strongest coherent message

A defensible opening is:

“Even over prime fields and below Elias, two quantitatively far
Reed--Solomon words can have every non-endpoint affine mixture nearby.
Moreover, uniform list bounds need an almost-quadratic, rather than
linear, exponent in the reciprocal capacity gap.”

Then present the fixed-gap quadratic ordinary-CA theorem as a separate
intrinsic limitation that survives in degree-two extensions. Combining
these into an undifferentiated “all proximity gaps fail” would weaken
the paper by erasing precisely the quantifiers it has worked to audit.

## What would most improve the venue case?

For a broad theory audience, the strongest missing theorem is fixed-gap
superlinear ordinary-CA exceptions over PRIME ambient fields, or a
first-order-regime intrinsic lower bound. Either would remove a central
remaining qualifier and address a structural open problem, rather than
merely improve a numerical coefficient. These are substantial new
research targets, not necessary prerequisites for making the current
paper e-printable.

For a cryptographic audience, the most valuable additional result would
connect one of the new obstructions to the prescribed protocol-relevant
evaluation domains or to a complete concrete parameter calculation.
The present abstract-domain results and finite circle examples should
not be conflated with that missing bridge. A better.codes improvement
would be useful evidence but would not substitute for the bridge.

Before expanding the theorem inventory further, the immediate highest-
value work is a precise theorem-by-theorem comparison with KKH and the
older list literature, independent external mathematical review, and a
focused presentation of the three claims above. They provide a legitimate
basis for considering STOC/CRYPTO as targets; no bounded literature audit
can responsibly turn that into an acceptance forecast.
