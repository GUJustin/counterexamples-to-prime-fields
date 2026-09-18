# Subgroup reduction: a quarter-rate obstruction and an exact remaining criterion

This concerns literal restriction of the classified native Dickson
polynomials to a multiplicative subgroup, followed by their unique
polynomial reduction modulo X^n-1. It is not Reynolds projection,
common-factor shortening, or a statement about arbitrary new sources.
No parameter search was performed.

## Normalization and exact parameter criterion

Let p=4k+1, e=2k+1=(p+1)/2, and let t=a^2 be a nonzero square in F_p.
Write

    G_t(X)=sum_(j=0)^k binom(e,2j+1)t^(k-j)X^j,
    P_t(X)=G_t(X)-X^k.

The coefficient of X^k is one, so P_t has degree at most k-1. These
are the parameters and normalization of the classified bank. The
primitive binomial identities, with a in F_p, give

    2 J_a G_t=a(1+X^(2k)),
    J_a^2+XG_t^2=t+X^(2k+1).

Eliminating J_a proves the exact polynomial identity

    t(1+X^(2k))^2
       =4G_t^2[t+X^(2k+1)-XG_t^2].                 (1)

Let n divide p-1. For 0<=r<n define

    F_r(T)=sum_(h>=0:r+hn<k)
              binom(e,2(r+hn)+1) T^h.

The coefficient of X^r in the reduction of P_t modulo X^n-1 is
exactly t^(k-r) F_r(t^(-n)). Thus a reduction of degree <d is
equivalent to a common nonzero root T=t^(-n) of all F_r with d<=r<n,
with the additional condition that T arises from a nonzero square t.
An empty coefficient sum means the zero polynomial, not an extra
condition. This is an exact algebraic criterion, not evidence that
the common roots exist.

One good parameter can generate a growing bank without solving for many
unrelated roots. Put g=gcd(n,k). For beta in mu_g,

    P_(t beta)(X)=P_t(X/beta).

Here beta^k=1, and beta is a square since g divides k. The native
received word W=(1+X^(2k))/2-X^k is invariant under this permutation
of mu_n. Hence every such parameter has the same reduced degree and
agreement count. If the nonzero exponents of one reduced polynomial
are E, its distinct orbit size is

    g/gcd(g,E),

with size one for a constant polynomial. Thus even one nonconstant
low-degree reduction with a small stabilizer and sufficient surplus
would provide a concrete source candidate. Exact nearestness against
all low-degree polynomials would still need a separate certificate.

## The odd-index 1 mod 4 branch is impossible at quarter rate

**Proposition.** Suppose n=4q divides p-1 and the index
r=(p-1)/n is congruent to one modulo four. If r>1, then for every
nonzero square t the reduced polynomial P_t has degree at least q.
Thus the degree-<n/4 reduced bank contains only the zero-parameter
candidate, if that candidate is included. No agreement argument is
needed for this obstruction.

**Proof.** Here k mod n=q. Suppose a reduction P has degree <q, and
put G=X^q+P, a monic polynomial of degree q. Reduce (1) modulo
X^(4q)-1. Since 2k mod n=2q, the polynomial

    F=t(1+X^(2q))^2
        -4G^2[t+X^(2q+1)-XG^2]

is divisible by X^(4q)-1. The degree-(4q+1) terms cancel because
G is monic. More explicitly G^2-X^(2q) has degree at most 2q-1,
so deg F<=4q. Therefore F=C(X^(4q)-1) for a constant C.
In particular G^2 divides

    (t-C)X^(4q)+2tX^(2q)+(t+C).                 (2)

Assume C!=0. As a polynomial in U=X^(2q), (2) has discriminant
4C^2. Since p>n+1>2q and t!=0, every nonzero root of (2) is
simple, including the degree-drop case C=t. It can have a multiple
zero only when C=-t, when (2)=2t X^(2q)(X^(2q)+1).
Because the monic degree-q polynomial G has its square dividing (2),
this last case forces G=X^q. But then

    F=t(X^(2q)-1)^2,

which is not -t(X^(4q)-1). Thus C!=0 is impossible.

We now have F=0. Regarding this as a quadratic equation in Z=G^2,

    4X Z^2-4(t+X^(2q+1))Z+t(1+X^(2q))^2=0,

its discriminant is

    16[(t+X^(2q+1))^2-Xt(1+X^(2q))^2]
      =16(t-X)(t-X^(4q+1)).                    (3)

A rational root Z would make this discriminant a square in k(X),
where k is an algebraic closure. But r>1 gives p>4q+1. The
polynomial X^(4q+1)-t therefore has 4q+1 distinct nonzero roots.
Multiplication by t-X can change the parity of at most one root
multiplicity, leaving at least 4q simple roots. Expression (3) is
not a square, a contradiction. This proves the proposition.

This argument also identifies the native-characteristic escape:
when n=p-1, X^(n+1)-t=X^p-t=(X-t)^p for t in F_p, so the last
squarefreeness assertion fails exactly as it must. No characteristic-
zero lifting claim or distributional heuristic was used.

## Other index classes and remaining target

If the index is divisible by four, then X^k=1 on mu_n, so the native
received word is identically zero. A nonzero reduced polynomial of
degree <d cannot have d or more agreements with it. Only the single
zero polynomial can have positive agreement surplus over the degree
budget; duplicate parameter representations do not enlarge a list.

If the index is two modulo four, all coordinates are squares and
k mod n=n/2. The original full-domain 3/8 agreement count cannot be
imported unchanged. If the index is three modulo four, k mod n=3n/4,
so the degree bound in the proposition's norm argument no longer
holds. These branches are not excluded by the quarter-rate proposition.
Coordinate inversion alone does not preserve the low-degree condition,
so it cannot silently transfer the proof to index three modulo four.

The strongest remaining concrete test is therefore the simultaneous
Fourier coefficient criterion above in the index-three branch, followed
by an exact agreement and nearestness certificate. No such parameter
has been exhibited here, and no new prime-field lower bound is claimed.
