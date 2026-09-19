# Odd-dimensional Gold forms: exact lists at every cubic exterior pole

September 19, 2026. Algebraic specialization; no field or codeword scan.

**Prior scope.** The odd-dimensional Gold mechanism already appears in the binary project's read-only source, sections/constructions/fullfield-elliptic.tex, proof of cor:elliptic-fixed-codimension. That proof includes odd-characteristic nondegeneracy, large-level selection, translations, and the high-rate compiler. The quadratic population and fixed-characteristic asymptotic regime are inherited. The refinements here are the smaller exact message dimension, injection at every cubic exterior pole, and an exhaustive threshold-list classification.

## 1. Parameters

Let p be odd and \(s\ge2\). Put
\[
m=2s+1,\quad r=p^s,\quad n=p^{2s+1}=pr^2,\quad
B=\mathbb F_n,\quad E=\mathbb F_{n^3},\quad \Lambda=X^n-X,
\]
\[
d=n/p+r,\quad T=n-d,\quad D=n-n/p,\quad
k=(p-1)T/p,\quad U=\left\lfloor\frac{(p+1)k-1}{p}\right\rfloor,\quad
M=n(n-1)/2.
\]
For every \(\beta\in E\setminus B\), the construction below has exactly M exceptional affine parameters at agreement T. They are interior, each has a singleton threshold list and maximum agreement T, and every other parameter has agreement at most \(T-1\). Its endpoints satisfy
\[
A(r_0)\le U<T,\qquad A(r_1)=\operatorname{CA}(r_0,r_1)=k.
\]
The alphabet is E, of degree \(3(2s+1)\) over the prime field. It is not a prime alphabet.

## 2. Reduced Gold trace and its split half

Let \(\Psi_a\) be the unique degree-less-than-n representative of
\[
x\longmapsto\operatorname{Tr}_{B/\mathbb F_p}(a x^{r+1}).
\]
Its terms have coefficients \(a^{p^i}\) and exponent \(p^i+p^{(i+s)\bmod m}\), \(0\le i<m\). Their largest exponent is \(d=p^{2s}+p^s\), with coefficient \(a^{p^s}\). The derivative is
\[
\Psi_a'=aX^{p^s}+a^{p^{s+1}}X^{p^{s+1}}.
\tag{1}
\]
Under the nondegenerate trace pairing this is also the polar operator on B.

For \(a\ne0\), its coefficientwise \(p^s\)-root is
\[
L_a(X)=a^{p^{s+1}}X+a^pX^p.
\]
Every nonzero homogeneous root satisfies
\[
\eta^{p-1}=-a^{p^{s+1}-p},\qquad \eta^{n-1}=-1.
\tag{2}
\]
For the second equality, raise the first to \((n-1)/(p-1)\); m is odd, and \(p-1\) divides \(p^{s+1}-p\). Thus \(L_a\) permutes B, so the polar form is nondegenerate.

The good half of coefficients is explicit. Since \(\gcd(p^s+1,n-1)=2\), the power maps \(x^{p^s+1}\) and \(x^2\) have the same value multiset on B. The odd-dimensional trace quadratic form has square discriminant: its Gram determinant is the square of the conjugate Vandermonde determinant, whose Frobenius row permutation has sign \(+1\). Multiplication by a changes its determinant by \(\operatorname{Norm}_{B/\mathbb F_p}(a)\). The usual diagonal quadratic-form count consequently gives
\[
\#\{x:\Psi_a(x)=t\}=n/p+\chi_B(a)\chi_p((-1)^s t)\,r
\quad(t\ne0),
\]
and the zero level has \(n/p\) points. Therefore exactly
\[
\mathcal A=\{a\in B^*:\chi_B(a)=\chi_p((-1)^{s+1})\},
\qquad |\mathcal A|=(n-1)/2,
\tag{3}
\]
give d roots at level \(-1\).

