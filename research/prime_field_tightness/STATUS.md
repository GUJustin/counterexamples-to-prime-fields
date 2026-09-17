# Prime-field upper-bound tightness: target and evidence

September 17, 2026. User priority: assess and pursue tightness of the
Dao–Kominers–Thaler prime-field proximity-gap paper. Work horizon extended
to 18:00 Eastern (22:00 UTC). This note separates established results from
research targets. No intrinsic fixed-gap superlinear lower bound is claimed.

**Current authoritative comparison:** EPRINT_2056_COMPARISON.md, from the
public145-page ePrint retrieved September17. It supersedes the older
105-page version7 comparison and the historical notes below. Current
first-order inverse-margin powers are2 for lists and4 for MCA.

**Positive intrinsic comparison:** The prime-field Dickson family already
forces linear list size at a fixed gap. QUADRATIC_EXTENSION_LOWER_BOUND.md
now spells out its strengthened consequence: at least ceil(n^2/20)
full-support MCA exceptions over F_(p^2), rate1/8 and gap1/16, with
p=n/2+1>k-1. Thus a linear capacity MCA theorem is impossible in the
current ePrint's full large-characteristic field class. This is NOT a
prime-ambient-field result and is below the first-order regime. Historical
statements below about missing superlinear examples refer to the prime
ambient-field target. The main manuscript now makes this distinction.

## Three different meanings of tightness

1. **Intrinsic exception count.** At fixed rate rho and fixed positive
   capacity gap eta, make block length n unbounded and force at least
   n^{g(eta)} exceptional labels on a single received line. The preferred
   stronger hypothesis is no correlated agreement at the threshold, so
   every nearby label is exceptional for both CA and full-support MCA.
   A result with g(eta)>1 would already go beyond our current prime-field
   constructions. Growing g(eta) would begin to address the polynomial
   exponent in the upper bound.
2. **Dependence of a linear coefficient on the gap.** We already prove
   C_rho(eta)n exceptions at every sufficiently small rational eta, with
   log_2 C_rho(eta) >= (H_2(rho)^2/2-o(1)) /
   (eta^2 log_2(1/eta)). This forces large constants, but is compatible
   with a linear-in-n theorem having sufficiently large constants.
3. **Sharpness of intermediate proof steps.** The actual regular
   differential solution locus has an O_d(D^{d+1}) isolated-point bound
   and an attaining Theta_d(D^{d+1}) family. Those attaining solutions
   have only O_{d,eta}(1) nearby labels on any one received line at fixed
   gap. Thus algebraic enumeration is tight before filtering by agreement,
   but need not be tight after filtering. Independently, a restored draft
   proves optimality of a first-derivative interpolation support method.
   It is a method limitation, not an intrinsic code lower bound.

## Recovered references and version caution

- Public source checked September17: Scott Kominers's mathematics page
  lists *Reed-Solomon Codes Beyond Johnson: Efficient Decoding and Smaller
  Cryptographic Proofs*, with Q. Dao and J. Thaler, as a2026 working paper:
  https://www.scottkom.com/research/mathematics/ . That entry has no paper
  link. This confirms a public title, not the contents or identity of the
  latest draft; the precise coauthor theorem comparison still relies on
  recovered excerpts below.
- Archive `rs_capacity_tr26164/starkware/CONTEXT_STARKWARE_2026-09-05.md`,
  section F, quotes an abstract titled *Reed–Solomon List Decoding and
  Mutual Correlated Agreement up to Capacity*, attributed there to
  Dao–Kominers–Thaler–Zheng. It states n^{O_eta(1)} lists and a sufficient
  derivative order ceil(exp(6.76/eta)). The complete current theorem
  statement has not been recovered from this excerpt.
- Archive `mca_exponent_one/paper/first_order_support_optimum_2026-09-13/`
  cites *Quantitative RS List Decoding and MCA: From Johnson to Capacity*,
  Dao–Kominers–Thaler, supplied file `rs-capacity-and-correlated-agreement
  (9).pdf`. This is probably a newer version, but version identity and
  exact upper-bound exponents must be checked, not inferred.
- The latter restored draft claims exact quarter-rate method threshold
  a_0=(3+sqrt(133))/31, including a finite-multiplicity converse and a
  translation-stable nonmonomial extension. It has not been independently
  re-audited in this takeover. Do not advertise it as a newly proved result.

## Why the existing strongest counterexamples do not answer item 1

The full-coverage, unique two-orbit, and generic endpoint examples have
eta tending to zero with n. The upper-bound constant and exponent may
both depend on eta. Consequently neither p nearby labels at shrinking
eta nor exp(O(n)) labels at eta=1/n force any superlinear exponent at one
fixed eta. Explicit finite examples, even with enormous ratios against a
specified conjectured formula, do not resolve that quantifier issue.

The fixed-gap anchored lift holds its finite seed fixed and grows fiber
size B. Its count L(Br+1) is linear in n=B(m+r), because L is fixed.
Allowing the seed to grow also changes the gap unless an entirely new
fixed-gap seed family is supplied. Repeating the same lift does not
multiply exponents for free.

## A useful elementary obstruction to bank amplification

Fix one candidate polynomial P and a received line f+zg on n coordinates.
Let h(P) count persistent agreements: g(x)=0 and f(x)=P(x). At every
coordinate with g(x)!=0, there is exactly one label z that agrees with P.
If h(P)<A, each label with at least A agreements consumes at least A-h(P)
of these coordinate-label incidences. Therefore the number of such labels
is at most floor(|supp(g)|/(A-h(P))). If h(P)>=A, the candidate is nearby
for every z but already explains the persistent agreement set with zero
direction polynomial; this is not automatically an MCA failure.

For a finite bank of L candidates all having h(P)<A, the union of nearby
labels is at most L*|supp(g)|, and if h(P)<=A-delta*n for every candidate,
it is at most L/delta. Thus obtaining n*L amplification requires candidates
already within O(1) coordinates of the agreement threshold. This is exactly
what anchored padding exploits. It does not supply a growing fixed-gap L.

## Next investigations

