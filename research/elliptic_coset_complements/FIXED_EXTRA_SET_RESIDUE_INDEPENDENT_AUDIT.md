# Fixed extra coordinates: residue space and dimension audit

September 18, 2026. **PASS.** Independent proof of the common-residue correction
and the generalized-space dimension bound in
[FIXED_EXTRA_SET_PATH_AUDIT.md](FIXED_EXTRA_SET_PATH_AUDIT.md).
No computation, manuscript edit, or generic intersection claim.
The final expanded Sections 5--6 of that note were also reread after the
residue correction: the statements, original-domain bound, multiplier
interpretation, and one-dimensional quotient-image caveat all pass.

Use
\[
\ell\ge23,\quad t=(\ell-1)/2,\quad n=(\ell^2-1)/2,\quad
k=n-4\ell+1,\quad T=n-2\ell-5.
\]
Fix \(Z\subset\mathcal D\), \(|Z|=d\le5\), with monic locator \(J=J_Z\);
write \(\mathcal D'=\mathcal D\setminus Z\). Its punctured code is
\(\operatorname{RS}_k(\mathcal D')\). A subgroup is clean here if its kernel
coordinates avoid \(Z\); some of its nonkernel tag fibers may still meet \(Z\).
Suppress \(H\) in
\[
B=K^2,\qquad Y=N/B,\qquad C=KB^{t-4}.
\]
Let \(V_{H,Z}\) be the syndrome image of the words
\[
\frac{C}{J}\sum_{j=0}^d X^j q_j(Y),\qquad \deg q_j<t,
\]
off the kernel, with value zero on the remaining kernel coordinates.

## The shared residue space is real

In the quotient by the punctured code, put
\[
\mathcal R_Z=
\left\{\left[\left.\frac{R}{J}\right|_{\mathcal D'}\right]:
                       \deg R<d\right\}.
\]
For \(d=0\), this is the zero space. For every clean \(H\),
\[
\boxed{\mathcal R_Z\subseteq V_{H,Z},\qquad \dim\mathcal R_Z=d.}
\]

Indeed, \(C\) is nonzero on \(Z\), since its only roots are kernel coordinates.
For any \(R\) of degree \(<d\), interpolate a polynomial \(P\), \(\deg P<d\),
such that \(C(z)P(z)=R(z)\) for every \(z\in Z\). Then
\[
Q=\frac{CP-R}{J}
\]
is a polynomial. The exact degree of \(C\) is
\[
\deg C=k-1-(t-4),
\]
so
\[
\deg Q\le\deg C-1=k-t+2<k.
\]
The numerator \(CP\) supplies an allowed generalized weighted word, using
constant tag polynomials. Its values on the kernel are zero. Since \(J\)
has no root there, the rational identity \(CP/J=R/J+Q\) holds at those
coordinates as well. Hence the claimed quotient inclusion respects the
specified zero extension; it is not merely an identity off the kernel.

If a nonzero \(R/J\) represented a codeword \(P_0\), the nonzero polynomial
\(R-JP_0\) would vanish on all \(n-d\) coordinates. Its degree is at most
\(k+d-1<n-d\), a contradiction. It cannot be identically zero because
\(\deg R<\deg J\). Thus the residue parameters are injective modulo code,
proving dimension \(d\).

## Every nonzero residue is far

For nonzero \(R\) with \(\deg R<d\), and every \(\deg P_0<k\),
\[
\frac R J=P_0\quad\Longleftrightarrow\quad R-JP_0=0
\]
on \(\mathcal D'\). The right side is a nonzero polynomial of degree at most
\(k+d-1\). Therefore
\[
\operatorname{agr}_{\mathcal D'}(R/J,\operatorname{RS}_k)
\le k+d-1.
\]
This also applies after adding a codeword or multiplying by a nonzero scalar.
Assigning **arbitrary** word values on the deleted coordinates adds at most
\(d\) possible matches. Every such original-domain extension therefore has
\[
\boxed{\quad\operatorname{agr}_{\mathcal D}\le k+2d-1<T,\quad}
\]
because
\[
T-(k+2d-1)=2\ell-2d-5>0.
\]
Consequently the punctured bound is also below its target \(T-d\).
The common \(d\)-space can contain many two-planes when \(d\ge2\), but every
nonzero point of those planes is far. Such a shared plane supplies no
qualifying labels. More strongly, on the punctured domain it has no nonzero
point represented by errors on two full fibers:
\[
(n-d-2\ell)-(k+d-1)=2\ell-2d>0.
\]

## The generalized dimension bound passes

The displayed word space has at most \((d+1)t\) parameters. Restricting each
\(q_j\) to degree at most \(t-4\) gives
\[
F=C\sum_{j=0}^d X^j q_j(Y),\qquad \deg F\le k-1+d.
\]
Its \((d+1)(t-3)\) parameters are independent. To see this, a rational
relation becomes \(\sum_{i=0}^m p_i(X)Y^i=0\), with \(\deg p_i\le d<t\).
After multiplication by \(B^m\), evaluation at the \(t\) distinct roots of
\(K\), where \(N\ne0\), forces \(p_m=0\); induction removes all coefficients.

Divisibility \(J\mid F\) imposes at most \(d\) linear conditions. Hence at
least \((d+1)(t-3)-d\) independent parameters give degree-\(<k\) polynomial
words \(F/J\). They agree with the prescribed kernel values, because every
such \(F\) has the factor \(K\) and \(J\) has no kernel root. Polynomial
evaluation is injective on \(\mathcal D'\), so these really are independent
codeword directions. Consequently
\[
\dim V_{H,Z}\le(d+1)t-\bigl((d+1)(t-3)-d\bigr)=4d+3.
\]
Together with the proved common subspace,
\[
\boxed{\quad\dim(V_{H,Z}/\mathcal R_Z)\le3d+3\le18.\quad}
\]
No exact generic dimension or pairwise-intersection dimension follows.

## Quotienting changes the code parameters

Multiplication by the nowhere-zero word \(J|_{\mathcal D'}\) maps
\[
\operatorname{RS}_k(\mathcal D')+
 \{R/J:\deg R<d\}
\]
onto \(\operatorname{RS}_{k+d}(\mathcal D')\). This is exactly Euclidean
division \(F=JP+R\), with \(\deg P<k\), \(\deg R<d\).
The new length is \(n-d\), dimension \(k+d\), and minimum distance
\[
(n-d)-(k+d)+1=4\ell-2d.
\]
Thus removing the universal residue space does not restore the distance
\(4\ell\) used in the strict two-fiber theorem. A new argument is still
required to bound usable common directions or construct qualifying labels.
The fixed-set reduction and this audit do not address extra sets varying
with the witness.
