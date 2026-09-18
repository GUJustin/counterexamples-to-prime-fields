# Elliptic Frobenius halving: an exact bounded construction test

No new lower construction results from this test. This is distinct from fixed
Legendre duplication: the endomorphism below has degree growing with p.

Let E/F_p have full rational two-torsion, p odd, and Frobenius pi. Since pi-1
annihilates E[2], it factors through [2]: pi-1=[2]alpha. Then

deg alpha=#E(F_p)/4, and alpha maps E(F_p) into E[2].

This suggests an elliptic analogue of the finite branch buckets in Dickson's
construction. Two exact tests expose missing ingredients.

## 1. Kernel-coset locators

K=ker alpha consists of rational points: alpha(T)=0 implies pi(T)=T.
The four rational cosets modulo K exhaust E(F_p). Thus translating by rational
points yields only four distinct kernel cosets and cannot supply a growing bank.

If Q has rational x coordinate but lies on the quadratic twist, pi(Q)=-Q,
consider the proposed locator with roots x(Q+T), T in K. For a non-two-torsion
Q, such a root lies in F_p only if

    pi(Q+T)=-Q+T=+(Q+T) or -(Q+T).

The first equality would require 2Q=0, excluded. The second requires 2T=0.
Thus at most |K intersect E[2]|<=4 of these roots lie in the prime field.
The full locator has rational coefficients (negation permutes K), but almost
none of its roots need lie in the prime field. Coefficient descent is not
split-root descent. This defeats this particular shifted-kernel locator bank.

## 2. Four branch values cannot share a Möbius normalization

In Legendre coordinates E: y^2=x(x-1)(x-lambda), the x-coordinates in the
two-torsion orbit of a point of x-coordinate a are

    a, lambda/a, (a-lambda)/(a-1), lambda(a-1)/(a-lambda).

Away from poles and coincidences, their ordered cross-ratio is

    C(a)=lambda*(a^2-2a+lambda)^2/(a^2-2lambda*a+lambda)^2.

Direct symbolic differentiation gives

    C'(a)=-4lambda(lambda-1)(a^2-lambda)(a^2-2a+lambda)
              /(a^2-2lambda*a+lambda)^3.

For a nonsingular Legendre parameter and odd characteristic this is not
identically zero. A fixed cross-ratio has at most four parameter solutions,
counting the polynomial degree before exceptional poles are removed. Therefore
no growing family can send all four ordered values to one fixed quadruple by
parameter-dependent Möbius maps. Allowing permutation only multiplies this
bound by a constant.

This calculation was independently checked by exact SymPy simplification of
the displayed four rational values; no numerical field scan was used.

Three branch values can always be normalized, but this leaves one moving value
and provides no automatic polynomial representative of the desired degree.
Moreover the natural three-of-four bucket heuristic on the rational-x half of
the domain is 3/8, precisely the audited Dickson family's transition, not the
DKT first-order threshold a1(1/4) approximately .46879. It cannot be advertised
as progress toward that threshold.

## Exact remaining construction problem

An elliptic approach would need a new COMMON polynomial normalization retaining
small message degree while either obtaining useful matches on the twist half
of the domain or making the fourth branch contribute without losing the first
three. Neither the shifted kernel locator nor Möbius normalization supplies it.
These tests do not rule out all elliptic constructions, higher-genus sources,
or parameter-dependent coordinate changes with separately verified degree and
agreement budgets. They do justify stopping this particular naive analogue.

## Comparison to the actual target

Cached DKT eprint2026/2056, Theorem1.1, bounds list size O_rho(n/eta1^2) and full
line-MCA exceptions O_rho(n^2/eta1^4) above a1(rho). Its equation(31) gives

    a1(rho)=[3rho+2sqrt(rho(5-rho)(2-rho))]/(8-rho)

on the upper branch, including rho=1/4. A lower list source at3/8 therefore
cannot establish first-order tightness at quarter rate. The existing prime-field
near-complete line source has shrinking gaps, and the fixed-gap quadratic
ordinary-CA source uses a quadratic extension. Neither distinction is removed
by the elliptic calculation above.
