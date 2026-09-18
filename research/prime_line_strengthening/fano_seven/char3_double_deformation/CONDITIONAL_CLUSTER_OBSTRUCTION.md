# Conditional all-order collision lemma

**Resolution:** the normalization and all-order combination are now proved and independently audited in `ALL_ORDER_DISTINCT_NODE_OBSTRUCTION.md` and `ALL_ORDER_INDEPENDENT_AUDIT.md`. Any remaining-gap language below records the earlier proof stage.

This note isolates a valid implication. The valuation normalization needed to apply it to every branch has not yet been proved.

Let R be a complete discrete valuation ring with residue characteristic three. Label eight polynomial candidates by cube vertices and six marked nodes by coordinate faces. Assume all face incidences hold. Suppose there are a center b, a positive integer s, and a nonzero residue a such that:

1. Each marked coordinate has the form b+pi^s z_f, with reduction z_f in {a,-a}.
2. For every pair of distinct candidates i,j, the polynomial pi^(-2s)(F_i-F_j)(b+pi^s Z) has coefficients in R and reduces to (c_i-c_j)(Z²-a²).
3. The eight residues c_i are pairwise distinct.

Then the six marked nodes cannot all be distinct.

Indeed, two coordinate faces from different axes have two common vertices i,j. Their marked nodes are both roots of the same scaled difference polynomial. If they belong to the same sign cluster, that polynomial has derivative 2(c_i-c_j)(±a), a unit, at their common reduced root. The usual simple-root uniqueness argument therefore identifies the two nodes. In a collection of distinct nodes, all faces belonging to one cluster must consequently have the same axis. There are only two faces of each axis. Each cluster has at most two distinct nodes, whereas there are six nodes and only two clusters.

This proof also works over a noncomplete valued field after completing it. It uses no assumption that the roots are rational over the initial residue field.

## Relation to the computed cone

The computed cone gives two centered velocities ±a and a vanishing residual slope tau. Its slope relation says that the noncommon linear coefficient of each candidate is alpha*c_i. After centering, it disappears. Whenever the first separating scale has a nonzero a, the incidence value at either sign then determines the noncommon constant coefficient to be -c_i*a². This gives precisely the reduced pair-difference polynomial in hypothesis 2, provided all lower-order noncommon coefficients have first been removed or shown divisible by the appropriate powers of pi.

The c_i in the present certificate are pairwise distinct. Thus the remaining difficulty is a formal valuation normalization theorem, not the cube-face collision step.

## Normalization gap

A natural equicharacteristic family has dimension 21:

    F_i(U)=C(U)+l*(U-b)²*P_i^hom(A(U),B(U)),

where deg C≤11, deg A,deg B≤3, B(0)=1, and l is a unit. Its parameters number 12+4+3+2=21. The core nodes are the lifted roots A-a_core*B, and all six marked nodes equal b. This agrees numerically with the 16 coordinate-change directions and five invisible directions of the quadratic calculation.

Dimension agreement alone does not justify successively removing this family to arbitrary valuation order. One must establish a formal transverse presentation in which, uniformly along the family, (i) normal linear terms vanish in characteristic three, (ii) the leading quadratic normal terms retain the proved cone form up to units and coordinate changes, and (iii) the characteristic-defect separator remains a unit. In particular, an unproved assertion that the Jacobian rank is constantly 164 along this family cannot be used silently. Terms involving a family parameter times a transverse parameter could otherwise precede the pure quadratic term at the chosen valuation.

If those conditions hold, the first transverse order s is constrained as follows: e<2s is excluded by the nonzero characteristic forcing; e=2s is excluded by its separation from the quadratic span; e>2s gives the homogeneous cone. One must additionally distinguish a genuinely separating transverse direction from a direction whose centered marked velocities all vanish. The latter does not yet define the first marked-separation scale.

No all-ramification obstruction is claimed in this note.
