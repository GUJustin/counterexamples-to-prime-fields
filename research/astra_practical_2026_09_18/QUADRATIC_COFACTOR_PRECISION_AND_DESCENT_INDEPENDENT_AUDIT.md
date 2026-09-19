# Independent audit: quadratic-cofactor precision, descent, and factor allocation

Date: 2026-09-18. Status: **PASS for the corrected statements and scope below.**

Audited sources:

* `QUADRATIC_COFACTOR_IDENTITY_COMMON_FACTOR_REDUCTION.md`;
* `QUADRATIC_COFACTOR_UNIT_KERNEL_PRECISION_UPGRADE.md`.

This receipt concerns necessary structure of normalized truncated pencils. It proves no cardinality bound for a finite root-subset fiber and no improvement to the practical factor-four deficit.

## 1. Truncated rational interpolation and Frobenius descent

The abstract all-minors argument is valid modulo \(Z^{13}\). A degree-at-most-two kernel relation between two unit series has numerator and denominator with the same \(Z\)-valuation, at most two. Removing that power loses at most two coefficients. Every later canceled factor is a unit, so there is no further loss of precision.

The interpolation steps are exact for the stated reason: rational functions of types \((d_1,e_1)\) and \((d_2,e_2)\), with unit denominators, agreeing modulo \(Z^N\), are equal if \(N>\max(d_1+e_2,d_2+e_1)\). Here the largest comparison degree is eight. Minimal fixed-denominator reduction is legitimate: a factor canceling for generic pencil parameter divides both coefficient numerators. Independence of \(U,V\) similarly makes the generic gcd of the two pencils a fixed common factor of their coefficient polynomials. Consequently the claimed common unit series times degree-two pencils follows.

The consequence about \(b/a\) requires \(a(0)\ne0\). This is now explicit and holds in the practical normalization \(a(0)=1,b(0)=0\). Generic invertibility of \(a+Ub\) alone would not suffice for that particular consequence.

For a genuine normalized direction \(b\ne0\), the reduced approximation \(b/a=B/A\) descends to \(E=\mathbb F_{p^6}\): the Padé equations are linear over \(E\), with \(A(0)=1\), and uniqueness follows from the degree-four cross-product bound. Put \(t=\max(\deg A,\deg B)\in\{1,2\}\) and \(H=a/A\). The primitive independent pencils cannot generically cancel fixed factors of \(H/H^\sigma\), nor each other. Hence its reduced numerator and denominator have degrees at most \(2-t\).

If \(t=2\), normalization forces \(H/H^\sigma=1\), so \(H\) is a base-field prefix. If \(t=1\), this ratio has type \((1,1)\). Its sixfold Frobenius norm equals one modulo the available precision, and both norm polynomials have degree at most six; the norm equality is therefore exact. A nonconstant ratio is

\[
\frac{1-uZ}{1-vZ},\qquad v=u^{p^j},
\]

and a partial Frobenius-orbit product removes it. A proper orbit segment can be chosen with length \(j<d\le6\), where \(d\) is the orbit length. The remaining series is over \(\mathbb F_p\). No extension of Frobenius to the auxiliary infinite scalar field is being assumed: the rational certificates descend first.

## 2. Large banks give the unit relation at full precision

Normalize \(P=1+x_1Z+x_2Z^2\), \(Q=1+y_1Z+y_2Z^2\). The equation

\[
(a+Ub)P=(a^\sigma+Vb^\sigma)Q\pmod {Z^{15}}
\]

is a fourteen-equation, four-unknown augmented linear system. If its generic coefficient rank is \(r\le4\) and it is generically inconsistent, some nonzero augmented \((r+1)\)-minor includes the right-hand-side column. At every actual valid \((\tau,\tau^p)\), consistency makes that minor zero, even when the coefficient rank drops. All coefficient \((r+1)\)-minors vanish identically, so specialization cannot increase that rank.

There are only two \(U\)-columns and two \(V\)-columns. Expanding the final column gives monomial support

\[
\{i\le3,j\le2\}\ \cup\ \{i\le2,j\le3\}.
\]

For \(p>3\), the exponents \(i+pj\) are distinct. Thus the nonzero minor remains nonzero after \(V=U^p\), with degree at most \(3p+2\). More than \(3p+2\) valid distinct labels force generic consistency with unit \(P,Q\).

Starting the previous proof with this unit relation removes the initial valuation loss. The complete normalized classification consequently holds modulo \(Z^{15}\). This structural implication discards no labels; later factor-allocation conclusions have their own explicit exceptional sets.

For \(p=2130706433\), \(3p+2=6392119301\), below the target \(274980728111395088\).

## 3. Allocation to the genuine quadratic cofactor

Suppose \(W_\tau=V_\tau q_\tau\pmod {Z^{15}}\), with \(V_\tau\) a base-field unit prefix and \(q_\tau(0)=1\), \(\deg q_\tau\le2\).

