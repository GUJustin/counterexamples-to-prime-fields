# Higher power fibers in the quadratic extension: a weighted center test

2026-09-18. Bounded algebraic assessment; no scan or manuscript edit.

**Outcome.** The fixed-angle center identity survives every exponent
`h | p²−1`, including arbitrary partial fibers. Higher multiplicity does
not multiply the native labels. An exact weighted incidence bound gives

\[
 B_{\rm can}\le \varepsilon^{-3}p\sqrt{n/h}
\]

when the agreement gain over ordinary common agreement is at least
`epsilon*sqrt(h*n)` and `h >= 4/epsilon²`. In particular `hn = Omega(p²)`
allows only `O(n)` qualifying labels from the canonical degree-`h` bank.
The concrete maximal-multiplicity choice `h=p−1` therefore does not give
the desired superlinear population, even with arbitrary partial fibers.
Smaller `h` leaves the sparse rich-center construction unresolved. General
degree-`h` witnesses need a separate analysis: the quartic-extension
branch-separation proof does not transfer to this alphabet.

## 1. Exact model and the surviving identity

Let `E=F_(p²)`, let `h | p²−1`, and assume `k=h+1 <= n`. Choose disjoint
physical coordinate sets `D0,D1` in `E`, with total size `n`, and a
nontrivial norm-one coefficient `c`. Set

\[
 f|_{D_0}=X^{hp},\qquad f|_{D_1}=cX^{hp},\qquad
 g=1_{D_1},\qquad w_\lambda=f+\lambda g.
\]

All codes in this note contain **every** polynomial of degree at most
`h`. Define the actual power-image multiplicities

\[
 w_i(y)=\#\{x\in D_i:x^h=y\},\qquad n_i=\sum_yw_i(y).
\]

They satisfy `w0(y)+w1(y) <= h` for nonzero `y`, and at most one for
`y=0`. In particular `0 <= wi <= h` and `n0+n1=n <= p²`.

Choose `eta` with `c=eta^(1−p)`; then `eta` is not in `F_p`. Exactly as
in `FP2_PARTITIONED_TWO_BLOCK_REDUCTION.md`, the polynomials canonical
on both unpunctured Frobenius blocks are

\[
 Q_{a,z}(X)=a(X^h-z)+z^p,\qquad
 a^{p+1}=1,\qquad \lambda=(1-c)z^p.
\tag{1}
\]

This follows by writing `y=x^h`; the constant equations are unchanged.
If `a=u^(p−1)`, the two supports are the power preimages of

\[
 z+u\mathbb F_p,\qquad z+\eta u\mathbb F_p,
\tag{2}
\]

with weighted agreement

\[
 w_0(z+u\mathbb F_p)+w_1(z+\eta u\mathbb F_p).
\tag{3}
\]

The two directions are distinct. The map `z -> lambda` is a bijection
of `E`, so there are at most `p²` native labels, independently of `h`.
For each fixed center, every coordinate outside `x^h=z` belongs to
exactly one of the `p+1` supports in (1), while a coordinate with
`x^h=z` belongs to all of them. Thus the exact incidence identity is

\[
 \sum_{a^{p+1}=1}\operatorname{agr}(w_{(1-c)z^p},Q_{a,z})
 =n+p e_z,\qquad e_z=w_0(z)+w_1(z)\le h.
\tag{4}
\]

There is no independent label-plane separation: all these planes are
the same two-dimensional field `E`.

## 2. Farness and what the canonical restriction actually covers

Let `Ui` be the maximum agreement with the restriction of `f` to `Di`,
maximized over all degree-`h` polynomials, and put `U=max(U0,U1)`.
Adding a constant to a block does not change this maximum. The usual
indicator argument gives the exact bounds

\[
 U\le A_{\rm common}(f,g)\le\max(U,2h).
\tag{5}
\]

A nonconstant polynomial explaining `g` has at most `h` zero-values
and `h` one-values; a constant explanation restricts to one block.
Thus common agreement is exactly `U` if `U>=2h`. Every line word has
individual agreement at least `U`.

There is also a useful complete statement **within** the bank
`aX^h+b`. At a threshold above the agreement of a far line parameter,
every qualifying polynomial of this form must occur in (1).

Indeed, when `Norm(a) != 1`, each block equation in `y` has at most one
solution, because both `y^p−ay` and `y^p−(a/c)y` are invertible. If
these two image values `y0,y1` are different, at every other label
`mu` an affine polynomial in `y` interpolates the two values
`y0^p` and `c*y1^p+mu`. Its composition with `X^h` matches all the
same physical coordinates. Hence this witness cannot improve on any
far endpoint. If the two image values coincide, the total agreement
is at most `h`, whereas every received word has agreement at least
`k=h+1` by interpolation. When `Norm(a)=1`, compatibility on only one
block gives agreement at most `U`; compatibility on both is precisely
(1). This argument includes partial fibers and fibers split between
the two blocks. It is not a classification of arbitrary degree-`h`
polynomials.

