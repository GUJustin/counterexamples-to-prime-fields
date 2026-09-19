# Exact full-rank trace--norm specialization in odd characteristic

2026-09-19. The full-rank elliptic construction already appears in
/Users/jthaler/Documents/binary_field_counterexamples/sections/constructions/fullfield-elliptic.tex,
Theorem thm:fullfield-elliptic, high row with its rank parameter equal
to half the ambient dimension. Its compiler and the two-source
normalization below are inherited. This note extracts the exact smaller
code dimension from that proof, proves injection at **every** exterior
pole, and records the finite source/threshold ledger.
The binary repository was read only.

The resulting alphabet is \(\mathbb F_{p^{4s}}\), a quadratic extension
of the evaluation field. It is not a fixed degree-four extension of
the prime field when \(s\) grows. The original fixed-prime-degree-four
padding question is therefore not settled by this specialization.

## Parameters and exact statement

Let \(p\ge3\) be an odd prime and \(s\ge2\). Put
\[
 Q=p^s,\quad B=\mathbb F_{Q^2},\quad E=\mathbb F_{Q^4},\quad
 n=Q^2,\quad \Lambda=X^n-X,\quad \beta\in E\setminus B,
\]
\[
 d=\frac{n+Q}{p},\quad T=n-d,\quad
 D=n-\frac np,\quad k=\frac{(p-1)T}{p},\quad
 U=\left\lfloor\frac{(p+1)k-1}{p}\right\rfloor.
 \tag{1}
\]
All these are integers. There are \(M=n(Q-1)\) distinct certified
interior labels on an affine line over \(E\), each with a displayed
strict-degree-\(<k\) witness having exactly \(T\) matches on \(B\).
The two endpoints can be chosen with
\[
 A(r_0)\le U<T,\qquad A(r_1)=A_{\rm common}(r_0,r_1)=k.
 \tag{2}
\]
In particular,
\[
 T-U=\left\lceil\frac{T}{p^2}+\frac1p\right\rceil,\qquad
 T-k=\frac Tp.
 \tag{3}
\]
The threshold lies above the first-order curve and strictly below
\(\sqrt{n(k-1)}\). These are certified labels and exact agreements
with their displayed witnesses, not an asserted complete label set,
nearest-agreement classification, or singleton-list theorem.

## Split trace--norm locators and normalization

For \(a\in\mathbb F_Q^*\) and \(b\in B\), define
\[
 G_{a,b}(X)=
 \operatorname{Tr}_{\mathbb F_Q/\mathbb F_p}
       \bigl(a(X+b)^{Q+1}\bigr)+1.
 \tag{4}
\]
The trace denotes its polynomial expansion
\(\sum_{i=0}^{s-1}a^{p^i}(X+b)^{(Q+1)p^i}\).
Its degree is \(d\), and its leading coefficient is \(a^{Q/p}\).
There are exactly \(Q/p\) nonzero norm values with trace \(-1\),
each having \(Q+1\) preimages. Thus \(G_{a,b}\) has exactly \(d\)
distinct roots in \(B\), so it divides \(\Lambda\).

Set
\[
 F_{a,b}=a^{Q/p}(X+b)^{Q/p},\qquad
 J_{a,b}=\Lambda/G_{a,b},\qquad P_{a,b}=F_{a,b}J_{a,b}.
\]
The leading coefficients of \(F_{a,b}\) and \(G_{a,b}\) agree.
Hence \(P_{a,b}\) is monic of degree \(D\). The root \(-b\) of
\(F_{a,b}\) already lies in the complement of \(Z(G_{a,b})\),
because \(G_{a,b}(-b)=1\). Consequently \(P_{a,b}\) has exactly
\(T\) distinct roots, all in \(B\).

Telescoping the trace gives
\[
 G_{a,b}^p-G_{a,b}=\Lambda F_{a,b}^p,\qquad
 P_{a,b}^p=\Lambda^{p-1}-J_{a,b}^{p-1}.
 \tag{5}
\]
The first nonleading degree of \(\Lambda^{p-1}\) is
\(n(p-2)+1\), whereas
\[
 \deg J_{a,b}^{p-1}=(p-1)T=pk,
 \qquad
 pk-\bigl(n(p-2)+1\bigr)
 =\frac{(Q-p)(Q+1)}p>0.
 \tag{6}
\]
Thus
\[
 P_{a,b}=X^D+C_{a,b},\qquad \deg C_{a,b}=k.
 \tag{7}
\]
The constant \(1\) in (4) removes the \(\mathbb F_p^*\) scalar
duplicates that would occur if all nonzero trace levels were counted.
There are \(n(Q-1)\) members after this normalization.

