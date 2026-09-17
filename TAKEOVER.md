# New-laptop research continuation — September 16, 2026

## Working state

This folder is a writable snapshot of GitHub commit
540a9853b2c392a898697595a4bc263f7796ef11, obtained through the GitHub API
and commit-pinned codeload archive. Git metadata has now been restored through Dulwich on branch
codex/new-laptop-2026-09-16; system git still requires the missing Apple
command-line developer tools. Use the toolchain venv Python and Dulwich. A pristine
remote baseline is preserved in the adjacent remote-baseline directory.
The restored archive has not been modified.

Python: /Users/jthaler/.local/bin/python3.12
Recovery provenance: ../prime-recovery-provenance.json
Original handoff:
/Users/jthaler/Research-Restored-2026-09-16/Documents/counterexamples-to-prime-fields/RESEARCH_HANDOFF.md

## Completed in this continuation

Recovered research/riccati_cross_ratio from the restored overnight-review
folder. Reviewed its proof and classical source. Replaced three obsolete
checker inequalities with the sharpened list, heavy-candidate, and
full-support label bounds. Added nine prime-field equality fixtures that
check polynomial differential identities and exact agreement counts.
Retained and strengthened the characteristic negative control.
All checks passed under the 384 MiB watchdog. Added the missing sharpness
proof and an explicit definition of bad full agreement support.
No manuscript integration, commit, publication, or messages to third
parties have been performed.

## Scientific state and next work

The general prime-field list/line counterexamples already in the paper
remain the baseline. The new Riccati note proves M<=floor(n/(A-D)) for
one Riccati equation in characteristic zero or p>2D, with equality
families. A fixed nonlinear equation has at most D+2 candidates and at
most 2n(n+D+2)/(A-D) bad labels. Challenge-dependent equations are outside
the latter bound.

Next manuscript task: integrate the reviewed Riccati note with the
classical attribution, then build and visually inspect the paper.
Main open construction target: quadratic full-support proximity error
at fixed positive rate and gap for fixed higher derivative order.
First-order frontier: challenge-dependent singular agreements and
isolated solution points; large algebraic solution counts alone do not
establish large nearby-label counts. better.codes incumbent remains
116.13; no improvement was established here.

Do not resume unrelated protocol exploitation from archived notes.
Do not repeat the completed large cubic enumeration without a reason.
Do not infer current publication permission from historical handoffs.

## Overnight continuation

User requests uninterrupted work until at least September 17, 2026, 08:30 EDT
(12:30 UTC). This deadline is active. Riccati appendix integrated locally;
106-page PDF builds and new pages 102--105 visually checked. New all-large-prime
logarithmic-length line corollary is in research/logarithmic_length_lines/PROOF.md;
finite parameter discovery is running sequentially under the watchdog.

At 02:40--03:00 UTC, proved a stronger Riccati theorem using Taylor
reconstruction and intersection multiplicities. The list bound now needs
only p>D. Candidate count C_D=D+2 except p=D+1, where C_D=2D+2.
Full-support fixed-equation count is 2n(n+C_D)/(A-D). All new checks pass,
including nonconstant cross ratios and F_9 extension-domain lines.
The all-large-prime logarithmic-length line theorem is integrated in
the main paper; the pure-prime p=2^127-1, n257/k72/t78 certificate
exceeds the finite line prescription by >76.40420 bits in count ratio.
A separate anonymous LNCS draft was started in submission/, then explicitly
set aside at the user's instruction. Do not continue that draft. The requested
deliverable is the complete ePrint manuscript: 11-point article, full-page
letter paper, one-inch margins. Its authoritative sources are paper.tex and
the research appendices it includes. The user prioritizes an e-printable
research paper before any conference packaging; no LNCS conversion is wanted.
Official Eurocrypt rules and AI policy have been fetched into the parent
workspace. Author disclosure provenance from historical AI sessions remains
incomplete; do not silently attest author review or submission eligibility.

## ePrint correction and current replay

At the user's explicit correction, the full ePrint article is the only
active publication draft. Standard pdfLaTeX now builds it successfully on
this laptop (installed missing enumitem and xurl in user-local TinyTeX).
The current native build remains 109 pages, letter size, one-inch margins,
without overfull boxes or undefined references. The new boundary-family
paragraph on page 107 was visually checked. Do not resume submission/.

Git PDF history confirms the user's remembered 71-page version at
73d4661fc8, then growth to 104 pages at the downloaded head. The 19-page
LNCS main text omitted substantial material; it was not a demonstrated
90-page editorial cleanup. See research/paper_referee/EPRINT_SCOPE_REVIEW.md.

New Riccati boundary family: for every prime p, (X^p-X)P'=-P-P^2 has
exactly p+2 degree-<p solutions over every extension field. Proof uses
binary evaluation values and f''=0. Added to appendix and checked at
p=2,3,5,7,11,13. Separate exhaustive nonlinear-equation scans over F3/F5
find maxima 5/7 solutions, respectively, via normalized rational-function
grouping; these are experimental finite-field counts, not a general
p+2 upper theorem. Source and independent checks are in
research/riccati_cross_ratio/boundary_search/.

A full sequential replay of the 61 default mathematical Makefile checks
is active; inspect research/eprint_replay_2026-09-16/verification.json and
the live exec session before restarting anything. Each numerical child
has the 384 MiB watchdog. Compiler wrappers in tmp/eprint-replay-bin use
Zig with explicit macOS 14 target; the native macOS 26.6 target failed in
bundled libc++ with an undefined INFINITY macro. No global compiler paths
or shell profiles changed. The replay does not use --full cubic search.

Replay follow-up: the cubic fixture initially failed because Zig -O3
defines NDEBUG, unlike the compiler used for the archived run. Its hashed
C++ source has lookup.emplace inside assert, so disabled assertions omit
the table insertion. Confirmed with the preprocessor: -UNDEBUG removes
NDEBUG. Added -UNDEBUG to all five C++ compile commands in four default
verification scripts; wrappers also supply it. Do not change the archived
cubic source merely to hide its hash difference. After the live replay
finishes, rerun the two Frobenius-index compiled checks, the cubic default
checker, and the new boundary scan with assertions enabled. They are the
affected prior runs. The overnight replay has not yet begun and will see
the corrected compiler flags. Preserve and report the initial failure.

Completed follow-up: all of those assertion-enabled replays passed,
including both boundary scans and their independent polynomial enumeration.
The overnight certificate replay also passed. The current Makefile has
62 mathematical checks, all covered by
research/eprint_replay_2026-09-16/final_verification.json. The initial
cubic failure remains recorded rather than overwritten. No jobs remain
running from this replay.

New finite prime-field comparison: research/prime_exponent_coefficients/
certifies half-rate interval-domain lists that force c2>2.00475,
3.97715, 7.84601, 27.31865 over primes 2^31-1, 2^61-1, 2^127-1,
2^521-1, respectively, at c1=1. The 521-bit example has n=29176,
k=14588, surplus 56, eta=1/521, and log2 L>14233.01899. Its sharper
Elias check passes although the crude p^56>2^n test does not. These
replace the older c2>22.2 finite comparison; no circle-domain claim.
The application section also spells out that even c1(p)<=p^K requires
c2(p)>=(1/2-o(1))*log2(p)/log2(log2(p)), a consequence of the existing
all-large-prime list theorem. New source/proof self-review is in
research/paper_referee/NEW_PRIME_RESULTS_REVIEW.md.

The updated native PDF is 110 pages, with no overfull boxes or undefined
references. New certificate page 74 was visually checked. The active
8:30 a.m. Eastern target is still 12:30 UTC on September 17; the last
clock check was only 03:14 UTC. Continue research, do not mark complete.

