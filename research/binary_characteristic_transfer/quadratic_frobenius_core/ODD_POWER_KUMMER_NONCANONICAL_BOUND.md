# Odd higher-power lifts: Kummer classification and exact source agreement

2026-09-18. The local shared-component case is completely classifiable.
It improves the earlier \(hp+h^2\) noncanonical bound, and makes every
nonexceptional parameter have **exactly** \(hp\) nearest agreement under
the sufficient conditions below. No finite search is used.

## Local classification

Let \(B=\mathbb F_{p^2}\), and let \(t>1\) be odd with
\(\gcd(t,p(p^2-1))=1\). Let \(P\in B[Z]\) be nonconstant, of degree at most
\(t\), and not of the form \(aZ^t+b\). Consider
\[
 z^{tp}=P(z),\qquad z\in B.
\tag{1}
\]

Let \(d\) be the greatest common divisor of \(t\) and all multiplicities
of the roots of \(P\) over \(\overline B\). Write \(t=dH\).
Then \(P=R^d\) with \(R\in B[Z]\), \(\deg R\le H\), and
\(U^H-R(Z)\) irreducible over \(\overline B[Z,U]\).

Here are the descent and irreducibility details. The map \(x\mapsto x^d\)
permutes \(B\), so the leading coefficient of \(P\) has a unique \(d\)th
root \(c\in B\). Choose the root \(R\in\overline B[Z]\) with leading
coefficient \(c\). Its coefficientwise \(p^2\)-Frobenius is another
\(d\)th root of \(P\) with the same leading coefficient; their quotient
is a \(d\)th root of unity and hence equals one. Therefore \(R\in B[Z]\).
By maximality of \(d\), \(R\) is not an \(\ell\)th power in
\(\overline B(Z)\) for any prime \(\ell\mid H\).

For completeness, the elementary Kummer argument proves the needed
irreducibility. The field \(F=\overline B(Z)\) contains all \(H\)th roots
of unity and has characteristic coprime to \(H\). If \(u^H=R\), then
\(F(u)/F\) is Galois, because all roots \(\zeta u\) already lie in it.
Its Galois group embeds in \(\mu_H\). If its order \(e\) were smaller
than \(H\), then \(u^e\in F\), so
\(R=(u^e)^{H/e}\) would be an \(\ell\)th power for some
\(\ell\mid H/e\), a contradiction. Thus its degree is \(H\).
The case \(H=1\) is immediate.

Because \(d\)-powering is a permutation of \(B\), (1) is equivalent to
\[
 z^{Hp}=R(z).
\]
Put \(u=z^p\), and let \(\sigma\) raise coefficients in \(B\) to the
\(p\)th power. Every solution lies on both curves
\[
 C_1:\ U^H=R(Z),\qquad C_2:\ Z^H=R^\sigma(U).
\tag{2}
\]
Both have total degree \(H\). If they have no common component,
Bézout gives at most \(H^2\) solutions.

If they do share a component, irreducibility of \(C_1\) and equality of
degrees force their defining polynomials to be scalar multiples.
Comparing the separate \(Z\)- and \(U\)-terms gives
\[
 R(Z)=aZ^H+b,\qquad a^{p+1}=1,\qquad b^p=-a^p b.
\tag{3}
\]
Since \(H\)-powering also permutes \(B\), substituting \(y=z^H\)
reduces the original solution set bijectively to
\[
 y^p-ay=b.
\]
This is a \(p\)-point affine \(\mathbb F_p\)-line. In the noncanonical
case \(b\ne0\), so all \(p\) solutions are nonzero. If \(d=1\), (3)
would make \(P\) canonical, excluded by hypothesis. Thus a genuine
shared-component exception has \(d>1\).

In particular, for every noncanonical \(P\),
\[
 \#\{z\in B:z^{tp}=P(z)\}\le\max(p,H^2)\le\max(p,t^2).
\tag{4}
\]
More precisely, either there are at most \(H^2\) solutions, or
\[
 P(Z)=(aZ^H+b)^d
\]
with the compatibility conditions (3), and there are exactly \(p\)
solutions. This classifies the relevant shared-component case; it does
not claim that every polynomial with at most \(H^2\) solutions is
irreducible before maximal-power reduction.

For \(t=5\), a noncanonical polynomial with more than \(25\) matches
must be \((aZ+b)^5\). Its full matching set is the ordinary affine
\(\mathbb F_p\)-line \(z^p=az+b\) in the physical branch coordinate.
After the map \(y=x^5\), its image is a degree-five parametrized curve;
it need not be a line in the normalized \(y\)-plane.

## Global higher-power bound

