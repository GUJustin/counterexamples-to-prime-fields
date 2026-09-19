# Independent audit: affine coefficient-plane list bound

September 19, 2026. Result: **PASS**, within the stated asymptotic and
coefficient-plane scope. No computation, positive construction, or
manuscript edit was performed.

Audited source:
`PRIME_AFFINE_COEFFICIENT_PLANE_LIST_BOUND.md`

SHA-256:
`c9e91dff2aaf2472306a941921fdbbf793d440aafcc9fa25c2af2bb2fe1ffb0e`.

The audited version states the result over ANY field of characteristic
zero, or characteristic `p` with `n<=p`, not just over prime alphabets.

## Algebraic reduction

For the affine plane `H0+aH1+bH2`, linear independence of `H1,H2`
ensures that both the parameterization by `(a,b)` and the associated
lines `Z=aY+b` are injective. `H2` is nonzero and has at most two roots.
After removing these coordinates, the map

    x -> (H1(x)/H2(x), (w(x)-H0(x))/H2(x))

has fibers of size at most two: fixing its first coordinate gives the
nonzero polynomial `H1-yH2`, of degree at most two. This remains true
when `H1,H2` have a common factor; denominator roots were removed first.
Thus the stated richness loss `(delta sqrt(n)-2)/2`, and its eventual
lower bound `delta sqrt(n)/4`, are valid. No real-order or prime-field
property enters this reduction.

## Incidence theorem and range

The primary theorem was checked directly: Stevens--de Zeeuw,
*An Improved Point-Line Incidence Bound Over Arbitrary Fields*,
Theorem 3, page 2 of [arXiv v4](https://arxiv.org/pdf/1609.06284).
It applies over arbitrary fields, with the stated characteristic
restriction when characteristic is positive.

Padding to exactly `n` points is legitimate because `F` already contains
`n` distinct evaluation coordinates. If there are at least `n`
qualifying lines, selecting `n` of them gives the incompatible bounds
`Omega_delta(n^(3/2))` and `O(n^(22/15))` for large `n`.
The characteristic expression is `n^11`, while `n<=p` gives
`n^11/p^15<=p^(-4)`. Thus the onset can be chosen uniformly in the
field and prime. Characteristic zero needs no such check.

For `n^(7/8)<K<n`, all size hypotheses hold and rearrangement gives

    K^(4/15) <<_delta n^(7/30), hence K<<_delta n^(7/8).

The small-`K` case already has the desired bound. The large-`n`
qualification correctly prevents an unsupported one- or two-agreement
bound over arbitrarily large or infinite fields.

## Transfer claim and limits

The norm-one bank's linear list size and square-root agreement scale
contradict the bound if reproduced on a comparable-length domain in the
specified characteristic regime with the image bank still in an affine
coefficient plane. Retaining fixed positive fractions changes constants,
not the contradiction.

The degree-two Mobius/GRS action is an invertible linear map on
quadratic coefficients; a common polynomial translation is affine, and
nonzero scalar multiplication is invertible. These preserve affine
dimension. If the transformed coefficient vectors belong to `F_p`, the
rank of their difference matrix is unchanged by extending scalars.
Hence an extension-defined change of coordinates cannot conceal a
three-dimensional prime-field span inside an extension-field plane.

The proof also covers extension alphabets on short domains `n<=p`.
Increasing extension degree alone does not change the characteristic
condition. The original norm-one construction has length of order
`p^2`, so it is outside the audited regime.

No assertion about unrestricted three-dimensional quadratic lists,
received-line label counts, explicit finite constants, practical security
bits, or literature novelty follows. These limitations are correctly
stated in the source.
