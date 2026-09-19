# Elliptic AG parity, structured quintics, and the remaining common-head identity

September 19, 2026. Exact algebraic reduction; no field scan or manuscript change.

**Outcome.** Elliptic function spaces give an explicit family of admissible moving quintics, with a rational formula from the group law. They do not yet give a common received pencil. Odd auxiliary terms disappear under paired agreement at the natural Reed–Solomon pole budget. A separate, narrowly scoped fixed affine AG norm-pencil ansatz has an exact three-column common-head test and cannot supply the desired cubic-size bank. The full moving-quintic recurrence remains open.

## 1. Setup and paired parity

Let the nonsingular curve be

\[
\mathcal E:y^2=f_{\rm c}(x)=x^3+A_{\rm c}x+B_{\rm c}
\]

over a prime field of characteristic greater than three. Assume all of \(\mathcal E[\ell]\) is rational, with odd prime \(\ell\ge23\), distinct from the characteristic. Put

\[
D=x(\mathcal E[\ell]\setminus\{O\}),\quad
n=(\ell^2-1)/2,\quad
\Phi=\prod_{x\in D}(X-x),\quad
k=n-4\ell+1,\quad T=n-2\ell-5.
\]

No point above \(D\) has zero y-coordinate. The even words on the two lifts of \(D\) are the words that descend to the x-coordinate Reed–Solomon domain.

Since the pole orders of x and y at O are two and three, respectively,

\[
L(mO)=\left\{A(x)+yB(x):
\deg A\le\lfloor m/2\rfloor,\quad
\deg B\le\lfloor(m-3)/2\rfloor\right\}.
\]

The even and odd leading pole orders have different parity, so they cannot cancel. In particular, a witness in \(L((2k-2)O)\) is \(A+yB\), with \(\deg A<k\) and \(\deg B\le k-3\). If it agrees with an even received word on both lifts of more than \(k-3\) x-coordinates, then subtraction at \(P\) and \(-P\) gives \(2y(P)B(x(P))=0\), hence \(B=0\). Our target satisfies \(T-(k-3)=2\ell-3>0\).

This assertion concerns paired matches. A count of unpaired AG matches cannot silently be substituted for a count of x-coordinate matches.

More generally, if a function \(R\in L(MO)\) vanishes on both lifts of a set with monic x-locator V of degree t, then

\[
R=V(x)W,\qquad W\in L((M-2t)O).
\]

Division has no remaining finite poles, and subtracts exactly \(2t\) from the possible pole order at O. For \(M=2(n-2\ell)\) and \(t=n-2\ell-d\), this becomes

\[
R=V(x)\bigl(A_d(x)+yB_{d-2}(x)\bigr),\qquad
\deg A_d\le d,\quad \deg B_{d-2}\le d-2.
\]

At five extra errors, the even projection is exactly \(VA_5\); the odd cofactor of degree at most three does not enlarge this even cofactor space. This is a pole-budget statement, not an obstruction to arbitrary nonlinear norm constructions or larger pole budgets.

## 2. An explicit split quintic from a signed torsion divisor

Choose five nonzero torsion points with distinct x-coordinates and

\[
P_1+P_2+P_3+P_4+P_5=O.
\]

The divisor \(\sum_i[P_i]-5[O]\) is principal. There is a function
\(u=A_2(x)+yB_1(x)\) with that divisor, where \(\deg A_2\le2\) and \(\deg B_1=1\). The latter degree is exact because the pole order is five.

This is constructive. For a nondegenerate ordering put \(S_2=P_1+P_2\), \(S_3=S_2+P_3\), \(S_4=S_3+P_4=-P_5\). If \(\ell_{P,Q}\) is a chord or tangent line function, then

\[
u=\frac{\ell_{P_1,P_2}\ell_{S_2,P_3}\ell_{S_3,P_4}}
{(x-x(S_2))(x-x(S_3))}
\]

has the required divisor. All finite denominators cancel as functions. Degenerate additions can instead be handled by the usual vertical-line divisor identity; the divisor criterion does not depend on choosing this particular ordering.

Normalize the leading coefficient of \(B_1\) to one, and write

\[
B_1=X+b,\qquad A_2=a_2X^2+a_1X+a_0.
\]

The monic, squarefree x-locator is

\[
\boxed{J(X)=f_{\rm c}(X)(X+b)^2-A_2(X)^2.}
\tag{1}
\]

It divides \(\Phi\). Its coefficients are

\[
\begin{aligned}
j_4&=2b-a_2^2,&
j_3&=b^2+A_{\rm c}-2a_2a_1,\\
j_2&=2bA_{\rm c}+B_{\rm c}-a_1^2-2a_2a_0,&
j_1&=A_{\rm c}b^2+2bB_{\rm c}-2a_1a_0,\\
j_0&=B_{\rm c}b^2-a_0^2.
\end{aligned}
\]

