# Independent numerical audit of the publication radial certificate

Date: 2026-09-15. Source bundle:
`/Users/jthaler/Documents/frontier_attacks_2026-09-15/stwo_port_review/radial_moment_experiment/publication/`.

## Result

**Passed.** Independently ran the complete standard-library publication verifier:

```text
python3 verify_publication.py
```

It exited with code zero and reported:

```json
{
  "certified_class_lower_bound": 5133798314667,
  "exact_denominator_crosscheck": true,
  "full_signed_lattice_points": 210135,
  "lattice_moment_degree": 25,
  "n": 64,
  "rational_to_integer_coefficient_crosscheck": true,
  "recomputed_mixed_moments": 676,
  "recomputed_radial_moments": 26,
  "small_exhaustive_moment_checks": 400,
  "t": 34,
  "verified": true
}
```

The process used approximately 30 MiB resident memory when sampled. The entrypoint reads its saved proof data without rewriting them. This is a complete rerun of the exact moment dynamic program and the signed-lattice denominator calculation, not just verification of a saved status field.

## Exactness and support checks

I inspected `moments.py`, `verify.py`, `crosscheck_saved_certificate.py`, and `verify_publication.py` before running the entrypoint.

1. **Integral signature lattice.** For a 30-subset, the displayed coordinates simplify to
   `x=sum a−945` and `y=sum binom(a,2)−31 sum a+9765`. They are integers and form a unit lower-triangular affine transformation of the two original integer moments. Thus their joint classes coincide. The denominator may safely sum over all of `Z^2`, whether or not every lattice point is attainable. The full-population sums of both coordinates vanish, so complementing a 30-subset to a 34-subset negates both coordinates and preserves every radial moment and class size.

2. **Exact DP.** The symmetric-pair recurrence accounts for taking zero, one, or both elements of each population pair `(u,v),(-u,v)`. Keeping only even powers of the first coordinate is justified by reflection symmetry. The independent small-fixture enumeration checks 400 mixed-moment identities. The main run recomputes all 676 mixed moments through total degree 50, and derives all 26 radial moments through degree 25 with exact divisibility checks by `4^j`.

3. **Exact integer weight.** Clearing the rational coefficient denominators yields
   `W(T)=(851547*1884025−580691*T) H(T)^2`, where `H` is an explicitly saved degree-12 integer polynomial. This is a positive constant multiple of the rational radial weight. The verifier reconstructs and compares every integer coefficient; a separate routine checks the rational-to-integer scaling. No numerical eigenvalue, optimization, floating-point positivity, or approximate root computation is used.

4. **Compact positive support.** Because the square is nonnegative, `W(T)` is nonpositive outside `T<851547*1884025/580691`. The maximum eligible integer is exactly `2762804`; both adjacent endpoint inequalities were checked with integers. The quadratic form is `T=341*x^2+5*y^2`, so integer square roots give a complete finite enumeration. The 210,135 points count the eligible ellipse, including any point at which `H` might vanish; counting such a zero does not change the denominator.

5. **Independent denominator.** The primary certificate calculation uses quadrant symmetry and direct evaluation of the squared polynomial. The crosscheck visits every signed lattice point and sums expanded monomial moments through degree 25. Their integer denominators agree exactly. The numerator is evaluated from the freshly recomputed radial moment sums, and all saved coefficients, moments, numerator, and denominator match.

6. **Integer rounding.** The numerator has 433 decimal digits and the positive denominator 420. Exact division gives floor `5133798314666` with nonzero remainder. Thus the required ceiling is exactly **5,133,798,314,667**. The integer numerator is positive. The weighting inequality bounds the largest class by this ceiling because negative weights outside the ellipse only decrease the numerator.

## Interpretation relative to the current draft

This proves a joint two-moment class lower bound for 34-subsets and therefore the stated length-64, dimension-32 interval Reed–Solomon list lower bound at radius `30/64`, over every prime `p>64`.

It is a valid unconditional radial alternative. It is **smaller** than the current conditional degree-24 certificate `5,141,180,908,468`; it should not replace that result as the best finite lower bound. The publication fragment's comparison against the older degree-20 certificate is arithmetically consistent but should be contextualized if included alongside the degree-24 result. No optimality, efficient list enumeration, or protocol security consequence is established by this verification.

## Audited source hashes (SHA-256)

| File | SHA-256 |
|---|---|
| `certificate_degree12.json` | `4fafcadb84e2c25e8070398bf5df436da21dea4ecfdfccc34aae4d91ae727b3f` |
| `moments_degree50.json` | `3b625dd854e129e2b608cdda7eb380ec7481a137f8c3333e188e984bc8bb31d4` |
| `moments.py` | `de3c4f9007a0db1e5169d85fc8375197f0bd6dad730d73414f67688a09a72718` |
| `verify.py` | `0af785228fbfeaaba6cb60dcb28e79c957eadcd706b85e18d39b7841c03fe42d` |
| `crosscheck_saved_certificate.py` | `c19421536212409de1dd21ba111eec37bbd6a5e6a68d8206b44b9a664ed2db15` |
| `verify_publication.py` | `3ba818ecd46dfc5ed47f9db857f65bfbacfdc1fc61d3998c3203e9a3bb5b0ab1` |
| `radial_certificate_fragment.tex` | `dbb73b392dba4cb21072aa3933226d6db0a51d66eaeafe92e201494cfd849c13` |

The theorem itself is being reviewed separately; this note records the independent exact computation and the assumptions its integer calculation uses.

## Concurrent update: compact factored alternative

The final hash comparison detected a concurrent frontier update after the full run above. The original certificate, moment data, `moments.py`, `verify.py`, and `crosscheck_saved_certificate.py` remained unchanged. The frontier added `certificate_factored.json` and `verify_factored.py`, and extended `verify_publication.py` to verify that additional certificate.

I inspected this additive change and ran the new component independently:

```text
python3 verify_factored.py
{"certified_class_lower_bound": 5133798314667, "factored_certificate_verified": true}
```

It exited with code zero. Its polynomial is supplied directly as twelve rational roots with common denominator `1000000`. The verifier expands those exact factors, evaluates the integer numerator using the already fully recomputed moments, and evaluates the denominator by integer products at every lattice site. It independently gives the same ceiling. This is a second rational certificate; no assertion that its polynomial is identical to the first is needed.

The original full verifier's checked components and this separately checked additive component cover the current entrypoint. I did not rerun the unchanged moment dynamic program a second time. Relevant new hashes are:

| File | SHA-256 |
|---|---|
| `certificate_factored.json` | `ba40cb85e5a0ebec3fa55d84c6d18569a7ff43b7b2132983258cd9ba47d7e970` |
| `verify_factored.py` | `fc24897d84d330b2b65317affc5222021f8883a0863c1be9a72b16059f408149` |
| updated `verify_publication.py` | `5ca8ded6580ac46a6948a7ae454f0e681ca0072a6e38f1c977645a6f3199a78f` |
