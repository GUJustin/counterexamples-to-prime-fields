# Sextic trace heads do not identify the original RS planes by polynomial weights

2026-09-19. A symbolic test of one proposed use of the sextic trace identity.
No field scan, new label bank, or general elliptic obstruction is claimed.

**Result.** The correction in the sextic chord identity lies in the quotient
coordinate space spanned by `Y_H, 1`. Even allowing a different polynomial
weight for every subgroup, these two heads cannot give the same original
Reed–Solomon syndrome plane across two different subgroups in the degree
range capable of reaching the current target. This remains true if the paired
image-chord slope and intercept conditions are satisfied. Rational weights,
parameter-dependent correction functions, and polynomial representatives of
degree at least the domain length are outside this statement.

## 1. Setup and the precise proposed pullback

Let `ell >= 23` be an odd prime and let the elliptic curve

    E: y^2 = F(X) = X^3 + A X + B

over the prime field `Fp` have all of `E[ell]` rational, with `p != ell`.
Write

    D = x(E[ell] \ {O}),
    n = (ell^2 - 1)/2,
    k = n - 4ell + 1,
    T_d = n - 2ell - d,       d in {5,6}.

The code is ordinary RS on `D`, with strict degree bound `< k`. Its
coefficient field may be any extension of `Fp`. Since `D` has `n` distinct
prime-field coordinates, `p >= n > 4ell - 1` for these values of `ell`.
In particular all the small integer divisors below are nonzero.

For an order-`ell` subgroup `H`, use the normalized Vélu x-map

    Y_H = N_H / B_H = N_H / K_H^2,
    deg N_H = ell,  deg B_H = ell - 1,
    Y_H = X + O(X^-1).

Both numerator and denominator are monic and coprime. The lack of a constant
term is part of the normalized Vélu map, not a further change of the RS
coordinate. Its target equation is

    Z^2 = Y^3 + A_H Y + B_H^curve.

The preceding [sextic chord calculation](SEXTIC_CHORD_TRACE_SLOPE_IDENTITY.md)
gives an exact trace correction in `span{Y_H,1}`. It also states the extra
slope and intercept equations needed for the normalized chord-product norm
to have its difference from the trace in this space. Grant all those
equations here: the remaining question is whether this quotient-coordinate
space can become one original RS source plane for different `H`.

We test the following precise way of doing that. Choose an arbitrary
nonzero polynomial `C_H` such that `C_H Y_H` is also a polynomial. This
allows independent weights for different subgroups. Coprimeness says
exactly that `B_H` divides `C_H`. Scale `C_H` to be monic and set

    G_H = C_H,              F_H = C_H Y_H,
    deg F_H = L_H,          deg G_H = L_H - 1.

All values, including the kernel coordinates, are the actual evaluations
of these polynomials. There is no independent assignment at a pole.
For a word `v`, write `[v]` for its class modulo `RS_k(D)`.

## 2. Two Laurent coefficients determine the normalized isogeny

**Lemma.** For distinct order-`ell` subgroups `H,H'`, the first two
coefficients in

    Y_H = X + u_H X^-1 + v_H X^-2 + O(X^-3)

cannot both agree with those of `Y_H'`.

**Proof.** Preservation of the invariant differential gives the rational
identity

    F(X) Y_H'(X)^2 = Y_H(X)^3 + A_H Y_H(X) + B_H^curve.       (1)

Here the prime on `Y_H` means differentiation, not another subgroup.
Comparing the coefficients of `X` and `1` in (1) yields

    5 u_H = A - A_H,          7 v_H = B - B_H^curve.         (2)

Thus equality of these two Laurent coefficients gives the same target
Weierstrass equation for both maps. Suppose nevertheless that the maps
differ, and let their first difference be

    delta = c X^-m + lower powers,       c != 0,  m >= 1.

Subtract (1) for the two maps. The leading terms at degree `2-m` are
`-2m c` on the left and `3c` on the right. Hence

    (2m + 3)c = 0.                                         (3)

