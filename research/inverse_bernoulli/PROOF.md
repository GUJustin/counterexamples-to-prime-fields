# Inverse Bernoulli equations in the critical characteristic range

September 16, 2026. Twice self-reviewed proof; no independent coauthor
review or novelty claim. The exact checker passed on 164,803 monic
polynomials, six sharpness fixtures, and four exceptional-characteristic
controls. These finite checks supplement the proof.

## Statement

Let E be algebraically closed of characteristic p, let s>=2, and assume
p>max(D,s+1). For any nonzero A(X), the equation

    P^(s-1) P' = A,  deg P <= D

has at most 2s polynomial solutions. This bound includes the range
p<=sD, where integrating the equation leaves a nonconstant p-th power.
In characteristic zero, or if p>sD, there are at most s solutions.
Over any subfield the same upper bounds hold.

The cutoff p>s+1 matters: if s=p-1 and D=p-1, then
P_a=(X^p-X)/(X-a), a in F_p, all satisfy
P_a^(p-2) P_a'=-(X^p-X)^(p-2). Multiplying by any nonzero F_p
scalar gives p(p-1) solutions. The jet degree s grows with p here.

## Reduction to monic solutions of one degree

If A is nonzero, every solution is nonconstant. Its degree d<p gives
deg A=sd-1 and leading coefficient d*a^s, where a is its leading
coefficient. All solutions thus have the same d, and the possible
leading coefficients differ by s-th roots of unity. Divide through
by one chosen leading coefficient and count monic solutions first.
It suffices to prove there are at most two monic solutions.

For any two monic solutions P,Q,

    (P^s-Q^s)'=0,  hence P^s-Q^s=C(X)^p,
    deg C <= floor((sd-1)/p) <= s-1.

If C is a nonzero constant, the factorization into P-zeta Q forces
every factor to be constant, contradicting d>0. If C=0, monicity
gives P=Q. The characteristic-zero / p>sd conclusion follows too.

## s>=3: every nontrivial pair is rigid

Cancel G=gcd(P,Q), and put U=P/G, V=Q/G. These are coprime monic
polynomials of the same degree h>=1, with h<=d<p. The rational map
U/V has degree h and is separable. The preimages of the s distinct
s-th roots of unity belong to the roots of C together with infinity.
There are at most s such points, and each of the s disjoint fibers
is nonempty. Therefore there are exactly s points: every such fiber
consists of a single point, totally ramified of degree h.

Here is an elementary ramification count. Make a generic fractional
linear change of the X coordinate so that all these s points are
finite and the new infinity maps to none of the s values. The new
coprime numerator and denominator have degree h. At each of the s
points the derivative numerator U'V-UV' has a zero of order h-1;
h<p ensures this order calculation. Its degree is at most 2h-2.
Thus s(h-1)<=2h-2, and s>=3 forces h=1.

Consequently U=X-u, V=X-v with u!=v. The polynomial
S=U^s-V^s has s-1 distinct roots, all finite, and none is u or v.
The polynomial C has exactly those s-1 distinct roots and degree s-1.
Comparing valuations in G^s S=C^p shows

    p=sg+1,  G=S_0^g,  d=(s-1)g+1,

where S_0 is the monic normalization of S and g=(p-1)/s. There are
no other roots of G. Since p>s+1, g>=2.

Direct differentiation, using sg=-1 in the field, gives

    A = nonzero_constant * (UV)^(s-1) * S_0^(p-2).

Any other monic solution T has a root of multiplicity m only where
A has multiplicity sm-1: m<p makes the leading derivative nonzero.
Its available roots therefore have multiplicity g at the s-1 roots
of S_0, or multiplicity one at u and v. If it chooses t of the former
and k of the latter, its degree gives

    tg+k=(s-1)g+1,  0<=t<=s-1,  0<=k<=2.

Because g>=2, necessarily t=s-1 and k=1. Thus T is P or Q.
This also proves that if p is not 1 modulo s, a nontrivial monic pair
is impossible. Conversely the displayed U,V construction attains two
monic solutions whenever p=sg+1 with g>=2 and D>=(s-1)g+1.

## s=2

For a distinct monic pair, P^2-Q^2=c(X-a)^p. The monic sum P+Q
has degree d and leading coefficient 2; the difference has degree
p-d. Both factors are powers of X-a. Hence

    P=(X-a)^d+v(X-a)^(p-d),
    Q=(X-a)^d-v(X-a)^(p-d),  v!=0.

Necessarily d>p/2. If p-d<=d-2, the coefficient of X^(d-1) in
P fixes a, and then fixes v. If p-d=d-1, p=2d-1>=5 and a is a
root of P of multiplicity d-1>d/2, so again a is unique. Thus each
monic P has at most one distinct partner Q. This proves the bound.
The displayed pair attains it (with the two signs of each polynomial).

## Consequence for full-support MCA

Every fixed candidate P has at most n genuinely bad labels on a
received line f+zg: a bad full support must include a coordinate with
g(x)!=0, which fixes z; otherwise (P,0) explains the support. Therefore
the nonzero-A family has at most 2sn bad labels, at any threshold.

If A=0, the degree guard d<p makes all solutions constants. Each
coordinate gives a line c=f(x)+zg(x) in the (z,c) plane. A bad support
of size at least A_agree must contain at least two distinct line
equations (otherwise constant F,G explain it). It contains at least
A_agree-1 pairs of coordinates with different line equations. Every
such pair belongs to at most one intersection point. Selecting one
candidate per bad label therefore gives at most

    binom(n,2)/(A_agree-1)

bad labels, when A_agree>=2. This is O(n) at fixed positive agreement.

Thus this nonlinear first-order family cannot supply quadratic MCA,
including the near-p characteristic regime not covered by the general
bounded-root argument. It does not establish the general first-order
conjecture or constrain arbitrary higher-order equations.
