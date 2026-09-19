# Common anchors for a complete subgroup coset of the nearest orbit

September 19, 2026. Exact elementary obstruction to one shortening
mechanism. It does NOT exclude arbitrary non-subgroup retained subsets
of the nearest orbit. No search, positive construction, or manuscript
edit was performed.

The current shortening target is to retain a growing, ideally linear,
subbank of the true-nearest orbit while imposing about `4r/5` common
agreement anchors. This note rules out retaining a complete subgroup
coset of linear size along the actual prime-selection sequence. It
also gives the exact residue decomposition for subgroup-stable anchors.

## 1. General orbit lemma

Let a field contain `4r` distinct roots of unity. On `D=mu_(4r)` let

    W_r(X)=(1+X^(2r))/2-X^r.

Let `deg V<r`, and assume its orbit `{V(zeta X):zeta in mu_r}` has
exactly `r` distinct polynomials. Let `S<=mu_r` have order `h>1`, and
retain every rotation in one coset `aS`, with `a in mu_r`.

Then the number of coordinates at which ALL retained polynomials
agree with `W_r` is at most

    r-h.                                                   (1)

This bound does not require nearestness or any information about the
other agreement coordinates.

Proof. Replace `V` by `U(X)=V(aX)`. The maximal common agreement set is

    C={x in D: U(sx)=W_r(x) for every s in S}.

Since `W_r(tx)=W_r(x)` for `t in S`, multiplication by `S` preserves
`C`. Its orbits on `D` all have size `h`, so `|C|` is a multiple of `h`.
For any `s in S` other than one, `U(sX)-U(X)` is nonzero: otherwise
the original full orbit would have a nontrivial stabilizer. This
difference has degree at most `r-1` and vanishes on `C`. Hence
`|C|<=r-1`. The largest multiple of `h` below `r` is `r-h`, proving (1).

Any prescribed common anchor set is a subset of `C`, so the same bound
applies whether or not that prescribed set was initially `S`-stable.
It also applies if a larger retained family merely CONTAINS the
complete coset `aS`.

## 2. Exact residue decomposition

Write `q=r/h` and decompose

    U(X)=sum_(j=0)^(h-1) X^j U_j(X^h), deg U_j<q.

Let `A` be an `S`-stable common anchor set, let
`B={x^h:x in A} subset mu_(4q)`, and put

    ell=|B|=|A|/h, Lambda_B(Y)=product_(b in B)(Y-b).

For any fixed `y in B`, evaluating on its full `h`-point fiber gives
`U(sx)=W_r(x)` for every `s in S`. Independence of the `h` characters
of `S` yields

    U_0(y)=W_q(y),
    U_j(y)=0 for every 1<=j<h.

Consequently

    Lambda_B divides U_j for all 1<=j<h.                   (2)

At least one such `U_j` is nonzero, since otherwise `U` would be
`S`-invariant. Since `deg U_j<q`, (2) forces `ell<=q-1`, recovering
`|A|<=r-h`. When equality holds, every nonzero component has the form
`U_j=c_j Lambda_B`, while `U_0` interpolates the `q-1` required word
values. Thus this argument does not secretly prohibit the lower-index
normal forms that remain algebraically possible.

For example, the hypothetical choice `h=r/5` and four complete anchor
fibers is not excluded by (1): it gives exactly `4r/5` anchors and the
displayed extremal residue form. Existence of a true-nearest polynomial
with the required additional matches would still need a separate proof.

## 3. Consequence for the actual rough-r sequence

The source construction in `appendix.tex` chooses primes with

    p=9 mod 16, p=-1 mod B_R,

where `B_R` is the product of odd primes at most `R`, and takes a
descended orbit length `r>R` dividing `(p-1)/4`. Hence

    v_2(r)<=1,
    every odd prime factor of r exceeds R.

Fix `c>0`. If `h>=c r`, then the index `q=r/h` is at most `1/c`.
For `R>1/c`, it cannot have any odd prime factor, and its 2-adic
valuation is at most one. Therefore `q` is either one or two.

For `q=1`, (1) gives no common anchors. For `q=2`, it gives at most
`r/2` common anchors. Thus along this sequence a retained complete
subgroup coset of any fixed positive relative size cannot supply the
approximately `4r/5` anchors needed by the proposed shortening.

In particular the tempting index-five residue construction is not
available in this prime-selection sequence once `R>=5`.

## 4. Precise remaining gap

An arbitrary set of `Theta(r)` rotations need not contain a complete
coset of a subgroup of order `Theta(r)`. Merely having many pairwise
ratios in `S`, or generating `S`, does not make its common agreement
set `S`-invariant. Neither the closure argument nor (2) has been proved
for such an arbitrary retained set.

This note therefore does not close the unknown-nearest-orbit shortening
target. It imports no Fourier estimate for the explicit Dickson bank,
and does not identify the unknown nearest polynomial with that bank.
