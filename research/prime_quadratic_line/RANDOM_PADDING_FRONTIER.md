# Analytic refinements and the fixed-rate bottleneck

## Audited singleton constant

The manuscript fragment `growing_gap_random_line.tex` now proves singleton
fraction at least 1/e−o(1). Both independent auditors confirmed the fixed-even
Bonferroni argument. No quantitative growing-order moment estimate is used.

## Arbitrarily slowly diverging field/domain ratio

This is a scoped refinement, not a larger leading-order separation.
Let h(p) tend to infinity with log h(p)=o(log log p). Define

    H_p(d) = exp((log p − 2 log(d!))/(2d+1)),

and choose the largest positive integer d with H_p(d)≥2h(p). Set
L=floor((p^d d!)^(1/(2d+1))) and retain the manuscript definitions of t,n.
The function H_p(d) is strictly decreasing: the numerator of the negative
successive log difference is

    2[log p − 2 log(d!) + (2d+1)log(d+1)] > 0.

Stirling gives d~log p/(2 log log p), and the successive log difference is
O((log log p)^2/log p)=o(1) there. Consequently p/n~h(p). All existing
moment estimates still hold, because t/p~1/(2h(p)) tends to zero; d t/p
need not tend to zero. The elementary Sidon core is available eventually
because p/L²~2h(p) tends to infinity. The singleton fraction remains at
least 1/e−o(1), and the gap has the same leading asymptotic as the c=1/2
endpoint. Translating h(p) to h(n) requires regularity, for example
h(p/h(p))/h(p)→1; no such assertion is made for arbitrary irregular h.

## A precise bottleneck for uniform random padding

Consider any fixed bank of L polynomial witnesses, any t fresh coordinates,
and independent fresh word values. Suppose each possible desired value has
probability at most C/p, where C is fixed. At a fixed line parameter, let Y
count bank witnesses gaining at least d fresh matches. A union bound gives

    Pr(Y≥1) ≤ L binom(t,d)(C/p)^d
             ≤ L (e C t/(d p))^d.

This requires no assumptions on the code degree or core incidence pattern.
Thus a constant fraction of qualifying parameters forces

    log L ≥ d log(d p/(e C t)) − O(1).

In the current distinct-value bank architecture L≤p and t≤n≤p. For d≥2,

    Pr(Y≥1) ≤ p(e C n/(d p))^d
             ≤ n(e C/d)^d.

The last inequality uses monotonicity of p^(1−d) and p≥n. Therefore
constant-density bad labels in this architecture require

    d ≤ (1+o(1)) log n / log log n.

In particular a linear-coordinate source separation at fixed rate cannot
come from this uniform independent padding scheme with L≤p and bounded
value-probability inflation. This is not an obstruction to structured
padding, banks larger than the field, nonuniform random laws, or witnesses
outside the specified bank.

## Interpolation further restricts larger banks

Suppose the core has N0 coordinates and each distinct degree-at-most-D bank
polynomial agrees on at least A>D core coordinates. Counting (D+1)-subsets
of matches gives the exact inequality

    L binom(A,D+1) ≤ binom(N0,D+1).

Each subset determines at most one polynomial. In particular L≤2^N0.
For independent fresh sampling with atoms at most C/p and t≤p, the bad
probability is consequently at most

    exp(N0 log 2 − d log d + d log(e C)).

If N0≤n and d=δn for fixed δ>0, this tends to zero superexponentially.
More generally constant density requires d=O(n/log n). Thus even a bank
larger than p cannot produce a fixed relative source separation by this
uniform independent padding mechanism when every incumbent already has
above-degree core agreement. This does not preclude a different mechanism
with A≤D at the core, correlated fresh values, or sharply concentrated laws.

## Concrete larger-bank target and its limitation

To escape the L≤p bottleneck while retaining independent sampling, use a
bank with many coincident evaluations at every fresh coordinate. The endpoint
blacklist then depends on the number of distinct values rather than L.
For a desired gap d, the preceding necessary condition is

    L ≥ exp(d log(d p/(e C t))−O(1)).

At fixed rate and d proportional to n this requires roughly n^(Theta(n))
bank size when p and t are comparable; the preceding interpolation bound
rules this out for A>D. For smaller separation, a useful candidate must simultaneously
have (i) small fresh evaluation alphabets, (ii) dense core agreement for every
bank member, and (iii) a strong nonbank core cap. The quadratic intersection
bank cannot meet (i) with L>p because its distinct-value property is exactly
what enabled its core and moment computations. The next mathematical target
is therefore a bank with controlled repeated evaluation buckets, not another
choice of padding length or Poisson tuning.
