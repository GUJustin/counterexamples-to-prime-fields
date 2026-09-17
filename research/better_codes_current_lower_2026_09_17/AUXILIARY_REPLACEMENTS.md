# Target-A auxiliary source replacements

This manifest supplies actual replacement inputs for all27 auxiliary interpolation sources at A181275. It does not assert a completed benchmark certificate.

## Verified source gates

Each replacement preserves B,s,U,k,n0 and changes only m and, when necessary,L. The chosen m minimizes feasible L among all multiplicities in the previously exhaustively checked closed-rank regime B<=m<=U−s with the cutoff hypotheses. Source1 deliberately retains its original L2819 rather than shrinking to2796, preserving its geometric caps exactly.

All27 replacements pass exact coefficient-versus-rank positivity, every cutoff-cap inequality, every Params.WellFormed inequality, and all hypotheses used by the closed-rank formula. The target reserve is m*181275−reserve*50206; gap is50204 and errors+1 is80870. The manifest includes exact counts and boolean gates, not just positive gaps.

| Source | m | B | s | U | L | k | n0 | ΔL |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0 | 132 | 54 | 24 | 180 | 1811 | 5 | 7 | 25 |
| 1 | 133 | 56 | 25 | 180 | 2819 | 6 | 8 | 0 |
| 2 | 136 | 56 | 25 | 185 | 2638 | 6 | 8 | 54 |
| 3 | 116 | 46 | 21 | 158 | 2845 | 5 | 7 | 73 |
| 4 | 114 | 45 | 21 | 155 | 3170 | 5 | 7 | 92 |
| 5 | 158 | 63 | 29 | 215 | 3075 | 7 | 10 | 62 |
| 6 | 167 | 73 | 34 | 226 | 3169 | 8 | 9 | 52 |
| 7 | 114 | 47 | 21 | 154 | 2857 | 5 | 7 | 76 |
| 8 | 142 | 56 | 26 | 193 | 2801 | 6 | 9 | 57 |
| 9 | 174 | 76 | 36 | 236 | 2785 | 8 | 9 | 49 |
| 10 | 170 | 71 | 32 | 231 | 3168 | 8 | 10 | 63 |
| 11 | 97 | 41 | 19 | 132 | 2426 | 4 | 6 | 39 |
| 12 | 142 | 59 | 27 | 193 | 2460 | 6 | 9 | 45 |
| 13 | 158 | 69 | 32 | 214 | 2457 | 7 | 8 | 41 |
| 14 | 146 | 58 | 27 | 198 | 2544 | 6 | 9 | 46 |
| 15 | 98 | 41 | 19 | 133 | 2350 | 4 | 6 | 61 |
| 16 | 150 | 60 | 28 | 204 | 2325 | 6 | 9 | 37 |
| 17 | 161 | 71 | 33 | 218 | 2343 | 7 | 8 | 5 |
| 18 | 114 | 47 | 22 | 155 | 2784 | 5 | 7 | 73 |
| 19 | 166 | 66 | 31 | 226 | 2713 | 7 | 10 | 46 |
| 20 | 174 | 76 | 36 | 237 | 2764 | 8 | 9 | 48 |
| 21 | 111 | 46 | 22 | 151 | 3188 | 5 | 7 | 99 |
| 22 | 189 | 83 | 39 | 256 | 3171 | 9 | 10 | 59 |
| 23 | 114 | 45 | 20 | 155 | 3158 | 5 | 7 | 92 |
| 24 | 190 | 84 | 40 | 258 | 3104 | 9 | 10 | 56 |
| 25 | 111 | 46 | 21 | 151 | 3169 | 5 | 7 | 98 |
| 26 | 189 | 83 | 39 | 257 | 3141 | 9 | 10 | 57 |

## Geometric changes and activation

Multiplicity m is absent from the downstream flag and helper-cap formulas. Holding B,s,U,k,n0 fixed and increasing L by h changes the budget flag by (h,0,0), the coefficient cap by h in its total coordinate, and the helper cap by h in its total coordinate. Thus source1 preserves all geometric caps; the other26 increase them. All helper characteristic gates pass at both the existing root-domain corner (r,y,t)=(31,142,7501) and the expanded diagnostic corner(36,163,9678). This does not extend the root theorem beyond its existing domain.

Each triple is usable only when its maximum sourceL is strictly below the factor total degree. Fifteen of16 group sourceLimit values rise. Applied to the stored singleton assignments, this invalidates4808 intervals, containing197293 integer z values. Groups1,6,15 have no stored singleton uses; notably the sole exactly geometry-preserving group1 was unused. The JSON audit records group counts and concrete invalidated intervals.

The updated source flags dominate their old flags. Since flagMixed has nonnegative coefficients on nonnegative flags, new graph>=old graph. Independently evaluating all48 old graph-coordinate polynomials proves coefficientwise that target50204*oldGraph >= scale*131073*80870*identityDegree. Therefore target identity absorption is established for all16 triples without needing a stronger geometric theorem.

## Rebuilt root evaluator

`repaired_auxiliary_roots.py` implements the exact generic Profile.bound arithmetic with replacement sources and target constants. For fixed group,r,v, `root_lines(group,r,v)` returns four integer (slope,intercept) pairs. Their **maximum** is a safe singleton upper bound: three lines cover the three helper alternatives and one covers the retained alternative. The retained numerator is gap*graph + scale*sum(coefficientNumerators), over denominator gap*scale; combining floors gives a valid upper bound. Every rational numerator is affine in z; rounding its slope and intercept upward produces the reported line.

Across eligible triples, the solver may take the **minimum** of their maximum-of-four bounds. `root_domain(group,r,v)` returns the inclusive valid z interval: 3<=r<=31, v>=2, r+v<=142, z>=3, maximum sourceL<r+v+z<=7501. It returns None outside this domain.

The independent symbolic audit matches the evaluator against all16 authoritative baseline graph polynomial identities, then checks all64 replacement numerators are affine in z with coefficientwise nonnegative remaining polynomial coefficients. Numerical endpoint checks confirm the rounded envelopes dominate their exact rational alternatives.

## Remaining certificate obligations

1. Port Interpolant/source existence statements from hardcoded A181284 to target181275 and insert the exact replacement source counts. The arithmetic hypotheses are supplied; no Lean build is claimed.
2. Update catalog common L cap3117 to3188 and rebuild count receipts using the new graph/coefficient/helper expressions and the verified target identity inequalities.
3. Regenerate singleton choices with the raised sourceLimit values and new root envelopes. Frontier owns this step and the subsequent eight own/packed Bellman sheets. Old own inputs cannot simply be reused.
4. Rebuild full base, phase, threshold, aggregate, and final-ledger receipts on the repaired primary-source domains, including TCap total9678 if that replacement is selected.

Reproduction: run auxiliary_source_replacements.py, auxiliary_geometry_audit.py, then verify_repaired_auxiliary_roots.py under the repository watchdog. Scripts and JSON outputs are dedicated research files; shared paper and primary upstream Lean files were not edited.
