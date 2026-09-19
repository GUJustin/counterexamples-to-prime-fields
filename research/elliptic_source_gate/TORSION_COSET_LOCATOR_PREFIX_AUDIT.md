# Elliptic torsion cosets: exact locator prefixes and small-order audit

September 18, 2026. **PASS for the identities and scoped counts below.** This is complementary to the received-line/syndrome audit: it neither constructs a common received line nor excludes arbitrary parameter-dependent residual cofactors.

## 1. The support bank and normalized Vélu formula

Work on \(E:y^2=x^3+Ax+B\) in characteristic zero or characteristic different from \(2,3,\ell\), with all \(\ell\)-torsion available and \(\ell\) odd prime. Put
\[
\mathcal D=x(E[\ell]\setminus\{O\}),\quad
n=(\ell^2-1)/2,\quad
\Phi_\ell(X)=\prod_{x\in\mathcal D}(X-x).
\]
For a cyclic subgroup \(H\) of order \(\ell\), set
\[
K_H(X)=\prod_{Q\in(H\setminus\{O\})/\{\pm1\}}(X-x(Q)),
\qquad D_H=K_H^2.
\]
The normalized Vélu map has \(x\)-coordinate \(N_H/D_H\), where
\[
\frac{N_H(X)}{D_H(X)}
=X+\sum_{Q\bmod\pm1}
\left(\frac{6x(Q)^2+2A}{X-x(Q)}
 +\frac{4y(Q)^2}{(X-x(Q))^2}\right).
\]
This follows by pairing \(Q,-Q\) in the defining translation sum; the normalization is the one in [Moody–Rasmussen, §2.1](https://arxiv.org/html/1210.2743#S2.SS1). In particular
\[
\deg N_H=\ell,\quad\deg D_H=\ell-1,\quad
N_H=XD_H+V_H,\quad\deg V_H\le\ell-2.
\]

For each nonzero coset of \(E[\ell]/H\), modulo sign, let \(\xi\) be the \(x\)-coordinate of its image under the isogeny. Its exact monic locator is
\[
F_{H,\xi}=N_H-\xi D_H.
\]
It has \(\ell\) distinct roots. There are \(h=(\ell-1)/2\) such fibers. Two distinct fibers give
\[
U_{H,\xi,\zeta}
=N_H^2-sN_HD_H+tD_H^2,\qquad
s=\xi+\zeta,\quad t=\xi\zeta.
\]
The retained-complement locator is \(C_{H,\xi,\zeta}=\Phi_\ell/U_{H,\xi,\zeta}\), of degree \(n-2\ell\).

For \(\ell\ge5\), the exact number of different omitted sets, and hence different retained complements, is
\[
(\ell+1)\binom h2=\frac{(\ell+1)(\ell-1)(\ell-3)}8.
\]
To check distinctness across subgroups, lift an omitted set back to \(E[\ell]\). It is a union of four \(H\)-cosets and has \(4\ell<\ell^2\) points. If it were also invariant under a different \(H'\), it would be invariant under \(H+H'=E[\ell]\), impossible for that nonempty proper subset.

## 2. The first two coefficients are not a free common prefix

Define
\[
c_H=\sum_{Q\in H\setminus\{O\}}x(Q),\qquad
t_H=\sum_{Q\bmod\pm1}(6x(Q)^2+2A).
\]
Write \(D_H=X^{\ell-1}-c_HX^{\ell-2}+d_2X^{\ell-3}+\cdots\). Then
\[
N_H=X^\ell-c_HX^{\ell-1}+(d_2+t_H)X^{\ell-2}+\cdots.
\]
The monic short-Weierstrass division polynomial has no \(X^{n-1}\) term; write its next coefficient as \(\phi_2\). The first two nonleading coefficients of \(U\) are
\[
u_1=-2c_H-s,\qquad
u_2=c_H^2+2d_2+2t_H+2c_Hs+t.
\]
Those of the retained locator \(C\) are
\[
C_1=2c_H+s,\qquad
C_2=\phi_2+3c_H^2-2d_2-2t_H+2c_Hs+s^2-t.
\]
All are direct polynomial-division identities.

Fixing the first nonleading coefficient of either \(U\) or \(C\) fixes \(s\) for each \(H\). Among the \(h\) distinct admissible values of \(\xi\), there are at most \(\lfloor h/2\rfloor\) unordered distinct pairs with a specified sum. Therefore a bank with a common first monic head has size at most
\[
(\ell+1)\lfloor(\ell-1)/4\rfloor=O(\ell^2)=O(n).
\]
Fixing both heads fixes \(s,t\), hence at most one unordered pair for each \(H\), for a total at most \(\ell+1\).

These bounds concern literal monic locators. A parameter-dependent monic cofactor of degree \(b\) has \(b\) free leading coefficients and can absorb the first \(b\) prefix comparisons triangularly. In particular the one- and two-head observations do not obstruct the general condition
\[
f+\lambda g-h_\lambda=C_{H,\xi,\zeta}W_{H,\xi,\zeta}.
\]
They also do not bound all line labels. The general cofactor/syndrome problem must be checked separately.

## 3. Small orders: exact symbolic identities and a finite replay

For \(\ell=3\),
\[
\Phi_3=X^4+2AX^2+4BX-A^2/3.
\]
If \(H=\{O,\pm Q\}\), \(x(Q)=q\), then \(K_H=X-q\), and its sole nonzero fiber has locator
\[
\Phi_3/(X-q)=X^3+qX^2+(q^2+2A)X+(q^3+2Aq+4B).
\]
The Vélu image value is \(\xi=-3q\). There are no two distinct nonzero fibers modulo sign, so this order cannot test a pair-fiber compiler.

For \(\ell=5\),
\[
\Phi_5=X^{12}+\frac{62A}{5}X^{10}+76BX^9-21A^2X^8+\cdots.
\]
Writing \(K_H=X^2-SX+P\), there are exactly two nonzero fibers. Their pair product is necessarily
\[
U=\Phi_5/K_H
=X^{10}+SX^9+(S^2-P+62A/5)X^8
 +(S^3-2SP+(62A/5)S+76B)X^7+\cdots.
\]
Their image values satisfy
\[
\xi+\zeta=-5S,\qquad
\xi\zeta=3S^2+19P+22A/5.
\]
Thus the retained complement is just \(K_H\). Multiplication of \(U\) by that quadratic produces the full-domain locator \(\Phi_5\), which is the zero evaluation word. This is a small-order artifact, not evidence of a useful fixed-degree common-source identity.

The exact verifier verify_torsion_coset_prefix.py derives the displayed characteristic-zero coefficients from the division-polynomial recurrence. It also reuses the existing curve \(y^2=x^3+16\) over \(\mathbb F_{211}\), without a curve search, and checks all six cyclic order-five subgroups, all twelve full fiber locators, their products and both prefix formulas. The six retained head pairs are
\[
(106,206),(98,141),(55,83),(137,21),(19,107),(7,75).
\]
Receipt: verify_torsion_coset_prefix.json, status PASS. This is identity verification, not a census of received lines.

## 4. Prime-field realization and the target's placement

Prime-field torsion is not an alphabet obstruction by itself. Fix an elliptic curve over \(\mathbb Q\) and adjoin all coordinates of its \(\ell\)-torsion. At completely split good primes other than \(\ell\), all that torsion reduces to \(\mathbb F_p\)-rational torsion. The identity Frobenius class has positive density, so such primes can be chosen arbitrarily large. This standard implication is explicit in [MIT 18.783, Problem Set 6, Problem 2](https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/fdf7e9a104859c26063bd422eb301667_MIT18_783S21_PS6.pdf). It supplies no polynomial upper bound on \(p\) as \(\ell\) grows, and cannot manufacture a missing common-line identity.

For the proposed ledger \(k=n-4\ell+1\), the unslacked canonical agreement \(n-2\ell\) lies above Johnson:
\[
(n-2\ell)^2-n(k-1)=4\ell^2>0.
\]
At a tested threshold \(T=n-2\ell-d\), the squared slack becomes
\[
T^2-n(k-1)=(4-d)\ell^2+4d\ell+d^2+d.
\]
Thus a fixed integer slack of four never suffices, while five gives strict below-Johnson placement for every prime \(\ell\ge23\). This arithmetic correction is separate from, and does not solve, the common received-line problem.

The support bank and all formulas are valid. Its raw cardinality does not yet provide a proximity-gap construction; the required common-source/cofactor identity remains the substantive missing step.
