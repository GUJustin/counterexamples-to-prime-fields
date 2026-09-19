# A fifth-root grid: short-domain witness control, but only linear labels

2026-09-18. One bounded geometry, with no scan or manuscript edit.

**Result.** The new odd-power classification does give useful control
after sparse puncturing: fifth roots of a rectangular prime-plane grid
have at most `5M+45` matches with every noncanonical degree-five
witness. This yields the explicit ledger

\[
 n=\frac{15}{2}M^2,\quad k=6,\quad T=6M,\quad
 5M\le A(r_i)\le5M+45,\quad
 5M\le A_{\rm common}\le5M+20,
\]

with `n/5` explicitly identified nonzero singleton labels and placement
above first order and below Johnson. Taking `M=o(p)` gives `n=o(p²)`.
However, the already proved sparse-grid incidence bound makes the
**entire** qualifying canonical bank `O(n)`. This is a short-domain
all-witness calculation, not the sought superlinear construction.

## Construction

Let `p>5` satisfy `p=2 or 3 mod5`, let `M` be even with `100<=M<p`,
and set `B=F_(p²)`, `E=F_(p⁴)`. Choose a primitive `xi in E*`, put
`eta=xi^5`, and choose `omega in B\F_p`. Use the tag sets

\[
 A=B_0=\{1,\ldots,M\},\qquad C=\{1,\ldots,M/2\},
\]
\[
 S_0=A+\omega B_0,\qquad S_1=A+\omega C.
\]

These exclude zero. Since `5 | p²+1`, every nonzero tag in `B` has
five fifth roots in `E`. Define the two disjoint physical blocks

\[
 D_0=\{x:x^5\in S_0\},\qquad
 D_1=\{x:x^5\in\eta S_1\}.
\]

They have sizes `5M²` and `5M²/2`, respectively. Set

\[
 f|_{D_0}=X^{5p},\qquad f|_{D_1}=\eta^{1-p}X^{5p},
 \qquad g=1_{D_1}.
\tag{1}
\]

The code contains all polynomials of degree at most five. Both blocks
are punctures of the audited full fifth-power construction; no neutral
coordinates are added.

## Why every new witness is controlled

The local Kummer classification in
`ODD_H_EXACT_SOURCE_AGREEMENT_AUDIT.md` implies the following for `h=5`.
For `P in B[Z]` of degree at most five, outside the family `aZ^5+b`,
more than 25 solutions to `z^(5p)=P(z)` force

\[
 P(Z)=(aZ+b)^5,\qquad ab\ne0.
\]

Fifth powering permutes `B`, so its solution set is then an ordinary
affine prime-field line `z^p=az+b`, if it has more than one point.
This is a line in the **physical branch coordinate**, not in the
power-image plane.

For a global polynomial `Q` with a nonzero coefficient of degree
`1,2,3,` or `4`, at most one of the ten physical `B`-branches is
coefficientwise `B` after normalization. Indeed, within a block the
chosen exponent is relatively prime to five, so its coefficient
membership allows at most one branch; the primitive-scale separation
excludes a good branch in both blocks. Each of the other nine branches
contributes at most five matches by projection.

On the one possible good branch, either there are at most 25 matches,
or its solutions lie on an affine line `z=v+ut`, `t in F_p`, `u!=0`.
The normalized tag on that branch is

\[
 y=\beta(v+ut)^5,\qquad \beta\in B^*.
\]

In the basis `1,omega`, its two coordinates are polynomials in `t`
of degree at most five. At least one is nonconstant: the vector leading
coefficient `beta*u^5` is nonzero. Membership in either rectangular
tag set forces that coordinate into a set of at most `M` values.
Each value has at most five preimages. Consequently at most `5M`
points of this exceptional line survive the puncture. It follows that

\[
 \operatorname{agr}(f+\lambda g,Q)\le5M+45
\tag{2}
\]

