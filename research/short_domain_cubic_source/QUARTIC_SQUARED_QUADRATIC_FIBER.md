# The exact squared-quadratic fiber stratum reduces to the degree-two pencil gate

Status: bounded algebraic reduction, checked independently by root. This is an
application of the audited rational-pencil theorem, not a classification of
all positive-dimensional critical schemes for quartic first integrals.

Let k be algebraically closed, D>=1, and

    F(X,u)=u^4+a3(X)u^3+a2(X)u^2+a1(X)u+a0(X),
    deg aj <= (4-j)D.

Let H be nonzero. Assume there is a constant c0 such that

    F(X,u)-c0 H(X)=G(X,u)^2,
    G(X,u)=u^2+g1(X)u+g0(X).

Take characteristic zero or p>max(2,10D). Then any n-coordinate received word
has at most max(40,floor(1/eta)) degree<=D sections of F(P)=cH agreeing on at
least D+eta*n coordinates, for eta>0. In characteristic zero the corresponding
max(16,floor(1/eta)) bound from the characteristic-zero nine-label reduction in RATIONAL_PENCIL_MOBIUS_BRIDGE.md also applies (the displayed manuscript Theorem R.6 states the positive-characteristic version).

Proof. Comparing u^3 and u^2 coefficients gives

    2g1=a3,   2g0=a2-g1^2.

Thus deg g1<=D and deg g0<=2D. If every section lies in the c0 fiber, there
are at most two polynomial roots of G and the result follows.
Otherwise choose one section P0 with label c1!=c0. Then

    G(X,P0)^2=(c1-c0)H(X).

Since constants are algebraically closed and c1-c0 is nonzero, this proves
H=h^2 for a nonzero polynomial h, after absorbing a constant into h. Every
other section consequently satisfies

    G(X,P)^2=(c-c0)h^2.

Choose lambda in k with lambda^2=c-c0. Factorization in the integral domain
k[X] gives G(X,P)=lambda*h or G(X,P)=-lambda*h. Thus the entire original
section bank is contained in the polynomial sections of ONE degree-two
rational pencil G(X,u)/h(X). The pencil has positive degree exactly two in u;
its numerator and denominator are coprime over k(X), because h is a nonzero
scalar in that field. Apply the audited rational-pencil list theorem.

This argument automatically includes the critical fiber lambda=0. No independent
assumption that H is square was needed. A noncritical section also gives
deg h<=2D, but the rational-pencil theorem does not require that extra bound.
Over an original smaller field, extend constants first and bound the enlarged
bank; no descent of lambda is necessary for the counting conclusion.

Scope: this proves the statement only when the repeated quartic fiber is an
EXACT square of a monic quadratic. A fiber of the form (u-R)^2 times a genuinely
different quadratic is not covered. Nor does a positive-dimensional critical
component by itself force this square stratum. No general quartic classification
or new lower construction is claimed.
