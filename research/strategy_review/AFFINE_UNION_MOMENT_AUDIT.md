# Complements and affine unions: bounded feasibility audit

September 17, 2026. This is an audit of specified composition operations,
not an impossibility theorem for all dependent moment constructions.
Let the target normalized moment depth be r, on a domain of size n.
The residue route near the quarter-rate first-order threshold needs
r approximately n-D, hence r/n>1/2 on the large singular core.

## Complements preserve depth but collapse the scalar-label parameter

For disjoint B,C with B union C equal to a fixed active support U,
equality of their normalized moments through degree r is equivalent
to each subset having the normalized moments of U through that degree.
This follows from

    mu_U=(|B|/|U|) mu_B+(|C|/|U|) mu_C.

There is no increase in moment depth. More decisively, for residues
{0,1,z} the zeroth moment gives z=-b/c=-b/(|U|-b). With U fixed there
are at most |U|-1 possible labels, even if exponentially many complementary
partitions exist. This argument works over a prime scalar field when
|U|<p, so the denominators are nonzero. Adding a fixed inactive zero
subset does not help: the active support cardinality remains fixed.
Thus complementing subsets cannot itself give a superlinear label count.

## Unions of same-ratio blocks preserve only the old gap and one label

If disjoint blocks each contain B_i,C_i with equal normalized moments
and the SAME cardinality ratio b_i/c_i, then taking their unions preserves
the known moment equalities but preserves exactly that scalar challenge
ratio as well. The number of labels has not increased. If the seed depth
r stays fixed while J independent blocks are added, domain size becomes
J times larger and r/n shrinks by J. Affine pushforwards preserve the
known moment depth by the binomial theorem; they do not automatically
create any further equalities.

Mixing different ratios is not covered by that preservation statement.
It imposes additional weighted moment constraints on block locations.
Those constraints are precisely new dependent cancellations; they must
be proved, not assumed from the seed identities.

## Exact bound for disjoint translated signed-seed amplification

There is a stronger obstruction for a common proposed depth amplifier.
Let nu be a nonzero signed seed measure on s0 distinct points, with
moments zero through degree r0, and with moment r0+1 nonzero. Take J
nonzero weighted translates of the SAME seed (a fixed common scale is
allowed), with distinct translation parameters beta_i. Assume their
supports are disjoint, so n=J*s0. In characteristic zero, or in prime
characteristic p>=n, the new moment depth r satisfies

    r <= r0+J-1 <= s0+J-3.                       (1)

Proof: use the exponential generating series of moments, truncated
before degree p in positive characteristic. The new series is

    F_nu(t) * sum_i w_i exp(beta_i*t).

The first factor has order r0+1. The second has order at most J-1 by
the Vandermonde determinant on the distinct beta_i. Also r0<=s0-2 by
the Vandermonde determinant on the seed support. The relevant orders
are below p under the stated assumptions, so factorial denominators
are legitimate. Orders add, proving (1).

For J,s0>=2, s0+J-3<Js0/2, since
Js0-2(s0+J-3)=(J-2)(s0-2)+2>0. Hence

    r/n < 1/2.

This cannot reach the required deep-moment regime. The estimate allows
arbitrary nonzero signed weights, so demanding a fixed small residue
alphabet cannot improve it. It covers translated signed trades, not
arbitrary mixed-ratio block unions. Distinct scales do not factor into
one common generating series and are not ruled out by this argument.
Overlapping translates can reduce the actual domain size, but then one
must separately prove that overlap cancellation retains the allowed
residue alphabet and produces many labels. That is a new mechanism,
not a consequence of the disjoint-union construction.

## Precise remaining bottleneck

A successful complement/union construction must simultaneously:

1. vary both active support cardinality and branch balance, to avoid
   the linear cardinality-ratio bound;
2. retain moment depth greater than half the actual domain size;
3. use dependent dilations or overlaps beyond the signed-translate
   factorization above;
4. preserve bounded residue alphabets and actual received-line agreement.

No such composition identity is presently available. Claiming that
arbitrary affine unions are impossible would exceed this audit; claiming
that the familiar operations amplify the existing seed would also be
incorrect. This branch should stop until an explicit dependent identity
meets those four tests.

## A genuinely distinct next candidate

Move one research slot to quadratic dependence on the derivative,
rather than another residue reformulation. A concrete test family is

    (P')^2-U(X,z)P'+V(X,z)P^2+W(X,z)P+Y(X,z)=0,

with bounded challenge degrees and squarefree equation. At a singular
agreement coordinate, the derivative is forced to U(x,z)/2, while
P(x)=f(x)+zg(x). If U is affine in z, these are affine Hermite data:
value and derivative are both prescribed by the challenge. This opens
an actual route to a stronger upper theorem through multiplicity-code
agreement, rather than requiring a new deep subset-moment source.

Before searching examples, isolate coordinates where the discriminant
U(x,z)^2-4[V(x,z)(f+zg)^2+W(x,z)(f+zg)+Y(x,z)] vanishes identically.
Outside them only boundedly many singular labels occur per coordinate.
On the persistent part, test whether a Johnson-type line bound for
order-two Hermite evaluation gives a linear exceptional-label bound at
the first-order agreement threshold. This is not claimed proved here;
it is a bounded, different theorem target with an exact singular-data
reduction. It also identifies what a nonlinear-derivative construction
would have to defeat. Avoid repeated-square equations, whose artificial
singularity disappears after squarefree reduction.
