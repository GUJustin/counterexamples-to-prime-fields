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


## September 17 ~06:20 UTC — exactly one far point at vanishing rate

Previousturnprogressa9fed246. Newtheorem4.15 integratedinvanishing_rate.tex
(inputatendaveraged.tex asSection4.3). Foranyfixedc1,c2 choosefixeds,K
withs+1>c2 andu=K-s(s-1)/2>c2K/(s+1), then1+c2K/(s+1)<a<u+1.
Everylargeprimep,n=floorp^(1/a),Kfixed,rhoK/n->0,eta(s+1)/n.
Anchoredt=K+s+1 supports on0..N,Nfloor2n/3, momentrangesO(N^j)since
tfixed, givingL=Omega(n^u). AfterdivideglobalfdegA-1,A=K+s+1,
candidatesdeg<K,coreagreementA-1. Withq=n-N,R=p-N,U=p-1,
M>=LR/(R+(K-1)(L-1)); qM/U=Omega(min(n,n^(u+1-a))).
Expecteduncovered<=p exp(-qM/U)<1 eventually, soALLnonzeroznearby,
zeroexactlyeta/(s+1)far. NoCAbyfdegree. Eliasfroma(s+1)>A;
prescription=n^(1+c2K/(s+1)+o1)=o(p). Polynomialfields,n=o(p).
ThisdoesNOTanswerfixedpositive-ratequestion, nowexplicitlyfixedrate
inpaperopenquestions. Noactualgloballistseparationasserted.

Simplec1c2=1:K2,s1,a5/2,n=floorp^.4,Nfloor2n/3. Triplesof1..N with
commonintegersumS giveL>=ceil(binomN3/(3N-8)); f=X³-SX²,
P=-(ab+ac+bc)X+abc. Allnonzeroznearbyat4agreements, zeroexact3,
far eta/2, rho=eta=2/n. Exactfinitecheckerverify_vanishing_rate_density.py
usesintegerfifthrootofp², exactL, conservativeM(nocorecollisionsubtraction),
96-termpositivebinomialsum. Eliascheckp²4^4>3^4n^4 andprescription
upper(3/2)n² viae<3 avoidn-digitintegers. GuardedPASS<1sec.
M31n5404density>0.45364109,prescfraction<2^-5. M61n22137669
missingfraction<2^-55,prescription<2^-11. M127n1960305596233800 and
M521CERTIFYJ=p-1 exactly (ceilcount, expecteduncovered<1). Theseare
existencecertificates, notexplicitdirectionenumerations.
READMEupdated, Makefile77checks. PDF122pagesclean, reviewed38,39.
VANISHING_RATE_ROBUST_DENSITY.md hasderivationandstrongerallnonzeroconclusion.
Noactiveprocess.

Furtherobservationfornextaudit: lowratephenomenonisevenpossiblefor
CONSTANTcodes alongprimesp=1modD. ChoosefixedintegerD>c2,
1+c2/D<a<2,n=floorp^(1/a),coreunionoffullDthpowerfibersN~n/2,
L=N/D constantsascodewords,w=X^D. OutsidecoreallP-w!=0 andevaluation
imagesizeEXACTL; q~n/2 randomnonzerodirectionscoverallnonzeroz since
qL/p=Omega(n²/p)>>logp. ThresholdA=D+1,K1,etaD/n, farpointeta/D,
strictElias aD>D+1, numericalthresholdn^(1+c2/D)=o(p).
Dirichletprovidesinfiniteprimesp1modD. Globalactualmaxlistfloor(n/(D+1)),
soactualell*n~n²>p; noactual-listcounterexample. Thisisanelementary
low-rateboundaryphenomenon, notnecessarilyanovelRSobstruction. Consider
simplifyingpresentationoraddingqualificationratherthanoversellingit.
Forc2=1 alloddprimesalreadyD2works; choosef=X²-(N+1)X andcore1..N
withN even, pairsx,N+1-x giveL=N/2 constants; n~p^.6 (a5/3) yields
allnonzeroznearby, far eta/2 atthreshold3, rho1/n,eta2/n.
Currentallprimearbitraryc2theoremstrongerthanconstantcodevariantin
primeuniformityandcorrect, so do notdeletewithoutreviewingtradeoff.
Goalactiveuntil12:30UTC; current~06:20UTC.


## September 17 ~06:26 UTC — simpler stronger constant-code formulation

Previousgoalturnprogressc7448974. The low-rate theorem is nowprovedfor
K=1 overEVERYsufficientlylargeprime, notjustprimes1modD. Keyelementary
pigeonhole: groupallbinom(p,D) moniclocatorsF byf=F-F(0), atmostp^(D-1)
groups. Onef hasOmega_D(p) fullD-elementfibers. ChooseD>c2,
1+c2/D<a<2,n=floorp^(1/a),L=floor(n/(2D)) suchfibers,coreN=DL.
Candidateconstantsarethefiber values. EveryoutsideimagehasEXACTsizeL,
allnonzero. Withq=n-N, expecteduncovered<=p exp(-qL/(p-1))<1 since
qL/p=Omega(n^(2-a)). AllnonzeroznearbyatD+1; zeroexactD,far eta/D,
etaD/n,rho1/n. Elias aD>D+1; prescriptionn^(1+c2/D)=o(p).
Becauseconstantcodeiscoordinate-permutationinvariant,thisholdsonANY
prescribedn-pointdomain. DoesNOTtransfertopositiverateonthatsamedomain.
Actualgloballist= floor(n/(D+1)), soactualell*n~n²>p, noactual-listclaim.

MainpaperSection4.3reframedasanelementarylow-rateboundarycase, not
mainfixed-rateobstruction. ReplacedmorecomplicatedmomentproofofTheorem4.15
withthisstrongerK1proof. EarlierallprimefixedKmomentvariantremainstrue,
savedvanishing_rate_moment_variant.tex (notinput), oldcheckerretained.
Newverify_constant_code_density.py exactfiberidentityauditsfor(p,D)
(5,2),(5,3),(7,3),(11,4), pluslargefieldcertificates. D2,c1c2=1 explicit
f=X²-(N+1)X,N=2floor(n/4),n=floorp^.6 givespairedcorefibers.
M31n397336density>0.99989788,prescription<1/4; M61n104159249330
andM127,M521 giveALLp-1nonzeroparametersnearby, far eta/2.
AllguardedPASS, <1sec. Exactprimality, sufficientElias p²>n³,
prescriptionupperceil(sqrt(3n³)), andexpecteduncovered<1.
Makefile78checks. PDF122pagesclean, reviewed38,39. READMEandnotesupdated.

Alsoauditedobviousrate-raisingattempt: addinghcommonzeroanchorsand
multiplyingbyVraisesratetofixedrho butpreservesgapO(1/n), whilep
polynomialinn implieseta logp->0. HenceaboveEliasatfixedpositiverate.
Thiscannotresolvefixedratequestion. Noactiveprocess.
Goalcontinuesto12:30UTC. Remaininghardtargetsunchanged: fixed-positive
rate robustdensity->1, or growingfixed-positivegaplists/superlinear
linecountonshortprime-fielddomains, or prescribed-domaintransferat
actualbenchmarkrates.


## September 17 ~06:32 UTC — cyclotomic support-lift audit

Previousgoalturnprogressed4c3419. Newcheck_cyclotomic_lift.py preserves
Dicksonsupportsetsbutmapsx=g^j inseedFp tozeta_n^j inQ(zeta_n), allowing
completelynewreceivedwordsandwitnesses. Modularranksatsplitauxiliary
primescertifychar0rankn-K: seeds17,41,97,193 haveauxq65537,65761,65761,
67777 andranks12,30,72,144, versusnative11,29,71,143. Prefixes7,11,11,15
supportsalreadysuffice. Distinctnodesensureinterpolationdenominators
specialize; globaldegree<Kwordskernelgivesmatchingrankupperbound.
Henceonlyglobalcodewordreceivedwordsonthesefixedcyclotomiclifts,
withallwitnessescoinciding. Strongerthanmerelytestingoldwordcoefficients.

Thencheck_cyclotomic_orbits.py restrictedtochi(a)=+1or-1 fullseed
orbits, droppingunusedcoordinatesbeforeinterpretingkernel. Allnodes
usedinthefixtures. Bothorbitsfullrankn-K forseeds41,97,193,257,337.
At17each4-supportsystemhasrank8andkernel8, underconstrainedsmallcase;
noasymptoticclaim. GuardedPASS, fullseed2.8sec, orbit7.9sec, lowRSS.
NewCYCLOTOMIC_LIFT_AUDIT.md documentsproofandlimits; AUDIT.mdlinked.
No manuscript changes; thesearesearchobstructions, notnewlistresults.

Possiblefollowup: exceptionalnewprimesannihilatingmaximalminors might
allowfixedsupportpatternsonrootsofunityovernewlargeprimefields, even
thoughchar0liftfails. Forq1modn musttestallprimitivezetaembeddings,
notjustone; rankcanvarybetweenprimeideals. A boundedmodularscan or
norm/gcd-of-minorsapproachcouldlocateexceptions. No suchsearchrunyet.
Couldalsoseekotherselectedsublists/movingdomains; currentauditsdonot
excludeallthose. Mainfixedgapshortdomainquestionstillopen.
Noactiveprocess; goaluntil12:30UTC.


## September 17 ~06:42 UTC — exceptional-prime census and complete n16 certificate

Previousgoalturnprogress909c4e6d. Newscan_cyclotomic_exceptions.cpp tests
everyprimitive-rootembedding forq1modn: n16/40 q<=100000,n96/192
q<=20000. Inputsareexactseed-supportlogindices. Counts1188,582,71,36
primesand9504,9312,2272,2304embeddings(total23392). Onlyexceptionsare
seedcharacteristics17,41,97,193 withrootgorg^-1,rankn-K-1. Nonewprime.
Independentverify_cyclotomic_exception_scan.py replaysall8exceptions,
2full-ranknewsamplesperseed,andprime/embeddingcoveragecounts. Guarded
scan20.3sec~2.4MiB,replay5.7sec.

Completeall-characteristicn16obstructionin cyclotomic16_integral_audit.py:
workZ[zeta16]=Z[X]/(X^8+1), clearLagrangerowsbyanchorVandermonde,
checkeverydeg<4monomialannihilated. Normalize4wordvalueszero, restrict
scalars:integer128x96matrix. Square96-rowminordetabs=2^161*17²;
rowlatticeindexviaHNF=2^151*17². Henceonlypossibleoddcharacteristic17
foranyprimitive-rootembedding(evenoverextensions); char2hasno16distinct
roots. Originalchar17works, givingcompleteclassificationforthisfixed
fullpattern. Nonzerominoralonealreadyprovesexclusion.
Initialdirect128-columnHNFhit384MiBguardandstopped; final96-column
modularHNFusesknownminordetmodulus,completes1.2sec~59MiB. Initial
failedreportretainedseparately. CYCLOTOMIC_EXCEPTION_AUDIT.mdexplainsall.
DoNOTgeneralizelarger-seedboundedscantobeyondcutoffsormovingdomains.

