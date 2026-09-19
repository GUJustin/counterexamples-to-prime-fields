# Hermitian norm specialization: injective labels and two far sources

This sharpens the label count in the norm section of
`LOCATORS_TREES_NORMS_TRANSFER.md`. The norm identity is the existing one;
the new point is that, at native degree two, its labels are injective on
the distinct Hermitian circles. The old `verify_odd_norm.json` already
reported 18 labels for the 18 distinct circles at \(p=3\), although its
proved general multiplicity bound was weaker. The argument below proves
the full count for every odd prime and a source bound for \(p\ge5\).

## Exact statement

Let \(p\ge5\) be prime, \(B=\mathbb F_{p^2}\subset E=\mathbb F_{p^4}\),
and choose any \(\beta\in E\setminus B\). Put

\[
 n=p^2,\qquad D=p^2-p,\qquad K=p^2-2p,\qquad
 T_0=D-1,\qquad T=D-2,
\]

and use the ordinary RS code of dimension \(K\) on the full domain \(B\).
Define

\[
 R=X^D,\qquad f=\frac{R-R(\beta)}{X-\beta},\qquad
 g=\frac1{X-\beta}.
\]

Here \(f\) is a polynomial of degree \(D-1\), evaluated on \(B\).
There are exactly \(p^2(p-1)\) distinct, nonzero exhibited labels \(z\in E\)
for which \(f+zg\) has a strict-degree-\(<K\) witness agreeing at exactly

\[
 T_0=p^2-p-1
\]

coordinates. Consequently the same labels qualify at the weaker threshold

\[
 T=p^2-p-2<\sqrt{n(K-1)}.
\]

For the sources and ordinary common agreement,

\[
 \operatorname{agr}_K(g)=\operatorname{CA}_K(f,g)=K,
 \qquad K\le\operatorname{agr}_K(f)\le D-r_p<T,
\]

where

\[
 r_p=\min\{e\in\mathbb Z:e\ge2,\ e^2-e+1\ge p\}.
\]

Thus both sources are individually far at threshold \(T\), within the
quartic alphabet. The claim concerns an exhibited bank, not a complete
list classification or singleton lists; the upper bound on
\(\operatorname{agr}_K(f)\) is not asserted to be exact.

## 1. The full Hermitian family is present

For \(s\in B\) and \(c\in\mathbb F_p\) with

\[
 \delta=c-s^{p+1}\ne0,
\]

set

\[
 G_{s,c}=X^{p+1}+sX^p+s^pX+c
         =(X+s)^{p+1}+\delta.
\]

There are \(p^2(p-1)\) different polynomials. Each has precisely \(p+1\)
simple roots in \(B\), since a nonzero norm fiber from \(B\) to
\(\mathbb F_p\) has that size. Its derivative is \((X+s)^p\), which is
nonzero at its roots.

These are exactly the distinct polynomials obtained from the old
two-shift family at any fixed \(A\in\mathbb F_p\setminus\{0,1\}\):

\[
 G=A(X+t)^{p+1}+(1-A)(X+u)^{p+1},\qquad t\ne u\in B.
\]

Indeed, \(s=At+(1-A)u\) and

\[
 c-s^{p+1}=A(1-A)(t-u)^{p+1}.
\]

For each prescribed \((s,c)\), choose a norm preimage \(v=t-u\) and put

\[
 t=s+(1-A)v,\qquad u=s-Av.
\]

Exactly \(p+1\) choices of \(v\) work. Thus the ordered-pair
multiplicity in this specialization is exactly \(p+1\) before evaluating
at the pole; it does not represent a further loss in the distinct-circle
count.

Write \(\Lambda=X^{p^2}-X\). Define

\[
 P_{s,c}=(X+s)\frac{\Lambda}{G_{s,c}}.
\]

This is monic of degree \(D\). Its distinct domain roots are exactly

\[
 B\setminus Z(G_{s,c}),
\]

of cardinality \(T_0\). The extra factor \(X+s\) repeats a root in this
complement; it does not add a new coordinate. Every algebraic root of

\(P_{s,c}\) is therefore in \(B\).

For an explicit high-coefficient check, put \(Y=X+s\). Translation by

\(s\in B\) fixes \(\Lambda\), and

\[
 P_{s,c}=Y^2\sum_{j=0}^{p-2}(-\delta)^j
                    Y^{(p+1)(p-2-j)}.
\]

Its leading term is \(Y^D\), and its next unshifted degree is \(K-1\).
Since \(D=p(p-1)\), translation gives

