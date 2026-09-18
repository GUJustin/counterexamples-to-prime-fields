# First marked splitting has at most two clusters

For the specific double-factor characteristic-three point in `RESULTS.md`, every geometric point of its homogeneous projected quadratic cone has at most two distinct velocities among the six marked coordinates. In particular, saturating this cone by all marked-velocity differences gives the empty scheme. This certificate alone concerns the first splitting order. The subsequently audited argument in `ALL_ORDER_DISTINCT_NODE_OBSTRUCTION.md` rules out a distinct-node DVR branch through this point by combining it with constant-rank normalization and simple-root uniqueness.

## Exact reduction

Use the independently verified rank-164 Jacobian, its 28-dimensional kernel, and the 12-dimensional complement to the 16 coordinate-change directions recorded in `solve.json`. Those coordinate changes are common polynomial addition, output scaling, and projective changes of the input. Their action moves the six initially coincident marks by a common velocity, so distinctness of marked velocities is unchanged on passing to this complement. Coordinate changes preserve the incidence equations and therefore preserve extendibility to second order.

Write the tangent polynomial of candidate i as R_i. Its slope at the common mark has the form

    R_i'(0) = beta + alpha*c_i + tau*d_i,

where c_i is the coefficient of U² in the base polynomial. In the tower-field encoding of `field.hpp`,

    c = [188,111,704,564,333,37,247,0],
    d = [0,1,324,39,234,8,486,0].

For marked velocities xi_s define omega_s=xi_s+alpha/2. The seven linear functions (omega_0,...,omega_5,tau) have rank seven on the twelve-dimensional complement. The five-dimensional kernel is invisible to the projected quadratic tensor, including its polar terms. Exact elimination gives

    omega_i² − omega_5² = 0,          0 ≤ i < 5,
    tau*(omega_i − omega_5) = 0,      0 ≤ i < 5,
    tau² = 0.

Over a field tau=0, and each omega_i equals omega_5 or −omega_5. Centering does not change differences, so the same at-most-two-cluster conclusion holds for xi_s. If omega_5=0 all six velocities coincide.

## Certificate and independent replay

`reduce_cone.cpp` reads `cone.in` and writes `cone.json`. Besides the active map, its right inverse and invisible kernel, the output includes eleven explicit linear combinations of the original 28 projected equations. No numerical approximation or Gröbner basis is used.

`verify_cone.py` uses the independent presentation F3[t]/Phi7(t³−t), rather than the generator's tower arithmetic. It checks all eleven linear-combination identities coefficient by coefficient in the ORIGINAL twelve tangent variables (78 coefficients each). Thus the necessary equations do not rely on trusting the intermediate active-coordinate elimination. It also checks that every omega_i−omega_j is the actual corresponding marked-velocity difference. `verify_cone.json` records PASS; the bounded replay took 0.54 seconds and 6.4 MiB.

Together with the preceding independently verified quadratic separator, the current conclusions are:

* unramified and ramification-two mixed-characteristic lifts of this point are impossible;
* for higher ramification, the homogeneous quadratic gate cannot split the six marked coordinates into six distinct first-order velocities;
* the later all-order argument rules out distinct-node branches at this point; the quadratic certificate by itself does not. No global eight-word obstruction is asserted.
