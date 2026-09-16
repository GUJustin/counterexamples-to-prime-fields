# Actual first-order solution components

For a first-order equation Q(X,z,P,P')=0 of fixed jet degree B and
challenge degree H, the sum of the degrees of its actual curve and
surface components is O(D), where deg P<=D and the characteristic
is zero or greater than D. The equation's X-degree is unrestricted.
The regular locus requires Q_{P'} not to vanish identically in X.

With tau=max(0,2D-3), b=1+tau(B-1), T=b+tau H, K=H+B T, and q=B+H:

    J_1 <= q K,      J_2 <= q T.

The reduced generic challenge fiber of the surface components has
degree at most deg_{P'} Q. Appendix H supplies the proof; `PROOF.md`
explains the geometry and scope. The proof is twice self-reviewed;
no independent coauthor review or novelty claim is asserted.

Corollary H.2 bounds the nearby pairs on all nonaffine curve components
by `(n-D)/(A-D) * q*K`, hence linearly in n at a fixed positive gap.
It follows by counting agreement hyperplanes. The omitted affine
codeword graphs are stated explicitly, rather than silently absorbed
into this finite nearby-pair count.

This does not settle the first-order linear MCA conjecture. The general contribution of isolated
joint points and the number of nearby persistent affine codeword
graphs remain unresolved. It supplies no quadratic lower bound.

## Sharpness

For R=X^(D+1)+zX-1, the equation R P'-R_X P+P^2=0 has an actual
nonzero solution curve of degree D+1, plus the zero line, when
p>D+1. This stricter cutoff belongs to the example's classification.
The equation (X-z)P'-D P=0 has an actual surface of degree D+1.
Thus the linear dependence on D is real in both dimensions.

## Quadratic isolated family

The equation `(z-X^2)(R P'-R' P+P^2)+2X R P-2R^2=0`, for monic
squarefree R of degree D+1 with nonzero roots, has exactly
`binom(D+2,2)` actual regular isolated solutions in characteristic zero
or p>D+2. They are `z=ab, P=R/(X-a)+R/(X-b)`, with repeated roots
allowed in the pair. A greedy multiplicative Sidon set makes every
label distinct over prime fields of size O(D^3).

Despite this quadratic solution count, any received line has only
O_eta(1) nearby labels from this family at agreement A-D>=eta*n
for sufficiently large n. If r0 domain coordinates are roots of R,
m=n-r0, t=A-r0, and t^3>4m^2, the explicit bound is
`2m/(t-(4m^2)^(1/3))`. A linear bound `(D+2)n/(A-D)` holds for all
A>D. This proves the need for an agreement argument beyond simply
counting isolated solutions; it is not a quadratic error lower bound.

## Checks

Run sequentially from the repository root:

```sh
python3 research/first_order_actual_components/verify_reconstruction.py
python3 research/first_order_actual_components/verify_curve_family.py
python3 research/first_order_actual_components/verify_isolated_family.py
```

The reconstruction checker requires SymPy. It checks five equations,
576 finite Taylor fixtures, and 40 explicit linear-equation curves.
The standard-library family checker exhausts 33,849 polynomial--label
pairs satisfying the nonlinear example's characteristic assumption,
verifies 39 split reduced sections, and includes 81 pairs in a negative
control outside that stricter assumption. The checks supplement the
proof; they cannot establish the generic-section argument.

Resource records use sequential 384 MiB watchdog runs. Their RSS values
are sampled process-group usage, not exact high-water measurements.

The isolated-family checker covers 180,384 polynomial--challenge pairs
by exhausting 17,410 polynomials and solving the residual's affine
challenge dependence exactly. It also checks 2,142 local received-value
choices, 108 derivative identities, 14,376 distinct-label rational
triple numerators, and 219,450 integer multiplicity vectors. Sidon
fixtures reach 2,145 distinct labels at D=64. A characteristic-three
negative control confirms the need for a characteristic restriction.