\[
 P_{s,c}=X^D-s^pX^K+\text{terms of degree at most }K-1.
 \tag{1}
\]

In particular \(P_{s,c}=R+C_{s,c}\), with \(\deg C_{s,c}\le K\).

## 2. Pole evaluation loses no circle

The old Frobenius identity specializes to

\[
 G^p-G=\Lambda(X+s)^p,\qquad
 P^p=\Lambda^{p-1}\bigl(1-G^{-(p-1)}\bigr).
 \tag{2}
\]

The latter is a rational identity, evaluated only where \(G\ne0\).
All \(G(\beta)\) and \(\Lambda(\beta)\) are nonzero. Consequently

\[
 P_{s,c}(\beta)=P_{s',c'}(\beta)
 \quad\Longrightarrow\quad
 \frac{G_{s,c}(\beta)}{G_{s',c'}(\beta)}\in\mathbb F_p^*.
 \tag{3}
\]

For \(a\in\mathbb F_p^*\), every nonzero polynomial

\[
 G_{s,c}-aG_{s',c'}
\]

has all its roots in \(B\). If \(a\ne1\), divide by \(1-a\); the result
is again a monic Hermitian polynomial

\[
 (X+v)^{p+1}+d-v^{p+1},\qquad v\in B,\ d\in\mathbb F_p.
\]

