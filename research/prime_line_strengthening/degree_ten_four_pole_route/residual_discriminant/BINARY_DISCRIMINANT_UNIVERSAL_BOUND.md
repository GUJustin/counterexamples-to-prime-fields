# A boundary-independent binary-discriminant condition

The open-boundary restrictions in the first proposal are unnecessary for the following **necessary** rationality condition. This note does not compute the resulting parameter locus or assert the existence of a rational member.

Let C be a geometrically integral, reduced degree-ten multisection of F_3, with no fiber component, in class10C_0+34F. Suppose its fourteen specified finite points have multiplicity at least4 at seven points and at least6 at seven points. Work in characteristic zero or29. Let Delta be the binary-fiber discriminant section, and divide by the fixed base divisor of exponents12 and30 to obtain the homogeneous base binary form D(S,T) of degree48.

**Necessary condition.** If the normalization of C is rational, then

    deg gcd(D_S,D_T) >=15.

The gcd is homogeneous over an algebraic closure. A zero discriminant is treated separately as automatically satisfying the degeneracy test; it is not divided through. For the geometrically integral separable curves in this statement Delta is nonzero.

## 1. Primitive binary equations at every base place

At any base point complete the local base ring to a DVR R with algebraically closed residue field. Trivialize the P1 bundle and the defining line bundle. The equation is a homogeneous binary form of fiber degree ten with coefficients in R. Its reduction is not the zero form: otherwise the fiber would be a component of C. Choose a constant projective fiber coordinate whose point at infinity avoids the finite set of roots of this reduction. The new leading coefficient is a unit.

After scaling by that unit, C over this base neighborhood is represented by a monic degree-ten polynomial. Thus its coordinate algebra is a finite flat rank-ten R-order. This construction includes points originally at fiber infinity; changing fiber coordinates has unit determinant and changes the local binary discriminant only by a unit. There is no assumption that the original affine leading coefficient is squarefree or nonvanishing.

Let Abar be the normalization of this order. The discriminant-index identity is

    ord Delta = total local different + 2 length_R(Abar/A).

Over the algebraically closed residue field the length is precisely the sum of the plane-curve delta invariants at all points of that fiber. This is also valid when the normalization has several branches. Singularities at the base point X=infinity are included in exactly the same manner. The cover is separable and tame in characteristic29 because its degree is ten.

## 2. Global degree and removal of the prescribed index

For class10C_0+34F, arithmetic genus is162. The finite-flat order has determinant degree -171, hence its discriminant section has degree342. Equivalently this is the coefficient calculation18*34-3*90.

A reduced plane-curve singularity of multiplicity m has delta at least m(m-1)/2, without any smooth-branch or unramified-projection hypothesis. The prescribed points therefore contribute at least147 to the normalization index. Their doubled contributions give the fixed degree294 discriminant divisor. After removing it, the residual degree48 divisor is locally

    ord_v D = r_v + 2 k_v,

where r_v is the nonnegative local different contribution and k_v is the remaining nonnegative normalization index after subtracting the specified lower bounds at that fiber. Rational normalization gives total different18 by Riemann--Hurwitz. Hence

    sum_v k_v = (48-18)/2 =15.

The sum runs over all base places, including infinity. Repeated tangents, singular branches, and ramified selected branches are all covered by this identity. They cannot be discarded as exceptions, but they do not invalidate the necessary condition.

## 3. Homogeneous derivative gcd

At a root of D with multiplicity e=r+2k, the common factor of the two homogeneous partial derivatives has multiplicity at least e-1. If k≥1 then e-1≥k; if k=0 the desired bound is zero. A characteristic-dependent derivative cancellation can only increase this common factor. Summing gives degree gcd(D_S,D_T)≥sum k=15.

The Euler identity48D=S D_S+T D_T is valid with48 invertible in characteristic zero and29. Thus the gradient gcd has no extraneous roots outside D. The homogeneous formulation handles every affine degree-drop and every infinity root without saturating away those strata.

Concretely, both partial derivatives are binary forms of degree47. Their homogeneous Sylvester matrix has size94. The necessary condition can be imposed as rank at most79. A zero partial derivative is allowed; both partials vanish only if D=0 in these characteristics. This formulation is global on the projective parameter plane. It may be computationally more expensive than open-chart subresultants, but it avoids an unproved removal of boundary strata.

For an affine residual polynomial d(X) of degree d, a weaker directly usable inequality is

    deg gcd(d,d') + max(47-d,0) >=15.

In characteristic zero this is exactly the homogeneous repeated-root count. In characteristic29 an infinity multiplicity divisible by29 may contribute an additional common factor, so this displayed affine inequality remains a valid necessary condition through the direct local estimate (its infinity term e-1 still bounds k). The homogeneous gradient condition is the cleaner exact encoding.

## 4. Lower actual class and artificial vertical factors

If the actual primitive class is10C_0+(30+c)F with c<4, then arithmetic genus is126+9c and its discriminant degree is270+18c. If the same multiplicities remain on the primitive curve, the prescribed index147 forces c≥3. For rational normalization its remaining true index is15-9(4-c).

Embedding its equation into class34 multiplies the binary form locally at infinity by a base parameter to the power4-c. The degree-ten discriminant acquires the factor of order18(4-c). This can be accounted for as an artificial index9(4-c) at infinity. The homogeneous degree48 residual then again has total (true plus artificial) excess index15, so the same necessary gradient-gcd bound holds. This is bookkeeping for a class drop, not permission to ignore arbitrary fiber components at selected nodes: those could lower the multiplicities of the primitive curve itself.

In the actual Paley net there is no such class drop. Its three weighted boundary polynomials are

    23 Z^8+10 Z,   15 Z^9+7 Z²,   20 Z^10+2 Z³

modulo29, with disjoint supports; every nonzero combination has actual weighted degree34. Their characteristic-zero character supports and unit boundary coefficients give the same conclusion there. The leading-Y10 projection is injective, so every nonzero net member also retains fiber degree ten. Members with finite vertical content or other reducibility are outside the geometrically integral norm-curve statement and require separate component analysis.

## Scope

This strengthens the initial necessary condition to all boundary strata of proper geometrically integral members, including selected-branch ramification. It does not make the condition sufficient, does not produce an integral ideal-membership certificate, and does not transfer a modular empty locus to characteristic zero automatically.
