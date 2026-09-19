# Exact partial-fiber system for high-rate KKH outsiders

Date: 2026-09-18. Bounded constructive audit. **No noncanonical split family
has been constructed.** The result is an exact, substantially smaller target
system that includes arbitrary partial-fiber witnesses, together with tests
excluding two natural packet constructions.

## The line and the target

Let \(D=\mu_n\subset\mathbb F_p^*\), \(n=sm\mid p-1\), and
\(G=\mu_s\). Write \(Y=X^m\), choose \(b\in\mathbb F_p\setminus G\),
and consider the translated Appendix A KKH line

\[
 f(X)=\frac{Y^{s-2}-b^{s-2}}{Y-b},\qquad
 g(X)=\frac1{Y-b},\qquad W_\lambda=f+\lambda g.
\]

The code has degree cap \(n-4m\), hence dimension \(k=n-4m+1\).
Both \(f\) and \(g\), and their common agreement, have exact maximum
agreement \(A=n-3m\): for \(f\) use its monic polynomial degree,
for \(g\) clear the denominator, and attain the bounds by interpolation on
any \(s-3\) full fibers. We seek witnesses with at least

\[
 T=n-2m-d,\qquad 0\le d<m.
\]

The usual two-omitted-fiber witnesses have \(n-2m\) agreements. This note
does not assume other witnesses have whole-fiber supports.

For orientation, write any codeword uniquely as
\(Q(X)=\sum_{j=0}^{m-1}X^jQ_j(Y)\). Its degree bounds are
\(\deg Q_0\le s-4\) and \(\deg Q_j\le s-5\) for \(j>0\).
On a particular fiber the nonconstant residues can give arbitrary partial
agreement; they cannot simply be discarded. The locator derivation below
retains all of them.

## Exact equivalence with a three-block split divisor

Suppose \(Q\) agrees with \(W_\lambda\) on a chosen \(T\)-point subset
\(S\subset D\). Let \(U=D\setminus S\), so \(|U|=2m+d\), and let
\(L_U=\prod_{x\in U}(X-x)\). Clear the denominator:

\[
 F(X)=X^{n-2m}-b^{s-2}+\lambda-(Y-b)Q(X).
\]

This is monic of degree \(n-2m\), with all coefficients in degrees
\(n-3m+1,\ldots,n-2m-1\) equal to zero. Therefore

\[
 F=L_S C=\frac{X^n-1}{L_U}C
\]

for a monic polynomial \(C\) of degree \(d\). Comparing the high-degree
band after multiplying by \(L_U\) gives

\[
 L_U=X^{2m}C+A_0,\qquad \deg A_0\le m+d.
\]

The label \(\lambda\) is nonzero: when \(\lambda=0\), the word is
\(f\), whose exact agreement is \(n-3m<T\). Reducing
\(FL_U=(X^n-1)C\) modulo \(Y-b\) gives
\(\lambda L_U\equiv(b^s-1)C\). Put

\[
 \kappa=(b^s-1)/\lambda\ne0.
\]

Since \(\deg C=d<m\), there is a polynomial \(B\), \(\deg B\le d\),
such that

\[
 \boxed{\quad
 L_U(X)=(Y^2-b^2+\kappa)C(X)+(Y-b)B(X),\qquad L_U\mid X^n-1.
 \quad}                                                   \tag{1}
\]

Conversely, take any monic degree-\(d\) polynomial \(C\), polynomial
\(B\) of degree at most \(d\), and nonzero \(\kappa\) satisfying (1).
The divisibility makes \(L_U\) a squarefree locator of \(2m+d\) points
of \(D\). Also \(\gcd(C,Y-b)=1\): otherwise (1) would give a common
root of \(L_U\) and \(Y-b\), impossible because \(b\notin G\).
Set

