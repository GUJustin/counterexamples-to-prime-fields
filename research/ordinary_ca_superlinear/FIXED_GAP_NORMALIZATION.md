# Exact fixed-gap ordinary-CA quadratic lower bound

September 17, 2026. Proof checked alongside independent exact finite computations.
The construction uses finite extensions of growing degree, NOT necessarily
quadratic extensions and NOT prime ambient fields. No novelty claim.

Starting from the descended source in PROOF.md, one can obtain exact
rate1/8, exact capacity gap1/16, and at least ceil(n^2/8192) nearby
labels with no ordinary correlated agreement at the tested threshold.
The characteristic exceeds the message degree. These are unbounded-length
families and are eventually strictly below characteristic-based Elias.

## Two boundary-preserving operations

Let a word w on N distinct points of a finite field F have true maximum
agreement M>=K with degree-<K polynomials. Keep any selected nearest list.
The same maximum holds over extensions: K matching base-field points and
values force base-field coefficients by interpolation.

(1) A coordinate with a new received value: choose a in F outside the
domain and b in a proper extension but outside F. Append coordinate a
with received value b. The maximum stays M. Indeed a polynomial with
M+1 total agreements would have to match at a and at M>=K old points.
The old matches force its coefficients into F, contradicting its value b
at a. Every selected old nearest polynomial retains exactly M agreements.
Length increases by1; dimension and maximum stay unchanged.

(2) A common zero: choose a outside F. Replace each old received value
w(x) by (x-a)w(x), append coordinate a with value0, and increase dimension
to K+1. Replace every selected polynomial P by (X-a)P. The new maximum
is exactly M+1.

For the upper bound, a degree-<=K polynomial with M+2 agreements either
matches at a, or does not. In the former case dividing by X-a gives a
forbidden degree-<K polynomial with M+1 old agreements. In the latter
case let S be M+2 old coordinates. Modulo the degree-<=K evaluation
space on S, the interpolation condition reads [xw]-a[w]=0. This is an
F-linear system. Since a is outside F, both classes must vanish: there
are A,B of degree<=K interpolating xw and w, respectively, on S.
Then A-XB vanishes on M+2>=K+2 points despite degree<=K+1, so it is zero.
Thus deg B<K, contradicting the original maximum M. This argument is
valid even when the putative polynomial coefficients lie in an extension.

Both operations can be iterated in finite fields. At each step a quadratic
extension of the current field supplies an element outside it. The second
operation requires a outside the ENTIRE current coefficient field; merely
choosing a fresh evaluation point inside it would not suffice.

## Exact parameters

The descended source has N=4r, K=r, nearest maximum m with
3r/2<=m<=2r, and r distinct nearest polynomials. Put

    Delta=m-r+1, u=13Delta-3r, s=2Delta-r+1.

Both u and s are nonnegative. First apply operation(1) u times, then
operation(2) s times. One may first extend to F_(p^2) so there are enough
distinct base-field coordinates for all u first-stage additions.
Every added received value is chosen outside the entire current field.
The resulting source has exactly

    N'=15Delta+1, K'=2Delta+1, M'=3Delta,

and retains r selected nearest polynomials. Its characteristic remains p.

Choose one agreement anchor incident to ell>=M'r/N'>=r/6 candidates.
Divide as usual. The old core has length15Delta, dimension2Delta, and
true maximum3Delta-1. Append q=Delta challenge coordinates. Their
root-count/translation compiler has J>=q*ell/4 after extending the field
if necessary so its cardinality Q>=2N'r. This further extension cannot
change the old maximum, by interpolation.

The final parameters are

    n=16Delta, K=2Delta, T=3Delta.

Thus rate1/8 and gap1/16 are BOTH exact. Every counted label is nearby.
For a zero explaining direction, common agreement is at most3Delta-1
on the old core. For a nonzero direction of degree<2Delta, it is at most
(2Delta-1)+q=3Delta-1. Ordinary CA at threshold T is absent.

Since Delta<=r+1 and Delta>=4, r>=3Delta/4. Therefore

    J>=Delta*r/24>=Delta^2/32=n^2/8192.

Also K-1=2Delta-1<=2r+1<p, since the descended source has p>=4r+1.
As r grows, so do Delta and p. The exact gap1/16 gives strict Elias for
all sufficiently large p by H_p(1-T/n)<=1-T/n+1/log_2(p).

## Field-size scope

The construction is not claimed over F_(p^2). A direct implementation of
the preservation lemmas uses a tower of quadratic extensions, one at each
padding step, and possibly one final enlargement. Its extension degree
can grow with n. The assertion concerns the full large-characteristic
field class, where the cited capacity bounds are uniform in field size.
The independent quadratic-extension result with gap merely bounded below
remains stronger in its field-degree restriction and is retained separately.


## Polynomial extension degree

The block operations in FIELD_DEGREE_REFINEMENT.md now replace the long
tower by a field F_(p^e) with e<=4n^2, without changing any code parameters
or the exceptional count. Main-paper Proposition N.4 contains the proof.
This still permits growing degree and does not assert a quadratic or prime
ambient field for the exact-gap construction.
