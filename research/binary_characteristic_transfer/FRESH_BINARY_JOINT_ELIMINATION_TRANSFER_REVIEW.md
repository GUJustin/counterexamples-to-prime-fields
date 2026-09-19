# Fresh binary-source review: one joint-elimination candidate

September 18, 2026. Read-only review of `/Users/jthaler/Documents/binary_field_counterexamples`. No file in that repository was edited, committed, or pushed.

**Outcome: no new constructive transfer is recommended.** The recent verified changes improve an existing padding error term and simplify existing population proofs. The one distinct recent identity examined below extends algebraically to odd characteristic, but its starting equation cannot hold nontrivially on the prescribed short domains. Its noncritical interpretation also degenerates over a prime alphabet. This is a decision about that identity, not an obstruction to other constructions.

## Exact source and status

The reviewed HEAD is `0d6549a5efe95773c7d988698da3b1af35516d43`. The most recent admitted improvement, in commits `b4b39f5` and `3169821`, replaces an existing high-rate padding error of order \(\sqrt{\log N/N}\) by \(O(N^{-1/2})\), with its seed, domain, field, rate, and label population retained. The actual proof is in `sections/balanced-padding.tex`; it is a characteristic-independent discrepancy improvement, not a new bank that fixes the prime-domain or rate problem.

The fresh candidate is in
`tmp/renewal-20260918/joint-quadratic-elimination-identity.md`.
This working note is **not Git tracked**, so its exact reviewed SHA-256 is
`26bd6474eea63791b2649f3d42ec2fed396560ecaa9979d246eddf44ba0f0e77`.
The tracked status/strategy at the stated HEAD, including commit `2746e49`, explicitly reports no common-source conversion or growing population from this candidate. The fixed-normalized-factor remainder pencil is already closed there. No claimed lower bound is imported from the working note.

For source pinning, `docs/research-strategy.md` has SHA-256
`8f620d0a0bc52bc39e430599c70b039aebf535f21f9e320ae7deaa76c1ae4f22`,
and `sections/balanced-padding.tex` has SHA-256
`1fea3095c2c378577fb84dfe97988fbe72caa400464bd8e76456d2c0bd11577c`.

## The binary identity and its exact odd-characteristic version

The source starts with Boolean polynomials satisfying

\[
u^2+u=L(gA)^2,\qquad v^2+v=L(gB)^2.
\]

For \(H=Bu+Av\), \(c=A^2+AB+B^2\), and \(d=AB(A+B)\), it derives

\[
H^4+cH^2+dH=L g^2d^2.
\]

At domain points where \(d\ne0\), the equation \(H=0\) detects the joint zero \(u=v=0\). The source correctly distinguishes this locator identity from a low-degree explanation on one shared received line.

The following extension was checked directly here. In characteristic \(p\), suppose

\[
u^p-u=L(gA)^p,\qquad v^p-v=L(gB)^p,
\]

and define

\[
H=Bu-Av,\qquad \Delta=AB^p-A^pB,\qquad
C=\frac{AB^{p^2}-A^{p^2}B}{\Delta},
\]

with \(\Delta\) not identically zero. The displayed quotient is a polynomial: the \(p+1\) distinct homogeneous linear factors of \(\Delta\) all divide its numerator. Direct cancellation gives

\[
H^p=B^pu-A^pv,\qquad
\Delta u=AH^p-A^pH,\qquad
\Delta v=BH^p-B^pH,
\]

and therefore

\[
\boxed{\quad H^{p^2}-CH^p+\Delta^{p-1}H
=L(g\Delta)^p.\quad}
\]

At every point where \(\Delta\ne0\), \(H=0\) is equivalent to \(u=v=0\). For \(p=2\), these formulas recover the source's quartic identity exactly. Thus the cancellation itself is Frobenius algebra, not an exclusively binary miracle. Its exponent becomes \(p^2\), and the critical determinant has homogeneous degree \(p+1\) in \(A,B\).

## Two exact failures at the requested endpoint

First, let \(L=L_D\) be the domain locator of degree \(n>0\). A nonconstant polynomial satisfying

\[
u^p-u=L_Da^p
\]

must obey

\[
p\deg u=n+p\deg a,
\]

so \(p\mid n\). The leading degree cannot cancel because \(p\deg u>\deg u\). If the right side is zero, \(u\) is only a constant in \(\mathbb F_p\). This argument allows coefficients in any extension field. Hence the starting identity supplies no nonconstant constraint on a domain of size \(0<n<p\), including the prescribed \(n=262144\) domains over the large benchmark primes. A replacement that changes this starting factorization would be a new construction, not a direct specialization.

Second, for a genuine prime-alphabet specialization \(A,B\in\mathbb F_p[X]\), every \(x\in\mathbb F_p\) satisfies

\[
\Delta(x)=A(x)B(x)^p-A(x)^pB(x)=0.
\]

Thus **every prime-field coordinate is critical**. The noncritical joint-zero implication contributes no points. The binary source avoids this because its coordinates and coefficient values live in a field of dimension greater than one over \(\mathbb F_2\); its two coefficients can be linearly independent over the two-element value field. Larger characteristic does not preserve that separation when the alphabet itself is \(\mathbb F_p\).

This second observation does not rule out a new treatment of all critical points or extension-valued coefficients. The first degree condition still rules out this starting identity on a short domain even with extension-valued coefficients.

## Decision

The recent joint-elimination calculation is distinct from the already reviewed single-locator and norm compilers, but it presently gives neither a populated binary received-line construction nor a viable short-domain odd-characteristic specialization. The characteristic-independent discrepancy refinement changes a lower-order padding error only. No new fixture, rental, or prime-paper addition is justified by this source review. A fresh lead would need a replacement for the displayed \(p\)-power factorization and an actual common-line compiler, not another normalization of its existing critical factors.
