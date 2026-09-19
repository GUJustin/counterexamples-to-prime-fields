# Quadratic-extension two-block Frobenius reduction

September 18, 2026. Bounded algebraic assessment; no scan or manuscript edit.

**Outcome.** For the specified two-block model, a coefficient of norm different
from one permits an additive common-agreement gap of at most four. A
nontrivial norm-one coefficient does give a valid lower-dimensional identity,
but its labels are centers of pairs of rich prime-plane lines, not the
disjoint label planes of the quartic construction. At length
\(n=\Theta(p^2)\) there cannot be superlinearly many native labels because
the alphabet itself has only \(p^2\) elements. At \(n=o(p^2)\), the identity
reduces the desired result to an explicit unresolved incidence construction.
For a prescribed domain contained in \(\mathbb F_p\), every line word already
has at least \(n/2\) quadratic agreement, excluding the below-Johnson
far-endpoint target.

This concerns the following words over \(E=\mathbb F_{p^2}\), \(p\ge5\), on
arbitrary disjoint sets \(D_0,D_1\subset E\):
\[
f(x)=
\begin{cases}x^{2p}&x\in D_0,\\c x^{2p}&x\in D_1,\end{cases}
\qquad g=1_{D_1},\qquad c\in E^*.
\]
The code has dimension \(k=3\), domain size \(n=|D_0|+|D_1|\le p^2\), and
rate \(3/n\). The received word is \(w_\lambda=f+\lambda g\).
All agreement counts below refer to actual retained coordinates, not to
complete fibers that might be absent from the domain.

## Common agreement and the block maximum

Let \(U_i\) be the maximum quadratic agreement with \(f|_{D_i}\), and put
\(U=\max(U_0,U_1)\). Adding a constant to the second block does not change
\(U_1\). Ordinary common agreement satisfies
\[
U\le\operatorname{CA}(f,g)\le\max(U,4).
\]
Indeed, a constant polynomial explaining \(g\) can use just one block, giving
\(U_0\) or \(U_1\). A nonconstant polynomial of degree at most two takes the
value zero at at most two points and the value one at at most two points,
so a common explanation of that kind uses at most four coordinates.
In particular \(\operatorname{CA}(f,g)=U\) whenever \(U\ge4\).

## Exact rich-witness restriction

For a normalized equation
\[
X^{2p}=A X^2+B X+C,\qquad B\ne0,
\]
Frobenius and substitution give
\[
B^pX^p=H(X):=(1-A^{p+1})X^2-A^pBX-A^pC-C^p.
\]
Every solution is a root of the degree-at-most-four polynomial
\[
H(X)^2-B^{2p}(AX^2+BX+C).
\]
More than four solutions force this polynomial to vanish identically. Its
fourth-degree coefficient and its quadratic coefficient then give
\[
N(A)=1,\qquad B^{2p-2}=A^{-3}.
\]
Moreover \(AX^2+BX+C=H(X)^2/B^{2p}\), so its discriminant is zero.
These are necessary identities; no converse or exhaustive scan is needed.

If \(B=0\), writing \(Y=X^2\) shows that \(Y^p-AY=C\) has at most one
solution unless \(N(A)=1\). Thus an even witness with more than four
matches also forces \(N(A)=1\).

Now write a witness as \(Q=aX^2+bX+d\). Richness on the first block forces
\(N(a)=1\), and richness on the second forces \(N(a/c)=1\). Consequently:

1. If \(N(c)\ne1\), no quadratic has more than four matches on both blocks.
   For every label,
   \[
   \operatorname{agr}(w_\lambda,\operatorname{RS}_3)\le U+4.
   \]
   Therefore the additive surplus over common agreement is at most four.
   At a square-root-scale threshold its fraction of the capacity margin
   tends to zero.
2. Suppose \(N(c)=1\) and \(c\ne1\). A non-even quadratic cannot be rich on
   both blocks either. The two zero-discriminant conditions are
   \(b^2=4ad\) and \(b^2=4a(d-\lambda)\), hence \(\lambda=0\).
   The two remaining coefficient identities would then require
   \[
   b^{2p-2}=a^{-3},\qquad
   (b/c)^{2p-2}=(a/c)^{-3}.
   \]
   Since \(c^p=c^{-1}\), these give \(c^4=c^3\), contradicting \(c\ne1\).
   Thus all witnesses outside the doubly canonical even family have total
   agreement at most \(U+4\).

The degenerate choice \(c=0\) has the still smaller bound \(U+2\):
a nonconstant quadratic matches the constant second block at at most two
points, while a constant witness has at most two first-block matches.

## Norm-one coefficients: the exact center identity

Assume \(N(c)=1\), \(c\ne1\). For each label define its unique center
\[
z=\left(\frac{\lambda}{1-c}\right)^p.
\]
The complete family of even quadratics canonical on both unpunctured
blocks is
\[
\boxed{\quad Q_{a,z}(X)=a(X^2-z)+z^p,\qquad
N(a)=1,\qquad \lambda=(1-c)z^p.\quad}
\]
To verify completeness, the constant term \(d\) of \(aX^2+d\) must satisfy
\[
d^p=-a^{-1}d,\qquad
(d-\lambda)^p=-a^{-1}c^{-1}(d-\lambda).
\]
Solving gives
\[
d=\frac{\lambda+a c\lambda^p}{1-c}=z^p-a z.
\]
Conversely this constant satisfies both conditions.

