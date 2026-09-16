# Linear first-order MCA from a positive density of nonsingular agreements

September 16, 2026. Stronger replacement for the first proof in PROOF.md.
Proof self-reviewed twice; exact finite checks passed. The conclusion applies to implicit
first-order equations as well as value-independent separants.

## The local theorem

Let Q(X,z,u,v) be nonzero, with jet degree <=B and challenge degree <=H,
and let D>=1, char F=0 or p>D. Its X-degree is unrestricted. Put

    tau=max(0,2D-3), b=1+tau(B-1),
    T0=b+tau*H, K=H+B*T0, q=B+H.

Fix a received line f+zg on n distinct points, an agreement threshold
A>D, and an integer L>=1. Consider labels possessing a degree-<=D
solution P of Q(X,z,P,P')=0 with full agreement support S such that:

* |S|>=A;
* no degree-<=D polynomial agrees with g on all of S;
* at least L coordinates x in S satisfy Q_v(x,z,P(x),P'(x))!=0.

Then the number of these labels is at most

    (n/L) * [q*K + q*T0*(n-D)/(A-D) + q*n].              (1)

At fixed B,H and A-D>=eta*n, L>=lambda*n, this is O(n).
No assumption that Q is linear in v, or nonlinear in u, is needed.
The statement controls only labels with a witness having L nonsingular
agreements; singular agreement points are the remaining obstruction.

## Proof

Fix a domain point x and restrict the initial value to u=f_x+z*g_x.
The initial equation Q(x,z,f_x+z*g_x,v)=0 has degree at most q in
(z,v). If it is identically zero, its v derivative is identically
zero too, so it contains no nonsingular initial data under consideration.
Otherwise restrict to its open locus S0=Q_v(x,z,f_x+z*g_x,v)!=0.

The Taylor construction in Theorem H.1 applies at this fixed center,
because S0 is nonzero at each retained initial datum. In projective
coefficient space (including z), reconstruction has coordinate degree
at most T0. Its common denominator is S0^tau; this has degree at most
T0-1, so z*S0^tau also has degree at most T0. The coefficient numerators
have degree <=T0 after the affine substitution for u. Exact polynomial
solutions are selected by residual equations of degree at most K.
The reconstruction and the initial-jet map are inverse regular maps
on this open exact-solution locus.

There are two types of components after imposing all the residuals.

1. Isolated points. On each component of the initial plane curve not
   entirely satisfying the residuals, at least one residual is nonzero.
   Over an algebraic closure choose a generic linear combination that
   is nonzero on every such component. Bezout bounds their isolated
   intersections by q*K in total. No point on a retained curve is an
   isolated component; boundary points with S0=0 are excluded.

2. Curves. Their source curves are distinct irreducible components of
   the initial plane equation. Thus there are at most q of them and
   their degrees sum to at most q. Under a rational map of degree at
   most T0, their image degrees sum to at most q*T0. Initial-jet
   recovery ensures the image of each is a curve rather than a point.

On a nonaffine image curve, at most D coordinate agreement hyperplanes
can be persistent: D+1 of them would force P=F+zG by interpolation.
The standard incidence count therefore gives at most

    degree(curve)*(n-D)/(A-D)

nearby pairs. This includes vertical curves, since D+1 persistent
coordinates would make a vertical curve a point. Sum over these curves.

Each remaining image curve is an affine graph P=F+zG. If its full
agreement support contains only persistent coordinates, F,G give common
witnesses. Every bad label must therefore be an accidental agreement
at a nonpersistent coordinate, which forces at most one label per
coordinate. There are at most n such labels per graph. If F,G are not
defined over F, two F-rational points at distinct labels would imply
descent; thus a graph failing descent contributes at most one F-label.
The bound n holds in either case. There are at most q graphs.

Consequently the fixed coordinate x participates nonsingularly in a
bad nearby candidate at no more than

    q*K + q*T0*(n-D)/(A-D) + q*n

distinct labels. Choose one qualifying witness for each selected label.
It has at least L nonsingular agreement coordinates. Double counting
coordinate-label incidences proves (1).

## Corollaries

For any regular candidate whose substituted separant is nonzero of
X-degree at most s<A, at least A-s agreeing coordinates are nonsingular.
Thus (1) applies with L=A-s. In particular it gives an O(n) result when
s<=D+O(1) at a fixed positive agreement gap.

For Q=R(X,z)v-A(X,z,u), R nonzero, r=deg_X R<A, there are at most H
labels for which R(X,z) is identically zero. Count all of these
exceptional labels separately; every other candidate satisfies the
nonsingular-agreement condition with L=A-r. Therefore

    #bad labels <= H + (n/(A-r))*
                         [q*K + q*T0*(n-D)/(A-D) + q*n].  (2)

This covers all value degrees of A, including affine-linear equations.
It supersedes the longer component-decomposition proof in PROOF.md,
although that proof gives a different explicit constant for nonlinear A.
The n/2 lower construction in PROOF.md remains valid and demonstrates
sharp linear order at fixed rate and gap within this subclass.

## Quantitative obstruction

For fixed B,H and positive agreement gap, (1) is O(n^2/L). Hence any
superlinear first-order construction must concentrate on candidates
with a vanishing fraction of nonsingular agreement coordinates. A
family of Omega(n^2) distinct bad labels cannot give every selected
witness an unbounded number L of nonsingular agreements. This is a
necessary condition, not a construction or a resolution of the general
first-order conjecture. Interpolation equations can be singular at many
agreement coordinates, so the hypothesis must not be silently assumed.

## Finite checks

The checker exhausts 65,062 polynomial--challenge pairs and checks 218
received lines. It verifies 675 nonsingular value-uniqueness instances,
ordinary-list incidences, full-support badness, and the coordinate-label
double count for implicit examples with solution-dependent separants.
The implicit equations have actual solution surfaces; they exercise a
case not covered by the earlier nonlinear quasilinear component proof.
Five fixed-rate lower fixtures attain exactly 6, 12, 18, 24, and 48 bad
labels on lengths 12, 24, 36, 48, and 96. The characteristic-three
negative control verifies failure of regular-value uniqueness once p>D
is omitted. These checks supplement the proof. No independent referee
or literature-priority claim is asserted.
