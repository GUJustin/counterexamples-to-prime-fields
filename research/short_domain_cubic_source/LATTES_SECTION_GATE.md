# A bounded Lattès construction audit: explicit duplication gates

No new short-domain source is constructed here. Two concrete versions of the elliptic-multiplication proposal have uniform section bounds. The distinction between a rational map preimage and a rational elliptic point is essential.

## 1. The explicit degree-four Legendre map

Let k be algebraically closed of characteristic different from two, K=k(X), and let lambda in K be nonconstant. On

    E_lambda: y²=u(u−1)(u−lambda),

the duplication x-map is

    R_lambda(u)=(u²−lambda)²/[4u(u−1)(u−lambda)].       (1)

A polynomial section P of a finite constant fiber c satisfies

    (P²−lambda)²=4cP(P−1)(P−lambda).                  (2)

This is already an actual rational first-integral construction: differentiating R_lambda(P)=c produces a common first-order differential equation of bounded jet degree. However its polynomial sections are severely restricted.

Treat (2) as a quadratic in lambda. Its discriminant is

    16c(c−1)P²(P−1)².

The two roots therefore have the form

    lambda=aP²+(1−a)P,
    a=1−2c±2sqrt(c(c−1)).                           (3)

Their two a-values have product one, so a is nonzero, including the cases c=0 or1. They satisfy c=−(a−1)²/(4a). Completing the square gives

    lambda−c=(sqrt(a)P+(1−a)/(2sqrt(a)))².           (4)

All constants used here belong to k. The identities need no degree/characteristic comparison and do not rely on Frobenius.

If lambda is rational but not polynomial, (3) makes polynomial P impossible. If lambda is a nonconstant polynomial, two different constants c,d supporting polynomial sections would produce polynomial squares U²=lambda−c and V²=lambda−d. Then

    (U−V)(U+V)=d−c

is a nonzero constant, forcing U,V and lambda to be constant, a contradiction. Thus at most one finite constant fiber has polynomial sections. Its numerator equation has degree four in P, giving at most four sections total.

The possible denominator values P=0,1,lambda do not create spurious sections for nonconstant lambda: the numerator of (1) is nonzero at each such rational-function value. A nonconstant rational map over constant coefficients, in contrast, can only take a constant value on constant P, so the constant-lambda case supplies merely constant polynomials.

**Conclusion:** the standard Legendre duplication model with any nonconstant lambda in k(X) has at most four polynomial sections across all finite constant fibers, and none if lambda is not polynomial. This applies in every odd characteristic, including p much larger than D.

For context, even allowing rational P in this fixed Legendre model gives at most two finite constant fibers. Three values would make lambda−c_i squares in k(X), and their product would give a nonconstant rational parametrization of the smooth genus-one curve y²=product_i(t−c_i), impossible by Lüroth's theorem. This auxiliary rational-section statement is not needed for the polynomial bound.

## 2. General Weierstrass duplication from rational elliptic points

Now let char k be zero or p>3 and consider a nonsingular curve

    E: y²=u³+A(X)u+B(X),  A,B in K.

Its duplication map is

    R(u)=[u^4−2Au²−8Bu+A²]/[4(u³+Au+B)].           (5)

Suppose rational points T_i in E(K) have polynomial x-coordinates P_i of degree≤D and their doubles have distinct finite CONSTANT x-coordinates c_i. Then

    c_i³+A c_i+B=y([2]T_i)² in K.                (6)

This is a cubic square-value problem in the constant label, rather than the degree-two pencil addressed in the earlier gate.

### Primary theorem and height condition

Pasten–Wang, *Extensions of Büchi's Higher Powers Problem to Positive Characteristic*, [Theorem 3](https://people.math.harvard.edu/~hpasten/preprints/PWposIMRN.pdf), applies over the genus-zero field K to a monic degree-three polynomial at M>11*3−3=30 distinct constant arguments. Take multiplicity parameter mu=2. A squarefree cubic with nonconstant coefficients cannot have31 square specializations if its nonconstant irreducible factors are separable and not in K^p[C]: the theorem would force their multiplicities to equal two. In characteristic zero the extra restrictions are automatic. In characteristic p>3 they follow if its projective coefficient height is less than p, by factor-height additivity and the fact that a nonconstant p-th power has height at least p.

The cubic C³+A C+B is squarefree because E is nonsingular. Thus31 labels in (6), under this height condition, force A,B to be constant.

### Eight polynomial preimages supply the needed height bound

No initial bound on the rational coefficients A,B is required. Eight distinct labels with polynomial preimages of degree≤D reconstruct the rational map (5). Form the8-by9 matrix with rows

    (P_i^4,P_i³,P_i²,P_i,1,−c_iP_i³,−c_iP_i²,−c_iP_i,−c_i).

Its rank over K is eight. Indeed two numerator/denominator pairs of degrees≤(4,3) agreeing on these eight distinct P_i have a cross-difference of degree≤7 with eight roots. It vanishes identically, and coprimality of the actual pair forces proportionality. Coprimality follows from nonsingularity: at a root u of the cubic denominator, the numerator equals (3u²+A)², which vanishes only at a repeated root of that cubic. The exact numerator and denominator degrees are4 and3.

The column degree caps sum to16D. Signed maximal minors therefore provide a polynomial representative of every rational-map coefficient with degree at most16D. The subvector corresponding to the coefficients of u^4,u²,u in the numerator is proportional to

    (1,−2A,−8B).

Consequently h(1,A,B)≤16D. In positive characteristic p>max(3,16D), this is strictly below p and the preceding application of the primary theorem is justified.

Therefore, if A,B are not both constant, there are at most30 constant target labels realized by rational points of this kind. Each quartic fiber of (5) has at most four distinct polynomial x-preimages, so the total bank has size at most120. If A,B are constant, any rational P with R(P) constant is itself constant. Such a bank has at most n/a members agreeing a times each with a received word on n coordinates, since the supports of different constants are disjoint.

This rules out a growing fixed-gap bank from actual rational-point duplication in characteristic zero or the specified short-characteristic regime. It is not a general bound on the Mordell–Weil rank: most rational points have nonconstant x([2]T), and therefore do not belong to a constant first-integral fiber.

## 3. The genuinely unexcluded twist possibility

A rational x-preimage P satisfying R(P)=c need NOT be the x-coordinate of a rational point of E(K). Its y-coordinate may require a quadratic extension. Thus (6) must not be inferred merely from the rational map equation.

One can see the missing square class explicitly. When c+2P is nonzero, solve (5) for B and substitute into c³+A c+B to get

    c³+A c+B=(−A−2c²−2cP+P²)²/[4(c+2P)].        (7)

The factor c+2P can carry a nontrivial square class. Distinct sections could require different quadratic twists, and the cubic square-value theorem does not apply automatically to that collection. The exceptional case c+2P=0 has constant P and should be treated separately rather than divided away.

Accordingly the remaining concrete target would be many degree≤D polynomials P_i, distinct constants c_i, and ONE pair A,B satisfying (5), with differing twist classes (7), together with a common received word and a fixed agreement surplus. No such family or surplus is produced here. X-dependent changes of the elliptic x-coordinate can also change which target values are constant and which sections are polynomial; the standard Legendre bound must not be carried through such a change without tracking those conditions.

Neither result is a generic rational-coordinate Dickson obstruction. They address a new explicit degree-four elliptic multiplication mechanism and identify exactly where it fails, and where a different mechanism would still be needed.
