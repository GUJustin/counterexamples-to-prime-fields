# Pending refinement: polynomial extension degree for exact-gap normalization

September 17. Algebraic derivation recorded for independent checking.
NOT YET a manuscript claim. The currently proved normalization permits a
tower of quadratic extensions. The following block operations appear to
replace that tower by an extension of degree at most n^3 over F_p.

## Block of new received values

For a source over F with M>=K, choose u distinct new coordinates in F.
In an extension of degree u+1 choose received values b_1,...,b_u such
that 1,b_1,...,b_u are F-linearly independent. Any degree-<K candidate
with a new agreement has at most K total agreements: otherwise select
K+1 agreements including a new one. The Vandermonde row dependence has
all nonzero coefficients in F, contradicting linear independence of the
new b_i together with1. Thus the true maximum stays M, and every old
nearest candidate retains M agreements. This simultaneously performs all
u new-value additions, in extension degree u+1 instead of2^u.

## Block of common zeros

Let 1<=s<=M-K+1, with characteristic not dividing s. Enlarge F to contain
mu_s; this costs degree at most s. Choose T of degree D=K+2s over this
field, and put a=T^s. Then a is outside the base field. Append the s
coordinates zeta*T for zeta in mu_s, with received value0, and multiply
all old received values and selected polynomials by Z(X)=X^s-a. Increase
dimension to K+s. The maximum should be exactly M+s.

Proof of the upper bound. If Q of degree<K+s has M+s+1 agreements, it
has at least M+1>=K+s old ones. Interpolation at K+s old base-field
coordinates therefore writes Q=A-aB, with A,B over the base field and
degree<K+s. At ALL old matches, independence of1,a gives A(x)=x^s w(x)
and B(x)=w(x). Let H=A-X^s B, of degree<D.

If there is a new match, H(zeta*T)=0. That element has degree D over
the base field, forcing H=0. If there is no new match, H has at least
M+s+1>=K+2s=D old roots, again forcing H=0. It follows that deg B<K
and B agrees with w at at least M+1 old points, a contradiction.
All chosen new points are distinct and outside the old base field.

## Application to the exact-gap construction

Start over F_(p^2), so all u new-value coordinates fit. Perform the
block new-value operation with u=13Delta-3r. Next perform TWO ordinary
single-common-zero operations, costing degree4. The remaining number of
common zeros is s'=2Delta-r-1, between1 andDelta because
Delta=m-r+1 lies in[r/2+1,r+1]. At this stage K=r+2, M=m+2 and
M-K+1=Delta, so the block-zero lemma applies to s'.

The final parameters are unchanged. The extension degree over F_p is at
most

    8 (u+1) s' (r+2+2s')
      <=8(10r+14)(r+1)(3r+4)=O(r^3).

For r>=40 this is at most440r^3<n^3, since n=16Delta>=8r.
The resulting field already has cardinality >=2N'r, so the final label
compiler needs no further extension.

Next checks: independently implement degree-D finite fields and exhaust
all determining subsets for a nontrivial s=2 fixture. Recheck all block
interpolation arguments and field-degree inequalities before promoting.
