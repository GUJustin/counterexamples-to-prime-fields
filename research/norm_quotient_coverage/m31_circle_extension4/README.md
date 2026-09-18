# M31, degree-four challenges: selected circle fibers

2026-09-18. **Proved finite existence certificate**, subject to the stated
ordinary Reed--Solomon code and selected-domain contract. The exact
arithmetic is checked by `verify.py` and recorded in `receipt.json`.
The tag set is proved to exist; it is not enumerated by this certificate.

Let `p=2^31-1`, `K=F_(p^2)`, `E=F_(p^4)`, and
`T={a in K*:a^(p+1)=1}`. There exist a 262144-point domain `D` contained
in `T` and words `f,g:D->E` for the ordinary RS code of degree below
131072 such that

* both individual agreements and common agreement are exactly **132095**;
* every one of the **p^4-1 nonzero** pencil labels has exact agreement
  **133119**;
* the source-to-near agreement gap is **1024**.

The domain is a selected union of 256 complete fibers of `X -> X^1024`
on `T`. This does not assert the theorem on an arbitrary prescribed circle
domain or the usual fixed NTT domain. It also does not identify this code
with a particular Circle-STARK implementation, its base-field coefficient
restriction, or its basis. The result is for ordinary univariate RS over
`E` evaluated at the indicated elements of `K`.

## Uniform circle character lemma

For any odd prime `p`, choose `i in K` with `i^p=-i`, `i!=0`, and let
`b in E\K`. For every nontrivial multiplicative character `chi` of `E*`
and every character `psi` of `T`,

\[
 \left|\sum_{a\in T}\chi(b-a)\psi(a)\right|\le4\sqrt p. \tag{1}
\]

For M31 one can take `i^2=-1`. The parametrization

\[
 a(t)=\frac{t-i}{t+i},\qquad t\in\mathbb P^1(\mathbb F_p),
 \qquad a(\infty)=1
\]

is a bijection onto `T`. Extend `psi` to any character `eta` of `K*`;
this is possible because `K*` is cyclic. Put

\[
 \rho=\chi|_{K^*},\qquad
 z=-i\frac{b+1}{b-1},\qquad
 \kappa=\eta^{p-1}\rho^{-1}.
\]

The fractional transformation and its inverse are defined over `K`.
Consequently `z` is outside `K` and has degree four over `Fp`. Its four
conjugates are distinct and disjoint from the two conjugates `i,-i`.
For `t in Fp`, `(t+i)^p=t-i`, so

\[
 \chi(b-a(t))\psi(a(t))
 =\chi(b-1)\chi(t-z)\kappa(t+i).
\]

Thus the sum in (1) is exactly

\[
 \chi(b-1)\left(1+
     \sum_{t\in\mathbb F_p}\chi(t-z)\kappa(t+i)\right). \tag{2}
\]

The product character on the etale algebra `E x K` restricts trivially
to the diagonal `Fp*`: on that group, `eta^(p-1)=1` and `rho=chi`.
This holds for every extension `eta`; it does **not** require
`eta|Fp*=1`. Changing `eta` by a character trivial on `T` does not change
`eta^(p-1)`.