The difference of the maps has denominator `B_H B_H'`, of degree
`2ell-2`, and a nonzero polynomial numerator. Therefore `m <= 2ell-2`.
It follows that `0 < 2m+3 <= 4ell-1 < p`, contradicting (3).
The maps must coincide. Their reduced monic denominators then coincide,
so their kernel x-sets, and hence their subgroups, coincide. This proves
the lemma. In particular the argument accounts explicitly for the possible
failure of differential uniqueness in small characteristic.

## 3. Polynomial regularization cannot produce a common source plane

**Proposition.** Suppose

    k + 4 <= L_H < n,       k + 4 <= L_H' < n.

For `H != H'`, the two syndrome planes

    span([F_H], [G_H])  and  span([F_H'], [G_H'])             (4)

are different, for every choice of the polynomial weights above. Each
plane has dimension two.

**Proof.** Each pair consists of monic polynomials of two different
degrees at least `k`, both below `n`, proving independence modulo the
code. Evaluation of polynomials of degree below `n` is injective on `D`.
Consequently equality modulo the code between their linear combinations
is an actual polynomial equality up to a polynomial of degree below `k`;
no multiple of the domain locator can be hidden in that equality.

Suppose the planes in (4) agree. Their maximum polynomial degree forces
`L_H=L_H'=L`. The unique lower-degree direction in either plane, together
with monicity, then gives

    G_H' = G_H + Q,
    F_H' = F_H + a G_H + P,         deg P, deg Q < k.         (5)

In the ratio `F_H'/G_H'`, the added `a G_H` contributes constant term `a`
at infinity. The terms involving `P,Q` contribute only negative powers
because `L >= k+4`. Both normalized maps have constant term zero, so
`a=0`. Equation (5) now gives

    Y_H' - Y_H = (P G_H - F_H Q) / (G_H (G_H+Q))
                = O(X^(k-L+1))
                = O(X^-3).                                (6)

The first two Laurent coefficients therefore agree. Section 2 forces
`H=H'`, which is the required contradiction.

Equality of planes already allows arbitrary invertible recombinations of
the two sources and independent codeword shifts. Thus those operations do
not evade the proposition within this model.

## 4. Target degree and kernel-value accounting

A genuine plane represented by polynomials of degree at most `L<n` cannot
contain a nonzero syndrome word with agreement greater than `L`: subtract
any codeword and apply the ordinary polynomial root bound. Thus a
polynomial-weighted two-head plane that supplies any witness at `T_d`
must have `L >= T_d`. Here

    T_d - k = 2ell - d - 1 >= 39,

so every such degree satisfies the hypothesis `L >= k+4`. The proposition
therefore excludes identifying these polynomial-weighted two-head planes
across different subgroups anywhere in the relevant degree range
`T_d <= L < n`.

Without a weight, a globally constant second head is already a codeword;
an extension of `Y_H` by specified values at the kernel does not by itself
turn `span{Y_H,1}` into a two-dimensional syndrome plane. If instead one
sets *both* heads to zero on the kernel, the second word is a kernel
indicator modulo the constant codeword. That is a different model with
additional subgroup-dependent coordinate corrections and is not covered
by treating `1` as the global constant.

Similarly, a single common polynomial weight clearing every subgroup's
poles must be divisible by `Phi_D^2`, since the kernel x-sets partition
`D`. The weight itself then evaluates to zero everywhere, while its
product with `Y_H` can only be supported on that subgroup's kernel. This
cannot supply two independent syndrome heads.

## 5. Scope and next constructive requirement

This closes the proposed direct use of the two sextic trace correction
heads with subgroup-dependent polynomial pole clearing and representatives
of degree below the domain length. It does not classify arbitrary sextic
omission locators, prove a general intersection bound for rational received
spaces, or rule out parameter-dependent residual cofactors.

A further use of the chord norm/trace identity would need an explicit
mechanism outside this proposition: for example, rational regularization
with fully specified kernel values, or additional head functions whose
relations survive reduction modulo the domain locator. The two quotient
heads alone and the paired slope/intercept equations do not provide that
mechanism. No additional finite computation is justified by this identity
at present.
