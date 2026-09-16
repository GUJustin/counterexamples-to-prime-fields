# Complete rational fibers covering a punctured subgroup

September 16, 2026. Proof complete and twice self-reviewed; finite checks
passed. Integrated as the strengthened Theorem 2.8 and Appendix E.
No independent coauthor review or novelty claim is asserted. This is
a structural exclusion, not a better.codes score improvement.

## Theorem

Let D=mu_n in a finite field of odd characteristic p, with

    p=ell*n+epsilon, epsilon in {1,-1}, ell>=6.

Let R be a rational function of degree B>=2. Suppose T is a union of
complete geometric fibers of R, each consisting of B distinct points,
with T contained in D and |D\T|<=c. If

    n>6*(B-1+c),                                      (1)

then R is geometrically Galois and all its deck maps are
X -> zeta*X or X -> zeta/X with zeta in mu_n. If additionally c<B/2,
the deck group acts freely on D, every fiber on D has B points, and B|n.
An output Möbius change can move all poles off D, since the field has
more than n elements; this does not change the hypotheses.

## 1. Collision components without the saturation step

The reduced collision curve R(x)=R(y) has bidegree (B,B), and contains
the diagonal. Each other component has coordinate-map degrees
a,b<=B-1. There are no vertical or horizontal components because R is
nonconstant. Separability follows from B<p. A component's normalization
has genus at most (a-1)(b-1).

Consider a component which is not a torus graph x/y=constant or
xy=constant. Put u=x^n, v=y^n, w=(u-1)/(v-1). Both x and y, and hence
u and v, are separating: their degrees are positive and less than p.

## 2. The extra boundary has controlled size

At a point with x in T, the complete geometric fiber lies in T, so y
also lies in T, and conversely. All those fibers are unramified.
The collision curve is smooth at their pairs and both projections are
étale, so u-1 and v-1 have simple zeros which cancel in w.

Consequently w has zeros and poles only at coordinate zeros/poles or
above x in D\T or y in D\T. Call this enlarged boundary S. The first
part has at most 2a+2b places, and the second at most c(a+b). Therefore

    chi=2g-2+|S| <= 2ab+c(a+b).                       (2)

This replaces the balanced argument's chi<=2a^2. No equality a=b or
saturation of the projection-point bound is needed.

## 3. Frobenius independence is unchanged

The three functions 1,u,w are independent over K^p, where K is the
component's function field over the algebraic closure. The proof in
Sections 3–4 of the published BALANCED_RATIONAL_FROBENIUS_INDEX.md
uses only the collision equation, 2*ell*B<p, and ell>=6; it does not
use balanced fibers or equality of the coordinate degrees. Inequality
(1) implies 2*ell*B<p just as in the published proof.

Explicitly, a dependence would yield a nonzero bidegree-(1,1) equation
P(u,v)=0 over K^p. Using x^p,y^p and p=ell*n+epsilon gives another
equation of bidegree at most (ell*B,ell*B). A nonzero resultant would
have degree <p in the separating function v, which is impossible.
Thus the first equation is a rational graph u=T(v). Degree multiplication
makes T Möbius. After adjoining ell-th roots of x^p,y^p, it gives a
deck map of R(Z^(epsilon*ell)). Its tame deck group has order at most
ell*B<p and contains the ell-th-root scalings. The tame PGL2
classification, with ell>=6, forces all deck maps to preserve {0,infinity}.
The resulting scaling or inversion makes x/y or xy constant, contrary
to the chosen component. This proves the required independence.

## 4. Height rules out every non-torus component

The four S-units -1,u,w,-wv sum to zero, and any three are independent
over K^p. The ordinary three-row Wronskian argument in the published
proof gives their projective height H<=3chi. The tuple contains u,
and v is a ratio of two of its coordinates; the height of either
function is at most H. Hence

    n*max(a,b) <= H <= 6ab+3c(a+b)
               <= [6*min(a,b)+6c]*max(a,b).

This implies n<=6*(B-1+c), contradicting (1). Thus all collision
components are torus graphs. Their bidegrees are (1,1), so there are
B deck graphs and the extension is geometrically Galois.

Every deck map sends T into T. Since T is nonempty, evaluating a torus
deck map at one point of T shows that its scaling constant lies in mu_n.
Thus the full deck group preserves D, even though this was not assumed.

## 5. Small defect forces free action and complete balance

The rotation subgroup has order b dividing n. If there are inversions,
the full group has order B=2b; otherwise all nontrivial deck maps are
rotations and act freely on D. A nonzero finite point is fixed by no
nontrivial rotation and by at most one inversion. Thus its stabilizer
has order at most two, and a nonfree orbit has B/2 points.

Every such orbit lies outside T: its geometric fiber has only B/2
distinct points, whereas T is a union of B-point fibers. Therefore
c<B/2 rules out all nonfree orbits. All orbits on D then have B points,
which proves B|n and full balance. The cutoff is strict: inversion on
mu_15 has one fixed point and seven two-point fibers; its defect is
1=B/2 and B does not divide 15. This example can be taken over F_181,
where ell=12 and n>6*(B-1+c).

## Why check this extension for better.codes?

The saved arithmetic in near_balanced_candidate_parameters.json identifies
three hypothetical packet choices just above degree 512. At the same
14 top-coefficient constraints their naive ledgers would pass the required
bank count and raise agreement:

    degree 513, coverage defect 1:  A=139792, score about 116.106;
    degree 514, coverage defect 4:  A=139809, score about 116.083;
    degree 516, coverage defect 16: A=139843, score about 116.039.

They require complete rational fibers covering all but 1, 4, or 16
points of the fixed multiplicative domain. Each satisfies (1) and c<B/2,
but none of 513,514,516 divides n=262144. The theorem therefore rules out the required maps, before any protocol or formal
certificate work. These numbers are hypothetical ledgers, not attained
agreements or improved scores. Arbitrary partial fibers and substantially
incomplete coverage remain outside this statement.

## Verification and scope

`check_near_balanced.py` compiles the C++17 pencil checker, verifies
26,880 integer inequalities, and exhausts 1,823,695 disjoint pairs of
complete fibers on four small domains. In particular, it finds 2,106
qualifying positive-defect pencils on mu_27 over F_163, all with torus
deck groups. The maximum degree-three coverage on mu_25 over F_151 is
12 of 25 points. Negative controls outside the hypotheses detect nine
and 32 non-torus balanced pencils. Three planted ramified examples check
the strict free-action cutoff and the distinction between Galois action
and full balance.

The finite check supplements the geometric proof; it is not a proof of
the general statement. The earlier balanced proof remains a special
case. The resource record reports a sequential 384 MiB watchdog run;
RSS is sampled, not an exact high-water mark.
