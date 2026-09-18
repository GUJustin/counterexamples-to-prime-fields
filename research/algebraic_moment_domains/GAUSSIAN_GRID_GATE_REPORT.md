# Exact Gaussian-grid lattice gate: six verified samples

All six certificates independently PASS. None yields a nontrivial list lower bound at s=m. Gaussian grids have a larger reduced width cost than the same-size intervals in all three samples. These are outcomes of the specified HNF + LLL coordinate search, not optimality or asymptotic impossibility statements.

The subsets have fixed cardinality n/2. Accordingly each integer coordinate uses the sharper width (sum of largest n/2 entries minus sum of smallest n/2 entries), rather than unrestricted subset-sum width. The certificate is log2 binom(n,n/2) minus sum log2(1+width).

| m=s | n | subset entropy | Gaussian width cost | interval width cost | Gaussian minus interval |
|---:|---:|---:|---:|---:|---:|
|8|64|60.669|144.227|140.292|3.934|
|12|144|140.087|363.653|343.566|20.087|
|16|256|251.673|692.389|645.276|47.113|

The invariant log2 lattice-normalized Gram covolumes (Gaussian, interval) are (107.069,120.956), (296.535,306.719), and (591.879,588.741). Thus the Gaussian invariant improves in the first two samples but not the third; the width certificate is worse throughout. The dimensions differ (2s+1 versus s+1), so the Gram invariant by itself is not a complete lattice-point entropy bound.

## Search and independent verification

`grid_gate.py` constructs exact integer moments. FLINT computes the row HNF of A^T and LLL with delta=.99 on normalized integer coordinates C. It saves A,B,C,J,U,R with

    A=B C, A J=B, R=U C, det(B)!=0, det(U)=+-1.

The first two identities prove equality of the column lattice of A with B Z^k, not merely containment. Every search result is an explicit integer certificate, independent of floating-point choices inside LLL. `verify_grid_certificates.py` uses only Python's standard library. It reconstructs Gaussian moments through binomial sums (a separate algorithm), verifies all matrix identities, computes determinants with exact Bareiss elimination, recomputes widths and the exact integer entropy comparison. All six PASS; every signature upper bound exceeds the number of subsets.

Each m job completed below 0.6 seconds including the watchdog. The six-case independent verification completed below 0.6 seconds. All stayed well inside the 384 MiB / 60 second caps. Raw matrices, JSON reports, and watchdog receipts are saved alongside this note. python-flint, fpylll, and cysignals were installed in the research-toolchain venv; this gate used FLINT HNF/LLL, not fpylll/BKZ.

No inference is made about better bases, other moment orders, other domains, actual maximum fibers, or the limit m->infinity. In particular, failure of this upper-bound-on-signatures certificate does not show that the actual fibers are small.