Paperclarification: actual-list-sizeTheorem5.1 nowexplicitlystates
ALLremainingp-Mlinepointshavedistance1-rho=theta+eta, maximumpossible
RSdistance. Thiswasalreadyimpliedbyexactnearbyclassificationplus
interpolationatKpoints; notanewconstruction. IntroandREADMEexplain
lineargloballists/exponentiallymanyuniquelynearbylinepointswithall
otherpointsmaximallyfar. Separatesconceptualmessagefromhuge-list
densefamilies. Addedexactfarprofileassertiontoexistingcurveendpoint
checker, plusaffinelinefixturee1,p101,n5,k2. Sevenfixturesnow, all
parameters/codewordsexhausted; guardedPASS. Makefilecount78unchanged.
PDF122pagesclean, reviewed2,40,41; finalparagraphsplitsforreadability
requirelastbuildcompletioncheck. Nootheractiveprocess.
Goalactiveuntil12:30UTC.

## 2026-09-17 06:50 UTC — independent headline audit and sharper concurrency

Independent density audit now replays gap-scale far certificates M2203,
M4423, M9689 with its own variance/root rounding, smooth collision bound,
32-term exponential estimate, and Lucas–Lehmer primality checks. No
construction imports. Bounds >.93155073, >.99999974, >.99999970 and
prescription <2^-126, <2^-619, <2^-1371 all PASS (3.35sec,21MiB).
Existing M2203 nearunit fixture now explicitly requests its box bound;
new M2203 gap-scale fixture uses the independent Gram bound.

Generalized existing quantitative incidence lemma (A.8) to either a far
DIRECTION or a far LINE POINT, and degree-e codeword graphs. If the far
word has maximum agreement a0<T, graph incidence <=floor(e(n-a0)/(T-a0)).
Proof: a identically matching coordinates <=a0; others have <=e roots;
qT<=qa+e(n-a). Coefficients/evaluation give a<=a0 in respective cases.
Applied to growing-far Cor4.14: r=floor(b^(1/6)), a0=A-r, concurrency
<=floor((n-A+r)/r)=O(n/b^(1/6))=o(n), uniformly over witness choices.
Degree-e version included. Intro/README state o(n) affine-graph bound.
This is elementary strengthening/application, not new construction.

New verify_far_concurrency.py exhausts 97,500 degree1/2 codeword graphs
over F5, K2,n5, both direction and point hypotheses (point z0=2),
several directions, all thresholds3,4,5; checks root incidence and final
bound. PASS2.31sec18MiB. Makefile now79checks. PDF122pages clean; rendered
pages37,69 and inspected. Existing asymptotic proofs remain written
mathematics, not formal verification. No live process.
Goal remains active until12:30UTC; currenttime~06:50UTC.

## 2026-09-17 06:53 UTC — broadened orbit search and domain optimality

Proved elementary full-orbit optimization lemma in
research/dickson_fixed_gap/ORBIT_DOMAIN_OPTIMALITY.md. For H=mu_L, L|k,
P_h=G(hX)-X^k, monic degG=k, n=qL<=p-1, max over ALL domains and words
of min_h agreements equals sum of q largest coset mode counts of G.
Averaging gives upper bound; modal full cosets attain. Addingzero gives
mean<=M+1-m_q/L<M+1, stillinteger min<=M. Thus earlier full-orbit
search cannot be improved by partialcosets/noninvariantwords/addingzero.
Scope only chosen complete subgrouporbit, not arbitrarysubsets/otherG.
Independentexhaustivecheck799domainfixtures10,816nondominatedwords
across5examples F7/F13 provesfiniteconsistency/attainment; PASS.

New subgroup_sections.cpp covers4,326cases, allj,r2..48,k16/32/64/128,
primep=2rk+1, subgrouporders4,8,...,k. CachesGvalues, exactmodularcounts.
Scan2.87sec3.1MiB. verify_subgroup_sections.py checkscoverage, fullorbit
rowsagainstpreviouscensus, exactEliasand8completecandidatefixtures
withintegerbinomialcoefficients; PASS~6sec35MiB. c4/8/16/32 belowElias
cases36/998/1908/2550,maxL64/8/16/32. c4maxL64isknownr2; outside r2
onlyL4except(r33,j0,k32,p2113,L8,n128,A43). No growingfixedgapfamily.
Results research-only; Makefile79checks/mainPDF122pagesunchanged.
Initialcompilehadnarrowingerror,fixedexplicitintcast; finalscanpassed.
Noactiveprocess. Goalactiveuntil12:30UTC, current06:53UTC.

## 2026-09-17 — quantitative density/separation tradeoff

Added derivation after gap-scale-far theorem: for fixedrho,c2 and
δ→0 across SEPARATE families, κ=Omega(loglog(1/δ)/log(1/δ)) is achievable.
For δ=2^-v, q smallestpoweroftwo>=max(2/(1-rho),2rho(v+1)/(1-rho)),
beta=1-1/q,C=2q/(rho log2q),s+1=floor(Cc2)+2. Entropylower
H(beta)>log2q/q ensures supportcondition; (s+1)/C>c2>=c2Hrho;
lambda>(1-rho)q/(2rho)>=v+1 ensures e^-lambda<δ/2. qTheta(v),
κ=1/(s+1)=Omega(logv/v). Roundedδextendsallvalues. This doesNOT
assertdensityto1withfixedκ. verify_density_separation_tradeoff.py
checks220rationalparameterfixtures exactly, PASS. Makefile80checks.
PDF123pagesclean, page34rendered/inspected. Nootheractiveprocess.

NEXT PROMISING UNIMPLEMENTED strengthening: choose shorter n~b*ell/c,
s~ell=log2b instead of n~b^1.5/sqrtell in nearunit theorem. With
h~2b/log2ell, supportlog~2b while momentcostO(ell^3)=o(b), so L/p→∞.
Then collisionresidual~h, q/h~(1-rho)/(2c)*ell*log2ell;
density1-exp[-Theta(ell logell)], eta~c/b, farfractionκ~1/ell.
This keeps farpointmuchlargerrelativetoeta than existingnearunit choice.
Potentialmulti-matchversion:s=ell,r=floor(ell^(1/3)),h~(3+eps)rb/log2ell,
log(n/h)~(2/3)logell; logL>rb, paircap~h,
r²h/n=O(1/logell), J/p>=1-O(1/logell), farfractionr/(s+r)~ell^-2/3,
numbermissingr→∞. Need completeconstant/asymptoticaudit, exactfinite
parameterchecker, THEN integrate. These are hypotheses/calculations,
not yet manuscriptclaims. General slowlygrowings mayyieldarbitrarily
slowlyvanishingκ but avoid assertingwithoutuniformproof.
Goalactiveuntil12:30UTC.

## 2026-09-17 07:02 UTC — slowly vanishing relative separation integrated

Completed the proposed parameter analysis. New Cor4.15 in
slow_separation.tex, proof audit SLOW_SEPARATION.md:
s→infinity, s^(5/3)log2b=o(b), n=sb/c+O(1), r=floor(s^(1/3)),
h=ceil(3(r+1)b/log2s),D=K+s,N=D+h. Supportlog>=(2-o1)rb;
momentcostO(s²logb)=o(rb). Uniformpaircap e=h-s-1~h,
r²e/(q-r+1)=(3c/(1-rho)+o1)/log2s. Existingmulti-matchlemma yields
J/p>=1-(3c/(1-rho)+o1)/log2s; eta~c/b; farκeta whereκ=r/(s+r)~s^-2/3,
r→infinity. NoCA,strictElias,o(n)graphconcurrency. Prescriptiono(p)
ifc>c2Hrho. Foranyepsilon(p)>0→0, take
s=floor(min(epsilon^-3/4,b^1/4)); κ>epsilon eventually andJ/p→1.
Intro/READMEstate this clearly; fixedpositiveκ withdensity→1 stillopen.
Qualitative arbitrarybuffer result also follows fromdiagonalization;
newparameterproof suppliesexplicitlengths/growingdeficits, notnewmechanism.

Companionone-matchchoice under s²logb=o(b): h=ceil2b/log2s,r1,
κ=1/(s+1), density>=1-exp[-((1-rho)/(2c)-o1)s log2s]. Samelemma.
Allthesedensefamilies stillhaveofflinelist>p: A=D+rsubsetsofthecore,
s+r-1moments,supportlog(2-o1)rb,momentcosto(rb). Notactual-listseparation.

verify_slow_separation.py audits7largeformalparameterfixturesusing
integerbitbounds (b=2^ell,s=ell,ell32..2048), including offlinelists
andone-matchvariant. AlsoexactM9689 instance:n62978,K31489,A31504,
r2,s13,m60570,J/p>.00563848,prescription<2^-5000,strictElias.
Thefiniteinstancevalidatesthemechanism,NOTnearunitdensityatthatprime.
PASS~2.9sec22MiB. Makefile81checks. PDF124pagesclean; rendered38/39,
finalpage39inspected. Noactiveprocess. Goalactiveuntil12:30UTC.

## 2026-09-17 07:16 UTC — MAJOR cubic-domain route, integration pending

NEW research/cubic_domain_warp/ contains a written proof apparently
closing fixed-positive-relative-buffer at density1: ALLp-1nonzero
parameters nearby atfixedpositive rate, withzeroeta/u outside forANY
integeru>c2. ShrinkingetaTheta1/logp,nTheta(logp), belowElias,
noCA,prescriptiono(p). Forc2=1,u2 giveseta/2far. NOTyetinputinmainpaper;
nextstep adversarial reread thenintegrate/promoteandfixstaleopenclaims.
MainPDFcurrently124pages, oldclaimsunchangedexceptofflinemomentfixbelow.

Mechanism: match3s integerseedmoments, then cubicwarp
phi_(a,b)(i)=i³+b i²+a i. Firsts moments remain equal. Injectiveonseed
for>=p²-binom(m,2)p parameterpairs. Foranysupportpair cancelcommon
nodes: residualcollisionequation product(X-phi(i))-product(X-phi(j))
is ABSOLUTELY IRREDUCIBLE in(X,a,b). Selfcontainedproof inproposed.tex:
homogeneousplanes l_i=X-iU-i²V-i³W areinP3generalposition(Vandermonde).
EachbaseA_i=B_jline liesonuniquecomponent; triplepoints2A1B or1A2B
smooth,connectingallbaselinesononecomponentG. RestrictGtooneAplane:
itcontainsu distinctB-lines ⇒degG>=u=degreeF ⇒Firreducible.
DehomW1valid,Wnotfactor. u1linearhandled. Carefullyrereadthisproof!

