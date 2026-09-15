# Independent review of the degree-25 radial certificate

2026-09-15. **The original rational-coefficient certificate is valid.** It
proves an unconditional class-size and Reed–Solomon list lower bound of
**5,133,798,314,667** at \(n=64,t=34,k=32\), for every prime \(p>64\).
No substantive arithmetic or mathematical error was found.

This exceeds the older degree-20 conditional certificate
5,074,503,250,115, but is **not the largest current certificate**: the
concurrent integration reports stronger degree-24 and degree-28 conditional
certificates. This review verifies the original rational polynomial in the
last entry of `certificates_grid12.json`; it does not independently certify
the separately rounded root-factor representation.

## Scope and source data

Reviewed source directory:
`/Users/jthaler/Documents/frontier_attacks_2026-09-15/stwo_port_review/radial_moment_experiment/`.
Files reviewed: `moments.py`, `verify.py`, `moments_degree50.json`,
`certificates_grid12.json`, and `crosscheck_saved_certificate.py`.

The original data files have SHA-256 hashes:

| File | SHA-256 |
|---|---|
| `moments_degree50.json` | `b6cd6f45bbb056394d4d7ca8c3134f3a5eef693d8be75f79f1621ba5c3ef8f7e` |
| `certificates_grid12.json` | `df7e976c9ac66cac58f1958cf13e6dc7ffe1aee057228781bf35adc0f38c6c1d` |

## 1. The even-\(X\) recurrence is closed and exact

For an element \(a\), put \(u_a=2a-63\) and

\[
 v_a=(u_a^2-1365)/4,
 \qquad X(A)=\sum_{a\in A}u_a,
 \qquad Y(A)=\sum_{a\in A}v_a.
\]

The 64 elements split into pairs with contributions \((u,v)\) and
\((-u,v)\), where \(u=1,3,\ldots,63\). For a selected subset of the
previous pairs, the four choices from the next pair add

\[
 (0,0),\quad(u,v),\quad(-u,v),\quad(0,2v)
\]

and increase its size by \(0,1,1,2\), respectively. If \(i\) is even,
the sum of the two one-element contributions to \(X^iY^j\) is

\[
 2\sum_{\substack{0\le p\le i\\p\text{ even}}}
   \sum_{q=0}^j
   {i\choose p}{j\choose q}X^pY^q u^{i-p}v^{j-q}.
\]

Odd powers of \(X\) cancel algebraically, so no discarded odd-\(X\)
moment is needed. Choosing both elements gives

\[
 \sum_{q=0}^j{j\choose q}X^iY^q(2v)^{j-q}.
\]

These are exactly the transitions in `moments.py`. The empty-subset
initial condition, size truncation, and use of the old stage as the source
are correct. Total degree never increases in the needed source moments.
Thus the degree-50 truncation suffices, and the 676 stored mixed moments
are raw sums over subsets, not normalized expectations.

The population totals of both coordinates are zero. Complementation
therefore sends \((X,Y)\) to \((-X,-Y)\), so the radial statistic is
identical on a 30-subset and its 34-subset complement. The computation at
size 30 correctly counts the size-34 population of

\[
 N={64\choose30}={64\choose34}=1620288010530347424.
\]

## 2. Coordinates, variances, and scaling

All \(u_a,v_a\) are odd integers. Since both subset sizes are even,
\(x=X/2\) and \(y=Y/2\) are integers. At size 34, writing
\(M_1=\sum a\) and \(M_2=\sum\binom a2\),

\[
 x=M_1-1071,\qquad y=M_2-31M_1+11067.
\]

This invertible affine integer transformation shows that equal \((x,y)\)
means equal first and second integer binomial moments. These are precisely
the centered first two Gram coordinates, with

\[
 \operatorname{Var}(x)=5525,\qquad
 \operatorname{Var}(y)=376805,
 \qquad
 Q=\frac{x^2}{5525}+\frac{y^2}{376805}
   =\frac{341x^2+5y^2}{1884025}.
\]

In particular \(\mathbb EQ=2\). If \(R_{ij}=\sum_A X(A)^iY(A)^j\)
and \(T=341x^2+5y^2\), the stored radial sums must be

\[
 \sum_A T(A)^d
 =4^{-d}\sum_{i=0}^d{d\choose i}341^i5^{d-i}
       R_{2i,\,2(d-i)}\quad(0\le d\le25).
\]

