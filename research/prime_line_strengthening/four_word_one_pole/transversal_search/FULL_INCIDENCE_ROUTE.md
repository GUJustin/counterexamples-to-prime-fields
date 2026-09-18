# Full-incidence deformation after the six-word certificate

This is a bounded strategic route and exact dimension ledger, not an existence
proof for a seventh word. The full six-word incidence rank gate has now passed (Section6). The next
target is the augmented extension system and its two necessary dependencies,
rather than another blind one-pole parameter scan.

## 1. A concrete selected incidence graph

The first28-point five-word bank has the following selected match sets:

* twelve points with two original words and G5 (degree3);
* twelve points with two original words only (degree2);
* two first-pole points with all four original words (degree4);
* two fresh points with G5 only (degree1).

The second proper rational witness matches exactly14 of these points:
five of the degree3 points, six of the degree2 points, one degree4 pole
point, and both degree1 fresh points. These are precisely the first p97 hit's
12 selected core nodes plus the independently verified fresh roots24,52.

For the six-word lift, duplicate every old point by its two quadratic
preimages. Preserve each old match set, adding word6 exactly over those14
rational agreements. Add two new pole points carrying words1,...,5, and
two new fresh points carrying word6. Every word has exactly30 SELECTED
incidences, and every one of the60 points is covered. The resulting selected
node-degree histogram is

    degree1:2, degree2:16, degree3:26, degree4:12, degree5:4.

It sums to60 nodes and180 incidences. Extra accidental agreements may be
ignored: these specified supports suffice for the claimed bank and define
the incidence scheme to be tested.

The polynomials have coefficients in F97. All28 old coordinates and the
second pole81 are in F97 and are nonzero. Their square roots lie in F97^2,
so the60-point realization can be constructed there. Two fresh points are
chosen outside the58 inherited/pole points. This is an exact finite-field
setup, not a numerical approximation to the number-field construction.

## 2. Full Jacobian, with received values eliminated

Write each polynomial P_i with15 coefficients (degree<=14). Initially the
unknowns are90 polynomial coefficients,60 nodes x_j, and60 word values w_j:
210 variables. Each selected edge imposes

    P_i(x_j)-w_j=0,

giving180 equations. At every node choose one incident reference word i0(j)
and eliminate w_j=P_i0(j)(x_j). The remaining120 equations are

    P_i(x_j)-P_i0(j)(x_j)=0.

There are150 remaining variables:90 polynomial coefficients and60 nodes.
The differential row is

    delta P_i(x_j)-delta P_i0(j)(x_j)
       +(P_i'(x_j)-P_i0(j)'(x_j))*delta x_j.

Thus the exact matrix is120 by150 over F97^2, not180 by150 and not a
matrix of fixed-node evaluation constraints. Its maximum rank is120.
The equivalence to the original formulation uses only that every node has
at least one selected incident word.

A rank120 certificate would give a smooth local incidence space of dimension
30 before gauge removal. It would justify formal/algebraic deformation after
restricting to open guards preserving node distinctness and distinct words.
Failure of full row rank is not an impossibility theorem: it may indicate
structural dependencies, singular obstructions, or a larger component.

## 3. The indispensable gauge correction

There are k+4=19 independent infinitesimal symmetries, with k=15:

* adding the same degree<=14 polynomial to every P_i and to the received word
  gives15 directions;
* projective changes of X give THREE directions, with node motions1,x,x^2;
  these are independent on at least three distinct nodes;
* common nonzero scaling of all word and polynomial values gives one more
  direction, independent of common addition because the words are distinct.

Consequently full rank leaves11 genuine moduli after fixing these gauges.
One can normalize one candidate to zero, three distinct nodes to fixed distinct
projective coordinates, and one nonzero coefficient of a remaining difference
polynomial to one. These are
local gauge choices, not additional incidence hypotheses.

The third projective direction, missed by the initial affine-only count, is

    delta x_j=x_j^2,
    delta P_i=D X P_i-X^2 P_i',
    delta w_j=D x_j w_j,       D=k-1.

The degree-D+1 terms in delta P_i cancel, and the differential of every
incidence equation vanishes. Its node motion is independent of1,x, so it is
an additional genuine gauge direction. Globally this is the ordinary PGL2
action on sections of O(D), with coordinate-dependent scaling of received
values. A proper degree-(D+1)/linear rational witness is also preserved:
a Mobius substitution and the same section scaling again produce a numerator
of degree<=D+1 over a linear denominator. Thus the extra gauge must also be
removed in the one-pole dimension ledger; it is not optional there.