PrimaryCafure–Matera2006PDFdownloaded/read. Cor5.6 printed174:
ifp>2d², absirredaffinehypersurfacein3vars degree d haspointcount
<=p²+(d-1)(d-2)p^1.5+3d4p. SourceauditURL/hashsaved; localPDFin tmp.
Thusonegoodmap totaloutsidepaircollisions<=binom(L,2)*B,
B=[p+(t-1)(t-2)sqrtp+3t4]/[p-binom(m,2)]=1+o1 formlogp.
CauchymeanimageM=LR/[R+(L-1)B]~p whenL>p^(1+eps).
qTheta(logp) paddingcoordinateswithnonzerorandomdirections give
expectedmissing U(1-M/U)^q<1 ⇒allnonzero labelscovered. Farw=H0/X
hasdegreeD=t-1, selectedP=(H0-Hi)/X degree<K=t-s-1, agreementDcore.
Anchorimage0canbeusedasnewpaddingpoint: cancelcommonanchorBEFORE
residualequation; remainingcommonfactorsrootsonlyincore,soequivalence
holds alsoat0. NoavailablepointomittedfromR=p-(m-1).

Allprimeparams: rho<beta<1,alpha=rho/beta; chooseC between
1/(alpha Hbeta) andu/(c2Hrho) possiblewithbetacloserho,u>c2.
s=u-1,n=Cb+O1,K=rhon,m=alphan,t=K+s+1. Fixed3s momentcostOlogm,
L>=p^(1+eps). eta=u/n,far1/n=eta/u. Source/geometry/finitechecksallPASS.
Mainproofinputproposed.tex isNOTyetreferenced; bibkeycafure-matera
mustbeaddedbeforeintegration. Actualglobal liststill>p asymptotically:
coret-subsetswith3(s+1)moments preserve s+1 prefix ⇒deg<K, count>p.
NoFFT/benchmarktransfer,no fixedgap superlinearclaim.

Exactcerts verify_finite_certificate.py usingGram+Cor5.6:
M1279 n3834K1917m2556A1921 seedmom9→3,q1279,ALLp-1nonzero,
farη/4,strictElias,prescriptionfraction<2^-307,listbits1653.
M9689 n18162K9081m12108A9083 seedmom3→1,q6055,ALLp-1nonzero,
farη/2,strictElias,prescription<2^-591,listbits9724.
Independent audit_finite_independent.py importsNOconstructionhelpers;
anchoredmomentBOXcounts1547/9702bits, weakerTheorem5.2error5t5;
separateLucasLehmer; both proveM/U>3/4 and2q>=b ⇒expectedmissing<1.
Eachguarded~2.3sec20MiB. GeometrycheckerF7/17/23/37u1..4 checksall
surfacepoints,Vandermondeminors,smoothtriplepoints; F131anchored
Thue–Morsepairmatches3moments,all5692injectivecubicmaps preserve
candidate deg<7, coreagreement8; totaloutsidecollisions5095. PASS1.7sec.
These areexistencecerts, NOTexplicitlistedmassivecodewords/directions.

CORRECTIONcaughtduringnewaudit: slow-separationofflinelistparagraph
requires s+r moments, nots+r-1 (unanchoredlocatorsneedA-Kmoments).
Fixedtex/note/checker; strengthenedintegerchecksPASS; asymptoticcost
andconclusionunchanged. Rebuilt124pagePDFclean. EarlierTAKEOVERentry
s+r-1 ishistoricalincorrectindex. Noactiveprocess. Goalactiveuntil12:30UTC.

## 2026-09-17 07:32 UTC — cubic theorem promoted, smaller certificate

Final adversarial review passed; see cubic_domain_warp/FINAL_PROOF_REVIEW.md.
Mainpaper now inputs cubic_warp.tex (renamedfromproposed.tex), Section4.3,
Lemmas4.16–4.17,Theorem4.18. Abstract/intro/READMEleadwithallnonzero
nearby andzeroeta/2outside atfixedratebelowElias. Formerfixed-kappa
openquestionremoved; replacedwithcompletecoveragePLUSuniqueness question.
Newconstructionnecessarilyhaslocalambiguity (L>p atonepaddingpoint).
Fixedgap/FFT/actual-list limitationspreserved. SourcebibCafure–Materaadded.
Oldlowrateintrocorrected: itsfeatureisallprescribeddomains,notfirstfull
puncturedline anymore. SLOW/DENSEscopenotesupdated. Makefile84checks.
PDF127pagesclean; renderedintro1–3andproof40–42; finaltable42inspected.

NewindependentlyverifiedM127row:n214,K107,m202,t109,s1,originalmom3,
q13,allp-1nonzeronearby,farη/2,strictElias,prescriptionfraction<2^-12.
PrimaryGramlist151bits, independentanchoredbox137bits; bothcheckexact
missing-labelrationalpower<1 (independentusesintegercross-products).
Largerrowsboundsimproved: M1279<2^-308, M9689<2^-593. All3primaryand
independentreplaysPASS~2sec20MiB. ExistinggeometrycheckerunchangedPASS.
Finitecoveragecheckernowallowsarbitraryn,m; smallrowsdirectpower,
largerrowsuseM/U>3/4 and2q>=b toavoidmassiveexponents.

Boundedexact search_small_certificates.py covershalf-rates1,b<=n<=2b
forM31/61/89/107/127. NoM31cert;M61smallestn120,m113 (fullcoverage
but DOESNOTbeatc1=c2=1numericalbound). M89n156,m143 Gramcertbeatsbound
butboxfails; M107n176,m165primary andn190,m181box; M127n200,m186primary,
n214,m202box. Searchrecordsbeats_prescriptionflag; absenceisnotnonexistence.
Allscannedcaseswereexactarithmetic; nofloatingcertification. ~1.1sec21MiB.

NEXT PROMISING EXTENSION (NOTYETPROVED/IMPLEMENTED): efficient randomized
construction mayfollowfromsamegeometry, removingneedtofindthelargeclass
orlargestimages. UniformlysampleanchoredsupportS; momentpartitionhasatmost
Rvec classes, totalQsupports, soP(classsize<Lmin)<=Rvec*Lmin/Q.
Chooseuniformcubicmapconditionedoninjectivity (efficientrejectionsampling).
ForactualclassL, define E=sum_outside_x sum_v r_xv²; deterministic
E>=R*L²/U sincevaluesnonzero, U=p-1. Good-map meanE<=LR+L(L-1)B.
ThusD=U*E/(R*L²)-1>=0 hasmean<=U/L+U*B/R-1.
ForL>=Lmin upperdelta=U/Lmin+U*B/R-1. MarkovP(D>gamma)<=delta/gamma.
WhenD<=gamma, meanimage>=U/(1+gamma). RANDOMqdistinctoutsidepoints
andrandomnonzerodirections havemeanmissing<=U*(gamma/(1+gamma))^q:
useMaclaurin/elementary-symmetricmean inequality forsamplingwithoutreplacement.
Failurebound<=Lmin/(Q/Rvec)+delta/gamma+U*(gamma/(1+gamma))^q.
Allquantitiesexact. ChooseLmin betweenp andQ/Rvec andconstantgamma
smallenoughq/logp→positive; success1-o1. Algorithmonlyneedsrandomsupport,
cubicmap, randompadding,directions; w=locator(mappedS)/X computable
poly(logp), noenumerationofmomentclass/witnesses needed! Recheckfullproof.
Couldyieldpolylog-time randomizedconstructionwithhighprobability, while
nearbywitnessrecoveryremainsunresolved. FiniteM521paramsn~990,m~900
likelygivefailure<2^-100; hypotheticaluntilchecked. DoNOTclaimanindividual
sampledeterministicallyverifiedjustbecausegeneratorhasfailurebound.
Noactiveprocess. Goalactiveuntil12:30UTC.

## 2026-09-17 07:58 UTC — efficient sampler integrated and replayed

The proposed randomized extension is proved and integrated in randomized.tex.
Failure <= H/mu + delta/gamma + (p-1)(gamma/(1+gamma))^q,
delta=(p-1)/H+(p-1)B/R-1. Size-biased moment classes, Markov on
collision excess, and elementary symmetric sampling without replacement
give success 1-p^-Omega(1), expected O(n²) field operations. No moment
class enumeration and no nearby-witness recovery required or claimed.

Finite M521,n990,K495,m900,t497,s1,q91,H=p*2^150,gamma2^-8:
exact failure<2^-137; independent integer replay each term<2^-130,
hence total<2^-128. Actual random sample samples/m521_n990.json has
990 coordinates and SHA25648469ccd5bbf61813ea26428b4eea71f5b8e240e099b354678450fc78d89d214.
Independent direct-root-product replay checks all coordinates, prime,
exact maxagreement496 at zero, strict Elias, prescriptionfraction<2^-16.
Complete coverage is a generator probability guarantee, not a deterministic
certificate for this individual sample. Sampling identity checker covers
16806 coordinate/direction choices and8008 symmetric-mean inequalities.
All new bounded checks PASS; Makefile87 check commands.

Strongest cubic section moved ahead of weaker interval refinements.
PDF128pages, 1-inch margins, article, no warnings; sampler page35 visually
inspected. Main theorem now4.12, randomized proposition4.13; use labels.
Goal remains active until12:30UTC (08:30Eastern), >4hours remaining.
No active numerical jobs; no push/publication.

## 2026-09-17 08:23 UTC — paired blocks give almost the entire gap

MAJOR NEW RESULT integrated in research/paired_domain_warp/paired.tex.
At every fixed rational rate and every sufficiently large primep, ALLp-1
nonzero line parameters are nearby; zero has exact distance1-rho-1/n,
one coordinate short of the maximum RS distance. Separation can be
(1-o(1))*eta, radius strictly below Elias, n*2^(Hrho/eta)=o(p).

Construction: corem random nonzero sign-orbits ±a_i; allD-subsets I
give H_I(X)=prod(X²-a_i²), w=H_0, P_I=w-H_I ofdegree<=2D-2.
K=2D-1; q padding blocks ofr sign-orbits each. Shared pair directions.
A block hit gives2r extraagreements, thresholdK+2r+1, faragreementK+1.
Exactrateparity handled by optionalzero coordinate and optionalX factor.

