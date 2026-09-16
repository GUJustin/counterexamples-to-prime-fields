# Binary-affine support transfer has a sharp odd-characteristic limit

For an r-dimensional affine binary family of t-element subsets of an
n-point domain, with the same first s leading locator coefficients,

    r <= floor(min(t,n-t)/(s+1))

in every characteristic other than two. The bound is sharp over suitable
prime-field domains. A trace-hyperplane family over F_16 violates it,
showing that this specific binary structure cannot transfer unchanged.
The theorem does not exclude nonlinear binary families or other transfers.

The new codimension-two corollary applies the theorem to affine planes
inside a potentially nonlinear support family. Under any injective
odd-characteristic relabeling of the nonzero elements of F_2^m, at most
`floor((N-1)*floor((1+sqrt(4*N-7))/2)/3)` punctured codimension-two
subspaces can share their first `N/8-1` locator coefficients. This is
`O(N^(3/2))`, whereas characteristic two supplies the entire quadratic
family. See `CODIMENSION_TWO_TRANSFER.md` and Corollary F.2.

`PROOF.md` gives the proof, examples, and scope. It is self-reviewed;
no independent mathematical review or novelty claim is made.

From the repository root:

```sh
python3 research/binary_affine_locator/verify.py
python3 research/binary_affine_locator/check_codimension_two_transfer.py
```

The standard-library checker visits 103,416 affine binary spaces and
checks all 8,407 constant-weight families, 20 sharpness examples, and
the characteristic-two negative control. It writes
`binary_affine_locator_verification.json`. Finite checks supplement the proof.
The second checker tests 24,825 prefix classes in 390 relabelings,
14,364 affine-plane parameterizations, and full binary negative controls
over F_16 and F_32. It includes an F_81 case with characteristic equal
to the prefix length. Both checkers are part of `make verify`.
