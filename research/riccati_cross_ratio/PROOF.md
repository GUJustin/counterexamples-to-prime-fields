# Original Riccati proof (superseded characteristic scope)

The stronger authoritative argument is in CHARACTERISTIC_REFINEMENT.md
and appendix.tex: ordinary lists and fixed-equation MCA now assume only
characteristic zero or p>D, with a separate candidate-count bound at
p=D+1. The narrower proof below remains valid under p>2D.

September 16, 2026: proof reviewed and exact finite checks replayed on the new laptop. Integration status updated September 18, 2026: the strengthened result is now integrated through `appendix.tex` in `paper.tex`; this file retains the original narrower proof. Historical replay receipts are unchanged.

## Setup and source

Let F have characteristic zero or p>2D, with D>=1. Consider polynomial
solutions of degree <=D to one fixed Riccati equation

    a(X) P' = b0(X)+b1(X)P+b2(X)P^2,       a != 0.       (1)

There is no restriction on the X-degrees of a,b0,b1,b2. The classical
constant-cross-ratio parametrization and its gcd form are described in
Gasull, Torregrosa and Zhang, *The number of polynomial solutions of
polynomial Riccati equations* (2016), Lemmas 6--7:
https://arxiv.org/abs/1602.03503 . Their main theorem concerns real or
complex equations and bounds the count using coefficient degrees.
Below we give the characteristic guard, bounded-candidate-degree count,
and agreement consequences needed here. No literature priority is claimed.

## 1. Cross ratios are genuine constants in the stated characteristic

For two solutions, their difference satisfies

    a(P_i-P_j)' = (b1+b2(P_i+P_j))*(P_i-P_j).

Thus the cross ratio of any four distinct solutions has derivative zero.
It is a rational function of degree at most 2D, since its numerator
and denominator are products of two degree-<=D differences. In positive
characteristic a nonconstant rational function with derivative zero has
degree at least p. Hence the cross ratio belongs to F, not merely F(X^p).
It is different from 0,1,infinity, by the distinctness of the solutions.
This is why this note uses p>2D rather than only p>D.

## 2. A collision at a coordinate forces almost all values to coincide

Take M distinct allowed polynomials. For M>=4, suppose two have equal
value v at x, while two others both have values different from v.
Substitute x into their polynomial cross-ratio identity. Both products
become the same nonzero number, forcing the cross ratio to equal one,
a contradiction. Therefore, at every coordinate, either all M values
are distinct, or some value occurs at least M-1 times. For M=3 this
alternative is automatic. No nonsingularity hypothesis is used here.

## 3. Uniform constant ordinary lists

On any n distinct points and for any received word, let M>=3 solutions
each have at least A>D agreements. At a coordinate the number h of
matching candidates belongs to {0,1,M-1,M}, by Section 2. Each of these
four values satisfies

    h <= 1 + 2*binom(h,2)/(M-1).

Sum over the domain and use the pairwise polynomial root bound:

    A*M <= n + 2*binom(M,2)*D/(M-1) = n+M*D.

Consequently

    M <= floor(n/(A-D)).                                (2)

For M=2 the same displayed inequality holds for every possible h;
for M=1 the conclusion is immediate. Hence every ordinary list is
constant-sized at a fixed positive agreement gap, even when all domain
coordinates are zeros of the leading differential coefficient a.
This applies at each fixed challenge to a challenge-dependent Riccati
equation, but does not by itself bound the number of challenge labels.

### Sharpness over prime fields

Fix an integer M>=3 and a prime p congruent to 1 modulo 2M. Put
s=(p-1)/(2M), n=p-1, D=(M-2)s, and A=Ms. Partition the image of
X^s on F_p^* into a_1,...,a_M,b_1,...,b_M. Write

    R(Y)=product_i(Y-a_i), T(Y)=Y^(M-1),
    C_i(Y)=R(Y)/(Y-a_i)-T(Y), P_i(X)=C_i(X^s).

