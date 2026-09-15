# Attribution audit: interval moments and concentration

Audit date: 2026-09-15. This note reviews the current manuscript's moment construction and the proposed Gram, Gaussian, and smoothed-ellipsoid additions. It makes no priority claim. Source files consulted: `paper.tex`, `gram_moment_norm_proof.md`, `gram_gaussian_class_bound.md`, and `ellipsoid_moment_bound_audit.md` in the frontier workstream. All references below are primary research sources or the NIST mathematical reference.

## Required attribution

1. **Equal moments and Reed–Solomon decoding are established connections.** Gandikota–Ghazi–Grigorescu, Section 2, Definitions 2.1/2.3 and Lemmas 2.2/2.4 explicitly connect moments subset sums, symmetric sums, and RS decoding. Their text also attributes the Newton-identity connection to earlier work. The current manuscript already acknowledges this correctly. Lai–Marino–Robinson–Wan explicitly define the higher-moment subset count over finite-field evaluation sets and study algorithms for special domains; their results should not be described as integer-interval Gaussian class estimates. Add this latter citation if the related-work discussion expands to counting/algorithms. [GGG](https://arxiv.org/html/1611.03069), [LMRW](https://pmc.ncbi.nlm.nih.gov/articles/PMC10941333/).

2. **The Gram polynomial identity is classical.** Lin–Wong (1.1) gives the forward-difference definition, and (1.2) gives the exact uniform-grid norm. For the draft's degree `j`, grid size `n`, and normalization `B_j`, the conversion is `B_j = j!/(2j)! * t_j(.,n)`. This yields exactly the draft's variance product. The zero-parameter Hahn interpretation is also stated there. DLMF uses grid `{0,...,N}`; set `N=n-1`. These are normalization conversions and a self-contained proof of a known identity, not a new orthogonal-polynomial result. [Lin–Wong](https://arxiv.org/html/1207.2536), [DLMF §18.19](https://dlmf.nist.gov/18.19).

3. **The Gaussian step uses the classical finite-population CLT.** Li–Ding Theorem 1 explicitly credits Hájek and supplies precisely the maximum-squared-deviation condition used by the proposed proof. Their formula (4) permits triangular arrays. Credit Hájek, citing Li–Ding for the convenient sufficient condition. The original Hájek article metadata was verified through its institutional archive; its scanned proof was not independently re-audited here. [Li–Ding Theorem 1](https://arxiv.org/html/1610.04821), [Hájek archive](https://real.mtak.hu/200979/).

4. **The sharp continuous ellipsoid bound is also classical.** Bobkov–Madiman Proposition III.1 and the proof of Corollary III.2 give, for density `f` with covariance `R`,

   `||f||_infinity >= 1/[omega_m (m+2)^(m/2) sqrt(det R)]`.

   Their Section III traces the comparison to Hensley and Ball. Applying this inequality after independent unit-cube smoothing yields exactly the proposed bound with `V_j+1/12` when the coordinates are uncorrelated. The continuous inequality should be attributed even if the manuscript retains its short signed-weight proof. No log-concavity is needed for this inequality. [Bobkov–Madiman, Section III](https://arxiv.org/html/1006.2883).

## What can be claimed precisely

- The manuscript establishes the displayed list/line lower bounds and the exact finite certificate. Its contribution can be stated as the **quantitative application and explicit bounds proved here**. This audit does not establish that these are the first such bounds in the literature.
- The factor `n^(m/2)` compares concentration with this paper's product-of-complete-ranges pigeonhole estimate, for **fixed** `m` and `t/n -> rho` in `(0,1)`. It is not an audited improvement over the best published general moment-counting bound.
- Gram orthogonalization improves the constant by using the exact covariance. It does not change the exponent `m(m+2)/2` already supplied by uncorrelated or even unadjusted moment concentration.
- The Gaussian result is a **liminf lower bound for a largest class**, with normalized constant `(2*pi)^(-m/2)`. It gives neither an asymptotic equality, a local limit theorem, nor the probability of a prescribed signature. The fixed-radius limit must precede the small-radius limit. A nonquantitative diagonal sequence may approach the center; no explicit shrinking rate follows.
- The finite smoothed-ellipsoid bound improves the constant relative to the manuscript's rectangular Chebyshev bound by `(m+2)*2^(m-1)/omega_m` asymptotically. This is an explicit comparison of two methods, not a priority claim for density concentration.
- The exact polynomial-weight certificate is a reproducible lower-bound certificate. Its general inequality follows directly by discarding negative contributions and bounding each positive-weight class by the largest class. Do not claim an optimal moment bound or a newly invented optimization principle without a separate comparison/proof.

## Suggested manuscript wording

> We combine the classical Gram-polynomial norm with finite-population concentration to count subsets of an integer interval having the same moments. The resulting bounds improve the complete-range pigeonhole estimate used above. The sharper asymptotic constant follows from Hájek's finite-population central limit theorem, in the form stated by Li and Ding, and a lattice-counting argument. We use only weak convergence; the conclusion is a lower bound on the largest class, rather than a local limit theorem.

For the optional ellipsoid proposition:

> The continuous inequality in the proof is the classical maximum-density/covariance bound; see Bobkov and Madiman, Proposition III.1 and the proof of Corollary III.2. Unit-cube smoothing transfers it to the triangular moment lattice, with the exact variance correction `1/12`.

## Integration checklist

- Cite `linwong` at the Gram norm and `liding`/`hajek` at the Gaussian step.
- Cite `bobkovmadiman` at the smoothed ellipsoid argument if included.
- Preserve the existing GGG attribution; optionally add `lmrw` for finite-field moment counting.
- State fixed `m`, `rho in (0,1)`, and the lower-bound-only qualification beside the Gaussian result.
- Do not label any of these probability/orthogonal-polynomial ingredients new.
- Bibliography entries are staged in `citations.tex`. No manuscript edits or git operations were performed by this audit.