Fourier collision proof uses BGKS arXiv1110.0812v2 Lemma17 (primary
PDFpage10 read). For fixed outside block, seed distribution onFp minus
0,±x_j has all nonprincipal Fourier coefficients<=(4r+2)/sqrtp.
Joint group(Fp*)^r. Distinct-square conditioning probability>=1-2m²/p.
Support pairs with differenceu<=r have ZERO collisions (residual monic
degreeu locators inY differ degree<=u-1, cannot vanish at rdistinctY).
Other pairs bounded by character mixing. L=binom(m,D), and
 delta=p^r/L+((4r+2)^(2r+2)+2m²)/(p-2m²).
Generator failure <=q*delta/gamma+(p-1)*(gamma/(1+gamma))^q.
No block-goodness independence assumed; union+Markov. Directions ARE
independent conditional on core/blocks. Algorithm expectedO(n²)fieldops.

Fixedr: chooseC between2r/(alpha Hbeta) and(2r+1)/(max(1,c2)Hrho),
possible for c2<1+1/(2r). n~Cblog, farfraction2r/(2r+1).
Growingr: ANYr→infinity withr logb=o(b), H=Hrho,J=-log2(1-rho),
t=1/(4J), n=(2r+.5)b/H+O1, m=(n-tb)/2+O(r), D=rhon/2+O1.
Thenlog2L=rb+b/8+O(b/r+r+logb), soL>=p^(r+1/9).
Choosegamma=p^-1/20, q~tb/(2r)→infinity; failurep^-Omega1.
Eliaseta*b-H=Theta1/r dominatesentropychangeO1/b. Prescriptionlog
log2n-b/(4r+2)+O1/r→-infinity. Take r=floorlog2b forlengthTheta(b logb).
This defeatsc2=1; arbitraryfixedc2 still uses separate cubic theorem.

Proof audit PROOF_AUDIT.md has15 checked steps; SOURCE_AUDIT.md records
primarycharacterinput andlimitedKKH/Kambire comparison (notnoveltyproof).
Primary exact finite rows and independentcoarserintegerreplay allPASS:
M521 n1458r1 far2/3 fail<2^-134 prescription<2^-24;
M521 n2518r2 far4/5 fail<2^-128 prescription<2^-6;
M1279 n8678r3 far6/7 fail<2^-298 prescription<2^-26;
M1279 n13782r5 far10/11 fail<2^-284 prescription<2^-12;
M1279 n26218r10 far20/21 fail<2^-60 prescription<2^-15.

Actual random sample samples/m521_r2_n2518.json (672066bytes):
SHA2560223dc5525c02b5bc79d77342e718af0dd3d1e8323e06653a59cdc9712d7d635.
Independentdirectrootproduct replay all2518coordinates, farmaxagreement1260,
far distance1258, threshold1264, prime/Elias/probability PASS~2sec22MiB.
ProbabilityguaranteeOVERGENERATOR, NOT deterministicallsamplecoverage.
No nearby-witness recovery. One can optionally reserve one paddingblock
for knownwitness atz1; notyetimplemented and notneededfortheorem.

ExactFourieridentitychecks useintegerconvolutions andcyclotomicreduction
overF11r2/r3 andF19r2; exhaustivejointimagesF23r2,F29r3; paritycheck
allcodewordsatfarpointforall3paritycasesoverF11. AllboundedPASS.
Simpleonepaircurveproofretained single_pair.tex (notintegrated); smaller
M127n318 existencecertificate far2/3; multiblockboundtoo weakatthatrow,
so doNOTclaim highprobabilityfrommultiblockthere.
Makefile94checks. PDF132pages, article1-inch margins, no warnings.
Renderedintro andnewproof/tablepage35 inspected. No numericaljobactive.
GoalACTIVE until12:30UTC (08:30Eastern), stillabout4hours remaining.


## 2026-09-17 09:09 UTC — completed product image, exact affine geometry

Stronger result integrated in research/paired_domain_warp/completion.tex.
A single padding block of r sign-orbits now suffices. For every z in Fp^r,
exact distance is 1-rho-(1+2 wt(z))/n. Nearby locus at eta=(2r+1)/n is
exactly (Fp*)^r, with pairwise disjoint decoding lists. Every full-support
line direction changes only 2r coordinates (minimal for the improvement).
Exceptional point remains one coordinate short of maximal RS distance.

Construction completes the base D0-subset product image by t pairs of new
core orbits, choosing exactly one orbit from each pair. For missing fraction
h, expected new missing fraction is at most Phi(h)=(h^2+C^2 h/p)/(1-4/p),
C=4r+2, uniformly over the entire past when p>(n+1)^2. Fourier/Parseval on
the intersection of two translates proves this. Initial expectation d0 is
the original energy bound with m0,D0. Successive averaging gives existence
if (p-1)^r Phi^t(d0)<1; threshold Markov/union gives sampler failure
 d0/h0 + sum_i Phi(h_(i-1))/h_i.
For r log b=o(b), n=(2r+4/5)b/Hrho+O1, t=16(r+1), base list has log2
rb+2b/5+o(b). Initial missing <=p^-1/8 with high probability; each step
reduces by p^-1/16 except probability4p^-1/16. Complete image after t.
Elias and prescription follow; far separation tends to entire eta ifr grows.

Exact certificates, primary + independent weaker C=4r+4, p-8 arithmetic:
M61 n158r1 direction2, existence, prescription<1/2; M127 n294r1 direction2,
existence, prescription<2^-20; M521 n2518r2 direction4 failure<2^-88;
M1279 n8678r3 direction6 failure<2^-228; n26218r10 direction20 failure<2^-123.
All strict Elias. Canonical primary rows now include M61/158 and M127/294.
Six new completion checks pass sequentially under384MiB (~4sec40MiB).
COMPLETION_PROOF_AUDIT.md records proof/quantifier review.

New actual sample completed_samples/m521_r2_n2518.json, SHA256
6d44a20b422122f4234e1f8a4fd5dd410763a78024b558bcf130b0a35935f318.
Generator m0=1241,D0=622,t8; direction=-f onpadding, weight4, zero codeword
nearest atz1. Deterministic exact distances1258/2518 atzero,1254/2518 atone.
Full coverage is probability OVERGENERATOR, NOT individualcoveragecertificate.
Original block sample remains separate (weight96,failure2^-128).

New Cor pd:witness-extension: any degree-e polynomial codeword graph hits
at most floor(e(n-K-1)/(2r)) nearby parameters; selecting all p-1 requires
degreeOmega(p/logp), not a computationallowerbound. Over any extensionE,
nearby torus is precisely(Fp*)^r and listsunchanged (interpolation onKcore
coordinates forcesbasecoeffs). On a scalar line everyzoutsideFp has EXACT
far distance1-rho-1/n: applyFp-linear functional lambda1=1,lambdaz=0 to any
codewordagreement; zero codeword attainstheK+1referencecoreagreements.
verify_extension_profile.py exhausts4368interpolationsF17n16K5, coversall
289 quadraticextensionparameters:16nonzero base distance8,272outside+zero
distance10;16disjointlists contain35codewords. No belowEliasclaimforthistoy.

Intro,abstract,README updated; PDF134pages, article1inch, cleanbuild.
Makefile100checks. Latestnewproof/table rendering inspected; finalintro and
extensioncorollary renderedunder tmp/completion-final-page-* forinspection.
No active numericaljob; no push/publication. GoalACTIVE until12:30UTC.

better.codes scope rechecked: fixed KoalaBear prime2130706433, extensionFp^6
(NOTquartic), n262144,k131072,8rows, winningdensity>2^-128 needsabout2^58
nearbylabels, largerthanp. Incumbent116.13, pinnedcdb451f13fdc6c84f5fe363e77ee13a89bd30974.
Newbasefieldline doesNOTimprove it. Archiveagents/better_codes_scope.md and
better_codes_construction.md have detailed benchmark audit. Do not conflate
our earlierM31quarticexample withthisbenchmark.

Potential next research: uniform multiplicities follow by declaring base
outputs with fewer than L0/(2V) witnesses bad; their density <=4Delta by
variance. Same completion fills this good set, giving minimumlist>=L0/(2V)
at everyfull-supportparameter; partialparameterweightj wouldhaveatleast
(p-1)^(r-j) times that manynearestwords. This is reasoned, NOTyetintegrated
orverified. Consider whether it improvesmessageenough to merit inclusion.


## 2026-09-17 09:53 UTC — deterministic unique witnesses, exact M31 lists

Major additional strengthening integrated. PDF139pages, article1-inch margins,
cleanbuild. Renderednewdecoderproof andM31listtable inspected. Makefile108checks.
Noactive numericaljobs. GoalACTIVE until12:30UTC (08:30Eastern), ~2h35left.

New files research/paired_domain_warp/unique.tex andpowers_two/deterministic.tex.
Exactlistcriterion: g supportedpadding±1, nearbythresholdK+3. AnynearbyQ must
matchbothpaddingandK+1nonpaddingcoords. H=F-Q monicdegreeK+1, coefficientX^K=0,
soitsroots sumzero. Cancel fullsign-orbits; remaining singles giveeps_i∈{-1,0,1}
withsum eps_i a_i=0 andprod((1-a_i)/(1+a_i))^eps_i=1. Ifonlyzerorelation,
EVERYnearbycodeword ispairedlocator, so listsare EXACTproductfibers. Optionalzero
root forced/excludedbyparity; all3paritycasesexhaustivelychecked.

Genericrandomunique theorem: n=.5log2p+O_rho1,m=.25log2p+O1. Invaliddomain
prob<=(m²+2m)/p; productcollisions<=2m4^m/p; nonzero ternaryrelations<=m3^m/p².
Foru>=3 eliminatesum, polynomialnonzero byspecializationX,Y,-X-Y gives±2XY(X+Y).
u1,2impossiblevaliddomain. Totalfailurep^-1/2+o1. Exactnearcountbinom(m,D),
ALLnearbyunique, far1-rho-1/n,near1-rho-3/n. Numericalc2<1.5defeatedexp(n),
strictEliaseta logp→6. Thisisnotfullnonzero coverage; no globalellbound.

DETERMINISTIC POWERS-OF-TWO FAMILY: a_i=2^i. Let1<=D<m and
p>2^[D(2m-D+1)]. All D-subsetpositiveproductsT_I=prod(4^i-1) are<p; also
sumcoremagnitudes<p, so ternarysumaloneforceszero bylargest-powerdomination.
Productsareinjective ELEMENTARILY: T=4^s U,s=sumI,2/3<U<=1, sobitlengthT=2s.
Atindexi residualU<=1-4^-i iffi∈I, becauseallfuturefactorsproduct>
1-(1/3)4^-i. Thisgivesintegergreedydecoder, nofactorization/Zsigmondyneeded.
Lift(-1)^(D+1)z modp tot, recoverDsupport, returnreference-minuslocator
(optionalXfactor). Exactclassificationmakes thisa WHOLELINEnear/fardecider
anduniquewitnessrecovery, deterministicpoly(logp). Allfixedrationalrates,
alllargeprimep, nTheta_rho(sqrtlogp), eta3/n, strictElias, c2<1.5violated
exponentially, exceptionalpointonecoordinatebelowmaxRSdistance.

