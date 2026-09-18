# Positive genus in the Paley norm net

**Subsequent sharpening:** independent residual-discriminant reconstruction proves generic genus exactly15 on the stated ordinary/simple-boundary open chart. See `../residual_discriminant/RECONSTRUCTION_INDEPENDENT_AUDIT.md`. The genus≥9 argument below remains a separate conservative geometric check.

The three symmetric eigenbasis members are not rational: their normalization genus is at least six. A general member of the characteristic-zero net has genus at least nine. These statements do **not** exclude special rational members elsewhere in the parameter plane. In particular, no conclusion about the entire rational locus follows from checking the three basis curves.

## Source and reduction

The section class on F_3 is D=10C_0+34F, with C_0²=-3. Thus D²=380 and arithmetic genus162. The fourteen prescribed points have multiplicities4 at seven quadruple-word points and6 at seven triple-word points. The associated square sum is364 and delta lower bound is147.

The independent interpolation certificate gives rank217 in220 columns modulo29. Therefore the characteristic-zero interpolation kernel has dimension exactly three: there are217 equations, and a217-minor is a unit at this prime. The kernel is free and reduces onto the displayed mod29 kernel. The mu7 action splits it into three one-dimensional character spaces, with characters1,3,5. This splitting is compatible with reduction because7 is a unit. Consequently each displayed eigenvector lifts to a characteristic-zero eigenvector with the same character support. All boundary coefficients used below are units, so the boundary polygons and squarefreeness conclusions persist. The modular irreducibility checks in `../factors.json`, together with a rational smooth toric boundary place, ensure geometric irreducibility of these special members and of their characteristic-zero lifts.

## Ordinary prescribed singularities

`boundary.py` computes the three homogeneous tangent cones at one representative of each orbit. Their common homogeneous gcd is one, so blowing up the prescribed point leaves no common basepoint on its exceptional curve. The sum of the three tangent cones is squarefree and has full degree4 or6. Thus ordinary singularities are a nonempty open condition at these points. Symmetry transports this verification to all fourteen points (the parameter combination witnessing the condition need not be the same after transport). Over the infinite characteristic-zero field the fourteen open conditions hold simultaneously for a general member.

## Generic net: genus at least nine

There is no fixed curve component, since the geometrically irreducible eigenbasis members are distinct. Resolve the remaining base locus, including infinitely near points, with generic multiplicities b_j. After the first fourteen blowups the square budget is16. The resolved moving system is basepoint-free and hence nef, so

    sum_j b_j² <=16.

Bertini in characteristic zero makes a general resolved member smooth. Its extra delta is exactly sum_j b_j(b_j-1)/2. Under the square budget16 this is at most6: a multiplicity4 exhausts the budget and contributes6; a multiplicity3 leaves at most7 and contributes at most3+1=4; if all multiplicities are at most2, the total is at most4. Multiplicity-one points contribute no delta. Therefore

    g_generic >=162-147-6=9.

This rules out the hypothesis that the net generically carries the extra15 delta needed for rationality. It does not bound delta jumps on special members.

## Three eigenmembers: a sevenfold-cover obstruction

For character r=1,3,5 put T=X^7 and Z=X²Y. After removing a Laurent monomial, the equation becomes f_r(T,Z)=0. The explicit polynomial is saved in `boundary.json`. Each quotient Newton polygon has22 interior lattice points. Its two prescribed torus singularities contribute at least6+15=21, so the quotient normalization has genus at most one; this observation is not needed for the lower bound below.

All edge polynomials are squarefree with nonzero endpoints. They therefore give smooth, transverse boundary branches on a toric resolution. The valuations of T, with multiplicities of the corresponding boundary places, are:

* r=1: 7,3,0 (four places),-1,-7,-1 (two places).
* r=3: 7,2,0 (four places),-2,-7,-1,1.
* r=5: 7,1,0 (four places),-3,-7,1 (two places).

Thus each quotient has exactly four boundary places where ord(T) is not divisible by seven. Interior torus places have ord(T)=0. The original curve is the Kummer cover X^7=T, with Y=Z/X². It is geometrically connected (in particular, T has a valuation prime to seven), and each of those four places is totally ramified. Tame Riemann--Hurwitz yields

    2g-2 = 7(2g_quotient-2)+4*6,
    g = 7*g_quotient+6 >=6.

The quotient genus bound above then leaves only g=6 or13 for each eigenmember. Determining which value occurs would require checking additional quotient singularities; it is unnecessary for excluding rational eigenmembers.

The same branch-count proof works in characteristic29 and on the characteristic-zero lifts: the edge coefficients and discriminants used in the certificate remain nonzero. A linear edge supplies a rational smooth boundary point, which also makes the finite-field irreducibility-to-geometric-irreducibility implication transparent.

## Reproducibility and open target

`boundary.py` independently reconstructs the tangent cones, character supports, quotient Newton hulls, and every edge polynomial from `../gate.json`. It checks squarefreeness exactly modulo29 and records all data in `boundary.json`. The bounded run took0.54 seconds. No Sage or Singular computation, rental, or unbounded elimination was needed.

The remaining positive-construction target is a **special nonsymmetric member** of this two-parameter net whose normalization genus drops to zero and whose branches realize the required incidence fibers. Neither the generic lower bound nor the eigenmember obstruction eliminates that locus.
