# All-order distinct-node obstruction at the archived double-factor point

This combines the constant-rank cover-family lemma with the independently replayed quadratic certificates. It concerns branches specializing to THIS characteristic-three incidence point, with its fixed cube-face labeling. It is not a global obstruction to eight-word banks at these parameters.

## Formal normal coordinates

Use the unit rank-164 minor to solve 164 incidence equations and variables over the complete unramified coefficient DVR W. There remain 28 coordinates and 28 residual equations g. The 21-dimensional repeated-factor cover family of `CONSTANT_RANK_COVER_FAMILY.md` has injective differential and can be straightened in characteristic three into z=0, with coordinates u_1,...,u_21 along it and z_1,...,z_7 normal to it. Lift this coordinate change to W.

Constant rank 164 throughout the family proves that g and its normal linear terms vanish on z=0 modulo three. Thus

    g(u,z)=3h(u)+3L(u)z+Q_u(z)+O(z³).

Here Q_u is homogeneous quadratic in z. The nonzero constant defect h(0) and the quadratic span at u=0 are precisely the cokernel data in `solve.json`, up to invertible changes of residual equations and normal coordinates. The independently checked separator annihilates the quadratic span and does not annihilate h(0).

The normal coordinates may be chosen with differentials equal to the seven active functions (omega_0,...,omega_5,tau). To see that their kernel is exactly the family tangent space, note that a family variation has marked velocity delta b and polynomial slope beta-2c_i*delta b. Thus alpha=-2delta b, tau=0 and omega_s=delta b+alpha/2=0. These functions have rank seven on the full 28-dimensional tangent space: the archived quotient calculation has rank seven, and the coordinate-change directions satisfy the same identities directly. Their kernel has dimension 21 and equals the family tangent space.

## First normal order

Suppose a mixed-characteristic DVR-valued solution specializes to the archived point and has all 48 nodes distinct. Write e=v(3). Its normal coordinates cannot vanish identically, since g(u,0)=3h(u) and h(0) is nonzero modulo the maximal ideal. Put s=min_j v(z_j)>0.

If e<2s, the nonzero leading characteristic forcing cannot cancel. If e=2s, applying the separating cokernel functional gives the same contradiction. Therefore e>2s, and the nonzero leading normal vector satisfies the homogeneous quadratic cone. Its equations imply tau=0 and omega_f in {a,-a} for some a≠0. This remains true when all six signs happen to be the same.

## Coefficient identification and simple roots

Take the repeated-factor family point with parameter u as reference. Because e>2s, its lifted characteristic-zero representatives and the implicit-function representatives differ only beyond the orders now used. Center the source coordinate at its marked center b. At order s the tangent polynomial slopes have the verified form

    beta+alpha*c_i+tau*d_i.

The term beta cancels in differences, and tau=0. Move the center once more by -pi^s*alpha/2, choosing any lift of alpha. Relative to this center, the marked leading velocities are exactly omega_f, and all polynomial differences have zero leading linear coefficient after division by pi^s. Their quadratic coefficients reduce to c_i-c_j. The c_i are pairwise distinct.

For adjacent cube vertices i,j, select any shared marked face f. Incidence gives (F_i-F_j)(x_f)=0, where x_f differs from the new center by O(pi^s). The linear coefficient at that center has valuation at least s; the quadratic and higher coefficients are integral. It follows by evaluating the Taylor expansion that the constant difference has valuation at least 2s. Consequently

    pi^(-2s)(F_i-F_j)(center+pi^s Z)

is integral. Its reduction is (c_i-c_j)Z²+k_ij, because the centered linear coefficient at order s vanishes. Evaluation at the shared marked velocity omega_f=±a determines k_ij=-(c_i-c_j)a². Thus the reduced pair difference is exactly

    (c_i-c_j)(Z²-a²).

The argument uses only the order-s derivative identity and incidence to control the initially unknown order-2s constant term. It does not assume those constants vanish or follow the cover family.

## Collision contradiction

Any two coordinate faces from different axes share an adjacent pair of cube vertices. If their marked velocities have the same sign, their scaled coordinates are roots of that adjacent pair difference with the same reduced root ±a. Its derivative there is 2(c_i-c_j)(±a), a unit. Simple-root uniqueness over the complete DVR forces the two marked coordinates to be equal.

Therefore a collection of distinct marked nodes can have, in either sign cluster, only faces from one axis, at most two faces. Two clusters cannot accommodate six distinct marked nodes. This contradicts the hypothesized branch.

## Scope and audit dependencies

The conclusion excludes all distinct-node mixed-characteristic DVR branches specializing to the archived n=48, D=11 double-factor point, with this labeling. It does not exclude branches through other special points, other incidence labelings, or global eight-word constructions.

Dependencies: the independently verified rank-164 minor and kernel, characteristic defect separator, eleven exact cone row identities (`verify_cone.py`), and the geometric constant-rank proof. The geometric proof and formal combination passed independent review; see `ALL_ORDER_INDEPENDENT_AUDIT.md`. No new computational assertion is hidden in this note.

## Equal-characteristic branches

The same conclusion holds for DVR-valued branches in characteristic three. If z=0, the branch lies on the straightened repeated-factor family and all six marks coincide. Otherwise take the first normal order s. There is no characteristic forcing, so its nonzero leading normal vector satisfies the same homogeneous cone. The coefficient and simple-root arguments apply without change, excluding six distinct marked nodes. This does not claim that the entire equal-characteristic local ring is smooth or reduced.
