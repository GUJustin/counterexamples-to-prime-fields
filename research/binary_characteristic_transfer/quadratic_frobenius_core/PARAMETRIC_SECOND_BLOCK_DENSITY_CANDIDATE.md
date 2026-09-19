# Parametric second-block puncturing: audited candidate

September 18, 2026. **PASS.** This is a concentration refinement of the existing two-block Frobenius construction. It has fixed message dimension three, vanishing rate and vanishing fractional gap; it is not a prime-alphabet or practical-length result.

## Exact finite formulation

Let \(p\ge5\) be prime, \(N=2(p^2-1)\), and choose an integer \(0<m<N\). Define
\[
\delta=m/N,\quad n=N+m,\quad
T=\lfloor\sqrt{2n-1}\rfloor,\quad
\ell=T-2p+2,\quad
\gamma=\delta-\frac{\ell-1}{2p-2}.
\]
Sufficient finite hypotheses are:

1. \(m\ge2p+3\), equivalently \(T>2p\);
2. \(\sqrt{3n/2}+(3n/8)^{1/4}<2p\);
3. \(\gamma>0\) and \(p(p+1)\exp[-4(p-1)\gamma^2]<1\).

Then the existing construction, retaining exactly \(m\) second-block points, has source and common agreement \(A=2p\), exactly \(B=(p+1)(p^2-1)\) singleton-list parameters, one further parameter with \(p+1\) witnesses, and empty lists elsewhere at threshold \(T\). Moreover
\[
n a_1(3/n)<A<T<\sqrt{2n}.
\]

For the proof, sample an \(m\)-subset of the second block. For a canonical support of size \(k\in\{2p-2,2p\}\), its retained size \(Z\) is hypergeometric with mean \(\delta k\). The strict failure event is \(Z\le\ell-1\), so sampling-without-replacement Hoeffding gives
\[
\Pr[Z<\ell]
\le\exp\!\left[-2k\left(\delta-\frac{\ell-1}{k}\right)^2\right]
\le\exp[-4(p-1)\gamma^2].
\]
The second inequality uses \(\ell-1>0\) and \(k\ge2p-2\). A union bound over the \(p(p+1)\) supports is less than one. Every doubly canonical witness then has at least \(2p-2+\ell=T\) matches. All other witnesses still have at most \(A\) matches by the existing classification. The exact source/common agreements and affine endpoint normalization are unchanged.

## Every fixed density below one third

Fix \(0<c<1/3\), and set \(m=\lfloor cN\rfloor\). Then
\[
\gamma\longrightarrow 1+c-\sqrt{1+c}>0,\qquad
\frac{\sqrt{3n/2}+(3n/8)^{1/4}}p
\longrightarrow\sqrt{3(1+c)}<2.
\]
All three finite hypotheses therefore hold for every sufficiently large prime, with the onset depending on \(c\). The formulas are exact; no numerical uniform onset over all \(c\in(0,1/3)\) is claimed. We have
\[
\frac{T-A}{T-3}\longrightarrow 1-\frac1{\sqrt{1+c}}.
\]
Thus these limits approach \(1-\sqrt3/2\) as \(c\) increases to \(1/3\). The fixed endpoint \(c=1/3\) is not asserted by this argument.

The existing explicit quarter-density choice is \(m=(p^2+3)/2\), which is two points larger than \(\lfloor N/4\rfloor\). The general finite formulation includes that choice directly, so its audited onset \(p\ge257\) can be retained without changing its length. A compact follow-on corollary, drafted in density_near_third_corollary.tex, chooses a varying density and attains the limiting ratio in one family.

Throughout, the code has only three message symbols, rate \(3/n=\Theta(p^{-2})\), and source/common fractional loss \((T-A)/n=\Theta(p^{-1})\). The field is \(\mathbb F_{p^4}\); the domain remains selected rather than explicitly enumerated.


## Rate-increase target after the user's parameter clarification

Increasing the message dimension alone cannot preserve the current placement:
for every k>=4, the first-order lower bound gives
n*a1(k/n)>sqrt(k*n/2)>=sqrt(2n)>T. Thus any successful dimension-increase
transformation must also increase the tested agreement; retaining the existing
quadratic witnesses at the old threshold cannot suffice.

There is a second, separate limitation for this exact received line. Its first
block has f=X^(2p), g=0, so once k>=2p+1 every line word has a codeword agreeing
on all 2(p²−1) first-block coordinates. This includes the normalized endpoint
words. Consequently the old source agreement A=2p cannot persist at those
dimensions. Neither observation is an impossibility theorem for changing the
sources, domain, or agreement threshold.

The next substantive target is therefore a construction that jointly raises
message dimension and agreement while proving source bounds against every new
codeword, rather than another optimization of this fixed-dimension ratio.
