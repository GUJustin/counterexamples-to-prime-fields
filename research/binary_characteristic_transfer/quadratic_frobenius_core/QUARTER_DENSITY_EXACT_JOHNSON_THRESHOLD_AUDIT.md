# Quarter-density puncturing: exact threshold below Johnson

September 18, 2026. **Independent audit: PASS.** This strengthens only the tested threshold in density_quarter_puncturing.tex; the selected-domain existence argument and its complete witness classification are unchanged.

For every prime \(p\ge257\), retain the existing
\[
n=(5p^2-1)/2,\qquad A=2p,\qquad B=(p+1)(p^2-1),
\]
and replace \(\lfloor11p/5\rfloor\) by
\[
T=\left\lceil\sqrt{5p^2-1}\right\rceil-1
 =\left\lfloor\sqrt{5p^2-2}\right\rfloor.
\]
The second expression has the exact integer implementation:

    T = isqrt(5*p*p - 2)

It handles a perfect-square radicand without accidentally including the Johnson boundary. By definition, \(T\) is the largest integer strictly below \(\sqrt{2n}\).

## The existing support guarantee is sufficient

Every doubly canonical witness already has at least
\[
L=2p-2+\lceil p/4\rceil\ge \frac{9p}{4}-2
\]
agreements. Both sides are positive, and
\[
L^2-(5p^2-1)
\ge \frac{p^2-144p+80}{16}>0\qquad(p\ge257).
\]
Indeed the numerator is positive at \(p=144\), with value \(80\), and its derivative is positive for \(p\ge144\). Thus
\[
L>\sqrt{2n}>T.
\]
Also \((2p+1)^2\le5p^2-2\) for every integer \(p\ge5\), so \(T\ge2p+1>A\).

All singly canonical and noncanonical witnesses have at most \(A\) matches, while every doubly canonical witness still qualifies at \(T\). Therefore the same normalized line has exactly \(B\) singleton-list parameters, one further parameter with list size \(p+1\), and empty lists elsewhere. The two source agreements and common agreement remain exactly \(A\). The existing first-order proof is unchanged:
\[
n a_1(3/n)<A<T<\sqrt{2n}.
\]

No exact agreement of an individual nearby witness with \(T\) is claimed: its agreement may exceed \(T\), and the proof now guarantees that it does.

## Improved ratio and finite onset

Since \(T/p\to\sqrt5\), the relative source and common-agreement loss satisfies
\[
\frac{T-A}{T-3}\longrightarrow 1-\frac{2}{\sqrt5}.
\]
At the smallest advertised prime \(p=257\), all arithmetic is integral:

| Quantity | Value |
| --- | ---: |
| \(n\) | 165122 |
| \(A\) | 514 |
| guaranteed canonical agreement \(L\) | 577 |
| strengthened \(T\) | 574 |
| \(2n-T^2\) | 768 |
| \((T+1)^2-2n\) | 381 |
| singleton parameters \(B\) | 17040384 |
| further list size | 258 |
| loss divided by capacity margin | \(60/571\) |

The alphabet is still \(\mathbb F_{p^4}\), the domain is selected by the existing existence argument, and \(p=\Theta(\sqrt n)\). This does not give a prime-alphabet transfer, an explicitly enumerated retained domain, or a practical fixed-domain construction.
