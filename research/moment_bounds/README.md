# Gram coordinates and moment class bounds

These notes support the moment-counting additions to `paper.tex`. The Gram norm, finite-population central limit theorem, and continuous density/covariance inequality are classical; the paper credits their sources. The notes give normalization details and proofs for this application. No priority claim is made.

- `gram_moment_norm_proof.md`: exact classical norms and orthogonality.
- `ellipsoid_moment_bound_audit.md`: triangular-lattice tiling and the exact unit-cube variance correction.
- `gram_gaussian_class_bound.md`: a lower bound for the largest class with a fixed number of moments; not a local limit theorem or finite-length estimate.

Run `python3 checks/check_gram_ellipsoid.py` from the repository root. It checks 243 Gram norms, 1,155 orthogonality identities, 65 exhaustive small-subset fixtures and the exact length-64 quadratic certificate. The existing conditional polynomial certificate remains stronger.
