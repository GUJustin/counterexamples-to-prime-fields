# Recovered Riccati results: current integration evidence

Reviewed September 18, 2026, without manuscript edits or rerunning historical enumerations. **The recovered main Riccati results are integrated.** No missing input or missing proof of the advertised recovered claims was found. This is a current-source and evidence audit, not formal verification or a fresh PDF/build certification.

## Authoritative manuscript and proofs

- `paper.tex` inputs `research/riccati_cross_ratio/appendix.tex` and `research/fixed_singular_cover/appendix.tex`. Its introduction describes both with the appropriate fixed-equation versus bounded-challenge scope.
- The authoritative strengthened fixed-equation proof is `CHARACTERISTIC_REFINEMENT.md`, reproduced in `appendix.tex`: characteristic zero or `p>D`; ordinary lists at most `floor(n/(A-D))`; nonlinear total solution count `D+2` above the boundary and `2D+2` at `p=D+1`; fixed-equation bad-full-support labels at most `2n(n+C_D)/(A-D)`.
- `PROOF.md` is explicitly superseded in characteristic scope. Its sentence saying “not yet integrated” is historical and contradicted by the actual current inputs; it is not unfinished integration work.
- The current appendix correctly uses multiplicities rather than falsely asserting constant cross ratios under `p>D`. Its candidate-count reconstruction, two-value-class argument, and heavy/light full-support count agree with the strengthened proof. The prime-field equality family and boundary counterexamples are included.

## Independent and computational evidence actually present

- `verification.json`: PASS; 183,581 candidate polynomials, 616 received lines, nine sharp-list fixtures, and the characteristic-three negative control. `verify.py` is the corresponding exact checker.
- `multiplicity_verification.json`: PASS; 1,084,807 polynomials in 549 equations, 2,790 coordinate-family checks, five nonconstant cross ratios, and the sharp characteristic-two count. Corresponding checker: `verify_multiplicities.py`.
- `boundary_extension_verification.json`: PASS; a separate F9 implementation exhausts 729 degree-at-most-two polynomials and 85 received lines, including boundary-characteristic full-support checks. Corresponding checker: `verify_boundary_extension.py`.
- These finite checks supplement the general mathematical arguments; they do not prove the general statements by enumeration.
- `manuscript_review.json` records a successful historical build and visual review of pages 104–107 of a 109-page version. It is not a current whole-paper visual review.
- I compared `replay_hashes.json` with current files. The original proof, refined theorem, characteristic refinement, and all three listed checker implementations still match. The README and current appendix no longer match the archived hashes. Therefore the old hash receipt must not be advertised as a byte-identical certification of the current appendix. This is a provenance qualification, not an identified mathematical defect.

## Singular-cover extension and its dependencies

`research/fixed_singular_cover/ROOT_AUDIT.md` supplies an explicit independent mathematical review of the fixed-cover argument, all-singular lower example, high-degree recurrence/resonance cases, and the moving-derivative-coefficient extension. The current appendix contains these arguments, including the exceptional-root exclusions and the nonzero quartic coefficient in the resonant elimination.

The dependencies are present and integrated: `thm:nonsingular-agreement-mca` is in `research/quasilinear_first_order/appendix.tex`, and `thm:triangular-newton` is in `research/two_branch_recurrence/appendix.tex`; both are inputs of `paper.tex` before the singular-cover appendix.

The receipts `checks.json`, `resonance_checks.json`, and `moving_resonance_checks.json` all report passing exact checks. They cover the small entirely-singular instance and six fixed/moving resonance fixtures; they should not be described as exhaustive verification of the general theorem.

The current appendix additionally states a polynomial-gauge corollary with its own proof and explicit divisibility/characteristic guards. The located ROOT_AUDIT does not separately identify an independent review of that later corollary. If a completion checklist demands a separate independent receipt for every subsidiary corollary, that particular receipt remains unlocated; it is not missing from the manuscript and is not needed for the headline monic theorem.

## Scope and remaining work

The fixed-equation full-support theorem does not follow for arbitrary challenge-dependent equations merely from the per-label list bound. The singular-cover theorem instead treats actual solutions of a specified identity, with a uniform hypothesis on singular agreements. The monic Riccati extension allows bounded challenge degree and unrestricted X-degrees but requires a constant nonzero quadratic value coefficient and agreement above `5D/3` with linear slack. It does not prove that every nearby codeword of an arbitrary received line belongs to such an identity. These limitations are stated in both the introduction and appendix.

`TWO_BRANCH_FRONTIER.md` contains older exploratory scope statements and a proved zero-branch/high-agreement obstruction. Its broad “unnormalized route remains open” language predates the integrated bounded-challenge monic theorem and should not override the latter within that theorem's hypotheses. There is no requirement to promote all exploratory statements into the paper. The general implicit first-order and fixed-rate positive-construction targets remain outside these recovered results.

**Completion conclusion:** the main recovered Riccati list/count/full-support results, their equality examples, and the singular-cover/monic extension are integrated with proofs and recorded checks. The only evidence qualifications found are stale integration wording, historical PDF/hash receipts that do not certify the current paper verbatim, and the absence of a separately located independent receipt for the polynomial-gauge corollary. No new numerical run or manuscript edit was needed for this audit.

## Evidence closure, September 18 follow-up

The subsidiary polynomial-gauge corollary has now passed a separate independent proof audit: `../fixed_singular_cover/POLYNOMIAL_GAUGE_INDEPENDENT_AUDIT.md`. The outdated integration-status sentence in `PROOF.md` has been replaced by a dated status update while preserving the original narrower proof. The new `current_integration_hashes_2026_09_18.json` records current relevant source/checker hashes separately; it does not overwrite the historical replay receipt or imply a fresh execution of those checkers. These actions close the concrete evidence gaps identified above. A current whole-paper build/visual review remains a separate manuscript-wide activity.
