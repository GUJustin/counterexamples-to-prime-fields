# Sharp isolated-solution counts at fixed derivative order

Appendix I proves that the number of actual isolated regular polynomial--
challenge solutions is O(D^(d+1)) at fixed differential order d, fixed jet
degree, and fixed challenge degree, in characteristic zero or p>D.
An explicit Wronskian equation attains exactly binom(D+d+1,d+1) solutions
in characteristic zero or p>D+d+1. All solutions are regular and isolated.
Their labels can be distinct over prime fields of size O_d(D^(2d+1)).

The construction sets r=d+1, chooses a squarefree degree-D+1 polynomial
R with nonzero roots, and takes

    Q_r = Wr(R phi_1'-P phi_1, ..., R phi_r'-P phi_r),
    phi_j=X^j (j<r), phi_r=X^r+z.

Every solution is P=R H'/H, z=H(0), for a degree-r root multiset H
supported on R. Its separant is a nonzero constant times
R^(r-1)*(X^r+(-1)^(r-1)z), so regularity is automatic.

This proves sharp growth of algebraic candidate counts. It does not
prove sharp proximity-gap error. For this same family, any received line
has only O_{d,eta}(1) nearby labels at agreement A-D>=eta*n and large n.
The general first-order linear conjecture and fixed-gap quadratic
proximity-gap lower-bound target remain open.

## Verification

Run sequentially from the repository root:

```sh
python3 research/isolated_solution_sharpness/verify_reconstruction.py
python3 research/isolated_solution_sharpness/verify_family.py
```

The reconstruction checker uses SymPy and verifies 360 Taylor fixtures
on four equations of orders two through five. The standard-library
family checker exhausts 760 polynomials, covers all 5270 polynomial--
challenge pairs in those fixtures, and checks the explicit separant
through order five. Six prime-field B_r fixtures include 969, 495, and
462 distinct isolated labels at orders two, three, and four. Two
small-characteristic negative controls produce extra solutions.

Triple checks include a genuine product-label collinear triple and a
five-point affine family under alternative labels. The latter attains
the collinear-triple allowance in the agreement argument.

Proofs have been twice self-reviewed, without an independent coauthor
review or novelty claim. The generic intersection argument is proved
in `appendix.tex`; finite checks alone do not establish it. Numerical
jobs are sequential under a 384 MiB watchdog. RSS in the records is
sampled process-group usage, not an exact high-water measurement.
