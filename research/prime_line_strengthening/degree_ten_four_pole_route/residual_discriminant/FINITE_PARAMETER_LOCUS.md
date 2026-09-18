# The global necessary parameter locus is finite

This proves finiteness, not emptiness or the existence of a rational member.
All arithmetic statements first refer to the archived Paley net modulo29.

## Closed scheme and the tested line

Homogenize each coefficient of the reconstructed residual discriminant to
parameter degree18. This gives a binary form D(X,V) of degree48 over the
parameter plane P²_(a,b,c). Let Z be the closed determinantal subscheme
where the two degree47 forms D_X,D_V have a common factor of degree at
least15. One defining presentation is rank at most79 of their94-square
Sylvester matrix. It includes D=0 and all leading-degree drops; it does not
discard reducible curves. Since48 is a unit in characteristic29, this is
the binary gcd condition used by the audited global discriminant lemma.

On the parameter line L: c=a, the affine chart a=1 is [1:u:1]. The saved
subresultant computation finds that the gcd of the low principal
subresultants is precisely the degree16 leading coefficient, up to a unit.
It factors into degrees1,1,2,4,8. Every possible affine point of Z on this
line is therefore among those leading-degree drops. Exact computations
over the corresponding residue fields give binary gcd degrees0,2,0,0,0,
respectively. No affine point qualifies.

The missing projective endpoint is [0:1:0]. Independent evaluation directly
from raw reconstruction exponents gives residual degree45, finite gcd2,
and infinity contribution2, for total4. Thus this endpoint does not
qualify either. `endpoint_independent.json` records the polynomial itself.
The initial line receipt incorrectly reported a zero endpoint because of
a Sage ETuple-versus-tuple dictionary lookup; this was corrected in the
script, independently replayed with FLINT, and the authoritative whole-line
receipt has been regenerated. That erroneous zero report must not be used.

Consequently the geometric support of Z misses the entire projective line
L over the algebraic closure of F29. Every positive-dimensional closed
subset of P² intersects every line. Therefore Z is zero-dimensional or
empty. This assertion includes possible zero-discriminant parameters.

## Smaller exact matrix and a scheme-degree bound

There is a smaller presentation useful for elimination. For homogeneous
forms f=D_X,g=D_V of degree47 consider

    M: Sym^32(k²) ⊕ Sym^32(k²) -> Sym^79(k²),
       (A,B) -> A f+B g.

Its matrix has80 rows and66 columns, with entries homogeneous of parameter
degree18. If f,g are nonzero with gcd degree d, their primitive syzygy has
degree47-d. Hence M has a nonzero kernel exactly when d>=15. The same
rank-drop condition correctly includes a zero form or both zero forms.
Thus Z can equivalently be defined, at the level of support, by the
66-square maximal minors. Use this determinantal scheme for the following
scheme-length bound; it need not have the identical nonreduced structure
as the94-square presentation.

Each minor has degree1188. Because their common projective zero set is
finite, two general linear combinations have no common curve over the
algebraic closure. Their complete intersection has length1188²=1,411,344
and contains this determinantal scheme. Its length, and therefore its
number of geometric parameter points, is at most1,411,344. This is a coarse
rigorous bound, not an estimate of the actual size.

## Characteristic-zero transfer

Use the exact integral kernel model over the localization of the base
number field at the chosen prime above29. The unit217-minor gives a free
rank3 kernel with the specified reduction. Discriminants and the fixed
locator division define the degree18 coefficient forms over this DVR;
the audited integral construction supplies their characteristic-zero
interpretation. Form the same projective determinantal locus and line
c=a over the DVR.

Their intersection is proper over the DVR. If it had a geometric generic
point, properness would give a special point after a finite extension of
the DVR, contradicting the empty geometric special intersection. Thus
the characteristic-zero necessary locus also misses this line and is
zero-dimensional or empty. The same coarse degree bound applies. This
does not infer that a modular point lifts, and does not remove parameters
whose reduction happens to lie on a reducible-graph line.

## Concrete next elimination chart

Since Z misses c=a, the single affine chart c-a=1 contains all its points.
Substitute [a:b:c]=[u:v:u+1] into the homogeneous coefficient forms and
build the80-by66 structured syzygy matrix above. This is preferable to
forming the huge discriminant of D or a blind full ideal of94-square
minors.

A bounded first algebraic pilot is one65-by65 pivot chart. Choose a pivot
nonzero at an explicitly checked ordinary parameter. Fraction-free
elimination produces the15 bordered66-square minors from the remaining
rows and one remaining column. Where the pivot is nonzero, these15
equations are exactly the rank-drop condition. Record degrees, term
counts and elapsed time before attempting a Groebner basis. If manageable,
compute their zero-dimensional ideal saturated by the pivot and test all
resulting parameter points against the original binary gcd and norm
curve. The pivot-zero locus MUST be retained for a separate chart or
lower-rank stratum; no absence claim may follow from this one chart alone.

This is an actual finite algebraic parameter target. Repeating independent
projective-line tests is unnecessary for proving finiteness and does not
recover isolated points outside those lines.