The factor \(4^{-d}\), all divisibility checks, and the degree-50 cutoff
are correct.

## 3. The integer weight and the entire-lattice denominator

Let \(D=1884025\), \(A=851547/580691=a/b\), and let \(h\) be the saved
degree-12 rational polynomial. The verifier constructs an integer
polynomial \(H(T)=c\,h(T/(DA))\) with positive rational \(c\), then uses

\[
 W(T)=(aD-bT)H(T)^2.
\]

This is a positive scalar multiple of
\((A-Q)h(Q/A)^2\). Its degree in \(T\) is 25; its total degree in
\((X,Y)\) is 50. There is no reliance on numerical eigenvalues, decimal
evaluation, or optimality of the chosen polynomial.

For integer \(T\ge0\), the positive part vanishes unless

\[
 T<DA,\qquad T\le2762804.
\]

The verifier's integer cutoff implements this strict inequality correctly.
Its quadrant multiplicities count exactly all integer pairs satisfying
\(341x^2+5y^2\le2762804\), including the coordinate axes once each.
There are 210,135 such pairs. Including signatures that no subset attains
is valid: it only increases the denominator. A zero of \(H\) inside the
ellipse contributes zero, also correctly.

Let \(n_{x,y}\) denote a class size and \(L=\max n_{x,y}\). The rigorous
inequality is

\[
 0<\mathcal N:=\sum_A W(T(A))
 \le\sum_{x,y}n_{x,y}W(T(x,y))_+
 \le L\,\mathcal D,
 \qquad
 \mathcal D:=\sum_{(x,y)\in\mathbb Z^2}W(T(x,y))_+.
\]

The stored moment sums already include all \(N\) subsets; no extra factor
of \(N\) belongs in this ratio. Exact integer comparison gives

\[
 5133798314666\,\mathcal D<\mathcal N
 \le5133798314667\,\mathcal D,
\]

so the certified lower bound is the ceiling 5,133,798,314,667. The exact
numerator and denominator have 433 and 420 decimal digits, respectively,
and are retained in the hashed certificate file.

## 4. Independent executed checks

The review did more than rerun the supplied final division:

- Regenerated all 676 degree-50 mixed moments and matched every saved
  integer.
- Independently computed moments of \(X+cY\), for \(c=1,2,3\), through
  degree 50 by an **individual-element** include/exclude recurrence
  retaining odd and even powers. All 153 identities matched the mixed
  moment expansion from the saved file.
- Reconstructed all 26 radial moments from the mixed moments, checked
  every rational-to-integer coefficient conversion, and checked the full
  polynomial identity defining \(W\).
- Recomputed the numerator as
  \(\sum_{i,j}H_iH_j[aD\,\sum T^{i+j}-b\,\sum T^{i+j+1}]\),
  independently of the saved expanded coefficient dot product.
- Recomputed the denominator by one-dimensional even-power prefix sums
  and binomial expansion: for each nonnegative \(x\), sum every power of
  \(341x^2+5y^2\) over its full signed \(y\)-interval, then apply the
  \(x\leftrightarrow-x\) multiplicity. This uses neither the verifier's
  pointwise Horner sum nor the supplied crosscheck's full signed-grid
  loop. It reproduced all 210,135 sites and the exact denominator.
- Verified the final ceiling by integer inequalities, without using
  `ratio_float_for_display`.

## 5. Conversion to a Reed–Solomon list

For a class of 34-subsets with equal \(M_1,M_2\), their monic root
polynomials \(F_A(X)=\prod_{a\in A}(X-a)\) share their coefficients in
degrees \(34,33,32\). For every prime \(p>64\), Newton identities are
valid and the domain elements remain distinct. Let \(G\) be those common
leading terms. Then \(G-F_A\) has degree below 32 and agrees with the
received word \(G|_{\{0,\ldots,63\}}\) exactly on \(A\). Different
subsets give different codewords. This proves the stated list lower
bound at relative radius \(30/64\), with no extra field-size condition.

The certificate is a finite lower bound, not an evaluation of the exact
largest class or a proof that the weight is optimal. Its distinction is
the unconditional radial-moment method; the stronger concurrent
conditional certificates should retain precedence in any headline.
