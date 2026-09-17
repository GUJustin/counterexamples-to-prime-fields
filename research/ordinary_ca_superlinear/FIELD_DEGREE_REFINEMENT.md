# Quadratic extension-degree bound for exact-gap normalization

September 17. Proved and independently checked by complete finite support
censuses. The exact-rate/exact-gap construction can use F_(p^e) with
e<=4n^2. It is not asserted over fixed-degree extensions or prime fields.
No novelty claim. The earlier cubic-degree proposal is superseded by the
translated-root argument below, which needs no roots-of-unity extension.

## Block of new received values

For a source over F with M>=K, choose u distinct new coordinates in F.
In an extension of degree u+1 choose received values b_1,...,b_u such
that 1,b_1,...,b_u are F-linearly independent. Any degree-<K candidate
with a new agreement has at most K total agreements: otherwise select
K+1 agreements including a new one. The unique Vandermonde row dependence
has all coefficients nonzero and in F, contradicting independence of the
new b_i together with 1. Thus the true maximum stays M, and every selected
old nearest candidate retains M agreements. Additional nearest candidates
are possible when M=K; completeness of the selected list is not claimed.

## Block of common zeros without adjoining roots of unity

Let 1<=s<=M-K+1 and choose s distinct c_i in F. Take theta of degree
D=K+2s over F, append coordinates theta+c_i with received value 0, and
multiply all old received values and selected polynomials by

    Z(X,theta)=product_i (X-theta-c_i).

Increase dimension to K+s. The maximum is exactly M+s.

For the upper bound suppose Q of degree<K+s has at least M+s+1
agreements. At least M+1>=K+s of these are old. Interpolation at K+s
old base-field coordinates lifts Q to Qtilde(X,Y) over F, of X-degree
<K+s and Y-degree<=s, whose specialization at Y=theta is Q.
At every old agreement x we have the polynomial identity

    Qtilde(x,Y)=Z(x,Y)w(x),

because both sides have degree<=s<D in Y and agree at theta.
If theta+c_i is a new match, Qtilde(Y+c_i,Y) is a polynomial of degree
<K+2s=D vanishing at theta, hence is identically zero. Thus X-Y-c_i
divides Qtilde in F[X,Y]. The distinct matching linear factors are
pairwise coprime; divide all j of them out of both Qtilde and Z.
The resulting Q0 and Z0 have X-degrees <K+h and h, and Y-degrees <=h
and h, respectively, where h=s-j.

Put B(X)=(-1)^h [Y^h]Q0(X,Y). On all old matches, B(x)=w(x).
Every Y-coefficient of Q0-Z0*B has X-degree<K+2h and vanishes at at
least M+h+1>=K+2h old points. Therefore Q0=Z0*B identically. Its
X-degree forces deg B<K, contradicting the original maximum M.
This includes the case j=0 and the case h=0. Selected nearest witnesses
attain M+s by multiplication with Z, proving equality.

## Application and extension-degree accounting

Start over F_(p^2), so all u=13Delta-3r new-value coordinates fit. Perform
the new-value block, costing degree u+1. Next perform TWO ordinary
single-common-zero operations, costing degree 4. The remaining number of
common zeros is s'=2Delta-r-1, between1 andDelta because
Delta=m-r+1 lies in[r/2+1,r+1]. At this stage K=r+2, M=m+2 and
M-K+1=Delta, so the translated-root block applies with degree
D=r+2+2s'<=3r+4.

The final code parameters and quadratic label count are unchanged. Its
extension degree over F_p is at most

    e=8(u+1)D <=8(10r+14)(3r+4)<4(8r+16)^2<=4n^2,

where n=16Delta>=8r+16. The final field has cardinality at least p^4,
which exceeds 2N'r, so the label compiler needs no further extension.

## Independent finite checks

verify_block_padding.py implements extension-field arithmetic using
coefficient tuples, checks every node-difference inverse, and exhausts
all determining supports. Irreducible moduli are checked separately by
SymPy. A three-value block over F_(7^4) preserves maximum2. Translated
common-zero blocks of size2 over F_(7^6) raise maxima3 and4 to5 and6;
all70 determining four-subsets are checked in each fixture. The earlier
root-of-unity variant is also replayed. All 7,383 field-degree and exact
normalization parameter checks pass. These are complete finite checks,
not a replacement for the algebraic proof above.