- Obtain the current upper theorem and compare separately its list bound,
  CA/MCA exceptional count, derivative order, and finite-length threshold.
- Seek a fixed-gap bank with unbounded L over superpolynomial prime fields, or a challenge-dependent family
  whose agreement geometry escapes the persistent-bank obstruction.
- Test any proposed algebraic isolated-solution family against one common
  received line before investing in larger solution counts.
- Keep additive-subspace constructions in small characteristic separate:
  their growing-exponent staircase does not automatically transfer to
  prime fields as n grows.
- A proof that large classes actually have O_eta(n) exceptions would be
  evidence against expecting the existing general exponent to be tight.
  The restored exponent-one program has substantial subclasses but no
  general theorem; its unresolved nonbase-residue case must stay explicit.

## More precise recovered theorem comparison

`mca_exponent_one/rounds/R1_UHD1_PROMPT.md` records the supplied paper's
order-d transfer as list size C_L n^d and full-set MCA count C_E n^{d+1}
for fixed interpolation parameters; d=1 gives quadratic exceptions,
d=2 cubic, etc. `R4_AS_PROMPT.md` quotes the then-current first-order
bound O(n^2/(q eta_1^4)) beyond Johnson, and an O(n/(q eta_0^3)) bound
above Johnson. These are recovered excerpts, not a reread of the PDF.

`research_night_2026-09-13/OPT_FULL_PAPER_PROMPT.md` states the owner's
precise earlier target: for arbitrarily large fixed c, find a fixed gap
eta>0 and an infinite family over prime p=n^{omega(1)} with more than n^c
exceptional scalar challenges on one received line. It explicitly permits
chosen domains and characteristic-zero constructions followed by reduction
at arbitrarily large splitting primes. This is the right intrinsic target.

The current isolated-locus theorem exactly matches the intermediate
n^{d+1} algebraic exponent, but its agreement-filtered lower-bound family
does not match the transfer theorem's exceptional count. This is affirmative
proof-step sharpness alongside an explicit obstruction to inferring
intrinsic sharpness from it.

The archive's `OPT_FULL_PAPER_RAW.md` already proves a same-length
projective compiler: an L-element list of degree<K polynomials at A>=K
agreements can be separated by a Mobius change of domain, then compiled
to L distinct MCA-bad challenges at dimension K-1 and the SAME agreement
threshold. For a complete source list each nearby challenge is unique.
Thus a growing fixed-gap list over sufficiently large prime fields is a
concrete sufficient route;
reproving this compiler is not new progress. Appended-coordinate compilation
can gain another factor n with an explicitly accounted gap dilution.

## New scoped theorem, September 17

`RATIONAL_ENVELOPE.md` and `rational_envelope.tex` prove a linear
full-support MCA bound for arbitrary families with one fixed rational
normalization (P-S)/R=a/b of residual numerator/denominator degree at most r.
If R has h domain zeros, A-h>=beta*n, and n>=48r/beta^3, the count is
at most16(n-A+1)/beta^3, in EVERY characteristic. It applies to arbitrary
logarithmic-derivative residue banks of bounded denominator degree, not
just the fixed residue alphabet in the isolated-sharpness construction.
This is a scoped upper bound and an obstruction to lower-bound mechanisms,
not an unrestricted improvement of the user's prime-field theorem.

The proof was manually checked in this session, including the sharp
n-A+1 bad-label bound for a polynomial pencil, reduction at denominator
zeros, and the distinction between scalar labels and candidate pairs.
Exact tests passed220 rational triple determinants and all field labels
for a pencil attaining13 bad labels at n20,A8. No independent human or
separate-agent review has occurred. The manuscript includes the result.


## Full-length lists are already unbounded: essential field-size qualifier

The manuscript's `research/dickson_fixed_gap/comparison.tex` already gives
n/2 list elements at fixed rate1/4 and gap1/8 when n=p-1, p=1 mod8.
Consequently an unqualified claim that no growing fixed-gap prime-field
list is available would be false. The unresolved list route needs large
prime fields relative to length, sufficient to separate/compile labels
and make an n^{1+epsilon} MCA count possible. On n=p-1, there are only
p=n+1 scalar challenges in the original prime field, so a superlinear
exceptional-label count is impossible by cardinality alone.

This full-length construction uses exponent (p+1)/2 and quadratic
characters. Enlarging the field to an extension preserves the base-field
identities but does not produce a prime field. Reducing its integer
coefficients modulo a different larger prime does not preserve the
character identities. No characteristic-zero or large-prime lift is
currently proved. Shortening also does not automatically help: the
candidate degree is (p-1)/4-1, requiring length Omega(p) at positive rate.

## Stronger rational-path rigidity, 12:43 UTC

`RATIONAL_PATH_RIGIDITY.md` proves that a rational candidate path T(X,Z)
of challenge degree at most h has at most(8h+10)n/(A-D) nearby labels,
unless it is an affine polynomial path U+ZV. The affine path has at most
n-A+1 full-support bad labels. No X-height or characteristic guard is
needed. The proof counts persistent received-coordinate identities and
noncollinear polynomial triples, handling specialization base points.

Thus at fixed positive gap a NON-affine bounded-degree rational path has
only a CONSTANT number of nearby labels. An explicit projective-path
construction shows the inverse-gap scale is necessary. Exact checks at
n160/320/640, rate1/4 and gap1/8 verify respectively41/81/161 polynomial
members but precisely10 nearby full-support bad labels. These are path
counts, not a census of all RS codewords.

TheoremI.5 and CorollaryI.6 are now in the manuscript. Any rational formula
selecting witnesses at L>n-A+1 bad labels has challenge degree at least
(A-D)L/(8n)-5/4. The complete-coverage construction therefore requires
Omega(eta*p)=Omega(p/log p) degree for a global rational witness formula.
This is not a computational hardness claim and does not prohibit branching
decoders. It quantifies the failure of low-degree witness coherence.

## General cyclic boundary route audited, 12:54 UTC

