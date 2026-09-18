# Pair-factor normalization without a transverse family

This is an independent partial replacement for the normalization hypothesis in `CONDITIONAL_CLUSTER_OBSTRUCTION.md`. It proves the required integrality of scaled differences, but not their common centered quadratic shape.

## Exact edge factorization

Let a valued-field deformation preserve the 42 distinct core nodes and all cube-face incidences. Each cube-edge pair of candidates shares nine specified core coordinates and two marked coordinates belonging to different axes. If all six marked coordinates are distinct, these eleven roots exhaust the degree-eleven difference. Therefore

    F_i(U)-F_j(U)=a_ij * product_{nine core roots}(U-t) * (U-x_f)(U-x_g).

The leading coefficient a_ij is a unit: reduction of the core product is nonzero at zero, and the coefficient of U^2 of the special-fiber difference is c_i-c_j, which is nonzero. The distinct core coordinates are units and remain separated from the marked cluster.

Choose b to be one marked coordinate and s the minimum valuation of any marked difference; extend the value group if necessary. All marks satisfy x_f=b+pi^s z_f, with at least two distinct residues. Substitute U=b+pi^s Z and divide the edge difference by pi^(2s). The exact factorization proves integrality and gives reduction

    (c_i-c_j)(Z-zbar_f)(Z-zbar_g).

Here c_i denotes the special-fiber U^2 coefficient. Since the cube-edge graph is connected, summing edge differences proves the same coefficientwise integrality for every candidate pair. Thus, after subtracting one common polynomial, every candidate has a reduced quadratic

    q_i(Z)=c_i Z^2 + l_i Z + d_i

(up to adding the same quadratic to all candidates). Its values satisfy all six cube-face incidences at the reduced marked coordinates. This argument works at arbitrary ramification index and requires no formal family normalization or constant-Jacobian-rank assertion.

## What it does not prove

It does not force l_i=beta+alpha*c_i or force all pair differences to be multiples of one centered quadratic. Those conclusions in the homogeneous cone calculation use the full core equations and the special tangent-space structure. They cannot be inferred merely from pairwise distinct c_i and the cube faces.

For example, over any characteristic-three field containing a transcendental element z, take the six face coordinates

    (0,1), (z^3,z^3+z), (z^4,z^4+z^2),

and the common word value x^3 at a face coordinate x. For each cube vertex, interpolate the three selected face values by a quadratic. Its leading coefficient is the sum of its three selected coordinates:

    c_i=z^3+z^4 + bit_0(i) + bit_1(i)*z + bit_2(i)*z^2.

All eight leading coefficients and all six coordinates are distinct. Every adjacent difference has exactly its two common-face roots. Thus the unrestricted six-face quadratic system permits complete separation even with pairwise distinct leading coefficients. This example does not match the specific eight c_i of our special point and is not a deformation of its core.

## Precise remaining obstruction

The remaining problem is whether the particular vector

    [188,111,704,564,333,37,247,0]

(in the archived tower encoding) permits such a six-face quadratic realization, or whether the full core equations force its slopes onto the affine span of the c_i at the first separating scale. The pair-factor argument removes the lower-order integrality gap, but does not establish that stronger slope constraint. A proof must either eliminate the marked quadratic system for this fixed vector, or transport the core-induced slope relation to the first separating valuation scale. The previous all-ramification conditional collision lemma remains conditional until one of these steps is supplied.
