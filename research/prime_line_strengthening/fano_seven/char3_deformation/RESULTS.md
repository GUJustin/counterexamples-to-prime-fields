**Subsequent exact local theorem:** `FORMAL_LOCAL_OBSTRUCTION.md` combines independently verified rank minors and the mod9 certificate with an explicit smooth20-parameter special-fiber family. It excludes every mixed-characteristic formal branch through these five points, and shows the marked nodes cannot separate even equicharacteristically. The degree2/3 calculations below remain useful checked intermediate data.

# Exact local obstruction for the eight-word collision special fiber

All five cyclic partition types have the following exact computed data:

| Triple mask (zero candidate added) | Jacobian rank | Nullity | Mod9 consistent | First-order node split |
|---|---:|---:|---|---|
|7|156|20|no|no|
|11|156|20|no|no|
|13|156|20|no|no|
|19|156|20|no|no|
|21|156|20|no|no|

The field is F729[theta]/(theta^3-theta-zeta), where zeta satisfies Phi7. The base polynomial is irreducible over F3 because3 has order6 modulo7; the Artin-Schreier extension is irreducible since Tr_F729/F3(zeta)=-1. Coordinates are encoded as c0+729c1+531441c2, with base coefficients encoded in ternary in the zeta basis.

`solve.cpp` reconstructs and verifies every original incidence, all42 distinct nonzero core nodes,21 matches per candidate and9 intersections per candidate pair. It builds each176×176 Jacobian and the mixed-characteristic defect from CHAR3_EIGHT_WORD_COLLISION_DEFORMATION.md, and performs tracked exact elimination. `solve.json` saves an explicit left-null obstruction lambda with lambda*rhs nonzero, an explicit row-space expression for xi_A-xi_B, the20-dimensional kernel basis and the20-dimensional left kernel. Thus the no-split assertion is a linear identity, not simply a solver boolean.

## Ramification degree two

The15 ordinary gauge directions (11 common-polynomial additions, one output scaling and three projective-coordinate directions) were constructed explicitly and checked in the kernel. A five-vector complement gives15 quadratic monomials. For a tangent direction v=(R_i,xi_j,omega_j), the Hasse-quadratic incidence correction is

    Q_ij(v)=F_i^[2](T_j)*xi_j^2+R_i'(T_j)*xi_j.

The20×15 projection of this tensor to the left kernel is identically zero in every case, whereas the projected characteristic defect is nonzero. Hence the necessary equation for a lift with3=pi^2,

    J*delta2+Q(v)=rhs,

has no solution.

This conclusion has a stronger independently checked certificate: the specific obstruction functional lambda vanishes on Q(v) for EVERY tangent vector. `verify.py` independently reconstructs the data in the different field presentation F3[t]/Phi7(t^3-t), verifies all20 saved kernel vectors and their independence, and checks all210 coefficients of lambda*Q on that basis. It also verifies lambda*J=0, lambda*rhs!=0 and the row-space identity for xi_A-xi_B for all five cases. This bypasses any need to assume a gauge-quotient invariance property for the obstruction calculation. The Jacobian rank156 is additionally certified by separately reconstructed nonzero156×156 minors in verify_minors.json, computed in the independent univariate field presentation.

## Artifacts and scope

- `solve.cpp/json/log/resources.json`: exact systems, elimination and certificates; bounded run about0.56 seconds. The shell-wrapped runner undersamples child RSS, so its very small reported peak should not be interpreted as actual solver memory.
- `verify.py/json/resources.json`: independent field arithmetic and direct certificate identities,40.38 seconds,93952KiB peak RSS, under384MiB/60sec guard.

The obstruction tensors by themselves do not address arbitrary ramification. The subsequent formal-family theorem does settle every ramification degree at these specific points. Other special points and support mechanisms remain open; no global characteristic-zero eight-word impossibility or positive construction follows.
