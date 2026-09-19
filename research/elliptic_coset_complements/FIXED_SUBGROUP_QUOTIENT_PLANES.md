# Elliptic two-coset complements: exact compiler and distinct received planes

September 18, 2026. Pure algebra; no finite search or manuscript edit.

**Result.** A cyclic-isogeny quotient gives the intended low-degree witnesses for one subgroup. For two different order-\(\ell\) subgroups, however, the resulting two-dimensional received spaces have zero intersection modulo the Reed–Solomon code. Thus the common multiplication map does not combine these particular banks into one received line, even with independent pole choices, codeword shifts, and invertible changes of the two sources. This is a statement about the displayed compiler, not arbitrary witnesses on the same supports.

## Domain and exact division identity

Let \(\ell\ge11\) be an odd prime and let \(E/\mathbb F_p\), with \(p>3\) and \(p\ne\ell\), have all of \(E[\ell]\) rational. Put

\[
\mathcal D=x(E[\ell]\setminus\{O\}),\quad
n=(\ell^2-1)/2,\quad t=(\ell-1)/2,\quad r=t-2,
\quad k=n-4\ell+1.
\]

The code consists of evaluations of polynomials of degree at most \(n-4\ell\). For an order-\(\ell\) subgroup \(H\), let

\[
K_H(X)=\prod_{T\in(H\setminus\{O\})/\{\pm1\}}(X-x(T)),
\qquad B_H=K_H^2.
\]

The normalized Vélu quotient has reduced x-map

\[
Y_H(X)=\frac{N_H(X)}{B_H(X)},\qquad
\deg N_H=\ell,\quad\deg B_H=\ell-1,
\]

with both polynomials monic and coprime. These degree and denominator statements follow directly from the poles of the quotient map; the normalization is the one in [Moody–Rasmussen, Section 2.1](https://arxiv.org/html/1210.2743).

Let \(\mathcal A_H\) be the x-coordinates of the nonzero points of \(\varphi_H(E[\ell])\). It has \(t\) members. For \(a\in\mathcal A_H\), put

\[
L_{H,a}=N_H-aB_H.
\]

This monic degree-\(\ell\) polynomial has precisely the \(\ell\) distinct x-coordinates of a nonkernel coset pair \((P+H)\cup(-P+H)\) as roots. Consequently, for the monic domain locator \(\Phi=\prod_{x\in\mathcal D}(X-x)\),

\[
\boxed{\quad\Phi=K_H\prod_{a\in\mathcal A_H}L_{H,a}.\quad}
\]

This is the exact divisor factorization supplied by \([\ell]=\widehat\varphi_H\circ\varphi_H\). It partitions the domain into one kernel set of size \(t\) and \(t\) full fibers of size \(\ell\). It does not itself identify received functions for different \(H\).

## The fixed-subgroup compiler

Choose any \(b_H\in\mathbb F_p\setminus\mathcal A_H\). This exclusion is from the images of **all** nonkernel torsion coordinates, not merely the fibers used by one witness. Therefore

\[
L_H=N_H-b_HB_H
\]

is nonzero at every point of \(\mathcal D\), including the kernel coordinates. Set \(C_H=K_HB_H^{r-2}\). Off the kernel set, define received words

\[
f_H=C_H\frac{Y_H^r}{Y_H-b_H}
    =\frac{N_H^r}{K_HL_H},
\qquad
g_H=-\frac{C_H}{Y_H-b_H}
    =-\frac{B_H^r}{K_HL_H}.
\]

At every kernel coordinate define **both word values to be zero**. The displayed rational formula for \(f_H\) has a pole there; the word is a specified extension by zero, not that rational function evaluated at its pole.

For any \(r\)-element subset \(S\subset\mathcal A_H\), let

\[
V_S(Z)=\prod_{a\in S}(Z-a),\qquad
c_S=b_H^r-V_S(b_H),\qquad
p_S(Z)=\frac{Z^r-V_S(Z)-c_S}{Z-b_H}.
\]

The numerator vanishes at \(b_H\), and cancellation of its leading term gives \(\deg p_S\le r-2\). Hence

\[
h_S(X)=C_H(X)p_S(Y_H(X))
\]

is a polynomial of degree at most

\[
t+(r-2)\ell=n-4\ell=k-1.
\]

Off the kernel, its residual is

\[
f_H+c_Sg_H-h_S
=\frac{\prod_{a\in S}L_{H,a}}{K_HL_H}.
\]

Every witness and both words are zero on the kernel set. Thus its exact canonical agreement is

\[
r\ell+t=n-2\ell.
\]

There are \(\binom t2=\Theta(\ell^2)=\Theta(n)\) indexed witnesses for this subgroup. Distinct labels are a separate condition: writing the omitted pair as \(\{a,a'\}\), equality of labels for two distinct pairs is equivalent to equality of \((b_H-a)(b_H-a')\). Each distinct pair of pairs forbids at most one additional value of \(b_H\). Thus sufficiently large prime fields allow a pole choice with all these labels distinct. No prime-size estimate beyond this finite exclusion is asserted.

The value \(n-2\ell\) lies above Johnson for this code. It may be tested at the weaker threshold \(n-2\ell-5\), whose eventual first-order/Johnson placement is checked separately in [PARAMETER_WINDOW.md](PARAMETER_WINDOW.md). This compiler alone also does not establish the required \(\Theta(\ell)\) source/common-agreement separation.

## The received planes for distinct subgroups are disjoint modulo the code

**Proposition.** For \(H\ne H'\), if scalars \(\alpha,\beta,\alpha',\beta'\) and a polynomial \(P\) of degree at most \(n-4\ell\) satisfy

\[
\alpha f_H+\beta g_H-\alpha'f_{H'}-\beta'g_{H'}=P
\quad\text{on }\mathcal D,
\]

