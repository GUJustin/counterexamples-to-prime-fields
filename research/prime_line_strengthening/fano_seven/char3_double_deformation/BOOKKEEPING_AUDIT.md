# Independent double-root cube-mark bookkeeping

Assume the already verified characteristic-three core has eight polynomials P_i(psi(U)), degree at most nine, on 42 distinct nonzero coordinates: each has 21 agreements, and every pair has nine common agreement coordinates. Put F_i(U)=U^2 P_i(psi(U)). Then degree is at most eleven; the old word is multiplied by U^2.

Index the eight candidates by the vertices of the three-dimensional binary cube. Add six marked nodes, initially all zero, with supports given by the two four-vertex halfsets in each coordinate direction. Each candidate receives exactly three marked incidences, giving 24 agreements on 48 labelled nodes. There are 192 incidence equations. Coefficients contribute 8*12=96 variables; node and word variables contribute 48 each, also 192 in total.

A pair of vertices at Hamming distance h shares exactly 3-h marked supports. Following a successful separation, its forced common roots would number 9+(3-h)=12-h, namely 11,10,9 for h=1,2,3. All are compatible with degree eleven. Initially all pairs have the common root zero of multiplicity at least two; the adjacent pairs use both multiplicities after splitting. Pair-degree counting alone therefore supplies no obstruction.

At each marked node F_i(0)=F_i'(0)=0. Consequently all six mark-position columns in the first-order incidence Jacobian vanish. Arbitrary distinct first-order velocities of these nodes are tangent directions. This is a substantive difference from the previous single-root/two-mark construction.

Write a formal perturbation F_i+pi R_i+pi^2 S_i and marked coordinate pi xi_s+pi^2 eta_s. Its order-two value is

    P_i(psi(0))*xi_s^2 + R_i'(0)*xi_s + S_i(0).

Thus the first nonlinear mark-separation equations form an auxiliary system of eight quadratics evaluated at six velocities, with each quadratic constrained on its three cube-face nodes. Their leading coefficients are prescribed by the special fiber. This statement uses Hasse coefficients and remains valid in characteristic three. Mixed-characteristic defects and core equations must be imposed separately; free tangent velocities alone do not prove a lift.

Scope: this is a bookkeeping and Taylor audit, not a numerical solver certificate or existence proof. Upper agent owns the solver; no competing job was launched.
