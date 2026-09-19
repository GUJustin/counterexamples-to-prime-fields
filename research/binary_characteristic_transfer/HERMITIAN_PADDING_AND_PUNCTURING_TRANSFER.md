# Fixed-rate padding and support-preserving puncturing of the Hermitian bank

2026-09-19. This uses the published
[Hermitian theorem](odd_hermitian_high_rate.tex).
There is a positive fixed-rate padding over the same degree-eight
alphabet already used by that theorem. It retains the full superlinear
bank and exact individual/common source agreements, but not the proved
singleton classification. Its fractional capacity margin still tends
to zero, and its threshold stays below first order.

A separate incidence argument bounds arbitrary puncturing with smaller
code dimension, even when the retained witnesses are replaced. At fixed
rate it allows only constantly many labels whose error supports remain
inside their original Hermitian circles. This is different from the
previous common-agreement shortening argument.

## 1. A positive fixed-rate padding

Let \(p\ge5\), put \(B=\mathbb F_{p^2}\subset E=\mathbb F_{p^4}\),
choose \(\beta\in E\setminus B\), and write
\[
 k=p^2-2p,\qquad D=p^2-p,\qquad
 \Lambda=X^{p^2}-X,\qquad R=X^D.
\]
For \(s\in B\), \(c\in\mathbb F_p\), and \(c-s^{p+1}\ne0\), define
\[
 G=X^{p+1}+sX^p+s^pX+c,\qquad
 P_G=(X+s)\Lambda/G,\qquad \lambda_G=P_G(\beta).
\]
The established identities give
\[
 P_G=R+C_G,\quad \deg C_G\le k,\qquad
 q_G=\frac{R-P_G+P_G(\beta)-R(\beta)}{X-\beta},
 \quad\deg q_G<k.
 \tag{1}
\]
All roots of \(P_G\) lie in \(B\), and its distinct root set is exactly
\(B\setminus Z(G)\), of size \(D-1\). The \(p^2(p-1)\) labels
\(\lambda_G\) are distinct and nonzero.