then all four scalars and \(P\) are zero.

The two kernel coordinate sets are disjoint, since \(H\cap H'=\{O\}\). Off their union there are

\[
n-2t=n-\ell+1
\]

coordinates. On those coordinates substitute the rational formulas and multiply by
\(K_HL_HK_{H'}L_{H'}\). The cross-numerator terms have degree at most

\[
r\ell+(t+\ell)=n-\ell,
\]

and the polynomial term has degree at most

\[
(n-4\ell)+2(t+\ell)=n-\ell-1.
\]

There are more roots than this degree bound, so the equality is an identity of rational functions on the affine x-line.

At a root of \(K_H\), both \(N_H\) and \(L_H\) are nonzero, whereas \(B_H\) vanishes. The term \(\alpha N_H^r/(K_HL_H)\) therefore has a genuine simple pole if \(\alpha\ne0\). The \(H'\) expression is regular there: \(K_{H'}\) is nonzero, and \(L_{H'}\) is nonzero at every torsion coordinate by the explicit pole exclusion above. It follows that \(\alpha=0\). Interchanging the subgroups gives \(\alpha'=0\).

The reduced denominator of \(g_H=-K_H^{2r-1}/L_H\) is exactly \(L_H\), because \(\gcd(K_H,L_H)=1\). Hence any nonzero equality
\(\beta g_H-\beta'g_{H'}=P\) requires both scalars nonzero and the complete pole divisors of \(L_H\) and \(L_{H'}\) to coincide, with multiplicities. Since both are monic of degree \(\ell\), this requires \(L_H=L_{H'}\).

Pull the resulting common zero divisor back to \(E\) by x. It has degree \(2\ell\). The zeros of \(L_H(x)\) are the fiber divisor of \(x\circ\varphi_H\) at \(b_H\), so this divisor, including multiplicities, is invariant under translations by \(H\). The same statement for \(H'\) makes it invariant under \(H+H'=E[\ell]\). Translation by this group acts freely on geometric points of \(E\); each orbit has \(\ell^2\) elements. A nonempty effective invariant divisor therefore has degree at least \(\ell^2\), contradicting \(2\ell<\ell^2\). Thus \(\beta=\beta'=0\), and then \(P=0\).

The same argument with one side zero proves that each fixed-subgroup received space has dimension two in the quotient by the code. Consequently these quotient planes cannot be identified by source reparametrization or addition of codewords.

## What remains open

The \(\Theta(\ell^3)\) distinct two-coset supports are real. This proof prevents their union from being compiled by the fixed-subgroup pullback above. It does **not** rule out a different common syndrome line meeting the error spaces of those supports, parameter-dependent error cofactors, or partial-fiber witnesses. Those alternatives require a new identity; neither the global division polynomial nor the common multiplication map supplies one automatically. No elliptic fixture or computational rental is needed to settle the displayed compiler.
