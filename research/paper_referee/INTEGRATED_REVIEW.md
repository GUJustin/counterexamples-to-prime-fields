# Final integration review of the current paper diff

Scope: additions and edits shown by `git diff -- paper.tex`, September 15,
2026. The root agent owns manuscript edits. No protocol code was executed.

## Required hypothesis fix

At `prop:support-incidence`, explicitly declare the finite field, dimension,
curve degree, and coefficient-word domain. Suggested opening:

```tex
Let $F$ be a finite field, let $C\subseteq F^n$ be a linear
$[n,k]$ MDS code with $1\le k<n$, and let $e\ge0$ be an integer.
Let $k+1\le t\le n$ be an integer, and let
$f(z)=\sum_{j=0}^e z^j f_j$ with $f_j\in F^n$.
```

Also write “for every integer $k+1\le b\le t$.” The displayed cardinality
bound uses `|F|`, so finiteness should be in the proposition rather than
inferred from neighboring statements. The `e=0` case is valid: a constant
word agreeing with a codeword on its entire agreement set explains that
set, so the exceptional-pair collection is empty.

At `cor:curve-endpoint-sharp`, call `e` an integer as well. The construction
and field-extension choice otherwise justify its stated scope.

## New arguments checked

- **Gap/field corollary:** the optimized length
  `n ~ H/(epsilon^2 log_2(1/epsilon))` gives leading list logarithm
  `H^2/(2 epsilon^2 log_2(1/epsilon))`. Rounding to an integral dimension
  and taking `m=ceil(epsilon n)` are handled correctly by monotonicity.
  All displayed error terms are `o(n)`. For every sufficiently large
  prime, `epsilon=(H+b^(-1/2))/b` guarantees strict Elias separation
  and yields `n ~ b^2/(H log_2 b)` and list logarithm at least
  `(1/2-o(1))b^2/log_2 b`.
- **Gram/ellipsoid:** the normalized Gram variance formula agrees with the
  first two special cases. Axis-aligned unit cubes do tile a lower-triangular
  unit-diagonal lattice: recursively select the integer coordinate in each
  successive row. Thus smoothing adds covariance `I/12` and the density
  calculation is justified; a shear does not invalidate this particular
  triangular tiling argument.
- **Sparse Gaussian regime:** for fixed moment count, the finite-population
  criterion tends to zero under `min(t,n-t)->infinity`, and all coordinate
  variances diverge. The limiting Gaussian ball argument takes the fixed
  radius limit before shrinking the ball, so it does not require a local
  central limit theorem or assert the mass of a prescribed signature.
- **Circuit incidence:** applying the local rejection lemma to one bad
  coefficient restriction supplies the weighted support count. Each test
  has at most `min(e,|F|)` accepting parameters and at most one global
  codeword per such parameter. No restriction `e<|F|` is needed. In the
  puncturing range, the successive-ratio argument correctly selects `b=k+1`.
- **Curve endpoint:** choosing distinct subset sums and an offset outside
  them makes all splitting polynomials separable with disjoint root sets.
  This gives exactly `e binom(n,k+1)` parameter-witness pairs and unique
  witnesses. The coefficient `-X^k` excludes joint agreement on `k+1`
  coordinates. Incidence counting gives concurrency `e(n-k)`, attained
  by composing the extremal affine codeword line with the scalar map.

## Certificate check and newest-artifact warning

I independently parsed the 24 displayed integer roots from `paper.tex`,
expanded their monic polynomial, evaluated its weighted numerator from the
saved exact centered moments, and summed the positive weights over all
integers in `[17969,26129]`. The resulting ceiling is exactly
`5,141,180,908,468`. The claimed ratio greater than `1197 * 2^32` is also
correct. This check does not recompute the moment dynamic program.

The saved `research/finite_weights/certificates_verification.json` currently
reports an additional passed degree-28 coarse certificate of
`5,183,805,053,471`. The degree-24 paper claim remains correct, but the root
should reconcile the weight agent's latest status before presenting it as
the strongest available certificate. Do not silently exchange the number
without its corresponding polynomial/certificate description.

## Wording and structural checks

The three earlier editorial corrections are integrated correctly. Exact
interval and isolated-line counts remain exact; the real circle-list proof
now distinguishes exact nonanchor agreement from full-domain lower bounds.

A structural scan found no duplicate labels, missing references, missing
bibliography keys, mismatched LaTeX environments, or unclosed environments.
This is a source scan, not a fresh LaTeX build. The inserted comment
“Insertion candidate” above the incidence proposition can be removed as
editorial cleanup; it does not affect the rendered paper.

The new comparison paragraph in the ellipsoid section still names the
degree-20 conditional certificate as stronger. That statement is true, but
for current-result emphasis it can mention the degree-24 certificate too,
or simply say “the conditional polynomial-weight certificates remain
stronger.” No numerical or logical correction is needed there.
