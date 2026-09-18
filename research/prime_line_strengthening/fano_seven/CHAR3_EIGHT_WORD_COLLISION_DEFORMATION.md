# A concrete characteristic-three deformation target for eight words

This is a specified algebraic deformation problem, not an existence claim. It avoids requiring a higher-degree construction to remain a pullback of the cubic bank.

## Exact special fiber

Work over an algebraic closure of F3. Let zeta have order7, eta=zeta+zeta^2+zeta^4, etabar=-1-eta, and

    P(X)=eta X^3+X^2+X+etabar,
    alpha=etabar/eta,
    P_i(X)=zeta^(5i) P(zeta^(-i)X), i=0,...,6,
    P_7=0.

The compact Paley identity remains valid in characteristic3, but its second word value c=3(eta+3)/4 is zero. Thus these EIGHT cubics each agree seven times on Omega=mu7 union alpha*mu7. Every column has four matching candidates. The seven first-orbit columns match four nonzero candidates; the seven second-orbit columns match P7 and three nonzero candidates. Every pair intersects at exactly three distinct nodes.

Take the separable cubic map phi(U)=U^3-U. Its derivative is -1, and every point of Omega has three distinct preimages. The resulting42 nodes are nonzero. Set

    F_i(U)=U P_i(phi(U)), i=0,...,7,
    received(T)=T*w(phi(T)).

Each degree-at-most10 polynomial has21 prescribed core agreements. All eight vanish at0, which is outside the core domain.

Partition the candidates into complementary four-subsets A,B. Add TWO MARKED nodes x_A=x_B=0, both of word value0, assigning the first to A and the second to B. Every candidate now has22 marked agreements among44 marked coordinates. This point lies on the desired incidence scheme, but NOT its distinct-coordinate open subset. The goal is a characteristic-zero deformation separating x_A and x_B while preserving all prescribed agreements.

The cyclic order7 symmetry permits five partition types: choose A to contain P7 and a three-subset of the other seven indices; the35 triples have five cyclic orbits. Thus the first tangent test requires five specified systems, not a random search.

## Incidence scheme and dimension accounting

Use variables for eight degree-at-most10 polynomials (88 coefficients),44 node coordinates and44 word values. For every prescribed incidence impose

    F_i(x_j)-w_j=0.

There are176 variables and176 equations, with four incidences at every marked coordinate. The desired open subset requires all44 coordinates distinct and all eight polynomials distinct. Each successful point would have n44,k11 and22 agreements per polynomial, precisely quarter rate and half agreement.

The usual common-polynomial additions (11 parameters), output scaling (one), and projective change of the independent variable for sections of O(10) (three) give15 symmetry parameters. Thus a characteristic-zero solution must have at least15 dependencies among the176 equations; generic dimension counting does NOT guarantee a solution. The special fiber is deliberately singular. This mechanism introduces separate degree10 coefficients and independent motions of all42 core nodes, rather than preserving a cubic-cover ansatz.

If one instead keeps a single common eight-fold fresh node, every polynomial difference has its nine core roots plus that common root. Dividing the common linear factor returns to an eight-word degree9 bank on42 nodes. The split complementary-fourfold marking specifically avoids imposing that extra common-factor condition on the generic fiber.

## Explicit tangent and mixed-characteristic obstruction

At the special fiber, write coefficient perturbations R_i(U) of degree<=10, coordinate motions xi_j, and word motions omega_j. The linearized equations are

    R_i(T_j)+F_i'(T_j) xi_j-omega_j=0

at core incidences, and

    R_i(0)+P_i(0) xi_A-omega_A=0, i in A,
    R_i(0)+P_i(0) xi_B-omega_B=0, i in B.

Here P_7(0)=0 and the other seven P_i(0)=zeta^(5i) etabar are distinct and nonzero. A necessary equicharacteristic first-order splitting condition is a Jacobian kernel vector with xi_A-xi_B!=0. Failure excludes a first-order split at this special point, not every higher-order or ramified deformation.

There is also an explicit FIRST mixed-characteristic obstruction. Lift zeta, eta, alpha and the compact seven-polynomial construction to the unramified3-adic coefficient ring, and lift all phi fibers uniquely by their nonzero derivative. Keep F7=0. The seven nonzero candidates and their word incidences hold exactly in this lift. Only the21 core incidences of the eighth candidate fail: above alpha*zeta^t their residual is

    -T*c*zeta^(5t), c=3(eta+3)/4.

After division by3 and reduction modulo3, this residual is

    -eta*T*zeta^(5t).

All other incidence residuals are zero, including the two marked coordinates at0. Therefore the necessary mod9 lifting test is the concrete inhomogeneous linear system

    J*delta = -residual/3,

with that explicitly supported right-hand side. A left-kernel vector of J pairing nontrivially with this vector certifies failure to lift modulo9 at the chosen special point. If solvable, inspect whether a solution has xi_A-xi_B nonzero, then address higher-order lifting obstructions; solving this first system alone is not a characteristic-zero existence proof.

The equations may be formed over F_(3^18): mu7 lies in F_(3^6), and all Artin-Schreier fibers split after the further degree3 extension. No large prime or support census is required. Common-polynomial gauges can be fixed by setting the eighth polynomial identically zero, reducing the linear system by11 columns and corresponding redundant word variables if desired.

## Outcome and next exact target

The construction supplies a fully explicit characteristic-three boundary point and a five-case linear obstruction/lifting problem. No tangent systems have yet been solved. A positive split mod9 result would identify a specific deformation branch worth higher-order lifting; a negative result would be an exact local obstruction, not a universal eight-word impossibility theorem.
