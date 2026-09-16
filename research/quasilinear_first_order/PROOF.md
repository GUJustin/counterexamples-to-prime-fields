# First-order equations with a value-independent separant

September 16, 2026. Proof self-reviewed twice; finite checks passed.
This is a restricted first-order linear-MCA theorem, not the general conjecture.
The stronger local argument in REGULAR_AGREEMENTS.md supersedes this
proof as the main result and also covers implicit first-order equations.

## Statement

Let F have characteristic zero or p>D, where D>=1. Consider

    Q(X,z,u,v) = R(X,z)v - A(X,z,u),

with R nonzero and deg_u A>=2 over F(X,z). Suppose Q has total jet degree
at most B and z-degree at most H. Put r=deg_X R, and define

    tau=max(0,2D-3), b=1+tau(B-1),
    K=H+B*(b+tau*H), q=B+H.

On n distinct domain points, fix a received line f+zg and an integer
agreement threshold T>max(D,r). A bad pair (z,P) is a solution with
deg P<=D whose full agreement support S has size at least T, but admits
no degree-<=D polynomial agreeing with g on all of S. Equivalently no
pair of degree-<=D polynomials explains f and g coefficientwise on S.
Count distinct labels z, not pairs. The proposed bound is

    #bad labels <= H + q*K*((n-D)/(T-D) + 3*n/(T-r))
                     + 2*n*n/(T-r).                         (1)

This is O(n) at fixed B,H and fixed positive lower bounds on
(T-D)/n and (T-r)/n. In particular it applies when r<=D+O(1) at a
fixed positive capacity gap. There is no claim here when the separant
depends on P, or when its degree r reaches the agreement threshold.

At each fixed z with R(X,z) nonzero, the ordinary list size is at most
floor((n-r)/(T-r)); this auxiliary bound does not require nonlinear A.

## 1. A value at a nonsingular coordinate determines a polynomial solution

If P1 and P2 are distinct solutions at the same z, their difference
Delta satisfies R Delta'=Delta*C(X), because A(X,z,P1)-A(X,z,P2)
is divisible by Delta. At a root x of Delta with R(x,z)!=0, write
m=ord_x Delta. Then 1<=m<=D<p, so the left side has vanishing order
m-1 and the right side at least m, a contradiction. In characteristic
zero the same argument applies. Thus two distinct solutions cannot
share a value at a nonsingular coordinate.

If r_z domain points are zeros of R(X,z), agreement supports of distinct
candidates are disjoint on the other n-r_z points. Each has at least
T-r_z such agreements. Hence the list has at most
(n-r_z)/(T-r_z) <= (n-r)/(T-r) members.

## 2. Every actual regular component has dimension at most one

Work over an algebraic closure. At a generic fixed z, a positive-
dimensional bounded-degree polynomial-solution family would contain
an affine coefficient curve. Complete and normalize that curve.
At some boundary point a coefficient of P must have a pole; let M>0
be the largest pole order. The residue polynomial of pi^M P is nonzero.
Write a_b(X) for the nonzero highest coefficient of A in u, b>=2.
Then a_b P^b has parameter pole order bM, and every lower power of P
has smaller pole order. The left side R P' has pole order at most M.
This is impossible. Thus the generic challenge fiber is zero-dimensional.

At every fixed challenge where R is nonzero, Taylor reconstruction at
a point where R does not vanish determines the solution by its value.
The solution locus has dimension at most one there. Consequently no
vertical regular surface exists either. All components of the closure
of the actual regular joint locus have dimension zero or one.
Theorem H.1 of the paper bounds the sum J1 of their curve degrees by qK.
Challenges with R(X,z) identically zero number at most H, by any one
nonzero X-coefficient of R; account for these separately throughout.

## 3. Count isolated nearby points using agreeing Taylor centers

Fix a domain coordinate x and impose u=f_x+z*g_x. On R(x,z)!=0,
the initial equation is the irreducible rational curve

    v=A(x,z,f_x+z*g_x)/R(x,z).

