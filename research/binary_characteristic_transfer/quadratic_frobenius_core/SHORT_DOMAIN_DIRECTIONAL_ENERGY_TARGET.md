# A sufficient directional-energy target for two short fifth-power blocks

2026-09-18. Exact conditional construction; no point set satisfying the superlinear-energy target is supplied here.

Let p≥7 be prime with 5|(p²+1), let B=Fp² inside E=Fp4, and choose primitive xi in E. Put eta=xi⁵. Let S⊂B* have m elements. Retain all five preimages of each tag in S on each block:

    D0={x:x⁵∈S}, D1={x:x⁵∈eta S}.

These are disjoint, n=10m, and the code has dimension k=6. Define (f,g)=(x^(5p),0) on D0 and (eta^(1−p)x^(5p),1) on D1. The fifth-power map permutes B.

## Exact energy-to-label correspondence

For each norm-one a∈B, let I_a=image(y↦y^p−ay). Write

    l_a(b)=|{y∈S:y^p−ay=b}|, b∈I_a.

These are exactly the parallel affine-line intersection counts in the prime plane B. A canonical polynomial q=aX⁵+b at label lambda=b−eta*v has agreement

    5(l_a(b)+l_a(v)).

Every nonzero such label has exactly one triple (a,b,v), since the planes I_a+eta I_a intersect only at zero. Zero has the p+1 triples (a,0,0). Consequently the number of nonzero canonical labels reaching threshold T is EXACTLY

    sum_a #{(b,v)∈I_a²:5(l_a(b)+l_a(v))≥T}
       − #{a:10*l_a(0)≥T}.

Pairs are ordered. Distinct parallel lines and repeated lines both count. If R_r(a)=#{b:l_a(b)≥r} and E_r(S)=sum_a R_r(a)², then at T=10r there are at least

    E_r(S)−Z_r,  Z_r=#{a:l_a(0)≥r}≤floor(m/r)

nonzero qualifying labels. The last bound uses disjoint nonzero rays through the origin, not the weaker p+1 subtraction. Thus E_r(S)=omega(m), r=Theta(sqrt m), gives a superlinear label count if all noncanonical witnesses are excluded.

For two distinct weighted tag sets, replace l_a by the retained physical weights w_i on each fiber. The exact paired threshold count is sum_a #{(b,v):w_0(a,b)+w_1(a,v)≥T}, with zero-instance duplication removed. If each single-block weight is≤U and the required source gap is g=T−U>0, every qualifying pair lies on g-rich fibers on BOTH sides. Therefore the necessary count bound is sum_a R_0(a)R_1(a). Conversely, thresholds r_0+r_1≥T give that energy as a sufficient canonical-instance count, up to zero duplication. Necessity and sufficiency use different richness thresholds in general.

## The extra curve-intersection parameter

Let L(S) be the largest intersection of S with an affine Fp-line in B. Define C(S) as the maximum of

    |S ∩ c{z⁵:z∈ell}|

over c∈B*, and affine Fp-lines ell⊂B not passing through zero. Counting points, not curve descriptions, is essential.

The existing Kummer proof gives a sharper punctured-domain conclusion. A noncanonical degree≤5 polynomial has at most one coefficientwise-B branch across the ten branches. On the other nine branches it has at most five matches each. On the good branch its two conjugate equations either meet in at most 25 points, or its normalized polynomial is (az+b)⁵ with a,b nonzero. In the latter case matches satisfy z^p=az+b, whose solution set is an affine prime line (or at most one point); in tag coordinates this is a scaled fifth-power image of that line. The line cannot pass through zero because b≠0. Consequently every noncanonical witness has agreement at most

    U_nc=max(25,C(S))+45.

The max(25,...) should not be silently dropped for small sets. The normalization factor c is included in C(S), so the bound covers every physical branch and received label.

Canonical witnesses outside the double-fiber bank have at most max(5L(S),10) matches. Hence, if

    T>max(5L(S),10,U_nc),

all the nonzero labels counted above have singleton threshold lists. Every label outside the union of the p+1 canonical planes has agreement between 5L(S) and max(5L(S),10,U_nc). There are explicit distinct outside labels 1+eta*z0 and 2+eta*z0 for z0∈B\Fp. They yield two individually far endpoints after affine reparameterization, and the number of successful labels is preserved.

If U_nc≤5L(S) and 5L(S)≥10, every outside word has exact agreement A=5L(S), and ordinary common agreement is also exactly A. Indeed a nonconstant degree≤5 explanation of g has at most ten matches; a constant explanation restricts to one block, bounded by the same single-block estimates. A largest line fiber with zero explanation of g attains A. No claim that ordinary line richness by itself controls U_nc is valid.

## One numerical asymptotic target

The following explicit sufficient conditions isolate a concrete combinatorial problem. Suppose m→infinity, S⊂Fp²*, and

    1.12 sqrt(m) ≤ L(S) ≤ 1.16 sqrt(m),
    C(S) ≤ 5.5 sqrt(m),
    r=ceil(0.66 sqrt(m)),  E_r(S)=omega(m).

For sufficiently large m, U_nc≤5L(S), so the construction has exact source/common agreement A∈[5.6,5.8]sqrt(m), singleton threshold T=10r=(6.6+o(1))sqrt(m), and omega(n) successful labels. The threshold is below Johnson sqrt(5n)=sqrt(50m). The source agreement exceeds the full low-rate first-order bound

    n*a1(6/n) ≤ sqrt(30m)+(30m)^(1/4)

for sufficiently large m. The loss is at least (0.8+o(1))sqrt(m), and its ratio to the capacity margin T−6 is bounded away from zero (at least 0.8/6.6 asymptotically). These are sufficient constants, not optimized ones. The alphabet is E, not the prime field.

## Why the global Kummer bound alone cannot finish this target

Without C(S), the existing bound is p+45. To place T below Johnson while excluding that bound requires m>p²/50. Thus it cannot certify the intended genuinely short-domain regime m=o(p²). This does NOT prove that dense sets have only linear energy: their mean line size may itself exceed r, giving many rich lines and superlinear energy. In particular, applying a centered-variance estimate without checking r>m/p would be invalid.

In the genuinely short regime m=o(p²), r=Theta(sqrt(m)) does exceed m/p. The centered variance then gives E_r(S)=O(p sqrt(m)), which still allows omega(m). That is the open combinatorial range isolated here.
The actual constructive task is therefore to produce a prime-plane set with superlinear directional rich-line energy AND the stated line and fifth-power-image caps. A grid may furnish a curve cap, but its energy must be counted separately; descriptions of many curves or supports are not distinct labels.


## Conditional incidence barrier

This target cannot be supplied by a set whose rich lines satisfy a uniform Euclidean-form incidence estimate with the finite-plane density term. Precisely, suppose for the r-rich line family H, writing q=|H|, one has

    I(S,H) <= K*(m^(2/3)*q^(2/3)+m+q+m*q/p)

with absolute K, while m=o(p²), m tends to infinity, and r>=c*sqrt(m). The left side is at least r*q. For sufficiently large m, the q and m*q/p terms can be absorbed into the left side. Splitting the remaining two terms shows q=O_{K,c}(sqrt(m)). Since R_r(a)<=m/r, it follows that

    E_r(S) <= (m/r)*q = O_{K,c}(m).

Thus a positive superlinear target must violate this particular uniform incidence estimate on its rich-line family. This is a conditional elementary implication, not an assertion that the displayed estimate is known over prime fields or that any named conjecture has been settled. It explains why transferring Euclidean grid constructions cannot suffice and why the unrestricted point-set target may itself be difficult.