Choose **any** set of distinct evaluation points
\[
 B\subseteq S\subseteq E\setminus\{\beta\},\qquad
 p^2+1\le n=|S|\le p^4-1,
 \tag{2}
\]
and use \(\operatorname{RS}_k(S)\) over
\(E'=\mathbb F_{p^8}=E\oplus\omega E\), where \(\omega\notin E\).
On this enlarged domain put
\[
 f(x)=\frac{x^D-\beta^D}{x-\beta},\qquad
 g(x)=\frac1{x-\beta},\qquad
 r_0=f+\omega g,\quad r_1=f+(\omega+1)g.
 \tag{3}
\]
Then
\[
 A(r_0)=A(r_1)=A_{\rm common}(r_0,r_1)=k.
 \tag{4}
\]
Indeed, any codeword \(q=q_0+\omega q_1\), with \(q_i\in E[X]\)
of degree less than \(k\), matching either endpoint must have
\(q_1(x)=g(x)\) at every matching position. The nonzero polynomial
\((X-\beta)q_1-1\), of degree at most \(k\), has at most \(k\) roots.
Interpolation on any \(k\) positions attains equality for either
endpoint. Simultaneous interpolation gives common agreement at least
\(k\), and subtracting the two explanations gives the reciprocal
direction bound for the reverse inequality.

The affine line through these endpoints is
\[
 (1-t)r_0+tr_1=f+(\omega+t)g.
 \]
At each of the \(p^2(p-1)\) distinct interior labels
\(t_G=\lambda_G-\omega\), equation (1) gives
\[
 f+\lambda_Gg-q_G=\frac{P_G}{X-\beta}.
 \tag{5}
\]
There are exactly \(D-1\) agreement coordinates for this displayed
witness on the **entire enlarged domain**, since no root of \(P_G\)
lies outside \(B\).

We may therefore use the full canonical threshold
\[
 T=D-1=p^2-p-1,\qquad T-k=p-1.
 \tag{6}
\]
It lies strictly below the finite Johnson threshold: for the smallest
allowed \(n=p^2+1\),
\[
 n(k-1)-T^2=p^2-4p-2>0,
 \tag{7}
\]
and the left side increases with \(n\).
Both endpoint gaps and the common gap equal the whole agreement
capacity margin \(T-k\). The exceptional set has **at least**
\(p^2(p-1)\) labels. No complete-set or singleton assertion is made
after padding: new evaluation points can help other witnesses.

For any fixed \(0<\rho<1\), take \(n=\lceil k/\rho\rceil\);
conditions (2) hold for all sufficiently large \(p\). Then
\[
 \frac{k}{n}\longrightarrow\rho,\qquad
 |\{t_G\}|=\Theta(n^{3/2}),\qquad
 \frac{T-k}{n}=\Theta(n^{-1/2}),
 \qquad
 \frac{T-A(r_i)}{T-k}=1.
 \tag{8}
\]
Thus fixed rate, two far affine endpoints, and a superlinear bank
survive this operation. The threshold has \(T/n\to\rho<a_1(\rho)\),
so it remains below first order. The domain still has order \(p^2\);
the message dimension still exceeds the characteristic. This is an
elementary transfer of the high-rate theorem, not a short-domain,
prime-alphabet, fixed-positive-margin, or practical-security claim.

## 2. Arbitrary puncturing and lower degree: an exact circle-support bound

Here the domain is an arbitrary subset \(S\subseteq B\), of size \(m\),
and the new code is \(\operatorname{RS}_{k'}(S)\), with
\(1\le k'<m\). Keep the received pencil \(f+\lambda g\), restricted
from the Hermitian construction, where \(g=1/(X-\beta)\).
Adding codewords to either source does not change the argument.

Let a retained bank consist of \(b\) distinct Hermitian circles
\(C_i=Z(G_i)\), with their distinct original labels \(\lambda_i\).
Assume only that for each \(i\) there is **some new**
degree-\(<k'\) witness \(h_i\) whose errors are contained in
\(C_i\cap S\):
\[
 f(x)+\lambda_i g(x)=h_i(x)\quad
 \text{for every }x\in S\setminus C_i.
 \tag{9}
\]
The witness need not be the restriction or remainder of \(q_{G_i}\);
errors may vanish at some circle points. Put
\[
 \Delta=m-k',\qquad r_i=|C_i\cap S|.
\]
For distinct \(i,j\), subtracting (9) supplies a degree-\(<k'\)
explanation for \(g\) on at least \(m-r_i-r_j\) positions.
The reciprocal has exact agreement \(k'\) on any such domain, so
\[
 r_i+r_j\ge\Delta.
 \tag{10}
\]

Two distinct Hermitian circles intersect in at most two native points.
Their defining polynomial difference is a nonzero trace-linear
polynomial, unless it is a nonzero constant. In the former case its
zeros form an affine \(\mathbb F_p\)-line. Restricting a nonzero-radius
norm equation to such a line is a quadratic with nonzero leading
coefficient, so it has at most two roots.

Suppose \(b\ge2\), and write
\(\bar r=b^{-1}\sum_i r_i\). Averaging (10) gives
\(\bar r\ge\Delta/2\). If \(\nu_x\) is the number of retained
circles through \(x\in S\), then
\[
 \sum_x\nu_x=b\bar r,\qquad
 \sum_x\nu_x^2
 =\sum_i r_i+2\sum_{i<j}|C_i\cap C_j\cap S|
 \le b\bar r+2b(b-1).
\]
Cauchy--Schwarz therefore gives the exact inequality
\[
 b(\bar r^2-2m)\le m(\bar r-2).
 \tag{11}
\]
If \(\Delta^2>8m\), then \(m\ge3\), and the function
\(m(u-2)/(u^2-2m)\) decreases for \(u\ge\Delta/2\).
It follows that
\[
 \boxed{\quad
 b\le\frac{2m\Delta-8m}{\Delta^2-8m}
 \quad}
 \qquad(b\ge2,\ \Delta^2>8m).
 \tag{12}
\]
In particular, if \(k'/m\to\rho<1\), then
\[
 b\le\frac{2}{1-\rho}+o(1).
 \tag{13}
\]
Thus arbitrary puncturing plus a fixed-rate degree reduction cannot
retain a superlinear portion of this circle-support bank. This holds
without a common set of agreement coordinates and without assuming
the old witness polynomials remain codewords.

The bound does not cover new near witnesses whose errors occur away
from their corresponding original circles. It also does not close
high-rate puncturing with \(\Delta=O(\sqrt m)\): the denominator in
(12) may cease to be positive. Those are separate construction
problems, rather than consequences of the present operation.

## 3. Affine corrections before shortening do not give a new large bank

A natural enlargement of common-agreement shortening is to first
subtract a fixed affine source correction. Suppose that on every
deleted coordinate \(x\) the original canonical witnesses satisfy
\[
 q_{G_i}(x)=A(x)+\lambda_i B(x)
 \tag{14}
\]
for two fixed value functions \(A,B\). This is the necessary condition
for the usual common factor division to preserve a received affine
pencil; no degree bound on these two functions is needed here.

The canonical error
\[
 e_i(x)=f(x)+\lambda_i g(x)-q_{G_i}(x)
 \]
is zero exactly when \(x\notin C_i\), and nonzero when \(x\in C_i\).
At a coordinate satisfying (14), \(e_i(x)\) is affine in the distinct
labels \(\lambda_i\). If it vanishes for two indices, it vanishes
for all of them. Therefore each deleted coordinate either avoids
every retained circle, or belongs to all but at most one of them.

Let \(v\) be the number of deleted coordinates of the latter type.
The circle intersection bound gives
\[
 v\binom{b-1}{2}
 \le\sum_{i<j}|C_i\cap C_j|
 \le2\binom b2,
 \qquad
 v\le\frac{2b}{b-2}.
 \tag{15}
\]
For \(b\ge7\), at most two deleted coordinates have this type.
All other deleted positions are common agreement coordinates.
Thus shortening a fixed positive fraction of the original \(p^2\)
positions by an affine correction reduces, up to two positions, to
the already audited common-agreement shortening bound. That bound
retains only \(O(p^2)\) circles.

This last observation permits arbitrary fixed affine corrections,
but not a correction depending nonlinearly on the challenge. Such
a correction would need a new proof that the received family remains
an affine line.

## Outcome

Padding gives a precise positive fixed-rate transfer with all original
labels and exact two-source farness over the degree-eight alphabet.
It preserves the vanishing margin scale and does not shorten the
domain. Support-preserving puncturing with a fixed-rate degree change
has the stronger obstruction (12), while affine-corrected shortening
essentially reduces to the existing common-agreement argument.
No field, domain, label, or codeword scan was used; no manuscript file
was edited.