The same exclusion holds at a threshold above ordinary common agreement.
For two distinct image values, interpolate both the raw source values
and the indicator values by affine functions of y, then compose with
X^h. These two codewords simultaneously explain all the same physical
coordinates. For coincident image values the support has size at most h,
whereas common agreement is at least k by simultaneous interpolation on
any k coordinates. A one-block compatible witness is bounded by U, which
is also at most common agreement by (5). Thus (1) includes every qualifying
canonical witness in either of these source-separation settings.

## 3. Exact weighted rich-center bound

Let `T` be a tested threshold and choose any positive `Delta <= T−U`.
For example, one may take `Delta=T−A_common` when this is positive.
Any qualifying support (3) must use a line of weight at least `Delta`
on **each** block, since either individual block contributes at most
`U`. For an affine line `ell`, write `ri(ell)=sum_(y in ell) wi(y)`.
The exact weighted affine-plane second moment is

\[
 V_i:=\sum_{\ell}\left(r_i(\ell)-\frac{n_i}{p}\right)^2
 =p\sum_yw_i(y)^2-\frac{n_i^2}{p}
 \le phn_i-\frac{n_i^2}{p}.
\tag{6}
\]

To check (6), each point lies on `p+1` lines and each pair of distinct
points lies on one; hence `sum_ell ri(ell)² = p sum_y wi(y)²+ni²`.
If `Delta>ni/p`, the number `Li` of lines of weight at least `Delta`
is at most `Vi/(Delta−ni/p)²`. In any one direction there are at most
`ni/Delta` such lines, because parallel lines partition the plane.

Each pair of rich lines whose directions have ratio `eta` determines
one center. Different pairs can give the same center, which only
reduces the label count. Therefore the exact finite bound is

\[
 B_{\rm can}\le\min\left\{p^2,
 \frac{n_1V_0}{\Delta(\Delta-n_0/p)^2},
 \frac{n_0V_1}{\Delta(\Delta-n_1/p)^2}\right\},
 \qquad \Delta>\max_i(n_i/p).
\tag{7}
\]

Suppose now `Delta >= epsilon*sqrt(h*n)` and `h >= 4/epsilon²`.
Since `n<=p²`, one has `ni/p <= n/p <= sqrt(n) <= Delta/2`.
Using (6), (7), and `n0*n1<=n²/4` gives

\[
 B_{\rm can}\le \frac{4phn_0n_1}{\Delta^3}
 \le\frac{phn^2}{\Delta^3}
 \le\varepsilon^{-3}p\sqrt{n/h}.
\tag{8}
\]

Thus `B_can/n -> infinity` requires `h*n=o(p²)` along any sequence
with fixed `epsilon`. This is an upper bound for this canonical bank,
not an existence result below that scale and not a universal bound on
all code witnesses.

For complete power fibers, write `Di=(X^h)^(-1)(Si)` for disjoint
`Si` in the power image, and `v=|S0|+|S1|`. Then

\[
 n=hv,\qquad k=h+1,\qquad
 \sqrt{(k-1)n}=h\sqrt v.
\tag{9}
\]

All line weights and agreements multiply by `h`, but the centers do
not. A square-root-scale gain forces `Omega(sqrt(v))` distinct image
points on each rich line, exactly the previous sparse-incidence
requirement. At low rate the leading first-order agreement, divided
by `h`, is `sqrt((1+1/h)*v/2)`; increasing `h` changes this constant
but not the required richness order. The length-normalized label
bound becomes `O(p/(h*sqrt(v)))`. The rate is approximately `1/v`,
so complete-fiber multiplicity alone raises dimension and length
together rather than raising the rate of a fixed image construction.

## 4. One concrete high-multiplicity test: the norm-one circle

Take `h=p−1`, still below the characteristic, and use nonzero physical
coordinates for this candidate. The power image is exactly

\[
 G=\{y\in E^*:y^{p+1}=1\},\qquad |G|=p+1.
\]

For every affine witness `a y+b`, matching the first block is
`a y²+b y−1=0`, because `y^p=1/y` on `G`; the second block has the
analogous quadratic equation. Thus every polynomial `aX^h+b` has
at most `2h` matches per block and `4h` in total, for arbitrary
partial fibers. If a first-order/Johnson-scale target satisfies
`T >= c0*sqrt(h*n)` for a fixed positive `c0`, any canonical match
requires

\[
 n\le16h/c_0^2.
\]

Together with `n>=k=h+1`, this gives `n=Theta(h)=Theta(p)`.
For a fixed positive square-root-scale proximity gain, (8) then gives
only `B_can=O(p)=O(n)`. The complete-fiber version has only boundedly
many selected image values; arbitrary partial fibers do not evade
the weighted bound. This candidate can have bounded positive rate,
but cannot produce the requested superlinear canonical label count
with that gain and far endpoints. This is different from the older
dense-conic-union test: multiplicities now grow with the code
dimension, and the bound permits any partial or split fibers.

The only remaining possibility inside this literal mechanism has
`hn=o(p²)` and requires a new sparse weighted rich-center construction.
It also requires bounds for **all** new degree-`h` witnesses. The
quartic proof's separating map had kernel `F_(p²)` in `F_(p⁴)`; it
has no nonzero counterpart when the alphabet itself is `F_(p²)`.
This note supplies neither missing step and claims no obstruction
to other received-word identities over a quadratic extension.
