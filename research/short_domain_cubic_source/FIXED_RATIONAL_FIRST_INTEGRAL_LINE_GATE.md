# Fixed rational first integrals cannot supply superlinear full-support MCA

Status: independently checked by root against the primary nonsingular-agreement theorem; direct corollary, with an
explicit reduction below. This is a scope clarification/application, not a new
reconstruction technique or a claim about all challenge-dependent first integrals.

## Fixed differential equation

Let D>=1 and B>=1. Let Q(X,u,v)=a(X,u)v+b(X,u) be nonzero, with total (u,v) degree at most B,
and primitive in X: the gcd of its coefficients as polynomials in (u,v) is 1.
Let k have characteristic zero or p>D. Fix n distinct evaluation points and a
received line f+zg having FULL SUPPORT g_x!=0 at every coordinate. Fix D<A<=n.
Use the full-support bad-pair definition from the paper: a degree<=D solution
P with at least A matches is bad when no degree<=D polynomial agrees with g on
its entire agreement support.

Put L=ceil(A/2), tau=max(0,2D-3), T0=1+tau(B-1), K=B*T0. Then the number of
bad labels admitting an actual solution Q(X,P,P')=0 is at most

    (n/L)[B*K+B*T0*(n-D)/(A-D)+B*n]
        + B*n/(A-L+1).                                  (1)

In particular this is O_{B,eta}(n) whenever A-D>=eta*n with eta>0 fixed.
There is NO additional Hermite-Johnson threshold in this linear-derivative case.

Proof: at a coordinate x where a(x,u) is nonzero, singular agreement forces

a(x,f_x+zg_x)=0,

at at most B labels. If a(x,u) vanishes identically, primitivity implies
b(x,u) is nonzero, and ANY actual agreement forces b(x,f_x+zg_x)=0, also at
at most B labels. The invertible affine substitution uses g_x!=0. Summed over
coordinates, all singular agreement coordinate-label incidences are at most B*n.
Labels with fewer than L regular agreements but at least A total agreements
therefore number at most B*n/(A-L+1). The remaining labels are bounded by
Theorem nonsingular-agreement-mca in research/quasilinear_first_order/appendix.tex,
with challenge degree H=0 and q=B, giving exactly the first term of (1).

This also explains the Hermite theorem's hypotheses: after X-content removal,
the ordinary core is empty. For an equation linear in v, the persistent
quadratic jet core is empty too. Thus its signed margin is A>=epsilon*n,
not A>=sqrt(D*n/2)+epsilon*n; the latter is only a convenient general-quadratic
sufficient condition.

## Any bounded-degree fixed rational first integral

Let R(X,u)=N(X,u)/T(X,u) be a rational function of positive degree in u at most b,
with N,T in k[X,u] coprime over k(X). Assume characteristic zero or
p>max(D,b). Consider all polynomial sections P of degree<=D satisfying

    N(X,P)=c*T(X,P)

for SOME constant c, which need not equal the received-line challenge z.
The entire section bank satisfies the single challenge-independent equation

    Q0=(N_u*T-N*T_u)v + (N_X*T-N*T_X)=0.                  (2)

The coefficient of v is nonzero: a rational map of positive degree less than p
cannot have zero derivative in u. Equation (2) has total jet degree at most 2b.
Divide Q0 by its nonzero X-content to obtain a primitive polynomial Q. This
does not lose ANY section, including its agreements at roots of that content:
Q0(X,P,P')=h(X)Q(X,P,P') is a polynomial identity and k[X] is an integral domain,
so Q(X,P,P') is identically zero. No pointwise division or exceptional labels
are required. Polynomial denominators in X can be cleared before this step.
Apply (1) with B=2b. Therefore the whole fixed rational-first-integral bank has
only O_{b,eta}(n) bad labels on a full-support received line at ANY fixed agreement
gap A-D>=eta*n, in characteristic zero or p>max(D,b).

At rate 1/4 the DKT first-order threshold approximately .46879 has a positive
capacity gap, so this corollary applies there, and even below that threshold.
It concerns LINE exceptions, not the size of an individual received-word list.
It does not disprove the existence of Omega(n) lists at the first-order threshold.

## What a lower construction must change

A superlinear fixed-gap full-support MCA construction cannot be obtained merely
by increasing the fixed value degree of a challenge-independent rational first
integral while keeping that degree bounded. It must leave at least one stated
hypothesis: for example, use genuinely challenge-dependent equations, allow jet
complexity to grow with n, or treat a received direction without full support.
This does not forbid a challenge-dependent compiler of a fixed section bank:
the compiled candidates may cease to solve the same fixed differential equation.
In particular no contradiction with the existing quadratic-extension compiler
is asserted.
