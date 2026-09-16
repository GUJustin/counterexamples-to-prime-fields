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

This does not settle the first-order linear MCA conjecture. Isolated
joint points and the number of nearby persistent affine codeword
graphs remain unresolved. It supplies no quadratic lower bound.

## Sharpness

For R=X^(D+1)+zX-1, the equation R P'-R_X P+P^2=0 has an actual
nonzero solution curve of degree D+1, plus the zero line, when
p>D+1. This stricter cutoff belongs to the example's classification.
The equation (X-z)P'-D P=0 has an actual surface of degree D+1.
Thus the linear dependence on D is real in both dimensions.

## Checks

Run sequentially from the repository root:

```sh
python3 research/first_order_actual_components/verify_reconstruction.py
python3 research/first_order_actual_components/verify_curve_family.py
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