Its plane closure has degree at most q. The exact Taylor-reconstruction
residuals have total degree at most K, by Theorem H.1; substituting the
affine expression for u preserves this bound. If every residual vanishes
on that curve, reconstruction gives an actual solution curve, so none
of its points is an isolated component of the actual solution locus.
Otherwise one nonzero residual cuts at most qK points by Bezout.
Thus at most qK isolated solution points agree at this coordinate while
R(x,z)!=0. Each nearby isolated point has at least T-r such coordinates.
Double counting bounds their number by n*qK/(T-r).

## 4. Nonaffine curves

A curve other than a graph P=F+zG has at most D persistent agreement
coordinates. Otherwise interpolation at D+1 points would make it that
graph, or would turn a vertical curve into a point. Each nonpersistent
agreement hyperplane intersects the curve in at most its degree many
points. Corollary H.2 therefore gives at most

    J1*(n-D)/(T-D)

nearby pairs on all these curves, also bounding their bad labels.

## 5. Affine graphs: persistent supports are almost disjoint

For a graph C, let p_C be its number of persistent coordinates, where
F(x)=f_x and G(x)=g_x. At a coordinate for which R(x,z) is not the zero
polynomial in z, at most one graph can be persistent: two such graphs
would have the same value for generic z at a nonsingular coordinate,
contradicting Section 1 unless they coincide.

The set Z0 of coordinates at which R(x,z) vanishes identically has size
at most r. Therefore sum_C (p_C-r)_+ <= n.

Call a graph heavy if p_C>(T+r)/2. There are at most 2n/(T-r) heavy
graphs. Each has at most n bad labels: a bad support must contain an
accidental agreement, and each nonpersistent coordinate forces at most
one label. A graph over the algebraic closure with fewer than two
F-rational points at distinct labels contributes at most one label;
otherwise its two points imply F,G are defined over F, so the common-
witness argument is valid over F itself. The heavy contribution is at
most 2n^2/(T-r).

A light graph has p_C<=(T+r)/2, so each nearby label requires at least
(T-r)/2 accidental coordinates. The total number of accidental
coordinate-label incidences on one graph is at most n. Hence there
are at most 2n/(T-r) nearby labels per light graph. Their number is at
most J1, giving a contribution at most 2n*qK/(T-r).

Add Sections 3--5 and the at most H exceptional challenges to get (1).

## 6. A linear lower family at fixed rate and gap

For any nonzero squarefree W of degree D, the nonlinear equation

    W P' - W' P - P(P-W) = 0                             (2)

has exactly two polynomial solutions, 0 and W, in every characteristic.
Indeed, writing Z=P/W gives Z'=Z(Z-1). For Z nonzero put U=1-1/Z;
then U'=U. In characteristic zero a rational function U has U'/U
vanishing at infinity, so cannot equal 1. In characteristic p the
p-fold ordinary derivative is zero on F(X), whereas U'=U would imply
the p-fold derivative equals U. Thus U=0, yielding Z=1.

For a fixed-rate family let n=12s, D=3s, T=6s and choose a prime p>12s.
Take distinct domain points x_i=i (0<=i<n) and let W have precisely
the first 3s of them as roots. On those roots put f=g=0. On the next
3s coordinates put f=g=0; on the next 3s put f=W and g=0. At each of
the final 3s coordinates, indexed j=1,...,3s, put f=3j*W and g=W.

For c in {0,1}, the candidate cW has persistent agreement support
of size 6s. It acquires one extra agreement at z=c-3j. These 6s
labels are pairwise distinct in F_p, since their integer representatives
are distinct and lie in an interval shorter than p. At each such label
the full support has 6s zero values of g and one nonzero value. No
degree-<=D polynomial agrees with g there, because 6s>D. Every one of
these labels is bad. At any other label both candidates have only their
persistent supports, on which g=0, so are good.

Thus (2), with B=2,H=0,r=D, has exactly n/2 bad labels, code rate
(D+1)/n tending to 1/4 and agreement gap (T-D)/n=1/4. It establishes
sharp linear order within the theorem's hypotheses, without claiming
a quadratic construction or a better.codes score improvement.
