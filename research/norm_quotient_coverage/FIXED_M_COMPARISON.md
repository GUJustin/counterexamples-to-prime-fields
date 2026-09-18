# Fixed two-point fibers: bounded audit and comparison

September 18, 2026. Audit passes. The separate input-ready statement is
`fixed_m_corollary.tex`; no main-paper edits were made.

For every sufficiently large odd prime, take the squares `H`, a
nonsquare `b`, and one reserved square `a0`. The population
`{b-a : a in H minus {a0}}` has size `(p-3)/2` and every nontrivial
character mean at most `(sqrt(p)+1)/((p-3)/2)`. The audited completion
corollary therefore gives exact-cardinality product coverage with
`s=ceil(C log p)`, for every fixed `C>1/h(rho)`.

The compiler with `m=2` has the exact ledger

```
n = 2(s+1), J = floor(rho n)
source agreements = common agreement = J+1
agreement of f+lambda*g = J+3 for every lambda != 0
capacity margin eta = 3/n
endpoint distance above the tested radius = 2/n = (2/3) eta
all p-2 non-endpoint affine mixtures are exactly at the tested radius.
```

The floor causes no loss: write `J-1=2(r-2)+w`, `w in {0,1}`, and
place the `w` core points in the reserved square fiber. Then `r/s->rho`.
The cleared residual is monic of degree `J+3` for any code polynomial,
so the near-agreement statement is an equality.

The below-Elias interval is nonempty:

```
1/h(rho) < C < 3/(2 h(rho)).
eta log p -> 3/(2C) > h(rho).
```

The alphabet is exponential in length, `log p=n/(2C)+O(1)`. This
all-prime corollary does not retain the polynomial-alphabet benefit
of growing fibers. Its gaps are of order `1/n`, equivalently `1/log p`,
and not of order `1/log n`.

## Comparison with the existing paired two-far statement

Use a different letter `k` for the old even padding count, `k>=2`.
The active statements are `pd:full-gap` in
`research/paired_domain_warp/completion.tex` and `pd:two-far-inputs`
in `far_inputs.tex`. For fixed `k`, their natural-log ledger is

```
n_old = ((2k+4/5)/h(rho)) log p + O_rho(1)
eta_old log p -> a_k = h(rho)(2k+1)/(2k+4/5)
endpoint_loss_old log p -> k h(rho)/(2k+4/5)
endpoint_loss_old/eta_old = k/(2k+1) < 1/2.
```

Both results work over every sufficiently large prime and place every
non-endpoint mixture at exactly the tested distance. The two-point
fiber result has loss ratio exactly `2/3` and proves its ordinary
common agreement exactly. This is a comparison of stated guarantees,
not a priority claim for the two-far pattern or the completion method.

For a matched capacity-margin coefficient at the same prime alphabet,
choose `C=3/(2 a_k)`. Since `h(rho)<a_k<=25 h(rho)/24`, this `C`
lies strictly between `1/h(rho)` and `3/(2 h(rho))`. Then

```
eta_new log p -> a_k = lim eta_old log p
endpoint_loss_new log p -> (2/3) a_k
endpoint_loss_old log p -> [k/(2k+1)] a_k
n_new/n_old -> 3/(2k+1).
```

Thus the endpoint separation improves at matched limiting rate, prime alphabet,
and leading capacity-margin constant. The lengths differ, so this is
not domination at identical `(n,p)`. At identical leading length and
alphabet relation, choosing `C=(2k+4/5)/(2h(rho))` instead makes the
new radius above Elias; no such matched-length improvement is asserted.

The existing paired theorem retains stronger separate features:
an exact multidimensional Hamming-weight profile, disjoint decoding
lists, an almost maximally far point, batching, exact rational rate,
and its stated efficient high-probability sampler. These are not
claimed for the fixed two-point-fiber corollary.
