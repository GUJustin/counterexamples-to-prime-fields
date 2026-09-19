# Exact fixed-extra quotient basis and intersection system

September 18, 2026. Fixed extra set only. This gives an exact linear test, not a construction or a generic-rank assumption.

Use the notation and hypotheses of [FIXED_EXTRA_SET_PATH_AUDIT.md](FIXED_EXTRA_SET_PATH_AUDIT.md): \(\ell\ge23\), \(0\le d=|Z|\le5\), \(t=(\ell-1)/2\), \(n=(\ell^2-1)/2\), \(k=n-4\ell+1\), and \(J=J_Z\). Only subgroups whose kernel is disjoint from \(Z\) are considered. Write \(K_H\) for the kernel locator, \(B_H=K_H^2\), \(Y_H=N_H/B_H\), and \(C_H=K_HB_H^{t-4}\).

## 1. Exact basis after removing the common residue space

Multiplication by \(J\) identifies the quotient \(V_{H,Z}/\mathcal R_Z\) with a word space modulo \(\operatorname{RS}_{k+d}\) on \(\mathcal D\setminus Z\). Terms with tag degree at most \(t-4\) become code polynomials. Therefore the quotient is spanned by

\[
X^j e_{i,H},\qquad 0\le j\le d,\quad 0\le i\le2,
\]

where the words are zero on the kernel and, elsewhere,

\[
e_{i,H}=C_HY_H^{t-3+i}
=\frac{N_H^{t-3+i}}{K_H^{2i+1}}.
\tag{1}
\]

These \(3d+3\) classes are independent. To see this, write a possible codeword relation as

\[
\sum_{i=0}^{2}p_i(X)e_{i,H}=P(X),
\qquad\deg p_i\le d,\quad\deg P\le k+d-1.
\]

After clearing \(K_H^5\), its numerator has degree at most \((t-1)\ell+d\), while it vanishes on \(n-t-d\) nonkernel retained coordinates. The latter count exceeds that degree by \(\ell-2d>0\), so the rational identity holds. At the roots of \(K_H\), the highest-pole term forces \(p_2\) to vanish. Since \(\deg p_2\le d<t\), it is zero. Cancelling the resulting two powers of \(K_H\) and repeating gives \(p_1=p_0=0\), then \(P=0\).

Thus

\[
\boxed{\dim(V_{H,Z}/\mathcal R_Z)=3d+3,
\qquad\dim V_{H,Z}=4d+3.}
\]

The proof uses both \(\ell>2d\) and \(d<t\); both hold in the stated parameter range.

## 2. An exact pairwise polynomial identity

