# Trace pullbacks of the norm bank: degree bound and remaining scope

September 19, 2026. Exact test of a named coefficient-trace compiler,
following the three-point affine-descent theorem. No manuscript changes,
search, or positive construction. The argument does not concern the
archived pure-character family.

## 1. Compiler and the degree-four bound

Let Q be a prime power, E=F_(Q^3), and let D be n distinct elements of
F_Q. The prime-alphabet specialization is Q=p. Write sigma for
coefficientwise Q-Frobenius, fixing the polynomial variable X. Put

    B_Q={(a,b): Norm(a)=-1, b=-a^(Q^2+1)}.

Choose A,B in E[X], B nonzero on D, and H in F_Q[X], with

    deg A, deg B, deg H <= d.

Here d bounds these chosen polynomials themselves; it is not merely a
bound on possibly cancellation-reduced output polynomials. For (a,b)
in B_Q the traced candidate is

    h_(a,b)(X)=H(X)+Tr_(E/F_Q)(a A(X)+b B(X)),          (1)

where trace applies to coefficients. These candidates have degree at
most d. The inherited received word is

    w(t)=H(t)+Tr_(E/F_Q)(A(t) A(t)^Q / B(t)^Q), t in D.              (2)

To relate this to the original norm bank, put y(t)=A(t)/B(t). If y(t)
is a square of a native evaluation coordinate, the original word at that
coordinate is y(t)^(Q+1), while the original witness is a y(t)+b.
Multiplication by B(t), followed by trace, gives exactly (1)--(2).
Actual membership in the native evaluation domain is a separate guard.
The degree conclusion below holds for (2) whether or not that guard holds.

Define the formal rational function

    R(X)=sum_(i=0..2) A^[sigma^i](X) A^[sigma^(i+1)](X)
                              / B^[sigma^(i+1)](X),                 (3)

with indices taken modulo three. Since t belongs to F_Q, twisting
coefficients in (3) computes the Q-Frobenius of evaluated values.
Thus w(t)=H(t)+R(t). This identity and its degree estimate would not
hold on arbitrary extension-field input nodes by just fixing X.

The common denominator

    N_B(X)=B(X) B^[sigma](X) B^[sigma^2](X)

belongs to F_Q[X], has degree at most 3d, and is nonzero on D. The
numerator of R after multiplication by N_B has degree at most 4d:
each summand has two A factors and the two remaining B factors.
Consequently, for every C in F_Q[X] of degree at most d,

    N_B(X) [H(X)+R(X)-C(X)] in F_Q[X],
    degree <=4d.                                      (4)

**Degree gate.** Unless H+R=C as a rational-function identity, C has
at most 4d agreements with w on D. In particular, at threshold T>4d
the entire degree-at-most-d Reed--Solomon list has at most one distinct
polynomial. Many bank parameters may map to that same polynomial;
parameter multiplicity is not list size.

For fixed d this excludes a growing-agreement prime-field list from
this compiler. More generally, if d=o(n), the first-order scale
sqrt((d+1)n/2) eventually exceeds 4d, so this route cannot supply a
growing list above that scale. No bound of 4d is asserted when only
the output candidates, rather than A,B,H, are known to have degree d.
Section 2 gives two cases where that missing premise is forced.

At fixed positive rate with a fixed positive agreement gap above d/n,
the already proved [fixed witness-span gate](../../strategy_review/fixed_witness_span_gate/INDEPENDENT_AUDIT.md)
separately bounds the number of traced-bank outputs by a constant:
(1) has F_Q-affine span of dimension at most six. If that span has
common evaluation zeros, one can first add the constant polynomial 1,
giving dimension at most seven and no common zero. This observation
uses the existing gate and is not a new general list-size theorem.

## 2. When cancellation cannot conceal the input degree

The whole bank affinely spans E^2 over F_Q. In fact every nonzero
affine F_Q-functional on E^2 vanishes on at most 3(Q+1) bank points.
The latter bound is deliberately elementary and need not be sharp.

Every such functional has the form

    ell(a,b)=c+Tr_(E/F_Q)(u a+v b),
                   c in F_Q, u,v in E, not all zero.                (5)

Let M=Q^2+Q+1 and write a=-z with z^M=1. On the bank b=a^(-Q)=-z^(-Q).
Expression (5), as a function of z, uses precisely the constant
character and the six characters with exponents

    +1,+Q,+Q^2,-1,-Q,-Q^2 modulo M.

These seven exponents are distinct for every Q>=2, including Q=2.
After reducing exponents to [0,M-1], a polynomial of degree below M
that vanishes on every M-th root of unity is zero. Comparing its
coefficients forces c=u=v=0. Thus a nonzero (5) does not vanish on
the entire bank, and the full affine span assertion follows.