CYCLIC_BOUNDARY_GENERAL_ORDER.md extends the restricted boundary-word
list bound to arbitrary cyclic domain order. At fixed eta=(A-K)/n,
the complete list is at most 2^{sum_{q|n,q<1/eta}phi(q)-1} in
characteristic zero, and for split primes p>n^{125/eta^3}. Thus this
particular route cannot yield growing fixed-gap lists over superpolynomial
prime fields. The restriction deg W<=A is essential. This is not a
general RS upper bound or an unrestricted nearby-line bound.

Exact checks passed all subset classes on six domains of sizes6 through20,
their independent finite-field moment classes, and44850 uniform-exponent
inequalities. Proof locally audited only; no novelty claim. Kept as a
research note rather than expanding the manuscript with another restricted
obstruction.

The boundary-value amplification route was reread. It currently uses an
extension field to separate padding-coordinate labels; base-field evaluation
points do not make its challenge field prime. In addition, unbounded value
diversity is unproved. It therefore does not yet answer the user's
prime-field exponent-tightness question, even conditionally on list growth
alone. The main open milestone remains superlinear exceptions at one fixed
positive gap in sufficiently large prime fields.

The projective-envelope note can now replace its projective-pencil bound
by max(n-A+1,18n/(A-D)), improving its constants and high-agreement dependence.
The earlier rational-parameter height reconstruction note is auxiliary and
not needed for the stronger rigidity theorem. No intrinsic fixed-gap
superlinear lower bound or universal prime-field improvement is claimed.

## Exact-parameter list amplification, 13:03 UTC

PRIME_BOUNDARY_AMPLIFICATION.md and list_amplification.tex make the
existing appended-coordinate compiler quantitative over the SAME prime
field. An arbitrary L-element source list at length N, dimension k,
agreement A>=k+1, over p>=2N+1 gives length2N, dimension k, threshold A
and at least ceil(p*A*L/(p+3*A*L)) full-support MCA-bad labels. Thus
rate and gap are EXACTLY halved, and the count is Omega(min(NL,p)) at
fixed source parameters. No source boundary/maximality hypothesis is
needed for full-support failure. Ordinary correlated agreement may
still exist, and a far point is not asserted.

This clarifies the tightness target: source lists N^c would force full-
support exponent c+1 when the field does not saturate the count. A
universal linear full-support theorem would imply constant fixed-gap
lists whenever p/N tends to infinity. No converse is proved, and no
new growing source list has been found. This is an application of the
already-used anchor/averaging mechanism, not a novelty claim.

For source lists attaining the maximum possible agreement M, the note
also proves ordinary-CA failure with q<=M-k+1 padding points, at the
same averaged union bound. This removes the extension-field dependency
from the boundary-value note but cannot overcome the p=O(N) cardinality
obstruction in the existing Dickson family.

The new checker exhausts source lists, padding translations, quotient
identities and all joint witness pairs in small fixtures. Exact scaling
is checked at N5->10 overF101 and N10->20 overF23; the latter checks
field saturation. Some fixtures explicitly have ordinary CA alongside
full-support failures. The manuscript includes the exact-scaling
proposition and an introduction paragraph explaining its conditional role.

## Higher binomial sections: arbitrary-subset obstruction, 13:35 UTC

The120-case two-coset scan produced only a finite full-length tradeoff,
not a short-domain source list. The subsequent locally audited proof in
research/two_coset_candidate_lists/BINOMIAL_BRANCH_BOUND.md now bounds
EVERY subset of that binomial-section orbit, not only subgroup or two-
coset subsets. For r>=3 and n<=c*k, more than k agreements force
L<=2^20*r^3*4^r+24*c*(r*2^r+1). Fixed r therefore cannot support
growing above-capacity lists in this family. The exceptional r2,j1
quadratic/Dickson mechanism remains valid.

The bound is exponential in r and does not rule out r growing at least
logarithmically with L. This remains a restricted-family obstruction,
not a universal prime-field list theorem or exponent-tightness result.
It suggests moving beyond fixed-index binomial-section mechanisms.
The proof combines a radical-branch classification, a conservative norm
degree bound, and multiplicative-character Fourier mixing. Its external
Weil estimate was checked against Sárközy–Sárközy Lemma2.

Exact checks:26 root-filter/constant-mask/residual-fiber fixtures and
26104 sign-pattern coefficient checks pass. Fourier diagnostics are
floating point and are not used as proof certificates. The manuscript
remains157pages; this family-specific result is kept in research notes.

## Ordinary CA and unique nearby points from nearest lists, 13:45 UTC

UNIQUE_BOUNDARY_AMPLIFICATION.md extends the interpolation-pool compiler
to arbitrary source words and arbitrary padding sizes, using a union
bound to exclude every outside-pool candidate at every scalar label.
Let a source word on N points have maximum agreement M>=k+1 and complete
nearest list L. With U candidates at an intermediate threshold T,
k+1<=T<=M, the explicit sufficient conditions are

    p>=N+q+(k-1)*binom(U,2),
    (q*U+binom(q,2)*U^2)/p+binom(N+q,M+1)/p^(M+1-T)<1.

The output line has EXACTLY qL nearby labels, each with exactly one
nearby codeword and maximum agreement M+1. Every other label, including0,
has maximum agreement M. This implies ordinary-CA failure, but only a
one-coordinate far/near separation. It is not a global list-size bound.

For q=N, rate halves exactly; gap becomes eta/2+1/(2N), not exactly
eta/2. With polynomial U at a looser fixed-gap threshold and
p=N^{omega(1)}, the hypotheses hold eventually. Importing such a bound
on U from a capacity list theorem is an explicit external dependency.
An exponential-in-N sufficient field cutoff is available without it.
The missing source now is a growing NEAREST list; arbitrary lists are
insufficient for this ordinary-CA version.

Complete line replays pass overF263 andF2003, including a source of
interpolation degree6 but maximum agreement3. They give exactly10 and21
unique nearby labels. All343 offsets in a separate small F7 fixture are
also exhausted. Main-paper length stays157; the compiler is kept in the
research notes pending a growing source family.

## Free-domain Dickson pilot completed, 13:55 UTC