Further progress: research/composed_bounded_root_mca/ contains a new
self-reviewed common-composition closure proof for the bounded-root
O(n) full-support MCA theorem. One common phi may have growing degree;
received words may vary within fibers. Large effective length uses the
old Wronskian proof with fiber multiplicity B; small effective length
uses a constant-dimensional linear space. Exact checker passes 43,545
small polynomial-label pairs and five growing-composition examples.
This remains an auxiliary research note, not another manuscript appendix.
The main fixed-gap quadratic target remains open. An exploratory
two-branch Riccati route is recorded in
research/riccati_cross_ratio/TWO_BRANCH_FRONTIER.md; do not mistake its
local necessary conditions for an actual construction or upper theorem.

September 17: direct source audit of the March 24 S-two whitepaper is in
research/paper_referee/STWO_QUANTIFIER_AUDIT.md, with PDF provenance JSON.
The abstract now states the numerical coefficient/remainder distinction
explicitly. Native rebuild passed; first-page visual review and commit
of this editorial change are still pending.

Recovered and independently audited the old full-field Dickson seed:
research/dickson_fixed_gap/AUDIT.md and verify.py. At p=1 mod 8,
n=p-1, rate 1/4, agreement 3/8, list size n/2 over F_p. For p>256 this
is strictly below Elias. Thus the unrestricted prime-field list claim
has a fixed-gap obstruction as well, but the archive records that the
owner explicitly did not accept n=p-1 as solving the n=o(p) target.
At p=1 mod 16 the old extension-field line gives n^2/64+n/16 full-set
MCA failures at agreement 5/16; persistent core correlated subsets mean
this is NOT the ordinary/subset CA result sought in the manuscript.
Six-prime independent exact verification passed under 384 MiB guard,
including p=257,337. This is recovered September 8 research, not a new
discovery. Priority review and a concise full-length comparison for the
ePrint remain pending. Do not inflate this into a short-domain result.

Latest user asks for a clearer, stronger conceptual message. Explained
the audited inverse-gap exponent obstruction and the remaining fixed-
gap short-domain target. Better.codes live display remains 68.11 to
116.13 bits; no verified benchmark improvement. Future strength claims
must distinguish short/full-length domains and full-set/subset CA.

User explicitly requested that the paper state the clearest audited
conceptual message. Updated abstract opening and introduction page 2:
short-domain n=o(p) examples force a nearly quadratic reciprocal-gap
exponent, versus the proposed linear one; changing universal constants
cannot repair it. The introduction separately states that superlinear
exceptional counts at one fixed positive gap on short domains remain
open. Native build still 110 pages; first three pages rendered and
visually checked; no overfull boxes or undefined-reference warnings.

Corrected the exploratory TWO_BRANCH_FRONTIER.md: the normalized
zero-branch equation R_z=P_z-T P_z'/P_z cannot yield the quarter-rate
target. When n>4D and char=0 or p>D, three labels force proportional
witnesses and a common correlated set of size at least n-D. Proof uses
triple support intersection and the zero-Wronskian identity. This is a
new proof-reviewed research-note closure, not yet a separately checked
computation or an addition to the manuscript. General two branches
remain open. Do not describe this normalized case as promising again.

The normalized closure now has an independent exhaustive verifier:
verify_zero_branch.py checks 586 candidates, 151605 pairs, 2040
collinearity events across (p,n,D)=(7,5,1),(11,9,2), with repeated
roots included. Passed under the resource guard. The frontier note
also records the elementary extension excluding a low-degree moving
branch: n-D agreement and n>4D force all three-or-more witnesses onto
one codeword line, with common coefficient agreement >=n-2D and at
most 2D selected full-set exceptions. This closes this route at quarter
rate; the genuinely two-high-degree-branch case remains open. Keep
these routine rigidity observations in research notes, not more pages
of the ePrint's main result section.

Direct Dickson lift check: check_integer_lift.py preserves all agreement
supports on integer representatives but allows new words and witnesses.
For p=17,41,97,193 the interpolation constraint rank is n-k-1 in the
native field and n-k modulo 65537, certifying rational rank n-k. Thus
only the common global codeword survives on those integer nodes in
characteristic zero. Moving nodes and other support patterns are NOT
excluded. Results and scoped proof are in dickson_fixed_gap/AUDIT.md.
The leading moment-count constant was rechecked: the main theorem
already retains binomial factorial savings, so that does not offer a
new asymptotic improvement. Continue seeking a different source of
growing fixed-gap lists/line witnesses rather than rediscovering it.

Added the full-length Dickson seed as a compact proved comparison,
Proposition full-length-fixed-gap, via dickson_fixed_gap/comparison.tex.
It explicitly makes no novelty claim; the full-set MCA construction is
NOT added. The S-two application distinguishes the unrestricted
fixed-gap obstruction from the short-domain inverse-gap obstruction.
The primary Guruswami--Rudra STOC 2005 paper was inspected; its displayed
full-field list results concern vanishing rate and do not establish
priority for this exact quarter-rate example. No novelty inference.
The manuscript is now 111 pages. Comparison pages 9-10 and application
page 48 were rendered and visually checked; no build warnings. Makefile
now includes the previously passed Dickson verifier: 63 checks total,
with the earlier 62-check replay plus dickson_fixed_gap/verification.json
covering them. A full rerun was not needed for this isolated addition.

Next exploratory direction recorded in dickson_fixed_gap/BOUNDARY_TRANSFER.md:
the full-field list-to-ordinary-CA conversion requires a true boundary
list, not just the known 3n/8 agreement. The natural received polynomial
has degree n/2, so the anchored padding degree proof does not apply.
A tiny unsaved interpolation experiment at p17 found maximum6 and22
maximizers (among1016 candidates determined by 4-node subsets); this
needs guarded saved replay before citation. Multiplicative orbits of
true maximizers may supply a boundary list, but small-orbit candidates
reduce to low-degree problems on mu_(4r) and remain an obstruction.
Do not assert ordinary CA failure from the recovered full-set MCA count.

Saved guarded exhaustive Dickson quotient census in quotient_scan.cpp,
run_quotient_scan.py, quotient_scan_results.json, resource record. For
r=1..7 on mu_(4r) over65521, degree<r maximum agreements are
1,2,4,4,5,8,8, all strictly below3r/2. Complete interpolation enumeration
uses constant memory; build -UNDEBUG is required. The p17 fixture
independently reproduces maximum6 with22 maximizers, replacing the
earlier unsaved observation. BOUNDARY_TRANSFER.md proves specialization
to characteristic-zero upper bounds and a Hadamard norm bound excluding
the same supports at all sufficiently large primes. Thus full-word
maximizers eventually cannot have orbit<=7. This is NOT an unbounded
orbit theorem and remains a research note, not a main-paper claim.

New proof-reviewed deduction: UNBOUNDED_BOUNDARY_LISTS.md uses primes
p=9 mod16 and p=-1 modulo every odd prime<=R. Dirichlet supplies
arbitrarily large such primes. Then k=(p-1)/4 has no divisors<=R except
1,2. A nearest polynomial's multiplicative orbit is therefore >R,
because orbit1/2 candidates agree on at most k coordinates, whereas
Dickson gives3k/2. Exact 56 cyclotomic determinant norms exclude orbit2
in all characteristics>17; verify_two_orbit.py records prime factors
only2,3,5,7,17. This proves unbounded true boundary lists along chosen
primes, still n~p. A three-coset version has exact rate1/3, maximum
agreement>=5/12, and an unused base-field coset. It follows by deleting
a square coset with at most half the total square agreement incidence.
Neither version is an ordinary-CA line theorem or n=o(p) result.

The quotient census extended through r9: maxima forr8,r9 are9,12,
below3r/2. The infinite-family proof needs onlyr1,2 and bypasses the
general quotient conjecture. Independent three-coset census atp41,k10
checks30,045,015 interpolation subsets: maximum14, exactly20 nearest
polynomials. Boundary anchor removal now works via true maximality;
value diversity on padding points is the remaining line-transfer issue.
These new results stay research notes pending further review, not
additional main-paper pages. Last current PDF remains111 pages.

