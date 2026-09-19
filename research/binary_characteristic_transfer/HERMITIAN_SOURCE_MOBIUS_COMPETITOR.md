# A competing witness for the explicit zero endpoint

This addresses the individual-source gap in odd_hermitian_high_rate.tex.
The small-cofactor bound is not merely an artifact of ignoring the pole:
a Möbius transform of a split multiplicative subgroup produces a
competing witness at the zero endpoint, for **every** exterior pole.
It sometimes attains the proved square-root bound exactly.

The construction below concerns the source

\[
 f_\beta=\frac{X^D-\beta^D}{X-\beta},
 \qquad D=p^2-p,\qquad K=p^2-2p,
 \qquad B=\mathbb F_{p^2}\subset E=\mathbb F_{p^4}.
\]

It leaves the Hermitian exceptional bank unchanged. In particular, it
does not dispute its exact singleton profile at \(T=D-2\).

## Exact competitor lemma

Let \(p\) be an odd prime. Suppose an even integer \(e\) satisfies

\[
 2\le e<p,\qquad m=p+e\mid p^2-1,\qquad
 L=\frac{p^2-1}{m}>e.
 \tag{1}
\]

For every \(\beta\in E\setminus B\), there is a polynomial \(h\) of
degree less than \(K\) agreeing with \(f_\beta\) at exactly \(D-e\)
coordinates of the full native domain \(B\). Consequently

\[
 \operatorname{agr}_K(f_\beta)\ge D-e,
 \qquad
 T-\operatorname{agr}_K(f_\beta)\le e-2.
 \tag{2}
\]

### Choose an exterior point and a native Möbius pole

Take a nonzero \(w\in E\) with \(w^{p^2}=-w\), and a generator
\(\zeta\) of \(B^*\). Since \(e\) is even, both \(w^e\) and
\((w\zeta)^e\) belong to \(B\). For \(t=w\) or \(w\zeta\), put

\[
 a=t^{-ep}\in B.
\]

At least one of these two choices satisfies \(a^m\ne1\). Indeed, if
the first has \(a^m=1\), the second changes it by
\(\zeta^{-epm}\), which is not one: otherwise \(L\mid ep\), hence
\(L\mid e\), contradicting \(L>e\) and \(p\nmid L\).
Fix the successful choice. It satisfies

\[
 a^p t^e=1,\qquad a\notin\mu_m.
 \tag{3}
\]

Put \(u=(t-a)^{-1}\), and write the conjugation over \(B\) as a bar.
For the prescribed exterior \(\beta\), set

\[
 \gamma=\frac{\beta-\bar\beta}{u-\bar u}\in B^*,
 \qquad b=\beta-\gamma u\in B.
\]

Then the \(B\)-Möbius map

\[
 M(X)=b+\frac{\gamma}{X-a}
\]

sends \(t\) to \(\beta\). Its pole \(a\) is outside \(\mu_m\), so it
sends the \(m\) distinct native points of \(\mu_m\) to \(m\) distinct
finite native points.

### Transformed split locator and its cofactor

In the new variable \(Y\), write

\[
 q(Y)=Y-b,\qquad U(Y)=a q(Y)+\gamma,\qquad
 \Delta=a^m-1\ne0.
\]

The monic locator of \(M(\mu_m)\) is

\[
 G(Y)=\frac{U(Y)^{p+e}-q(Y)^{p+e}}{\Delta}.
\]

Frobenius expansion gives the exact short-block decomposition

\[
 G=Y^p F+A,
 \tag{4}
\]

where

\[
 F=\frac{a^p U^e-q^e}{\Delta},
 \qquad
 A=\frac{(\gamma^p-a^pb^p)U^e+b^pq^e}{\Delta}.
\]

Both \(G\) and \(F\) are monic, of degrees \(p+e\) and \(e\), and
\(\deg A\le e\). Since \(U(\beta)=tq(\beta)\), (3) yields
\(F(\beta)=0\).

Moreover \(\gcd(F,A)=1\). The two coefficient rows expressing \(F,A\)
in \(U^e,q^e\), before the common nonzero scaling, have determinant
\(\gamma^p\ne0\); and \(\gcd(U,q)=1\). Thus \(\gcd(F,G)=1\).
The locator \(G\) is squarefree and divides
\(\Lambda=Y^{p^2}-Y\).

Set

\[
 P=F\frac{\Lambda}{G}.
\]

This is monic of degree \(D\), and it has exactly \(p^2-(p+e)=D-e\)
distinct native roots. Any native roots of \(F\) are already in the
complement of \(G\), so they add no new coordinates. In particular
\(P(\beta)=0\).

Equation (4) gives

\[
 (P-Y^D)G=-YF-Y^D A,
\]

whose degree bound proves \(\deg(P-Y^D)\le D-p=K\). Therefore

