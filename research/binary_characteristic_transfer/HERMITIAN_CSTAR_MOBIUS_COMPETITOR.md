# A competing witness for the explicit c-star endpoint

The second explicit endpoint also has a structured competitor for
infinitely many relevant primes. Together with
HERMITIAN_SOURCE_MOBIUS_COMPETITOR.md, this rules out a uniform positive
fraction of the capacity margin for either of the two prescribed
quartic-alphabet endpoints. It does not address arbitrary alternative
endpoint choices on the line.

Use \(B=\mathbb F_{p^2}\subset E=\mathbb F_{p^4}\),
\(\beta\in E\setminus B\), \(D=p^2-p\), \(K=p^2-2p\), and

\[
 f_\beta=\frac{X^D-\beta^D}{X-\beta},\qquad
 g_\beta=\frac1{X-\beta},\qquad
 c_*^p=(\beta^{p^2}-\beta)^{p-1}.
\]

## Exact competitor lemma

Suppose

\[
 2\le e<p,\qquad m=p+e\mid p^2-1,
 \tag{1}
\]

and there exists \(t\in E\setminus B\) with

\[
 t^{p^3+e}=1.
 \tag{2}
\]

For every exterior pole \(\beta\), the word \(f_\beta+c_*g_\beta\)
has a strict-degree-\(<K\) witness with exactly \(D-e\) agreements on
the full domain \(B\).

To construct it, express

\[
 \beta=b+\gamma/t,\qquad b\in B,\quad\gamma\in B^*.
\]

This is always possible because \(1,1/t\) is a \(B\)-basis of \(E\).
Writing bars for conjugation over \(B\), explicitly

\[
 \gamma=\frac{\beta-\bar\beta}{t^{-1}-\bar t^{-1}},
 \qquad b=\beta-\gamma/t.
\]

Put \(q=X-b\) and

\[
 G=q^{p+e}-\gamma^{p+e},\qquad F=q^e,\qquad
 A=-b^pF-\gamma^{p+e}.
\]

Then \(G\) is the monic split locator of
\(b+\gamma\mu_m\), with \(m\) distinct native roots. Also

\[
 G=X^pF+A,\qquad \deg A\le e,\qquad \gcd(F,G)=1.
\]

The corresponding rational map is

\[
 Q=-A/F=b^p+\frac{\gamma^{p+e}}{(X-b)^e}.
\]

At \(\beta=b+\gamma/t\), condition (2) gives

\[
 Q(\beta)=b^p+\gamma^p t^e
          =b^p+\gamma^p t^{-p^3}
          =\beta^{p^3}.
 \tag{3}
\]

Define \(\Lambda=X^{p^2}-X\) and \(P=F\Lambda/G\). As before,
\(P\) is monic of degree \(D\), \(\deg(P-X^D)\le K\), and its distinct
native roots are exactly \(B\setminus Z(G)\), of cardinality \(D-e\).
Here the native root of \(F\) is already in that complement.

Since \(F(\beta)\ne0\), equation (3) yields

\[
 G(\beta)^p=(\beta^{p^2}-\beta)F(\beta)^p.
\]

Consequently

\[
 P(\beta)^p=(\beta^{p^2}-\beta)^{p-1}=c_*^p,
 \qquad P(\beta)=c_*.
\]

Thus

\[
 h=\frac{X^D-P+c_*-\beta^D}{X-\beta}
\]

is a polynomial of degree at most \(K-1\), and

\[
 f_\beta+c_*g_\beta-h=\frac{P}{X-\beta}.
\]

This proves the exact witness agreement. The result is a lower bound
on the source's nearest agreement, not a full distance classification.

## A fifth root provides the required exterior point

A particularly simple sufficient condition for (2) is

\[
 p\bmod5\in\{2,3\},\qquad e\equiv p\pmod5.
 \tag{4}
\]

Indeed a primitive fifth root \(t\) lies in \(\mathbb F_{p^4}\) but
not \(\mathbb F_{p^2}\), since \(p^2\equiv-1\pmod5\).
Moreover \(p^3+e\equiv-p+e\equiv0\pmod5\).

The small example \(p=13,e=8\) satisfies (1) and (4): \(m=21\)
divides \(168\). It does **not** need \(L=(p^2-1)/m>e\), which was a
sufficient condition for the separate zero-endpoint construction.
The bounded verifier verify_hermitian_cstar_competitor.py constructs
the fields, the fifth root, the locator, and the witness. Its exact
ledger is

\[
 n=169,\quad K=143,\quad T=154,\quad
 \deg h=142,\quad \operatorname{agr}(h,f+c_*g)=148.
\]

The existing universal theorem gives the upper bound \(152\) on this
source's nearest agreement. The finite certificate therefore proves
\(148\le\operatorname{agr}_K(f+c_*g)\le152\), not equality at \(148\).
It checks all 169 native residuals and performs no codeword enumeration.

## Both explicit endpoints have arbitrarily small relative gaps

Fix an odd integer \(r\ge3\) with \(r\equiv3\pmod5\), and let

\[
 j=10h+7,\qquad e=1+rj,\qquad
 p=(r-1)e+r.
\]

The prime progression is

\[
 p=10r(r-1)h+(7r^2-5r-1).
 \tag{5}
\]

Its residue is coprime to the modulus: it is odd, is \(-1\) modulo
\(r\), \(1\) modulo \(r-1\), and \(2\) modulo five.
Dirichlet's theorem gives infinitely many prime values for each fixed
\(r\).

For these parameters \(e\) is even,

\[
 e\equiv p\equiv2\pmod5,\qquad
 m=p+e=r(e+1)\mid p^2-1.
\]

Also \(L=(r-1)(p+1)/r>e\), so the preceding zero-endpoint lemma
and the present c-star lemma both apply, for **every** exterior pole.
At the common tested threshold \(T=D-2\), each endpoint consequently
satisfies

\[
 T-\operatorname{agr}_K(r_i)\le e-2,
 \qquad
 \limsup_{\substack{p\to\infty\\\text{in (5)}}}
 \frac{T-\operatorname{agr}_K(r_i)}{T-K}
 \le\frac1{r-1},
 \quad r_i\in\{f_\beta,f_\beta+c_*g_\beta\}.
\]

Taking unbounded \(r\equiv3\pmod{10}\) and a sufficiently large prime
from each progression gives an unconditional sequence on which both
ratios tend to zero. Thus no uniform constant-fraction improvement
for these two prescribed endpoints can follow from extra pole
constraints alone.

The earlier exclusion of c-star from the prime-quadratic saturated
orbit is consistent with this result: (4) selects different arithmetic
parameters. The exact Hermitian singleton bank and its below-first-order
placement are unchanged. Whether another pair of endpoints on the
same line has a better gap is a separate question.
