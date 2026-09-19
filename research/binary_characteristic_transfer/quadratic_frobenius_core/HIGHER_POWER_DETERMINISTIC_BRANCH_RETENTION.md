# Deterministic branch retention for odd higher-power lifts

2026-09-18. **Positive result:** when \(h\) is odd, the retained domain in
[HIGHER_POWER_FULL_FIBER_LIFT.md](HIGHER_POWER_FULL_FIBER_LIFT.md) can be
specified algebraically, with no random subset or concentration argument.
This preserves the growing-\(h\) loss limit and the full singleton-label
bank. It does not reduce length below order \(hp^2\).

## An explicit domain of every desired retained size

Keep the notation of the full-fiber theorem:

\[
 B=\mathbb F_{p^2}\subset E=\mathbb F_{p^4},\quad
 Q=p^2+1,\quad L=p^2-1,\quad h\mid Q,\quad 1<h<Q.
\]

Assume \(h\) is odd, and choose a primitive \(s\in E^*\). Put
\[
 z=s^Q,\qquad \alpha_j=s^{(Q/h)j}\quad(0\le j<h),\qquad
 \eta=s^h.
\]
Thus \(z\) generates \(B^*\), the core is
\(D_0=\coprod_{j=0}^{h-1}\alpha_jB^*\), and its scaled copy is
\(D_1=sD_0\).