research/dickson_domain_deformation/README.md records both prescribed
fixtures, with independent stdlib certificates. At p17 the 32-equation
Jacobian has a 32-column minor of determinant1 modulo17; a saved first
correction also verifies modulo289. Hensel gives an all-orders finite
lift. Exhausting1820 determining supports gives source maximum agreement6
and nearest list22. Only8 selected candidates lift; they remain nearest.
A finite-type open-locus argument yields an algebraic-number realization
and arbitrarily large split-prime reductions. This is finite n16,k4,
not a growing fixed-gap family.

At p41 a left-kernel witness annihilates all240 Jacobian columns but
pairs to14 with the correction right side. Hence no unramified mod41^2
lift of this exact seed exists, even with all nodes free. Ramified lifts
and other seeds remain open. Independent verification does not assert
the generator's rank216; the direct obstruction is sufficient.
No expanded lifting census planned without a new symbolic reason.
Main paper stays157pages. Continue until22:00UTC,18:00 Eastern.

The follow-up SMOOTHNESS_METHOD_LIMIT.md explains why a full-row-rank
lifting census cannot meet the growing-list target. For L distinct
candidates, degree<k, selected agreements A_i and m covered nodes, the
eliminated incidence Jacobian has kernel dimension at least k+4: common
polynomial addition, scaling, and three projective node motions. Thus
left-nullity >= sum_i(A_i-k)-2m+k+4. At fixed gap full row rank requires
L*eta<=2-rho-4/n. This is a limitation of that certificate method only;
exactly dependent equations can still define a liftable smooth locus.
A scalable construction must control these dependencies explicitly.

## Generic fibers preserve complete nearest lists, September17

research/generic_fiber_nearest_lists/PROOF.md gives a locally audited
algebraic scaling lemma for ANY finite characteristic-zero received
word, without a received-polynomial degree restriction. Replace source
node a_i by all B roots of X^B=t+a_i over a transcendental t. Independent
Kummer rotations of each fiber imply every degree<Bk candidate with
at least B(k+1) agreements descends to Q(X^B-t), deg Q<k. Thus source
maximum M>=k+1 becomes BM, with exactly the same complete nearest list,
rate k/N, and gap (M-k)/N. Finite interpolation minors permit algebraic
specialization and reduction at arbitrarily large completely split
primes; no quantitative field bound. A positive-characteristic-only
seed cannot be transported to different prime characteristics this way.

Anchoring the degree B(k-1) variant and applying the unique-nearby
compiler gives EXACT fixed parameters n=B(N+r), K=B(k-1), A=BM and
exactly (Br+1)*ell uniquely nearby labels, where ell is the source
nearest-list incidence at the anchor. All other labels, including0,
have maximum agreement BM-1. The lifted Dickson seed gives, with r8,
rate=gap=1/8 and at least n+3 unique-nearby labels. This is linear and
not stronger than all existing fixed-gap constructions. The useful
change is applicability to arbitrary finite characteristic-zero seeds.
No growing list or exponent-tightness claim.

The stdlib checker exhausts210 and5005 determining supports for two
specializations (B2,F1009,t3 and B3,F10009,t53). Their complete nearest
lists have size2, maximum agreements6 and9. Noncomposed controls stay
below the theorem threshold. All checks pass under384MiB watchdog.
Main manuscript remains157pages; new lemma is retained in research notes.

A separate source check is recorded in PUBLIC_LIST_BOUND_SCOPE.md:
arXiv2609.08005v1's formal bounds are polynomial in q; do not silently
substitute that proof for the n-polynomial pool dependency over
superpolynomial prime fields. No claim of falsity of its informal
stronger statement. Current external dependency remains explicit.

## Complete profile strengthening, September17

Quadratic towers improve the generic fiber lemma: at length BN and
dimension Bk, B=2^s, EVERY candidate above Bk agreements is a composed
source candidate. All high-agreement counts scale exactly by B.
QUADRATIC_TOWER_PROFILE.md proves this using independent fiber swaps;
sharing h-1>=2k points suffices at each quadratic step. A complete finite
replay at n20,K8,F1000000007 examines125970 determining supports:
124980 distinct interpolants have agreement8 and exactly2 have12.
No candidate has agreement9,10,11 or above12. Verified under384MiB.

The p17 Dickson seed can also be sharpened to an EXACT characteristic-zero
profile. Its selected smooth incidence locus has16 free tangent directions.
All4368 five-supports split into4112 already inconsistent,48 belonging
to the selected8 candidates, and208 unwanted consistent supports.
Every unwanted residual has nonzero tangent derivative, independently
verified using a different interpolation and residual formula.
Thus one smooth characteristic-zero deformation avoids ALL208 residuals
simultaneously. It has exactly8 above4 candidates, each at6 agreements;
all others have at most4. See dickson_domain_deformation/EXACT_PROFILE.md.

Quadratic towers yield n16B,K4B,exact list8 at6B agreements and all others
<=4B. Anchoring where four candidates meet gives a pool of exactly4 at
threshold4B, so the unique-nearby compiler needs no external list bound.
With q8B+1 it yields n24B,K3B,A6B,rate=gap=1/8 and EXACTLY32B+4 uniquely
nearby labels; every other label has agreement6B-1. The compiler alone
requires only p>=32(8B+1)^2, but the source specialization may require
much larger split primes. Do NOT claim polynomial field size, growing
list size, superlinear exceptions, or constant far/near separation.
New results stay in notes; main paper remains157pages.

## Degree-growing scaled-power family excluded in characteristic zero

SHIFTED_POWER_LIST_BOUND.md proves that, on arbitrary complex nodes,
a fixed-exponent family (uX+v)^m has at most2 candidates through any
three prescribed values. The proof uses three independent Hermitian
magnitude equations and a quadratic determinant on their affine line.
Hence L<=2*binom(n,3)/binom(A,3), independent of the growing exponent m.
A common offset S and multiplier R give the corresponding bound after
removing R-zero nodes; at positive capacity gap this is O(eta^-3).
The proof is locally audited, not independently reviewed; no novelty
claim. It covers a growing-degree family missed by fixed residual-degree
bounds. Mixed exponents and candidate-dependent factors remain outside.
Characteristic zero is essential: an explicit full-field power family
violates the analogous finite-field bound below capacity. No uniform
large-prime transfer is claimed. The introduction already clearly states
our actual fixed-gap limitation and was left unchanged.

