# Riccati cross-ratio bounds

Local research result recovered and checked September 16, 2026.
See CHARACTERISTIC_REFINEMENT.md and appendix.tex for the strengthened
p>D hypotheses and complete arguments; PROOF.md retains the original
narrower proof and the
sharp prime-field ordinary-list family. This is a restricted upper-bound
result, not a disproof of the general first-order proximity conjecture.

Run `python3 verify.py` from this directory (standard library only).
The checker imports polynomial helpers from ../quasilinear_first_order/verify.py.
It verifies the sharpened list and fixed-equation incidence inequalities,
183,581 candidate polynomials, 616 received lines, and nine sharp-list
fixtures. The p=3 negative control demonstrates why p>D alone does not
make cross ratios constant; the multiplicity proof handles this case.
See verification.json and check_resources.json for the completed replay.
Numerical jobs should run sequentially under the 384 MiB watchdog.

The ordinary-list bound now holds in characteristic zero or p>D.
For nonlinear equations the candidate count is D+2 when p>D+1 and
2D+2 when p=D+1, giving the fixed-equation bad-label bound
2n(n+C_D)/(A-D). Run `python3 verify_multiplicities.py` for boundary
checks, including nonconstant Frobenius cross ratios.