\[
 \lambda=(b^s-1)/\kappa,\qquad
 F=(X^n-1)C/L_U,\qquad
 Q=\frac{X^{n-2m}-b^{s-2}+\lambda-F}{Y-b}.
\]

The remainder condition makes \(Q\) a polynomial. The high-band identity
makes \(\deg Q\le n-4m\). It agrees with \(W_\lambda\) on at least
\(n-2m-d\) coordinates. Thus (1) is an equivalence, not merely a necessary
moment condition.

For fixed \(d\), this is a system with \(2d+2\) field parameters:
\(d\) lower coefficients of monic \(C\), \(d+1\) coefficients of \(B\),
and \(\kappa\). Divisibility by \(X^n-1\) is the exact remaining test.
The field parameters do **not** grow with \(m\) when \(m/s\) and the
integer deficit \(d\) are fixed. Support choices still grow, but they are
not free once the divisor equation is imposed.

## Remove artificial padding before counting outsiders

Let \(H=\gcd(C,B)\), made monic, and write \(h=\deg H\),
\(C=HC_0\), \(B=HB_0\). Then \(H\mid L_U\mid X^n-1\), so
\(H\) is itself a squarefree domain locator. Dividing (1) by \(H\) gives

\[
 L_0=(Y^2-b^2+\kappa)C_0+(Y-b)B_0,\qquad
 \gcd(C_0,B_0)=1,\quad \deg C_0=e=d-h.
\]

Now \(\gcd(C_0,L_0)=1\), since \(\gcd(C_0,Y-b)=1\). The cleared
residual is \(F=(X^n-1)C_0/L_0\), and its domain zero set is **exactly**
\(D\setminus Z(L_0)\). Hence the exact agreement is

\[
 n-2m-e.
\]

If \(e=0\), then \(C_0=1\), \(B_0\) is constant, and \(L_0\) is a
quadratic in \(Y\). Its split roots are exactly two full fibers: this is a
canonical label, regardless of the padding \(H\). For a genuine outsider
we must therefore have \(e\ge1\) and a nonconstant rational function
\(R=B_0/C_0\).

On a fiber \(Y=a\in G\), the primitive locator specializes to the
nonzero polynomial

\[
 (a^2-b^2+\kappa)C_0(X)+(a-b)B_0(X)
\]

of degree at most \(e\). It cannot vanish identically, because that would
make \(B_0/C_0\) constant. Thus the omitted set has at most \(e\) points
per fiber, which forces

\[
 2m+e\le se,\qquad e\ge\left\lceil\frac{2m}{s-1}\right\rceil.       \tag{2}
\]

This bound allows spread-out partial fibers. It is not the previously closed
whole-packet model.

## Concrete asymptotic gate: \(m=2s\), \(d=5\)

Let \(s\ge16\) be a power of two, \(m=2s\), \(n=2s^2\), and
\(T=2s^2-4s-5\). For \(\rho=k/n\), \(a=T/n\), the high-branch curve
polynomial satisfies the exact identity

\[
 F_{\rm curve}(a,\rho)=
 \frac{48s^4-16s^3+742s^2+160s-25}{8s^6}>0.
\]

Since \(\rho\ge3/4\), this means \(T>n a_1(k/n)\). Also

\[
 T^2-n(k-1)=-4s^2+40s+25<0.
\]

Thus this integer threshold is strictly above first order and below exact
Johnson. Its loss-to-capacity-margin ratio is
\((2s-5)/(4s-6)\to1/2\). The source agreement \(A=n-3m\) is not claimed
to lie above first order.

Here (2) forces every genuine outsider to have \(e=5\). The exact target is
therefore a coprime pair \(C,B\), with \(C\) monic quintic and
\(\deg B\le5\), and \(\kappa\ne0\), for which

\[
 (X^{4s}-b^2+\kappa)C(X)+(X^{2s}-b)B(X)
\]