**Primitive quadratic branch.** Write \(W_\tau=H P_\tau\), \(P_\tau=A+\tau B\), with \(H\) over the base field. The quotient \(P_\tau/q_\tau\) is exactly in \(\mathbb F_p(Z)\): its Frobenius cross-difference has degree at most four and vanishes modulo \(Z^{15}\). Exclude at most \(p\) parameters with an \(\mathbb F_p\)-root, at most \(p\) for which the normalized polynomial is entirely over \(\mathbb F_p\), and at most one degree drop. Outside these \(2p+1\) parameters, \(P_\tau\) has degree two and no nonconstant base-field polynomial divisor. In reduced base-field form \(P_\tau/q_\tau=R/S\), coprimality gives \(R\mid P_\tau\), so \(R\) is constant. Degree and normalization then give \(q_\tau=P_\tau\) and \(V_\tau=H\pmod {Z^{15}}\).

**Primitive linear branch.** Write \(W_\tau=H_{\rm base}F P_\tau\), with \(F\) a proper segment of one Frobenius orbit, of length \(j<d\le6\). The quotient \(FP_\tau/q_\tau\) is exactly base-field rational: its cross-difference has degree at most \(j+3\le8\). Excluding at most \(p+1+d\le p+7\) parameters removes base-field \(P_\tau\), degree drops, and intersections of its root with that orbit. For a remaining parameter, if \(P_\tau\nmid q_\tau\), its non-base root survives in the reduced numerator, whose Frobenius orbit cannot be completed by \(F\). Hence \(q_\tau=P_\tau q_0\), with \(\deg q_0\le1\), and \(F/q_0\in\mathbb F_p(Z)\).

A proper orbit segment \(F\) has no nonconstant base-field divisor. Therefore \(j\ge2\) is impossible outside the exceptional set; \(j=1\) forces \(q_0=F\) and fixes \(V_\tau\); \(j=0\) gives a base-field linear \(q_0\) and fixes only \(V_\tau q_0=H_{\rm base}\pmod {Z^{15}}\). These conclusions do not assume a numerical dimension-to-count principle.

## 4. Constant-prefix branch: exact additional classification

This branch must remain separate: \(b=0\pmod {Z^{15}}\) does not imply that \(V_\tau\) is fixed. The following stronger description is valid, with **no exceptional labels**.

Choose one valid factorization

\[
a=V_*q_*\pmod {Z^{15}}.
\]

Let \(B_*\in\mathbb F_p[Z]\) be the maximal normalized base-field polynomial divisor of \(q_*\), and put \(q_*=F_*B_*\). Maximality is unambiguous: normalized base-field divisors of a fixed polynomial are closed under least common multiple. All factors have constant coefficient one.

For any other valid \(a=V_\tau q_\tau\), the unit quotient \(q_*/q_\tau\) agrees modulo \(Z^{15}\) with the base-field series \(V_\tau/V_*\). Its Frobenius cross-difference has degree at most four, so

\[
q_*/q_\tau=R/S\in\mathbb F_p(Z)
\]

exactly. Choose coprime \(R,S\in\mathbb F_p[Z]\) with \(R(0)=S(0)=1\). The identity \(q_*S=q_\tau R\) gives \(R\mid q_*\), hence \(R\mid B_*\). Thus

\[
q_\tau=F_*B_\tau,\qquad
B_\tau=(B_*/R)S\in\mathbb F_p[Z],\qquad
\deg B_\tau\le2-\deg F_*.
\]

Canceling the unit \(F_*\) in the truncated factorization yields

\[
V_\tau B_\tau=V_*B_*\pmod {Z^{15}}.
\]

Accordingly this branch has a fixed base-field prefix after multiplication by a varying base-field cofactor of degree at most two. If \(\deg F_*\) is two, one, or zero, that remaining degree is respectively zero, one, or two. A fixed base-field product prefix can indeed permit varying base-field quadratic cofactors, so it cannot be absorbed into the nonconstant-pencil conclusion using only linear cofactors.

## 5. Precision and practical limits

Modulo \(Z^{15}\) retains coefficients zero through fourteen: the normalization and **fourteen nonconstant packet heads**. Modulo \(Z^{13}\) retains twelve nonconstant heads. The unit-kernel upgrade restores two coefficients; it does not determine the coefficient of \(Z^{15}\).

For the practical boundary \(\deg T=e+1031\), the applicable interface is therefore fourteen heads **plus a separate remainder condition**. The fifteenth-head gate does not follow from this proof. The constant-prefix branch and the base-field linear-cofactor branch likewise retain their own arithmetic obligations. Actual prescribed root subsets, root-free cofactors, denominator compatibility, and the required finite fiber cardinality remain unproved here.
