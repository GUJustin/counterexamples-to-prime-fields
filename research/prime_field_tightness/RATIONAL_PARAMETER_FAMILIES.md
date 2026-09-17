# Bounded rational dependence on the challenge forces linear MCA

September 17, 2026. Auxiliary proof note; no novelty claim.

The stronger theorem in RATIONAL_PATH_RIGIDITY.md now gives a constant
nearby-label bound for non-affine paths at a fixed gap. The height-reconstruction
argument below remains a separate algebraic observation; it is not needed
for the stronger theorem and has not been added to the manuscript.

## Theorem

Fix h>=1. Let T(X,Z) be a rational function in Z over F(X), with numerator
and denominator Z-degrees at most h. Its X-coefficient heights are
unrestricted. On n distinct evaluation points, use polynomial code degree
cap D and integer agreement threshold D<A<=n. Count finite scalar labels z
such that T(X,z) is defined as an element of F(X), is a polynomial of degree
at most D, and is a full-support MCA-bad candidate for a received line f+zg.
Then the count is at most

    max(2h, h(2h+1)D+h, n-A+1, (h+1)n/(A-D)).

Thus at fixed h and fixed positive capacity gap, the count is O_h(n),
without any restriction on characteristic or the original coefficient
heights. A fixed union of these families has the same linear conclusion.

The h=1 projective-pencil lemma has the sharper finite-member term D+2.
This theorem is about rational dependence on Z. It does not cover algebraic
branches of unbounded degree, arbitrarily many rational families, or a
candidate assignment that has no such common rational representation.

## 1. A height bound forced by polynomial specializations

If T has at most2h polynomial values of degree<=D, the conclusion is
immediate. Otherwise choose2h+1 distinct scalar labels z_i with polynomial
values P_i of degree<=D. A representation T=A/B with Z-degrees<=h satisfies

    A(z_i)-P_i B(z_i)=0.

These are2h+1 linear equations over F(X) in2h+2 coefficients, with matrix
columns z_i^j and -P_i z_i^j for0<=j<=h. Choose a nonzero kernel vector by
maximal-rank minors. It represents a nonzero polynomial pair A,B in F[X,Z]
with Z-degrees<=h. Its A coefficients have X-degree at most(h+1)D, and
its B coefficients at most hD: a cofactor for a B coefficient omits that
one of the h+1 polynomial-valued columns. Constants in the other columns
have X-degree zero. This remains true for deficient rank by taking a
maximal independent set of rows and a dependency among one more column.

No nonzero kernel vector can have B=0, since a degree<=h polynomial A(Z)
cannot vanish at2h+1 distinct labels. This new A/B is the original T:
its cross product with any original degree-h representation has Z-degree
at most2h and vanishes at all2h+1 selected labels. The original denominator
is nonzero at these labels. Thus the cross product vanishes identically.

Cancel the common polynomial factors of A,B. The bounds remain

    deg_Z A,deg_Z B<=h,
    deg_X A<=(h+1)D, deg_X B<=hD,

and A,B are coprime in F[X,Z].

## 2. The generically nonpolynomial case

If deg_X B>0, the resultant R(Z)=Res_X(A,B) is nonzero. Its degree is at
most h(deg_X A+deg_X B)<=h(2h+1)D. At a scalar z where B_z remains of
positive degree, a polynomial quotient A_z/B_z forces a common root and
hence R(z)=0. The labels where B_z loses its leading X coefficient number
at most h. Labels where B_z is identically zero give no defined value:
A_z cannot also vanish identically, since A,B have no common Z-z factor.
Thus there are at most h(2h+1)D+h polynomial specializations, irrespective
of their agreement. This is the second term of the theorem.

## 3. The generically polynomial case

Otherwise B is a polynomial in Z alone. Every selected polynomial value
has B(z_i)!=0. Each X-coefficient of A above degree D is a degree<=h
polynomial in Z vanishing at2h+1 labels. Hence deg_X A<=D. All defined
T_z are now polynomials of degree<=D.

Take any two distinct labels at which T is defined and let U+ZV be the
polynomial pencil interpolating those two values; deg U,deg V<=D.
If T=U+ZV identically, at most n-A+1 labels are full-support bad, by the
sharp polynomial-pencil incidence bound.

Otherwise E(X,Z)=A(X,Z)-B(Z)(U(X)+ZV(X)) is nonzero, has X-degree<=D,
and Z-degree<=h+1. A coordinate identity T(x,Z)=f(x)+Zg(x) forces
(f(x),g(x))=(U(x),V(x)) by the two chosen labels. It therefore makes
every Z-coefficient of E vanish at x. At most D coordinates can be
persistent identities, since some coefficient is a nonzero polynomial
of degree<=D.

At each other coordinate,

    A(x,Z)-B(Z)(f(x)+Zg(x))

is a nonzero polynomial of degree<=h+1. It permits at most h+1 defined
scalar labels. Every nearby label needs at least A-D such nonpersistent
agreements. Total incidence gives at most(h+1)n/(A-D) nearby labels,
and thus at most that many bad labels. This proves the theorem.

## Why this is relevant to the tightness question

Large algebraic coefficient heights cannot, by themselves, make a
fixed-degree rational candidate path have superlinear exceptional count.
Enough low-degree polynomial specializations force a low-height
representation, and its resultant already pays for all nongeneric
specializations with a linear budget. A fixed-gap superlinear construction
must evade a cover by boundedly many bounded-Z-degree rational paths.
This is a restriction on possible constructions, not a proof that all
candidate banks admit such a cover.