Extracted all20 p41 three-coset maximizers from the complete C++ census,
then independently verified an anchored ordinary-CA line. At anchor2,
10 candidates survive. Five unused padding points have10,10,9,9,9
distinct values; extension shifts produce47 nearby labels for n34,k9,
agreement14. No correlated subset of size14 exists: zero direction uses
the certified core maximum13, nonzero direction has <=8+5=13 common
coordinates. All labels/witnesses saved in boundary_line_verification.json.
IMPORTANT: exact Elias check fails for characteristic41. This is only a
finite mechanism check / coefficient-one obstruction, NOT a new
below-Elias counterexample or a superlinear family. No manuscript change.

New scoped transfer lemma in BOUNDARY_VALUE_AMPLIFICATION.md: for a true
boundary list (N,k,M), q<=M-k+1 unused base-field points with value
diversities V_x give an extension-alphabet ordinary-CA line with at least
ceil((M/N)sum V_x) labels, dimension k-1 and length N-1+q. Anchor
averaging preserves that much diversity, without requiring injective
evaluation. Exact p41 replay confirms unanchored diversity75 yields
guarantee35 labels, actual47. The three-coset asymptotic route remains
conditional on unbounded value diversity, which large orbit alone does
not imply. An exact-rate7/22 specialization adjusts p mod7 and sets
q=(k-15)/7; its gap is bounded below by7/88, but not fixed exactly.
Do not conflate bounded-below gap with the separately-fixed-gap remainder
question. No asymptotic counterexample has been obtained from this lemma.

Incidence audit of the value-diversity obstacle: for L distinct cap-D
polynomials with M old agreements on N nodes and <=V values on each of
S unused nodes, L*(M^2/N+S/V-D)<=M+S-D. For the three-coset family this
excludes V<=2 once L>=60, but permits bounded V=3 at the guaranteed
M/k>=5/4. Only M/k approaching sqrt3 would force unbounded diversity by
this argument, and that is not known. Recorded in the amplification
note. The full-length boundary route should not monopolize further
research: return to n=o(p) constructions, preserving this conditional
route without claiming its missing value-diversity step.

Returned to short-domain lifts. PRIME_FIBER_RIGIDITY.md proves that for
distinct rational-prime seed nodes and prime fiber degree B, arbitrarily
large splitting primes can be chosen so subset sums vanish only for
unions of whole fibers. More strongly, equal-sum subsets differ only by
whole/empty fibers. Kummer independence over Q(zeta_B), the prime
cyclotomic relation, and exclusion of finitely many nonzero norms prove
this. Consequently the ENTIRE decoding list at W(X^B), for monic W of
degree t and code dimension kB<tB, consists exactly of seed candidates
P(X^B). This is pointwise list control, NOT a global maximum-list bound.

Distinct-prime seed domains preserve the leading moment-count exponent:
q_m=O(m log m) gives the same (c^2/4+o(1))*m moment cost. Fixing such
a seed, the resulting growing-prime-B family has exact fixed rate, gap,
and full list size L at its displayed word; p can ensure n=o(p) and
strict Elias. No stronger inverse-gap exponent is claimed. Guarded
verify_prime_fiber_rigidity.py passes all1024/32768 subset checks for
B2/B3 and exactly preserves the two-word seed list on3,5,7,11,13.
This proof and consequence remain research notes pending further audit.

Extended prime-fiber rigidity to entire received lines U(X^B)+zV(X^B)
with deg U,deg V<=t: the full nearby-witness profile, nearby labels,
selected-witness affine concurrency, and ordinary CA at thresholdtB
are preserved from the seed. Leading-degree cancellation is handled
separately by root counting. Thus this controlled composition cannot
amplify line counts. Exact B2/B3 replay of W_z(Y)=Y^2+(z-16)Y has
exactly8 nearby labels and maximum list2, matching the seed completely.

Potential extension currently being audited: arbitrary distinct integer
seed nodes q_i and arbitrary B>=2 could use a generic centered monic
polynomial phi_B with Gal(product_i(phi_B-q_i))=S_B^m. Independent
transposition monodromy at the distinct discriminant hypersurfaces
would prove the generic product group; Hilbert irreducibility would
specialize it over Q. Transpositions rule out every partial-fiber subset
sum relation. Chebotarev plus finite norm exclusions then gives exact
list preservation for W(phi_B) without prime-node restrictions. This
is not yet a verified theorem; check the generic Galois-group and
specialization steps before using it.

The arbitrary-integer-seed extension is now proved by a simpler route:
translate all nodes q_i by c chosen via CRT so v_(r_i)(q_i+c)=1 and
v_(r_i)(q_j+c)=0 for j!=i, with private primes r_i larger than every
node difference. These private valuations give Kummer independence
for every prime B, including B=r_i (ramification index B-1). Thus the
existing exact-list and line-profile proof applies to any integer seed
after translation, with no Hilbert irreducibility or generic Galois
claim. The earlier generic-polynomial idea is unnecessary for this
extension and remains unaudited for arbitrary composite fiber degrees.
Guarded CRT replay on seed0,1,2,3 and B2/B3 passed, preserving exactly
the two-word list0,-2 and all five nearby line labels. Original prime-
node fixtures retain eight labels. The note also spells out extension
to fixed-degree parameter curves via interpolation at d+1 labels; this
is profile preservation, not amplification. No manuscript pages added.

Rechecked primary TR26-169 PDF (37 pages, September 5): Theorems1.1/1.2
give polynomial-in-n list/MCA bounds at fixed slack, not exponent-one
exception bounds. Section8.5 disclaims competitive numerical exponents.
Scope audit saved as research/paper_referee/JERONIMO_SCOPE_AUDIT.md.
This is not an independent proof audit; the fixed-gap superlinear target
remains compatible with its stated bounds.

NEW strengthened anchored-padding theorem: its coefficient lower bound
now holds at EVERY sufficiently small rational eta, not merely along a
sequence, with exact fixed rational rate rho and exact gap eta.
Flexible padding permits arbitrary integer n,K provided q=n-mB+1>=1,
K>=B(k-1), and K-1+q<Bt. Choose a=rho+eta,
m=floor(H/(eta^2 log2(1/eta))), t=ceil(a*m/(1-eta/2)),
k=floor(rho*t/a). Then am<t<am/(1-eta), and B can range over multiples
making n=Bt/a,K=rho*n integral. The old moment estimate gives the same
log2 C >= (H^2/2-o(1))/(eta^2 log2(1/eta)), with
C=(1-am/t)*L. No denominator restriction on eta and no uniform bound on
the first length/field. Counts remain linear at each fixed gap.
Proof in research/fixed_gap_padding/PRESCRIBED_GAP.md; integrated into
paper theorem fg:anchored-fixed-gap, abstract and application statements.
Guarded verify_prescribed_gap.py passes15 exact rational/moment checks
and full prime-field fixtures (p,n,K,A)=(1009,21,5,10),(14449,42,10,20).
Rate and gap both5/21; labels8,14; global joint-agreement bounds9,19.
Added checker to Makefile (now64 checks). Native rebuild passes at111
pages, without overfull boxes or undefined references. Visually reviewed
abstract and theorem/proof pages1,27,28. The old anchored checker also
passes all six fixtures,70 moment checks,378 affine transforms and its
two coefficient calculations after the shared fixture signature edit.

Further strengthening: the prescribed-gap parameters also give a list
lower bound at EVERY small rational gap by keeping the full mB fibers,
adding n-mB points, and using W(X^B) with candidates G_i(X^B). Added a
short manuscript consequence and exact unanchored checks for the two
prescribed-gap fixtures. This is a selected-list lower bound.

