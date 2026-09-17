# Beyond the monic Riccati limitation: structural search gates

September 17, 2026. No new scalable superlinear construction is claimed.
This review identifies exact remaining hypotheses, rather than treating a
nonconstant coefficient or a moving singular set as a construction.

## 1. Gaugeable quadratic coefficients: a limited escape

For

    T P' - A P^2 + R P - S = 0,

put Y=AP. Direct differentiation gives

    T Y' - Y^2 + (R-T A_X/A)Y - AS = 0.           (1)

Thus A | T A_X is precisely the polynomial gauge condition. If all
challenge degrees are bounded, the transformed coefficients also have
bounded challenge degrees: polynomial division cannot increase the
z-degree beyond that of its numerator. However deg_X Y<=D+a, where
a=deg_X A. Degree inflation is the material cost.

The transformed received values A(x,z)(f(x)+zg(x)) have bounded challenge
degree rather than being affine. This is not a fundamental obstacle to
the high-degree incidence argument. Their agreement equations still have
bounded parameter degree and z-degree O(D+a). Remove coordinates where
A(x,z) is identically zero, of which there are at most a. On a residual
curve with more than D persistent remaining coordinates, fix D+1 of them
and exclude the O_h(D) labels where their A-values vanish. Every original
polynomial candidate on that curve then agrees with f+zg at those D+1
fixed points. Interpolation forces those ORIGINAL candidates onto one
affine codeword pencil, with at most n full-support bad labels. This
argument does not require the entire transformed curve to parameterize
polynomials divisible by A.

Consequently the monic proof has a conservative gauge extension under

    A_agreement > (5D+4a)/3 + lambda*n,            (2)

with fixed challenge degrees, characteristic zero or greater than D+a,
and positive linear gap. The stronger characteristic bound is necessary
for the transformed recurrence through degree D+a; the low-T cover by
itself only needs characteristic greater than D. Indeed, if
 deg_X T<=2(D+a), apply the ORIGINAL fixed-cover theorem with at most
2(D+a) persistent singular coordinates; (2) is its triple threshold.
If deg_X T>2(D+a), apply the high-degree transformed recurrence and plane
incidence proof. Nonpersistent nearby incidences number at least
A_agreement-D-a, which is positive with linear slack under (2).
Source degrees are O(D+a)=O(n) in this parameter range. Exceptional
labels where A vanishes identically are bounded by its challenge degree.
This paragraph is a proof sketch; the exact audited statement is now
Corollary riccati-polynomial-gauge in fixed_singular_cover/appendix.tex,
with the stronger characteristic restriction made explicit.

At quarter-rate first-order agreement A_agreement/D about1.87517,
(2) permits a/D below about0.15638. Therefore bounded-X-degree gaugeable
quadratic coefficients do not constitute a promising escape. The known
Wronskian coefficient A=z-X^2 is gaugeable because it divides T; it
already lies inside the stronger singular-cover limitation.

## 2. Moving singular roots alone are not a mechanism

For ANY value-independent separant T(X,z) of challenge degree h, let

    S={domain x : T(x,z) is identically zero in z}.

Outside S, the total number of singular coordinate-label incidences is
at most hn, REGARDLESS of deg_X T. Discarding at most h/epsilon labels
leaves at most epsilon*n singular coordinates outside S per label.
The fixed-cover theorem therefore proves a linear bound whenever

    |S| < (3*A_agreement-D)/2 - positive linear slack.

At quarter first-order agreement, a superlinear construction in any
linear-derivative equation must therefore possess roughly more than
2.31275D PERSISTENT singular domain coordinates. A large moving root set
by itself does not suffice. This corrects the earlier informal search
suggestion of merely making the separant's roots move.

## Three distinct remaining directions

### A. A large fixed singular core and non-gauge/high-degree quadratic term

