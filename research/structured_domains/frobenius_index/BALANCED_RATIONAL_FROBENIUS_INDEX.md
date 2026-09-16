# Balanced rational maps: use the Frobenius index instead of the subgroup size

September16, 2026. Proof complete and self-reviewed; exact finite checks
passed. Integrated into Theorem 2.8 and Appendix E of the official manuscript
after a second self-review; no claim of novelty or independent coauthor
proof review is made.

The later `NEAR_BALANCED_RATIONAL.md` extends this to coverage defect c
under n>6(B-1+c), with free action when c<B/2. The manuscript now
uses that stronger version. The original balanced proof follows.

## Statement

Let F be a finite field of odd characteristic p, containing D=mu_n. Suppose

    p=ell*n+epsilon,       epsilon in {1,-1},       ell>=6.

Let R in F(X) have rational degree B, no poles on D, and exactly B distinct
points in each fiber of its restriction to D. If B>=2 and

    n>6(B-1),

then the geometric extension Fbar(X)/Fbar(R) is Galois. Since ell>=6,
p>n, so the earlier balanced Galois classification applies: up to output
Möbius relabeling, R is a power quotient or a free twisted-inversion quotient.
B=1 is immediate without the inequality.

At p=2130706433, n=262144, epsilon=1 and ell=8128. The condition covers
all integer degrees B<=43691. Full balance forces B to divide n, so it
covers every possible dyadic degree through32768. Degree65536 remains
outside this sufficient criterion. This is a structural restriction,
not a numerical better.codes improvement or an arbitrary-list bound.

## 1. Saturation of each collision component

The reduced collision curve H(X,Y)=A(X)V(Y)-A(Y)V(X), for R=A/V, has
bidegree(B,B) and exactly nB points on D squared. Remove all deck graphs. Each deck map preserves mu_n because every
fiber meeting mu_n is entirely contained there. The preceding Möbius
classification therefore makes each graph Y=zeta*X or XY=zeta.
Let their number be g>=1 and put
D0=B-g. They contribute ng distinct subgroup points, and do not intersect
any other component at these points: all relevant fibers are unramified.

For a remaining component of bidegree(a_i,b_i), its subgroup-point count
satisfies N_i<=n*min(a_i,b_i), by either coordinate projection. The degree
sums are both D0, while sum N_i=nD0. Consequently every component has

    a_i=b_i,              N_i=n*a_i.

This uses only full balance and reducedness. In particular, each component
has coordinate degrees at most B-1. Its logarithmic Euler characteristic
chi, after removing coordinate zeros and poles on its normalization,
satisfies chi<=2*a_i^2.

## 2. A four-term unit equation

Fix one non-torus component, with function field K=k(x,y), where k is an
algebraic closure of F. Put u=x^n and v=y^n. The coordinate maps x,y have
degree at most B-1<p, so they and u,v are separating. In particular,

    [K^p(v):K^p]=p.

Put w=(u-1)/(v-1). Outside the coordinate zeros and poles, u-1 vanishes
if and only if v-1 vanishes. Indeed, if x is in D, the complete geometric
fiber of R(x) consists entirely of D, so y is in D, and conversely.
Both zeros are simple: the full fibers are unramified, and both coordinate
projections of the collision curve are étale at such points. Thus w has
zeros and poles only in the coordinate boundary S. The four functions

    -1,                 u,                 w,                 -w*v

are S-units and sum to zero. We next prove that their span over K^p has
dimension3, which is the separability condition needed for a three-row
ordinary Wronskian.

## 3. Linear independence from the Frobenius index

We claim the three functions

    w=(u-1)/(v-1),          1,          u,

are linearly independent over K^p.

Suppose otherwise. Clearing v-1 gives a nonzero polynomial P(U,V) over
K^p of bidegree at most(1,1), with P(u,v)=0. Explicitly,
P=A*(U-1)+(B+C*U)*(V-1); its four coefficients show that it is zero
only when A=B=C=0.
Any common factor in the two coefficients of P as a polynomial in U
has degree at most1 in V and cannot vanish at v. Remove it. If P were
independent of U, it would already contradict the degree-p minimal
polynomial of v. Thus P defines a rational graph U=T(V). Here T is
nonconstant, since u is separating and hence is not in K^p.

Set c=x^p and d=y^p, which belong to K^p. The identity p=ell*n+epsilon
gives

    x=(c/u^ell)^epsilon,       y=(d/v^ell)^epsilon.

Therefore u,v also satisfy the rational equation

    R((c/U^ell)^epsilon)=R((d/V^ell)^epsilon).

After clearing coprime denominators, its polynomial G(U,V) has bidegree
at most(ell*B,ell*B). All its coefficients belong to K^p because k is
perfect. If P and G were coprime, their resultant in U would be a nonzero
polynomial over K^p of degree at most2*ell*B in V, vanishing at v.
But

    2*ell*B < p

follows from n>6(B-1), B>=2, and ell>=6. This is impossible. Hence P
divides G, giving the rational-function identity

    R((c/T(V)^ell)^epsilon)=R((d/V^ell)^epsilon).

Rational degrees multiply under composition. Both outer maps have degree
ell*B, so T must have degree1: it is a Möbius transformation.

## 4. The exceptional rational graph must be a torus graph

Work temporarily over an algebraic closure of K^p. Choose a^ell=c and
b^ell=d, and define

    F0(Z)=R(Z^(epsilon*ell)),        M(Z)=a/T(b/Z).