divides \(X^{2s^2}-1\). It must have \(4s+5\) distinct roots in the
domain, at most five in each old fiber. A superlinear label family would need
more than \(\Theta(s^2)\) distinct values of \(\kappa\), not merely many
factorizations with the same \(\kappa\).

The first illustrative integer instance is
\((s,m,n,k,A,T)=(16,32,512,385,416,443)\). The curve polynomial is
\(3272679/134217728>0\), and the squared Johnson slack is \(359\).
This is a parameter certificate, not an outsider existence certificate.

## Two concrete constructor checks

**Binary packet support trees.** Let \(U\) be a primitive quintic omitted
set. For \(\zeta\in\mu_m\),

\[
 L_U(\zeta X)C(X)-L_U(X)C(\zeta X)
 =(Y-b)\,[B(\zeta X)C(X)-B(X)C(\zeta X)].                 \tag{3}
\]

The bracket has degree at most nine and has zero constant term. If it is
nonzero, it has at most eight nonzero roots. It cannot vanish identically for
\(\zeta\ne1\): that would make the degree-five rational map \(B/C\)
invariant under a nontrivial group of power-of-two order, so it would factor
through \(X\mapsto X^h\), forcing \(h\mid5\).
Consequently

\[
 |U\cap\zeta U|\le8\qquad(\zeta\in\mu_m\setminus\{1\}).          \tag{4}
\]

In particular, \(U\) contains at most four opposite pairs. A binary support
tree built from multiplicative subgroup packets must therefore leave at
least \(4s-3\) of the \(4s+5\) roots as singleton leaves; packets of size
at least two can account for at most eight roots. This rules out assembling
the desired locator from many full small packets. It does not exclude an
irregular, almost unpaired support.

For comparison, summing (4) gives
\(\sum_{a\in G}|U_a|(|U_a|-1)\le8(m-1)\). The smallest possible left
side at \(|U|=4s+5\), \(|U_a|\le5\), is \(12s+40\), attained by five
fibers of size five and all others of size four. For \(s\ge16\) this is
compatible with the upper bound \(16s-8\); the test is therefore genuinely
inconclusive for arbitrary supports.

**One q-Pochhammer block.** Suppose the roots form one geometric progression
\(u,uq,\ldots,uq^{\ell-1}\) of distinct elements, with \(\ell=4s+5\)
and \(q\) of power-of-two order \(h\). Then \(\ell<h\), since \(\ell\)
is odd and greater than one. In
\(\prod_{j=0}^{\ell-1}(X-uq^j)\), every coefficient is nonzero: its
Gaussian-binomial product formula has only factors \(1-q^a\) with
\(1\le a\le\ell<h\) in both numerator and denominator. This contradicts
the long zero coefficient gaps in (1). Thus a single such progression cannot
produce the primitive outsider. Products of multiple progressions with
characteristic-specific coefficient cancellations remain outside this check.

A further simple attempt, \(B/C\) a nonconstant Möbius transform of
\(X^5\), also fails: \(X\mapsto X^5\) permutes \(D\), so the rational
function is injective wherever defined on \(D\). Equation (1) would then
have at most one omitted point per old fiber, far fewer than \(4s+5\).

## Reproducible gate and remaining work

`verify_outsider_system.py` checks the symbolic band and rotation identities,
the finite curve placement, and an exact \(p=65537\), \(n=512\) algebra
fixture. The fixture deliberately pads a canonical locator by five domain
roots. It reconstructs the degree-384 witness, checks all 512 coordinates,
finds 448 agreements, and detects the degree-five gcd. This guards against
mistaking padding for an outsider. It also checks a single progression's
nonzero coefficients. The receipt is `outsider_system_receipt.json`.

The next genuine construction gate is to produce coprime quintics satisfying
the displayed divisor identity for growing \(s\), then count distinct
\(\kappa\). No such family, productive search method, or justified rental
has been obtained here. The exact system preserves all partial-fiber
possibilities and avoids claiming a general impossibility.
