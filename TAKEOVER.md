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
