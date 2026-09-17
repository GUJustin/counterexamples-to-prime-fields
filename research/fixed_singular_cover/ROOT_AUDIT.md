# Independent root audit — September 17, 2026

Status: the three mathematical arguments in PROOF.md,
ALL_SINGULAR_LOWER.md, and FIXED_T_RICCATI.md pass independent proof review.
This is a human-readable mathematical audit, not formal verification.

## Fixed cover

The cited nonsingular-agreement bound applies to actual implicit-equation
solutions and their substituted separants. Removing labels counted by that
bound leaves at least kappa+1 agreements in the fixed set. When kappa<s,
three such supports intersect in more than D positions; polynomial
interpolation forces the candidates into an affine pencil. The final n
counts accidental coordinates outside its coefficientwise agreement set.
The hypothesis must quantify over every candidate being counted. A formal
factorization of the separant alone does not establish that hypothesis.

## Entirely singular lower example

At z=x_i, the agreement equation outside the core is u_j(z-x_j)=0,
so nonzero u_j give exactly one extra coordinate. The s>D core positions
force any full-support direction to be X^D, which fails at that extra
coordinate. The implicit identity factors into h(h+R0(X)(X-z)); its
second factor cannot vanish by degree. Characteristic greater than D
then implies all its polynomial solutions are zX^D+c. Thus the singular
cover is uniform, including solutions other than the displayed witnesses.

The ordinary-common-agreement strengthening is a separate probabilistic
choice of direction values. For an A-subset with m core coordinates,
there are at most q^(D+1-m) possible nonzero residual polynomials and each
has matching probability at most (q-1)^(-(A-m)). The stated union bound
follows, using A=s+1 and A-m<=n-s when m<=D only after comparison of the
q factors: in fact A-m may exceed n-s for arbitrary subsets. This detail
requires the actual feasible-subset constraint A-m<=n-s, which always
holds because there are only n-s outside coordinates. With that constraint,
the printed bound is correct. For n=100m the displayed logarithmic upper
bound is negative already at m=1 and decreases thereafter. This establishes
existence over every prime q>100m, not an explicit selection algorithm.

## All fixed-T Riccati identities

The low-degree-T case follows from the cover theorem since its coordinate
root set has at most 2D members. When deg R>=deg T>2D, the selected high
coefficients are linear triangular: the derivative uses strictly higher
message indices and the quadratic term has smaller degree. Cramer's rule
gives the claimed degree bounds even when the determinant has roots;
those roots are explicitly excluded.

In the remaining case the only possible identically zero pivot is indexed
by one j in 1..D, since these integers remain distinct in the field. Its
compatibility equation is independent of both free coefficients. Descending
recurrence leaves P=c+Q+dV with V monic of degree j. Generic translation
to X+w preserves all original labels and agreements over F(w), and makes
T(w)V'(w) a nonzero polynomial in z. Absorbing Q(w)+dV(w) into the constant
parameter keeps the stated challenge-degree bounds.

The translated constant residual is linear in d. After solving it, the
X^(2j) residual has a nonzero constant quartic leading coefficient in c:
its d^2 coefficient is -1 and it has no cd or c^2 term. Hence the plane
residual system is nonzero and has no vertical common component. Its
bidegree and the agreement bidegree are bounded by (3M,4) and (M+K+1,2).
Removing the common curve factors before applying the two-equation
intersection bound accounts for isolated points without discarding curves.
Summed intersection counts give the printed 24M and 6M+4J terms.

More than D persistent coordinates interpolate an affine polynomial
pencil over the original field: the received coordinate values are already
in that field. The parameter c equals its value at the translated origin,
and d is its degree-j coefficient after subtracting Q, so reconstruction
is injective outside the excluded roots. Each such curve contributes at
most n bad labels. The h=0 case and nonmonic constant scaling cause no
additional exceptions.

Scope: these statements count actual solutions of the stated identity.
An application to all nearby codewords additionally requires containment.
They prove a linear-order limitation for this broad fixed-T family, not
a universal improvement of the first-order proximity-gap theorem and not
a better.codes score.

## Extension: moving derivative coefficient (independent derivation)

The argument also permits T(X,z) to have challenge degree at most h.
For deg_X T<=2D, take S to be the coordinates where T(x,z) vanishes
identically. Its size is at most 2D, by any nonzero challenge coefficient.
Outside S there are at most hn singular coordinate-label incidences in
all. With e=floor(lambda*n/2), at most hn/(e+1)<=2h/lambda labels have
more than e such coordinates. The fixed-cover theorem then has
L>=lambda*n/2. No uniform small moving root count at each label is needed.

For high degree T, the high-degree-R Cramer argument is unchanged. In the
resonant case the other pivots are (i-j)tau(z), where tau is the leading
X coefficient of T. After excluding tau roots, a shared denominator
delta=tau^D gives P=c+(Q+dV)/delta, with delta,Q,V of challenge degree
at most K=h(D+1), V of X degree j and leading coefficient delta. Generic
translation again makes Q,V have zero constant term. It preserves these
bounds. The full residual multiplied by delta^2 has challenge degree
at most M=2K+h. Its constant coefficient has a common factor delta;
after dividing, it equals

  -delta*c^2 + R(w,z)*delta*c + T(w,z)*Q'(w,z)
      + T(w,z)*V'(w,z)*d - S(w,z)*delta.

Thus v=T(w,z)V'(w,z) is nonzero and d=N(z,c)/v, with N of c degree2 and
challenge degree at most M. Substitution and multiplication by v^2 give
bidegree (3M,4) residual equations. The X^(2j) equation has leading c^4
coefficient -delta^4. Consequently every vertical common factor is
supported on already excluded delta roots. Agreement equations have
bidegree (M+K+1,2). The previous intersection argument applies with
at most K+M excluded labels and 24M isolated points, giving

  K+25M + n(6M+4(M+K+1))/(A-D) + 4n.

A nonzero resonant compatibility polynomial instead contributes at most
K labels. Persistent interpolation is in the original message P, so the
rational recurrence and generic coordinate translation do not change the
meaning of full-support common direction. This proves the broader
bounded-challenge monic Riccati limitation under the same two agreement
slacks. It removes moving T as an escape within this monic quadratic
class; a genuinely nonconstant quadratic coefficient or a different
nonlinearity remains outside the conclusion.
