# Signed ellipsoid concentration on a triangular moment lattice

2026-09-15. All proposed steps are valid, with the asymptotic qualification
below. Exact cell averaging gives a stronger finite bound that removes
the proposed radius inflation. No canonical manuscript changes or
protocol computations are involved.

## Setup and strongest finite conclusion

Let a uniformly chosen object from a finite population of size \(N\)
have statistic \(B\in\Lambda\), where

\[
 \Lambda=b_0+T\mathbb Z^m,\qquad m\ge1,
\]

and \(T\) is lower triangular with diagonal entries one. Rationality of
\(T\) is unnecessary. Let \(L\) be the largest statistic-class size,
\(\mu=\mathbb EB\), and \(V_j=\operatorname{Var}(B_j)>0\). Write
\(\kappa_m=\pi^{m/2}/\Gamma(m/2+1)\) for unit-ball volume. Then

\[
 \boxed{\displaystyle
 L\ \ge\ \frac{N}
 {\kappa_m(m+2)^{m/2}\prod_{j=1}^m\sqrt{V_j+1/12}}.}
 \tag{1}
\]

For the moment application take \(N=\binom nt\). The proof needs the
stated coordinate variances; pairwise orthogonality is not required for
(1). If the moment coordinates are orthogonal, their covariance matrix
is diagonal and (1) uses its exact diagonal after smoothing.

The mean need not be a lattice point, but it must be the actual mean.
Centering at an arbitrary different point would add a squared-bias term
to the second-moment identity.

## 1. Axis-aligned unit cubes really do tile

Set \(C=[-1/2,1/2)^m\). The sets \(\lambda+C\), for
\(\lambda\in\Lambda\), partition \(\mathbb R^m\).

For any \(x\), determine integers recursively by

\[
 z_j=\left\lfloor x_j-b_{0,j}-\sum_{i<j}T_{ji}z_i+\frac12\right\rfloor.
\]

For \(\lambda=b_0+Tz\), this gives
\(x_j-\lambda_j\in[-1/2,1/2)\) in every coordinate. Conversely,
membership in such a cube forces \(z_1\), then \(z_2\), and so on,
so the cube is unique. These half-open cubes are measurable, have volume
one, and have centroid \(\lambda\).

This conclusion uses the triangular unit-diagonal structure. Covolume
one alone would not justify an axis-aligned unit-cube tiling.

## 2. Audit of the proposed signed-weight argument

Let

\[
 Q(\lambda)=\sum_j\frac{(\lambda_j-\mu_j)^2}{V_j},\qquad
 P=\prod_j\sqrt{V_j},\qquad
 \epsilon=\frac12\sqrt{\sum_jV_j^{-1}}.
\]

Then \(\mathbb EQ(B)=m\). For \(R>\sqrt m\), let
\(a_\lambda\) be the number of objects with statistic \(\lambda\).
The signed weight is handled in the correct direction:

\[
 N(R^2-m)
 =\sum_\lambda a_\lambda(R^2-Q(\lambda))
 \le\sum_\lambda a_\lambda(R^2-Q(\lambda))_+
 \le L\sum_\lambda(R^2-Q(\lambda))_+.
 \tag{2}
\]

After centering and dividing coordinate \(j\) by \(\sqrt{V_j}\),
the tiling cells have volume \(1/P\) and every point is within
Euclidean distance \(\epsilon\) of its center \(c\). For a positive
center, \(\|c\|<R\), and every cell point \(x\) satisfies

\[
 \|x\|^2-\|c\|^2\le2R\epsilon+\epsilon^2,
 \qquad
 R^2-\|c\|^2\le((R+\epsilon)^2-\|x\|^2)_+.
\]

Integrating over these disjoint cells and then enlarging to all space gives

\[
 \sum_\lambda(R^2-Q(\lambda))_+
 \le P\,\frac{2\kappa_m}{m+2}(R+\epsilon)^{m+2}.
 \tag{3}
\]

Here the radial integral is exactly
\(\int(A^2-\|x\|^2)_+dx=2\kappa_m A^{m+2}/(m+2)\).
Thus the proposed finite bound is valid:

\[
 L\ge\frac{N(m+2)(R^2-m)}
 {2\kappa_m P(R+\epsilon)^{m+2}}.
 \tag{4}
\]

Its unique maximizing radius is

\[
 R_* =\frac\epsilon m+\sqrt{m+2+\frac{\epsilon^2}{m^2}},
 \qquad
 L\ge\frac{NR_*}{\kappa_m P(R_*+\epsilon)^{m+1}}.
 \tag{5}
\]