Fix distinct clean subgroups \(H,H'\), and abbreviate their kernel locators to \(K,K'\). Let \(p_0,p_1,p_2\) and \(p'_0,p'_1,p'_2\) have degree at most \(d\). Their common-denominator numerators are

\[
A=N_H^{t-3}(p_0K^4+p_1N_HK^2+p_2N_H^2),
\]

with the analogous definition of \(A'\). The two quotient classes agree precisely when there exists \(P\), \(\deg P\le k+d-1\), whose word values equal their difference. Off the two kernels this says

\[
AK'^5-A'K^5-PK^5K'^5=FQ,
\qquad F=\frac{\Phi}{JKK'},
\tag{2}
\]

for a polynomial \(Q\) satisfying

\[
\deg Q\le q_*:=2\ell+2d-3.
\]

Indeed the left side has degree at most \(n+\ell-2+d\), and it vanishes at all \(n-\ell+1-d\) retained nonkernel coordinates. Conversely (2) gives the desired agreement on those coordinates.

The actual kernel values are zero extensions, so pole cancellation alone is insufficient. Their exact conditions are

\[
\boxed{
FQ\equiv AK'^5\pmod{K^6},\qquad
FQ\equiv-A'K^5\pmod{K'^6}.}
\tag{3}
\]

For example, at the first kernel, the difference between \(P\) and the required value \(-A'/K'^5\) is
\((AK'^5-FQ)/(K^5K'^5)\). Its value is zero exactly when its numerator has the sixth factor of \(K\). The kernel locators are squarefree, and \(F\) is invertible modulo both powers.

Conditions (3) imply divisibility of \(AK'^5-A'K^5-FQ\) by \(K^5K'^5\), giving a unique polynomial \(P\). Its degree is at most \(k+d-1\) exactly when the coefficients at the three degrees

\[
n+\ell-2+d,\quad n+\ell-3+d,\quad n+\ell-4+d
\tag{4}
\]

vanish in that numerator. Thus (3), the bound on \(Q\), and (4) are necessary and sufficient, including all retained kernel values.

## 3. Reduce the equations using the isogeny factorization

The CRT modulus in (3) is \(K^6K'^6\), of degree \(12t=6\ell-6\). For any choice of the \(6(d+1)\) coefficients of the two triples, there is a unique CRT representative \(Q_0\) of degree below this modulus. Impose

\[
[X^j]Q_0=0\quad(q_*<j<6\ell-6)
\]

and the three infinity equations (4). This is an exact homogeneous linear system with

\[
\boxed{\;6(d+1)\text{ unknowns and }4\ell-2d-1
\text{ displayed equations}.\;}
\]

The equations may be dependent; their actual nullity, not a dimension heuristic, is the pairwise intersection dimension. Independence from Section 1 ensures that no nonzero solution merely represents zero on one side.

Full degree-\(n\) expansions are unnecessary for the local congruences. Let
\(\sigma_1=\sum_{a\in\mathcal A_H}a\) and
\(\sigma_2=\sum_{a<a'}aa'\). Since \(B_H=K^2\), the exact factorization of \(\Phi\) gives

\[
\frac{\Phi}{K}
\equiv N_H^t-\sigma_1N_H^{t-1}K^2
+\sigma_2N_H^{t-2}K^4\pmod{K^6}.
\]

Put \(u=K^2/N_H\) in this local ring, so \(u^3=0\). The first CRT condition is equivalently

\[
\boxed{
Q\equiv\frac{JK'^6}{N_H}
\left[p_2+(p_1+\sigma_1p_2)u
+(p_0+\sigma_1p_1+(\sigma_1^2-\sigma_2)p_2)u^2\right]
\pmod{K^6}.}
\tag{5}
\]

The other condition is the same formula with the subgroups exchanged and an overall minus sign. Every inverse here is of a unit. This is the precise contribution of the common division identity: only the first two elementary symmetric tag sums enter each local condition. It does not assert that a nonzero low-degree CRT representative exists.

## 4. One bounded fixture and its scope

For \(\ell=23\), \(d=5\), the system has 36 unknowns, a degree-132 CRT modulus, cofactor cap 53, 78 cofactor cutoff equations, and three infinity equations: an \(81\times36\) matrix. This is small enough for an exact one-pair replay against the independent direct-syndrome construction; no curve or extra-set scan is required.

The fixture and replay are recorded in `ell23_fixture/verify_fixed_extra_crt.py` and `ell23_fixture/fixed_extra_crt_pair_1_2.json`. They use the saved curve over \(\mathbb F_{1657}\), subgroup indices 1 and 2, and the fixed set \(Z=\{7,231,340,411,470\}\). The verifier constructs the CRT conditions independently from polynomial arithmetic and also checks the local simplification (5).

**Finite replay: PASS.** The independent integer-arithmetic CRT matrix has rank 36 and nullity zero. All 36 basis-column comparisons with the local formula (5) pass, and both domain factorizations are rechecked. This agrees with the separate direct-syndrome replay for the same pair. Only this one pair was tested by the CRT implementation.

A zero intersection at this fixture excludes only this subgroup pair with this fixed extra set. A nonzero intersection would still require a common nonresidue direction or plane across growingly many subgroups, actual sparse-error representations, distinct labels, and source-distance bounds. The system is an exact manageable target; no growing construction or generic-intersection theorem follows from the parameter count.