## Why every exterior pole is injective

Consider the full \(\mathbb F_p\)-linear space
\[
 \mathcal H=
 \left\{
 \operatorname{Tr}_{Q/p}(aX^{Q+1})
 +\operatorname{Tr}_{B/p}(\ell X)+c:
 a\in\mathbb F_Q,\ \ell\in B,\ c\in\mathbb F_p
 \right\}.
 \tag{8}
\]
Every nonzero polynomial in this space splits over \(B\).
If \(a=0\), this follows from the affine trace equation, or the
polynomial is a nonzero constant. If \(a\ne0\), write
\(\ell=ab^Q\) and complete the norm to obtain
\(\operatorname{Tr}_{Q/p}(a(X+b)^{Q+1})+c'\).
For \(c'\ne0\), the preceding count supplies all \(d\) roots.
For \(c'=0\), there are \(d-Q\) distinct native roots.
The center \(-b\) has multiplicity exactly \(Q+1\), from the
lowest term \(a(X+b)^{Q+1}\); all other roots are simple since the
derivative is \(a(X+b)^Q\). The total multiplicity is again \(d\).
This includes the zero-radius case rather than assuming it squarefree.

Evaluation at any \(\beta\notin B\) is therefore injective on
\(\mathcal H\). If \(P_1(\beta)=P_2(\beta)\), (5) gives
\(G_1(\beta)=uG_2(\beta)\) for some \(u\in\mathbb F_p^*\).
The difference belongs to \(\mathcal H\), so it is the zero polynomial.
Its derivatives first give \(a_1=ua_2\) and \(b_1=b_2\);
evaluation at the common center then gives \(u=1\).
Thus \((a_1,b_1)=(a_2,b_2)\).
The labels
\[
 \lambda_{a,b}=P_{a,b}(\beta)
 \tag{9}
\]
are distinct and nonzero for every prescribed exterior pole.

## Compiler and native two-source bound

Put
\[
 f=\frac{X^D-\beta^D}{X-\beta},\qquad g=\frac1{X-\beta}.
\]
Equation (7) gives a strict-degree witness
\[
 h_{a,b}=\frac{X^D-P_{a,b}+\lambda_{a,b}-\beta^D}{X-\beta},
 \qquad
 f+\lambda_{a,b}g-h_{a,b}=\frac{P_{a,b}}{X-\beta}.
 \tag{10}
\]
The reciprocal has exact agreement \(k\), by multiplying any
approximation by \(X-\beta\) and then interpolating. The same argument
gives \(A_{\rm common}(f,g)=k\).

Choose \(c_*\ne0\) with
\[
 c_*^p=\Lambda(\beta)^{p-1}.
 \tag{11}
\]
For any \(\deg h<k\), set
\[
 W=X^D-\beta^D+c_*-(X-\beta)h,\quad
 Z=W^p-\Lambda^{p-1},\quad
 \Omega=W'Z-W\Lambda^{p-2}.
 \tag{12}
\]
The fixed leading term of \(W\) has derivative zero, so
\(\deg W'\le k-1\); (6) gives \(\deg Z\le pk\).
Moreover
\[
 \deg\Omega\le
 \max\{(p+1)k-1,\ D+(p-2)n\}=(p+1)k-1,
 \tag{13}
\]
because the difference between the two displayed bounds is
\((Q-p^2)(Q+1)/p^2\ge0\).
At the pole, \(Z(\beta)=0\), while
\(\Omega(\beta)=-c_*\Lambda(\beta)^{p-2}\ne0\).

Each native agreement root of \(W\) has multiplicity at least \(p\)
in \(\Omega\). Indeed,
\[
 \Omega=W'W^p-\Lambda^{p-2}(W'\Lambda+W).
 \]
At such a root the parenthesis and its derivative vanish, since
\(\Lambda'=-1\) and
\((W'\Lambda+W)'=W''\Lambda\).
The second term therefore has multiplicity at least \(p\), as does
the first. Counting roots of the nonzero \(\Omega\) proves
\[
 A(f+c_*g)\le U.
 \tag{14}
\]
This is the complementary normalization from the existing elliptic
theorem, applied at the exact smaller dimension.

To retain **every** nonzero label, use the affine endpoints
\[
 r_0=f+c_*g,\qquad r_1=c_*g.
 \tag{15}
\]
Their common agreement is \(k\), and \(A(r_1)=k\).
For \(t=1-c_*/\lambda_{a,b}\),
\[
 (1-t)r_0+tr_1
 =\frac{c_*}{\lambda_{a,b}}\,(f+\lambda_{a,b}g).
 \tag{16}
\]
All these parameters are distinct and different from \(1\).
They are also different from \(0\), since (14) and \(U<T\) exclude
\(\lambda_{a,b}=c_*\). Scaling (10) supplies the witnesses, without
discarding one label in the projective-to-affine conversion.

## Exact placement

The finite Johnson slack is
\[
 n(k-1)-T^2=\frac Qp\,T-n>0
 \tag{17}
\]
for odd \(p\ge3\) and \(Q\ge p^2\).
For \(\alpha=T/n\) and \(\rho=k/n\), the high-branch first-order
sign is
\[
 (8-\rho)\alpha^2-6\rho\alpha+\rho(4\rho-5)
 =
 \frac{((p-1)Q-1)
 [3(p-1)Q^2-(4p^2+2p+2)Q-(p-1)]}{p^4Q^3}>0.
 \tag{18}
\]
These rates lie on the high branch. The bracket is increasing for
\(Q\ge p^2\), and at \(Q=p^2\) it equals
\[
 3p^5-7p^4-2p^3-2p^2-p+1>0\quad(p\ge3).
 \]
Thus the tested agreement is strictly above first order and below
finite Johnson. The positivity in (18) is not a large-characteristic
counterexample: the code dimension is much larger than \(p\).

For \(p=3,s=2\), the exact ledger is
\[
 n=81,\ d=30,\ T=51,\ D=54,\ k=34,\ U=45,\ M=648.
 \tag{19}
\]
The Johnson slack is \(72\) and the first-order sign is
\(1496/59049>0\). Thus both-source farness is certified over
\(\mathbb F_{3^8}\), with the evaluation field \(\mathbb F_{3^4}\).
The independent finite checker is
[norm_trace_p3_s2_fixture/verify.py](norm_trace_p3_s2_fixture/verify.py).
Its stable receipt verifies all \(648\) original and transformed affine
labels, degree-\(33\) witnesses, and \(51\) matches per witness.
The source upper bounds are proved by (12)--(14), not by codeword
enumeration.

## Matched comparison and limitations

The prior full-rank elliptic high row has the same full-field domain,
agreement \(T\), and polynomial population \(M=n(Q-1)\), at dimension
\[
 k_{\rm old}=\frac{(p-1)^2n}{p^2}.
 \]
Its proof already displays the sharper correction degree
\((p-1)T/p\); the present choice uses that exact degree as the
strict message dimension. The reduction is
\[
 k_{\rm old}-k=\frac{(p-1)Q}{p^2}.
 \]
The prior general collision argument gives, for \(|E|=n^2\),
\[
 \left\lceil
 \frac{M(n^2-n)}{n^2-n+(p-1)(M-1)}
 \right\rceil-1
 \]
distinct nonzero labels at a suitable pole. Here the complete splitting
of the full-rank trace--Hermitian difference space removes all
collisions at every exterior pole, yielding exactly \(M\) certified
labels. These are finite refinements of the existing mechanism.

For fixed \(p\) and \(s\to\infty\),
\[
 k/n\to(1-1/p)^2,\quad T/n\to1-1/p,\quad
 M=n^{3/2}-n,
\]
and the smaller guaranteed individual loss is asymptotically \(1/p\)
of the capacity margin. The fixed-rate, constant-margin,
superlinear-count regime is already present in the prior theorem.
When the characteristic grows, the fractional capacity margin is
asymptotic to \(1/p\), and the relative individual guarantee also
degrades like \(1/p\).
No prescribed short domain, fixed prime-field extension degree as
\(s\) grows, prime-alphabet result, full list classification, or
practical-security claim follows.
