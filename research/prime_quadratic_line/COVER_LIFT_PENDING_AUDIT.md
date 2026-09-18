# Correlated cover candidate: root parameter analysis

Status: PASS after two independent audits; see CORRELATED_COVER_INDEPENDENT_AUDIT.md and the coding audit in the Astra strategy folder. Source is the completed external
Astra response `strategy_breakthrough_finish_finish.answer.md`. Do not treat
its self-description as verification.

For L=floor(p^(1/3)), 2s dividing p−1, and s at most L/100, the proposed
construction has

- dimension k=2s+1;
- length n=s(2L²−2L+1);
- exact endpoint and common agreement A=2s(L−1);
- threshold T=s(2L−1), gap d=s;
- at least (1/e−o(1))p singleton exceptional challenges;
- exact identity (k−1)n−T²=s².

The union bound over nonbank polynomial/label pairs is
p^(2s+2) binom(L²−L+1,L−1) (s/(p−2L))^(L−1).
For s=Theta(L^b), fixed 0<b<1, its logarithm is at most
[6s+(b−2+o(1))L] log L, and thus tends to minus infinity.
The endpoint b=1 also works with s≤L/100.

The arithmetic audit provides such prime/divisor pairs. Let
alpha=b/(b+2). Then

d=Theta(n^alpha), k=Theta(n^alpha),
p=Theta(n^(3(1−alpha)/2)), 0<alpha≤1/3.

For alpha<1/3, this combines a polynomial absolute source gap with a
superlinear exceptional count. For example alpha=1/5 gives gap n^(1/5)
and count n^(6/5). At alpha=1/3 the exceptional count is only linear.

Scope caveat: this is a covering construction. The normalized source gap
is still 1/(2L²−2L+1) and the code rate is asymptotic to 1/L². The gap
relative to the agreement threshold is 1/(2L−1). All these quantities
vanish. Merely enlarging absolute parameters is not fixed-rate tightness.

Potential restricted sharpness: the independently audited conic-bank bound
M≤2n(n−1)/((T−k+1)d) is asymptotic to 4L³ for these parameters,
whereas the candidate gives M≥(1/e−o(1))L³. Thus it would attain that
restricted counting bound up to a constant. This does not establish
sharpness of the Dao–Kominers–Thaler bounds for arbitrary RS lines.
