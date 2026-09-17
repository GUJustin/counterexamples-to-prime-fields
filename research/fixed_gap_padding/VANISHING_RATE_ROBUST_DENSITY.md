# Robust near-unit density when the rate tends to zero

September 17. New deduction; pending independent finite audit and manuscript
integration. This does NOT answer the fixed positive rate question.

Fix positive integers K,s. Put u=K-s(s-1)/2 and choose a>1 with

    1+c2*K/(s+1) < a < u+1,

where c2>=1 is the proposed list exponent constant. Such parameters exist
for every fixed c2: choose s+1>c2 and then K sufficiently large. For every
large prime p take n=floor(p^(1/a)), a core of N~alpha*n integer points,
0<alpha<1 fixed, and all anchored supports of size t=K+s+1. The anchor
is a further fixed point, removed after division as in the main construction.

There are Theta(N^(K+s)) anchored supports. For fixed t and s, the jth
binomial-moment range is O(N^j), not O(N^(j+1)): each support contains
only t points. Thus a moment class has

    L=Omega(N^(K+s-s(s+1)/2))=Omega(n^u).

After division, all candidates have degree<K and exactly A-1 core
agreements, where A=K+s+1. The global received polynomial has degree A-1.
The far-padding lemma gives, with q=n-N, R=p-N, U=p-1,

    M >= L*R/(R+(K-1)*(L-1)),
    J/U >= 1-exp(-q*M/U).

Since q=Theta(n), the exponent grows at least as a positive constant
multiple of min(n,n^(u+1-a)), so J/p tends to one. The zero word is
exactly 1/n=eta/(s+1) outside, where eta=(s+1)/n and rho=K/n->0.
No correlated agreement is possible at A.

Strict Elias follows from a(s+1)>K+s+1: the logarithm of its finite
entropy inequality has leading coefficient [a(s+1)-(K+s+1)] log n.
The numerical prescription satisfies

    c1*n*2^(c2*H2(K/n)/eta)=n^(1+c2*K/(s+1)+o(1))=o(p).

Thus for every fixed c1,c2 this supplies near-unit density with a fixed
positive fraction of eta as far separation, but at vanishing rate.
Field size is polynomial in n, with exponent a depending on the constants.

## Particularly simple case c1=c2=1

Take K=2,s=1,u=2,a=5/2, n=floor(p^(2/5)), N=floor(2n/3).
Triples from {1,...,N} have sums between6 and3N-3, hence one class has
L>=ceil(binom(N,3)/(3N-8)). For its common sum S, use w=X^3-SX^2.
For a triple {a,b,c}, P=-(ab+ac+bc)X+abc has degree<2 and
w-P=(X-a)(X-b)(X-c). Hence the finite mechanism is transparent.
The radius is 1-4/n, rho=eta=2/n, and zero is eta/2 outside.

The simple collision estimate gives qM/p=Omega(p^(1/5)), so nearby
fraction is at least 1-exp(-Omega(p^(1/5))) up to the missing zero label.
The numerical prescription is at most (3/2)n², because
(1-2/n)^(-(n-2)/2)<e<3. Thus its fraction is O(p^(-1/5)).
A convenient exact sufficient Elias check is
p²*4^4 > 3^4*n^4, using (1+4/(n-4))^(n-4)<e^4<3^4.
These avoid constructing integers with n digits in a finite certificate.

## Stronger conclusion: exactly one far parameter

The same bound actually gives ALL nonzero parameters nearby for sufficiently
large p. The expected number of uncovered nonzero labels is at most
U*exp(-qM/U). Here qM/U grows as a positive power of n, whereas log p=O(log n).
Thus the expectation is <1 eventually, and some domain/direction has zero
uncovered nonzero labels. Parameterzero remains far by the degree bound.
Consequently the line has exactly p-1 nearby parameters, not merely density
tending to one. This strengthens both the general c1,c2 construction and
the K2 case. Fixed positive rate is still NOT addressed.

Exact finite replay has already passed. K2 case at M31 n5404 gives nearby
fraction>0.45364109 versus prescription<2^-5. M61 n22137669 gives missing
fraction<2^-55 versus prescription<2^-11. M127 n1960305596233800 and M521
have a certified count J=p-1: a 96-term positive binomial sum makes the
expected uncovered count <1. All are strict Elias, far eta/2, n=o(p).
No directions or all list members were enumerated at these huge sizes;
these are exact existence certificates from the proved averaging lemma.
