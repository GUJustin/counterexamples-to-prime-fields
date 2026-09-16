# Binary-affine support transfer has a sharp odd-characteristic limit

For an r-dimensional affine binary family of t-element subsets of an
n-point domain, with the same first s leading locator coefficients,

    r <= floor(min(t,n-t)/(s+1))

in every characteristic other than two. The bound is sharp over suitable
prime-field domains. A trace-hyperplane family over F_16 violates it,
showing that this specific binary structure cannot transfer unchanged.
The theorem does not exclude nonlinear binary families or other transfers.

`PROOF.md` gives the proof, examples, and scope. It is self-reviewed;
no independent mathematical review or novelty claim is made.

From the repository root:

```sh
python3 research/binary_affine_locator/verify.py
```

The standard-library checker visits 103,416 affine binary spaces and
checks all 8,407 constant-weight families, 20 sharpness examples, and
the characteristic-two negative control. It writes
`binary_affine_locator_verification.json`. Finite checks supplement the proof.
