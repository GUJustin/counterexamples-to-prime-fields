# Balanced fibers on a root-of-unity domain

## Polynomial classification: correct, with a weaker characteristic hypothesis

Let `F` be any field whose characteristic does not divide `n`, let
`D=mu_n` be the full set of `n` distinct nth roots in a splitting field,
and let `R in F[X]` have exact degree `B>=1`. Suppose `R` takes `M`
distinct values on `D`, every one exactly `B` times. Then `n=BM` and

\[
R(X)=aX^B+b,\qquad a\ne0.
\]

The converse holds whenever `B|n`. Each fiber of `X^B` on `mu_n`
has precisely `B` elements. If the domain and its values are required
to lie in `F` itself, add `mu_n subset F`; the algebraic proof needs
only the splitting field. The resulting coefficients `a,b` are the
original leading and constant coefficients, hence lie in `F`.

### Product identity and the proposed derivative proof

Let `Y` be the set of image values and `P(T)=prod_{y in Y}(T-y)`.
Every degree-`B` factor `R(X)-y` has its full `B` roots on the domain.
The product has degree `BM=n`, leading coefficient `a^M`, and exactly
the `n` distinct roots in `D`. Thus

\[
P(R(X))=a^M(X^n-1).
\]

There is no cancellation of the highest degree: `P` is monic and
`a` is nonzero. Under the proposed assumption `char(F)=0` or
`char(F)>n`, differentiating yields

\[
P'(R(X))R'(X)=a^M nX^{n-1}.
\]

Therefore `R'` divides a monomial. Its degree is exactly `B-1`, so
`R'=BaX^(B-1)`. Since every integer from `1` through `B` is nonzero
in the field, integration leaves only `R=aX^B+b`. This proof is sound.

### Stronger coefficient proof, supplied by structured_domains and checked independently

The derivative proof unnecessarily assumes large characteristic. Put
`Q(X)=R(X)-R(0)` and shift the outer polynomial accordingly, preserving
its being monic of degree `M`. Suppose `Q` has a nonleading nonzero
term, and let `j` be its largest exponent below `B`. Then `1<=j<B`.
In the outer composition, the coefficient of degree `n-B+j` is

\[
M a^{M-1}[X^j]Q.
\]

Only the leading outer term `Q^M` can contribute: every smaller outer
power has degree at most `(M-1)B=n-B`. Within `Q^M`, taking exactly
one degree-`j` term yields the displayed coefficient; taking any smaller
term or at least two nonleading terms yields smaller degree. The
coefficient is nonzero because `char(F)` does not divide `M`, as
`M|n`. But `a^M(X^n-1)` has zero coefficient there. Contradiction.

This proves the classification under only `char(F) not dividing n`.
It also handles `M=1`: every degree between `1` and `n-1` must vanish.

### Endpoints and scope

- `B=1`: every nonconstant linear polynomial qualifies, as stated.
- `B=n`, `M=1`: the map is constant on the domain, and
  `R-y=a(X^n-1)`. The classification still holds.
- `n=B=1`: the statement remains true.
- Degree zero is excluded; the phrase “exactly B-to-one” would otherwise
  not specify a nonempty fiber size.
- The roots must be the **whole** `mu_n` and each fiber must have the
  **full algebraic degree B**. An arbitrary subset or partially filled
  fibers do not imply the product identity.
- If characteristic divides `n`, there are fewer than `n` distinct
  roots, so the stated domain hypothesis fails before the proof starts.
- For a coset `c mu_n`, replacing `X^n-1` by `X^n-c^n` gives the same
  classification `R=aX^B+b`.

## Rational maps: no comparable classification, even up to two Möbius changes

The polynomial result does **not** extend to all degree-`B` rational
maps. In fact, for any partition `mu_(2B)=A disjoint-union A'` with
both parts of size `B`, put

\[
U(X)=\prod_{a\in A}(X-a),\quad
V(X)=\prod_{a\in A'}(X-a),\quad
R(X)=\frac{U(X)}{U(X)+V(X)}.
\]

The numerator and denominator are coprime, the rational map has degree
`B`, and there are no poles on the domain: on `A`, the denominator
equals the nonzero value `V`; on `A'`, it equals the nonzero value `U`.
The two fibers are exactly `A` (value `0`) and `A'` (value `1`).
Thus arbitrary equal-size partitions already give fully balanced maps.

Here is a concrete example satisfying the original large-characteristic
assumption. Work over `F_13`, with

\[
D=\mu_6=\{1,3,4,9,10,12\},\quad
A=\{1,3,4\},\quad A'=\{9,10,12\}.
\]

Then

\[
U=X^3+5X^2+6X+1,\qquad
V=X^3-5X^2+6X-1,
\]

and

\[
R(X)=\frac{X^3+5X^2+6X+1}{2X^3-X}
\]

is balanced three-to-one on `D`, with finite image `{0,1}`. Its
derivative numerator is

\[
U'V-UV'=3X^4+2X^2+1
=3(X^2+X+3)(X^2-X+3)\quad\text{over }F_{13}.
\]

The two quadratics are distinct and each has discriminant `2`, which
is nonzero in `F_13`. They have no common root, and the derivative
numerator has no common factor with `2X^3-X`. Consequently the rational
map has four distinct finite critical points over the algebraic closure.
The power map `X^3` has just two critical points, `0` and infinity,
each of multiplicity two. Independent Möbius changes in source and
target preserve the number and multiplicities of critical points.
Therefore this example is not even of the form
`L_1 composed-with X^3 composed-with L_2`; in particular it is not
Möbius-conjugate to `X^3`.

This counterexample is a statement about finite-field rational maps and
balanced set partitions. It supplies no claim about protocol behavior.