Composite fiber rigidity is now proved in a research note: for B
coprime to private primes, Kummer monomial independence plus the FIRST
B-1 root moments forces any zero-moment subset to be a union of whole
fibers. The full DFT replaces the prime cyclotomic single-moment argument.
Positive integer padding nodes cannot occur in such a subset (the
rational part of its first moment would be positive). This gives exact
entire lists at threshold tB for dimensions K<=(t-1)B+1, including K
not divisible by B. Choosing B through suitable denominator multiples
gives exact pointwise-list preservation at every small rational gap.
It does NOT control global lists or amplify a list with length.
Guarded verify_composite_fibers.py passes all262144 and1048576 subsets
for B4/B6; exact list sizes2/6 at K4/5 and1/3 at K6/7. Research note
COMPOSITE_FIBER_RIGIDITY.md; not added to manuscript or Makefile.

IMPORTANT new conceptual strengthening integrated into anchored lemma
and fixed-gap theorem: EVERY nearby word on the entire received line
can have EXACTLY ONE nearby codeword. Form the pool T of all code
polynomials interpolating any K old coordinates, |T|<=M=binom(N,K).
Because A-q>=K, every possible nearby candidate is in this finite pool.
Choose all pad evaluation maps injective on T and all (P,pad) labels
distinct, using p>N+1+q+(K-1)binom(M,2) and p>(q-1)M^2. Then every
nearby candidate has exactly A-1 old agreements and one new agreement,
and no label has two candidates. The exact nearby-label count is q
times the ENTIRE core boundary-list size. No-CA proof unchanged.
All fields prime; n=o(p) still available. No global-list bound follows.
Proof UNIQUE_NEARBY_PADDING.md and exhaustive verify_unique_padding.py
pass fixtures (p,n,K,A)=(1571,11,2,5),(114874079,21,5,10), with core
interpolant pools18/5918, exact boundarylists2/2, nearbylabels6/8 and
maximum list ON THE LINE1. Added Makefile checker (now65). Abstract
and introduction explicitly state this conceptual separation. Native
rebuild passes at112 pages, without overfull boxes or undefined
references. Visually reviewed pages1,2,27,28,29 after these edits.

Audited the distinction between line-wise and global list size further.
The SAME unique-padding code realizes every exact list cardinality
r<=min(q,L_boundary): retain the core word, assign r different boundary
polynomials to r different padding coordinates, and choose all remaining
pad symbols outside the corresponding evaluation image of the complete
pool T. Every possible nearby candidate is in T, and pad evaluation
injectivity leaves exactly those r. Thus global maximum list is at least
min(q,L_boundary), eventually at least the fixed selected seed size L.
This explicitly prevents interpreting the new line-wise uniqueness as
global unique decodability. UNIQUE_NEARBY_PADDING.md records the proof;
the checker now exhaustively verifies alternate words with exact lists
0,1,2 in both fixtures. Added a short scope paragraph to the manuscript.
Native rebuild remains112 pages with no overfull or undefined-reference
warnings; visually reviewed the new global-list scope paragraph onpage29.

Returned to the fixed-gap subgroup search. New research-note constraint:
POWER_TWO_BOUNDARY_RIGIDITY.md (actually all prime-power orders) gives
an EXACT moment-class description for degree<=A received polynomials
at agreement A, dimension K, s=A-K, on mu_n in characteristic zero.
For n=ell^e, let h be the smallest ell-power>s and q=n/h. Every class
freezes all partly occupied mu_h cosets and freely chooses b full cosets
among the remaining q-r; its size is exactly binom(q-r,b). Thus list
size <=binom(q,floor(q/2))<2^(n/s), with the q1 case bounded by1.
Proof: rational difference masks propagate Fourier zeros by cyclotomic
Galois orbits, leaving only frequencies multiple of h, hence q-periodic
differences. Whole-coset swaps supply the converse.

Finite-field transfer is stronger than the initial crude norm bound:
for p=1 mod n, it holds when p>n^E, where
E=max_{d=ell^j<=s} phi(n/d)/(floor(s/d)-floor(s/(ell*d))) <=2n/s.
Every vanished conjugate moment contributes a DIFFERENT p factor to
the integer norm, so p^R divides a nonzero norm of size<=n^phi(n/d).
This proves the transfer condition. It does NOT apply to arbitrary
received words or give a better.codes bound. The unbounded-list search
on these subgroup boundary words must use finite-characteristic
collisions below this threshold, or leave this low-degree-word setting.
No novelty claim and no manuscript addition.

Guarded verify_power_two_boundary.py passes321398 exact characteristic-
zero subset checks at n8,9,16,25, plus exact finite-field class checks
(n,A,s,p)=(8,4,1,65537),(16,8,3,65537),(16,8,7,1009).
At n16,A8, char0 maxima for s1..7 are70,6,6,2,2,2,2.
For s1, finite-field maxima758,198,120 at p17,97,113 demonstrate that
p>n alone is NOT enough. These finite examples are not below-Elias
counterexamples. Results and resource report live beside the note;
not added to Makefile. No research process remains running.

Finite-characteristic subgroup census completed: all12870 eight-subsets
of mu16 in22 primes, and all10518300 eight-subsets of mu32 in each of
p97,193,257,353,449 (52,591,500 supports). No violation of the exact
char0 MAXIMUM list size was below Elias in these cases. But support
classification does fail below Elias: overF97 onmu32, dimension4,
agreement8, W=X8+23X4 has ENTIRE list {75,8+16X2,8-16X2}, each with8
agreements. Rate and gap both1/8; exact integer Elias check passes.
Its support differences are not4-periodic, although size3 remains
below the char0 uniform maximum4. Independent interpolation enumerates
all35960 determining4-subsets,28833 distinct candidates, and certifies
the full list. The quadratics have only a two-element mu4 rotation
orbit and are mu2-invariant: no growing-orbit or growing-characteristic
family is proved. Details in SUBGROUP_EXCEPTION_SEARCH.md and saved
censuses/checkers under research/fixed_gap_padding/. No manuscript
addition, no Makefile addition, no research process remains running.

Audited removal of the logarithmic loss in the reciprocal-gap lower
bound. MOMENT_LOGARITHM_AUDIT.md records the connection to height-one
polynomials: two distinct INTEGER interval subsets matching moments
0..s give nonzero F with coefficients{-1,0,1} and (X-1)^(s+1)|F.
The classical O(sqrt n) multiplicity upper bound implies n=O(eta^-2)
at eta=s/n, hence log(seed list)<=O(eta^-2). Our lower bound is within
a logarithmic factor of this mechanism's ceiling, not of a universal
code bound. Source checked: Erdelyi arXiv2409.09553v5 Theorem3.1 (M1
case attributed there to BEK99 Theorem4.1); Borwein--Mossinghoff P153
first page visually inspected for classical height-one degree bounds.
No claim that the search proves current open-problem status. Real-
coefficient sharpness in the2024 paper does not supply binary subsets.
Disjoint binary switches cannot help: each needs at leasts+2 nonzero
positions by Vandermonde, so2^r disjoint choices satisfylog2L=r<1/eta.
Removing the log needs exponentially many compatible relations, not
just one high-multiplicity pair. Existing Gram factorial savings are
already included. No lower-bound improvement or manuscript edit here.

New attempted short-domain character route: p=2rk+1 prime, section
0<=j<r, G(X)=sum_i binom(rk+j,ri+j)X^i, and P_h=G(hX)-X^k for
h inmu_k. Exactly k distinct degree<k candidates. On eachmu_k coset,
choose the modal value of G minusX^k as received symbol; all candidates
get the same agreement count. Selecting topc cosets givesn=ck and
rate1/c. If r,k grew and topc modal sum M/k>1+c*eta at fixedc,eta,
this would give unbounded fixed-gap lists withn=o(p). This received
word is generally outside the low-degree boundary-word setting.

