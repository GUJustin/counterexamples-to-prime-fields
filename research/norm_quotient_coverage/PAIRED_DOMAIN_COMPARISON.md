# Paired-domain versus prime random-fiber comparison

**Historical comparison, superseded in part on September 18.** The table
below audits the original Cauchy-only proof with C>64. The subsequent
`fixed_weight_completion.tex`, independently audited in
`NONUNIFORM_SEED_PAIR_COMPLETION_INDEPENDENT_AUDIT.md` and
`ENTROPY_COMPILER_ELIAS_PRIOR_ADDENDUM.md`, replaces that restriction by
C>1/h(rho). Choosing C<2/h(rho) retains the strictly below-Elias radius
with polynomial prime alphabet. A separate cleared-denominator root
count also proves exact agreement T at every interior mixture. Thus
the old above-Elias and non-exact-profile limitations below no longer
apply to the strengthened theorem. The older paired theorem still has
additional affine-space, disjoint-list, and prime-quantifier guarantees.
KKH already has polynomial prime alphabets and below-Elias inverse-log
gaps; the new comparison concerns all interior labels and both far endpoints.

September 18, 2026. Read-only manuscript comparison. No main-paper edits.

**Verdict:** the paper's paired-domain construction already gives two
quantitatively far inputs with all `p-2` non-endpoint mixtures nearby.
The new random-fiber theorem must not be presented as the first such
construction, even within this manuscript. Its gain is the polynomial
alphabet versus length relation and the associated inverse-logarithmic
gap in **block length**. Its present constants lose the paired theorem's
strict-below-Elias regime and several exact-profile guarantees.

## Active primary statements inspected

* `paper.tex`, current context paragraph beginning “Krachun, Kazanin,
  and Haboeck,” around lines 691--704.
* `research/paired_domain_warp/completion.tex`, active Corollary
  `pd:full-gap`, with exact profile `pd:exact-profile`.
* `research/paired_domain_warp/far_inputs.tex`, Corollary
  `pd:two-far-inputs` and the batching extensions.
* `research/norm_quotient_coverage/prime_random_fiber_log_gap.tex`,
  Theorem `thm:prime-random-fiber-log-gap`.

The older `single_pair.tex` and `previous_growing_r.tex` are not the
active strongest paired theorem. The comparison below uses completion.

## Exact ledgers at fixed rate

Write `h(rho)=-rho log(rho)-(1-rho)log(1-rho)`, using natural logs.

| Parameter | Existing paired two-far corollary | New prime random-fiber theorem |
|---|---|---|
| Prime quantifier | every sufficiently large prime | infinitely many progression primes |
| Dimension | `K=rho n`, exact rational rate | `J=floor(rho n)` |
| Auxiliary parameters | even `r>=2`, `b=log2 p`, `H=H2(rho)`, `r log b=o(b)` | fixed `beta>12/5`, `p=Theta(m^beta)`, `s=ceil(C log p)`, `C>max(64,4/[rho(1-rho)])` |
| Length | `n=((2r+4/5)b)/H+O_rho(1)` | `n=(s+1)m` |
| Nearby agreement threshold | `T=K+2r+1` | `T=J+2m-1` |
| Both endpoint agreements | exactly `K+r+1` | exactly `J+m-1` |
| Capacity margin | `(2r+1)/n` | `(2m-1)/n` |
| Endpoint gap above nearby radius | `r/n` | `m/n` |
| Endpoint gap / capacity margin | `r/(2r+1)`, tends to `1/2` from below | `m/(2m-1)`, tends to `1/2` from above |
| Non-endpoint affine mixtures | exactly `p-2`, each at **exactly** the tested distance | exactly `p-2` qualify; their distance is **at most** the threshold |
| Domain | selected coordinate pairs, with completion core | selected union of `m`-point multiplicative cosets |
| Elias regime | strictly below Elias | asymptotically **above** Elias under the displayed constant |

The paired corollary does not assert that the ordinary common agreement
of its reparameterized two-endpoint pair equals the individual endpoint
agreement; no such extra identity is assumed in this table. Its underlying
one-far line has common agreement exactly `K+1` (the reference locator
roots are common, and its far word has agreement `K+1`). The new theorem
proves the separate exact identity `CA_J(f,g)=J+m-1`.

## Which gap improves, and which comparisons are unmatched

