# Exact radial certificate: publication bundle

**Result:** some joint class of the first two binomial moment sums among 34-subsets of `{0,...,63}` has at least **5,133,798,314,667** members.

This exceeds the earlier conditional certificate 5,074,503,250,115 by 59,295,064,552 (about 1.17%). Concurrent work has since reported stronger conditional certificates. This bundle preserves an independent unconditional method and makes no claim to the overall best bound or to optimality.

## Verify

From this directory run:

```sh
python3 verify_publication.py
```

Only Python's standard library is required. The entrypoint recomputes the degree50 symmetric-pair DP, checks all 676 saved mixed moments and 26 radial moments, checks the exact rational-to-integer polynomial conversion, enumerates the compact lattice support, and independently recomputes its denominator using full signed coordinates and expanded monomial sums. It reads the artifacts without modifying them and emits a deterministic JSON report. No floating-point optimization, external services, or random sampling is used.

## Files

- `moments.py`: exact subset-moment dynamic program and exhaustive small-fixture checks.
- `moments_degree50.json`: exact mixed and radial moment sums; no timing metadata.
- `certificate_degree12.json`: one selected rational weight, its integer form, support bound, exact numerator and denominator, and resulting ceiling; no timing metadata.
- `verify.py`: exact rational-weight certificate calculation using quadrant symmetry.
- `crosscheck_saved_certificate.py`: independent signed-lattice, expanded-moment denominator check.
- `verify_publication.py`: deterministic end-to-end entrypoint.
- `radial_certificate_fragment.tex`: concise proposition and proof for integration.
- `certificate_factored.json` and `verify_factored.py`: a compact, explicit integer factorization with the **same certified ceiling**, independently expanded and checked.
- `radial_factored_presentation.tex`: optional short root-table presentation for the paper; does not replace the original proposition fragment.

The weight is `w(Q)=(A-Q)h(Q/A)^2`, with `deg h=12`, `A=851547/580691`, and `Q=(341x²+5y²)/1884025`. Its degree is 25 and its positive region contains 210,135 integer points. Full coefficients are in the selected JSON instead of the paper text.

The surrounding experiment searched only a limited family of radial weights. The bound for this specific rational weight is exact; the discovery search is not a proof of optimality.

The factored alternative uses the integers in `verify_factored.py` directly; no root-finding is required to verify it. The end-to-end entrypoint verifies both versions and emits `factored_alternative_verified: true`.
