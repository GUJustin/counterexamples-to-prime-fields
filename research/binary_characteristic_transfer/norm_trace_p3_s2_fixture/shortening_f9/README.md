# Restriction of the 648-word norm–trace bank to the fixed subfield F9

This is a bounded shortening pilot for the saved \(p=3,s=2\) fixture, not a
new counterexample. The coefficient field remains \(E=\mathbb F_{6561}\);
the domain is the nine native points of \(\mathbb F_9\subset\mathbb F_{81}\).
Strict dimension \(k'\) means degree less than \(k'\).

The input bank, field encoding, pole \(\beta\), and corrected endpoint
constant \(c_\star^3=\Lambda(\beta)^2\) are taken from the parent fixture.
The original received words are
\[
 f=\frac{X^{54}-\beta^{54}}{X-\beta},\qquad
 g=\frac1{X-\beta},\qquad
 r_0=f+c_\star g,\quad r_1=c_\star g.
\]
For every saved label \(\lambda=P_G(\beta)\), the script reconstructs the
canonical witness and its affine scaling \(c_\star/\lambda\), then reduces
both modulo \(X^9-X\). It checks all nine residual values directly.

## Exact finite output

All 648 original witnesses and all 648 scaled affine witnesses reduce to
degree exactly eight. None of these unmodified reduced witnesses belongs
to a strict code of dimension \(k'\le8\).

| Retained agreements on F9 | Number of labels |
|---:|---:|
| 4 | 144 |
| 5 | 252 |
| 7 | 180 |
| 8 | 72 |

Over \(E\), the full raw bank and scaled bank each have linear span rank
nine and difference span rank nine. For every fixed \(a\in\mathbb F_9^*\),
the 81-translation raw bank has linear rank nine and difference rank eight;
its scaled affine bank has both ranks nine.

For each of the five entire groups retaining at least \(4,5,6,7,8\)
agreements, the script forms the columns consisting of \(1\), the label,
and witness coefficients of degrees \(k',\ldots,8\). Its rank minus two is
\[
 9-k'\qquad(1\le k'\le8).
\]
The same result holds with the actual affine parameter and scaled
witnesses. Thus no one fixed affine-in-label correction cancels all the
high coefficients on any of these whole groups, including the best
72-word group. This does not exclude selected smaller subsets or other
witnesses. No subset search was performed.

## Exact all-witness consequence for dimensions six through eight

On the shortened domain \(X^{54}=X^6\). Put
\[
 L(X)=\frac{X^6-\beta^6}{X-\beta},\qquad
 \alpha=\beta^6-\beta^{54}.
\]
Then \(\deg L=5\) and, as received words on \(\mathbb F_9\),
\[
 f=L+\alpha g,\qquad
 (1-t)r_0+tr_1=(1-t)L+\bigl((1-t)\alpha+c_\star\bigr)g.
\]
The script verifies this identity and verifies
\(\alpha\ne0\), \(c_\star\ne0\), and \(\alpha+c_\star\ne0\).

For \(k'\in\{6,7,8\}\), \(L\) is a codeword. A codeword plus a nonzero
multiple of \(1/(X-\beta)\) has exactly \(k'\) agreements with the strict
dimension-\(k'\) code: clearing the denominator gives a nonzero polynomial
of degree at most \(k'\), while interpolation on any \(k'\) coordinates
attains this bound. Consequently both endpoints and their common
agreement equal \(k'\). Exactly one affine parameter,
\[
 t_\star=1+\frac{c_\star}{\alpha},
\]
gives a codeword and can have more than \(k'\) agreements. It is distinct
from both endpoints. Every other affine word has exact agreement \(k'\).
This conclusion bounds all codewords, not just the saved bank.

In the parent field encoding, \(\alpha=2893\), the exceptional original
pencil label is \(4733\), and \(t_\star=4673\). These are encodings, not
integers interpreted in the prime subfield.

The exact conclusion above is limited to \(k'=6,7,8\). The rank data for
\(k'\le5\) do not classify arbitrary subsets or all possible codewords.
The original 81-coordinate source bound is not assumed after restriction.

## Integer threshold obstruction at lengths nine and 27

There is also a construction-independent obstruction to the proposed
first-order/Johnson target at both of these lengths. For every strict
dimension \(1\le k<n\), there is no integer \(T\) satisfying
\[
 n a_1(k/n)<T<\sqrt{n(k-1)}
 \qquad(n=9\ \text{or}\ 27).
\]
Here the right side is the finite Johnson threshold for degree less than
\(k\). For \(k=1\) it is zero. For \(k\ge2\), the largest admissible integer
is \(T_{\max}=\lfloor\sqrt{n(k-1)-1}\rfloor\), so it suffices to check this
one integer per dimension.

For the high branch, whose boundary is
\(\rho_c=11-3\sqrt{13}\), \(a_1(\rho)\) is the unique positive root of
\[
 F(a,\rho)=(8-\rho)a^2-6\rho a+\rho(4\rho-5).
\]
All dimensions \(2,\ldots,8\) at length nine are in this branch. Exact
substitution gives:

| \(k\) | \(T_{\max}\) | \(F(T_{\max}/9,k/9)\) |
|---:|---:|---:|
| 2 | 2 | \(-602/729\) |
| 3 | 4 | \(-145/243\) |
| 4 | 5 | \(-424/729\) |
| 5 | 5 | \(-800/729\) |
| 6 | 6 | \(-26/27\) |
| 7 | 7 | \(-532/729\) |
| 8 | 7 | \(-824/729\) |

At length 27, all \(k=5,\ldots,26\) likewise have negative high-branch
polynomial values at \(T_{\max}\); the complete rational table is in
integer_windows.json. For the three remaining dimensions:

* \(k=2,T_{\max}=5\): \(\rho/2-a^2=2/729>0\), so
  \(a<\sqrt{\rho/2}<a_1(\rho)\).
* \(k=3,T_{\max}=7\) and \(k=4,T_{\max}=8\): put
  \(b=\sqrt{\rho/2}\) and \(u_0=a/b-1>0\). The low branch is
  \(a_1=b(1+u)\), where \(u^2(u+3)=b\). To verify \(u_0<u\), set
  \[
  R=\rho^2/4-a^3+3a\rho/2.
  \]
  It suffices that \(R>0\) and \(R^2-\rho^3/2>0\). The exact pairs are
  \[
  \left(\frac{2273}{78732},\frac{915001}{6198727824}\right),
  \qquad
  \left(\frac{892}{19683},\frac{165808}{387420489}\right),
  \]
  respectively.

The standalone verifier uses only exact integer and rational arithmetic
and independently reproduces these comparisons. Thus the proposed
27-coordinate trace-hyperplane field pilot was cancelled before any
field computation. No arbitrary-subset optimization at length nine is
needed for this particular target. This does not rule out other lengths
or comparisons outside the stated strict window.

## Reproduction and scope

Run from the repository root:

    /Users/jthaler/.local/share/research-toolchain/venv/bin/python research/binary_characteristic_transfer/norm_trace_p3_s2_fixture/shortening_f9/verify.py

The saved run took 1.63 seconds. The script writes receipt.json and leaves
the parent certificate unchanged. Its SHA-256 is
09975e9fdabdcaed50a25ea8e5a8fbdcc9a63bf2e834821f71288db71ac7428c.
The input bank hash is
d69ce3fc1159feaee6e9cc81e634bfcd3b89b619b6297dfb5a35584fdde04f68.
The input verifier hash is
eb06422d9a3d4fa89eeca7a4377383a874826ab3e9cb8c5ad6a1bb793f4c2e5d.

The separate parameter check is reproduced by:

    python3 research/binary_characteristic_transfer/norm_trace_p3_s2_fixture/shortening_f9/verify_integer_windows.py

The output combines exact finite-field ranks and residuals, the reciprocal
root-bound proof, and the separate integer-window check. It does not
enumerate all codewords or address puncturings of other lengths.
