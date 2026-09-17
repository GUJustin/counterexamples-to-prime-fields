# Sparse padding preserves the first-order regime

September 17, 2026. A conditional consequence of the already verified
prime-field boundary compiler. This does not construct growing source
lists or establish an intrinsic quadratic lower bound.

The exact-halving compiler can leave the first-order agreement regime.
That is not an unavoidable obstruction: a small positive padding fraction
preserves any strictly positive margin above a continuous sufficient curve.

## Quantitative compiler with an arbitrary padding fraction

Let a word on N distinct points of F_p have L distinct degree-<k
candidates agreeing in at least A positions, where k>=2 and A>=k+1.
Let q>=1 and p>=max(2N,N+q). There is a received line on

    n=N-1+q, dimension K=k, agreement threshold A

having at least

    J >= p*q*A*L / [N*p+(2*(k-2)+q)*A*L]                 (1)

full-agreement-set MCA-bad labels (round the right side upward).
This is a saturation-aware inequality: it never asserts more than p
labels. It needs no source-list maximality or nearest-list assumption.

Proof. Choose an anchor incident with ell>=AL/N candidates and form
their distinct quotients Q=(P-w(anchor))/(X-anchor), each of degree
at most k-2. Each quotient has at least A-1 old agreements. On R=p-N
unused coordinates, their mean number of distinct values is at least

    mu=ell*R/[R+(ell-1)*(k-2)].

Since R>=p/2,

    mu >= ell*p/[p+2*(k-2)*ell].

Take the q unused coordinates with largest image sizes and independently
translate their images by the padding received values. The expected
union size is at least p*(1-(1-mu/p)^q), which is at least
p*q*mu/(p+q*mu). Substitution gives

    J >= p*q*ell/[p+(2*(k-2)+q)*ell].

The expression increases in ell. Substitute ell>=AL/N to obtain (1).
Set the line direction to zero on the old coordinates and one on the
new coordinates. A degree-<k direction witness for a selected candidate's
entire agreement set would vanish at its A-1>=k old agreements. It must
therefore be identically zero, contradicting any new agreement, where
the direction is one. Each label in the union is consequently a
full-agreement-set MCA failure. This does not rule out ordinary CA
on a different support.

## Exact parameters and exponent transfer

Fix rational 0<theta<=1 and let theta*N be integral. Choose
q=theta*N+1. Then exactly

    n=(1+theta)*N,
    rho_out=rho/(1+theta),
    a_out=a/(1+theta),
    eta_out=eta/(1+theta),

where rho=k/N, a=A/N, eta=a-rho. Assume p>=2N+1.
For q<=N+1 and k<=N,
2*(k-2)+q <= 3N-3 < 4N, whereas q>=theta*N. Thus (1) implies

    J >= theta*p*A*L/(p+4*A*L)
      >= (theta/5)*min(A*L,p).                           (2)

At fixed a>0 and theta>0, if p is superpolynomial in N and
L=Omega(N^c), (2) gives Omega(n^(c+1)) full-support MCA failures.
It suffices more generally that p=Omega(N^(c+1)). If L merely tends
to infinity and p/N tends to infinity, then J/n tends to infinity.
The source-family hypothesis remains unproved in the first-order regime.

## Staying above the coauthor first-order curve

Let a_1(rho) be the continuous sufficient curve in the recovered
Dao--Kominers--Thaler version-7 draft. If a>a_1(rho), continuity at
theta=0 gives a rational theta>0 such that

    a/(1+theta) > a_1(rho/(1+theta)).

Thus sparse padding stays strictly inside that theorem's first-order
regime. If the source was also below Johnson, a^2<rho, then the output
is below Johnson too, since a^2/(1+theta)^2 < rho/(1+theta).

An exact numerical parameter example is

    source: rho=1/4, a=49/100;
    theta=1/100;
    output: rho=25/101, a=49/101.

Both rates lie on the high-rate branch (rho>=11-3*sqrt(13)), where
a_1 is the positive root of

    F_rho(a)=(8-rho)*a^2-6*rho*a+rho*(4*rho-5).

The exact certificates are:

| Parameters | F_rho(a) | rho-a^2 |
|---|---:|---:|
| source | 5031/40000 | 99/10000 |
| output | 115008/1030301 | 124/10201 |

Both columns are positive. The constant term of F is negative for
0<rho<1, so its positive argument has F>0 exactly above the positive
root. For the branch condition, (11-rho)^2-117 equals -23/16 and
-14121/10201 respectively, proving rho>11-3*sqrt(13).
These are parameter certificates, not examples of growing lists.

## Consequence for the research target

A linear-size source list above the first-order curve over primes large
enough to avoid saturation would establish a quadratic full-support MCA
lower bound at nearby fixed parameters still above that curve. More
generally a source-list exponent c produces exception exponent c+1.
Therefore a construction of growing lists in this regime would address
both list tightness and exception tightness. The two parameter pairs
need not coincide; this is not a same-rate or same-agreement equivalence.

Conversely, a universal linear full-support exception bound throughout
the open first-order regime would force constant source lists at every
fixed parameter pair in that regime along families with p/N tending to
infinity. This follows by choosing one fixed sufficiently small theta
and applying (2). No converse from constant lists to linear exceptions
is asserted.

For source lengths not divisible by the denominator of theta, take
q=floor(theta*N)+1. The output rate and agreement converge to the
displayed pair. The strict open-regime margin survives rounding. One
can apply a hypothetical uniform upper theorem at a fixed slightly
larger rate cap and slightly smaller agreement threshold, still inside
that regime. This suffices for the stated implication; it does not
silently assert exact parameter equality at every rounded length.

The accompanying check_sparse_padding.py checks the compiler at four
padding sizes over F_23. For every selected bad support it exhausts
all 12167 possible direction polynomials, confirming the required
full-support failure. It separately verifies the exact rational curve
certificates above. These fixtures do not supply the missing asymptotic
list family.

This closes only the parameter-preservation issue in the earlier
comparison. It does not close the principal gap: no growing fixed-gap
source list in this first-order regime has been constructed here.
