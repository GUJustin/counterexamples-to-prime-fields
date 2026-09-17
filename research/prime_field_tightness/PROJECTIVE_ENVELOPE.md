# Projective normalization: a broader linear MCA bound

September 17, 2026. Proof candidate under audit. No novelty claim.

## 1. Polynomial members of a rational projective pencil

Let T_z=(a z+b)/(c z+d) over F(X), with ad-bc nonzero. Consider scalar
labels z for which T_z is a polynomial of degree at most D. Either:

- there are at most D+2 such labels (including projective scalar labels); or
- the entire family is U+phi(z)V, where U,V are polynomials of degree at
  most D, V nonzero, and phi is a scalar fractional-linear transformation.

Proof. If there are at most two polynomial members there is nothing to
prove. Otherwise reparameterize three of them to P_0,P_1,P_infinity,
all distinct, at labels0,1,infinity. Write A=P_1-P_infinity, B=P_1-P_0,
g=gcd(A,B), A'=A/g, B'=B/g. Then

    T_lambda=(P_0 A'-lambda P_infinity B')/(A'-lambda B').

If A',B' are both constant this is the second alternative. Otherwise
for lambda nonzero and finite, E_lambda=A'-lambda B' is coprime to A'.
Polynomiality implies E_lambda divides Q=P_0-P_infinity, by subtracting
P_infinity E_lambda from the numerator. Distinct E_lambda are pairwise
coprime. Thus the number of nonconstant E_lambda that give polynomial
members is at most deg Q<=D. There is at most one additional lambda for
which E_lambda is a nonzero constant. If it exists, A' has positive degree,
and T_lambda=P_infinity+A'Q/E_lambda can have degree<=D only if

deg Q+deg A'<=D, hence deg Q<=D-1. Counting this possible member and the
two distinguished endpoints still gives at most D+2. This proves the claim.

The D+2 bound is sharp: for squarefree R of degree D+1 with nonzero roots,
T_z=zR/(zX-1) has the polynomial value0 at z0 and R/(X-a) at z=1/a for
every root a. These are D+2 distinct scalar labels and polynomial values.

## 2. Bad labels on one projective pencil

Use code degree cap D, length n and threshold A>D. Let M=n-A+1.
For any nondegenerate T_z as above, the number of full-support MCA-bad
labels with polynomial candidate degree<=D is at most

    B_old=max(D+2, M, 2n/(A-D)).

This first bound follows from the finite-member alternative immediately. In the other alternative,
T_z=U+phi(z)V. If phi is affine, the sharp polynomial-pencil bound gives
M. If phi is genuinely fractional-linear, a coordinate identity
f(x)+z g(x)=U(x)+phi(z)V(x) can hold identically in z only if V(x)=0,
g(x)=0, f(x)=U(x). There are at most D such persistent coordinates.
At each other coordinate, clearing the scalar denominator gives a nonzero
polynomial of degree at most2 in z. Every nearby label therefore consumes
at least A-D nonpersistent incidences, and there are at most2n in total.
This bounds all nearby labels, hence also the bad ones. No characteristic
restriction is used.

The stronger rational-path rigidity theorem subsequently proved in
`RATIONAL_PATH_RIGIDITY.md` replaces this with

    B=max(M,18n/(A-D)).

Indeed a non-affine rational path of Z-degree1 has at most18n/(A-D)
nearby labels, whereas an affine polynomial path has at most M bad labels.
Taking the minimum of B and B_old is also valid. The argument in Section3
below uses the new B, so it no longer pays the potentially large D+2 term.

## 3. Low-degree projective residuals

Fix a polynomial matrix M(X)=[[a,b],[c,d]] with nonzero determinant Delta.
Let h count domain zeros of Delta, N=n-h>0, and t=A-h>0. Consider any
family of degree<=D polynomials P such that

    [aP+b : cP+d]=[u_P:v_P]

