# Relative discriminant and rational-member audit

The degree-62 equation reconstructed modulo 29 is the reduction of the
characteristic-zero residual discriminant cycle, not merely an unrelated
modular Gauss image. Here is the required relative argument and the
exceptional-divisor check.

Work over the DVR of Q(eta) at eta=7 above 29, extending it unramified to
split the seventh roots as necessary. The independently verified exact
kernel sections define the sixteen disjoint basepoint sections and their
smooth blown-up surface. The resolved net is basepoint-free: the closed
relative base locus is proper and has empty geometric special fiber.

The universal first-jet incidence on this surface times the member plane
is cut out by three equations. Its special fiber has pure expected
codimension three: jet rank zero is impossible, rank two lies on a
curve, and rank one occurs only at finitely many surface points. The
ambient space is smooth over the DVR. Consequently these three equations,
together with the uniformizer, are a regular sequence; the incidence is
a relative complete intersection and flat over the DVR. Its fundamental
cycle specializes to the fundamental cycle of its special fiber. Proper
pushforward to the member plane commutes with specialization of cycles.
The pushed effective divisor has degree 90 by the computed jet Chern
class.

The seven horizontal old-graph parameter lines contribute exactly four
each in both fibers, using the saved coprime normal quartics and simple
ramification orders. Subtracting them leaves a horizontal effective
degree-62 divisor. Its equation can be chosen primitive over the DVR.
In the special fiber, the geometrically irreducible Gauss image has
degree 62: its degree is at most 62 from the preceding effective cycle;
4,018 distinct certified points and Bezout force every interpolated
degree-62 relation to contain it; the full degree-62 relation space has
dimension one, ruling out image degree less than 62. Thus it consumes the
entire residual cycle with multiplicity one. In particular there are no
additional rank-one image lines. The primitive residual equation reduces
to the computed equation up to a nonzero scalar.

## Rational curves and exceptional components

An integral original curve might in principle acquire exceptional
components after subtracting the fixed base multiplicities. This must not
be silently identified with an integral member on the resolved surface.
Here the issue is completely controlled.

At the multiplicity-four and multiplicity-six representatives, the first
three coefficient columns of the three tangent cones have determinants
5 and 20 modulo 29, respectively. They therefore have rank three in
characteristic zero. No nonzero member can jump its multiplicity at any
of these fourteen points. At each of the two additional simple
basepoints, the linear-part map has kernel exactly [0:1:0]. Its independent
F0,F2 linear coefficients are units. The exceptional member F1 has order
exactly two at both points: its quadratic terms reduce to 24Y^2 at the
origin and 7Z^2 in the infinity chart. Eigen-support excludes lower terms
exactly; the displayed coefficients certify the upper bound on the order.

It follows that an integral rational original member produces either an
integral rational resolved divisor, or a reduced divisor consisting of
its rational strict transform and the two exceptional rational curves,
each with multiplicity one. The latter divisor is connected, since each
exceptional curve meets the strict transform. All components have
rational normalization. For either case, with k components,

    sum(delta) = p_a(L) + k - 1 >= 15.

Choose a generic pencil through this member. Its other section avoids
the finitely many singular points because the net is basepoint-free.
The resulting local total spaces are smooth and their discriminant
intersection lengths are the characteristic-zero Milnor numbers.
For a reduced plane-curve singularity, mu=2delta-r+1 >= delta. Thus the
multiplicity of the full discriminant divisor at this parameter is at
least 15. An integral original curve cannot contain an old cubic graph,
so its parameter is off all seven old-factor lines. The residual
polynomial consequently has multiplicity at least 15 there too.

Finally the multiplicity-at-least-15 locus of the homogeneous residual
polynomial is closed over the DVR (use all Hasse derivatives of total
order below 15 on projective charts). If its entire geometric special
fiber is empty, properness of the parameter plane excludes a generic
fiber point. A characteristic-zero parameter is allowed to specialize
onto an old line: the closed residual multiplicity condition still
specializes, so this creates no missing boundary case.

This audit uses the saved exact kernel, resolved-base-locus, Gauss
factorization, old-normal-quartic, independent source-point, and full
interpolation certificates. It does not infer flatness or rationality
from a finite sample of curves.

## Explicit global rank-one-locus guard

The affine gcd of jet minors is only one chart of the required check.
The supplement `verify_base_boundary.py` / `base_locus_boundary.verified.json`
checks the remaining divisors. The fourteen exceptional restrictions are
basepoint-free tangent maps of degree at most six, nonconstant by their
rank-three coefficient matrices. The two simple exceptional restrictions
are rank-two linear maps. On C0 the restriction is [25:27X^2:20X^4];
on the infinity fiber the saved three restrictions have distinct exponent
supports and define a nonconstant map of degree at most ten after
removing the common simple basepoint factor. Each degree is below 29,
so each map is generically separable. The surface map has differential
rank at least one there, equivalently its jet matrix has rank at least
two. Thus none of these divisors supports a rank-one jet locus. Combined
with the affine gcd certificate, this proves global finiteness.

The supplement also serializes the tangent minors 5 and 20, the linear
kernels at both extra points, and the exact modular order-two initial
forms of F1. It leaves the original base-locus receipt unchanged so that
previous hashes remain valid.
