# Complete F49 monomial gate

Field F7[theta]/(theta²−3), domain F49*, all exponents d=0,...,47. `gate.py/json` enumerate the 49² quadratics normalized by Q(1)=1 and recover the exact codewide histogram using L_A=48 H_A/A. The same orbit identity applies to the invariant subfamily with all three coefficients nonzero. Zero-agreement counts follow by subtraction. All three factorial incidence moments (through triples) are checked for every exponent.

Runtime: 0.34 seconds. No larger-field search.

Six exponents have full-coefficient quadratics with at least seven matches:

| d | Full-coefficient words with ≥7 matches | Their agreement | Coefficient span rank over F49 |
|---|---:|---:|---:|
| 14,21,22,28,29,36 | 48 each | exactly 7 | 3 |

Each is exactly one multiplicative-scaling orbit: any full-coefficient quadratic has trivial stabilizer under the action Q(X)→t^d Q(X/t), since the three coefficient exponents are consecutive. Thus these are genuine three-coefficient banks, but their size is only p²−1, not p³. Linear span rank three alone does not show absence of a nonlinear conic relation among coefficients.

For d=14 and 36 there are additionally 24 quadratics with eight matches and four with twelve matches; those have at least one zero coefficient. Their total ≥7 population is 76, the largest nontrivial population in the census. The codeword exponents 0,1,2 each have their trivial exact witness and are not construction candidates. No exponent has a full-coefficient ≥7 bank larger than 48.

`replay.py/json` independently enumerates ALL 49³ quadratic coefficient triples, evaluates by tuple-arithmetic Horner, and directly matches against the six positive monomial words. It does not use Q(1)=1, multiplicative normalization, or the histogram recovery formula. All six full and unrestricted histograms agree exactly. It also computes the coefficient ranks. Runtime: 2.33 seconds.

This small gate finds full-coefficient rank-three families but no population improvement over the p²-scale core. It provides no asymptotic obstruction or counterexample. Do not enlarge the scan merely on these results; a structural identity increasing the number of orbits is still needed.
