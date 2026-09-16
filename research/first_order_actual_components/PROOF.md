# Actual first-order components: proof and review record

September 16, 2026. Twice self-reviewed; no claim of independent coauthor
review or novelty. The complete integrated proof is in `appendix.tex`.

## Exact statement

Over an algebraically closed field of characteristic zero or p>D, let
Q(X,z,u,v) be nonzero, of jet degree <=B and z-degree <=H. Take the
Zariski closure of the actual pairs (z,P), deg P<=D, satisfying Q=0
identically in X and with Q_v(X,z,P,P') not identically zero.

Every component has dimension at most two. If J_i sums the projective
degrees of the i-dimensional components, then

    tau=max(0,2D-3), b=1+tau(B-1), T=b+tau H,
    K=H+B T, q=B+H,
    J_1<=q K, J_2<=q T.

The surface components' reduced generic challenge fiber has summed
degree at most deg_v Q. There is no bound here on the X-degree of Q.

## Why actual components matter

Define the actual coefficient-space locus before adjoining a generic
Taylor center t. Its projective curves have finitely many points at
infinity over the original algebraically closed field. The restricted
hyperplane P(t)+lambda*z=c misses those points because t and lambda
are independent transcendentals. This ensures it counts the full curve
degree. An arbitrary Taylor-image cover defined using t need not have
this property; its points at infinity can lie in P(t)=0.

On a curve, P(t)+lambda*z is separable. The coefficient functions and
z generate the function field; they cannot all have zero differential.
Independence of t and lambda prevents cancellation. Generic sections
are therefore reduced, including in positive characteristic.

## Reconstruction and residuals

Put S=Q_v and A=Q_X+v Q_u. Along a solution, differentiation is

    partial_X + v partial_u - (A/S) partial_v.

The jth derivative has denominator S^(2j-3), jet numerator degree
<=1+(2j-3)(B-1), and z-degree <=(2j-3)H. The explicit induction
recurrence is in the appendix and is checked symbolically.

With common denominator S^tau, the degree-D Taylor polynomial has
coefficient numerators of jet degree <=b and z-degree <=tau H.
After substitution into Q and clearing S^(tau B), every coefficient
residual has total initial-data degree <=K. Initial data also satisfy
Q(t,z,u,v)=0, of total degree <=q.

On S!=0, residual-zero reconstructed polynomials are precisely the
actual degree-bounded solutions, with their original initial value and
derivative. The initial-jet and reconstruction maps are inverse regular
maps on these opens. Thus dimensions, actual points, and local components
are preserved. The closure of this regular locus has no new irreducible
components lying entirely in its boundary.

## Curves

Cut by P(t)+lambda*z=c, avoiding curve boundary points and intersections
with other actual components. The selected J_1 points are distinct and
do not lie on actual surfaces. In initial data this substitutes
u=c-lambda*z into the degree-q equation, leaving a plane curve.

Any plane component where all residuals vanish maps, on S!=0, to a
positive-dimensional component of the generic hyperplane section.
It must therefore come from an actual surface; none of the selected
J_1 points lies there. On all remaining plane components, a generic
linear combination of the degree-K residuals is nonzero. Bezout gives
at most q K intersection points. This proves the curve bound.

## Surfaces

The same generic hyperplane contains no curve at infinity of an actual
surface. Its affine section closures therefore retain full surface
degrees. Regularity makes projection of initial data to (z,u) generically
separable, so generic line sections are generically reduced.

The initial-data curves of these sections are distinct components of
Q(t,z,c-lambda*z,v)=0 and have total degree <=q. After clearing the
common denominator, the projective output coordinates are S^tau,
z S^tau, and the coefficient numerators. Their total degrees after
substitution are at most T-1, T, and T, respectively. Homogenizing to
degree T and pulling back a generic hyperplane bounds the rational
image degrees by T times the source degrees. Thus J_2<=q T.

For the generic-fiber statement, fix a generic challenge first. The
regular initial-jet curves lie in a plane equation whose v-degree is
at most deg_v Q. A generic initial value therefore has at most that
many preimages. Choosing a new independent generic Taylor center makes
this section count the full coefficient-space curve degrees, as above.

## Sharpness and remaining obstacles

There is also a direct agreement-incidence consequence. Any actual
curve other than an affine codeword graph P=F+zG has at most D
persistent agreement coordinates on a received line f+zg: D+1 such
coordinates would force that graph by interpolation. All other
coordinate hyperplanes meet the curve in at most its degree many
points. Thus its nearby pairs at threshold A>D number at most
deg(C)*(n-D)/(A-D). Summing and applying J_1<=q K gives Corollary H.2,
an O(n) count for these nonaffine curve components at fixed positive gap.

`verify_curve_family.py` checks the family

    R=X^(D+1)+zX-1,    R P'-R_X P+P^2=0.

For p>D+1, every nonzero solution is P=R/(X-a), where
z=a^-1-a^D. The degree-D coefficient curve is birationally parameterized
by a!=0. After multiplying projective coordinates by a, their span is
1,a,...,a^(D+1), so it is a rational normal curve of degree D+1.
The zero line gives total curve degree D+2. At p=D+1, extra solutions
can occur; the negative control checks this and does not contradict
the general theorem, whose weaker characteristic condition is p>D.

The surface c(X-z)^D has degree D+1 by the generic two-hyperplane
elimination argument in the appendix. Earlier Taylor checks also
verify the linear equation P'+zP-X^D=0, whose unique solution for
z!=0 gives an actual curve of degree D+2.

The isolated actual joint points can actually be quadratic in number,
as the following construction now proves. A linear number of persistent affine codeword graphs
could also each contribute linearly many accidental labels. Nothing
here establishes the constant nearby symbolic-list bound that would
remove that second obstruction. The first-order O(n/|F|) conjecture
and higher-order quadratic lower-bound target remain open.


## Quadratic isolated solutions and constant nearby-label count

Added September 16, 2026, after exact checks and a second proof review.
The integrated statements are Theorem H.3 and Proposition H.4.

For monic squarefree R of degree D+1 with nonzero roots, put

    Q=(z-X^2)(R P'-R'P+P^2)+2XRP-2R^2.

Let U=(X^2+z)P-2XR, V=R-XP. The identity U'V-UV'=Q is exact.
V cannot vanish identically because V(0)=R(0)!=0. If Q=0,
U/V has degree <=D+2 and derivative zero. Characteristic zero or
p>D+2 makes this quotient constant, say -u, giving

    (X^2-uX+z)P=(2X-u)R.

The quadratic's root multiset lies among the roots of R. Thus all
solutions are P=R/(X-a)+R/(X-b), z=ab, including a=b. Distinct
multisets have different partial-fraction residues (characteristic
not two). All are regular since Q_{P'}=(z-X^2)R is nonzero in X.
The geometric point count is exactly binom(D+2,2). We assert the
count of the reduced locus, not reducedness of the original scheme.

The greedy Sidon exclusion count (k+2)k(k+1)/2+k+1 equals
(N^3+N)/2 at k=N-1. The extra +k+1 excludes old roots and zero;
then new off-diagonal products cannot collide with one another or
with the new square. This justifies distinct prime-field labels
at field size O(D^3), without a number-field splitting argument.

For any received line, count nonzero agreements: there are at most
D zeros per degree-D candidate, at most N=D+1 nonzero matches at a
root of R, and at most N+1 unordered matches elsewhere. The latter
uses at most 2N ordered matches and at most three diagonal ones.
This gives (D+2)n/(A-D), even counting pairs rather than labels.

For the constant bound, pick one witness per distinct nearby label.
An affine relation among three functions W=P/R has three nonzero
coefficients. Every root in their support union must occur at least
twice, so at most three roots occur. Three roots force a triangle,
whose residue determinant is 2. Two roots force the three multisets
aa,ab,bb; their unique affine relation (1,-2,1) does not vanish on
labels a^2,ab,b^2. Thus no triple is affine-collinear as labeled
functions. This argument allows global label collisions because
only triples of distinct selected labels are used.

The common quadratic denominator product has degree six. The
numerator's degree-five term cancels (sum of coefficients zero),
leaving a nonzero polynomial of degree <=4. Hence at most four
common agreeing coordinates outside roots of R. With m outside
coordinates, t guaranteed agreements per witness, and L labels,
triple counting and Jensen give (tL-2m)_+^3<=4m^2 L^3.
When t^3>4m^2 this rearranges to the displayed constant bound.
The case tL<=2m satisfies it too; m>0 follows from the hypothesis.
For fixed gap A-D>=eta*n, t>=eta*n-1 and m<=n prove O_eta(1).

Second review explicitly checked: zero denominators; doubled roots;
small-characteristic failure; collisions of new Sidon products;
ordered-to-unordered incidence counting; triples with repeated
labels excluded; all possible support unions; cancellation at
infinity; and the small-multiplicity cases in the convexity bound.
The exact checker passes in 4.28 seconds with sampled RSS 24736 KiB.
No independent coauthor review or novelty assertion is made.