TWOLEVEL REFINEMENT (unadjustedn2m+2,K2D-1 only): additionally
p>2^[m(m+1)/2+2m+2] ⇒EVERYnonbankparameterhasexactfar distance(n-K-1)/n.
ProofatK+2agreements: with2paddingandKknowncoreroots,lastroot=-sumroots.
Cancelpairedroots; remainoddnumberuof signedpowers. u1completespair(bank).
u>=3 paddingequalityrequiresF=(1+S)prod(1-y)-(1-S)prod(1+y)=0modp.
F/2=(Se2-e3)+(Se4-e5)+... uniqueleast2-adictermis u0²v0 forsmallest
magnitudepowers2^a,2^b; valuation2a+b. Fnonzero,|F|<statedfieldbound.
Onepaddingmatchforcespairedlocatorandhenceboth. Zeroalwaysattainsfar.
DoNOTextendtwolevelclaimtooddK+optionalzero: deliberatefixturehasmiddlelevel.

Finitefullydeterministicrows powers_two/verify.py (independentrationaldecoder):
M521 n74K15D8m36 exactJ30260340, beatsc1=1; no twolevelclaim.
M1279 n82K41D21m40 J131282408400, ratio>2^3; twolevelnear38/82,far40/82.
M2203 n106K53D27m52 J477551179875952, ratio>2^6; twolevel.
M9689 n226K113D57m112 J383737587959312915862780874001472, ratio>2^25;twolevel.
Storedpowers_two/deterministic_instance.json isM1279n82 fullcoordinates and
3explicitwitnesses; classificationDETERMINISTIC,not samplingguarantee.
check.py32,738exhaustivesubsetdecodings; verify.py256largesupportrecoveries;
check_two_adic.py59,028signedvectorsvaluation; check_two_levels.pyexhausts
allinterpolationpencils, classifiesENTIREfieldsincluding61-bitfield. PASS.
UNIQUE_PROOF_AUDIT.md recordsallproofobligationsandlimits.

CONCRETE M31 EXHAUSTIVE BANKS m31_exact/: n58K27J39763294;
n62K31J140916078; n64K31J281212602; n68K33J897817238 (lastbeatsc1=2).
TwoindependentC++enumerators MITM/Mersennemod versusrecursivecomplements/%mod
agree. Each256MiBbitmap, whole4rows~60sec<300MiB. Smallcorecoordinatesprinted
inpaper; sourcecompact, nobigbitmap retained. verify.pyrecovers16witnesses.
For n62ONLY, twoindependentternaryrelationchecks(3^15eachhalf,219MiB)prove
onlyzerorelation. Twoindependentsegmentedhistogramcountsgive EXACThistogram
listsizes0..5:[2006567569,136494714,4337028,83442,891,3]. Thus136494714
UNIQUELYnearbyparametersalonebeatB<103199661, everypointonthislinehaslist<=5.
NOTglobalell<=5. verify_local_lists.py~37sec<285MiB PASS.

OPTIMIZED COMPLETION CERTIFICATES: optimize_completion.py searchesfineupward
fixedpointrecurrenceswithweakerC4r+4andp-8. audit_optimized_completion.py
independentlychecksinequalities,nohelperimports. Newmaintable:
M61n158r1existpresc2^-1;M127n294r1exist2^-20;
M521n1090r1exist2^-147;n2142r2exist2^-81;n2414r2fail2^-64,presc2^-26;
M1279n7742r3exist2^-160;n8014r3fail2^-64,presc2^-121;
n25970r10fail2^-64,presc2^-27. AllstrictElias. Searchnotoptimalityproof.
OriginalM521n2518completion sample remains, failure2^-88, direction4.
The tabledistinguishesexistenceandrandomizedrows. ExactM31banksareseparate.
Erdos-Renyirandom-translatestrategycredited (primary1965paperTheorem2read).

CURRENT NEXT RESEARCH IDEA (notyetproved/integrated): replacepairsbyorbits
ofprimeorderd, tocombineUNIQUENESS+efficientdecodingwithfarfractiond/(d+1)
arbitrarilyclose1. Forp≡1modd, primitiveω, core2^iω^j (i1..m,j0..d-1),
paddingω^j, c<dextra singletons2^(m+1)..2^(m+c). n=d(m+1)+c,K=dD-1.
Referencew=prod(X^d-2^(di)), g1padding0else. Candidatesdeg<=dD-d<K.
FaragreementK+1=dD, nearK+d+1, eta(d+1)/n, sep d/(d+1)eta.
ANYnearQmustmatchallpaddinganddDcore/extraroots; theirsum0modp.
Liftroot sumtoZ[zeta_d]. Boundabsolutealgebraicnormby
 A^(d-1), A=2^(m+1)(d+2^c). Ifp>A^(d-1), modpzero forcesalgebraiczero.
Forprimed, minimalpoly1+...+X^(d-1), soallcoefficients(rootmembershipbinary
sums)equal. BinaryuniquenessforcesfullorbitsandNOextrasingles. ThusEVERYnearQ
isourlocator. Labels(-1)^(D+1)prod(2^(di)-1), injective/greedydecodedby
samebase2^dargumentifp>2^[dD(2m-D+1)/2]. Normboundalsoensuresdomainnocollisions.
Forrho=a/breducedandprimednotdividinga, choosen=btwithat≡-1modd, c=nmodd,
m=(n-c)/d-1,D=(rhon+1)/d. Allfixedrho realizablebychoosinglargeprimedavoidinga.
Primesp≡1modd only (infinite, notallprimep). nTheta_{rho,d}(sqrtlogp),
logJ=nHrho/d+Ologn beatsc2nHrho/(d+1) wheneverc2<1+1/d, inparticular1.
Givenωdeterministicconstruction/decoder; ωcanbefoundLasVegasbyh^((p-1)/d)
withsuccess1-1/dpertrial. Avoidclaimunconditionaldeterministicpolylogrootfinding.
Possiblefinitehalfraterows: d3,M9689,D46,m90,n274,c1 (factor~2^9);
d5,M19937,D52,m102,n518,c3 (factor~2^2);
d7,M44497,D65,m128,n908,c5 (factor~2^1).
KnownMersenneprimesbutneedactualLLchecks; fastMersennefoldreductions
s=(s*s-2 &p)+(s*s-2 >>b), subtractpifneeded, savehuge%cost.
No gmpy2installed; sympyavailable. Theseorbitideasareunpromoteduntilproofaudit,
finitechecksandnorm/cyclotomic/domain/paritydetailsresolved.

## 2026-09-17 10:15 UTC — audited orbit strengthening

The prime-order orbit idea above is now proved, independently checked, and
integrated as Section 4.3.4 (`research/orbit_unique/orbit.tex`). The paper is
142 pages, full-margin article; clean TeX build, new proof page visually
inspected. PROOF_AUDIT.md records the norm/resultant, root classification,
rate congruence, product decoding, and algorithmic qualifications.
All three finite Mersenne fields were Lucas-Lehmer certified twice; saved
roots independently satisfy exact order; all domain points are distinct;
48 support recoveries and six full polynomial witnesses passed. The d=7
ratio is >1, not >2 (correcting the provisional estimate above).
Small fixtures exhaust 2,048 / 8,192 / 524,288 subset sums and 792 / 12,870 /
3,060 interpolation pencils. Primality of their fields is checked too.
Makefile now includes 111 check commands including verify-overnight. All newly added checks passed.
The paired powers-of-two two-level theorem now explicitly notes both
f and f+g are far; its five exhaustive fixtures were rerun successfully.

Orbit conclusion: for every fixed positive epsilon, suitable infinitely
many prime fields admit unique efficiently recoverable nearby witnesses,
separation >=(1-epsilon)*eta, and exponential violation of the c2=1 bound.
Length Theta(sqrt(log p)); sparse nearby bank. Given omega deterministic;
finding omega is zero-error Las Vegas. NOT full coverage, NOT a global
list bound, NOT a prescribed FFT domain or better.codes improvement.

Continue research until 12:30 UTC (8:30 Eastern). Next possible improvement:
random scaled prime-order orbits can give uniqueness and near-full gap
at length Theta(log p), though efficient arbitrary witness recovery is
not known. A union bound over nongenuine zero-sum subsets costs 2^(n-d)/p;
product collisions cost dD*binom(m,D)^2/(2p). For prime d, every proper
nonempty subset of roots of unity has nonzero sum if p>d^(d-1), by the
same small-resultant argument. Independent random orbit scalars and extra
coordinates make each forbidden subset sum a nonzero linear equation.
This extension remains provisional until independently tested/audited.

## 10:24 UTC working notes — not yet promoted

A logarithmic-length random-orbit theorem is drafted in
research/orbit_unique/random.tex, with check scripts verify_random.py and
check_random_geometry.py NOT YET RUN. Exact failure bound before valid-
domain conditioning: [binom(n,2)+2^(n-d)+dD*binom(binom(m,D),2)]/p.
For n=alpha log2p+O(1), alpha<1, this is p^(alpha-1+o(1)). Gives near-full
relative gap, unique lists, J=p^Omega(1), but no arbitrary witness decoder.
The 110 main Makefile checks are running sequentially in session37155;
currently check108. Need run the separate verify-overnight prerequisite
as well: total Makefile check count is 111, not 110. Wrapper clang++ is
in tmp/eprint-replay-bin. Do not start another numerical job until done.

NEW PROMISING DETERMINISTIC FINITE STRENGTHENING (still provisional):
Replace core 2^i*omega^j by alpha^i*omega^j, i=2,...,m+1, where alpha^d=2
and omega has prime order d. Extra coordinates alpha^(m+2)...alpha^(m+c+1),
padding omega^j. n=d(m+1)+c, K=dD-1. Work in Kummer splitting field
Q(2^(1/d),zeta_d), degree d(d-1): degrees d and d-1 coprime prove this.
A root sum groups powers alpha^i by i mod d; independence over Q(zeta)
then binary coefficient uniqueness again forces whole core orbits and no
extras. A norm bound suffices for modular lifting:
 A=n*2^ceil((m+c+1)/d), p>A^[d(d-1)].