For the zero-count bound, use the Moore parameterization

    (a,b)=(-z^(Q^2)/z,-z^Q/z),
                   z in E* modulo F_Q*.

Multiplying (5) by Norm(z) turns it into a homogeneous cubic in the
three F_Q-coordinates of z. It is nonzero as a function on P^2(F_Q)
by the preceding character argument. Choose an F_Q-projective point
where it is nonzero. Each of the Q+1 lines through that point meets
the cubic in at most three rational points, because its restriction
to the line is nonzero. Every zero lies on exactly one such line.
Hence (5) has at most 3(Q+1) zeros on the bank.

Now allow arbitrary polynomial degrees for A,B,H, and suppose every
retained output in (1) has formal degree at most e. For each j>e,
its coefficient of X^j is

    H_j+Tr(A_j a+B_j b).

If more than 3(Q+1) distinct bank parameters are retained, the
zero-count bound forces H_j=A_j=B_j=0. Thus A,B,H themselves have
degree at most e, and Section 1 applies with d=e. The same conclusion
holds for the entire bank for every Q, by its full affine span, even
when the numerical 3(Q+1) bound is vacuous at a small Q.

There is also an exact evaluation-level version. First replace A,B,H
by their remainders modulo the domain locator prod_(t in D)(X-t).
Coefficient trace commutes with this reduction because the locator
has coefficients in F_Q. If the retained candidate evaluations admit
degree-at-most-e representatives, their reduced polynomials have
degree at most e. The preceding argument then forces the reduced
A,B,H to have degree at most e. Their evaluations, nonvanishing B,
and received word (2) are unchanged. Thus the argument does not
confuse a high-degree chosen representative with its codeword values.

This retained-parameter threshold does not exclude every growing
subbank: 3(Q+1) itself grows with Q. In particular, cancellation on
a smaller retained family remains outside this degree-forcing claim.
The ternary-cubic argument is for Tr_(E/F_Q); a further trace to a
proper subfield of F_Q does not inherit its zero-count bound.

## 3. Growing extension degree: a real remaining distinction

Let Q=p^r and E=F_(p^(3r)), take prime-field nodes D subset F_p, and
instead trace all the way to F_p. With the same formulas for the
native bank and chosen A,B of degree at most d, write sigma for
coefficientwise p-Frobenius. The inherited trace word is

    R_p(X)=sum_(i=0..3r-1)
       A^[sigma^i](X) A^[sigma^(i+r)](X)
                                / B^[sigma^(i+r)](X).

Clearing Norm_(E/F_p)(B) gives denominator degree at most 3r*d and
numerator degree at most (3r+1)d. Including a common prime-field
translation H of degree at most d, every nonidentity degree-at-most-d
candidate therefore has at most (3r+1)d agreements.

The traced witness span has dimension at most 6r over F_p. When r
grows, neither its dimension nor the received-word degree bound is
constant. The fixed-r conclusion must not be used to rule out this
regime. At fixed d>=1, agreement of order sqrt(n) would at least require
r of order sqrt(n)/d from this particular degree test; this is a
necessary condition, not a construction.

Nevertheless, increasing r does not increase the inherited native
agreement at a fixed pullback degree. Before the final trace, native
agreement at a prime-field node is precisely

    A A^[sigma^r] - a A B^[sigma^r] - b B B^[sigma^r] = 0.          (6)

This polynomial has degree at most 2d, independently of r. If A/B
is nonconstant, at most one pair (a,b) can make (6) identically zero:
subtracting two such identities gives

    (a-a') A+(b-b') B = 0.

Every other bank member inherits at most 2d matching coordinates.
If A/B is constant, all candidates having the identity produce the
same pre-trace received function, hence the same traced output.

Thus a proposed low-degree growing-r construction with far more than
d agreements must obtain those agreements from new zeros of the final
trace, rather than from the native norm-bank incidence pattern. The
present work supplies no such new trace-kernel coincidence identity.
Arbitrary F_p-linear coefficient maps with a separately chosen word
are a different problem: they have no reason to obey the inherited
received-word identity (2).

## Conclusion

For the named bounded-degree trace/pullback compiler at Q=p, the
received word has rational residual degree at most 4d. This blocks
its low-rate growing-list transfer even if its traced quadratics
occupy the full three-dimensional coefficient space. The existing
span bound handles its fixed-rate, fixed-capacity-gap use. These are
precise failures of this route, not a general obstruction to prime-
field lists, nonlinear parameter transformations, or growing-r
trace constructions with genuinely new agreements.