Use the primitive-scale domain of
[HIGHER_POWER_FULL_FIBER_LIFT.md](HIGHER_POWER_FULL_FIBER_LIFT.md), with
odd \(h>1\) dividing \(p^2+1\), and
\[
 h-1<(p^2+1)/h.
\tag{5}
\]
Arbitrary puncturing of the two blocks is allowed for this upper bound.
Let \(q\) have degree at most \(h\), but not be \(aX^h+b\).
An intermediate nonzero coefficient \(q_j\), \(0<j<h\), permits at most
\(\gcd(j,h)\) coefficientwise-\(B\) branches in one block. The previous
primitive-scale congruence excludes coefficientwise-\(B\) branches
in both blocks at once. If \(\ell_0\) is the smallest prime divisor of
\(h\), there are therefore at most \(h/\ell_0\) good branches among
the \(2h\) branches.

Each good branch obeys (4), and every other branch has at most \(h\)
matches by a nonzero \(B\)-linear projection. Thus
\[
 \operatorname{agr}(f+\lambda g,q)
 \le {h\over\ell_0}\max(p,h^2)
       +(2h-h/\ell_0)h.
\tag{6}
\]
In particular this is strictly less than \(hp\) whenever \(p\ge h^2\):
after division by \(hp\), it is at most
\[
 {1\over\ell_0}+{2-1/\ell_0\over h}<1
 \quad (h\ge\ell_0\ge3).
\]

For \(h=5\), there is at most one good branch and (6) becomes
\[
 \operatorname{agr}(f+\lambda g,q)\le\max(p,25)+45.
\]
It is at most \(5p\) for all admissible primes \(p\ge17\).

## An optional composition refinement

The same argument improves (6) when the exponents of \(q\) have a
common divisor. Put
\[
 \delta=\gcd\bigl(h,\{j:0<j<h,\ q_j\ne0\}\bigr),\qquad H_0=h/\delta.
\]
Then \(\delta\) is a proper divisor of \(h\), so \(H_0\ge3\).
There are at most \(\delta\) good branches globally: differences of
two compatible branch indices must lie in the simultaneous kernels of
all multiplication-by-\(j\) maps on \(\mathbb Z/h\mathbb Z\).
Every normalized branch polynomial is
\(\widetilde P(z^\delta)\), with \(\deg\widetilde P\le H_0\).
Since \(\delta\)-powering permutes \(B\), a good branch has at most
\(\max(p,H_0^2)\) matches by (4) at exponent \(H_0\).
On a bad branch the projected polynomial is also a polynomial in
\(z^\delta\), giving at most \(H_0\), rather than \(h\), roots in \(B\).
Consequently
\[
 \operatorname{agr}(f+\lambda g,q)
 \le\delta\max(p,H_0^2)+(2h-\delta)H_0
 =\delta\bigl(\max(p,H_0^2)+(2H_0-1)H_0\bigr).
\tag{7}
\]
This is at most \(hp\) whenever \(p\ge3h-1\). Indeed \(p\ge3H_0-1\);
if \(p<H_0^2\), the parenthesized expression is
\(3H_0^2-H_0\le H_0p\). If \(p\ge H_0^2\), the inequality follows from
\[
 (H_0-1)H_0^2-(2H_0^2-H_0)
 =H_0(H_0^2-3H_0+1)>0.
\]
For odd prime \(p\), equality \(p=3H_0-1\) cannot occur, so the bound
is actually strict. The simpler sufficient condition \(p\ge h^2\)
already covers the main growing-\(h\) family and the BabyBear instance.

## Exact source and complement profile

Retain the complete first block. At any label, a canonical nonzero
core fiber attains \(hp\) agreement. Outside the union of the canonical
label planes, every canonical polynomial has at most \(hp\) total
matches, and (6) or (7) bounds all noncanonical polynomials by \(hp\).
Therefore **every** nonexceptional label has exact nearest agreement
\(hp\), not merely a selected pair of endpoints.

Ordinary common agreement remains exactly \(hp\) by the independent
indicator-polynomial argument. For any retained second block where all
doubly canonical polynomials attain a threshold \(T>hp\), the complete
threshold-list profile remains unchanged, and both chosen endpoints
have exact agreement \(hp\).

For the explicit \(p=97,h=5\) fixture the noncanonical bound is
\(97+45=142<485\); its endpoint interval can thus be sharpened to the
exact value \(485\), without any codeword enumeration. The endpoint
loss at threshold \(593\) becomes exactly \(108\), or \(108/587\) of
the capacity margin. For the BabyBear \(h=12241\) fixture and for the
growing-\(h\) family, \(p\ge h^2\), so their former \(h^2\) uncertainty
in endpoint agreements also disappears.