The identity just obtained says F0(M(Z))=F0(Z). Thus M is a deck
transformation of F0. Its deck group has order at most ell*B<p, and
contains the cyclic group of ell-th-root scalings. It is therefore a tame
finite subgroup of PGL2 containing an element of order ell>=6.

The tame finite-subgroup classification gives cyclic, dihedral, A4, S4,
or A5. The last three have no element of order at least6. In a cyclic or
dihedral group, an element of order at least3 has the rotation subgroup's
unique pair of fixed points. Our scalings fix {0,infinity}, so every deck
map preserves this pair. Hence

    M(Z)=zeta*Z        or        M(Z)=zeta/Z.

The deck maps of F0, which is defined over the algebraically closed
constant field k, are themselves defined over k. Indeed, a deck map
takes each k-point into its geometric F0-fiber, all of whose points lie
in k. The images of three distinct k-points determine the Möbius map.
Thus zeta lies in k.

In the first case u/v=a/(zeta*b). Raising to ell yields

    (x/y)^(ell*n)=(x/y)^p/zeta^ell,

so (x/y)^epsilon=zeta^ell and x/y is constant. In the second case uv=ab/zeta,
and the same calculation makes xy constant. Either conclusion says the
original component is a torus graph, contrary to its selection. This
proves the three-function linear independence.

## 5. Elementary unit-equation height bound

Write the four S-units as f0,f1,f2,f3, with sum zero. Any three are
linearly independent over K^p, by the preceding argument and the one
displayed relation. Their ordinary Wronskians are nonzero and differ
only by sign. Multiplying a Wronskian with rows of derivative orders
0,1,2 by (dt)^3 gives a well-defined rational cubic differential Omega.

At a place P in S, choose the three functions that omit a function of
smallest valuation. In a local parameter, differentiation loses at most
one order each time, so

    ord_P(Omega) >= sum_(i=0)^3 ord_P(f_i)
                    - min_i ord_P(f_i) - 3.

Outside S all functions and their local derivatives are regular, so
ord_P(Omega)>=0. Each f_i has divisor of degree zero supported on S.
Summing the inequalities, and using deg(div(Omega))=3*(2g-2), gives

    H := -sum_P min_i ord_P(f_i) <= 3*(2g-2+|S|)=3*chi.

Because the tuple contains a nonzero constant and u, its projective
height H is at least deg(u)=n*a_i. Since chi<=2*a_i^2, we obtain

    n*a_i <= 3*chi <= 6*a_i^2.

This forces n<=6*a_i<=6*(B-1), a contradiction. No non-torus
component remains. There are B deck graphs, so R is geometrically Galois.

Explicitly, W(1,u,w)=(u')^2*(w'/u')'. If it vanished, then
w'/u' and w-(w'/u')u would both lie in K^p, contradicting the
proved independence. This uses u' nonzero and the fact that K^p is
the constant field of the derivation. The displayed
local calculation supplies the needed height inequality directly; no
characteristic-zero S-unit theorem is silently imported.

## Sources, checks, and limitations

The approach was prompted by the linear-independence and Wronskian method
in [Corvaja--Zannier, JEMS15(2013), Proposition2, pp.1939--1940](https://ems.press/journals/jems/articles/10688).
The proof above supplies both its Frobenius-index independence step and
the four-term unit-equation valuation bound directly.
The tame PGL2 classification is recalled in
[Beauville, Finite subgroups of PGL(2,K), Introduction](https://math.univ-cotedazur.fr/~beauvill/pubs/PGL%282%29.pdf).

The checker verify_rational_frobenius_index.py independently checks the pinned arithmetic,
enumerates small finite-field deck groups of R(X^ell), and verifies nonzero
three-function Wronskians on rationally parametrized non-torus cubic
collision components in both signs p=ell*n+/-1. These finite checks
supplement the proof and do not establish a classification by themselves.
Its certificate rational_frobenius_index_verification.json reports passed.

An additional exhaustive checker, verify_balanced_rational_pencils.py,
examines27273130 disjoint pairs of complete fibers on five small domains.
Every degree-B rational map with two complete fibers A,B is, up to output
Möbius transformation, P_A/P_B, so this enumerates the entire relevant
rational-map family on those domains. The cases satisfying the theorem
have only the cyclic and free dihedral pencils. Two cases outside its
hypotheses have9 and32 other pencils respectively, confirming that the
test can detect non-Galois maps. Evidence:
balanced_rational_pencils_verification.json. The latter build/check took
5.6seconds with106672KiB sampled RSS; counting was suspended and resumed
automatically during this sequential check.

The index ell>=6 and complete-fiber hypotheses are substantive. This
argument does not cover the full norm-one circle n=p+1, whose index is1,
nor an arbitrary n prime to p. The earlier general-characteristic bound
remains useful outside the two congruence classes. The known non-Galois
cubic on mu6 over F13 has ell=2 and violates the large-domain condition.

The resulting classification covers every fixed-map full-fiber construction that could have the required
number of distinct supports at the pinned parameters. Indeed, the remaining
dyadic block sizes have at most4 fibers, hence at most16 unions of fibers,
far below the required274980728111395088 labels in the locator/pole construction. This last observation
only concerns unions of complete fibers of one fixed map, optionally
with one fixed core; varying the map or allowing partial fibers remains
outside the argument.
