# Affine varying twists: native incidence and residual values

2026-09-19. Necessary conditions only; no constructed common received line.

Let D be n distinct prime-field points, Lambda its monic locator, and
G_i monic divisors of Lambda with degree at most e<n. Suppose

    G_i^p - A_i G_i = Lambda F_i^p,
    A_i=A_0+t_i A_1,

for M distinct parameters t_i in a containing field. Put
Q_i=Lambda/G_i and P_i=Q_i F_i. No degree bound on A_i is imposed.
Define the active coordinate set

    R={x in D : (A_0(x),A_1(x)) != (1,0)}.

At any x outside the root set of G_i, G_i(x) is a nonzero prime-field
element. The identity forces A_i(x)=1. For each x in R, the equation
A_0(x)+t A_1(x)=1 has at most one solution t. Thus x belongs to the
root set of all but at most one G_i. Counting incidences gives

    M |R| - |R| <= sum_i deg G_i <= M e,
    M (|R|-e) <= |R|.

In particular if M>n, then |R|<=e. Moreover at most |R| indices can
omit any point of R: take the union of the at-most-one exceptional index
at each point. All remaining G_i have the entire set R as common roots.
This conclusion allows R to be empty; that case imposes no common root.

The exact polynomial identity can also be written

    P_i^p + A_i Q_i^(p-1) = Lambda^(p-1).

At x in D outside the roots of G_i, P_i(x)=0. At a root of G_i,
Q_i(x) is a nonzero prime-field element, so

    P_i(x)^p = -A_i(x).

Consequently on D outside R every residual takes only the values 0 and
-1, independently of the containing field. If P_i is neither the
constant 0 nor the constant -1, the nonzero polynomial P_i(P_i+1)
vanishes on D outside R, and therefore

    2 deg P_i >= n-|R|.

These observations provide a concrete further requirement for an affine
twist construction with more than n parameters: a large subfamily has
a common active root set and binary-valued residuals elsewhere. They do
not rule out that requirement. In particular A_i congruent to 1 modulo
Lambda gives R empty and remains possible at the level of this argument.
The common received-head condition, distinct challenge labels, and far
source bounds must still be proved separately.