## Coauthor PDF recovered: update comparison before further tightness claims

The continuing Dropbox sync now provides version(7), modified Sep10,
105pages, by Dao–Kominers–Thaler. Direct statements are recorded with
SHA256 and page numbers in COAUTHOR_DRAFT_COMPARISON_2026-09-10.md.
First-order list O(n/eta_1^3), MCA O(n^2/eta_1^5); capacity sufficient
order ceil(exp(1.5/delta)), not the old6.76/6.88 excerpts. Lists and
exceptions have powers d,d+1; the draft also states deterministic
bit-complexity reconstruction without field enumeration. This version
is not asserted to be the user's latest; version(9) remains unrecovered.

At rate1/4 its first-order curve is (3+sqrt133)/31~=0.46879. Our new
agreement3/8 profile lies below that curve and does not test first-order
sharpness. Capacity gap delta and first-order gap eta_1 must stay distinct.
The exact-halving compiler may also leave the first-order regime.
Next concrete audit: restored first_order_support_optimum_2026-09-13/
main.tex and finite_and_spaces.tex, which claim method optimality at
that same quarter-rate threshold. No independent audit yet.

An older Sep5 Dropbox source already contains a DIFFERENT exact-eight
boundary construction at rate1/4,gap0.24. Mere list size8 is not novel;
our new exact-profile deformation has gap1/8 and no other candidates
above4 agreements. No source PDF or private draft has been committed
or published; local snapshot is in ignored tmp/recovered-coauthor-draft.

## First-order method optimality audited, September17

research/first_order_support_audit/AUDIT.md checks the restored Sep13
support-optimum note. At quarter rate, the specified leading
'dimension > n*saturated local rank' method has exact infimum
(3+sqrt133)/31. Every fixed finite multiplicity m needs agreement
strictly greater than that plus(1-2*a0)/(8m). The proof audit covers
rank, sorting, diagonal compression, quarter-rate cap optimality,
one-sided finite correction, and translation-stable nonmonomial
flat degeneration. It does NOT prove intrinsic bad-code behavior,
first-order n^2 optimality, or absence of globally dependent certificates.
That restored converse alone does not handle growing multiplicity; the subsequent exact finite-length extension below does so for the full-coefficient monomial model.

A fresh stdlib replay passes320 direct ranks,3750 rearrangements and
marginals,3128 exact polygon-integral finite inequalities, and two strict
high-rate improvement certificates. At rates.9 and.75, agreements.94778
and.86098 lie below the recovered DKT curve. Their enormous supports
and conservative challenge degrees320257184 and19137094352 give no
practical better.codes improvement. The full high-rate continuum
optimality theorem is not included in this audit verdict. No new discovery
credit claimed: these are restored statements now locally checked.
Main counterexample manuscript left unchanged at157pages.

## Uniform finite-length method converse added

New UNIFORM_FINITE_LENGTH_CONVERSE.md strengthens the restored quarter-
rate method result for the exact weighted full-coefficient monomial model.
For N divisible by4,N>=12,D=N/4-1, any multiplicity m and any downward-Y0
support with G>N*R must have
 A/N > (1-8/N)*(a0+(1-2*a0)/(8m))+8/N^2,
 a0=(3+sqrt133)/31.
Thus even m growing with N cannot lower the asymptotic threshold; only
O(1) agreement coordinates can be gained from finite-length corrections.

Key exact identity: at degree q, L_q=mA-(D-1)q, source dimension is
sum_u(L_q-u), and local rank is the usual sum of minima truncated to
ell<min(m,L_q). An injection proves G_q<=2R_q whenever L_q<m, so those
diagonals cannot help an N-times-local-rank count. Remaining diagonals
have saturated rank and are dominated by the audited quarter-rate
benefit at a_star=(AN-8)/(N(N-8)). No fixed-m limit is needed.
Fresh exact tests pass1920 direct cutoff ranks,32752 half-rank subsets,
and1920 reductions. Still no intrinsic list/MCA lower bound: global
coordinate dependencies and other source classes remain outside. The
nonmonomial finite-length extension has NOT been proved.

## Self-contained first-order technical note completed

research/first_order_support_audit/note/main.pdf is a separate 12-page,
11pt letter-format article with one-inch margins. It presents the audited
quarter-rate support converse, the new exact finite-length uniform-in-m
extension, the fixed-jet-space nonmonomial degeneration, and two exact
high-rate improvement certificates. It does not claim the full high-rate
optimum or intrinsic list/MCA tightness. The final LaTeX log has no
undefined references or layout warnings; all twelve pages were rendered
and visually inspected. Main counterexample paper remains 157 pages.

## First-order-preserving list amplification

FIRST_ORDER_PRESERVING_AMPLIFICATION.md removes a parameter obstacle in
the tightness comparison. With q new coordinates and unchanged output
dimension k, a list of L candidates at threshold A yields at least
 p*q*A*L/[N*p+(2*(k-2)+q)*A*L]
full-support MCA-bad labels, provided A>=k+1 and p>=max(2N,N+q).
Taking q=theta*N+1 preserves rate and agreement up to the exact common
factor1/(1+theta). Any strictly positive first-order margin survives a
sufficiently small fixed theta. Thus a source list of size Omega(N^c)
inside that regime would give Omega(n^(c+1)) full-support exceptions
at nearby parameters still inside the regime, for sufficiently large
primes. This is conditional: no growing source list is constructed.
Exact parameter certificates and four variable-padding finite fixtures
pass; every selected bad support was checked against all12167 possible
directions in the F23 fixture.

## Smaller high-rate certificates checked

The first-order technical note remains12pages and now uses smaller
certificates at the same agreements. At rate.9, multiplicity4096
uses1632467monomials and sufficient challenge degree241481265; at
rate.75, multiplicity65536 uses786044039monomials and degree16569483999.
Both improve the restored support size and conservative challenge degree.
An independent homogeneous-diagonal recount agrees with both original
column sums, after21295 checks of the summation identity. These remain
very large theoretical certificates, with no practical parameter claim.
See research/first_order_support_audit/SMALLER_FINITE_CERTIFICATES.md.