The leading terms cancel, so deg P_i<=D. On the fiber over a_j choose
the received value -T(a_j); on the fiber over b_j choose C_j(b_j).
On a root fiber, exactly M-1 candidates agree: the exceptional candidate
has difference R'(a_j)!=0. On a nonroot fiber, all candidate values are
distinct, since R(b_j)!=0 and the denominators b_j-a_i are distinct.
Consequently every P_i has exactly (M-1)s+s=A agreements, and
M=n/(A-D). Thus (2) is attained, including among all solutions of the
common equation below, since (2) forbids any extra nearby solution.

The functions U_i=R/(Y-a_i) satisfy R U_i'=R' U_i-U_i^2. Translation
U=C+T gives

    R C'=(R'T-T^2-RT')+(R'-2T)C-C^2.

Substitute Y=X^s and multiply its right-hand side by s X^(s-1).
This gives one polynomial Riccati equation for every P_i, with nonzero
quadratic coefficient and p>2D. For each fixed M, primes in this
arithmetic progression give unbounded n, rate (D+1)/n tending to
(M-2)/(2M), and gap (A-D)/n=1/M. The capacity gap measured from the
code dimension D+1 is 1/M-1/n and tends to the same positive value.
The checker verifies nine instances, including (M,p)=(8,97).

## 4. At most D+2 bounded-degree solutions when b2 is nonzero

If there are fewer than three solutions, the claim holds. Choose P0,
write P1-P0=g*u and P2-P0=g*v, with gcd(u,v)=1 and h=deg g. Nonlinearity
implies u,v are linearly independent: proportional differences would,
upon subtraction in (1), force b2=0. All other differences have form

    g*u*v / (c*u+(1-c)*v),

by the constant cross ratio. For c not 0 or 1, a nonconstant denominator
must divide g. Distinct such denominators are coprime, so there are at
most h of them. At most one additional c has constant denominator.
Without this additional solution the count, including P0,P1,P2, is
at most h+3<=D+2. If it exists within degree D, then
deg u=deg v=d>=1 and h+2d<=D; the count is at most h+4<=D+2.

The bound is attained when a is squarefree of degree D+1, b0=0,
b1=a', b2=-1: the solutions are 0 and a/(X-r) for the D+1 roots r
of a. They are distinct, and the same count bound proves completeness.

## 5. Linear full-support MCA for a challenge-independent Riccati equation

Assume b2!=0 and retain the same fixed equation (1) for every received-
line label z. Fix f+zg on n distinct points and A>D; set delta=A-D.
There are at most D+2 candidate polynomials by Section 4.
Here the full agreement support of P at z is S={i:P(x_i)=f_i+z*g_i}.
Call this support bad when no degree-<=D polynomial interpolates g on S.
Indeed, because P already interpolates f+zg there, interpolating g is
equivalent to the existence of two degree-<=D polynomials jointly
explaining f and g on S. If every agreement is persistent, g=0 on S
and this support cannot be bad.

For a candidate P, persistent coordinates satisfy g_i=0 and P(x_i)=f_i.
Call it heavy if it has at least D+delta/2 such coordinates. The heavy
candidates are an ordinary list for the received word f at threshold
D+delta/2. Formula (2), also valid for real thresholds, bounds their
number by 2n/delta. Each contributes at most n bad labels: every
bad full support must contain an accidental agreement at a coordinate
with g_i!=0, and that coordinate determines one z.

A light candidate needs more than delta/2 accidental agreements at
each nearby label. It has at most n accidental coordinate-label
incidences altogether, so it contributes at most 2n/delta nearby labels.
Thus all bad labels number at most

    n*(2n/delta) + (D+2)*2n/delta
      = 2n*(n+D+2)/(A-D).                                (3)

This is O(n) at fixed positive gap, with no bound on the coefficient
degrees and no restriction on singular agreement coordinates. The
nonlinear n/2 family in ../quasilinear_first_order/PROOF.md shows sharp
linear order in a subclass. Affine-linear fixed equations are covered
by the earlier linear-system result, independently of this finite count.

## Remaining scope

For challenge-dependent nonlinear Riccati equations, (2) gives constant
lists at each fixed label, but (3) does not follow: the candidate set
can vary with z, and the actual joint locus can have quadratically many
isolated points. The previous quadratic isolated family is an example
of that algebraic growth. The first-order conjecture for such equations,
and the requested higher-order quadratic proximity-gap construction,
remain open.
