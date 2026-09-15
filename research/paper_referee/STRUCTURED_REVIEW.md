# Independent review of the structured-domain transfer note

Reviewed `research/structured_domains/TRANSFER_LIMITS.md` on September 15,
2026. This review concerns the mathematics in the note; no protocol code or
contest submission was executed.

## Verdict

The three requested claims are correct with the ordinary Reed--Solomon
dimension restriction made explicit. The field-pigeonhole statement bounds
the **numerical lower bound supplied by one certificate**, not the actual
list size. That distinction is essential and is correctly stated in the note.

### 1. The below-Elias field-pigeonhole guarantee is at most three

Assumptions: prime `p > n`, integers `k,m >= 1`, `t=k+m<n`, and
`theta=1-t/n` strictly below the manuscript's characteristic-`p` Elias
radius at rate `k/n`.

The entropy rearrangement is correct:

```text
n H_2(theta) < m log_2(p) + (n-t) log_2(p/(p-1)).
```

Combining this with `binom(n,t) <= 2^(n H_2(theta))` yields

```text
binom(n,t)/p^m < (p/(p-1))^(n-t) < e.
```

For the last strict inequality, use `log(1+x)<x` for `x>0` and
`(n-t)/(p-1)<1`, since `p-1 >= n` and `t>0`. Consequently the ceiling
is at most three. The increasing-branch requirement in the Elias definition
is satisfied: `0<theta<1-1/p` follows from `t>=2` and `p>n`.

The constant three is deliberately crude; this review does not claim that
it is attained or optimal. This is still a useful negative result about the
certificate because it holds for every evaluation domain under the stated
parameters. It does not prohibit concentration, large coefficient fibers,
other counting arguments, or large true lists.

**Recommended wording:** say “the lower bound certified by the bare
`p^m` class count is at most three,” rather than “pigeonholing cannot give
large lists.” The latter could include more informative partitions or
nonuniform signature counts that the calculation does not address.

### 2. No affine interval can equal a proper subgroup coset

The lemma and proof are correct as written. A proper subgroup with
`n>=3` has `3<=n<=(p-1)/2`, forcing `p>=7`. The first two power sums
of a coset vanish because its character exponents `1,2` are not divisible
by `n`. After centering the interval, its second power sum is

```text
b^2 n(n-1)(n+1)/12.
```

Every factor in the numerator is nonzero modulo `p`, and `12` is
invertible. This gives the contradiction. The exceptions `n<=2` and
the full group are necessary. The note appropriately does not infer an
obstruction to arbitrary generalized Reed--Solomon equivalences or
projective changes of coordinates.

The Prouhet example also checks out. Its characteristic-greater-than-order
hypothesis is stronger than the product argument needs, but harmless. Its
conclusion concerns moment signatures of the exponents, not all possible
subgroup coefficient certificates. The Newton-series degree argument is
correct for the displayed ordering.

### 3. Complete-fiber transfer and the exact dimension

The rate-preserving ambient dimension is `dk`, but the compositions fit
the smaller dimension

```text
k' = d(k-1)+1.
```

At length `dN`, the smaller dimension reduces the rate and increases the
gap, respectively, by

```text
(dk-k')/(dN) = (d-1)/(dN).
```

The witness list and agreement sets are unchanged by choosing this smaller
ambient code. In particular, this is an ambient-code refinement, not an
increase in the number of witnesses. The original paper's lift should
retain dimension `dk` wherever preserving its prescribed rate is essential.

**Required small hypothesis patch:** In the general pullback lemma, add
`1 <= k <= N` and `0 <= t <= N`, where `N=|D|`. The proof says that
surjectivity preserves distinct evaluation words, whereas the premise
currently asserts only distinct polynomials. Without `k<=N`, distinct
polynomials can have identical evaluations on `D`. For example, `D={0}`,
`k=2`, and polynomials `0,X` give only one codeword. Alternatively state
the premise directly for distinct codewords, but the dimension restriction
is clearer and matches the claimed code rate.

Suggested opening:

```text
Let phi in F[X] have degree d >= 1. Let D',D be finite nonempty
evaluation sets such that phi maps D' onto D and every fiber has
exactly d points. Put N=|D|, and assume 1<=k<=N and 0<=t<=N.
```

The subgroup power-map specialization and the coset-image formula are
correct. They show why the existing variable-prime interval lift does
not itself supply a certificate on a prescribed subgroup.

## Placement in the manuscript

**Main text:** one compact paragraph after the discussion of interval
certificate transfer should make two points: (i) a power-map pullback from
a subgroup requires a certificate on its quotient subgroup; (ii) the bare
field-sized coefficient partition supplies at most three witnesses below
Elias, so useful transfer requires additional coefficient-signature structure.
The second point warrants a short displayed calculation or a proposition
if the paper wants to emphasize the limitation. It strengthens the paper's
explanation of the unresolved prescribed-domain problem without implying
a new contest result.

**Appendix or research note:** keep the affine-interval obstruction,
Prouhet example, Newton interpolation calculation, and Fourier identity
here unless a main-text argument explicitly relies on them. They are
correct diagnostics, but introducing all four into the main narrative
would distract from the headline coding results.

**Dimension refinement:** a sentence or footnote in the existing lift
lemma is enough: the witnesses fit dimension `d(k-1)+1`, while dimension
`dk` is used to keep the stated rate exactly fixed. Do not replace the
rate-preserving dimension throughout the fixed-rate theorem.

The Fourier identity is correct by orthogonality and Parseval. Its
nonzero-frequency contribution is a precise missing statistic, not an
established positive lower bound of a useful size. It belongs in the
research note or a brief open-question formulation.
