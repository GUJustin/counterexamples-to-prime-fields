# A boundary-characteristic family for every prime

Let p be any prime, D=p-1, and a=X^p-X. Over any extension field of
F_p, the Riccati equation

    a P' = -P-P^2,   degree P <= p-1,

has exactly p+2 solutions: 0, -1, and a/(X-r) for r in F_p.
Consequently the D+2 count cannot extend to p=D+1 even for arbitrarily
large primes. This does not improve the proved universal upper bound 2p.

At every r in F_p the equation forces P(r) in {0,-1}. Since deg P<p,
these values determine P, even over extension fields. Write S for the
set of coordinates with value -1 and f=product_(r in S)(X-r).
The Lagrange basis gives P=a f'/f: a/(X-r) is -1 at r and zero at
the other p-1 prime-field coordinates. Direct differentiation gives

    a P' - a'P + P^2 = a^2 f''/f.

Here a'=-1, so the equation is equivalent to f''=0. Since deg f<=p,
this means f=c0+c1 X+cp X^p. A nonempty proper S has degree strictly
between 0 and p, and its monic f must therefore have degree 1.
Thus S is empty, a singleton, or all of F_p. These choices yield
exactly 1+p+1 distinct solutions.

The exhaustive scan in scan.cpp is a separate experiment concerning
the maximum over all nonlinear Riccati equations at small p and D.
It does not establish an upper bound in arbitrary characteristic.
For each monic nonzero U and every V distinct from 0,U, it groups
the reduced rational functions

    gamma=(V' U-U' V)/(U V(V-U)).

For gamma!=0, each group is precisely the additional solutions of
P'=(U'/U-gamma U)P+gamma P^2 that lie in the degree range. Conversely,
translation by one solution and scalar normalization of a second
reduce every family of at least three solutions to one enumerated
group. Thus the maximum over these groups plus {0,U} is exhaustive
over equations with at least three solutions over the stated prime
field. It makes no assertion about extension-field solutions.