Scanned726 cases: r2..80, k8,11,16,23,32,47,64,97,128, sectionsamong
0,1,floor(r/2),r-1. Initial184 section1 cases had nofour-coset positive
surplus except r2. Extendedscan has finitepositive higher-section
examples, but rate1/4 below-Elias examples remain only r2,j1 (known
Dickson). Atc8,16,32, below-Elias casesnumber30,143,240 and largest
observedk11,16,32: no growing-family evidence. Independentinteger-
binomial checks verifyallcosets and allcandidateorbits infivefixtures.
Example r78,j0,k8,p1249,n64,A16 hasrate/gap1/8 andlist8; no universal
bound violation follows. BINOMIAL_SECTION_SEARCH.md and allcensus/
verification sources/results inresearch/dickson_fixed_gap/. No
manuscript addition, no active numerical job, no asymptotic claim.

Independent-product amplification audit: for nontrivial monic factor
families of degrees A_i, put d_i=maxdeg(F-F'). Independent products of
degree A=sumA_i have maximum difference degree exactly
D=max_i(A-A_i+d_i), by changing one factor and telescoping for the
reverse inequality. A common-prefix gap s=A-K therefore requires
s<=min_i(A_i-d_i-1), hence r(s+1)<=A<=n and r<1/eta. This rules out
unboundedly many independent factors at fixedgap, in every field;
it does not constrain a single large family or coupled cancellations.
INDEPENDENT_PRODUCT_LIMIT.md gives proof and18 exact fixtures r1..6,
B1,2,3, plusfullselectedagreement checks overF101 forB1. The example
has2^r choices at exactgap1/(4r), only reciprocallog-listgrowth.
Also closed a naturaluv-factor line: ifQ=-uCB-vAD fits becauseboth
cross terms individually have degree<K, whiledegAB>K, then
g=CD hasdegree<K. The line isparalleltoacodeword, soevery nearby
witness has afullcorrelatedexplanation. This doesnotcoverhighdegree
cross-term cancellations. No manuscript addition or strongerlowerbound.

NEW manuscript strengthening: fixed-gap selected lists and genuine
ordinary-CA bad-label lower bounds can be realized with polynomial-size
prime fields p=n^{O_rho,eta(1)}, still n=o(p), exact rate/gap and strict
Elias. Corollary fg:polynomial-fields. A multiplicative-character count
finds a shift c making all m seed nodes c+a Bth powers once
p>16m^2 B^(2m). Bound N>=p/B^m-m sqrt(p)-m, from BGKS arXiv1110.0812v2
Lemma17 with constant additive phase (primary source checked).
Linnik for leastprime1mod B^(2m+2) supplies B^(2m+2)<p<=C B^((2m+2)L0)
with absoluteL0 (Xylouris arXiv0906.2749 checked; no bestconstant claim).
Translate seed, choose alpha^B=c+anchor, divide byX-alpha. Padding
separates ONLY fixedselectedL, so itsfieldbounds O_seed(B) suffice.
Wholeline uniqueness is NOT included in polynomial-field corollary;
that older proof separates an exponential interpolationpool. Nor does
this imply exact-listfiber rigidity or any prescribedsubgroup result.
Exponent in n can be O_rho(eta^-2/log1/eta); constants/firstlength not
uniformineta. Fullproof research/fixed_gap_padding/POLYNOMIAL_FIELDS.md.
Three exact positive shiftcountchecks; two fulltranslatedpadding/list
fixtures(p,B,n,K,A)=(1009,2,20,6,10),(65539,3,30,9,15), secondshift443,
anchor2139. Allpass under384MiB watchdog, ~0.6sec. Addedchecker to
Makefile (now66). NewPDF113pages buildswithno warnings/overfull/undefined;
visuallyreviewedpages1,2,4,5,29,30,111,112. No livejob. Continue until
atleast12:30UTC Sep17; currenttimeabout05:16UTC, goalnotcomplete.

Further dependency note POLYNOMIAL_UNIQUENESS_DEPENDENCY.md: if one
uses Jeronimo TR26-169 Theorem1.1's uniformprimefieldpolynomiallistbound,
wholeline uniqueness can also be realized withpolynomialp. PoolT only
needs candidateswith>=A-qoldagreements, whosegap overK is Bd-1,
d=m-(1-eta)t/a>0. Fixedgamma=d/(2m) gives |T|<=N^C; chooseleastprime
1modB^E withE>max(2m,2C+1), separateT asbefore. Exponentdependsongamma
and externaltheorem; nottheexplicitO(eta^-2/log1/eta) boundofthe
standalonecorollary. This is recorded asdependency, NOT integrated
or described asan independentlyauditedupperbound. Currentclock05:09UTC
(earlier05:16estimatewasincorrect); goalstillactive, cutoff12:30UTC.

NEW stronger padding lemma and asymptotic integrated: averaged.tex under
research/fixed_gap_padding/, inputafterpolynomialfields/concretecoeffs.
Allowlabelcollisions; coreN worddegreeA-1, L candidatesdegree<K,
pairdiffdegree<=d, eachA-1oldagreements; q<=p-N andK-1+q<A.
T=d binomL2-pairs(L(A-1),N)>=0,R=p-N,M=L^2R/(LR+2T).
Chooseqavailablepointswithlargest evaluationimages, offsetaverage gives
J>=ceil(p*(1-(1-M/p)^q)). Oldjointdegreeargumentunchanged. Integer
momentseedB1 givesN=m-1,K=k-1,A=t,q=t-k+1,n=m+t-k.
Exactnewfinitecertificates(p exponent,n,K,A,J,excessbits c1=c2=1):
31,72,12,15,381222100,6.73559;
61,155,35,40,326877636368105821,27.01590;
127,273,70,76,16423077798015443787467749084096814366,78.16602;
521,1065,381,393,>3.1200e155,422.98809.
AllstrictElias; arbitrarypaddedintervaldomains, nosecurity/subgroupclaim.
verify_average_padding.py usesexactGram,anchoring,balancedpairs,rational
unionformula,outwardlogintervals,LucasLehmer. TwoF17fixturesexhaust
5202offsets+167042codewordpairs. 5.4m discoverytriples,notoptimality.
AsymptoticTheoremfg:larger-gap-lines: eachlargeprimeb=log2p,
n~2b/H exactrateρ, eta~H/sqrt(b log2b),
J>=(H/[ρ(1-ρ)]-o)p/sqrt(b log2b), noCA. Choose
s~2(1-eps)sqrt(b/logb),m=n-s,k=ρn+1,t=k+s;
anchoredlogL>=b+Ω(eps*b) forsloweps->0. q=s+1, balancedbudget
2T/L²~ρ(1-ρ)n. NewPDF114pages cleanbuild; viewed4,30,31,32,33.
Makefile67checks,newcheckguardedpassed<1sec. No activeprocess.

MAJOR further strengthening: dense nearby parameters via nonconstant
padding direction, nowinmanuscriptTheoremfg:dense-lines (replaces
weakerfg:larger-gap-lines inpaper; oldresultproofretainedinresearchnote).
ForcoreN, dimensionK, thresholdA, qnew,n=N+q, replaceK-1+q<A by
binom(n,A)*p^q < p^(A-K)*(p-1)^q. Randomnonzerodirectionvalues
onpadding, zerooncore: foranyA-support rold,u=A-rnew, nonzeroG
vanishingroldimpossibleifr>=K; otherwise<=p^(K-r)possiblevectors,
prob<=p^(K-A)(p/(p-1))^q. UnionboundexcludesALLnonzeroGwithA
agreements. G0stillconfinesjointagreementtocoredegreeA-1.
Fixgoodg; randomf offsets translate/scalecandidateimages, soaveraged
labelunionformulaunchanged. Thispermitsq=Θ(n), henceconstantfractionp.

Forfixedrationalρ<β<1, α=ρ/β,H=H2β,b=log2p, n~2b/(αH),m=αn,
K=ρn,k=K+1,s~2(1-eps)sqrt(b/logb),t=k+s,N=m-1,q=n-m+1.
AnchoredlogL>=b+Ω(eps*b), eps=sqrt(loglogb/logb), L/p->∞.
2T/L²~ρ(1-β)n,M/p~1/[ρ(1-β)n]. Directionunionboundholds because
logbinom<=n=O(b) whereas(A-K)b~b^1.5/sqrtlogb.
eta~(ρH2β/β)/sqrt(b logb); J/p>=1-exp(-(β-ρ)/[ρβ(1-β)])-o1.
Thus ANYfixedfractionbelow1 ofallparameterscanbenearby atloglength,
noordinaryCA, strictElias, exactρ, everylargeprime. Chooseβnear1
forfraction1-δ. Gapstillshrinks; constantsdependρ,δ; nofixedgap
superlinearclaim. Predictedc1*n*2^(c2H2ρ/eta)=p^o1 vsactualΘ(p).
Abstractandintroexplicitlystatecontrast. NOuniquenessclaimfordensecase.

DENSE_PADDING.md proof; verify_dense_padding.py independentlyexhausts
F17 coreN6,K2,A4,q4,n10:directionbound30345/32768<1, gnew1112,
83521offsettuples+83521codewordpairs, guarantee10labels, maxselected
union12, jointagreementmax3. Oldqrestrictionfails. This smallfixture
checksmechanism, notElias. Allpassguarded<1sec,Makefile68checks.
LatestPDF115pages cleanbuild/nooverfull/undefined; renderedreview1,4,
31,32,33. Noactiveprocess. Continueuntil12:30UTC; current~05:20UTC.

Potentialnextstrongerregime (NOTproved/inpaper): letβ approach1withp
toobtain J/p->1 ratherthananyfixedfraction. Fixedβtheoremalready
sufficesforclearclaim. Near1 with1-β~c/sqrt(b logb) suggests
n~Cb^1.5/sqrtlogb,eta~C'/b,missingfractionexp(-Θsqrt(b logb));
needuniformentropyerroranddirectionconstantchecks. Noallpclaim.
Mainopenfixedgapshortdomainsuperlineartargetstillrequiresgrowingseed
lists; fiberliftkeepsLfixed andcannotresolveit.

NEW near-unit-density theorem integrated asfg:near-unit-density.
Forfixedrationalρ andc>H2ρ,b=log2p,ell=log2b:
n~sqrt2/c*b^1.5/sqrtell, eta~c/b,
J/p>=1-exp(-((1-ρ)/(2sqrt2*c)-o1)*sqrt(b ell))->1,
noordinaryCA, strictElias, n=o(p), everylargeprime.
Proofparametersnroundedρdenominator,K=ρn,s=floor(cn/b),
h=ceil((4+eps)b/ell),k=K+1,t=k+s,m=t+h,N=m-1,q=n-N,
eps=sqrt(logell/ell). Anchoredsupportcountbinom(m-1,h) haslog
>= (2+eps/2)b-O(b/ell), momentvectorslog<=b+O(b/ell+sqrt(bell)),
soL/p->∞. Pairbudgetd-(A-1)^2/N=h-s-1-h²/(K+s+h)~h.
Directionunionboundneedslogbinom(n,A)~Hρn<cn=(A-K)b, exactly
sameconstantstrictEliascondition. ThenqM/p~(1-ρ)/(2sqrt2c)sqrtbell.
Foranyfixedc1,c2 choosec>max(Hρ,c2Hρ):proposedcounto(p),actualp(1-o1).
Noallpclaim; gapstillshrinks; nofixedgapsuperlinearsolution.

ExactfinitecertificateatM521:n2800,K1400,A1411,eta11/2800,
nearbyfraction>0.99485642. Furtherhalf-ratefixturesM1279,M2203,
M3217,M4423give>0.99987751,0.99999545,0.99999976,0.99999998.
verify_near_unit_density.py usesmax(boxanchoredcount,anchoredGram),
exactintegerdirection/Eliaschecks,LucasLehmer,downward128bitdyadic
imageboundand32-termpositivebinomialsumforrationaldensitylower.
All5passunder384MiBguard<1sec. Initialbox-onlycheckfailedatb127,
521,1279 (finiteboundsnotyetlargeenough); b127omitted, Gramhandles
521/1279. Theasymptoticproofrequiresonlyboxandsufficientlylargep.
ResearchproofNEAR_UNIT_DENSITY.md; manuscriptnear_unit.texinputfrom
averaged.tex. Makefile69checks. PDF116pagescleanbuild; inspected
1,2,4,32,33,34. DateupdatedSep17. Abstractandpage2stateclearconcept:
nearbyfraction->1withoutcommonexplanation, proposedfraction->0.
Openquestionp<=n^DnowdistinguishesDfixedindependentofgapfromthe
newpolynomial-fieldcorollary. Noactiveprocess. Goalactiveuntil12:30UTC.

Audit and finite-density work after near-unit theorem: new independent
checker audit_density_independent.py imports none of the construction
helpers. It uses alternative binomial Gram variances, integer sqrtupper,
smooth occupancy instead of balanced, and complement-box sums atM2203.
AllM31/61/127/521 displayed density rows plusM2203replay. All65536F17
nonzero directions independently classified:5984bad,59552good, exact
badprob187/2048 vsunion30345/32768. Makefile now71checks (includes
independent audit and newverify_dense_half_rate.py).

New half-rate density table in near_unit.tex:
M31 n92 K46 A50 J/p>0.74303810, finiteprescription<2^-1;
M61 n216 K108 A113 >0.91025173, prescription<2^-10;
M127 n468 K234 A240 >0.96160200, prescription<2^-40;
M521 n2800 K1400 A1411 >0.99485642, prescription<2^-255.
AllstrictElias, arbitrarypaddedintervaldomains. AlsoM61n168K84A89
>.69859851 vs2^-20 in savedcertificate. Search1,381,044triples,notoptimal.
READMEupdatedcentralmessage, alldenseclaims,everyrationalgapquantifier,
polynomialfieldscope. Paper117pages clean; viewed30,31,33,34.

DENSE_SCOPE_AUDIT.md records whitepaperDefinition24/Conjecture2 reread:
noCA impliesanyselectedwitnessconcurrency<=n via vA<=va+n-a,a<A.
No farpoint was asserted by additive-offset construction (important
forotherformulationsofproximitygaps). Nearunitfamilyhasactualglobal
maxlist>p asymptotically:oneextramomentoncore costsO(sqrt(b logb)),
less thaneps*b seedslack. Addedscopeparagraphinpaper. Notanactual-list
separation; generic-domainsectionprovidesthatseparateresult.

PROMISING NEXT ACTION: FAR_POINT_PADDING.md contains a simpler STRONGER
variant, notyetintegrated/replayed. Setf=w globally (degreeA-1) and
randommultiplicativedirectionsg_j onpadding, g0core. DifferencesP_i-w
haveallA-1rootsinthecore, henceeachnewimageexcludes0. Randomscalings
covernonzerolabelswith union>=ceil((p-1)*(1-(1-M/(p-1))^q)).
No qrestriction or directionunionboundneeded! z0 isexactlyonecoordinate
farther thanthreshold, andf alonecannotagreewithanycodewordonApoints,
so noCA automatic. Same dense asymptotics, now WITH a farpoint.
NeednewF17mechanismcheck and exactp-1densityreplay; rounded finite
counts maychangebyone, don'tsilentlyreusep-basedformula. Then replace
complicateddirectionparagraphinpaperwiththiscleanerlemma/proof,
strengthentheoremswithfarpoint, updateREADME/mainmessageandscopeaudit.
Oldadditivecertificatesstayvalid; canretain inresearchnotmaintext.

Far-point variant NOW VERIFIED AND INTEGRATED. Lemmafg:far-padding
replaces the random-direction union-bound paragraph in the main paper.
f=w globally, g0core, randomnonzerog_jpadding. All differencesP_i-w
haveallA-1rootsinthecore, so eachoutsideimageexcludes0. Multiplicative
averaging givesJ>=ceil((p-1)*(1-(1-M/(p-1))^q)), anyq<=p-N.
z0hasEXACTagreementA-1; noCA automatic becausef alonecannotagreeA.
Bothdenseasymptotictheoremsnowincludeexactfarpointdistanceθ+1/n.
NearunitproofusesJ/(p-1)>=1-exp(-qM/(p-1)); 1/p lossabsorbedo1.
No directionunionboundneeded; strictEliasstillneedsc>Hρ.
Abstract,page2,READMEstatefarpointonecoordinateoutside,notconstantfar.

verify_far_point_padding.py: all65536F17nonzerodirectionsexhausted,
expectedselectedunion36975/4096, maxselected12; fullcodewordprofile
has15nearby nonzero labels, farlabels0and11 (maxagreement3,A4),
allcodewordpairsjointmax3. NotanEliasfixture. MainM31/61/127/521
exactp-1replaypreserveseightdecimaldensitybounds; integerJatM61,
M127,M521dropsbyonefromadditiveversion. verify_near_unit_density.py
andindependentauditalsoupdatedtop-1, allpasssequentialguardedchecks.
LargerM1279/2203/3217/4423densitydecimalsunchanged. Makefile72checks.
Oldadditive-directionchecksandproofretainedasvalidhistoricalalternative.
DENSE_SCOPE_AUDIT.mdupdated: finalconstructionDOEShaveafarpoint;
actualglobal-listdistinctionunchanged. PDF117pagescleanbuild,reviewed
1,2,31,32,33,34 (alsoearlier4). Noactiveprocess.

Possible next clean strengthening: give the fixed-gap UNIQUE-nearby
construction a farpoint too. Keep oldqrestrictionA-q>=K so everynearby
candidate belongs interpolationpoolT (size<=M=binom(N,K)). Choosepads
excluding roots of everyP-P' AND everyP-w, P inT, so all differences
P(x)-w(x) distinctnonzero. Sufficientp>N+q+(K-1)binomM2+(A-1)M.
Greedyg_j!=0 make(P(x_j)-w(x_j))/g_j distinctacrossall(P,j);
p-1>(q-1)M²suffices. Setf=wglobally,g0core. Thennearby iffPboundary
(A-1oldagreements)+onepad; allnearbywordsunique; z0far; noCAbyfdegree.
Samefixed-gapcoefficientandparameters, slightlylargerfieldbound.
Needs new exactfiniteunique-poolreplay beforeeditingoldlemma/theorem.
This would unifyallmainlinefamilieswithafarpoint. Existingoldunique
verifierfields1571and114874079likelymeetnewguardbutcheckcarefully.


## September 17 ~05:56 UTC — fixed-gap unique-nearby far point verified

Completed the next-step strengthening described above. Main anchored-padding
lemma and fixed-gap theorem now use f=F_old globally, nonzero padding g_j,
and multiplicative labels (P(x_j)-F_old(x_j))/g_j. Extra exclusions cost
(A-1)M roots, and p-1>(q-1)M² separates labels. Every nearby word still has
a unique nearby codeword; z=0 has EXACT maximum agreement A-1. No correlated
agreement follows immediately from the global degree bound. Fixed gap, rate,
count and asymptotic coefficient unchanged. Polynomial-size selected-list
corollary also upgraded, with extra O_seed(B) exclusions; still no whole-line
uniqueness in that corollary.

New UNIQUE_FAR_PADDING.md and verify_unique_far_padding.py with exact whole
interpolation-pool replay: B1/p1571/n11/K2/A5 (18 pool polynomials, 6 labels),
B2/p114874079/n21/K5/A10 (5918 pool polynomials, 8 labels), max list online1,
exact far agreements4,9. Both PASS under384MiB watchdog. Shared old verifier
replayed and PASS. Shifted polynomial-field fixtures now multiplicative
far-point too: p1009/B2 and p65539/B3, PASS with exact far agreements9,14.
Makefile now73checks. README and companion notes updated. TeX clean117pages,
visually reviewed2,27,28,29,30; no clipped text. No active process.

Continue until12:30UTC. Next mathematical possibilities: try r-coordinate
far points (r>1) using multi-padding matches and second moments; or pursue
growing fixed-gap lists on short domains, still the main unresolved target.
Do not conflate fixed-gap unique-nearby family with dense shrinking-gap family.


## September 17 ~06:00 UTC — growing far-point separation

Previous goal turn was progress (commit28a14611). This turn proves and
integrates a further strengthening, not just a status repeat. New
MULTI_MATCH_FAR_PADDING.md, multi_match.tex, verify_multi_match_far_padding.py.
For degree-D global core word w with L degree<K candidates having D old
agreements on N points, choose q random distinct outside points and random
nonzero padding directions. X counts (candidate,r-subset) matching at fixed
nonzero z. E X=L*binom(q,r)/(p-1)^r. Exact second-moment ratio is sum over
intersection a of v_a U^a[1/L+L^-2 sum_i!=j(c_ij)_a/(R)_a], where
v_a=binom(r,a)binom(q-r,r-a)/binom(q,r),R=p-N,U=p-1. Rootbound plus
balanced core overlaps gives sum c_ij<=T. Cauchy-Schwarz and averaging
yield at least ceil(U/B) nearby labels at threshold D+r. z0exactagreementD.

CRUCIAL improvement: c_ij <= e=(K-1)-max(0,2D-N), because two large
core supports must intersect. This is much smaller than K in our regime.
For e>=1, ratio<=U^r/L+(U/(R-r+1))^r exp(r²e/(q-r+1)), from hypergeometric
factorial moments. Set b=log2p,ell=log2b,n~sqrt2/c*b^1.5/sqrtell,
K=rho*n,s=floor(cn/b),r=floor(b^1/6),eps=ell^-1/4,
h=ceil((3+eps)(r+1)b/ell),t=K+1+s,m=t+h,D=t-1,N=D+h,q=n-N.
Anchored support log>= (1+eps/3)(r+1)b-O(rb/ell), moment costb+lowerorder,
so L>=p^r*2^Omega(eps*r*b). e=h-s-1~h, r²e/q=O(ell^-1/2). Thus
J/p>=1-O_rho,c(ell^-1/2), farpoint r/n outside, r->infinity. eta~c/b,
strictElias,c>Hrho, n=o(p), noCA. Numerical prescriptiono(p)ifc>c2Hrho.
Relative separation stillvanishes, gapstillshrinks; noactualglobal-list
separation. Replaces earlier weaker sqrt(ell) separation attempt; historical
derivation retained in note, final theorem uses b^1/6.

Verifier exhausts55000 domain/direction choices in F11: D=K2,N4,L6 and
D=K3,N5,L10; r1,2,3. Checks exactfirst/secondmoments, balancedT and uniform
paircap, plus1968hypergeometric identities and fullcodewordprofileofselected
lines. GuardedPASS<384MiB. MechanismfixturesnotEliasclaims. Makefile74checks.
PDF119pages; newLemma4.12/Corollary4.13 around34–36, visually reviewed1,2,34–36;
cleanbuild. Abstract/intro/README makegrowingcoordinateseparationclear and
retainvanishingrelativeseparation.

Possible nextprogress: finite multipadding exactcertificates at Mersenne
primes using existing gram/list bounds, r>=2. Need L>>p^r, q large vs
r²e to certifyhighdensity; existingone-matchtabledoesnottransferunchanged.
Or further theoreticalimprovement to growingfixedgapshortdomainlists.
Continue until12:30UTC; currentlyonly~06:00UTC.


## September 17 ~06:03 UTC — exact multi-coordinate finite certificates

Previousgoalturnprogresscommit2eb879916. Added floatingsearch
search_multi_match.py (expandedn<=40b afterr3besthitboundary), exactreplay
verify_multi_match_finite.py. New4rowtableonpage36: half-rate M127
(n694,K347,A356,r2) J/p>0.25107817, prescription<2^-40;
(n830,K415,A426,r3)>0.02273637 vs2^-40; M521
(n5840,K2920,A2936,r2)>0.59499256 vs2^-100;
(n8140,K4070,A4091,r3)>0.28599616 vs2^-100. Also M61/M1279 r2/3.
Allprime/Elias/Gram/count/prescriptioninequalitiesexact, guardedPASS.
Refinedaggregatebounduses(e-1)fallinsteadof(d-1)fallbecauseuniformpair
rootcap e alreadyproved; lemma explicitlynotesreplacement. Smallfixtures
replayedagainstrefinedboundPASS. Makefile75checks, PDF119pagesclean,
newpage36tablevisuallychecked. Noactiveprocess.

PROMISING NEXT THEOREM (notyetintegrated): dense lines with far distance
a FIXED POSITIVE FRACTION OF eta, rather thanonlycoordinatecountgrowth.
Use originalfar-paddinglemma with n=C*b (b=log2p), fixedinteger s,
K=rho*n, t=K+s+1,m~K/beta for fixedrho<beta<1. Anchoredsupportlog
~(rho/beta)*C*H2(beta)*b; fixeds momentcostO_s(logb). Pick
C>beta/(rho*H2(beta)) so L/p->infinity. Residualcollision~rho(1-beta)n,
q~(1-rho/beta)n, so nearbyfraction>=1-exp(-(beta-rho)/(rho*beta*(1-beta)))-o1.
Pickbeta near1 to make this>1-epsilon, thenCconstantlargeenough, then
fixedinteger s with(s+1)/C>max(Hrho,c2Hrho). Exacteta=(s+1)/n~c/b,
strictElias, numericalprescriptiono(p), farpointseparation1/n=eta/(s+1).
Thus for anyepsilon,c1,c2 obtain fixedkappa=1/(s+1)>0, fraction>1-epsilon
andfarpointkappa*eta beyondradius. kappa depends on epsilon/constants;
no assertiondensity->1 atfixedkappa. nTheta(logp), etaTheta(1/logp).
This may be conceptually stronger than growingcoordinatecount; verify
rounding/exactrate andpresentcleanly. Can amplifycoordinatecount by
multi-match withfixedr andnCb ifdesired butunnecessaryforthismessage.
Relativegapscale distinction could meaningfully sharpenintro.
Continuegoaluntil12:30UTC, current~06:03UTC.


## September 17 ~06:08 UTC — far separation proportional to eta

Previousgoalturnprogresscommitc4bce4d9. Implementedpromisingnexttheorem
fromlastentry, nowTheorem4.11 in gap_scale_far.tex. Foranyfixedrho,delta,
c1,c2 choosebeta withlambda=(beta-rho)/(rho beta(1-beta))>ln(2/mindelta1),
alpha=rho/beta,C>1/(alphaHbeta),fixedintegers>=1 with(s+1)/C>max(Hrho,c2Hrho).
n=Cb+O1 exactdenoms,m=alpha n,K=rho n,t=K+s+1. MomentcostO_s(logb),
logL>=alphaCHbeta*b-Ologb>b+Omega(b). Originalfarlemma gives
J/p>=1-exp(-lambda)-o1, eta=(s+1)/n, farpointdistanceθ+eta/(s+1).
Numericalthresholdp^{c2Hrho*C/(s+1)+o1}=o(p), strictElias. Fixedkappa
1/(s+1)>0 dependsontargetfraction/constants. DoesNOTgiveJ/p->1 atfixedkappa.
Gapstillshrinks, arbitrarypaddedintervals, noactualgloballistseparation.

Concreteheadline:rho1/2,beta15/16,C6,s6, alpha8/15. Exactentropyguard
15^15<2^59 provesCalphaHbeta>1. Nearbyfraction>1-exp(-224/15)>0.999999,
farpointeta/7outside, n~6log2p,eta~(7/6)/log2p, prescriptionfraction
p^-1/7+o1 for c1=c2=1. Otherchoicebeta3/4,C15/8,s1 gives>93% nearby
withfarpointeta/2outside; exactentropyguard3^5<2^8.

Exactfiniteverify_gap_scale_far.py passedguarded: M4423 n26520,K13260,
A13267,eta7/n,J/p>0.99999974,prescription<2^-619,farpointeta/7.
M2203 n4128,K2064,A2066,J/p>0.93155073,prescription<2^-126,farpointeta/2.
AlsoM521/4423halfgapandM9689seventhgap. AllGram/primality/Elias/count
comparisons exact; publisheddecimalsandparamsasserted. Only3.3sec/<384MiB.
Makefile76checks. Abstractandintro/README nowexplainfixedfractioneta
separation; introconcrete99.9999%example. PDF120pagesclean, reviewed1,2,33,34.
Noactiveprocess. Newtheoremstrongerconceptually thanmerelygrowingnumber
ofcoordinates; keepbothasdistincttrades.

Remainingresearchprioritystillfixedpositivegapshortdomainswithgrowing
lists/superlinearlinecount, or a domaintransfer relevanttobetter.codes.
Currentnewresultsdonotsolvethose. Goalcontinuesto12:30UTC.


## September 17 ~06:12 UTC — fixed-gap route audit and scope update

Previousgoalturnprogresscommite39368dc. Expandedbinomialsectionsearch
toALLj=0..r-1 at r2..48,k16,32,64,128 wheneverp2rk+1prime:989cases.
Newall_sections.cpp, scan/resources/summary, verify_all_sections.py.
ExactEliasfilter: c4 onlyknownDicksonr2j1k64p257; c8zero; c16six
withmaxk16; c32has261withmaxk32. No growingfamily ornewtheorem.
Independentintegerbinomial/fullcoset/fullcandidate replayof4fixtures
passes, includingnewr38j29k16. Coveragecheckerassertsalladmissible(r,k)
andallsections. Scan2.9sec, replay0.55sec, lowRSS. Initialsufficient
Eliasfilterhad260c32cases; finalexactcharacteristicfilterhas261 and
summarynowmatches. NoteappendedBINOMIAL_SECTION_SEARCH.md.

NewCOMPOSITION_GAP_LIMIT.md provesordinarydegreebarrier: monicFdegA,
monicG,HdegB,diffdega<B,charpnotdividingA =>
deg(F(G)-F(H))=(A-1)B+a. Cartesianinnercompositionlocatorfamilies
withsharedprefixK,degreeAB<=n<p requireeta=(AB-K)/n<1/A. Thus
independentinnerbranchingrequiresouterdegree<1/eta; nestedcomposition
cannotfreelymultiplylistsatfixedgap. Scopeexplicitlyexcludescoupled
outer/innerchoicesandgeneralreceivedwords. Elementaryproofonly, not
manuscriptclaim, complementsindependentproductlimit.

Paperapplicationsectionnowmentionsnewdensegap-scalefarresultwith
remainderqualification. Openquestionsadds: canJ/p->1 atfixedkappa>0
withfarpointkappa*etaoutside? Currentanyfixedfractionresultlets
kappadependonfraction; currentdensity->1 hasseparationo(eta).
PDF120pagesclean, reviewed58,59; builddone. Mainmakeverifycount76
unchanged (exploratorynewscancheckerkeptresearch-only).

Potentialrouteforthenewrobust-densityquestion: fixeds,n=C logp has
L/p->infinity, farpointeta/(s+1), butrootpairboundonlyprovesoutside
evaluationimage~p/n. Actualsubsetproductimagesmightbemuchlarger,
perhapsnearFp*, butwouldneedrealnumbertheoretic/equidistributionproof
underfixedmomentconstraints. DoNOTinferfromL>>p. Ifonepaddingpoint
hasimageFp*, wouldgiveallnonzeroznearbywithfixedkappa. Noevidenceyet.
Goalactiveuntil12:30UTC; noactiveprocess.
