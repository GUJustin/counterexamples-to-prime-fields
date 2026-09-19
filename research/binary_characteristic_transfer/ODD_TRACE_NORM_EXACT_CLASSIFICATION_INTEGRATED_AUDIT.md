# Integrated exact trace–norm classification audit

Status: PASS. Independent actual-text second pass, 2026-09-19. No manuscript edits made.

The frozen theorem `thm:odd-trace-norm-refinement` states and proves exactly n(Q−1) interior affine exceptions, maximum agreement exactly T and a singleton threshold list at every exception, and agreement at most T−1 elsewhere. These conclusions hold for codewords over the stated challenge extension E, not only native coefficient polynomials.

## Proof checks

- For every residual W=X^D+C with deg C≤k, the nonzero polynomial Δ=W^p−Λ^(p−1) has degree at most (p−1)T. Factoring out the native root locator to multiplicity p−1 proves A_W≤T.
- Equality makes the remaining factor a nonzero constant. Evaluation at a native root gives c=−α^(p−1) with α∈B*. The resulting identity L^p+cL=ΛH^p descends H, hence W, to B. This step does not assume native coefficients initially.
- The cyclic base-p exponent argument at degree cap p^(2s−1)+p^(s−1) permits exactly the single-one and antipodal-two-one orbits. Coefficient Frobenius relations give the claimed trace–norm plus linear-trace space. Exact degree and squarefreeness exclude the missing leading norm term and zero completed level.
- Differentiation and normalization recover F₀=H/(αc₁) and W=F₀Λ/G₀ with no scalar ambiguity. Thus equality recovers precisely the normalized bank. Pole injectivity then proves uniqueness of the strict-degree witness.
- The Ω argument retains the independent endpoint bound U. The affine chart t=1−c*/λ loses no bank label: every bank label is nonzero, c* is excluded by U<T, and the omitted chart point has reciprocal agreement k<T. Common agreement remains exactly k by invertible source transformation.
- The Johnson and full first-order comparisons and the finite n=81, k=34, T=51, U=45, M=648 ledger agree with the established exact formulas. The text explicitly distinguishes the algebraic exhaustive-list proof from the finite canonical-witness check.

## Finite corroboration and scope

The independent finite classification receipt reports the expected exponent orbit dimensions 7, 10, 7 for (p,s)=(3,2),(3,3),(5,2). For (3,2), it enumerates the entire 2187-element trace coefficient space, finds 1296 full-degree squarefree polynomials and 648 normalized locators/residuals (each occurring twice before scalar normalization), and recovers the existing bank exactly. This is corroboration of the equality classification, not an enumeration of all challenge-field words or codewords. Its status and hashes were inspected in this pass; parent and producer independently replayed it.

The manuscript correctly attributes the inherited fixed-characteristic asymptotic regime, and identifies the finite degree improvement, every-pole injectivity, and complete-list classification as refinements. No prime-alphabet, prescribed short-domain, or large-characteristic DKT claim is made.

## Frozen SHA256 hashes

- `odd_trace_norm_refinement.tex`: `1de24dfcd521710a729457db5a3eb09d6fc8afa4939916276d2aa98a01fca532`
- `ODD_TRACE_NORM_EXACT_THRESHOLD_CLASSIFICATION.md`: `0fa4c213c0a232a535da5383bd479821862ae5020975f6624c8755bf1a903444`
- `norm_trace_p3_s2_fixture/threshold_classification/verify.py`: `e479d9e5dc4369ba408773600c21bd01b3d1c844f79fe7b6789ac4d764fe5e74`
- `norm_trace_p3_s2_fixture/threshold_classification/receipt.json`: `866f7bd7ef7e4e76b76c2d570b69b99c43e7907cb5df693fa0f0ed6c00e77621`
