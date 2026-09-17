# All fixed-T monic Riccati identities: proposed linear exception theorem

Proof, September 17, 2026. Independently audited in ROOT_AUDIT.md.
The stronger moving-T theorem is proved in appendix.tex.
This controls actual solutions, not the existence of an interpolating
identity containing every nearby candidate.

Let F have characteristic zero or p>D, D>=1. Let T(X) be any fixed
nonzero polynomial, and let R(X,z), S(X,z) have z-degree at most h,
where h is fixed; their X-degrees are unrestricted. Consider

    T P' - P^2 + R P - S = 0, deg P<=D.             (1)

On an n-coordinate received line with D<A<=n, call a solution bad when
its full agreement support has no degree-at-most-D common direction.
Assume A-D>=eta*n and A-5D/3>=lambda*n for positive constants eta,lambda.
Then the number of labels with a bad A-near solution is O_{h,eta,lambda}(n),
uniformly in deg T, deg_X R, and deg_X S.

The proof has four cases. Let t=deg T. Scale (1) by the leading
coefficient of T when considering pivots; retaining the monic P^2
coefficient is harmless, since nonzero constant scalings preserve all
arguments below. For simplicity the discussion takes T monic.

## 1. t<=2D: singular cover

The separant is T. Its actual domain root set has s<=2D coordinates.
The fixed-cover theorem, with e=E=0, B=2, H=h, applies with
L=A-min(s,floor((2s+D)/3))>=A-5D/3>=lambda*n.
It gives the stated O(n) bound without any restrictions on R or S.

## 2. t>2D and r=deg_X R>=t: unique rational family

The coefficients of X^(r+j), in descending order j=D,...,0, are linear
triangular equations for a_j in P=sum a_j X^j. Their pivot is R_r(z).
The derivative term uses only coefficients with index greater than j,
and P^2 contributes nothing because r+j>2D. Unless a coefficient of S
above r+D is nonzero, there are exactly D+1 such necessary equations.
A nonzero high coefficient restricts labels to at most h, finishing
this case. Otherwise, outside the at most h roots of R_r, Cramer's rule
gives one possible P=W/Delta, with

    deg_z Delta, deg_z W <= K0=h(D+1).

(Every matrix entry and right-hand side has z-degree at most h.)
Any further residual may reduce the set of labels; ignoring it is safe.
A coordinate agreement has numerator W(x,z)-Delta(z)(f_x+zg_x),
of degree at most K0+1. If at most D coordinates are persistent, each
nearby label contributes at least A-D nonpersistent incidences, giving
at most n(K0+1)/(A-D) labels. If D+1 persist, interpolation makes the
family an affine codeword pencil; bad labels then number at most n.
Thus h+n(K0+1)/(A-D)+n is a valid bound.

## 3. t>2D, deg_X R<=t-1, and no identically zero pivot

A nonzero coefficient of S above t+D-1 restricts labels to at most h.
Otherwise the already audited general triangular/Newton criterion applies:
nonlinear degree 2D<t, linear degree <=t-1, and pivots

    d_i(z)=i+R_(t-1)(z), i=1,...,D.

With all pivots nonzero polynomials, its bound is O_h(n) when A-D has
linear slack. Roots of nonconstant pivots are already counted by that
criterion. This case imposes no extra resonance assumption.

## 4. An identically zero pivot: reduction to a quartic plane curve

Since p>D, at most one pivot vanishes identically. If it is d_j, then
R_(t-1)=-j is constant and every other pivot i-j is a nonzero constant.
Again first remove the case of a nonzero S coefficient above t+D-1.
Solve the top equations in descending order, leaving a_j=d free and
a_0=c free. At the j-th equation the compatibility condition is a
polynomial in z independent of d,c. If nonzero, its z-degree is at most
K=h(D+1), and there are at most K labels. Otherwise recurrence gives

    P=c+Q_z(X)+d V_z(X),
    Q_z(0)=V_z(0)=0, deg_X Q<=D, deg_X V=j,
    V monic, deg_z Q,deg_z V<=K.

