# Complete threshold profile of the Hermitian norm line

This is a further consequence of the cofactor argument in
HERMITIAN_NORM_INJECTIVE_LABELS.md. It strengthens that note's conservative
statement about exhibited witnesses. It does not change the dimension,
alphabet, or below-first-order placement.

Let \(p\ge5\), \(B=\mathbb F_{p^2}\subset E=\mathbb F_{p^4}\),
\(\beta\in E\setminus B\), and set

\[
 n=p^2,\qquad D=p^2-p,\qquad K=D-p,\qquad
 r_p=\min\{e\ge2:e^2-e+1\ge p\}.
\]

Use strict-degree-\(<K\) RS on \(B\), with

\[
 f=\frac{X^D-\beta^D}{X-\beta},\qquad g=\frac1{X-\beta}.
\]

Let

\[
 \mathcal Z=\left\{
 P_{s,c}(\beta):
 s\in B,\ c\in\mathbb F_p,\ c-s^{p+1}\ne0
 \right\},
 \qquad
 P_{s,c}=(X+s)\frac{X^{p^2}-X}
 {X^{p+1}+sX^p+s^pX+c}.
\]

The preceding note proves that these are \(p^2(p-1)\) distinct nonzero
labels, and gives a strict-degree witness for each.

**Exact threshold classification.** At every integer agreement threshold

\[
 D-r_p < \tau \le D-1,
\]

the list of \(f+\lambda g\) is a singleton if \(\lambda\in\mathcal Z\),
and is empty otherwise. The unique listed witness at a bank label agrees
on exactly \(D-1\) coordinates. In particular

\[
 \operatorname{agr}_K(f+\lambda g)=D-1
 \quad(\lambda\in\mathcal Z),
 \qquad
 \operatorname{agr}_K(f+\lambda g)\le D-r_p
 \quad(\lambda\notin\mathcal Z).
 \tag{1}
\]

The latter is an upper bound, not an asserted exact nearest distance.
For \(p\ge5\), \(r_p\ge3\), so the below-Johnson threshold
\(\tau=T=D-2\) is included. Thus the same bank is the **entire**
threshold-\(T\) exceptional-label set, with singleton lists.

## Proof

Fix any \(\lambda\in E\) and code polynomial \(h\), and form the monic
cleared residual

\[
 P=(X-\beta)(f+\lambda g-h)
   =X^D+C,\qquad \deg C\le D-p,\qquad P(\beta)=\lambda.
 \tag{2}
\]

Its native roots are precisely the agreement coordinates. Let \(V\) be
the monic locator of **all** these roots, whose number we write as \(D-e\).
Since \(P\) has degree \(D\), \(e\ge0\). We need only classify
\(e<r_p\); note that \(r_p\le p-1\) for \(p\ge5\).

Set

\[
 F=P/V,\qquad G=(X^{p^2}-X)/V.
\]

Here \(F\) is monic of degree \(e\), while \(G\) is squarefree of degree
\(p+e\), split over \(B\). Comparing the highest \(e\) coefficients in
(2) shows \(F\in B[X]\), since \(e<p\), the first \(p-1\) coefficients
below the leading one of \(P\) vanish, and \(V\in B[X]\).
For \(e=0\), this simply says \(F=1\).

The identity \(PG=(X^{p^2}-X)F\) gives

\[
 G=X^pF+A,\qquad \deg A\le e.
 \tag{3}
\]

Moreover \(\gcd(F,G)=1\): the roots of \(G\) are exactly the native
coordinates not included in \(V\), where \(P\) is nonzero.
Consequently \(\gcd(F,A)=1\).

If \(e=0\), (3) says \(G=X^p+a\). This cannot be a squarefree polynomial
of degree \(p>1\). Thus agreement \(D\) is impossible for every label.

If \(2\le e<r_p\), the degree-\(e\) rational map \(Q=-A/F\) satisfies

\[
 x^p=Q(x),\qquad x=Q^\sigma(Q(x))
\]

at all \(p+e\) native roots of \(G\). Its coefficient-conjugate
composition has degree \(e^2>1\), so its fixed-point numerator is
nonzero of degree at most \(e^2+1\). This yields
\(p+e\le e^2+1\), contrary to \(e<r_p\).

It remains to classify \(e=1\). Write \(F=X+s\), with \(s\in B\).
Equation (3) becomes

\[
 G=X^{p+1}+sX^p+aX+c,\qquad a,c\in B.
 \tag{4}
\]

This polynomial has \(p+1\) distinct roots in \(B\). On \(B\), its
\(p\)-th power is represented modulo \(X^{p^2}-X\) by

\[
 X^{p+1}+a^pX^p+s^pX+c^p.
\]

Subtracting (4) gives a degree-at-most-\(p\) polynomial vanishing at
\(p+1\) points. It is zero, so

\[
 a=s^p,\qquad c^p=c.
\]

Hence \(G=G_{s,c}\) is Hermitian. Its squarefreeness implies
\(c-s^{p+1}\ne0\). It follows that

\[
 P=(X+s)\frac{X^{p^2}-X}{G_{s,c}}=P_{s,c},
 \qquad \lambda=P_{s,c}(\beta)\in\mathcal Z.
\]

The proved injectivity of \(P_{s,c}(\beta)\) identifies \((s,c)\)
uniquely from \(\lambda\). Equation (2) then identifies \(h\) uniquely.
Conversely every member of \(\mathcal Z\) has the already-constructed
witness with \(D-1\) agreements. This proves the classification and (1).

In particular zero is outside \(\mathcal Z\), recovering the all-witness
source bound \(\operatorname{agr}_K(f)\le D-r_p\). The reciprocal and
common agreements remain exactly \(K\).

## Two far affine endpoints without losing any bank label

Choose \(c_*\in E^*\setminus\mathcal Z\), which exists since
\(p^4>p^2(p-1)+1\). Use endpoint words

\[
 r_0=f,\qquad r_1=f+c_*g.
\]

Their affine combination is

\[
 (1-t)r_0+tr_1=f+c_*t\,g.
\]

Both endpoints have individual agreement at most \(D-r_p<T\).
Their ordinary common agreement is exactly \(K\), since simultaneous
agreement of \(r_0,r_1\) with codewords is equivalent, by an invertible
linear change, to simultaneous agreement of \(f,g\). The exceptional
interior affine parameters are exactly
\(\{z/c_*:z\in\mathcal Z\}\), all distinct and different from zero and
one. Thus there are exactly \(p^2(p-1)\) exceptional interior parameters,
with singleton threshold-\(T\) lists. Neither endpoint's individual
agreement is asserted to be exactly \(K\).

## What this adds, and what it does not

The general rational-map exclusion applies to every label, not just to
the normalized source at zero. The only low-degree cofactor that
survives is the linear one, and its complementary locator is forced
to be Hermitian. This supplies the previously missing singleton and
complete exceptional-set argument without a codeword enumeration.

The \(p=5,7\) verifier checks the explicit bank, symbolic identities, the
explicit far endpoint, and the compact decoder on all \(625\) and \(2401\)
field labels. Every membership decision and recovered Hermitian pair
matches the bank. It does not enumerate codewords; the completeness
classification here is an algebraic proof. The bank is below the full
first-order curve, the code dimension
exceeds the characteristic, and the domain is the whole quadratic
subfield. No prime-alphabet or prescribed short-domain statement follows.