for every label and every noncanonical `Q`. The same argument on one
block alone gives `5M+20`. This proof uses the classification only for
the exceptional branch and works uniformly in the challenge.

For a canonical polynomial `aX^5+b`, an affine tag line meets `S0`
or `S1` in at most `M` points, hence contributes at most `5M` physical
matches per block. Every canonical polynomial not rich on both full
blocks has at most `5M` total matches; non-norm-one and external
leading coefficients give at most ten. The doubly canonical labels
are still exactly

\[
 \lambda=b-\eta v,\qquad
 a^{p+1}=1,\quad b,v\in I_a=\operatorname{Im}(y^p-ay).
\tag{3}
\]

The planes `I_a+eta I_a` intersect only at zero. Hence each nonzero
label has at most one doubly canonical polynomial, regardless of the
puncture. At `T=6M`, (2) excludes all other witnesses because `M>45`.
Every nonzero qualifying label therefore has a singleton code-wide
list; no uniqueness claim is made at label zero.

## Sources, common agreement, and explicit label population

Choose two distinct labels outside the full union of planes in (3)
and use the corresponding words as endpoints. Every canonical
witness there contributes at most `5M`; (2) therefore proves

\[
 5M\le A(r_i)\le5M+45.
\]

The lower bound comes from a complete horizontal core grid row.
The maximum block agreement `U` lies in `[5M,5M+20]`. A nonconstant
degree-five explanation of the indicator `g` uses at most ten common
coordinates, and a constant explanation can attain `U` on one block.
Thus ordinary common agreement is exactly `U`, giving the interval
stated above. Invertible reparameterization to the chosen endpoints
preserves these counts.

Horizontal tag fibers have `M` points in both blocks. There are `M`
core rows and `M/2` fresh rows, giving `M²/2` labels with `10M` matches.
Vertical fibers have `M` core points and `M/2` fresh points; their
`M²` pairs give labels with `15M/2` matches. All intercepts are nonzero
because `A`, `B0`, and `C` exclude zero. Thus all these labels are
nonzero, and the two slope planes make the two populations disjoint.
They give exactly

\[
 \frac32M^2=\frac n5
\]

explicitly identified singleton labels at threshold `6M`. Additional
qualifying labels are possible; this is a lower count, not an exact
full-list census.

The exact Johnson inequality is `T²=36M²<5n=(75/2)M²`.
At the very small rate `6/n`, the usual first-order upper bound gives

\[
 n a_1(6/n)
 \le\sqrt{3n}+(3n)^{1/4}
 <\frac{19}{4}M+\frac94\sqrt M
 <5M
\]

for `M>=100`. Hence the source, common-agreement, and threshold ledger
is genuinely above first order and below Johnson. Both the common and
individual loss fractions relative to the capacity margin tend to
`1/6`; the absolute fractional loss and the rate still vanish.

## Why this geometry stops short of the requested task

The new classification has removed the `p`-sized uncertainty from the
noncanonical source bound on this sparse domain. It has not changed
the tag-plane incidence problem. Any qualifying canonical pair at
`T=6M` must have at least `M/5` tag points on each of its two lines,
because the other line contributes at most `5M` physical coordinates.
For `M=o(p)`, the balanced-grid rich-line bound already established
in `PUNCTURING_ASSESSMENT.md` gives only `O(M)` such lines in each
rectangle, and each direction has at most `O(M)` of them. Thus their
paired-label count is `O(M²)=O(n)`. The `M` by `M/2` rectangle is still
balanced in the required sense.

Therefore this one concrete inverse-grid geometry has rigorous
all-witness control and a short-domain constant relative loss, but
cannot give `B/n -> infinity`. No further grid or Fermat scan is
justified. A genuinely different sparse tag geometry with many paired
rich lines remains necessary; the new Kummer classification can then
control its noncanonical witnesses if its fifth-root pullbacks have
small intersections with ordinary prime-field lines.
