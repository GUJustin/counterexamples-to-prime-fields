# Independent audit of the all-order local obstruction

**PASS**, with the exact local scope stated in `ALL_ORDER_DISTINCT_NODE_OBSTRUCTION.md`: mixed-characteristic DVR branches specializing to this archived characteristic-three point and this cube-face labeling cannot have all marked nodes distinct. This is not a global eight-word obstruction.

## Constant rank and formal coordinates

The tangent reduction is correct. Connected face incidences force one common value of all coefficient tangents at b; division by U-b then produces eight degree-at-most-ten polynomials. At core nodes the common-word derivative terms cancel, leaving precisely the pullback of the fixed two-dimensional target rowspace. The two independent rowspace generators determine node and word tangents uniquely. The resulting bundle kernel E and projection-formula count therefore compute the full tangent dimension, not merely a subspace.

The splitting pi_*O(1)=O^2+O(-1) is justified: Euler characteristic gives degree -1; absence of sections after twisting by O(-1) forbids positive summands; two global sections then force two zero summands. Tensoring by O(3) gives pi_*O(10)=O(3)^2+O(2). Hence the Jacobian nullity is constant and equals the independently certified 28.

The family differential is injective. Vanishing core motions makes delta A*B-A*delta B vanish at 42 distinct nodes, hence identically, since its degree is at most six. Coprimality, exact degree three, and B(0)=1 remove the common scalar variation. The zero base candidate determines delta C; marked positions determine delta b, and a nonzero remaining candidate determines delta l. A nonzero tangent minor consequently gives a formal smooth embedding of the 21 family parameters into the 28 remaining coordinates.

After eliminating the unit rank-164 minor, the 28 residual equations vanish on that family modulo three. Constant rank also makes every residual differential vanish along it, so the coefficients linear in the seven normal coordinates vanish identically as functions of the family parameters modulo three. This is stronger than a rank calculation only at the central point and removes the problematic family-times-normal terms. Lifting the coordinate change yields the asserted expansion with constant and linear-normal terms divisible by three.

## First normal order and reference representatives

The defect separator remains nonzero on h(0), while annihilating the quadratic span. With e=v(3) and s the first normal order, it excludes e<2s and e=2s. For e>2s the leading normal vector lies in the verified homogeneous cone. The seven active functions have kernel exactly the 21-dimensional family tangent space, so that vector is nonzero; the cone therefore gives tau=0 and omega_f=+/-a with a nonzero.

One subtle coefficient issue is harmless: the explicitly lifted family need not solve the mixed-characteristic incidence equations. It does solve them modulo three, and the implicit-function solution of the eliminated 164 equations differs from it by terms divisible by three. Since e>2s, those terms cannot change any coefficient identification through order 2s. Varying family parameters reduce to the archived point, so the leading normal slope identity and the distinct c_i are unchanged in the residue field.

## Constants and collisions

After the prescribed center shift, pairwise linear coefficient differences have valuation strictly greater than s; quadratic coefficient differences reduce to c_i-c_j. A shared marked root and its displacement of order at least s then force the constant coefficient difference to have valuation at least 2s. This is a valid inference from the polynomial Taylor expansion; it does not assume that all constant differences followed the reference family.

The scaled pair difference is integral, with reduction (c_i-c_j)(Z^2-a^2). The roots +/-a are simple. Two same-sign cross-axis faces share an adjacent candidate pair, so simple-root uniqueness identifies their actual marked coordinates. Each sign cluster can contain faces from only one axis if all nodes are distinct, hence at most two nodes; six nodes cannot fit.

Crucially, this works even if all six leading omega values are the same nonzero a. It does not require first normal order to equal first actual marked-separation order. That resolves the gap left in the earlier conditional note.

## Relation to the direct pair analysis

`PAIR_FACTOR_NORMALIZATION.md` and `edge_cycle_gate.json` show why the direct pair-degree route alone was insufficient: its first-separation residue system allows a four-cluster shape. The formal argument supplies additional constraints from the core through the complete tangent and quadratic tensors. It does not claim those constraints follow from mark incidences alone. There is therefore no conflict between the four-cluster direct calculation and the all-order obstruction.

This audit is mathematical and read-only with respect to the upper agent's files. The arithmetic dependencies remain the independently replayed rank minor, 28-dimensional kernel, 406 full-tangent quadratic identities, and the independently verified eleven cone identities.
