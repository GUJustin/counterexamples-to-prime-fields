# Why the current first-order finite bounds miss the pinned lower track

September 17, 2026. This is a finite arithmetic diagnostic of the current
public ePrint 2026/2056, not a new prize submission, formal verification,
or an optimality theorem. It concerns the **lower track**: certifying safe
proximity for arbitrary words. The fixed-domain counterexample/count route
is the distinct upper track studied in `../better_codes_revisit_2026_09_17`.

## Quantitative result

We independently reproduce the ePrint's attained agreement threshold
A=183210 using its current derivative-weighted support, graded challenge
count, and squarefree regular-family count. We then test the pinned
incumbent threshold A=181284. The best sampled support there misses the
entire permitted numerator budget by a factor greater than1100, from the
regular-family term alone.

| A | multiplicity m | derivative bound | total jet bound | challenge bound | optimized regular term / budget |
|---|---:|---:|---:|---:|---:|
|183210|26|7|36|485|0.9982344391|
|181284|152|47|210|12365|1100.4331189|

Here n=262144, D=131071, p=2130706433, and the budget is
floor(p^6/2^128)=274980728111395087. At the first support, including the
ordinary tail and list gives ratio0.9982532703 and passes the exact rational
inequality. At the second, the ordinary tail costs only0.1166333401 budgets;
the regular term is the obstacle. This reproduces66.15bits, not an
improvement on the pinned68.11bits.

The refinement scan tests3863 supports, varying multiplicity, derivative
cap and total jet cap; its precise finite grids are in refine.py. An
additional initial grid tests570 supports. These are restricted searches,
not a proof that every possible support fails. The characteristic guard
p>max(D,Bpartial) holds for all displayed supports.

## Formulas and independent checks

`finite_scan.py` implements ePrint Eqs61--63 exactly. Its local rank is
recounted by direct summation for all small m<15 and all b<=m. For each
support it finds the first integer challenge height H satisfying the graded
row inequality, rather than the older uniform challenge budget. Degree
truncations are retained.

The regular term is the exact Lemma5.6/Eq55 term, with Eq54 degrees, and
its integer threshold L is optimized. Write N=n-D, C=A-D+1, x=L-D,
lambda=N/(A-D), F=Freg and J=J_1. The term is

    R(x) = lambda J (N+1-x)/(C-x) + F N (N-x)/x.

Its derivative has sign of

    lambda J (n-A) x^2 - F N^2 (C-x)^2.

This expression increases through its unique zero, so binary search plus
adjacent integer checks finds the global integer minimum. The independent
`verify.py` checks **every** allowed L (102352 thresholds total) for the two
reported supports. It also directly recounts their support dimensions and
ranks, and checks every height below the reported H, proving these heights
are minimal within Eq63 for these supports.

For the ordinary tail we use the conservative explicit Eq58 expression;
for the list we use Eq57. Substituting the sharper regular term is valid
because the Eq58 ordinary bound separately bounds the same ordinary tail.
Thus the first row is a complete rational numerical certificate conditional
on the cited ePrint theorems and its scalar-to-interleaved transfer, not just
a regular-part test. The second row fails before those extra costs arise.

The continuum at rate1/2 is a=(1+sqrt(6))/5, corresponding to68.5497759bits
and180852.6078 agreements. This is not a finite certificate. At the pinned
threshold the agreement margin above it is only431.3922 coordinates,
versus2357.3922 at the reproduced certificate. The finite cost is dominated
by the growth in interpolation degree and the required challenge height,
which feed into the joint degree of the regular solution family.

## What this does and does not suggest

Graded heights and the optimized regular threshold are already included;
turning either on again is not a missing improvement. For the displayed
support at the incumbent agreement, no change to its Eq63 height or Eq55
threshold can bridge the gap: both have been exhaustively minimized.
Sharpening only the ordinary tail or fixed-word list also cannot bridge it.

A competitive lower-track result would require different supports/rank
estimates, or a substantially stronger count of regular components. The
current ePrint's Section10.5 explicitly distinguishes later submissions'
whole-kernel, multiple-equation and Taylor-tail arguments from its displayed
single-explainer transfer. This calculation supplies no new such argument.
The new exact-list padding and random-direction counterexamples do not
provide arbitrary-word upper bounds for this fixed benchmark.

Primary source: https://eprint.iacr.org/2026/2056.pdf?download=1,
retrieved locally September17, SHA256
b67c188ec477b6063caf9c1c06b214c71e358ff09b9517adcdb1db212ea2700a.
Formula checks use the cached text in tmp/eprint-2056; no full proof audit
or Lean verification is claimed.
