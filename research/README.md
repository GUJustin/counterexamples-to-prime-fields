# Proof notes and exact checks

The manuscript and repository README identify the current claims and strongest
certificates. These folders also preserve intermediate certificates and review
notes, whose numbers describe their recorded checkpoints.

| Folder | Contents |
|---|---|
| `finite_weights` | Exact degree-40 conditional certificate and earlier checkpoints |
| `gram_norm`, `moment_bounds` | Classical Gram norms, normalization, and proof reviews |
| `ellipsoid_bound`, `gaussian_bound` | Finite concentration, Gaussian asymptotics, and radial reviews |
| `growing_m` | Uniform estimates and the gap/field-size corollary |
| `curve_audit`, `puncturing_improvement` | Witness bounds, sharp endpoints, and exact finite checks |
| `structured_domains` | Proven transfer lemmas and limits of proposed transfer arguments |
| `moment_literature` | Primary-source attribution checks |
| `paper_referee`, `reproducibility` | Integration reviews and validation records |
| `workspace_reconciliation` | Saved-draft comparisons and historical source repair |

Run `make verify` from the repository root. Numerical checks supplement the
proofs and retain the parameter restrictions stated in the manuscript.