Use the rank-one Lang sheaf in
[Katz, *An Estimate for Character Sums*, Theorem 2 and its proof,
pp.198--199](https://web.math.princeton.edu/~nmk/old/estcharsums.pdf)
for `E x K` and the regular element `(z,-i)`. It is tame, with the four
`z`-conjugates and at most the two `i`-conjugates as finite punctures.
The trivial diagonal restriction makes infinity removable, with trace
one. Thus the parenthesized expression (2) is the full projective trace
sum. Nontriviality of `chi` gives nontrivial local monodromy at the
`z`-conjugates, so `H_c^0` and `H_c^2` vanish. Tame Euler characteristic
gives `dim H_c^1<=6-2=4`, and weights at most one prove (1).
This is the boundary refinement of Katz's proof, not a claim that his
displayed affine estimate already has constant four.

In particular, no restriction is placed on `chi|K*` or `chi|Fp*`.
If `kappa` is trivial, its two punctures disappear and the same proof
even gives `2 sqrt(p)`; this improvement is not needed.

## From the circle to fixed-cardinality product coverage

Set `m=1024` and `H=T^m`, of size `(p+1)/m=2^21`. Averaging (1) over
the `m` characters of `T/H` gives

\[
 \left|\sum_{a\in H}\chi(b-a)\right|\le4\sqrt p.
\]

Reserve the tag `a0=1` and use the distinct population

\[
 \mathcal A=\{b-a:a\in H\setminus\{1\}\}\subset E^*,
 \qquad P=2^{21}-1.
\]

Its normalized nontrivial character bias is at most
`(4 sqrt(p)+1)/P < 185365/P`. The verifier establishes M31 primality by
29 Lucas--Lehmer iterations and checks `sqrt(p)<46341` by squaring.

Apply `../fixed_weight_completion.tex` with final tag count `s=255`,
product cardinality `r=129`, and six completion pairs. The seed has
`s0=243`, `r0=123`. The exact overlap sum, rather than its coarser
exponential upper bound, gives

\[
 h_0<2^{-88.3827},\qquad
 h_6<2^{-130.3574},\qquad (p^4-1)h_6<0.012196<1.
\]

The displayed decimal values are informational. The certificate uses
integer fractions throughout and rounds each hole bound upward to a
multiple of `2^-256`; the final decision is a strict integer inequality.
Hence some 255-element `G subset H\{1}` has all of `E*` represented by
products of exactly 129 distinct elements `b-a`, `a in G`.

## Exact ordinary-RS compiler

Let

\[
 D=\{x\in T:x^{1024}\in G\cup\{1\}\},\quad
 Y=X^{1024},\quad R(X)=\frac{X^{1024}-1}{X-1}.
\]

Then `|D|=256*1024=262144`, and `R` vanishes at the 1023 reserved-fiber
points other than `1`. The denominator `Y-b` never vanishes on `D`.
Define

\[
 f=R\frac{Y^{129}-b^{129}}{Y-b},\qquad
 g=-\frac{R}{Y-b}.
\]

For a 129-subset `S` of `G`, put `V_S(Y)=prod_(a in S)(Y-a)` and
`P_S(Y)=Y^129-V_S(Y)`. With label `lambda=-V_S(b)`, the witness

\[
 h_S=R\frac{P_S(Y)-P_S(b)}{Y-b}
\]

has degree at most `1023+127*1024=131071`, and its residual is
`R V_S(Y)/(Y-b)`. It agrees at `1023+129*1024=133119` domain points.
Product coverage supplies every nonzero `lambda in E`.

The same root count is an upper bound for every witness of degree below
131072: after clearing `Y-b`, the residual of `f+lambda g-h` has the
uncancelled monic leading term of `R Y^129`, of degree 133119.
Thus every nonzero pencil label has **exactly** this agreement.

For the source and common lower bounds, choose any 128-subset `A` of `G`
and use its monic locator `V_A`. Subtracting `R V_A(Y)` from `f` cancels
its leading term and gives a degree-at-most-131071 witness. A witness for
`g` on the same roots is

\[
 R\frac{V_A(Y)/V_A(b)-1}{Y-b}.
\]

Both match on the 128 complete fibers and the 1023 core points, totaling
132095. The polynomial `f` has degree exactly132095, so this is its
agreement upper bound. For `g`, clearing the denominator gives a nonzero
residual of degree at most132095; it cannot be identically zero because
`Y-b` does not divide `R`. Thus both individual agreements and common
agreement equal132095.

This finishes the finite existence proof. It is a new field/domain
specialization of the fixed-cardinality quotient compiler, with the
circle character estimate as its additional ingredient. It gives no
practical protocol-state or implementation-code claim.