For any integer \(0\le m<hL\), write
\[
 m=rL+d,\qquad 0\le r<h,\quad 0\le d<L.
\]
Retain exactly
\[
 D'_1=
 \coprod_{j=0}^{r-1}s\alpha_jB^*
 \ \cup\
 \{s\alpha_rz^t:0\le t<d\}.
\tag{1}
\]
Together with the complete core, this gives the explicitly specified
domain \(D=D_0\cup D'_1\) of length \(n=hL+m\).

The key identity is
\[
 \frac{(s\alpha_j z^t)^h}{\eta}=z^{j+ht}.
\tag{2}
\]
Because \(h\mid p^2+1\) is odd,
\(\gcd(h,p^2-1)=1\). Thus, on each complete fresh branch, (2) runs
bijectively through \(B^*\). Every canonical affine \(p\)-fiber in the
normalized \(y\)-plane therefore has exactly \(p\) fresh matches on that
branch, or \(p-1\) if it passes through \(y=0\). The partial branch adds
nonnegative contributions. Uniformly over every slope and intercept,
all doubly canonical polynomials have at least
\[
 (h+r)(p-1)
\tag{3}
\]
matches in \(D\). The oddness hypothesis matters: for even \(h\),
the power map restricted to an individual \(B\)-line is not a
bijection onto all \(B^*\).

## Exact finite corollary

Define the same two received words as in the full-fiber theorem:
\[
 f=x^{hp},\quad g=0\quad\hbox{on }D_0;\qquad
 f=\eta^{1-p}x^{hp},\quad g=1\quad\hbox{on }D'_1.
\]
Take \(k=h+1\) and
\[
 T=\lfloor\sqrt{hn-1}\rfloor.
\]
It is sufficient that
\[
 h-1<Q/h,\qquad hp+h^2<T\le(h+r)(p-1).
\tag{4}
\]
Then the complete threshold-\(T\) profile is exactly the same:
\((p+1)(p^2-1)\) singleton parameters, one parameter with \(p+1\)
polynomials, and empty lists elsewhere.

Two parameters with empty lists can be used as endpoints. Their nearest
agreements lie in \([hp,hp+h^2]\), and their ordinary common agreement is
exactly \(hp\). The proof is precisely the all-witness branch-separation
and common-agreement proof in the full-fiber note; replacing random
retention by (1) changes only the lower bound on canonical supports.
In particular it does not assume that all witnesses are compositions.
If
\[
 \sqrt{kn/2}+(k^3n/72)^{1/4}<hp
\tag{5}
\]
in the low-rate branch, both endpoint agreements are above first order,
and \(T\) is the largest integer strictly below Johnson.

This also handles arbitrary retained sizes, rather than only unions of
whole branches. The prefix order in (1) is part of the exact construction;
no existence choice remains after the finite field and primitive \(s\)
have been fixed.

## Growing-dimension family

Take odd \(h\to\infty\), \(h\mid p^2+1\), \(p\gg h^4\), and retain
\[
 r=h-\lceil2\sqrt h\rceil
\]
whole fresh branches, with \(d=0\). Then
\[
 n=(h+r)(p^2-1)\sim2hp^2,\qquad
 k=h+1,\qquad T\sim\sqrt2\,hp.
\]
The minimum canonical support is \((h+r)(p-1)\sim2hp\), comfortably
above \(T\). The first-order estimate and all-witness bounds from the
full-fiber note apply. Consequently the common and both endpoint loss
ratios converge to \(1-1/\sqrt2\), approximately \(29.2893\%\).

The schedule \(h=5^a\), with primes \(p>h^{a+4}\) in a square-root-of-\(-1\)
residue class modulo \(h\), supplies the same unconditional infinite
family. Its singleton count is \(n^{3/2-o(1)}\), and its dimension tends
to infinity. The rate is still \(\Theta(p^{-2})\), and the fractional
agreement loss is still \(\Theta(p^{-1})\). Algebraic specification of
the domain is not a rate or practical-parameter improvement.

The prior BabyBear choice \(h=12241\), \(m=\lfloor54hL/55\rfloor\) is
compatible with (1): it retains \(r=12018\) whole fresh branches and a
prefix of the next. Its length and all previously reported numerical
parameters remain unchanged. Only (3), in place of the probabilistic
retention argument, needs checking.

## Scope of the short-domain question

Allow completely arbitrary coordinate retention in both blocks, including
different numbers of roots from different power-map fibers. Write the
resulting nonnegative weights on \(B^*\) as \(w_0,w_1\le h\), with
totals \(n_0,n_1\), and let \(C_a(b),D_a(v)\) be their weighted affine-line
counts. A canonical label has exactly
\[
 C_a(b)+D_a(v)
\tag{6}
\]
matches. For every one slope \(a\),
\[
 \sum_{b,v\in I_a}\big(C_a(b)+D_a(v)\big)=p(n_0+n_1)=pn.
\tag{7}
\]
Thus retaining all \(p^2-1\) nonzero labels in even a single slope plane
at threshold \(T\) requires
\[
 (p^2-1)T\le pn.
\]
If \(T>n a_1(k/n)>\sqrt{kn/2}\), this forces
\[
 n>\frac{k(p^2-1)^2}{2p^2}.
\tag{8}
\]
In particular, thinning either or both blocks cannot retain an entire
canonical slope plane, much less the entire bank, above first order on
\(n=o(hp^2)\). This is an exact averaging bound, with no uniform-sampling
assumption.

Selecting fewer slope planes while keeping only some labels is different.
If \(A\) is an endpoint or common-agreement upper bound and
\(g=T-A>0\), every qualifying pair in (6) must have
\(C_a(b),D_a(v)\ge g\): every single-block line count can already be
attained by a suitable explanation of that endpoint, or by simultaneous
explanations on that block. For a selection of \(J\) slope planes this gives
the exact resource bound
\[
 B_{\rm retained}\le
 J\left\lfloor\frac{n_0}{g}\right\rfloor
  \left\lfloor\frac{n_1}{g}\right\rfloor.
\tag{9}
\]
In the low-rate regime \(g=\Omega(\sqrt{hn})\), superlinear counts thus
require \(J/h\to\infty\); a fixed or \(O(h)\) number of planes does not
suffice.

The sharper weighted variance and paired-moment bounds, independently
checked in
[HIGHER_POWER_SHORT_DOMAIN_MOMENT_AUDIT.md](HIGHER_POWER_SHORT_DOMAIN_MOMENT_AUDIT.md),
give
\[
 B_{\rm retained}=O\!\left(p\sqrt{n/h}\right)
\]
when \(n/h\to\infty\), \(n=o(hp^2)\), and the agreement loss is a fixed
positive fraction of \(T-k\) at an above-first-order threshold.
Therefore \(B_{\rm retained}=\omega(n)\) in this shortened regime
requires \(n=o(p^2/h)\). This leaves a possible smaller-scale range;
it is not a partial-bank impossibility theorem.

No constructive retained point set meeting that remaining range was
identified in this bounded assessment. There is also a separate
all-witness issue: below Johnson on \(n=o(hp^2)\), one has
\(T\le\sqrt{hn}=o(hp)\), whereas the inherited noncanonical bound is
\(hp+h^2\). It gives no source-farness or list-exhaustiveness guarantee
there. A successful short-domain construction must supply both a rich
partial canonical bank and a new agreement bound for all other
degree-\(\le h\) witnesses.