## Main manuscript: open-regime amplification integrated

Corollary4.10 now states and proves sparse-padding list amplification
inside any strict continuous agreement regime. The introduction points
to it when explaining the missing fixed-gap source-list target. The
main article still has157pages, letter format with1inch margins. Its
final build has no reference/layout warnings; the changed introduction
and corollary pages were rendered and inspected.

## Variable-degree generic tower obstruction

research/generic_fiber_nearest_lists/VARIABLE_DEGREE_TOWER_BOUND.md
extends the generic quadratic-fiber argument to arbitrary degree caps D
at n=B*N0. For threshold A>D, choose the largest power of two
C<=min(B,A-D). Every candidate descends through log2(C) stages, giving
 L<=binom(n/C,floor(D/C)+1)<=2^max(N0,2*n/(A-D)).
Thus a fixed seed cannot yield growing lists at a fixed positive capacity
gap even by varying the degree cap with tower height. This holds for the
generic tower and suitable algebraic/splitting-prime specializations,
not every special parameter choice or arbitrary RS domains.

An exhaustive20-node fixture at dimension5 has70candidates at threshold6
(64at6,4at8,2at12). All descend one step to exactly70quadratic interpolants
on the10-node intermediate word. All15504 determining supports and all
120residual triples checked. This is stronger scope than the earlier
dimension8 profile with only2high candidates, but still no growing list.

## Characteristic41 Dickson seed: all DVR lifts excluded

New research/dickson_domain_deformation/RAMIFIED_OBSTRUCTION.md closes
the ramified-lifting loophole for the exact20-candidate seed over F41.
After normalizing14 geometric freedoms (three nodes, one polynomial,
one coefficient difference), the274x240 Jacobian has rank230 and a
10-dimensional kernel. Ten certified left-kernel quadratic forms are
t_i^2+c_i*t_i*t9 (i<9), t9^2, so their common zero over any residue
extension is only zero. Another left-kernel combination kills the
quadratic map identically on the kernel but has constant obstruction8.
A valuation split2r<e,2r=e,2r>e excludes every mixed-characteristic DVR
lift, for every ramification indexe. The normalization preserves all
incidences via projective node change, weighted polynomial pullback,
common scaling and addition.

A separate stdlib verifier reconstructs the binomial seed and equations,
computes rank230, checks the14-dimensional gauge action, all kernel and
left-kernel identities, and605 quadratic coefficients. Both generator
and verifier pass below384MiB in about0.5seconds. This supersedes the
earlier 'ramified lifts remain open' statement for this exactseed only.
It does not exclude different subsets, incidence patterns, or primes.
The p17 positive lift is unaffected. No growing fixed-gap list is claimed.

## A ten-candidate characteristic41 subset does lift

SUBSET_LIFT.md and verify_subset_lift.py retain binomial labels
3,8,10,11,12,13,16,17,18,20. Their110x140 free-domain Jacobian has
a110-column minor of determinant29 mod41. A direct mod1681 correction
check preserves all selected supports. Hensel and algebraic specialization
give n40,k10,ten candidates each at15agreements over characteristic zero
and arbitrarily large splitting primes. No complete-list or maximum-
agreement claim is made. This is a fixed finite bank below the first-order
curve, not a growing-list result. It shows the all20 obstruction does
not exclude useful subsets; maximality of ten is not claimed.

## Classical prime-field coset attribution added

A targeted literature check found an attribution missing from the related
work: the Guruswami–Rudra prime-field multiplicative-coset construction
presented in Rudra's2007 thesis Section6.4.3. The original theorem pages
were inspected visually because PDF text extraction garbled the formulas.
CLASSICAL_COSET_SCOPE.md records the parameter comparison and scope.
The manuscript now credits that mechanism explicitly; it does not claim
that the older displayed family supplies growing fixed-gap lists. Main
paper rebuilt cleanly to158pages, with changed pages visually inspected.
The separate first-order technical note remains12pages.

## September 17: sharp inverse-margin powers for the first-order proof bounds

The new GAP_COST_CONVERSE.md and Section 7 of the 14-page technical note
prove that at quarter rate, for agreement a0+epsilon, arbitrary positive-
surplus downward-Y0 monomial supports require m=Omega(1/epsilon), both
jet degrees Omega(1/epsilon), and rank/surplus >=1/(8epsilon). Hence the
unchanged uniform challenge count needs Omega(1/epsilon^2), and the
recovered DKT interpolation-plus-reconstruction budgets necessarily cost
Omega(D/epsilon^3) for lists and Omega(D^2/epsilon^5) for MCA. These match
the draft's upper margin powers within that specified framework. They do
not lower-bound actual lists, exceptions, or all possible first-order
proofs, and are leading-normalized rather than uniform finite-length
claims. Exact checks passed for 3743 arbitrary supports, the narrow-cap
inequality, and three positive-surplus fixtures. The technical note builds
without warnings and its new pages were visually checked.

## September 17: nonmonomial cost extension and GitHub synchronization

The inverse-margin cost theorem now also covers the audited fixed
translation-stable nonmonomial jet-space class. Both flat degenerations
preserve separate jet-degree bounds; deleting nonpositive-benefit
monomials preserves benefit and lowers rank. Monotonicity of R/(B-R)
transfers the ratio bound. 504 direct finite-field rank comparisons pass,
including 196 strict drops. The technical note remains 14 pages, builds
cleanly, and the updated page was visually checked.

The user explicitly instructed keeping the current paper pushed to
https://github.com/GUJustin/counterexamples-to-prime-fields. This supersedes
earlier local-only/no-push working assumptions. Keep verified manuscripts,
sources, and certificates synchronized; do not upload ignored temporary
files or recovered third-party manuscripts. The remote main was checked
at the original baseline 540a9853b2c392a898697595a4bc263f7796ef11, so the
current research branch can fast-forward it.

Live better.codes checked September 17: interval 68.11--116.13 bits; no
improvement from this work. Method tightness does not resolve the
prescribed-domain and extension-field transfer obstacle.

