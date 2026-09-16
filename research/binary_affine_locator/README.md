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

Theorem F.3 gives a sublinear bound within every fixed multiplicative
orbit of subspaces of fixed binary codimension. At codimension two
and prefix length `N/8-1`, it is `(4/h)*N^(15/16)`, where the scalar
stabilizer size h is one or three. Thus a bounded number of such orbits
cannot supply a linear-sized transferred list. This includes the
F4-linear hyperplane family (h=3), but leaves open a collection spread
across an increasing number of orbits. See `MULTIPLICATIVE_ORBIT_TRANSFER.md`.

Theorem F.4 treats multiplicative (and affine-multiplicative) relabeling
across all subspaces. Gauss sums transfer primal moments to the small
dual subspaces. For codimension r, `2^(r+1)-3` coefficients distinguish
all supports in every odd characteristic; `2^r-1` suffice when the
characteristic exceeds that number. The latter cutoff is sharp. At
codimension two this means five coefficients, or three in characteristic
greater than three. See `MULTIPLICATIVE_LABEL_RIGIDITY.md`.

`PROOF.md` gives the proof, examples, and scope. It is self-reviewed;
no independent mathematical review or novelty claim is made.

From the repository root:

```sh
python3 research/binary_affine_locator/verify.py
python3 research/binary_affine_locator/check_codimension_two_transfer.py
python3 research/binary_affine_locator/check_multiplicative_orbit_transfer.py
python3 research/binary_affine_locator/check_multiplicative_label_rigidity.py
```

The standard-library checker visits 103,416 affine binary spaces and
checks all 8,407 constant-weight families, 20 sharpness examples, and
the characteristic-two negative control. It writes
`binary_affine_locator_verification.json`. Finite checks supplement the proof.
The second checker tests 24,825 prefix classes in 390 relabelings,
14,364 affine-plane parameterizations, and full binary negative controls
over F_16 and F_32. It includes an F_81 case with characteristic equal
to the prefix length. The third checker tests the Fourier support
formula on binary affine flats, both codimension-two stabilizer cases,
and a codimension-three orbit; it includes odd-field prefix fixtures,
a characteristic-two control, and a complete small odd-field transfer.
The fourth checker exhausts 26,114 subspaces in prime-field fixtures
and 155 in a characteristic-three extension, checks the Gauss identities,
and verifies sharpness at N=512. All four checkers are part of `make verify`.
