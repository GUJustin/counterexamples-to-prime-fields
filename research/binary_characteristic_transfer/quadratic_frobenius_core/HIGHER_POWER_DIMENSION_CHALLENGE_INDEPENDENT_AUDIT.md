# Independent audit of the higher-power dimension/count gate

2026-09-19. **PASS** for the finite and asymptotic statements in
`HIGHER_POWER_DIMENSION_CHALLENGE_GATE.md`. No scan, manuscript edit,
or additional geometric assumption is used.

Let the two weighted tag sets have weights `0<=wi(y)<=h`, totals `ni`,
and squared-weight sums `Si`. Suppose a qualifying canonical pair uses
at least `g>h` physical coordinates on each block.

For one block and a line `L`, set

\[
 C(L)=r(L)^2-\sum_{y\in L}w(y)^2
 =\sum_{\substack{y,z\in L\\y\ne z}}w(y)w(z)\ge0.
\]

These are **ordered** distinct-tag pairs. Each such pair determines
exactly one affine prime-plane line, so

\[
 \sum_L C(L)=n_i^2-S_i.
\]

The weight cap gives `sum_(y in L) w(y)²<=h*r(L)`. If `r(L)>=g>h`,
then `r(L)(r(L)−h)>=g(g−h)`, because this function is increasing on
`[g,infinity)`. Contributions of non-rich lines remain nonnegative;
there is no subtraction or sign loss when they are discarded. Thus

\[
 L_i\le\frac{n_i^2-S_i}{g(g-h)}.
\]

In one direction, parallel lines partition the weighted points, giving
at most `floor(ni/g)` rich lines. Pairing same-direction lines between
the two blocks proves exactly

\[
 B\le\min\left\{
 \left\lfloor\frac{n_0}{g}\right\rfloor
       \frac{n_1^2-S_1}{g(g-h)},\quad
 \left\lfloor\frac{n_1}{g}\right\rfloor
       \frac{n_0^2-S_0}{g(g-h)}
 \right\}.
\]

Counting pairs bounds the number of distinct labels even if multiple
pairs give the same label. In particular the multiply represented zero
label causes no undercount. Empty blocks also cause no issue: the
corresponding factor vanishes.

The source-gap premise is valid. The matches of any canonical witness
on one block can be reproduced at any other line parameter by a
constant adjustment to that witness. Therefore a block contribution
never exceeds the agreement of either chosen endpoint. If the total
agreement is at least `T` and the endpoint agreement is at most `T−g`,
the other block must contribute at least `g`; apply this to both blocks.
The same conclusion follows from `T−CA>=g`: on a one-block support,
the explaining source polynomial and the constant indicator polynomial
give simultaneous agreement, so each block contribution is at most CA.

For an explicit asymptotic constant, discard the floors and the
nonnegative `Si`. Writing `n=n0+n1` gives

\[
 B\le\frac{n_0n_1\min(n_0,n_1)}{g^2(g-h)}
 \le\frac{n^3}{8g^2(g-h)}.
\]

If `g>=c*sqrt(h*n)` with fixed `c>0` and `n/h -> infinity`, then
`g>=2h` eventually, and consequently

\[
 B\le\frac{n^3}{4g^3}
 \le\frac{1}{4c^3}\left(\frac nh\right)^{3/2}.
\]

It follows that `B/n -> infinity` requires `h=o(n^(1/3))`. More
quantitatively, `B>=F*n` implies, eventually,

\[
 h\le\frac{n^{1/3}}{4^{2/3}c^2F^{2/3}}.
\]

Since `k=h+1`, the equivalent dimension condition is correct. For full
fibers with comparable tag populations `m`, this is `B=O(m^(3/2))`
and superlinearity over `n=Theta(hm)` requires `h=o(sqrt(m))`.

The primary note correctly retains the necessary scope: `g>h` for the
finite denominator, `n/h -> infinity` for the displayed asymptotic
specialization, canonical paired-line witnesses, and a fixed positive
square-root-scale gap. It makes no universal constant-rate claim and
does not exclude noncanonical witnesses or smaller-gap constructions.