in the projective line over F(X), where u_P,v_P are coprime polynomials
of degree<=r, not both zero. The value infinity is allowed. Suppose
A>D, beta=t/N, and N>=128r/beta^4. Then every received line has at most

    38 B/beta^4,
    B=max(n-A+1,18n/(A-D)),

full-support MCA-bad labels witnessed by this family. In particular this
is O(n) at fixed positive capacity gap and fixed positive beta, for fixed r.
The matrix entries may have arbitrary degrees; their relevant restriction
is the number h of singular domain points.

Proof. Select one bad polynomial per distinct label and discard the h
singular coordinates. At retained points M is invertible, so the residual
projective value is well defined and agrees with M applied to the received
line. There are at least t=beta*N retained agreements for each selected
candidate.

For four distinct scalar labels, equality of projective cross ratios is
a homogeneous relation involving products of two wedges of residual pairs.
Its numerator has degree at most4r. If nonzero as a rational identity,
the quadruple can share at most4r retained agreement coordinates. This
remains valid when the received direction is zero or residuals are infinite.

For an identically zero relation, consider the first three residual values.
If they are all distinct, a unique projectivity from the scalar label line
maps to these values. All permitted fourth points lie on that projective
pencil over F(X). Composing with the inverse of M gives a projective pencil
of original polynomial candidates, which has at most B selected bad labels
by Section2. If exactly two of the first three residual values coincide,
the fourth value must equal the repeated value; these are all the same
original polynomial, and at most M=n-A+1 selected bad labels share it.
If all three coincide, any fourth value satisfies the relation, but there
are at most M^2 L such ordered triples, since each equal-value class has
size at most M. Thus the total number of coherent ordered quadruples is
at most B L^3+M^2 L^2.

For L>=6/beta, the fourth agreement incidence is at least
beta^4*N*L^4/16, by (b)_4>=(b-3)_+^4 and Jensen. Its upper bound is

    4r L^4+N B L^3+N M^2 L^2.

The size assumption gives4r<=beta^4*N/32. Rearranging yields

    L^2 <=(32B/beta^4)L+32M^2/beta^4,
    L <=32B/beta^4+sqrt(32)M/beta^2 <=38B/beta^4.

The case L<6/beta also satisfies the bound since B>=M>=1. This proves
the claim, subject to audit of the projective degeneracies above.

## Scope

This generalizes the affine rational normalization theorem. The latter
has sharper cubic constants and is preferable when it applies. The
projective statement allows reciprocal transformations and moving poles
in the normalization, but does not cover arbitrary candidate families.
In particular the determinant-zero budget and positive retained agreement
margin are essential. It is not a general prime-field exponent-one theorem.

## 4. Ordinary lists inside the normalized family

There is also a constant-size ordinary-list bound for the restricted
candidate family. Retain N=n-h coordinates, and let t=A-h. If

    t^2>2rN,

then at any received word the number L of candidates from this family
with at least A agreements is at most

    floor((t-2r)/(t^2/N-2r)).

Indeed distinct normalized projective functions have a nonzero wedge of
degree at most2r. They therefore agree at at most2r retained coordinates.
Choose exactly t retained agreements for each candidate. Pair incidence
and Cauchy give L^2*t^2/N-L*t<=2rL(L-1), which is the bound. This is an
ordinary list bound for the specified family only, not for the whole RS
code. At fixed beta=t/N and bounded r it is O(1/beta).

## Verification status

The proof above has been checked locally, including the constant-denominator
case in the D+2 lemma and the all-equal/partly-equal projective triples.
`check_projective_envelope.py` passes1489 polynomial-pencil fixtures over
three prime fields,13 sharp D+2 examples, and5392 exhaustive projective
quadruples over F5 and F7 including infinity. The complete fourth-incidence
argument is mathematical, not inferred from those finite checks. No separate
agent or human referee has reviewed this new note. It is not yet integrated
in the main manuscript; the simpler affine normalization result is included.