For \(a\in\mathcal A,b\in B\), define
\[
G_{a,b}=\Psi_a(X+b)+1,\qquad
F_{a,b}=(G_{a,b}')^{1/p},\qquad
P_{a,b}=F_{a,b}\Lambda/G_{a,b}.
\]
The polynomial G has d distinct native roots. Its only native critical point is its center \(-b\), where its value is one. Both G and F have leading coefficient \(a^{p^s}\), and \(\deg F=r\); hence P is monic of degree D with exactly T native roots. F also has nonnative roots in the quadratic extension of B; they are not extra native agreements.

## 3. Differential identity and exact correction degree

Every polynomial G of degree at most d taking B into \(\mathbb F_p\) satisfies
\[
G^p-G=\Lambda G'.
\tag{4}
\]
The left side is divisible by \(\Lambda\). Its quotient has degree at most \(pd-n=pr<n\); differentiation at the n native points identifies it with \(G'\), also of degree less than n.

Thus the displayed family satisfies
\[
P^p=\Lambda^{p-1}-(\Lambda/G)^{p-1}.
\tag{5}
\]
Since
\[
pk-[(p-2)n+1]=r^2-(p-1)r-1>0,
\]
the leading cancellation in (5) gives
\[
P=X^D+C,\qquad \deg C=k.
\tag{6}
\]

## 4. Quadratic splitting and every-cubic-pole injection

The full difference space is
\[
\mathcal H=\{\Psi_a+\operatorname{Tr}_{B/\mathbb F_p}(\ell X)+c:
a,\ell\in B,\ c\in\mathbb F_p\}.
\]
Every nonzero polynomial in this space splits over \(B_2=\mathbb F_{n^2}\).

To prove this, first take \(a\ne0\). The derivative is the \(p^s\)-th power of an affine polynomial \(L_a(X)+c_0\), where \(c_0\in B\). It has one native root \(x_0\), and all its algebraic roots are \(x_0+\eta\mathbb F_p\). By (2), \(\eta^n=-\eta\), hence \(\eta\in B_2\). At a root outside B, equation (4) forces the derivative to vanish, so that root lies in \(B_2\). If \(a=0\), a nonconstant linear trace polynomial has nonzero constant derivative, and (4) forces all roots into B. A nonzero constant has none.

Because \(B_2\cap E=B\), evaluation at every \(\beta\in E\setminus B\) is injective on \(\mathcal H\). If two P-values agree there, (5) gives \(G_1(\beta)=uG_2(\beta)\) for some \(u\in\mathbb F_p^*\), hence \(G_1=uG_2\) as polynomials. Their quadratic coefficients give \(a_1=ua_2\); invertibility of the polar operator gives the same center; the normalized center value one gives \(u=1\). Thus all M labels \(P_{a,b}(\beta)\) are distinct.

They are also nonzero: F has all roots in \(B_2\), and \(\Lambda/G\) has all roots in B. The conclusion holds in every odd-degree extension of B greater than one, not merely at an averaged choice of pole.

## 5. Complete threshold classification

For any containing field, let \(W=X^D+C\), with \(\deg C\le k\), and put \(\Delta=W^p-\Lambda^{p-1}\). It is nonzero because \(\Delta'=-\Lambda^{p-2}\ne0\), and has degree at most \((p-1)T\).

Let V be the monic locator of all A distinct native roots of W, set \(L=\Lambda/V\), and write \(H=W/V\). Then
\[
\Delta=V^{p-1}(H^pV-L^{p-1}),
\]
so \(A\le T\). At equality the bracket is a nonzero constant c. Choosing a root v of V and setting \(\alpha=L(v)\in B^*\) gives
\[
c=-\alpha^{p-1},\qquad
L^p+cL=\Lambda H^p,\qquad
G=L/\alpha,\qquad G^p-G=\Lambda(H/\alpha)^p.
\tag{7}
\]
In particular \(H\in B[X]\) by uniqueness of pth roots. G is a squarefree degree-d polynomial with d native roots, taking B into \(\mathbb F_p\).

Every such low-degree \(\mathbb F_p\)-valued polynomial belongs to \(\mathcal H\). Indeed its exponent support is a union of multiplication-by-p orbits modulo \(n-1\), cyclically rotating \(2s+1\) base-p digits. Every digit is zero or one, or a rotation exceeds d. Each circular gap between consecutive ones is at least s. Since \(s\ge2\), there are at most two ones; with two, the gaps are s and \(s+1\). Thus the only nonconstant orbits are the linear-trace orbit and the single Gold orbit, with coefficient Frobenius relations precisely as above.

Exact degree gives a nonzero quadratic coefficient. Its invertible polar operator allows completion of the square:
\[
G=\Psi_a(X+b)+c_1,\qquad c_1\in\mathbb F_p.
\]
The center and squarefreeness exclude \(c_1=0\). Normalize \(G_0=G/c_1\). Since it has d native roots, \(a/c_1\in\mathcal A\). Differentiating (7) gives \(F_0=H/(\alpha c_1)\), so
\[
W=HV=F_0\Lambda/G_0.
\]
Equality therefore recovers exactly a displayed bank member, including descent of initially extension-valued coefficients.

For \(f=(X^D-\beta^D)/(X-\beta)\), \(g=1/(X-\beta)\), any strict-degree-less-than-k witness h to \(f+\lambda g\) gives
\[
W=X^D-\beta^D+\lambda-(X-\beta)h,\qquad W(\beta)=\lambda.
\]
The classification and pole injection prove the exact exceptional set and singleton lists. The displayed witness is
\[
h_{a,b}=\frac{X^D-P_{a,b}+P_{a,b}(\beta)-\beta^D}{X-\beta}.
\]

## 6. Sources, placement, and finite ledger

The reciprocal has exact agreement k and ordinary common agreement k. Choose \(c_*^p=\Lambda(\beta)^{p-1}\). For a residual numerator W of \(f+c_*g-h\), the inherited auxiliary polynomial
\[
\Omega=W'(W^p-\Lambda^{p-1})-W\Lambda^{p-2}
\]
is nonzero at \(\beta\), and every native agreement contributes multiplicity at least p. The degree dominance needed for the bound \(A(f+c_*g)\le U\) is
\[
(p+1)k-1-[D+(p-2)n]
=\frac{r(r-p^2+1)}p-1>0 \qquad(r\ge p^2).
\]
Thus \(r_0=f+c_*g,r_1=c_*g\) retain every exception through \(t=1-c_*/\lambda\). These are interior; at \(t=1\) the agreement is k. Moreover
\[
T-U=\left\lceil T/p^2+1/p\right\rceil,\quad
T-k=T/p,\quad n(k-1)-T^2=rT-n>0.
\]
For \(\alpha=T/n,\rho=k/n\), the high-branch first-order sign is
\[
(8-\rho)\alpha^2-6\rho\alpha+\rho(4\rho-5)
=\frac{((p-1)r-1)
[3(p-1)r^2-(4p^2+2p+2)r-(p-1)]}{p^4r^3}>0.
\]
This is the already verified expression with \(r\ge p^2\). The restriction \(s\ge2\) matters: \(s=1\) falls below first order and does not give this source-margin argument.

For \(p=3,s=2\):
\[
n=243,\quad d=90,\quad D=162,\quad
k=102,\quad T=153,\quad U=135,\quad M=29403,
\]
with alphabet \(\mathbb F_{3^{15}}\). The Johnson slack is 1134 and first-order sign \(1496/59049\). These are proved algebraic parameters, not a finite implementation receipt.

For fixed p, the rate tends to \((1-1/p)^2\), the agreement to \(1-1/p\), and the exact population is quadratic. The inherited old dimension is \(k_{\rm old}=(p-1)^2n/p^2\); the exact reduction is \((p-1)p^{s-1}\). As p grows the fractional capacity margin is of order \(1/p\), as is the guaranteed individual-loss fraction. No practical domain, prime-alphabet result, or new fixed-characteristic asymptotic regime is claimed.