Every complex conjugate has coordinate magnitude <=2^ceil(...), so this
bounds both subset sums and point differences. Ring evaluation into Fp
using supplied alpha,omega shows a nonzero norm divisible by p.
Products are now prod_{i in I}(2^i-1), i>=2; bound
 p>2^[D(2m-D+3)/2], improving the exponent by about d.
The elementary decoder works at BASE TWO when the first index is 2:
normalized product >1/2, so bitlength(T)=sum indices; tail product after i
is >1-2^-i. Greedy membership and unique products follow without Zsigmondy.
All-nearby classification and efficient decoder survive verbatim.
For Mersenne p=2^b-1, d!=b and p≡1modd, alpha=2^(inverse(d) modulo b)
is an explicit dth root of 2, so no extra root search for alpha.
Potential finite improvements: d2,M521,m34,D18,n70,K35 half rate;
d3,M1279,m56,D29,n172,K86; d5,M9689,m158,D80,n798,K399;
d13,M23209,m247,D123,c0,n3224,K1598 (near half rate), likely ratio>1.
M44497 admits d19 (b≡1mod18); optimize m,D near rho=.25, perhaps gives
19/20 separation with unique efficient witnesses. Need check actual ratios!
For arbitrary rho, exact ratio J > 2^q*n*2^[nH(K/n)/(d+1)] iff
 J^(d+1)*K^K*(n-K)^(n-K) > 2^[q(d+1)]*n^(n+d+1).
Do not alter the existing all-p≡1modd asymptotic theorem: this Kummer
variant additionally requires a dth root of 2. Could present as finite
refinement / conditional-root theorem, not overclaim same progression.

## 2026-09-17 10:43 UTC — new results integrated and checked

Paper now146pages, clean build, fullmarginarticle. Newfigureonpage3 and
Kummerproofpage46visuallyinspected. All110mainchecks+12overnightstepsPASSED;
summary research/verification_2026-09-17.json, commitd0bfd041. Newadditions
separatelychecked; Makefile now116commands includingovernight.

NEWMAINMESSAGE: twofarinputsu,v canhaveALLp-2otheraffinemixturesnearby,
eachendpointalmosthalfgapoutside. Corollarypd:two-far-inputs followsby
partitioningrpaddingdirectionsintoequalgroups. Endpointsparameterweight
r/2, otherparametersweightr, soendpointdistanceθ+r/n. Moreoverrinputs
f+e_j eachθ+2(r-1)/n, uniformaffinecombinationsnearwithprobability
((p-1)^r-(-1)^r)/p^r =1-O(r/p), whileeachinputalmostwholegapoutside.
far_inputs.tex+check_far_inputs.py: all37parametersofp37,n36,K15,r2toy
fixtureexactdistances18at0,1and16else;16exhaustiveaffinecoefficientcounts.
ToynotbelowElias; asymptoticcompletionprovidesthat. Figuregenerator
figures/two_far_inputs.py withPDF/PNG. Matplotlibinstalledusinguvandpinned
inuser-localtoolchainrequirements.

RANDOMORBITTHEOREM ou:random nowintegrated: n=alpha log2p+O(1),alpha<1,
allp≡1modfixedprimed, nearfractiond/(d+1)gap, allnearbyunique,
J/prescription=p^Omega(1) forc2<1+1/d. Failureatmostp^(alpha-1+o1).
Noarbitrarywitnessdecoder. Finitehalfrateunionbounds:
M521d3n466K233ratio>2^24failure<2^-57;
M521d5n468K234ratio>2failure<2^-57;
M1279d7n1146K573ratio>2^4failure<2^-139.
verify_random.pyand9exhaustivecheck_random_geometry.pyfixturesPASSED.

KUMMERREFINEMENT ou:kummer nowproved/integrated/certified. Root-of-two
corealpha^iω^j,i2..m+1, alpha^d2. NormboundA=n2^ceil((m+c+1)/d),
p>A^[d(d-1)], productboundp>2^[D(2m-D+3)/2]. ClassifiesALLnearQ;
base2decoderworksstartindex2(normalizedproduct>1/2). Fiveexactrows:
M521d2n80K29,m39D15,ratio>2^3;
M1279d3n198K68,m65D23,ratio>2^4;
M9689d5n905K324,m180D65,ratio>2^14;
M23209d13n3588K1338,m275D103,ratio>2^2;
M44497d19n7068K2830,m371D149,ratio>1, separation19/20eta.
Allc0, ratesvary. IndependentLLroot/domain/entropy/witnessreplay36sec89MiB.
80decodedrandomsupports,10fullwitnesspolynomials. 32766exhaustivebase2
subsetdecodings, 1024/4096/524288rootsubsets,56/1287/12870/2380interpolation
pencilsPASSED. Savedkummer_instances.json~compactrecipesandcoefficients.
No samplingfailureassumptionafterrootscertified. Requiresbothroots; NOT
allp≡1modd. Existingintegerorbitasymptotictheoremunchanged.

Noactive numericaljobs atthischeckpoint. Continueuntil12:30UTC.

PROVISIONALNEXTIDEA — NOTYETPROVED/INTEGRATED:
Two padding orbits can potentially double the exponent-constant range
while retaining near-full separation and unique recoverable witnesses.
Fix prime d, choose q a large power of2 with q-1>3*d^(d-1). For indices
i=L,...,L+m-1 set R_i=(q^(i+1)-1)/(q^i-1)=q+(q-1)/(q^i-1), positive
real a_i=R_i^(1/d), t=q^(1/d), and corea_i*zeta_d^j. Paddingorbitsat
x^d=1 andx^d=q (2dpoints). Extra c<d singletonsatnextindices forrate.
LetM=m+c, chooseq^L>4*(dM)^(d-2). Then eacha_i=t+δ_i with
 t/(3d)*q^-i < δ_i <=t/d*q^-i.
Forselectedrootssum S=Σa_i C_i, C_i=sumselecteddthroots, |C_i|<=d;
nonzeroC_i has|C_i|>=d^-(d-2). IfΣC_i≠0 itsabsolutevalue>=
(dM)^-(d-2), so tΣC dominatesδtail bychoiceL. IfΣC_i=0, firstnonzero
δ_i C_i dominateslaterterms byq-1>3d^(d-1). ThuszerosumforcesALLC_i0,
whichforprimedforceswholecoreorbitsandnoextras. Formaldomainpointsdistinct.
Choose primes splitting the finite Galois field of these radicals plus
zeta_d,t, avoiding finitely many nonzero norms/denominators. Infinitelymany
suchprimes (standard splitting-prime existence; can prove viaSchurprime
divisorsofminimalpolynomialofprimitiveintegralGaloisgenerator+degree-one
primeideal). Choosep arbitrarilylarge toalsoavoidwrap ofallq^s/products.
ThenallnearQ classifiedasDwholeorbits asbefore, w degree dD,K=dD-1.
Now n=d(m+2)+c, farK+1agreements,nearK+1+2d, eta=(2d+1)/n,
separation2d/(2d+1)eta. ForDsupportI:
 H_I(1)/H_I(t)=q^(sumI),
 -H_I(t)=(-1)^(D+1)(q-1)^D / prod(q^i-1).
ChoosefixedsumS maximizing number ofDsupports (atleastbinom(m,D)/
[D(m-D)+1]). Directionq^S onfirstpaddingorbit,1onsecond,0core.
Allnearby iff sumI=S (p>q^maxsum preventsmodularpowercollision).
Labelinverse yieldsintegerproductT<p, greedilydecodablebaseq (i>=1,q>=4).
Hencewhole-linenearlistsunique andefficientlyrecoverable. EntropylogJ=
mHrho+O(logm), n~dm, beatsc2< (2d+1)/d =2+1/d!
Thusforc2=2, arbitrarilynearfullgapseparationbylarged, astrongeruniform
constantobstruction than currentorbitc2<1+1/d. Fields may be extremelylarge;
noallprime/noTheta(logp) claim. Need rigorous reduction/primeexistence,
exact-rate n congruence nowm=(n-c)/d-2, D=(rhon+1)/d, andtoychecks.
Onecanboundthemultiradicalnorms explicitly withfielddegree<=d^(m+c+1)(d-1),
sochoosep enormous; existence alone suffices foruniformboundcounterexample.
For d2, a_i=sqrt(4+3/(4^i-1)) realdescendingperturbations of2 already
force signed dissociation. Moregenerald usescyclotomicnormlowerbounds.
Do not claimthisuntilproofandtestsarefinished.

## 2026-09-17 11:15 UTC — two padding orbits, doubled exponent, audited

The previously provisional two-orbit construction is proved and integrated
in `research/two_orbit_unique/`. It retains unique nearby witnesses and
separation 2d/(2d+1) of the gap while defeating every c2<2+1/d. Thus
c2=2 survives with arbitrarily close to full-gap separation. The integer
form has an efficient witness decoder given roots over sufficiently large
splitting primes. The function-field form gives n=(log_2 p)/8+O(1) for
all large p=1 mod d, but no polylog sampler or arbitrary-witness decoder.
Primary Weil source verified: Sárközy–Sárközy (2005), Lemma 2.

Five finite half-rate existence certificates (not explicit domains) pass
independent Lucas–Lehmer and integer replay, from M521 (ratio>2^7,
separation4/5) to M44497 (ratio>2^5,separation38/39). Norm/power bounds,
formal-series independence, rotation counting, and product injectivity
are audited. Two million-element-field scans classify all parameters;
small-field extras and a genuine forbidden-root negative control pass.
Actual M9689 integer fixtures have all-codeword interpolation audits and
decoder checks. Every numerical job remains sequential under384MiB.
One naive-modulo LL replay hit180seconds; the independently written
folding replay passed all rows in31seconds under19MiB. No claimed
mathematical failure resulted from that resource timeout.

Paper is151pages, article11pt letter with1-inch margins. New result,
finite table, and scope are reflected in abstract/introduction. Build
layout correction removes a long unbreakable tuple list. Still no
better.codes improvement. Continue until12:30UTC (8:30Eastern).
Potential next improvements: variance concentration strengthens the
largest index-sum class; allow code dimension K=dD-h,1<=h<d for a
c2/separation tradeoff up to c2<3; optimize the logarithmic length constant.

## 2026-09-17 11:38 UTC — ongoing refinements, NOT ALL REPLAYED YET

HEAD41ef1944496164a5ba9f7fdb57b318fb9eef3af5 commits the first audited
two-orbit result. Subsequent work is uncommitted. Deadline remains
12:30UTC; do not conclude early.