\[
 h(Y)=\frac{Y^D-\beta^D-P(Y)}{Y-\beta}
\]

is a polynomial of degree at most \(K-1\), and

\[
 f_\beta-h=\frac{P}{Y-\beta}.
\]

Its exact native agreement is \(D-e\), proving (2).

## Exact saturation at a prime-quadratic parameter choice

If \(e\ge4\) is even and

\[
 p=e^2-e-1
\]

is prime, then \(m=e^2-1\), \(L=e(e-2)>e\), and all conditions (1)
hold. Also

\[
 r_p=\min\{j\ge2:j^2-j+1\ge p\}=e.
\]

Combining (2) with the proved upper bound in the Hermitian theorem gives

\[
 \operatorname{agr}_K(f_\beta)=D-r_p
 \qquad\text{for every }\beta\in E\setminus B.
 \tag{5}
\]

The finite prime examples \((p,e)=(11,4),(29,6),(89,10),(131,12)\)
therefore attain the source bound exactly. No assertion is made that
this quadratic polynomial is prime infinitely often.

The separate bounded verifier
verify_hermitian_source_competitor.py checks \(p=11,e=4\) by explicit
quadratic-tower arithmetic, all native coordinates, exact polynomial
identities, and the strict witness degree. It does not enumerate
codewords or search over parameters.

## An unconditional growing family defeats a uniform linear source gap

The absence of a uniform positive fractional source gap does not require
infinitely many primes of a quadratic polynomial. Fix any odd
integer \(r\ge3\), let \(j\) be a positive odd integer, and put

\[
 e=1+rj,\qquad
 p=(r-1)e+r=r(r-1)j+2r-1.
 \tag{6}
\]

For \(j=2h+1\), these primes lie in the progression

\[
 p=2r(r-1)h+(r^2+r-1).
\]

The residue is coprime to \(2r(r-1)\): it is odd, \(-1\) modulo \(r\),
and \(1\) modulo \(r-1\). Dirichlet's theorem supplies infinitely many
prime values for each fixed \(r\).

Here \(e\) is even, \(m=p+e=r(e+1)\), and

\[
 p-1=(r-1)(e+1),\qquad r\mid p+1,
 \qquad L=\frac{(r-1)(p+1)}r>e.
\]

Thus the competitor lemma applies for every exterior pole, and

\[
 \limsup_{\substack{p\to\infty\\\text{in this progression}}}
 \frac{T-\operatorname{agr}_K(f_\beta)}{T-K}
 \le \frac1{r-1}.
\]

Since \(r\) is arbitrary, no absolute positive constant can lower-bound
this ratio uniformly over all primes in the stated Hermitian family.
Choosing a prime from each progression with \(r\to\infty\) gives an
unconditional sequence with \(e/p\to0\).

This rules out the proposed uniform \(e=\Omega(p)\) strengthening for
the explicit zero endpoint. It does not rule out stronger bounds on
selected prime subsequences, a different choice of two endpoints, or
a separate improvement for the explicit endpoint \(c_*\).

## The second explicit endpoint imposes a different condition

For completeness, let \(Q=-A/F\) be the rational map of an arbitrary
small-cofactor witness. The pole condition for \(z=0\) is \(F(\beta)=0\).
For \(z=c_*\), where \(c_*^p=\Lambda(\beta)^{p-1}\), it instead gives

\[
 Q(\beta)=\beta^{p^3}.
\]

Indeed \(P(\beta)=c_*\) implies
\(G(\beta)^p=\Lambda(\beta)F(\beta)^p\), and (4) then gives
\(A(\beta)^p=-\beta F(\beta)^p\).
Here \(F(\beta)\ne0\). The present construction deliberately enforces
the first, pole condition; it does not silently establish this second
condition. The zero endpoint alone already suffices for the stated
failure of a uniform lower bound on the smaller individual loss.

There is also an exact prediction for the prime-quadratic examples.
For the entire \(B\)-Möbius orbit of \(Q_0(X)=1/X^e\), the transformed
map is \(Q_M=M^\sigma\circ Q_0\circ M^{-1}\). At
\(\beta=M(t)\), the \(c_*\) condition is equivalent to

\[
 t^{p^3+e}=1.
\]

When \(e\) is even and \(p=e^2-e-1\), one has

\[
 \gcd(p^3+e,p^4-1)=p+e.
\]

Indeed the gcd with \(p^2-1\) is \(p+e\), while the gcd with
\(p^2+1\) is
\(\gcd(p-e,e^2+1)=1\): it is odd, divides \(e+1\), and divides two.
Thus every such \(t\) is native, contradicting that
\(\beta\notin B\) and \(M\) is defined over \(B\).
The \(c_*\) label is therefore absent from this entire orbit, including
the \(p=11,e=4\) case. This does not give a distance bound against other
rational maps or other codeword competitors.