A nonzero norm target gives \(p+1\) native roots, and a zero target gives
the sole root \(-v\), with multiplicity \(p+1\). If \(a=1\) and \(s\ne s'\),
the difference is

\[
 uX^p+u^pX+d,\qquad u\in B^*,\ d\in\mathbb F_p.
\]

This is a nonzero trace functional on \(B\), hence has \(p\) native roots;
its nonzero derivative shows there are no other roots. If \(a=1,s=s'\),
the difference is a constant. Thus (3), with an exterior pole, forces

\[
 a=1,\qquad s=s',\qquad c=c'.
\]

Hence \(P_{s,c}(\beta)\) is injective on the entire Hermitian family.
Every such value is nonzero because every root of \(P_{s,c}\) lies in \(B\).

## 3. Strict code dimension and common agreement

For \(z=P_{s,c}(\beta)\), define

\[
 H_{s,c}(X)=
 \frac{R(X)-P_{s,c}(X)+P_{s,c}(\beta)-R(\beta)}{X-\beta}.
\]

Equation (1) shows that this is a polynomial of degree at most \(K-1\),
and

\[
 f+zg-H_{s,c}=\frac{P_{s,c}}{X-\beta}
\]

on the domain. This proves the exact \(T_0\) agreement of the exhibited
witness and the distinct nonzero label count.

For any polynomial \(Q\) of degree \(<K\), the reciprocal agreement
equation \(g(x)=Q(x)\) is the nonzero degree-at-most-\(K\) equation

\[
 1-(X-\beta)Q(X)=0.
\]

Thus \(\operatorname{agr}_K(g)\le K\). Interpolation on any \(K\)
coordinates attains equality and simultaneously interpolates both
sources. It follows that

\[
 \operatorname{agr}_K(g)=\operatorname{CA}_K(f,g)=K.
\]

## 4. A rational-map bound makes the other source far

Let \(h\) be any polynomial of degree \(<K\), and put

\[
 P=(X-\beta)(f-h)=X^D+C,\qquad \deg C\le D-p,
 \qquad P(\beta)=0.
\]

Let \(V\in B[X]\) be the monic locator of **all** roots of \(P\) in \(B\).
Write their number as \(D-e\). Since \(f-h\) has degree \(D-1\), we have

\(e\ge1\). If \(e\ge p\), the desired bound is immediate. Assume

\(1\le e<p\), and write \(F=P/V\), monic of degree \(e\).
The highest \(e\) nonleading coefficients of \(P\) vanish. Recursively
comparing them with the product of the monic \(B\)-polynomial \(V\) and

\(F\) shows that every coefficient of \(F\) is in \(B\).
Since \(F(\beta)=0\), necessarily \(e\ge2\).

Set \(G=\Lambda/V\), of degree \(p+e\). It is squarefree and all its roots
are in \(B\). The identity \(PG=\Lambda F\) implies

\[
 G=X^pF+A,\qquad \deg A\le e.
 \tag{4}
\]

To see the degree bound directly,

\[
 X^D(G-X^pF)=-XF-CG
\]

has right-hand degree at most \(D+e\). Crucially, \(V\) contains *all*
native roots of \(P\). Thus \(P\), and hence \(F\), is nonzero at every
root of \(G\). Therefore \(\gcd(F,A)=\gcd(F,G)=1\).

The rational map \(Q=-A/F\in B(X)\) has degree exactly \(e\). At each
of the \(p+e\) roots \(x\in B\) of \(G\),

\[
 x^p=Q(x),\qquad x=Q^\sigma(Q(x)),
\]

where \(\sigma\) raises the coefficients to their \(p\)-th powers.
All denominators are nonzero at these points: the second denominator is
the \(p\)-th power of the first, up to the cleared factors. The composition

\(Q^\sigma\circ Q\) has degree \(e^2>1\), so it is not the identity.
The fixed-point numerator has degree at most \(e^2+1\). Hence

\[
 p+e\le e^2+1.
\]

By the definition of \(r_p\), this forces \(e\ge r_p\). The case \(e\ge p\)
also implies it, because \(r_p\le p\). We have proved

\[
 \operatorname{agr}_K(f)\le D-r_p.
\]

For \(p\ge5\), \(r_p\ge3\), so this is strictly less than \(T=D-2\).
This uses the degree-two native field \(B/\mathbb F_p\) and the fact that

\(\beta\notin B\); it is an all-witness bound, not merely a check of the
Hermitian bank.

## 5. Placement and limitations

The exact Johnson calculations use strict dimension \(K\):

\[
 T_0^2-n(K-1)=2p+1>0,
\]

\[
 T^2-n(K-1)=-2p^2+4p+4<0\qquad(p\ge3).
\]

Thus lowering the tested agreement by one coordinate really moves the
bank below the exact Johnson threshold.

It does **not** place it above the full first-order curve. Write

\(\rho=K/n=1-2/p\). This is on the high branch, whose positive root is
specified by

\[
 F(a,\rho)=(8-\rho)a^2-6\rho a+\rho(4\rho-5)=0.
\]

Exact substitution gives

\[
 F(T/n,\rho)=-\frac{(p-2)(p+2)(9p+2)}{p^5}<0,
\]

and even

\[
 F(T_0/n,\rho)=-\frac{p^3-11p-2}{p^5}<0
 \qquad(p\ge5).
\]

Both agreements are below \(n a_1(K/n)\). Asymptotically,

\[
 n a_1(K/n)=p^2-p-\frac78-\frac1{32p}+O(p^{-2}).
\]

The positive quantitative statement is

\[
 \#\text{exhibited labels}=p^2(p-1)=n^{3/2}-n,
 \quad \frac K n=1-\frac2p,
 \quad \frac{T-\operatorname{CA}}n=\frac{p-2}{p^2}.
\]

The common-agreement loss divided by the agreement-minus-dimension
margin is exactly one, since \(\operatorname{CA}=K\). The guaranteed
individual separation of the first source is smaller:

\[
 \frac{T-\operatorname{agr}_K(f)}n
 \ge\frac{r_p-2}{p^2}\asymp p^{-3/2}=n^{-3/4}.
\]

The alphabet has \(p^4=n^2\) elements; the displayed exceptional-label
probability under uniform native challenges is \((p-1)/p^2\sim1/p\).
The characteristic is \(p<K\) for \(p\ge5\). This is neither a prime
alphabet theorem nor a prescribed short-domain result, and it does not
give fixed positive rate bounded away from one, constant absolute
fractional loss, or first-order tightness.

## 6. Exact finite regression

`verify_hermitian_norm_injective.py` independently constructs quadratic
towers for \(p=5,7\), checks all distinct circles and all their native
coordinates, and writes `verify_hermitian_norm_injective.json`. It checks
the norm-pair coverage, polynomial division and high coefficient, both
Frobenius identities, disjoint \(\mathbb F_p^*\)-scaled pole values,
nonzero injective labels, strict witnesses, and exact witness agreement.
It also verifies the Johnson and first-order formulas symbolically.
The decoder extension tests all \(625\) and \(2401\) field labels against
the independently constructed bank, checking both membership and the
recovered Hermitian parameters. It checks the explicit second endpoint
\(c_*^p=\Lambda(\beta)^{p-1}\), its exclusion from the bank, and that every
resulting exceptional affine parameter avoids zero and one.
The source bound in Section 4 is a proof, not an exhaustive enumeration
of all codewords in these tests.

The finite ledgers are

| \(p\) | \(n\) | \(K\) | \(T_0\) | \(T\) | labels | \(r_p\) | proved source upper bound |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 5 | 25 | 15 | 19 | 18 | 100 | 3 | 17 |
| 7 | 49 | 35 | 41 | 40 | 294 | 3 | 39 |

No manuscript file, other repository, or old regression was modified.