Indeed the derivative vanishes exactly when
\(2R(R+\epsilon)=(m+2)(R^2-m)\); the objective tends to zero at both
ends of \((\sqrt m,\infty)\).

At the uninflated optimum \(R=\sqrt{m+2}\), the proposed asymptotic
constant is multiplied by the explicit factor

\[
 \left(1+\frac\epsilon{\sqrt{m+2}}\right)^{-(m+2)}.
 \tag{6}
\]

For fixed \(m\), \(\epsilon\to0\) suffices for this factor to tend
to one. For growing \(m\), a sufficient condition for this particular
argument is \(\epsilon\sqrt m\to0\); merely \(\epsilon\to0\)
does not suffice. For example, \(V_j=m^2\) gives a factor tending to
\(e^{-1/2}\) in (6). Bound (1) removes this loss.

## 3. Stronger proof by exact cell smoothing

Let \(U\) be independent of \(B\) and uniform on \(C\), and put
\(Y=B+U\). The tiling proves that its density satisfies, almost
everywhere,

\[
 f_Y(y)=\frac{a_\lambda}{N}\quad\text{on }\lambda+C,
 \qquad \|f_Y\|_\infty=L/N.
\]

Also

\[
 \mathbb EY=\mu,\qquad
 \operatorname{Var}(Y_j)=V_j+\frac1{12}=:W_j.
\]

Standardize \(Z_j=(Y_j-\mu_j)/\sqrt{W_j}\). Then
\(\mathbb E\|Z\|^2=m\), and its density is bounded by
\(M=(L/N)\prod_j\sqrt{W_j}\). Apply the same signed weight to this
continuous distribution:

\[
 R^2-m
 =\int (R^2-\|z\|^2)f_Z(z)\,dz
 \le M\int(R^2-\|z\|^2)_+\,dz
 =M\frac{2\kappa_m}{m+2}R^{m+2}.
\]

Choosing \(R^2=m+2\) proves (1). This argument is exact: it uses the
cube variance \(1/12\), with no worst-case radius enlargement.

For comparison, averaging cells while retaining the original \(V_j\)
already improves (3). With \(\delta=\sum_j1/(12V_j)=\epsilon^2/3\),
the cell average of squared norm is \(\|c\|^2+\delta\). Thus

\[
 \sum_\lambda(R^2-Q(\lambda))_+
 \le P\frac{2\kappa_m}{m+2}(R^2+\delta)^{(m+2)/2}.
\]

Optimizing gives a correction factor \((1+\delta/m)^{-m/2}\)
relative to the limiting constant. Bound (1) is at least as strong,
by the arithmetic-geometric mean inequality. This also confirms directly
that (1) improves the optimized radius-inflation bound (5).

## 4. Asymptotics and rectangular comparison

Bound (1) is equivalently

\[
 L\ge\frac{N}{\kappa_m(m+2)^{m/2}\prod_j\sqrt{V_j}}
 \prod_j\left(1+\frac1{12V_j}\right)^{-1/2}.
 \tag{7}
\]

The last factor tends to one whenever \(\sum_jV_j^{-1}=o(1)\), even
if \(m\) grows. In particular the claimed leading constant follows for
fixed \(m\) with every \(V_j\to\infty\).

The rectangular Chebyshev/union-bound method uses standardized thresholds
\(R\) in every coordinate, mass at least \(1-m/R^2\), and asymptotic
box count \((2R)^m\prod_j\sqrt{V_j}\). Its optimized choice is also
\(R^2=m+2\), giving leading bound

\[
 \frac{N}{2^{m-1}(m+2)^{(m+2)/2}\prod_j\sqrt{V_j}}.
\]

Consequently the proposed improvement ratio is correct:

\[
 \boxed{\frac{(m+2)2^{m-1}}{\kappa_m}.}
\]

This compares leading constants of these two methods; finite lattice
corrections must still be retained when variances are small.

Two useful normalization checks are:

- For \(m=1\), (1) becomes \(L\ge N/\sqrt{12V_1+1}\). It is exact
  for equal class sizes on consecutive integers, whose variance is
  \((q^2-1)/12\) on \(q\) consecutive points.
- For \(m=2\), (1) is
  \(L\ge N/[4\pi\sqrt{(V_1+1/12)(V_2+1/12)}]\), and the leading
  improvement over rectangular Chebyshev is \(8/\pi\).
