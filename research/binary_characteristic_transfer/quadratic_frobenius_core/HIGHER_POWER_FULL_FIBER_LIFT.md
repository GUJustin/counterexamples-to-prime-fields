# Higher-power Frobenius lifts: unchanged rate, improved relative loss

2026-09-18. This is a proved extension-field construction on a selected
domain. Increasing the full-fiber multiplicity does **not** improve its
asymptotic orders of rate or fractional proximity gap. It does permit growing message
dimension and a larger loss as a fraction of the capacity margin, while
preserving superlinear singleton-label counts and placement above the
first-order curve and below Johnson.

The noncanonical bound is independently audited in
[HIGHER_POWER_FROBENIUS_BRANCH_AUDIT.md](HIGHER_POWER_FROBENIUS_BRANCH_AUDIT.md);
the positive regime is independently audited in
[HIGHER_POWER_MINIMAL_DIMENSION_POSITIVE_AUDIT.md](HIGHER_POWER_MINIMAL_DIMENSION_POSITIVE_AUDIT.md).
No neutral padding or restriction to composition-only witnesses is used.

**Deterministic refinement:** for odd h, the retained subset can now be
specified by complete multiplicative branches and one branch prefix; see
[the exact recipe](HIGHER_POWER_DETERMINISTIC_BRANCH_RETENTION.md). The
manuscript uses this shorter deterministic criterion, including the same
BabyBear numerical parameters. The general-h probabilistic criterion below
is retained as a separate valid formulation.

## Finite statement

Let \(p\ge5\) be prime, \(B=\mathbb F_{p^2}\), \(E=\mathbb F_{p^4}\), and
\(Q=p^2+1\). Let \(h>1\) be a proper divisor of \(Q\), and assume

\[
 h-1<Q/h.
\tag{1}
\]

Choose a primitive \(s\in E^*\), put \(\eta=s^h\), and define

\[
 D_0=\{x\in E^*:x^h\in B^*\},\qquad D_1=sD_0,\qquad
 N=h(p^2-1).
\]

These are disjoint sets of size \(N\). Choose an integer \(0<m<N\) and put

\[
 n=N+m,\quad k=h+1,\quad T=\lfloor\sqrt{hn-1}\rfloor,\quad
 K=h(p-1),\quad \ell=T-K,\quad
 \gamma=\frac mN-\frac{\ell-1}{K}.
\]

Assume

\[
 hp+h^2<T,\qquad 1\le\ell\le K,\qquad \gamma>0,\qquad
 p(p+1)\exp(-2K\gamma^2)<1.
\tag{2}
\]