## September 17: exact finite-length margin-cost extension

FINITE_LENGTH_GAP_COSTS.md and Corollary 7.4 of the now 15-page technical
note transfer all four cost inequalities to exact full-coefficient
monomial sources. With a*=(AN-8)/(N(N-8)) and epsilon*=a*-a0, the
rank/surplus bound follows by deleting nonpositive-surplus diagonals and
comparing the retained benefit. This is uniform in multiplicity. At
A=ceil(N a0), it forces multiplicity Omega(N), challenge budget Omega(N^2),
and unchanged list/MCA budgets Omega(N^4), Omega(N^7). These remain proof
framework costs, not intrinsic code lower bounds or a benchmark gain.
Exact verifier passed 6750 reductions, 1054 positive-surplus ratio
comparisons, and one near-critical positive length-one-million fixture.
The note builds cleanly and the new page was visually inspected.

The preceding GitHub main update was verified at
86facc474c40d8edbe463de6721b99233cf7d5b1, with both manuscript PDFs and
their principal sources matching remote blob hashes. Continue pushing
verified updates, as explicitly requested by the user.

## September 17: full-row lifting test cannot yield growing fixed-gap banks

New research/dickson_domain_deformation/FULL_ROW_LIFT_LIMIT.md proves a
necessary condition for the uncompressed incidence Jacobian to have full
row rank. With c covered nodes, L distinct degree-<k candidates and
agreement counts A_i, the k common additions, one scaling, and three
projective coordinate motions give k+4 independent kernel directions.
Thus sum_i(A_i-k)<=2c-k-4 is necessary. At fixed capacity gap eta this
forces L<2/eta, independently of length. Consequently searching for larger
full-row-rank seeds cannot solve the growing-list target. This does NOT
exclude lifts with dependent equations, smooth reduced loci with redundant
presentations, or singular lifting.

The full p41 seed has44 row dependencies, at least34 forced by this count;
the additional10 correspond to the normalized tangent directions used in
the separate second-order obstruction. Exact matrices and all geometric
motions checked for the p17 bank, full p41 bank, liftable ten-candidate
subset, and a two-candidate subset with uncovered nodes. Next intrinsic
construction work must handle compatible equation dependencies rather
than merely enlarge the existing full-row minor search.

## September 17: high-rate support shape audited over an interval

The restored high-rate shape theorem is now independently audited and
included in Section 8 of the 17-page technical note. For rho>1/2, the
optimal decreasing endpoint is min(a/rho,(2a-1-s)/(2rho-1)), with prefix
width optimized in [0,(a-rho)/(1-rho)]. The exact surplus adds
rho*(B-(a/rho-1))_+^3/(6*(2rho-1)) to the old cubic cap polynomial.
The proof completes/deletes columns according to the signs of three
affine densities; it does not rely on numerical optimization.

A simpler untrimmed-cap argument already proves a strict improvement
over the recovered DKT curve at every rate 8-3sqrt(6)<rho<1: its rank
truncation adds (B0-(a/rho-1))^3/12>0 at the old threshold. Continuity
and lattice approximation give finite certificates at a smaller agreement.
This is recovered mathematics newly audited, not a new discovery claim.
The explicit optimized-threshold cubic and its asymptotics have not yet
been included in this audit verdict.

Independent verifier passed 220 exact rational polygon integrals and
4851 endpoint comparisons, plus positive examples at both certified
rates. The note builds without warnings; new theorem/proof pages were
rendered and inspected. No practical parameter or better.codes gain is
claimed.

## September 17: explicit high-rate curve and renewed intrinsic priority

The restored explicit high-rate continuum threshold is now audited in
Theorem 8.3 of the 18-page technical note. Existence of an interior
optimizer forces a definite square-root sign and the largest cubic
root; the proof does not merely select a numerical branch. Three exact
symbolic identities and six rational branch isolations pass, with
agreement intervals narrower than 10^-28 and admissible support widths.
The note builds without warnings; new pages were visually checked.
This remains continuum method tightness, not intrinsic code tightness.

The user specifically asked about intrinsic or spiritually meaningful
tightness of https://eprint.iacr.org/2026/2056.pdf. Direct web retrieval
failed and HTTPS download returned403; no copy was recovered by the
filename lookup. Do not claim this current ePrint has been read. The
comparison remains the recovered September10 version7. Our large
gap-dependent coefficient in a linear-n lower bound rules out easy
uniform gap dependence, but neither forces the first-order quadratic
exception count nor an n exponent growing toward capacity. Method
optimality must not be presented as a substitute. Prioritize a growing
fixed-gap list or superlinear fixed-gap exception construction next.

## September 17: intrinsic binomial search and the Dickson first-order barrier

Primes p comparable to n are sufficient for intrinsic list-size tightness;
the large-prime condition belongs to the superlinear exception compiler.
The new binomial_first_order_search tests273 full candidate banks over
seven primes; their modal words produce no three-candidate hit above the
first-order curve. This finite search is not a subbank optimum.

A separate character-mask proof handles the r2,j1 family excluded from
the earlier higher-section bound. For every arbitrary L-subset of one
Dickson orbit on F_p^*, minimum agreement is at most
1.5k+4Lambda+8Lambda*sqrt(k/L)+36k/L+1, Lambda=8(sqrt(p)+3). The
complete bank consists of two twisted orbits. Therefore fewer than2^22
complete-bank members can simultaneously lie above the first-order
quarter-rate curve, uniformly in p. This is a restricted-family barrier,
not a general constant-list theorem, and does not treat punctured domains.
Exact character branches and orbit identities pass at eight primes.
Next intrinsic search should change the polynomial family or domain
substantially rather than merely optimize words on this full-domain bank.

## September 17: CURRENT EPRINT RETRIEVED; quantitative comparison corrected