For fixed even `r`, the paired result has `n=Theta(log p)`, hence
`p=exp(Theta(n))`, capacity margin `Theta(1/n)`, and endpoint gap
`Theta(1/n)`. Its frequently used growing choice `r=floor(log2 b)`
gives `n=Theta(b log b)`, `p=exp(Theta(n/log n))`, and gaps of order
`log n/n`. Throughout the permitted growing range, the alphabet is
superpolynomial in `n`: polynomial `p` would make `b=O(log n)`, while
`n=Theta(r b)=o(b^2/log b)`, a contradiction for growing `n`.

The new result has

```
p = Theta((n/log n)^beta), beta>12/5
capacity margin = Theta(1/log n)
endpoint gap = Theta(1/log n).
```

Thus it improves these gap scales **as functions of block length while
using a polynomial alphabet**. This is not a simultaneous comparison
at the same `n,p`: the two stated families have incompatible field/length
relations. At a fixed field size `p`, both have gaps of order `1/log p`,
and the new certified constants are smaller. For growing `r`, the old
paired margin times `log p` tends to `h(rho)`, and its endpoint gap
times `log p` tends to `h(rho)/2`; the new limits are `2/C` and `1/C`.

The old result also retains an exact `r`-dimensional distance profile,
pairwise disjoint nearby lists, a line with one point only one coordinate
short of maximal distance, and general fixed-size batching. None of
those stronger profiles follows from the new two-source theorem.

## The Elias distinction is decisive

For fixed rate and large prime alphabet,

```
H_p(1-rho-eta)
 = 1-rho-eta + h(rho)/log p + o(1/log p).
```

The new theorem has `eta log p -> 2/C`. Its required constant satisfies

```
2/C < rho(1-rho)/2 < h(rho).
```

The second strict inequality follows, for example, from
`-log x >= 1-x`, which gives `h(rho)>=2rho(1-rho)`.
Consequently `H_p(1-rho-eta)>1-rho` eventually: the tested radius
is **above** the Elias radius. This is not a matter of omitted finite
rounding; the constant gap is strict. The paired construction explicitly
chooses its constants on the other side and remains below Elias.

The new result therefore removes polynomial-size alphabets from the list
of features absent from the paper's complete-coverage constructions,
but it does not remove the below-Elias qualification from the comparison.
KKH's subgroup domain remains a distinct feature. Their below-Elias
specializations should also remain distinct from the present random-fiber
constant regime.

## Crites--Stewart and the interval-list theorem

There is no immediate subsumption of the below-Elias interval-list
claim by Crites--Stewart Corollary 1. Its lower hypothesis is

```
n(1-H_p(theta)) + 2 + sqrt(n H_p(theta)-n theta) <= K.
```

It forces `H_p(theta)>1-K/n`; hence that corollary is above Elias.
The interval theorem `im:all-list` explicitly stays strictly below Elias,
and proves `log L=Omega(n)` at
`eta=Theta(1/sqrt(n log n))`, `log p=Theta(sqrt(n log n))`.
All-label line coverage also does not, by itself, count many witnesses
at one received word. The known Borwein--Erdelyi--Kos moment mechanism
is already credited for the interval theorem's asymptotic reciprocal-gap
exponent. This bounded audit establishes no broader new literature claim.

## Proposed one-paragraph replacement for the context paragraph

```tex
Krachun, Kazanin, and Hab\"ock~\cite{kkh} construct large lists and
affine-line obstructions on multiplicative subgroups of prime fields,
with inverse-logarithmic gaps. Our interval construction concerns
interval domains and gives lists larger than every fixed exponential
in the reciprocal gap, strictly below Elias. The paired-domain
Corollary~\ref{pd:two-far-inputs} already gives two quantitatively far
inputs with all $p-2$ non-endpoint mixtures at the tested distance;
its underlying affine-space profile also has an almost maximally far
exception. Theorem~\ref{thm:prime-random-fiber-log-gap} retains the
two-far coverage pattern with a polynomial-size prime alphabet and
gaps of order $1/\log n$, on selected unions of multiplicative cosets,
but its displayed radius is above Elias. Crites--Stewart already give
all affine challenges nearby with a far direction above Elias
\cite[Corollary~1]{crites-stewart2025}. Thus neither prime-field
counterexamples nor the two-far pattern is new here; the subgroup
domains in~\cite{kkh}, the below-Elias paired profiles, and the
polynomial-alphabet fiber profiles retain different guarantees.
```

The sentence introducing the circle examples can remain immediately
after this replacement. No manuscript file was changed by this audit.