The equation at the resonant step is independent of d because its pivot
vanishes, and independent of c because all top degrees are at least t.
The remaining descending equations below j stay affine in d. The degree
bound follows by at most D multiplications by R coefficients of degree h;
all pivots divided out are nonzero constants.

For the next step, work over F(w) and translate X by a transcendental
w. This does not change z-degree, X-degree, or agreement counts. After
absorbing constant terms into c, write the translated Q,V with zero
constant terms again. V remains monic of degree j. Now

    v(z)=T(w) V'_z(w) != 0,

because j is nonzero in F and V'_z is nonzero. Translation is a proof
device: all original F-valued candidate labels remain distinct over this
extension, and persistent-coordinate interpolation eventually descends
any affine graph with two original F-points.

Write every residual coefficient as a polynomial in (z,c,d). Its degree
in (c,d) is at most 2 and its z-degree at most

    M=2K+h.

The constant-X coefficient has the special form

    E0=-c^2+u(z)c+v(z)d+w0(z),

with all coefficient degrees at most M. Exclude the at most M roots of v.
Solve d=(c^2-u c-w0)/v, and substitute into every residual, multiplying
by v^2. The resulting plane equations in (z,c) have bidegree at most

    (Z,ell)=(3M,4).

They are not all zero. Indeed the coefficient of X^(2j), before this
substitution, is

    -d^2 + alpha(z)c + beta(z)d + gamma(z).

Here V is monic degree j; the cd term is zero because deg V<2j, and
c^2 occurs only in the constant-X residual. Therefore after substitution
its c^4 coefficient is exactly -1. This also ensures the common residual
gcd has no vertical factor outside the excluded labels (in fact this
particular residual has no vertical factor at all).

An agreement at a coordinate, after multiplying by v, is

    v[c+Q_z(x)-f_x-zg_x]+V_z(x)[c^2-u c-w0]=0,

of c-degree at most 2 and z-degree at most

    J=M+K+1.

The plane gcd/Bezout incidence argument from NEWTON_DEGREE_CRITERION.md
now applies with agreement degree 2 instead of 1:

* isolated residual points: at most 2Z*ell=24M;
* curve components have total bidegree at most (Z,ell)=(3M,4);
* nonpersistent coordinate incidences on these curves: at most
  2Z+ell*J=6M+4J per coordinate;
* on a curve with at most D persistent coordinates, each nearby point
  has at least A-D nonpersistent incidences;
* more than D persistent coordinates force an affine codeword graph.
  Reconstruction is injective: c is the constant coefficient after
  translation, and d is recovered from the leading degree-j coefficient
  of P-Q. Thus distinct source curves cannot collapse to one graph.
  There are at most ell=4 such curves, and at most n bad labels on each.

A valid bound for this resonant case, with compatibility identically
zero, is therefore

    25M + n(6M+4J)/(A-D) + 4n.                    (2)

If h=0, M=0 and J=1; the argument still holds (the finitely many
constant solutions give horizontal curves, and no isolated labels).
For nonmonic fixed T, divide (1) by its nonzero leading coefficient;
replace the occurrences of -1 by the resulting nonzero constant
coefficient of P^2. All counts and degree estimates are unchanged.

## Scope and search implication

If all nearby candidates of interest obey one identity (1), then this
is an actual line bound for that line. Without that containment it is
only a bound on the equation's nearby solution subset. It is neither an
unconditional coding theorem nor a better.codes certificate.

At quarter-rate first-order agreement, A/D tends to about 1.87517,
which is strictly greater than 5/3. Thus a fixed derivative coefficient
and constant nonzero quadratic value coefficient cannot realize a
superlinear bad-label lower example there, at fixed challenge degree.
A future quadratic construction must evade at least one of these
conditions; a large genuinely moving singular set or a nonconstant
quadratic coefficient remain possible avenues.
