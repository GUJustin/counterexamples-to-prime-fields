# Exact test of the prescribed isogeny-norm label

The existing curve fixture is \(E/\mathbb F_{1657}:y^2=x^3+121\), with
full rational 23-torsion. The code has length 264, strict dimension 173,
redundancy 91, and tested agreement 213.

For every tested subgroup \(H\) and point \(P\notin H\), the support is
the two complete fibers tagged by \(x(3\phi_H(P))\) and
\(x(7\phi_H(P))\), together with the five coordinates
\(x(P),x(2P),x(4P),x(5P),x(6P)\). It has exactly 51 points.
The prescribed label is
\[
 \lambda=\kappa_H(P)=\prod_{j\in\{1,2,4,5,6\}}K_H(x(jP)).
\]
Its norm interpretation is proved in NORM_QUINTIC_PADE_ELIMINATION.md,
two directories above.

For the monic support locator \(U=\sum_{i=0}^{51}U_iX^i\), every
candidate pair of global syndromes must satisfy
\[
 \sum_{i=0}^{51}U_i(s_{f,i+j}+\lambda s_{g,i+j})=0,
 \qquad 0\le j<40.
\]
These are necessary and sufficient support conditions: the 40 shifted
rows are independent, and their kernel is the 51-dimensional span of
the corresponding parity-check columns.

**Exact result: rank 182, nullity zero.** The verifier stopped after 25
supports in 0.326 seconds, using 44.4 MB. The first five supports reached
rank 175; the 25th raised it to 182. The saved 182 independent original
row indices use only support records 0,1,2,3,4,24, providing a small
independent replay certificate.

Files:

* verify.py constructs supports, labels and recurrence rows from the
  existing immutable curve fixture, and stops immediately at full rank.
* selected_supports.json saves points, torsion coordinates, full supports,
  tags, labels, locators, rank progression, and the independent row indices.
* receipt.json saves hashes, resource usage and the exact scope.

Run from the repository root:

    /Users/jthaler/.local/share/research-toolchain/venv/bin/python research/elliptic_coset_complements/ell23_fixture/kappa_pencil/verify.py

The independent matrix SHA-256 is
6b7618ea3e29a81f9f4f46724ba77b119367a154c520efc104304ebbc7e4f2fb.
The verifier SHA-256 is
9d55beefc60b5248e1591c943390e8cf144efdbb02cf3d94f0301995cbb4d315.

Full rank excludes even a nonzero common syndrome pair satisfying these
selected prescribed-label constraints; hence it excludes the entire
prescribed labelled bank in this fixture. It does not exclude selected
subbanks omitting constraints, other labels, other curves, or general
moving quintics. One global projective reparameterization changes the
two syndrome blocks by an invertible linear transformation, so inversion
or affine changes of the labels do not require separate runs.

The subsequent all-label bound of at most \(2n\) for this particular
torsion support family is a separate structural argument in the parent
algebraic note; it is not inferred from this finite rank calculation.
