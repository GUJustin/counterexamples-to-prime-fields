# Independent audit: moving-extra three-edge path rationality

2026-09-19. **PASS for the corrected final source.** The pole-free strengthening and discrepancy intersection are now integrated; the hash below identifies that version.

Adjacent chosen syndrome points are indeed distinct: their proportional difference has support at most 3ell+10≤4ell−1, and is nonzero on an exclusive leaf outside the other error's at most five extras. MDS independence forbids such a codeword. Consequently the first and third coefficients in a path relation are nonzero. The resulting word is nonzero because at most ten contaminating extra coordinates can cancel the first leaf's more-than-ten nonzero entries.

Removing from the combined extra set all four path fibers leaves a squarefree locator J with degree d≤15 and no leaf roots. The representing codeword is divisible by Φ/(F_a F_b F_c F_d J). The strict code dimension gives degree of its remaining nonzero factor Q at most d, exactly as stated. The quotient-map product identity restricts Φ/(F_a F_b F_c F_d) to a nonzero scalar times C_H on each selected fiber. Hence the leaf weight equals cQ/J away from the at most ten extra positions of the other two edges. No full-support assumption is needed.

Two path models have nonvanishing denominators on the leaf. They agree at at least ell−20 points; their cross-product has degree≤30, so ell>50 forces rational identity. Its reduced denominator divides every path locator J. This proves path independence without asserting any global label bound, common model across edges, or exact equality on the contaminated coordinates.

## Stronger precise compatibility consequences

Every path representation has deg Q≤deg J. Cancellation preserves that degree inequality. Thus for the intrinsic reduced model P/D,

    deg P≤deg D,  D divides gcd_(all extensions) J.

If the common path-extra intersection is empty, D is constant and P is constant too. The final source correctly includes this conclusion. The actual leaf vector may still have up to ten discrepancies from this constant model; those discrepancies are the reason one cannot immediately recover an exact canonical leaf vector.

There is also an exact constraint on those discrepancies. For each path a-b-c-d define Z_path=(E_bc union E_cd) intersect D_a. The discrepancy set of e_ab/C_H from its intrinsic model is contained in EVERY Z_path, hence in their intersection. If two extensions have disjoint contamination sets on D_a, the intrinsic model is valid on the entire leaf. Combining this with gcd J=1 makes that leaf exactly C_H-weighted. These are conditional compatibility consequences, not a claim that a large graph automatically supplies such paths.

No scan, manuscript edit, or unproved global edge bound was used.

## Bounded graph follow-up: a shared outside hub defeats clean-path forcing

The cardinality restriction |E_edge|≤5 and a large graph core do NOT by themselves ensure trivial path-denominator gcd. Fix a domain coordinate z* outside all fibers used as graph vertices (for example, in one omitted tag fiber or in the kernel). Take the complete graph on all the remaining nonkernel fibers and assign E_edge={z*} to every edge. Every simple path then has J=X−z*, so its path-locator gcd is nonconstant, however large the minimum degree. Its leaf contamination sets are empty, yet the intrinsic leaf model is only constrained to (uX+v)/(X−z*), not to a constant.

This is a support-allocation counterpattern to a graph-only clean-path argument, NOT a construction of error vectors with their syndromes on a genuine common line. The syndrome compatibility may further constrain these models. It is precisely a fixed-extra-set case of the already defined generalized subgroup spaces. A positive route or global bound must use that additional algebra, or prove a structural alternative separating shared hubs from sufficiently clean paths. The argument does not establish a global linear bound or a superlinear construction.

Final source SHA256: `01f9ae93f1e95df7686f9210e1d6fea864fe74edf367f65abcc9aa9429671b0f`.
