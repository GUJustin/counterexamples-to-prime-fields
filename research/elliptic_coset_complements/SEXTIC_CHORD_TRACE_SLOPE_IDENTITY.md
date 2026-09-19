# Sextic chord products: exact two-coefficient trace and slope identities

2026-09-19. Algebraic identities only; no new field scan or common
Reed–Solomon pencil is claimed.

Let \(E:y^2=f(x)=x^3+Ax+B\), in characteristic greater than five.
Let \(\phi:E\to E_H\) be the normalized Vélu isogeny of odd degree
\(\ell\), with
\[
 E_H:Z^2=Y^3+A_HY+B_H,\qquad
 c_H=\sum_{T\in H\setminus O}x(T),\qquad
 K_H(X)=\prod_{T\in(H\setminus O)/\{\pm1\}}(X-x(T)).
\]
Use the invariant derivation \(D x=2y,\ D y=3x^2+A\).
Normalization means \(\phi\) preserves the invariant differential.

## 1. A genuine additive two-coefficient identity

For two nonvertical line functions put
\[
 u=(y-m_1x-c_1)(y-m_2x-c_2).
\]
When their two balanced torsion triples have six distinct x-coordinates,
their norm under \(y\mapsto-y\) is the genuine split sextic
\[
 J=[f-(m_1X+c_1)^2][f-(m_2X+c_2)^2].
\]
This branch need not be a quintic multiplied by a fixed root.

The established trace identities are
\[
\begin{aligned}
 \operatorname{Tr}x&=Y+c_H,&\operatorname{Tr}y&=Z,\\
 \operatorname{Tr}x^2&=Y^2+(A_H-\ell A)/3,&
 \operatorname{Tr}(xy)&=YZ.
\end{aligned}
\]
Differentiate the last identity and use
\(D(xy)=5x^3+3Ax+2B\). It gives the exact new formula
\[
 \operatorname{Tr}x^3
 =Y^3+\frac{3(A_H-A)}5Y
       +\frac{2B_H-2\ell B-3Ac_H}{5}.                    \tag{1}
\]
Expanding the two line factors and substituting these traces yields
\[
 \boxed{\operatorname{Tr}u
 =(Z-m_1Y-c_1)(Z-m_2Y-c_2)
       -\frac25(A_H-A)Y+C_H,}                            \tag{2}
\]
where
\[
 \boxed{C_H=
 \frac{A_H-\ell A}{3}m_1m_2
 +c_H(m_1c_2+m_2c_1)
 +(\ell-1)c_1c_2
 +\frac{-3B_H+3\ell B+2Ac_H}{5}.}                        \tag{3}
\]
Thus the additive correction is in \(\operatorname{span}\{Y,1\}\).
This is an exact identity; the coefficient of \(Y\) is independent of
the chosen lines.

The product on the right uses the SAME slopes and intercepts as the
original lines. It is not automatically the product of the two chords
through their isogeny images. In particular (2) does not assert that
the trace has the image torsion divisor.

## 2. The exact additional condition for the norm

Assume the original line triples avoid \(H\), so their isogeny norms
retain pole order three. Write the normalized image chords as
\[
 g'_i=Z-m'_iY-c'_i,\qquad
 \operatorname{Norm}_\phi(y-m_ix-c_i)=\kappa_i g'_i,
 \quad \kappa_i\ne0.
\]
Norm multiplicativity gives \(\operatorname{Norm}u/(\kappa_1\kappa_2)
=g'_1g'_2\). Direct coefficient comparison with (2) shows
\[
 \frac{\operatorname{Norm}u}{\kappa_1\kappa_2}
       -\operatorname{Tr}u\in\operatorname{span}\{Y,1\}
\]
if and only if
\[
 m'_1+m'_2=m_1+m_2,\qquad
 m'_1m'_2=m_1m_2,\qquad
 c'_1+c'_2=c_1+c_2.                                    \tag{4}
\]
Equivalently the unordered pair of image slopes must equal the original
unordered pair, and the intercept sum must be preserved.
Allowing the slopes to swap is already included in (4); it is not an
extra cancellation beyond these equations.

These are additional algebraic conditions on the actual torsion chords.
Neither the norm identity nor the linear trace alone implies them.
Even if (4) is achieved, a common high-degree received pencil and its
far-source bounds still require a separate compiler identity.

## 3. A rational slope correction, without analytic zeta functions

Define the explicit odd rational function
\[
 \mathcal R_H(P)=2y(P)\frac{K'_H(x(P))}{K_H(x(P))}.
\]
Let \(P_1,P_2,P_3\) be a nonvertical chord triple, with
\(P_1+P_2+P_3=O\), none in \(H\), and let its slope be \(m\).
Suppose its normalized image chord has slope \(m_H\).
Then
\[
 \boxed{m_H=\ell m-\sum_{i=1}^3\mathcal R_H(P_i).}        \tag{5}
\]
This also specifies the exact slope-preservation condition:
\(\sum_i\mathcal R_H(P_i)=(\ell-1)m\).

For a purely algebraic proof, put \(g=y-mx-c\), whose zero divisor is
the chord triple. With local parameter \(t=-x/y\) at infinity,
\[
 g=-t^{-3}(1+mt+O(t^2)).
\]
Normalized Vélu has \(Y=x+O(x^{-1})\) and \(Z=y+O(t)\), so its target
local parameter equals \(t+O(t^3)\), with no quadratic term.
Expand \(\prod_{T\in H}g(S+T)\) to first order at \(S=O\).
After dividing by its leading constant this gives
\[
 m_H=m+\sum_{T\in H\setminus O}\frac{Dg(T)}{g(T)}.        \tag{6}
\]
All denominators are nonzero by the kernel-avoidance assumption.

Write \(l(X)=mX+c\), \(F_l=f-l^2=\prod_i(X-x(P_i))\).
At a kernel pair \(T,-T\) with x-coordinate \(a\), direct algebra gives
\[
 \frac{Dg(T)}{g(T)}+\frac{Dg(-T)}{g(-T)}
 =2l(a)\frac{F'_l(a)}{F_l(a)}-4m.
\]
Using \(F'_l/F_l=\sum_i1/(X-x(P_i))\) and
\[
 \frac{l(a)}{a-x(P_i)}
 =m+\frac{y(P_i)}{a-x(P_i)}
\]
and then summing over the \((\ell-1)/2\) kernel x-coordinates proves
(5). Tangencies can be handled with root multiplicities; the sextic
split-support application uses distinct roots.

## 4. Scope and remaining constructive requirement

The extra sixth root permits two independent balanced chord triples.
Equations (2)--(5) give actual additive identities and exact conditions
on how their slopes change under each isogeny. They do not identify
trace with norm, preserve the image divisor for free, or put many
subgroup-dependent residuals on a shared received line.

The two-parameter signed quintic
\[
 P,\ 6Q,\ -4P,\ 2Q,\ 3P-8Q
\]
has Miller partial sums \(P+6Q,-3P+6Q,-3P+8Q\).
The first two give independent quotient tags: their coefficient matrix
has determinant 24. After excluding the finite linear collision
conditions modulo \(\ell\), it supplies many different base fiber pairs.
Its multiplicative norm label on the entire family is already excluded
in the saved \(\ell=23\) fixture, because its diagonal \(P=Q\) contains
the previously certified inconsistent labelled bank. No such label
test was repeated. Its off-diagonal subfamilies and the sextic
conditions (4) are not settled here.

No additional elliptic computation was launched after saving these
identities.
