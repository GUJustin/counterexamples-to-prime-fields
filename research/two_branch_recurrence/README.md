# Agreement-first triangular Riccati bound

September17,2026. Working theorem, awaiting independent audit; no novelty
claim and no main-manuscript integration yet.

For T monic of degree t>2D, deg_X R<=t-2, deg_X S<=t+D-1,
deg_z R<=1, deg_z S<=2, and char0 or p>D, actual solutions of

    T P'-P²+R P-S=0, deg P<=D

have at most4D+4 isolated challenge labels. The nonconstant coefficients
of P are polynomial functions of z of degrees at most D+1; only its
constant coefficient remains. The residual locus lies on a plane curve
of bidegree at most(D+1,2). No z-denominators or separant assumption occur.

For any received line on n distinct points and A>D, actual nearby
solutions have full common witnesses outside at most

    4D+4+3n(D+1)/(A-D)+2n

labels. This is O(n) at a fixed positive agreement excess. The proof treats
persistent nonlinear components, affine codeword graphs and isolated
points separately using actual agreement incidences.

A corollary closes the ENTIRE unnormalized polynomial two-branch family
T P'=(P-F_z)(P-G_z), where T is the domain locator, n>4D, and F_z,G_z
are affine received branches of X-degree<n. Either there are at most two
labels, the triangular theorem applies, or one branch is a codeword
pencil and high agreement forces all remaining solutions onto another
codeword pencil. This extends the previously closed zero-branch case.

This is a restricted family theorem, not a general first-order linear
MCA theorem or an intrinsic tightness result. See PROOF.md for quantified
statements, proof, and the precise remaining scope.

`verify_symbolic.py` derives the triangular coefficients independently
in SymPy, checks the residual bidegrees for D1..4, and attains the degree
sequence D+1,...,2. It checks an isolated zero fixture by Groebner basis,
a persistent nonlinear c²=z component, and failure of the top pivot
outside the characteristic guard.

`verify_finite.py` independently exhausts29968 polynomial--label pairs,
including genuine domain agreements, persistent codeword pencils, and a
nonlinear persistent component whose many solutions are mostly not near.
Both watchdog runs completed within384MiB/60seconds. These finite checks
corroborate the formulas; the quantified argument is in PROOF.md.
