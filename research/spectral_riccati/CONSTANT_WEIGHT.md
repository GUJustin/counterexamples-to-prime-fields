# A spectral Riccati family has at most three nonzero labels

September 16, 2026. Self-reviewed deduction with exhaustive finite checks.
This closes one proposed construction; it is not a general nonlinear MCA
bound and is not a quadratic lower bound.

## Statement

Let D>=1, and work in characteristic zero or characteristic p>D+1.
Let R be any monic polynomial of degree D+1. A nonzero polynomial P of
degree at most D satisfying

    R P' - R' P + P^2 - z P = 0

necessarily has degree D and leading coefficient one. If z=0, the
solutions over the algebraic closure are precisely R/(X-a), for roots a
of R. If z!=0, then D>=2 and

    P=(X-a)^D,
    R=(X-a)^(D+1)+c(X-a)^D+[z/(D-1)](X-a)

for some a,c. In particular there are at most three nonzero labels when
D=2, at most two when D=3, and at most one when D>=4. These are bounds
on solutions as well as on labels. The zero polynomial, which solves the
equation at every label, is deliberately excluded from this statement.

## Proof

Write d=deg P. If d<D, the term RP'-R'P has degree D+d and nonzero
leading coefficient (d-D-1)lc(P), whereas P^2 and zP have smaller degree.
This is impossible under the characteristic hypothesis. If d=D, the
coefficient at degree 2D is lc(P)^2-lc(P), so P is monic.

At a root a of P of multiplicity e, if R(a)!=0, then RP' has order e-1,
strictly less than every other term. Since 1<=e<=D<p, its leading local
coefficient is nonzero. Thus every root of P is a root of R. If r is
the number of distinct roots of P and h=deg gcd(R,P), then h>=r>=1.

When z=0, the equation says (R/P)'=1. The rational function R/P-X
has degree at most D (leading terms cancel), strictly less than p in
positive characteristic. A nonconstant rational function with zero
derivative in characteristic p has degree divisible by p; hence R/P-X
is constant in either characteristic. This gives the stated solutions.

Suppose z!=0 and put U=(X-R/P)/z. Direct differentiation gives U'=1/P.
The numerator XP-R has degree at most D and has gcd(R,P) as a factor.
After cancellation the rational map U therefore has degree at most D-h
and is finite at infinity. For D=1 this would make U constant, impossible.

For D>=2 let k be the order of the first nonconstant term of U at
infinity. This is positive and at most deg U<=D-h<p. Differentiation
does not kill this term, so U'=1/P~X^(-D) forces k=D-1. Consequently

    D-1 <= deg U <= D-h,

so h=r=1. Write P=(X-a)^D; its root a is a simple root of R.
The displayed formula for R follows by
integrating (R/P)'=1-z/P. To justify the integration also in finite
characteristic, subtract its claimed primitive: the difference has
zero derivative and denominator dividing (X-a)^(D-1), numerator degree
at most D-1. Its rational degree is less than p, so it is constant.

For D=2 every solution root is among the three roots of R. For D=3 the
formula implies R''(a)=0, giving at most two roots. For D>=4, it implies
that a is a root of R'' of multiplicity at least D-2. The nonzero
polynomial R'' has degree D-1; two such roots would require
2(D-2)>D-1. Thus at most one exists.

## A bounded-degree extension, and its limitation

Replace zP by zB(X)P, with B nonzero of degree b<=D-2. Degree comparison
and the local root argument are unchanged. For z!=0 the same U satisfies
U'=B/P, so the first nonconstant term at infinity has order D-b-1.
It follows that

    deg gcd(R,P) <= b+1, and hence r <= b+1.

If b=D-1 there is no nonzero-label solution: U is finite at infinity,
whereas U'=B/P would have a simple pole in its Laurent expansion at
infinity (a term proportional to X^-1), which a rational derivative
cannot have. This refers to the derivative with respect to X.

When b grows with D, the bound on r grows too. Even for fixed b>0 this
does not bound the number of labels or establish full MCA: supports and
multiplicities can vary. No conclusion about general challenge-dependent
Riccati equations follows.

## Verification evidence

`verify_constant.py` checks 32 split-squarefree fixtures, including
planted R=X^(D+1)-X through D=8 and random root sets. It tests all 70,322
monic candidates supported on the roots of R. In the small cases it also
tests all 59,740 degree-bounded polynomials, including nonmonic and
lower-degree ones, to check the preliminary reductions independently.
All equations, zero-label classifications, nonzero-label formulas, and
counts pass. Twenty nonzero solutions were encountered.

The fixture R=X(X-1)(X-2)(X-3) over F_11 has two distinct nonzero labels
at D=3, attaining that bound. The full JSON records all solutions.
An additional exhaustive check covers all 775 monic R over F_5 of degrees
two through four, testing 81,375 monic candidates. This includes repeated
roots and nonsplit R; all 975 solutions satisfy the classification.
The standalone replay ran sequentially under a 384 MiB cap; its resource
report records elapsed time and sampled RSS. Finite checks support the stated
identities and catch implementation mistakes; the proof supplies the
general conclusion, including nonsplit R over the base field.
