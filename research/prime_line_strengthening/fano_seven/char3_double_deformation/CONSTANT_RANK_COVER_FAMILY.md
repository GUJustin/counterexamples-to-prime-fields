# Constant rank on the repeated-factor cover family

**Resolution:** the normalization and all-order combination are now proved and independently audited in `ALL_ORDER_DISTINCT_NODE_OBSTRUCTION.md` and `ALL_ORDER_INDEPENDENT_AUDIT.md`. Any remaining-gap language below records the earlier proof stage.

Work in characteristic three and near the archived point. Keep the base eight-cubic bank, fourteen base nodes, and four-candidate incidence mask at each node fixed. Let pi=A/B be a degree-three rational map, unramified over those nodes, with 42 distinct finite preimages. Let b avoid the preimages and let l be nonzero. Consider

    F_i=C+l(U-b)² B³ P_i(A/B),

with deg C≤11, deg A,deg B≤3, and B(0)=1. All six marked nodes equal b. This is a 21-parameter family (12+4+3+2).

**Claim.** The full 192-by-192 incidence Jacobian has rank 164 throughout this open family. The argument is algebraic and does not require the rational cubic map to give an automorphism of the source line.

## Tangent reduction

Write R_i for a polynomial coefficient tangent. At the coincident marks F_i'(b)=0. The face incidences force all R_i(b) to equal a single scalar c: the face hypergraph is connected. The six marked word tangents are determined by c, while the six marked node tangents are free. Consequently

    R_i=c+(U-b)S_i,       deg S_i≤10.

At a core preimage U=t of a base node a, all four matched P_i(a) agree. In differences of derivatives, terms differentiating C, (U-b)², and B³ therefore cancel, leaving

    F_i'(t)-F_j'(t)=l(t-b)² B(t)³ pi'(t) [P_i'(a)-P_j'(a)].

The scalar is a unit. After an invertible change of node and word tangent variables, the core incidence condition on the vector (S_i(t)) is exactly membership in the fixed two-dimensional subspace spanned by the all-ones vector and the vector of base derivatives P_i'(a), restricted to the four matched candidates. These two vectors are independent at every archived base node. Thus the core node and word tangents are uniquely determined once the S_i satisfy these two linear conditions per node.

Define E as the kernel of the evaluation map O^8 → ⊕_a k_a² on the target projective line, using those two linear conditions at each of the fourteen nodes. This is a locally free elementary modification. The allowable S vectors form

    H^0(P1_source, O(10) tensor pi^*E).

The scalar trivializations used for O(10) do not affect homogeneous vector membership in the fixed rowspaces.

## Cover-independent dimension

For every degree-three map pi, the rank-three bundle pi_*O(1) splits as

    O ⊕ O ⊕ O(-1).

Indeed its Euler characteristic is two, hence degree -1; it has two global sections, and its twist by O(-1) has no global sections because that pullback is O(-2). These facts force the displayed splitting by the splitting theorem for bundles on P1. Since O(10)=O(1) tensor pi^*O(3), projection formula gives

    pi_*O(10)=O(3)² ⊕ O(2).

Writing h_d=dim H^0(E(d)), the dimension of allowable S vectors is therefore 2h_3+h_2, independent of the map. Including c and the six free marked node tangents, the full Jacobian nullity is

    7+2h_3+h_2.

At the independently certified archived point this nullity equals 28. Hence it equals 28 throughout the stated open family, proving rank 164.

## Formal use and remaining scope

The family has injective differential: zero core motions imply delta A*B-A*delta B, of degree at most six, vanishes at 42 nodes and hence is zero; the normalization and coprimality fix the rational-map variation. Candidate 7 is zero before adding C, so its zero coefficient tangent forces delta C=0. The remaining polynomial tangents and the marked center then force delta l=delta b=0. Thus the family is a smooth 21-dimensional immersed formal subspace.

After using the unit 164-minor to eliminate the corresponding equations and variables, one can straighten this family in characteristic three into coordinates (u_1,...,u_21,z_1,...,z_7). Constant rank shows that the remaining equations and all their first z-derivatives vanish at z=0 in characteristic three. In mixed characteristic their constant and linear-normal coefficients are divisible by three. This removes the previously identified uncontrolled family-parameter times transverse-parameter terms modulo three.

It does NOT by itself identify the first transverse order with the first actual marked-separation order. The computed cone permits all six centered velocities to coincide and be nonzero. Thus an all-order distinct-node obstruction still requires the pair-factor argument or another control of such directions. This note does not claim that final obstruction.
