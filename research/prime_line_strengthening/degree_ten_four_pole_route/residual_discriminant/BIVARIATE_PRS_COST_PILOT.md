# Direct bivariate PRS cost pilot

The new direct algorithm completed six exact Brown subresultant remainder
steps over F29[s,t], reaching X degree41. It stopped at its own intermediate
term guard while forming the next pseudo-remainder. This is a cost result,
not an exclusion, and it did not reach the target X degree14.

`bivariate_prs_pilot.py` uses native python-flint multivariate polynomial
coefficients. It checks every scalar polynomial division for zero remainder.
At each completed step it independently specializes the coefficient
polynomials and compares them to a univariate finite-field PRS at all
fixed comparison points with matching nondegenerate degree profiles.
Six such points remain valid through the final completed step.

| X degree | Total coefficient terms | Maximum parameter total degree | Cumulative seconds |
|---:|---:|---:|---:|
|46|9148|52|0.004|
|45|25187|88|0.022|
|44|48489|124|0.232|
|43|78656|160|1.967|
|42|115240|196|7.033|
|41|157404|232|20.557|

There were220 verified exact coefficient divisions. The next intermediate
exceeded1,200,000 coefficient terms, triggering a deliberate stop after
38.83seconds. The wrapper reported38.99seconds and95328KiB peak RSS, below
its60second/384MiB limits. This was neither a timeout nor an out-of-memory
failure. The exact checkpoint and wrapper receipt are
`bivariate_prs_pilot.json` and `bivariate_prs_pilot.resources.json`.

The profile establishes that this algorithm behaves substantially better
than a generic giant determinant at its early steps. It does not establish
that completing all33 steps is economical: per-step time and intermediate
term counts are increasing rapidly. No rental or larger continuation was
launched on the strength of this pilot alone.

All Brown divisions were algebraically exact, not saturations or discarded
parameter conditions. The finite-field comparison points validate the
implementation at those points and supplement exact arithmetic; they are
not a parameter census or a proof of global rank. No zero-content,
degree-drop, or boundary stratum has been removed from a mathematical
conclusion, because no global conclusion is claimed.