Then there is an \(m\)-subset \(D'_1\subset D_1\) such that the
dimension-\(k\) Reed--Solomon code on \(D=D_0\cup D'_1\) has an affine line
with the following exact threshold-\(T\) list profile:

* \((p+1)(p^2-1)\) parameters have singleton lists;
* one further parameter has a list of size \(p+1\);
* every other parameter has an empty list.

One can select two parameters with empty lists as the endpoints. Each
endpoint has nearest agreement in \([hp,hp+h^2]\), and their ordinary
common agreement is exactly \(hp\). Consequently the guaranteed loss from
either endpoint is at least \(T-hp-h^2\); the common-agreement loss is
exactly \(T-hp\). The tested threshold is the largest integer strictly below
the Johnson value \(\sqrt{(k-1)n}\).

For first-order placement, it suffices additionally that \(k/n\) be in
the low-rate branch and

\[
 \sqrt{kn/2}+(k^3n/72)^{1/4}<hp.
\tag{3}
\]

This places even the lower endpoint-agreement bound above
\(n a_1(k/n)\). The familiar low-rate formula
\(a_1(\rho)=t(1+u)\), \(t=\sqrt{\rho/2}\),
\(u^2(u+3)=t\), implies the bound in (3), since
\(u\le\sqrt{t/3}\).

## Full-fiber and canonical identities

The multiplicative quotient \(E^*/B^*\) is cyclic of order \(Q\).
The group \((E^*)^h\) contains \(B^*\) because \(h\mid Q\).
Thus every \(y\in B^*\) has exactly \(h\) roots of \(x^h=y\) in \(E\),
and \(D_0\) has \(N\) points. It is the union of the \(h\) multiplicative
\(B\)-lines with representatives
\(\alpha_j=s^{(Q/h)j}\), \(0\le j<h\). Since \(h<Q\), the class
of \(\eta=s^h\) is nontrivial, so \(\eta\notin B\) and the two blocks
are disjoint.

Conversely, within this literal complete pullback model with
\(h\mid |E^*|\), pulling back **every** \(y\in B^*\) with \(h\) roots
requires \(h\mid Q\). A disjoint second scaled block requires \(h<Q\).
Arbitrary higher exponents without these conditions do not give the
advertised complete-fiber ledger.

On the two active blocks set

\[
 f(x)=
 \begin{cases}
 x^{hp},&x\in D_0,\\
 \eta^{1-p}x^{hp},&x\in D'_1,
 \end{cases}
 \qquad
 g(x)=\begin{cases}0,&x\in D_0,\\1,&x\in D'_1.\end{cases}
\]

For \(a^{p+1}=1\), let
\(I_a=\operatorname{Im}(y\mapsto y^p-ay)\subset B\).
These are the \(p+1\) different \(\mathbb F_p\)-lines in \(B\).
The witness \(q_{a,b}=aX^h+b\), \(b\in I_a\), matches \(f+\lambda g\)
on the core whenever

\[
 y^p-ay=b,\qquad y=x^h.
\]

It has \(hp\) core matches for \(b\ne0\), and \(h(p-1)\) for \(b=0\).
Writing \(x^h=\eta y\) on the second block, its fresh equation is
\(y^p-ay=(b-\lambda)/\eta\). Hence it is canonical on both blocks exactly
when

\[
 \lambda=b-\eta v,\qquad b,v\in I_a.
\tag{4}
\]

Because \(E=B\oplus\eta B\), the \(p+1\) two-dimensional
\(\mathbb F_p\)-planes \(I_a+\eta I_a\) meet pairwise only at zero.
Every nonzero label in their union therefore determines exactly one
canonical polynomial. There are \((p+1)(p^2-1)\) such labels.
At zero there are exactly \(p+1\) canonical polynomials.

For completeness, any polynomial of the form \(aX^h+b\) which is not
canonical on both blocks has at most \(hp\) total matches. If
\(a\in B\) has norm different from one, each block contributes at most
\(h\). If \(a\notin B\), projection onto \(E/B\) gives at most one
value of \(y\) on either block, again at most \(2h\) total. If \(a\in B\)
has norm one, a compatible right-hand side gives a \(p\)-point
affine fiber, and an incompatible one gives no matches. Thus a
polynomial canonical on only one block contributes at most \(hp\).

There are \(p(p+1)\) fresh canonical supports, each of size \(hp\) or
\(K=h(p-1)\) before puncturing. For a uniformly random \(m\)-subset of
the second block, the hypergeometric lower-tail bound gives probability
at most \(\exp(-2K\gamma^2)\) of retaining fewer than \(\ell\) points
from any one support. Larger supports obey the same bound, because
their normalized lower-tail deviation is at least \(\gamma\).
Condition (2) and a union bound therefore produce a single retained
set meeting every support in at least \(\ell\) points. Every
doubly canonical witness then has at least \(K+\ell=T\) matches.

## Why new degree-\(h\) witnesses do not enter the list

Let \(q(X)=\sum q_jX^j\) have degree at most \(h\), but not be of the
form \(aX^h+b\). Some coefficient with \(1\le j<h\) is nonzero.
On a core branch \(\alpha_tB^*\), coefficientwise membership of the
normalized matching polynomial in \(B[X]\) requires
\(q_j\alpha_t^j\in B\). On a fresh branch \(s\alpha_uB^*\), it requires
\(q_js^{j-h}\alpha_u^j\in B\). If both occurred, then

\[
 j-h+(Q/h)j(u-t)\equiv0\pmod Q.
\tag{5}
\]

This congruence is solvable precisely when
\((Q/h)\gcd(j,h)\mid j-h\), which (1) excludes. Thus at least one entire
block has no coefficientwise-\(B\) branch. On each of its \(h\)
branches a nonzero \(B\)-linear projection annihilating \(B\) gives a
nonzero polynomial of degree at most \(h\), hence at most \(h\) matches.
That block contributes at most \(h^2\). On the other block the ordinary
matching equation has degree exactly \(hp\), hence at most \(hp\)
matches. Arbitrary second-block puncturing preserves both bounds.

Every noncanonical polynomial therefore has at most \(hp+h^2<T\)
matches. This proves the complete list profile, not just the canonical
lower bound. The union of label planes has
\(1+(p+1)(p^2-1)<p^4-1\) elements, so two endpoints outside it exist.

For ordinary common agreement, a nonconstant degree-\(\le h\)
polynomial explaining the indicator \(g\) has at most \(h\) zeros
on the core and at most \(h\) one-values on the fresh block. A constant
explanation restricts the common support to one block, where explaining
\(f\) is an ordinary degree-\(hp\) root problem. Thus common agreement
is at most \(hp\). A canonical core fiber with \(b\ne0\), together with
the zero explanation of \(g\), attains \(hp\). Invertible affine
reparameterization to the two chosen endpoints preserves this common
agreement and the threshold-list counts.

## What increasing \(h\) changes

For a fixed retained fraction \(c=m/N\in(0,1)\), the exact ledger gives

\[
 n\sim(1+c)hp^2,\quad k=h+1,\quad
 T\sim hp\sqrt{1+c},\quad A_{\rm common}=hp.
\]

When \(h=o(p)\), the endpoint upper bound \(hp+h^2\) differs from
\(hp\) by \(o(hp)\). The endpoint and common loss ratios therefore tend to

\[
 \frac{T-A}{T-k}\longrightarrow 1-\frac1{\sqrt{1+c}}.
\tag{6}
\]

The rate remains \(\Theta(p^{-2})\), even though the dimension grows.
The capacity margin \((T-k)/n\), and both the endpoint and common
fractional losses, remain \(\Theta(p^{-1})\). The label count is still
\(\Theta(p^3)\), independent of \(h\). Thus its ratio to length is
\(\Theta(p/h)\); superlinear inherited counts require \(h=o(p)\).
If \(h=p^{\alpha+o(1)}\), their exponent becomes
\(3/(2+\alpha)\), not \(3/2\).

At leading order, placing the core agreement \(hp\) above the
first-order curve requires

\[
 c<\frac{h-1}{h+1}.
\tag{7}
\]

This is the positive effect of growing \(h\): (7) permits \(c\to1\).
It does not raise rate. For example take \(h\to\infty\),
\(c=1-2/\sqrt h\), and \(p\gg h^4\).
The leading term in (3) is below \(hp\) by
\(\Theta(p\sqrt h)\), and the correction is \(O(h\sqrt p)\).
All of (1)--(3) hold eventually: the retention parameter
\(\gamma\to2-\sqrt2>0\), the union-bound exponent is \(\Theta(hp)\),
and \(T-hp-h^2\sim(\sqrt2-1)hp\).
Consequently

\[
 \frac{T-A_{\rm source}}{T-k}\longrightarrow1-\frac1{\sqrt2},
 \qquad
 \frac{T-A_{\rm common}}{T-k}\longrightarrow1-\frac1{\sqrt2}.
\tag{8}
\]

Here \(A_{\rm source}\) denotes either actual endpoint agreement;
its interval bounds have the same limit. Both sources remain above
the first-order curve and below the tested threshold, and the threshold
approaches Johnson from below.

This regime exists unconditionally, without assuming conveniently sized
divisors for every prime. Let \(h_a=5^a\), choose a square root of \(-1\)
modulo \(h_a\), and use Dirichlet's theorem to select a prime
\(p_a>h_a^{a+4}\) in that residue class. The primes can be chosen increasing.
Then \(h_a\mid p_a^2+1\), \(h_a=p_a^{o(1)}\), and

\[
 n=p_a^{2+o(1)},\quad k=h_a+1\to\infty,\quad
 \#\{\text{singleton labels}\}=n^{3/2-o(1)}.
\]

There is no effective moderate-size prime bound asserted here. In
particular this sequence retains rate \(n^{-1+o(1)}\), rather than a
positive rate.

The separately audited enlargement to degree \(D\) obeys the same
branch argument whenever
\(D<hp\) and \(\max(h-1,D-h)<Q/h\), giving noncanonical agreement at most
\(hp+hD\). Choosing \(D=\Theta(p)\) can retain a positive relative gap
with an appropriate small constant, but its rate is
\(\Theta(1/(hp))\), worse as \(h\) grows. Moreover a canonical-scale
threshold has
\(T/\sqrt{(D+1)n}=\Theta(\sqrt{h/p})\to0\) for \(h=o(p)\).
This enlargement cannot supply the above-first-order placement just proved.
These are limitations of this lift and these witness bounds, not a
universal exclusion of other constructions.

## One exact finite parameter certificate

[verify_higher_power_babybear.py](verify_higher_power_babybear.py) and
[its receipt](verify_higher_power_babybear.json) verify all finite
hypotheses for \(p=2013265921\), \(h=12241\), and \(m=\lfloor54N/55\rfloor\).
The code is over \(E=\mathbb F_{p^4}\), with

| Quantity | Exact value |
|---|---:|
| Length \(n\) | 98329309808423281932846 |
| Dimension \(k\) | 12242 |
| Common agreement \(hp\) | 24644388138961 |
| Endpoint agreement upper bound | 24644537981042 |
| Threshold \(T\) | 34693646123820 |
| Singleton labels | 8160249298611705595853537280 |

The certified first-order upper bound is \(24533338196068<hp\);
the concentration exponent exceeds \(63>\log(p(p+1))\).
The guaranteed endpoint loss is more than \(0.28965\) of the
capacity margin. These are explicit parameters for a probabilistically
selected domain, not an enumerated domain. The rate is approximately
\(1.25\cdot10^{-19}\). This is neither a practical-length instance nor
a prescribed NTT-domain or prime-alphabet construction.