Active numerical job: exec session42349, `finite.py` under384MiB and1800s
watchdog, started about11:19UTC. First five regenerated rows passed LL;
currently proving M216091 by standard Python LL. New rows use variance
class bound and last-valid-length binary search. Expected rows:
M521d2n346K173ratio>2^9; M1279d3n862K431>2^13;
M9689d5n6638K3319>2^85; M23209d7n16546K8273>2^119;
M44497d19n36060K18030>2^9;
M216091d43n190144K95072>2^6 (last primality pending).
Do not promote the final row until the job and independent replay pass.
`verify_finite.py` now optionally uses gmpy2 standard modular LL as an
independent backend; gmpy2 2.3.1 installed in research venv and toolchain
records updated. Fallback is standard Python folding. Run replay using
venv Python after generation completes; numerical jobs remain sequential.

New proof refinements:
- `function_field.tex`: n=alpha log2p+O(1) for any alpha below
  d/(log2d+max(log2(2^d-1),2Hrho)); conditional failure exponent is
  1-alpha(log2d+max(...))/d. Oldalpha1/8 remains valid.
- `degree_tradeoff.tex`: K=dD-s,1<=s<d gives c2<2+s/d,
  separation2d/(2d+s). Thus any fixedc2<3 with >2/3-gap separation.
  All existing witness polynomials still fit; no new nearby codewords.
- `concentration.tex`: J>=ceil[binom(m,D)/sqrt(D(m-D)(m+1)+1)].
  Proof smooths integer subset-sum distribution by uniform[-1/2,1/2]
  and uses density/variance inequality. Exhaustive2,097,110-support
  check passed (`check_concentration.py`).
- Far batching strengthened for anyfixedt dividingr: input separation
  (2r/(2r+1))(1-1/t)*eta. Unrestrictedlinear nearby probability
  1/p+(1-1/p)*[(1-1/p)^t-(-1)^t/p^t]. Multilinear t=2^ell weights
  give exactnearby probability(1-2/p)^ell. Usesn-K>=4r+1, automatic
  asymptotically. `far_inputs.tex` contains proof.
- `profile_lines.tex`: every prescribed integer allocation of <=r
  vanished coordinates can be realized on a line; total excess distance
  <=2r/n for lines having anynearby point. Only a converse for this
  constructed affine space, not allRS lines.

Checks WRITTEN BUT NOT YET RUN (wait for current LL):
`two_orbit_unique/check_tradeoff.py` (all-codeword smaller-code fixtures),
`paired_domain_warp/check_far_mixtures.py` (linear/tensor counts andall
plane lines), `two_orbit_unique/short_finite.py` (searchProthprime and
exactGaussian-binomial class for n226K113,c2=2), and `verify_short.py`
(independent subsetDP+Proth+exactbounds). The short row is speculative
until execution. It gives an explicitfield, but still only existence
of a successfulq/domain, not actualdomain coordinates.

`check_exhaustive.py` gained optionaldimension reductions andnegative
controls; its previouss1 path must be replayed after these changes.
Makefile nowincludesnewchecks butshortpairnotyetadded. README updated
withtheory. Abstract shortenedfrom625to300words; fullproofsretained.
LatestPDF153pages, cleanpdfLaTeXbuild, visualpage1and54inspectionPASS.
Newfinite table/intro stillcontainoldvalidnumbers; updateonce newrowspass.
No better.codes improvement. No publication or push.

## 2026-09-17 12:00 UTC — new proofs and certificates passed; frontier running

All nine strengthening checks in
`research/new_strengthening_verification_2026-09-17.json` passed,
including independent GMP ordinary-modulo Lucas–Lehmer on all six
Mersenne rows (324s). Their combined watchdog peak was45MiB. The
standard-Python M216091 generation was deliberately stopped after1391s
for speed, then GMP folding generated all rows in74s; the independent
ordinary-modulo replay passed. No primality claim relies on that stopped
run. Both new far-mixture and curve-profile checks pass (2290 cyclic
allocation fixtures plus all small-field interpolation cases).

New explicit-field finite existence certificates:
- n226,K113 (half rate), p=204255*2^320+1,338bits, Prothbase11;
  m111,D57,S3192,J441734689284929317660654122848.
  Ratio>119/100 for c2=2 and>2^45 for c2=1.
- n220,K95 (rho19/44), p=121*2^320+1,327bits, Prothbase3;
  m108,D48,S2616,J31495815243247545087807036124.
  Ratio>21/20 for c2=2 and>2^43 for c2=1.
Both use exact Gaussian-binomial counts, independently replayed by subset
DP, exact entropy comparisons, and deterministic Proth primality proofs.
They specify fields and support classes, but NO successfulq/domain.
The shorter-rate search tested5544parameterpairs; no general minimality
claim. Paper includes both rows.

A new remark proves the integer construction's dimension cutoff: reducing
K further to dD-d leaves at most one nearby parameter at the same agreement
threshold. DistinctDsupport sums ofRi are forced by dominant geometric
tails and survive the existingp>B no-wrap bound. 5916rational support
checks and an actualM9689fixture pass. NewMakefiletargets added.

ACTIVE: exec session20730, `proth_frontier.py`,900s/384MiB watchdog.
It searches compact Proth prime fields for d3,5,7,11,19, using the variance
class bound and target ratio>2 againstc2=2. First three generated rows:
d3 n568 K284 p=65703*2^830+1(base5),847bits;
d5 n1678 K839 p=66495*2^2451+1(base7),2468bits;
d7 n3442 K1721 p=110915*2^4847+1(base3),4864bits.
All have conditional bad-parameter bound<2^-4 and original c2=1 ratios
>2^82,>2^153,>2^230, respectively. d11and19stillpending. These rows
must be independently replayed before manuscript integration. Checkpoint
`proth_frontier_certificates.json` is currently partial. All other new
research is verified and can be committed separately from frontier files.

Latest build before final short-row/degree-cutoff edits was153pages, clean;
rebuild and inspect new finite pages before committing. Continue until
at least12:30UTC (8:30Eastern). No better.codes improvement; no push.

## 2026-09-17 morning steering: work until 6 p.m. Eastern

User explicitly extended the research horizon to **2026-09-17 18:00 America/New_York = 22:00 UTC**. This supersedes the previous 08:30 Eastern stopping time. Do not mark the active goal complete at 12:30 UTC. User asks whether results can show the prime-field proximity-gap paper with Scott and Quang is tight-ish. Prioritize precise fixed-gap comparisons and lower bounds in block length.

Recovered reference: rs_capacity_tr26164/starkware/CONTEXT_STARKWARE_2026-09-05.md section F identifies Dao–Kominers–Thaler–Zheng, Reed–Solomon List Decoding and Mutual Correlated Agreement up to Capacity, September 2026. Abstract gives n^{O_eta(1)} lists and derivative order ceil(exp(6.76/eta)). Need actual complete theorem statements before claiming matching exponents. Current fixed-gap anchored padding gives C_rho(eta)n exceptions with log C = Omega(eta^-2/log(1/eta)); does NOT force superlinear n dependence. Current isolated-solution appendix matches algebraic D^{d+1} growth before agreement filtering, but proves its own examples have only constant nearby count at fixed gap. Thus neither currently establishes tightness of the MCA exponent. Shrinking-gap constructions must remain clearly distinguished.

## 2026-09-17 12:23 UTC — tightness work, clean manuscript, verified frontier

Morning strengthening commit: dc68a1655549683d47b5d1b769a87e0792eaeb6b
(51 files, all previously checked new theory/certificates, 154-page PDF).

The Proth frontier search reached its900s watchdog limit before finding
d19. Its four checkpointed d3,5,7,11 rows independently PASSED standard
Python Proth/existence/ratio replay in4.5s,18MiB. d11 row is n9018,K4509,
p=191499*2^11953+1,base13,11971bits; ratio>2 against c2=2 and>2^393
against c2=1, separation22/23. Search status remainspartial deliberately;
no d19 Proth claim. README documents all four rows and failed search scope.

New priority folder research/prime_field_tightness/ records exact user
question and recovered upper-bound excerpts. The target is unbounded
fixed-gap exponent over superpolynomial prime fields, not shrinking-gap
finite violations. Existing full-length Dickson lists DO grow at fixedgap
(n/2 elements at n=p-1,rho1/4,eta1/8), but cannot yield superlinear scalar
challenge counts because p=n+1. Enlarging to extension fields does not
satisfy the prime-field target. Be precise about this qualifier.

A new elementary rational-normalization theorem is proved, manually
reviewed and checked: for candidates(P-S)/R=a/b with degrees<=r, R having
h domain zeros, A-h>=beta*n, n>=48r/beta^3, full-support bad labels
<=16(n-A+1)/beta^3 in every characteristic. It uses the sharp n-A+1
bad-label bound on a polynomial pencil and third agreement incidence.
220 rational determinant checks and an exact13-bad-label pencil PASS.
It is included after isolated-solution sharpness. Clean PDF build155pages,
new propositionI.4 page142 visually inspected. Main introduction has just
received a short reference to it; rebuild after that edit is still needed.

A broader projective-normalization proof is in PROJECTIVE_ENVELOPE.md:
any rational projective pencil has<=D+2 polynomial members of degree<=D,
or lies on a scalar-reparameterized polynomial line. This yields a linear
full-MCA bound for projectively normalized degree-r families via fourth
incidence. All degeneracies including infinity are handled;1489 polynomial
pencil fixtures,13 sharp examples,5392 projective quadruples PASS.
This broader theorem is locally reviewed but not yet in the manuscript;
no independent human/agent review. A constant ordinary-list bound for the
restricted family is also proved by pair incidence. These are scoped upper
bounds, NOT intrinsic tightness or a general prime-field exponent-one result.

User asked for work until18:00 Eastern=22:00UTC. Do not stop at the OLD
08:30deadline. Optional async question asks for latest coauthor-paper path;
no answer yet. No numerical job currently active. No publication/push.

## 2026-09-17 12:43 UTC — rational witness coherence quantified

Previous goal turn was progress: authoritative commit c900f9ded3f314dd37f4b3a0d5a268a7050cd0f6
saved the155-page manuscript, finite frontier checks, and tightness notes.
This continuation makes further proved/tested progress; no wait/blocker.

New strongest structural theorem: a candidate rational function T(X,Z)
with numerator/denominator challenge degree<=h has at most(8h+10)n/(A-D)
nearby polynomial specializations of degree<=D, unless T is affine in Z
with polynomial coefficients. The affine exception permits at mostn-A+1
full-support bad labels. NO coefficient-X-height or characteristic guard.
Persistent coordinate identities exclude at mosth labels each; other
coordinates support at mosth+1 labels. Triple incidence and the h+1
intersection bound with a graph line prove the constant fixed-gap count.
Full proof at research/prime_field_tightness/RATIONAL_PATH_RIGIDITY.md.

