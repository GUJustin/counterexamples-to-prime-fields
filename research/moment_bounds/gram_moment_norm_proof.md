# Exact uniform-grid Gram polynomial norm

Date: 2026-09-15. This is a self-contained derivation of a classical discrete Chebyshev/Gram polynomial identity; no novelty claim. No canonical manuscript edits.

## Statement and normalization

Fix an integer `n >= 2`. Write

\[
(x)_{\underline j}=x(x-1)\cdots(x-j+1),\qquad
\Delta f(x)=f(x+1)-f(x),\qquad
\nabla f(x)=f(x)-f(x-1).
\]

For `0 <= j < n`, define

\[
F_j(x)=(x)_{\underline j}(x-n)_{\underline j},
\qquad
B_j(x)=\frac{\Delta^j F_j(x)}{(2j)!}.
\tag{1}
\]

The candidate formula and its indexing are **correct as written**, with falling factorials and the forward difference. Its leading coefficient is `1/j!`. For `X` uniform on `{0,...,n-1}`, the family is orthogonal, and for `1 <= j < n`,

\[
\mathbb E B_j(X)=0,
\qquad
\operatorname{Var}(B_j(X))
=\mathbb E B_j(X)^2
=\frac{\prod_{i=1}^{j}(n^2-i^2)}
{(2j+1){2j\choose j}^{\!2}(j!)^2}.
\tag{2}
\]

In particular, `B_j` is the degree-`j` polynomial with leading coefficient `1/j!` obtained by orthogonalizing `binom(x,j)` against all smaller degrees.

## Self-contained proof

### 1. Leading coefficient

`F_j` is monic of degree `2j`. Each forward difference lowers the degree by one and multiplies the leading coefficient by the previous degree. Consequently `Delta^j F_j` has degree `j` and leading coefficient `(2j)!/j!`. Division by `(2j)!` proves the asserted normalization. It also gives

\[
\nabla^j B_j(x)=1.
\tag{3}
\]

### 2. Exact summation by parts, including boundaries

The zeros of `F_j` include

\[
0,\ldots,j-1\quad\text{and}\quad n,\ldots,n+j-1.
\]

For any polynomial `p`, expand the forward difference and put `y=x+t`:

\[
\begin{aligned}
\sum_{x=0}^{n-1}p(x)\Delta^j F_j(x)
&=\sum_{t=0}^{j}(-1)^{j-t}{j\choose t}
  \sum_{x=0}^{n-1}p(x)F_j(x+t)\\
&=\sum_{y=j}^{n-1}F_j(y)
  \sum_{t=0}^{j}(-1)^{j-t}{j\choose t}p(y-t)\\
&=(-1)^j\sum_{y=j}^{n-1}F_j(y)\nabla^j p(y).
\end{aligned}
\tag{4}
\]

The second equality is exact: terms outside `j <= y <= n-1` vanish by the listed boundary zeros, and inside that interval every `0 <= t <= j` gives `0 <= y-t <= n-1`.

For `deg p < j`, the right side is zero. Thus `B_j` is orthogonal to every smaller-degree polynomial. Taking `p=1` gives its mean zero when `j>=1`; taking `p=B_i` for `i<j` gives pairwise orthogonality.

### 3. Evaluate the squared norm

Use (4) with `p=B_j`, then (3):

\[
\sum_{x=0}^{n-1}B_j(x)^2
=\frac{(-1)^j}{(2j)!}\sum_{y=j}^{n-1}F_j(y).
\tag{5}
\]

For `j <= y <= n-1`,

\[
(-1)^jF_j(y)
=(j!)^2{y\choose j}{n-y+j-1\choose j}.
\tag{6}
\]

The convolution identity

\[
\sum_{y=j}^{n-1}{y\choose j}{n+j-1-y\choose j}
={n+j\choose 2j+1}
\tag{7}
\]

has a direct counting proof: choose `2j+1` elements of `{0,...,n+j-1}` and sum over their middle element `y`. There are `j` chosen elements below and `j` above it.

Combining (5)--(7) yields the useful equivalent form

\[
\boxed{\quad
\sum_{x=0}^{n-1}B_j(x)^2
=\frac{(j!)^2}{(2j)!}{n+j\choose 2j+1}.
\quad}
\tag{8}
\]

Since

\[
\frac{(n+j)!}{(n-j-1)!}
=n\prod_{i=1}^{j}(n^2-i^2),
\]

division of (8) by `n` gives (2). All factorials have nonnegative arguments because `j<n`.

### 4. Uniqueness and extremal interpretation

The uniform-grid inner product is positive definite on polynomials of degree `<n`: a nonzero such polynomial cannot vanish at all `n` grid points. Hence the leading coefficient and orthogonality determine `B_j` uniquely.

For any degree-`j` polynomial `P` with the same leading coefficient, write `P=B_j+q`, `deg q<j`. Orthogonality gives

\[
\mathbb E P(X)^2=\mathbb E B_j(X)^2+\mathbb E q(X)^2,
\]

and

\[
\operatorname{Var}(P(X))
=\operatorname{Var}(B_j(X))+\operatorname{Var}(q(X)).
\]

Thus (2) is also the minimum variance after arbitrary lower-degree adjustments; variance equality permits an additive constant, while the minimum squared norm is uniquely attained by `B_j`.

## Checks and endpoint qualifications

- `j=1`: `B_1(x)=x-(n-1)/2`, with variance `(n^2-1)/12`.
- `j=2`: `B_2(x)=((x-(n-1)/2)^2-(n^2-1)/12)/2`, with variance `(n^2-1)(n^2-4)/720` (when `n>=3`).
- `j=0`: `B_0=1`; the empty-product formula gives squared norm 1, but its **variance is 0**, so the variance statement requires `j>=1`.
- At `j>=n`, the uniform-grid inner product is no longer positive definite on degree-`j` polynomials. The stated result intentionally assumes `j<n`.
- These are real/rational norms and variances. Interpreting a rational identity modulo a prime requires checking its denominators separately; the probabilistic variance claim here is over the reals.

## Primary-source provenance and normalization conversion

[Y. Lin and R. Wong, *Global Asymptotics of the Discrete Chebyshev Polynomials*, arXiv:1207.2536, equations (1.1)--(1.2)](https://arxiv.org/pdf/1207.2536) state the forward-difference formula and exact norm for their classical polynomial `t_j(x,n)`. Their normalization and ours satisfy

\[
t_j(x,n)=\frac{\Delta^j F_j(x)}{j!},
\qquad
B_j(x)=\frac{j!}{(2j)!}\,t_j(x,n).
\]

Their equation (1.2) gives

\[
\sum_{x=0}^{n-1}t_j(x,n)^2
=\frac{(n+j)!}{(2j+1)(n-j-1)!},
\]

which converts exactly to (8). Their introduction identifies this as the zero-parameter Hahn specialization. The result is therefore classical, not a new norm identity.

For a second normalization check, [NIST DLMF, Tables 18.19.1--18.19.2](https://dlmf.nist.gov/18.19) use Hahn polynomials on `{0,...,N}`. With `N=n-1` and both Hahn parameters zero, the correct conversion is

\[
B_j(x)
=\frac{(-1)^j j!(n-1)_{\underline j}}{(2j)!}
Q_j(x;0,0,n-1).
\]

The shift `N=n-1` is essential. DLMF's Pochhammer symbols are rising factorials, whereas (1) explicitly uses falling factorials.
