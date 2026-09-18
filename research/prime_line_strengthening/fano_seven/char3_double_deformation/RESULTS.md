# Double-factor eight-word collision: all-order local obstruction

This is a different marked degeneration from char3_deformation. It does not inherit that point's smooth-special-fiber argument.

## Setup

Use the characteristic-three Paley eight-cubic bank Pi, i=0,...,7 with P7=0, and phi(U)=U^3-U. Put

    F_i(U)=U^2 Pi(phi(U)), degree at most11.

The42 core coordinates are the three separable preimages of each of the14 base nodes. The core word is U^2*w(phi(U)), and each candidate has21 core agreements. Add six marked coordinates, all initially0, corresponding to cube coordinate halfsets

    {i in {0,...,7}: bit_j(i)=b}, j=0,1,2, b=0,1.

Each candidate belongs to three halfsets, giving24 marked agreements out of48. Generic distinct coordinates would give length48, dimension12, half agreement and eight candidates. The192 defining equations have192 variables:96 polynomial coefficients,48 coordinates and48 word values.

A pair of candidate labels at Hamming distance h shares3-h marked nodes. Its nine core intersections plus these are11,10 or9, within the degree11 budget. This avoids the immediate pair-root obstruction to splitting too many nodes from a simple common factor.

## Exact computed gates

The Jacobian rank is164 and its nullity28. All six fresh coordinate columns are zero, since F_i'(0)=0. Thus arbitrary fresh coordinate motions are tangent directions; in particular0,1,2,zeta,zeta+1,zeta+2 are an explicitly verified distinct choice.

The unramified mod9 system is inconsistent. The exact forcing comes from the compact seven-bank lift, with only the21 zero-candidate second-orbit rows nonzero:

    rhs=eta*T^2*zeta^(5t).

A left-null obstruction vector is saved. Unlike the simple-factor point, the tangent kernel has extra directions beyond the obvious cover/common-factor family, so its former complete-local-ring argument does not apply.

For ramification degree2, remove the16 explicitly checked gauge directions (12 common-polynomial additions, output scaling, three projective-coordinate directions). A12-vector complement remains. The Hasse-quadratic correction is

    Q_ij(v)=F_i^[2](T_j)*xi_j^2+R_i'(T_j)*xi_j.

Its projection to the28-dimensional left kernel has78 quadratic coefficient columns. Their linear span has rank11, and the characteristic defect is OUTSIDE that span. An explicit28-entry separating functional is saved as quadratic_left_obstruction. Hence even allowing3=lambda*pi^2 for any nonzero residue-field lambda, the ramification-two equation cannot hold. This conclusion does not require solving the Veronese relations or imposing distinct fresh velocities.

## Reproducibility and limits

`solve.cpp` and `field.hpp` use the tower F729[theta]/(theta^3-theta-zeta), with Phi7(zeta)=0. `solve.json` saves every core node/word/mask, coefficient vector, exact forcing, kernel and left-kernel bases, a nonzero164-minor index set, the12 tangent-complement vectors, full28×79 projected quadratic augmented matrix, and both obstruction certificates. All original incidences and internal certificate identities are checked during the run. Runtime is under one second; the shell-wrapper RSS sample should not be treated as an accurate peak.

Independent reconstruction and replay passed, including the rank minor, full-kernel quadratic separator, and eleven cone identities. The geometric/formal extension was independently audited in `ALL_ORDER_INDEPENDENT_AUDIT.md`: **no DVR branch through this specific point has all marked nodes distinct**, in mixed or equal characteristic three. See `ALL_ORDER_DISTINCT_NODE_OBSTRUCTION.md` and `CONSTANT_RANK_COVER_FAMILY.md`. The finite certificates alone establish the initial gates; the all-order conclusion additionally uses the constant-rank family and simple-root uniqueness. This is a local obstruction, not a global eight-word list bound.
