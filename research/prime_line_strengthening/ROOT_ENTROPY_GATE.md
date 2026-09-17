# Exact entropy gate for full-image completion at the covering radius

2026-09-17. Root derivation; conditional template statement, not a general line impossibility.

Let n=2m+2r, k=2D, 0<D<m, r>=1, rho=k/n, eta=2r/n, and y=rho+eta<1. Suppose a bank indexed by D-subsets of an m-element set surjects onto (F_p^*)^r. Then

    (p-1)^r <= binom(m,D).

Write a=2m/n and theta=D/m. Thus y=a theta+eta and a+eta=1. With natural-log binary entropy h,

    eta ln(p-1) <= (2/n) ln binom(m,D) <= a h(theta).

The exact entropy identity gives

    h(y)-a h(theta)
      = a KL(Ber(theta) || Ber(y)) + eta ln(1/y)
      >= eta ln(1/y).

On the other hand, the strictly below characteristic-entropy/Elias condition at radius delta=1-rho-eta is

    H_p(delta) < 1-rho,

which is equivalent to

    h(y) < eta ln(p-1) + (1-rho) ln(p/(p-1)).

These inequalities are incompatible whenever

    eta ln(1/y) >= (1-rho) ln(p/(p-1)).

In particular, for fixed rho in (0,1), eta -> 0, n=o(p), and r>=1, the left side is Omega(1/n), while the right side is O(1/p); the incompatibility holds eventually.

This says that a full product-image construction with exactly this dimension/padding accounting cannot simultaneously put the exceptional point at covering radius and keep the other points strictly below the characteristic-entropy threshold. It does not exclude a construction that only realizes a diagonal of the product image, or different dimension/padding accounting. Apply to the manuscript only after checking those identities in its actual notation.