It gives h>=(A-D)L/(8n)-5/4 for any rational witness selection onL>n-A+1
bad labels. Hence the full-coverage examples need Omega(p/log p) challenge
degree for any single rational witness formula. This is an algebraic degree
bound, NOT an algorithmic lower bound or a fixed-gap exponent converse.
The auxiliary rational-parameter height reconstruction proof is retained
in notes but is superseded by this stronger, simpler incidence theorem.

New exact construction gives a non-affine projective path with order1/eta
nearby bad labels, showing inverse-gap dependence is necessary. At exact
rho1/4,eta1/8 the checker passesn160,320,640 overF1009: path-bank sizes
41,81,161, exactly10 nearby labels each, all full-support bad by independent
interpolation. Counts outside this path in the full RS code are NOT claimed.
Verification took2.3s/19MiB under the384MiB watchdog.

TheoremI.5 and CorollaryI.6 integrated after the rational-envelope result.
LatestPDF156pages, clean final TeX log (no warnings/overfull/underfull),
page143 visually inspected. New theorem proof/math locally audited;
no independent person/agent review. No active numerical/build job now.
Work must continue until18:00 Eastern=22:00UTC under the user's extension.

## 2026-09-17 13:05 UTC — fixed-gap tightness bridge made precise

Previous turn was progress: STATUS.md recorded the general cyclic-boundary
audit and clarified the unresolved large-prime source-list target. This
turn adds a proved and checked transfer, not a new growing list.

Proposition4.9: any L source candidates at length N, dimension k,
agreement A>=k+1, over prime p>=2N+1 produce a length2N, dimension k
line with at least ceil(p*A*L/(p+3*A*L)) full-support MCA-bad labels.
Rate and gap are EXACTLY halved. The bound is Omega(min(NL,p)) at
fixed source parameters. The proof anchors, divides once, and uses
averaged additive padding; allowing the target dimension k gives exact
parameter scaling. This is an application of existing mechanisms, not
a novelty claim. Ordinary CA may coexist and a far point is not asserted.

Consequences: source lists N^c would force exponent c+1 before field
saturation; universal linear full-support bounds would force constant
fixed-gap list sizes whenever p/N tends to infinity. The construction
does not supply such growing lists. The Dickson p=Theta(N) family
cannot give superlinear prime-field scalar counts.

Files: research/prime_field_tightness/PRIME_BOUNDARY_AMPLIFICATION.md,
list_amplification.tex, check_prime_boundary_amplification.py and JSON
reports. Checker passes exhaustive nearest-list and arbitrary-list
fixtures, all translations in small cases, all relevant direction
interpolants, and exact scaling N5->10 overF101 and N10->20 overF23.
The F23 fixture has11 source candidates and23 exhibited bad labels.
Runtime1.15s, peak26MiB, bounded by384MiB.

General-order cyclic boundary note and checker from the preceding work
are also retained, with6 complete subset-class tests and44850 exponent
inequalities. These restrict boundary-degree words on cyclic domains,
not arbitrary words. Both new checkers are in Makefile.

paper.pdf now157pages; article11pt, letter, margin1in. Final TeX log
clean. New proposition pages33–34 visually inspected. Intro explains
fixed-gap exponent tightness and its missing source-list ingredient.
No build/numerical job remains active. Continue research until22:00UTC.

## 2026-09-17 13:23 UTC — non-subgroup candidate search checked

Previous turn was progress, committed5655da0f609b261ddfec06e3bcf13fab572cab7e:
the exact-scaling same-prime amplification proposition,157-page manuscript,
and cyclic-boundary research notes. The current turn pursued actual source
lists by testing a previously unscanned family of candidate subsets.

research/two_coset_candidate_lists/ searches two adjacent cosets of H
inside mu_k, with |H|=k/4. Their union is not a subgroup. An exact DP
chooses n/|H| coordinate cosets and received symbols to maximize minimum
agreement across the two candidate groups. The optimum is only in this
invariant domain/word class. Census:120 cases at k32,64,128; r2..48 with
p=2rk+1 prime; j0,1,floor(r/2),r-1; n4k.

Only four cases have A>k. The sole below-Elias case is p257,k64,n256,
L32,A100, gap9/64. It improves agreement for those32 candidates from96
to100, but the standard96-agreement family has a larger list. It remains
full-length and gives no short-domain asymptotic or better.codes claim.
No extra finite example was added to the manuscript.

All120 certificates independently replayed. Four small optimizations
exhausted290560 domain/word choices total, with the same optima. A genuine
subgroup control reproduces29agreements. Scan14.6s/<38MiB; validation
6.8s/<22MiB. Reports and reconstructible coset/symbol data saved.

BRANCH_ANALYSIS_AGENDA.md records a prospective multiquadratic branch
explanation of why r2,j1 is exceptional. It is explicitly UNPROVED:
norm-product/base-point bookkeeping and character-sum constants remain
to audit. Do not state the proposed fixed-r or arbitrary-subset upper
bounds as established. This may guide the next investigation, but the
main target is still a growing fixed-gap source list or actual stronger
counterexample, not simply more restricted upper bounds.

Scott's public research page was checked and gives the working title
Reed-Solomon Codes Beyond Johnson: Efficient Decoding and Smaller
Cryptographic Proofs, with Q.Dao and J.Thaler, but no linked draft.
STATUS.md records the source and version caution. Exact latest coauthor
theorems remain unavailable beyond restored excerpts. No live jobs.
Work horizon remains18:00 Eastern=22:00UTC, NOT the original08:30 deadline.

## 2026-09-17 13:35 UTC — binomial branch agenda resolved locally

Previous turn was progress, commita28d1e608f630e37c4dd87aa5a60eb1c8ceb49f6
saved the120-case two-coset search and its independent replay. This turn
proves a restricted upper bound suggested by those failures, rather than
finding the desired new lower-bound family.

research/two_coset_candidate_lists/BINOMIAL_BRANCH_BOUND.md now proves:
for p=2rk+1, r>=3, any subset of the candidatesG(hX)-X^k, h in mu_k,
on any n<=c*k coordinates and any word, cannot all have k+1 agreements
unless L<=2^20*r^3*4^r+24*c*(r*2^r+1). This includes arbitrary non-
subgroup candidate subsets, non-invariant domains and words, and zero.
It is NOT a general RS list bound. r2,j1 is the Dickson exception.

Proof: a root filter gives multiquadratic radical branches. Constant
branches occur only in the rth-power class, and additionally in its
order2 class for j1. All other per-value fibers are bounded by a
Galois-invariant nonconstant-branch norm, of degree<=r*2^r; use safe
B=r*2^r+1, not the earlier proposed factor-r improvement. Character-
pattern estimates and nontrivial Fourier coefficients are bounded by
Lambda=2^(r+1)(sqrt(p)+3). Parseval controls arbitrary candidate subsets.
The leading agreement coefficient is<=7/8 for allr>=3, including a
separate r4,j1 sign-count refinement. Explicit constants absorb small k.

Locally audited pitfalls: dependent but distinct square classes still
give independent character spaces; exclude identically constant factors
from norm products; their multiset remains Galois invariant; clear j0
denominators; base points add at most1; lifted nontrivial H characters
are neither principal nor quadratic, preventing a trivial expanded sum.
Weil input checked at https://web.cs.wpi.edu/~gsarkozy/Cikkek/23.pdf,
Lemma2. No independent human/agent review or novelty claim.

check_branches.py passes26 exact fixtures including every section for
r3,4,6 overF12289; checks coefficients, root filter at every nonzero
t, r-to-one masks and residual fibers. Max observed residual fiber4.
Uses NumPy integer arrays; FFT values are diagnostic only. Runtime1.1s,
peak37MiB. check_branch_classification.py passes26104 exact sign-pattern
coefficient checks forr2..8, stdlib,0.55s/<7MiB. Reports saved. The latter
is in make verify; NumPy fixtures have a separate optional target.

The exponential-in-r bound leaves r>=Omega(log L) open, so it does not
resolve the large-prime fixed-gap lower-bound target. Do not spend the
remaining horizon only expanding restricted upper-bound appendices.
No new paper appendix: manuscript remains157pages at the previously
verified build. No live jobs. Continue substantive research to22:00UTC.

## 2026-09-17 13:45 UTC — ordinary-CA amplification strengthened

Previous turn was progress: commit20004eb071973b45272ec5bb986ab1682c09b7cd
saved the restricted binomial-branch bound and its checks. Current turn
proves/checks a stronger transfer for NEAREST source lists, kept in notes.

UNIQUE_BOUNDARY_AMPLIFICATION.md: source maximum agreement M>=k+1,
complete nearest list L, pool U at threshold k+1<=T<=M, padding q.
If p>=N+q+(k-1)binom(U,2) and
(qU+binom(q,2)U^2)/p+binom(N+q,M+1)/p^(M+1-T)<1,
there is a same-prime line with EXACTLY qL nearby labels, all uniquely
decodable at agreement M+1. Every other label, including0, has maximum
agreement M. Thus no ordinary CA at the threshold. Far/near separation
is only one coordinate; no global list-size bound follows.

Proof separates every pool evaluation, chooses offsets with all pool
labels distinct/nonzero, and excludes all outside-pool candidates at
all labels via a support union bound. Unlike the older unique-padding
lemma, no condition q<A-k and no degree bound on the received word is
needed. With q=N rate halves exactly, but gap is eta/2+1/(2N); do not
erase this quantifier distinction. Polynomial U from a cited capacity
list theorem suffices over superpolynomial primes; that is an explicit
dependency. p>=8N^2*4^N is an unconditional sufficient cutoff via the
trivial interpolation pool bound. Missing ingredient: growing fixed-gap
nearest lists in sufficiently large prime fields, still not found.

check_unique_boundary_amplification.py independently exhausts all labels
and all determining pairs overF263 andF2003. Exact near counts10 and21;
all other253 and1982 labels have agreement3, nearby agreement4. The
second source has polynomial interpolation degree6, exceeding maximum
agreement3. An additional exhaustive343-offset F7 fixture gives96 good
profiles and42 outside-pool failure cases. All pass in0.56s/<15MiB.
Checker added to make verify; no manuscript expansion (still157pages).

Next proposed bounded pilot is DEFORMABLE_DICKSON_PILOT_PLAN.md. It
allows ALL nodes, received symbols and candidate coefficients to deform,
unlike the existing fixed-cyclotomic-domain tests. Only p17 and p41
initially: compute first p^2-lift systems, save a correction or exact
left-kernel obstruction, and independently replay. This has NOT run yet.
The archive's analogous ternary bank pilot already has a positive finite
case and later unramified obstruction; do not redo that census or infer
it settles the different Dickson system. No live numerical/build jobs.
Continue to18:00 Eastern=22:00UTC.

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