Choose \(\eta\in E^*\) with \(c=\eta^{1-p}\). Such an \(\eta\) exists because
the map \(\eta\mapsto\eta^{1-p}\) has image the norm-one group; and
\(\eta\notin\mathbb F_p\) since \(c\ne1\). Write \(a=u^{p-1}\), with
the direction \([u]\in E^*/\mathbb F_p^*\). The support is exactly
\[
\{x\in D_0:x^2\in z+u\mathbb F_p\}
\ \coprod\
\{x\in D_1:x^2\in z+\eta u\mathbb F_p\}.
\]
Thus a label is a center \(z\), and its \(p+1\) possible canonical witnesses
correspond to pairs of lines through that center with fixed direction ratio
\(\eta\). The two directions are distinct. This differs from independent
two-dimensional label planes in the quartic-extension construction:
every old label plane \(I_a+\eta I_a\) now equals all of \(E\).

There is a useful exact incidence check. At fixed \(z\), any coordinate with
\(x^2\ne z\) lies in the support of exactly one of these \(p+1\) witnesses:
\[
a=(x^2-z)^{p-1}\quad\text{on }D_0,\qquad
a=c(x^2-z)^{p-1}\quad\text{on }D_1.
\]
A coordinate with \(x^2=z\) belongs to every witness. If there are \(e_z\)
such retained coordinates, then \(0\le e_z\le2\) and
\[
\sum_{N(a)=1}\operatorname{agr}_{D_0\cup D_1}(w_{(1-c)z^p},Q_{a,z})
 = n+p e_z.
\]
The remaining supports are a partition. This is an incidence identity,
not a bound asserting that every label has a rich witness.

For completeness, \(c=1\) returns the parallel-line case. Put
\(I_a=\operatorname{Im}(Y^p-aY)\). A doubly canonical even witness requires
\(\lambda\in I_a\), \(d\in I_a\); its two fibers have constants \(d\) and
\(d-\lambda\). Each nonzero \(\lambda\) fixes \(a\) uniquely. The exceptional
non-even double-rich case can occur only at \(\lambda=0\). This is the
already noted parallel-fiber collision model, not a replacement for
quartic label separation.

## Square-lift accounting in the actual quadratic extension

The doubled full-plane domains of the quartic theorem do not exist inside
\(E\): the map \(x\mapsto x^2\) reaches only half of \(E^*\), with two
preimages each. More precisely, for a norm-one \(a\), let
\(\ker(Y^p-aY)=u\mathbb F_p\), and write \(\chi_E\) for the quadratic
character of \(E\).

- A nonzero affine fiber \(y_0+u\mathbb F_p\) has exactly
  \(p-\chi_E(u)\), hence \(p-1\) or \(p+1\), square-root coordinates in \(E\).
- The zero fiber has \(2p-1\) coordinates if \(\chi_E(u)=1\), and only the
  coordinate zero if \(\chi_E(u)=-1\).

For the first count, \(\chi_E(y)=\chi_p(N(y))\), and the norm of
\(y_0+ut\) is a quadratic in \(t\) with nonzero discriminant. Its character
sum is \(-\chi_E(u)\), giving the stated count. The second count uses that
every element of \(\mathbb F_p^*\) is a square in \(E\). Puncturing or
partitioning can only reduce these complete-fiber counts.

## Domain, rate, and the remaining construction problem

At \(n=\Theta(p^2)\), the native affine line has at most \(p^2=\Theta(n)\)
labels, regardless of the partition or coefficient. Thus this model cannot
give \(B/n\to\infty\) at that scale.

At \(n=o(p^2)\), the norm-one identity has native label room, but it supplies
no structured short domain. An exact sufficient target is now explicit:
choose disjoint \(D_0,D_1\), compute \(U\), and find superlinearly many centers
\(z\) whose paired-line support above has size at least \(T>U+4\), while
retaining at least two centers where every paired-line support has size at
most \(U+4\). The latter yield two far endpoints, since all other
quadratics already have agreement at most \(U+4\). Reparametrizing through
those endpoints preserves the full label count and ordinary common agreement.

For a constant fraction of the capacity surplus at a dimension-three
above-first-order, below-Johnson threshold, the target is
\[
T=\Theta(\sqrt n),\qquad T-(U+4)=\Omega(\sqrt n),\qquad
B=\omega(n).
\]
Each qualifying pair must have \(\Omega(\sqrt n)\) matches on **both**
blocks, since either block contributes at most \(U\). This is a weighted,
fixed-direction-ratio version of the rich-line problem already left open in
[PUNCTURING_ASSESSMENT.md](PUNCTURING_ASSESSMENT.md).
Weights are the actual square-root multiplicities, at most two, with the
two blocks sharing that total multiplicity budget. The center formula
removes the noncanonical-witness uncertainty in this particular model;
it does not construct the required rich lines or establish many distinct
rich centers.

Finally, if \(D_0\cup D_1\subseteq\mathbb F_p\), then on the two blocks the
word is respectively \(X^2\) and \(cX^2+\lambda\). Every label therefore
has agreement at least
\[
\max(|D_0|,|D_1|)\ge n/2.
\]
For \(n>8\) this exceeds the dimension-three Johnson agreement
\(\sqrt{2n}\). Hence no two far endpoints below that threshold exist,
including on a prescribed base-field NTT subgroup. The same conclusion
holds asymptotically for domains covered by a fixed number of affine
\(\mathbb F_p\)-lines: Frobenius is affine on each such line, so one of the
finitely many block-line pieces gives a quadratic agreement of order \(n\).

The rate remains \(3/n\), and a square-root-scale capacity margin is
\(\Theta(n^{-1/2})\). This note proves no fixed-rate result, no practical
Goldilocks-squared exception family, and no obstruction to arbitrary
received words over a quadratic extension.
