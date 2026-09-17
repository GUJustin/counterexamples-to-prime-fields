# Prime-field upper-bound tightness: target and evidence

September 17, 2026. User priority: assess and pursue tightness of the
Dao–Kominers–Thaler prime-field proximity-gap paper. Work horizon extended
to 18:00 Eastern (22:00 UTC). This note separates established results from
research targets. No intrinsic fixed-gap superlinear lower bound is claimed.

Direct coauthor PDF comparison is now available in
COAUTHOR_DRAFT_COMPARISON_2026-09-10.md (105-page version7, recovered
from Dropbox). Use it before the historical excerpt-only references below.

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
