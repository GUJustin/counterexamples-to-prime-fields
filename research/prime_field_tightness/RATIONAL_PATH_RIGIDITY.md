# Many nearby labels force a bounded-degree rational path to be affine

September 17, 2026. New proof under local audit. No novelty claim.

## Theorem

Let F be any field, let D<A<=n be integers, and let f+Zg be a received
line on n distinct field points. Let T(X,Z) in F(X)(Z) have numerator and
denominator Z-degrees at most h>=1. Count scalar labels z at which T_z
is defined, is a polynomial of degree at most D, and agrees with f+zg
on at least A coordinates.

Either T(X,Z)=U(X)+ZV(X) identically with polynomial U,V of degree<=D,
or the number of these nearby labels is at most

    (8h+10)n/(A-D).

In the affine case, the number of full-support MCA-bad labels is at most
n-A+1. Thus a fixed positive agreement surplus A-D=eta*n allows only
O(h/eta) nearby labels on any non-affine bounded-degree rational path,
regardless of field characteristic or the X-heights of the rational
function. This is stronger than merely a linear bad-label bound.

## Proof

Clear denominators in X and cancel common factors to write T=a(X,Z)/b(X,Z),
with coprime a,b in F[X,Z], b nonzero, and both Z-degrees<=h. Only labels
where b(X,z) is nonzero as a polynomial are considered. For every defined
polynomial specialization P_z, the polynomial identity a_z=b_z P_z holds.

At domain point x define

    F_x(Z)=a(x,Z)-b(x,Z)(f(x)+Zg(x)),  deg F_x<=h+1.

Call x persistent when F_x is identically zero, and let H be their count.
At a persistent point b(x,Z) is not identically zero: otherwise X-x would
divide both a and b. Thus at each persistent coordinate, all but at most h
of the selected scalar labels agree with the received line. At a
nonpersistent coordinate, agreement implies F_x(z)=0, so at most h+1
selected labels can agree there. These assertions include specialization
base points where both a(x,z) and b(x,z) vanish.

Put delta=A-D. If H<=D+delta/2, each nearby label needs at least delta/2
nonpersistent agreements. Their total incidence is at most(h+1)n, giving
at most2(h+1)n/delta nearby labels.

Suppose H>D+delta/2, and select L nearby labels. If T is affine in Z over
F(X), then any two polynomial values make its two coefficients polynomials
of degree<=D; the affine alternative follows. With at most one selected
label the numerical bound is immediate. We may therefore assume T is not
affine over F(X).

Any graph line P=U+ZV over F(X) meets the graph of T in at most h+1 labels:
otherwise the nonzero numerator of T-U-ZV, of Z-degree<=h+1, would have
too many roots. Thus the selected graph points (z,P_z) have at most
(h-1)L(L-1) ordered collinear triples. Every noncollinear triple has a
nonzero affine-incidence determinant, a polynomial in X of degree<=D.
It can share at most D persistent agreeing coordinates.

At each persistent coordinate at least L-h selected candidates agree.
For L>=h+2 the ordered triple count therefore satisfies

    H(L-h-2)^3 <= D L^3+H(h-1)L^2.

Here the lower bound follows from(b)_3>=(b-2)_+^3, and the upper bound
counts noncollinear triples by their degree-D determinant and collinear
triples by H. Since

    (L-h-2)^3 >= L^3-3(h+2)L^2,

we obtain

    (H-D)L <= (4h+5)H,
    L <= (4h+5)H/(H-D) < (8h+10)n/delta.

The smaller L<h+2 case also satisfies the stated bound. This proves the
non-affine alternative. In the affine alternative, if c coordinates agree
persistently with U,V, then c<A permits at most(n-c)/(A-c)<=n-A+1 nearby
labels; c>=A permits at most n-c bad labels, because a bad full support
must contain a nonpersistent agreement. This proves the final assertion.

## A matching inverse-gap scale inside a non-affine projective path

The dependence on the reciprocal gap cannot be removed. Fix an even J>=2,
a degree cap D>=J-1, and t>=2. Let R be monic with D+1 distinct nonzero
roots, including a_1,...,a_J. Use the rational path

    T_z(X)=zR(X)/(zX-1).

Its polynomial values are0 at z0 and P_a=R/(X-a) at z=1/a for every
root a. There are D+2 such values. Pair the J selected roots. For each
pair(a,b), introduce t distinct nonzero domain points outside the roots
of R, all different across pairs. At each such point x, choose f(x),g(x)
so that the received affine line passes through (1/a,P_a(x)) and
(1/b,P_b(x)). On all D+1 roots of R set f=g=0.

The domain has n=D+1+Jt/2 points. Every selected P_a agrees on exactly
D+t coordinates: D roots of R other than a, and the t padding points
assigned to its pair. At a padding point x, the function
z -> zR(x)/(zx-1) is a non-affine projectivity and its chord at two
nonzero labels meets it exactly at those labels. All other nonzero
polynomial members have just D agreements; the zero member has D+1.
Hence at A=D+t the nearby labels WITHIN THIS RATIONAL PATH are exactly
the J selected labels.

All J labels are full-support MCA-bad. Any degree<=D interpolant G for g
on the support of P_a has D prescribed roots, namely the roots of R except
a. Thus G=cP_a. On a padding point assigned to pair(a,b), direct subtraction
gives

    g(x)/P_a(x)=-ab/(x-b).

This ratio differs at the t>=2 distinct padding points, ruling out such G.
The construction works over every sufficiently large prime field; all
points and polynomials lie in that prime field.

Taking D proportional to t and increasing t keeps J fixed and the rate
and gap convergent to positive constants. The relation

    J=2(n-D-1)/(A-D)

shows that J is of order(1-rho)/eta. Exact fixed rational rate and gap can
also be obtained by adding unused padding points: choose J even with
J*eta/2<1-rho, K=rho*n, D=K-1, t=eta*n+1, and fill the remaining
(1-rho)n-Jt/2 coordinates with values avoiding all D+2 path members.
For sufficiently large n all counts are nonnegative integers, and prime
fields can be arbitrarily large. This remains a constant-in-n example,
not the sought superlinear fixed-gap counterexample for the whole code.

No assertion is made that these are the only nearby witnesses in the
entire Reed-Solomon code. Exactness here concerns the specified path.

## Consequence for the existing complete-coverage counterexamples

If one rational formula selects witnesses at L>n-A+1 full-support bad
labels, its challenge degree must satisfy

    h >= (A-D)L/(8n)-5/4.

The affine alternative cannot account for that many bad labels. In the
complete-coverage constructions L=p-1 and A-D=eta*n+1, so EVERY rational
witness selection has challenge degree Omega(eta*p), or Omega(p/log p)
when eta=Theta(1/log p). This is a degree obstruction, not a running-time
lower bound; branching algorithms can still recover witnesses efficiently.

## Verification status

Local proof audit checks: specialization base points are counted among
at most h excluded labels per persistent coordinate; an affine rational
path with two polynomial values has polynomial coefficients; graph-line
intersection degree is at most h+1; the ordered-triple constants and
small-L case are valid in every characteristic. No separate agent or human
referee has reviewed the theorem.

`check_rational_path.py` passes complete path-bank checks at lengths160,
320,640 over F1009, all at exact rate1/4 and capacity gap1/8. Polynomial
member counts are41,81,161, but precisely10 labels on each path are nearby.
Independent interpolation verifies every selected full agreement support
is bad. All other path members' agreement counts and the specialization
base-point incidence ledger are checked. These finite checks supplement,
and do not replace, the general proof or enumerate the whole RS code.
