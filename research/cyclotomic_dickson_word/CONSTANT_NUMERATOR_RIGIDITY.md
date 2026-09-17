# Complete characteristic-zero bound for constant-numerator kernels

Let r>=3, let A be a t-element subset of mu_r, and write

    S_A(X)=product_(a in A)(X-a),  pi_A=product_(a in A)a.

For c nonzero, consider the polynomial

    P(X)=c*(X^r-1)/S_A(X)

and the word W(X)=(X^r-1)^2/2 on mu_(4r), in characteristic zero.
All the following arguments take place in the complex numbers; they
therefore apply to cyclotomic coefficients and arbitrary complex c.

## General bound

The agreement count is at most

    r-t+gcd(r+t,4r).

Indeed, on mu_r the polynomial agrees precisely at the r-t points
outside A. At a in A, cancellation gives

    P(a)=c*r*a^(r-1)/S_A'(a),

which is nonzero, whereas W(a)=0.

Now take an agreement point x outside mu_r and put z=x^r. Cancelling
z-1 gives c=(z-1)S_A(x)/2. Since all relevant roots lie on the unit
circle,

    conjugate(S_A(x))=(-1)^t*pi_A^(-1)*x^(-t)*S_A(x),
    conjugate(z-1)=-z^(-1)*(z-1).

Conjugating the agreement identity and dividing by its original form
therefore yields

    x^(r+t)=(-1)^(t+1)*c/(pi_A*conjugate(c)).

The power map x -> x^(r+t) on mu_(4r) has kernel size
gcd(r+t,4r), so this equation has either zero or exactly that many
solutions in the whole domain. In particular there are at most that
many outside mu_r. This proves the bound.

## Prime r=3 modulo4

If r is prime, r=3 modulo4, and 2<=t<r, the agreement count is at most r.
For gcd(r+t,r)=1 implies

    gcd(r+t,4r)=gcd(r+t,4).

For t=2 this is1, for t=3 it is2, and for t>=4 it is at most4<=t.
Thus the general bound never exceeds r. The t=r case is a nonzero
constant polynomial and has at most r agreements as well.

For t=1, write A={a}. The maximum is r+1, attained exactly when c=a.
To prove the upper bound and equality statement, suppose there are
at least two agreements outside mu_r. The preceding power equation
puts all such agreements in one coset of mu_4. Since r is odd, that
coset has a unique representative u in mu_r. Its possible outside
points are iu,-u,-iu. For r=3 modulo4 the required values of c are,
respectively,

    C1=((1-i)u+(1+i)a)/2,
    C2=u+a,
    C3=((1+i)u+(1-i)a)/2.

C1=C2 would force u=i*a, impossible for u,a in mu_r with r odd.
Similarly C3=C2 would force u=-i*a, also impossible. The only
possible pair is C1=C3, which forces u=a and gives c=a. Then both
points ia,-ia really agree, while -a does not. Along with the r-1
zero agreements, the count is exactly r+1.

Consequently this entire constant-numerator family, for arbitrarily
large prime r=3 modulo4, attains no fixed positive agreement surplus
above r. Its only members with more than r agreements are precisely
the r rotated geometric-sum polynomials from GEOMETRIC_KERNEL_FAMILY.md.

## Scope

This is a complete theorem for the stated constant-numerator family,
not a theorem for all degree-<r polynomials. A general candidate
factored by its zero-word agreements has a residual numerator that
may be nonconstant; the conjugation step then contributes the ratio
of that numerator to its conjugate, so the fixed power-map fiber
argument no longer applies. The earlier finite t<=5 probe is now
superseded by this theorem at all prime r=3 modulo4 within its scope.