Conversely, if (1) is squarefree and divides \(\Phi\), then \(X+b\) is nonzero at each root: otherwise \(A_2\) also vanishes there and J has a repeated root. Thus each root selects a unique sign through \(y=A_2(x)/(x+b)\). The resulting five points sum to O, because they are the zeros of \(A_2-y(X+b)\in L(5O)\). Therefore (1) describes exactly the subclass of split quintics admitting a balanced signed divisor, rather than every split quintic.

For five distinct nonzero odd-torsion x-coordinates, a balanced choice of signs is unique up to global reversal. Indeed two such choices give a proper nonempty subset summing to O after multiplication by two is inverted. Either this subset or its complement has at most two members; neither a singleton nor a pair with distinct x-coordinates can sum to O. The normalized functions are consequently related by \(A_2\mapsto-A_2\), with the same b.

For two full fiber locators \(L_0\), one still requires \(\gcd(J,L_0)=1\). More importantly, the same global syndrome pencil must satisfy the exact recurrence in [FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md](FIVE_EXTRA_ERRORS_QUINTIC_TARGET.md), equation (3), after substitution of these five coefficients. The construction above solves the native, split-extra condition; it does not solve that recurrence or establish distinct challenge labels.

## 3. A torsion-rich one-parameter specialization

For any nonzero \(P\in\mathcal E[\ell]\), with \(\ell>11\), the signed points

\[
P,\ 2P,\ 6P,\ -4P,\ -5P
\]

sum to O and have five distinct x-coordinates. Hence

\[
\boxed{J_P(X)=\prod_{j\in\{1,2,4,5,6\}}(X-x([j]P))}
\tag{2}
\]

belongs to (1). Multiplication formulas make its coefficients rational functions of one elliptic parameter, of degrees bounded independently of \(\ell\). Formula (2) is therefore an explicit torsion-rich specialization for the common-head equations, without enumerating arbitrary quintics. Counting its distinct polynomials still does not count challenge labels.

## 4. Exact common-head gate for a fixed affine AG norm pencil

The following narrower ansatz has a sharp test. It is not the general family obtained by dividing by \(L_0J_P\).

Take fixed AG functions \(U_0,U_1\), regular away O, and \(U_z=U_0+zU_1\). Suppose \(\Phi\mid\operatorname{Norm}(U_z)\) for at least three distinct field elements z. Since the norm has degree at most two in z, coefficientwise divisibility gives

\[
\operatorname{Norm}(U_z)/\Phi=Q_0+zQ_1+z^2Q_2.
\tag{3}
\]

Use the degree-less-than-n representatives of the Q's modulo \(\Phi\). Let \(\pi\) denote quotient by the degree-less-than-k code. If at least three z-values lie in the same received projective line, then

\[
\boxed{\dim\operatorname{span}(\pi Q_0,\pi Q_1,\pi Q_2)\le2.}
\tag{4}
\]

Indeed, in the quotient by that fixed two-dimensional syndrome space, (3) is a vector polynomial of degree at most two with three roots. Condition (4) accommodates scaling and projective reparametrization; requiring the literal affine head image itself to be a line would impose the stronger dependence of \(\pi Q_1\) and \(\pi Q_2\).

There is a simple bank bound once (4) holds. Let C be the common zero set of the three Q's in D and \(v=|C|\). Outside C, each coordinate is a zero of (3) for at most two parameters. If the span of the Q's contains a nonzero codeword, then \(v\le k-1\). Consequently a collection of B parameters, each with at least T zeros, satisfies

\[
B(T-v)\le2(n-v),\qquad
B\le\left\lfloor\frac{2(n-k+1)}{T-k+1}\right\rfloor
=\left\lfloor\frac{8\ell}{2\ell-5}\right\rfloor=4.
\]

If instead the span contains no nonzero codeword, its image under \(\pi\) is injective and (4) makes the actual polynomial span at most two-dimensional. Distinct projective residuals then have disjoint zero sets outside C. Provided the received line has a point of agreement strictly below T, necessarily \(v<T\), so its distinct qualifying projective labels satisfy

\[
B(T-v)\le n-v,\qquad B\le n-T+1=2\ell+6.
\]

A one-dimensional residual span gives at most one projective label. Thus a fixed affine AG function pencil followed by its norm cannot produce the desired order-\(\ell^3\) bank in this window. This conclusion does not apply to the rational dependence of \(\Phi/(L_0J_P)\), to varying AG spaces or poles, or to a higher-parameter construction satisfying a different common-head identity.

## 5. Remaining constructive requirement

The positive output is the explicit signed-divisor family (1)–(2). A successful compiler must still exhibit one rank-two syndrome pair shared by the subgroup-indexed two-fiber locators and these quintics; remove any zero-error extra factors; count distinct projective labels; and prove the source/common-agreement bounds separately. No such common pencil is asserted here.
