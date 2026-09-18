# The five collision points have no characteristic-zero formal branch

## Theorem (local, for these five marked incidence points)

Let k=F_(3^18), and consider the incidence scheme over W(k) for eight degree-at-most10 polynomials,44 marked coordinates and44 word values, with the176 prescribed incidences of CHAR3_EIGHT_WORD_COLLISION_DEFORMATION.md. For each of the five cyclic partition representatives7,11,13,19,21, let s be its specified characteristic-three collision point.

The completed local incidence ring at s is isomorphic, as a W(k)-algebra, to

    k[[z1,...,z20]].

In particular3 vanishes in this completed ring. There is no mixed-characteristic formal branch through s, regardless of ramification degree. Moreover the two marked fresh coordinates remain equal in every formal deformation through s, including equicharacteristic deformations. This theorem concerns these explicit special points, not all eight-word constructions or all characteristic-three banks.

## Exact finite certificates

The Jacobian has rank156 in each case. The independent implementation `verify_minors.cpp` uses arithmetic in F3[t]/Phi7(t^3-t), different from the original tower-field solver. `minor_input.py` reconstructs the Jacobian from the defining polynomials and incidence masks, then extracts the saved156×156 row/column minors. Their nonzero determinants, encoded in the base3 polynomial basis1,t,...,t17, are

    mask7:146422208; mask11:220118361; mask13:86328690;
    mask19:171462975; mask21:266406886.

The verified20 independent kernel vectors prove the matching upper bound on rank. The row/column indices are in solve.json; reconstructed minor inputs and verifier outputs are rank_minors.in and verify_minors.json. The independent bounded minor run completed in0.59 seconds.

For each case an explicit left-null vector lambda is saved and independently checked against the original Jacobian. Its pairing with the mixed-characteristic defect/3 is nonzero, so the point has no lift modulo9. In the independent polynomial basis this pairing (up to the sign convention of the right-hand side) is

    [2,1,0,0,2,1,2,0,1,1,1,2,2,2,2,0,0,2].

The defect calculation follows from the exact compact Paley lift: the seven nonzero candidates satisfy their incidence equations integrally; only the21 zero-candidate rows on the second orbit have defect divided by3 equal to -eta*T*zeta^(5t). Thus the saved linear certificate is an obstruction for the actual defining equations over W(k), not an arbitrary forcing vector.

## A smooth20-parameter family in the special fiber

Keep the characteristic-three base cubics P_i fixed and write their binary homogenizations as P_i^hom(A,B), including P_7^hom=0. Choose

    deg A<=3, B=1+B1 U+B2 U^2+B3 U^3,
    L=L0+L1 U, deg C<=10,
    H_i(U)=C(U)+L(U)P_i^hom(A(U),B(U)).

There are4+3+2+11=20 parameters. The base point is A=U^3-U, B=1, L=U, C=0. For each old base node a, the three core coordinates are the uniquely specified formal roots of A-aB near their original values; these exist since their derivative at the base point is -1. Their received values are

    C(T)+L(T)B(T)^3*w(a).

Both marked fresh coordinates are the root -L0/L1, with received value C(-L0/L1). All176 incidences hold identically in characteristic3, for every choice of the complementary four-subsets at the coincident node.

The tangent map of this20-parameter family into the176 ambient variables is injective. If its image is zero, every core coordinate motion vanishes. Therefore

    delta A(T)-A(T)delta B(T)=0

at all42 distinct core nodes. This polynomial has degree at most6 and hence is identically zero. Since deg A=3, deg delta A<=3 and delta B has constant coefficient0, it follows that delta B=delta A=0. The zero candidate H7=C then forces delta C=0. Any nonzero other base cubic gives delta L*P_i(A)=0, hence delta L=0. Thus the family has20 independent tangent directions and fills the entire Jacobian kernel.

## Formal implicit-function argument

Use a certified156×156 Jacobian minor to select156 equations and156 variables. The formal implicit-function theorem over W(k) solves these variables in terms of the remaining20 variables z. The completed local ring becomes

    W(k)[[z1,...,z20]]/(g1,...,g20),

where the g_i are the remaining residual equations.

Reduce modulo3. The explicit special-fiber family maps into this presentation. Its projection to the20 free variables has invertible tangent map: the family tangent space is the full kernel, and projection of that kernel to the free variables is an isomorphism by the chosen minor. The formal inverse-function theorem makes this parameter map an automorphism of k[[z]]. Since all residual equations vanish on the family, every g_i reduces to the zero power series. Hence each g_i is divisible by3.

At least one g_i(0) is not divisible by9. Otherwise, after the implicit solutions of the selected156 equations, setting the free variables to zero would supply a solution of ALL equations modulo9, contradicting the saved left-null obstruction. Thus one g_i=3*u with u a unit power series. All residuals are divisible by3 and one generates3, so their ideal is exactly(3). This proves the displayed completed-ring isomorphism.

Finally, the family has equal marked fresh nodes identically, and its formal parameter map is an isomorphism after reduction. Their coordinate difference therefore vanishes in the completed local ring itself. The inability to separate the nodes is an exact local statement, not merely a first-order observation.

## Earlier obstruction calculations

The projected quadratic tensor and the projected cubic tensor both vanish identically, while the characteristic defect does not. These calculations were independently replayed (`verify.py` and `verify.py --cubic`; the latter checked all20×35 projected cubic coefficients in50.87 seconds and about100MiB). They correctly obstruct ramification degrees2 and3, but are no longer needed for arbitrary ramification once the formal-family argument is combined with the rank and mod9 certificates.