The public145-page ePrint2026/2056 was successfully retrieved using the
normal download query after plain URL403. SHA256
b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a.
Read-only snapshot stays ignored under tmp/eprint-2056. Current source
comparison is EPRINT_2056_COMPARISON.md, superseding version7 for theorem
statements. Theorem1.1 has eta1^-2 lists and eta1^-4 MCA, not the older
eta1^-3/eta1^-5. Proposition5.10 has graded challenge counts, and the
capacity characteristic guard is p>k-1. Page47 already acknowledges the
high-rate curve refinement. Do not present our old-budget converse as
current-theorem tightness or the high-rate refinement as absent from
the current paper.

The note abstract and first-page notice, legacy cost statements, README,
and comparison documents now make this distinction explicit. Main paper
related work now cites the public ePrint and states the missing intrinsic
lower bounds against its correct powers. Whole145-page proof and Lean
formalization have not been independently audited here. The user's
intrinsic tightness target remains unresolved.

## September 17: qualitative intrinsic comparison and puncturing audit

The existing full-length Dickson list already gives a linear intrinsic
list lower bound at a fixed gap over prime fields. Its combination with
the anchored compiler over F_(p^2) now gives a concrete quadratic
full-support MCA corollary: n=2(p-1), rate1/8, gap1/16, and at least
ceil(3n^2/100) exceptional labels. The characteristic exceeds k-1. This
excludes a universal linear capacity MCA bound in the full field class
of the current ePrint, but is not a prime-field scalar-label result and
does not reach the first-order regime. No novelty claim for this direct
combination of established ingredients. Exact extension-field replays
give63 certified labels at p17,n32 and358 at p41,n80; these are lower
bounds, not exhaustive counts of all exceptional labels. The manuscript
now states the corollary and the correct positive partial comparison.

The restricted Dickson family barrier also extends to arbitrary domain
puncturing. The baseline average agreement is at most
min(n/2,n/4+k/2), plus the existing spectral error. Fewer than2^23
complete-bank candidates can exceed the audited first-order threshold
on any such domain. Three symbolic identities and15147 exact domain
counts pass. This is another family-specific obstruction, not a general
list theorem or a new lower bound. It is kept in research notes.

The main paper builds to159pages, retaining11pt letter and1inch margins;
the altered introduction and both corollary pages were visually checked.
No better.codes improvement and no superlinear fixed-gap prime-field
exception construction has been obtained. Continue until22:00UTC.

## September17: expanded polynomial search and finite-count calibration

research/projective_dickson_search/ now records complete scalar/projective
and affine-output orbit searches at p17,41,73. The latter gives14,20,36
candidates at agreement3n/8; no first-order-regime witness appears in
these searched families. Independent coefficient expansion replays134
certificates, and a separate complete p17 list/orbit comparison confirms
22 total nearest candidates versus8/14 from the searched orbits.

One million determining-support samples at p41 discovered202 candidates
with15 agreements. Independent Vandermonde reconstruction and closure
under the exact mu10 symmetry certify210 degree-nine candidates in21
orbits. This is a finite lower bound, not a complete list or a family.
The exact random-word expected count at these parameters is194.86, so
the numerical size alone is weak evidence of asymptotic growth beyond
the explicit Dickson bank. None of the21 support classes lifts while
keeping the same40th-root-of-unity nodes and quartic-character word:
nonzero residuals at other split primes exclude those fixed cyclotomic
lifts. Arbitrary deformations remain untested.

The finite certificates and calibration are retained as research evidence;
no manuscript expansion or new asymptotic claim. Larger random-support
sampling has rapidly vanishing hit probabilities and is not the next
route. Continue searching for a structurally different growing family,
with the prime ambient-field condition enforced. Work horizon22:00UTC.

## September17: exact characteristic-zero cyclic-word test

research/cyclotomic_dickson_word/ tests W=(X^k-1)^2/2 on mu_(4k)
directly in characteristic zero. A (k+1)-point agreement support is
equivalent to h_k(S)=2. Exhaustive split-prime filtering followed by
integer cyclotomic reduction gives complete above-capacity list sizes
0,0,3,0,0,9,28 at lengths4,8,12,16,20,24,28. Independent exact
cyclotomic-field interpolation verifies every resulting polynomial and
reconstructs every retained support. At n12 and24, the agreements are
4 and8, respectively, so both have fixed gap1/12 and rate1/4.

The apparent3-to-9 growth does not continue in the tested shared-zero
class. Exhaustive residual interpolation with at least2r zero-word
agreements at n12r,k3r,A4r gives3,9,3,9 witnesses for r1,2,3,4.
All lift exactly and descend by composition to length12 or24. The n36
and48 searches are not complete unrestricted lists. No asymptotically
growing family is established. The main paper remains159pages.

Live better.codes still reports68.11--116.13 bits. A fresh primary-source
search found the current przchojecki/rs-mca repository synthesis, but
its additional claimed finite parameter results have not been audited
here or imported. The earlier pinned paving-source audit remains the
only checked claim from that project in our literature notes.

## September 17: Dickson difference splitting follow-up

Exhaustive exact factorization of all 2,922 pairwise source differences at
p17,41,73,89,97 found only linear factors, with multiplicities one or two.
This implies collision-free extension-field evaluations for these banks.
A general theorem would sharpen the quadratic MCA constant via exact
translation occupancy, but would not give prime-field tightness. See
`../dickson_difference_splitting/README.md`; the general proof remains open.


## September 17: splitting proved and quadratic constant strengthened

A Frobenius calculation proves that every root of every pairwise Dickson
polynomial difference lies in F_p, for all primes p=1 mod4. Thus anchored
quotients have distinct evaluations at every extension-field point outside
F_p. Exact translation occupancy strengthens the uniform fixed-gap MCA
bound from ceil(3n^2/100) to ceil(n^2/20), with the same rate1/8 and gap1/16.
The main paper now includes the splitting lemma and stronger corollary.
This is a constant improvement over quadratic extension-field growth, not
a prime-field transfer or first-order tightness theorem.

The exact nonsquare-anchor incidence count is N/4, improving the generic
average3N/16 and giving the final uniform constant1/20. Independent replay
checks separation at all272 and1640 non-prime-field points for p17 andp41,
and certifies63 and370 exceptional labels. The final159-page PDF builds
without TeX warnings; the changed proof pages were rendered and inspected.