For a general quarter-rate bank with n=4k, polynomial degree k-1, A=2k, and
L words, the naive dimension before gauge removal is

    Lk+2n-LA = k(8-L).

The gauge-free expected dimension is instead

    k(7-L)-4.                                    (1)

Thus L=7 already has expected dimension minus4, despite a positive raw count
of k. At every nondegenerate seven-word configuration the incidence rows must
have at least four dependencies. At L=8 at least k+4 dependencies are forced.
This conclusion is a rank constraint, not a nonexistence result. It explains
why ordinary full-row-rank Hensel lifting cannot, by itself, certify the next
seven-word incidence system.

## 4. Comparing a third one-pole step with a direct seventh word

The verified smooth six-word system has gauge-free dimension11. A prospective
one-pole function N/(X-beta), deg N<=15, adds17 parameters (16 numerator
coefficients and one pole), after fixing the denominator monic. Agreement on
30 chosen old coordinates imposes30 equations. The expected surplus is

    11+17-30 = -2.

A direct seventh polynomial of degree<=14 instead adds15 coefficients and
imposes30 matches, for expected surplus minus4. Thus full-incidence deformation
is a much larger search space than the original restricted constructor, but
neither next step is guaranteed by dimension. A third one-pole step needs at
least one structural dependence in its augmented incidence equations; a direct
seventh polynomial needs at least three.

If the six-word full Jacobian has lower rank, the tangent space is larger, but
this extra tangent dimension must not be confused with actual unobstructed
moduli. One should first isolate the algebraic dependencies or obstruction
maps, rather than claiming that a singular tangent space automatically supplies
additional deformation parameters.

## 5. Concrete next gate and stop criterion

The prescribed gate was to construct the selected60-point bank over F97^2
and compute the exact120-by150 rank under the384MiB/60second watchdog,
recording all180 incidences and derivative entries. The frontier agent has
completed this bounded computation successfully; see Section6.

The successful rank120 result now calls for preserving a minor certificate
and a local11-parameter quotient chart before testing a carefully chosen
third-step support. Analyze the
augmented system's two-dimensional expected obstruction rather than sampling
unstructured rational functions. If rank is lower, report the deficiency and
identify its algebraic source; do not immediately launch a wider search or
infer liftability. Either result is more informative than treating the raw
positive dimension count as evidence that seven words must exist.

## 6. Completed rank gate and exact left-kernel characterization

The frontier agent's `six_bank_incidence.py/json/resources` now certifies
rank120 over F97^2 (rank240 after restriction of scalars to F97). The full
incidence rank is180 and the raw tangent dimension is30. Its exact selected
incidence histogram agrees with Section1. Independent source review confirms
the coefficient blocks, node-derivative blocks, finite-field representation,
and restriction-of-scalars matrix. This is a smooth six-word configuration
with11 local moduli after the full19-dimensional gauge, not12.

There is also an exact algebraic formulation of any row dependence. For each
word i, let S_i be its30-point support and L_i(X)=product_(x in S_i)(X-x).
A dependence is a collection of weights lambda_(i,x) on selected edges such
that

    sum_(x in S_i) lambda_(i,x)*x^j=0, j=0,...,14,
    sum_(i incident to x) lambda_(i,x)=0,
    sum_(i incident to x) P_i'(x)*lambda_(i,x)=0.

The first condition is equivalent to

    lambda_(i,x)=h_i(x)/L_i'(x),  deg h_i<15.

One direction is the Lagrange leading-coefficient identity for polynomials
of degree<=28; the converse follows because the15-by30 Vandermonde matrix
has rank15 and this15-dimensional parameterization is injective. Thus the
left kernel is exactly six degree-at-most14 polynomials satisfying the two
explicit node conditions. This works in arbitrary characteristic with distinct
nodes; factorial denominators are unnecessary.

At a degree-one node the weight is zero. At a degree-two node it is also zero
on both incident edges whenever the corresponding polynomial difference has
a simple root there: subtracting the two node conditions gives
(P_i'-P_j')lambda_(i,x)=0. These forced zeros can reduce the h_i parameters
and may expose structural dependencies or provide a smaller symbolic rank
certificate. They are not by themselves a proof that every dependence vanishes.
