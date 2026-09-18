# Independent integrable-curvature routing audit

The integration and heavy-group argument is valid under the explicit
hypotheses below. It does not by itself prove that the new curvature
source is integrable, or supply a numerical benchmark receipt.

## Integration and Frobenius: precise sufficient assumptions

Let G(X,Z,Y,R) be polynomial, independent of V, and

    Q=G_X+R G_Y+2V G_R.

For an actual candidate P of degree <=w, substituting
R=P', V=P^[2] gives

    Q(X,z,P,P',P^[2]) = d/dX G(X,z,P,P').

Thus Q=0 only implies that G(X,z,P,P') has zero derivative.
In characteristic p it need not be constant: X^p is the basic warning.
An explicit weighted degree bound wt(G)<p, for weights X=1,Y=w,
R=w-1, is sufficient. Then the substituted polynomial has degree <p,
so zero derivative forces it to be constant. Characteristic zero has
no corresponding degree restriction.

There is a constructive degree normalization if polynomial integrability
is already known. The differential operator above is homogeneous of
weight -1, with wt(V)=w-2. If wt(Q)<T, decompose any polynomial primitive
G into weighted homogeneous parts and discard every part of weight >T.
Each discarded derivative vanishes separately. This gives another
primitive of weight <=T, hence the required bound when T<p. One can
also discard Z-homogeneous components above deg_Z Q, since the operator
does not mix Z degrees. These observations do NOT establish polynomial
integrability of an arbitrary curvature-linear Q.

## Coordinate constants and degree after substitution

Assume the formal curvature contact condition holds at every received
coordinate x. Its t^0 coefficient is

    G_X(x,Z,f_x+Zg_x,R)+R G_Y(x,Z,f_x+Zg_x,R)
      +2V G_R(x,Z,f_x+Zg_x,R)=0.

For characteristic different from two this forces the displayed G_R to
vanish. If the R degree is <p (as follows from the p-safe weighted
bound when w>=2), then

    G(x,Z,f_x+Zg_x,R)=h_x(Z)

is independent of R. In characteristic zero the same conclusion is
automatic. An actual solution with agreement at x therefore has
integration constant h_x(z).

The degree parameter H in the counting lemma MUST bound deg h_x.
It is not enough to bound deg_Z G: substitution Y=f_x+Zg_x can raise
the Z degree. The safe general bound is

    H=max{deg_Z(monomial)+deg_Y(monomial): monomials of G},

and a joint jet-plus-challenge degree cap L gives H<=L.

## Exact heavy-group dichotomy

Partition the n coordinates by identical polynomials h_x(Z). Fix
integers 1<=t<=A<=n. There are at most floor(n/t) classes of size >=t.
For any challenge z and any solution P agreeing on at least A
coordinates, choose A such coordinates S. Their h_x(z) are all equal.

If some identity class contributes at least t coordinates of S, the
solution is routed to that heavy class's first-order equation

    G(X,z,P,P')-h(z)=0

and has at least t agreements within that fixed class. This does not
assert that it agrees with the entire class or its full original
agreement support.

Otherwise write the class sizes within S as a_i<=t-1. The number of
ordered pairs from different classes is

    A^2-sum a_i^2 >= A^2-(t-1)A = A(A-t+1).

For each ordered coordinate pair in distinct classes, the nonzero
polynomial h_x-h_y has at most H challenge roots, over any extension
field. Counting incidences (challenge,ordered pair) therefore bounds
the number of unrouted challenges by

    floor(H n(n-1) / [A(A-t+1)]).

Only one selected witness per unrouted challenge is needed. Multiple
candidate solutions at the same challenge do not multiply this bound.
An exact numerator H times the number of cross-class ordered pairs
would improve the displayed conservative bound.

## Zero specializations and downstream use

If a subsequent first-order theorem requires its specialized equation
to be nonzero, this is an extra issue: G(X,z,Y,R)-h(z) can vanish
identically at special z. When Q is nonzero, G has a nonzero coefficient
c(Z) of some nonconstant monomial in (X,Y,R). Every zero specialization,
for every heavy class simultaneously, lies among the roots of c.
Thus one common exceptional set of at most deg c<=H suffices; one
does not need H exceptions per group. If Q=0 identically, this reasoning
is unavailable and that case must be excluded or treated separately.

After excluding these labels, the heavy-group conclusion remains a
routing statement. Applying an existing first-order theorem still
requires checking its degree, characteristic, ordinary-core, and
agreement-threshold hypotheses on that particular group. It is not
legitimate to count routed challenges as already bounded merely because
there are few groups, or to replace t agreements by full-support
ordinary correlated agreement.

## Formal local integration check

The equivalence recorded in INTEGRABLE_SOURCE_DOMINATION.md also checks
under its degree/characteristic assumptions. Restrict curvature contact
to formal quadratic arcs P=w+a1*t+a2*t^2. Integrating dG/dt through
order m uses invertibility of 1,...,m, and the constant term is h_x.
The invertible change R=a1+2a2*t, E=-a2 gives the first-jet identity
G(x+t,w+tR+t^2E,R)-h_x=0 mod t^(m+1).
Conversely substitute a formal cubic arc into this identity and
differentiate; R=a1+2a2*t+3a3*t^2, V=a2+3a3*t, E=a3 recover the
full curvature contact relation by an invertible triangular change.
No assumption about the availability of actual low-degree codeword
arcs is used: these are identities in indeterminates.

The standard coefficient-count domination in that note follows under
its stated shared caps. At the target, adding the X coefficients for
jet monomials 1 and Y already gains (A-1)(2L+1), exceeding the
n(L+1) freed constants by 100404L-80870>0 for L>=1. This is a
comparison of sufficient dimension certificates, not a nonexistence
claim about all integrable sources or global constraint dependencies.
