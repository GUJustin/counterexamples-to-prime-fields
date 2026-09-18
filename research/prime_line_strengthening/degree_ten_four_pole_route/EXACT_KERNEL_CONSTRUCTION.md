# Exact Paley net over the quadratic coefficient field

The prepared job `exact_kernel.sage.py` constructs the characteristic-zero
net directly over K=Q(eta), eta²+eta+2=0. This file describes the certificate;
successful execution is recorded separately by `exact_kernel.json` and
`exact_kernel.verified.json`. No characteristic-zero discriminants are
computed by this job.

Set alpha=(eta−1)/2 and c=3(eta+3)/4. The two base orbits are
`(zeta^j,zeta^(5j))` and `(alpha*zeta^j,c*zeta^(5j))`, where zeta is a
primitive seventh root. A monomial X^iY^j has character i+5j modulo7.
For each character1,3,5, the weighted box `i+3j<=34, j<=10` has32 monomials.
Impose the ten Hasse conditions of order below4 at(1,1) and the twenty-one
conditions of order below6 at(alpha,c). This gives a31-by32 matrix over K.
Eigencharacter equivariance carries the corresponding ideal-power
vanishing to all fourteen orbit points.

The job certifies rank31 and a one-dimensional kernel for each matrix.
Normalize the respective coefficients of Y10, X²Y10, X⁴Y10 to25,27,20.
At the split prime over29 with eta=7, these forms reduce exactly to the
three saved modular eigenvectors. The representative coordinates reduce
to alpha=3,c=22, and zeta=16 has quadratic period
zeta+zeta²+zeta⁴=7. The full saved217-rank modular minor bounds the exact
full220-column kernel dimension by3. The three constructed independent
eigenforms show it is exactly3. Thus this is a characteristic-zero lift
certificate, not an inference that an arbitrary modular kernel lifts.

Coefficient reduction uses a Hensel lift of eta when a rational-coordinate
denominator is divisible by29: integrality at the selected prime can hold
even when the coefficient has a pole at the other split prime. The
independent checker implements the quadratic field as Fraction pairs and
rechecks the equations and modular ranks without Sage.

Run from this directory, with the two explicit input files available:

```sh
sage -python exact_kernel.sage.py --gate gate.json --fibers ../quadratic_one_pole_route/fiber_patterns.json --output exact_kernel.json
python3 verify_exact_kernel.py
```

The intended job guard is60seconds and2GiB. Output checkpoints are written
after each character. All exact coefficients and a nonzero31-by31 rank
minor determinant per component are serialized as rational pairs in the
basis1,eta, with input hashes for provenance.
