# Linear differential constraints and full-support proximity gaps

This supplementary note proves an O(n) bad-challenge bound at a fixed
positive gap for polynomial candidates satisfying a challenge-dependent
affine linear system with bounded challenge degree and bounded generic
kernel dimension. It applies in particular to differential equations of
any fixed order that are affine-linear in the polynomial and derivatives,
in characteristic zero or characteristic greater than the degree bound.

The statement includes inhomogeneous equations and exceptional rank-drop
labels. The number of operator rows and their X-degrees are unrestricted.
`PROOF.md` gives the finite bound, proof, classical attribution, and scope.

This does not prove the general first-order linear conjecture, which also
allows nonlinear jet constraints, and supplies no quadratic lower bound.
It does not improve the pinned better.codes score. The proof is self-reviewed;
no independent mathematical review or literature priority is claimed.

## Reproduce

From the repository root, run:

```sh
python3 research/linear_differential_mca/verify.py
```

The checker uses only Python's standard library. It enumerates solutions
and verifies the proof's intermediate inequalities on 24 matrix/ODE
fixtures and 88 received lines, including rank drops and inhomogeneous
systems. Results are written to `linear_differential_mca_verification.json`.
Finite tests supplement the proof. Resource reports record sequential
execution under a 384 MiB watchdog; sampled RSS can miss a short job's peak.
