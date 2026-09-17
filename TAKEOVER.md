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