This is the closest unexcluded algebraic route. Required ingredients:
(1) a persistent singular domain core larger than (3A-D)/2;
(2) a genuinely non-gaugeable A, or gauge degree large enough to defeat
(2); (3) many ACTUAL degree-D solutions agreeing on that core, not only
many isolated solutions elsewhere.

A concrete algebraic source to test is residue-coded interpolation. For
R(X)=product_{a in S}(X-a), write

    P_epsilon(X)=sum_{a in S} epsilon_a R(X)/(X-a).

These candidates have exactly P_epsilon(a)=epsilon_a R'(a). Their degree
is <=D precisely when

    sum_a epsilon_a a^j=0, j=0,...,|S|-D-2.       (3)

Thus low-alphabet residues directly give a fixed set of candidate value
branches at singular coordinates, while (3) supplies an exact degree
certificate. This is a viable formulation, but NOT yet a viable scalable
source: one needs many low-alphabet vectors satisfying a linear number
of Vandermonde moments, plus a challenge labeling making their selected
branches affine. The old quadratic Wronskian family has |S|=D+1 and
never approaches the required core size. Enlarging R without enforcing
(3) simply raises the message degree and loses the target regime.

Highest-payoff next test on this branch: derive an explicit parameterized
residue family satisfying (3) with |S|>2.313D, and prove actual agreement
before deriving its differential equation. Stop immediately if moment
depth stays bounded/logarithmic while |S| grows. This is closely related
to the existing dependent-moment gate; it does not justify another
cyclic census or another multiplicative-Sidon construction.

### B. Three or more value branches

A cubic identity T P'-P^3+RP-S=0 escapes the quadratic theorem. The same
low/high-degree division would place the naive cubic threshold at
A>7D/3, above the first-order target around1.875D. The unexcluded window
is therefore a large persistent singular core with derivative degree
between roughly2.313D and3D, where cubic terms interfere with leading
coefficient elimination. At core coordinates the cubic allows up to
three candidate values, rather than two.

Concrete next test: use the residue representation above with three
allowed residues, and attempt a coefficient identity producing many
solutions while retaining the required linear moment depth. Alternatively
start with a three-branch value product and prove high-coefficient
cancellation symbolically before counting solutions. Stop if each new
branch only increases degree or if candidate agreement is supported on
at most D shared coordinates. This is a genuinely unexcluded template,
but no scalable solution family or superlinear nearby count is in hand.

### C. Candidate-dependent singular loci in genuinely implicit equations

For a squarefree equation nonlinear in P', the separant can depend on
P and P', so the hn incidence bound for T no longer applies. This is the
most conceptually distinct escape. Repeated equations such as F^2=0 do
not qualify: remove repeated factors first, or artificial singularity
would merely hide an already-controlled equation.

A concrete diagnostic is the discriminant in v of
Q(x,z,f(x)+zg(x),v). If this is a nonzero polynomial in z, a fixed
coordinate supports singular agreements at only boundedly many labels.
Hence a superlinear example again requires MANY coordinates at which
that discriminant vanishes identically. For a quadratic in v, a
persistent repeated derivative root specifies a derivative value along
the received line, suggesting Hermite-interpolation constraints rather
than unrestricted singular freedom. Before searching examples, test
whether those constraints yield another linear bound; if they do, move
to higher jet degree or a genuinely nonrational repeated-root branch.
This diagnostic can produce a broader theorem, but it currently supplies
no lower construction.

## Priority and stop list

The highest-value constructive target is the exact agreement-first
residue/moment gate in A; it gives an explicit success condition and
prevents another quadratic isolated-solution count with no nearby
witnesses. In parallel mathematical work, C has the best prospect of a
conceptually broader upper theorem. B is a reserve mechanism, not an
excuse for an unstructured coefficient search.

Stop treating bounded-degree gauge coefficients, moving roots alone,
or larger Wronskian/Sidon solution banks as promising superlinear
sources. None currently provides a better.codes improvement or intrinsic
tightness. Direct nearest-list constructions over prime fields remain
independent of these differential-template limitations and should
continue in their separate existing exploration slot.
