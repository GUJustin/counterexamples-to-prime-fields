# Logarithmic random norm tags: exact audit

September 18, 2026. Integration candidate: `random_tag_log_gap.tex`.
The construction and independent character audit pass. This combines
known quotienting, Katz's affine-line character estimate, concentration,
and the elementary fixed-cardinality Cauchy lemma. No novelty claim is made.

## Statement and exact-rate ledger

Fix `rho in (0,1)`, fixed degree `d>=2`, and
`C>max(64,4/[rho(1-rho)])`. For every sufficiently large prime `p`, set

```
q = p^d, E = F_q
m = (q-1)/(p-1)
s = ceil(C log q)
n = (s+1)m
J = floor(rho n)
J-1 = (r-2)m+w, 0<=w<m
theta = r/s.
```

Choose `b` of degree exactly `d`, a reserved nonzero norm tag `a0`, and
`G`, an `s`-subset of `F_p* \ {a0}` with the simultaneous character bound
below. The domain is `D=N^-1(G union {a0})`, where `N(X)=X^m`.
The reserved fiber is part of the domain; omitting it would invalidate
the arbitrary-dimension padding.

Take `w` core points inside the reserved fiber and let `R` be their
monic locator. The same compiler gives

```
f = R (N^r-b^r)/(N-b)
g = -R/(N-b)
agr_J(f) = agr_J(g) = CA_J(f,g) = A = J+m-1
agr_J(f+lambda g) >= T = J+2m-1 for every lambda!=0.
```

The nearby labels are exactly `E*` at threshold `T`, since `f` has only
`A<T` agreement. The normalized capacity margin is `2/(s+1)-1/n`;
the normalized source gap is `1/(s+1)`. Both are `Theta(1/log n)`.
The affine line through the two far endpoints `f,g` has exactly `q-2`
nearby points: `(1-t)f+t g` is near for all `t` other than `0,1`.

All degree and source-attainment calculations are unchanged from
`COMPILER_AUDIT.md`; they use selected full fibers and the reserved core,
not evaluation on every point of `E`. The source witnesses interpolate
`r-1` selected tags, substitute `N`, and multiply by `R`; their common
agreement is exactly `(r-1)m+w`. Every nearby residual is
`R V_S(N)/(N-b)`, with disjoint zero sets of size `w+rm`.

## Concentration without replacement

The full population has size `P=p-2`. Katz plus deletion of `0,a0`
gives, for every nontrivial multiplicative character of `E*`,

```
|population mean| <= ((d-1)sqrt(p)+2)/(p-2).
```

Assume this is at most `1/4`. For a uniform `s`-subset `G`, the bound

```
Pr[ |sum_(a in G) chi(b-a)| > s/2 ] <= 4 exp(-s/64)
```

holds. Here is a self-contained finite-population reduction. For one
real coordinate of the character values, reveal a uniformly random
ordering of the sample, let `T_j` be the sum of its first `j` values,
and let `T_all` be the population sum. The Doob martingale is

```
M_j = T_j + (s-j)/(P-j) (T_all-T_j).
M_j-M_(j-1)
  = (P-s)/(P-j) [v_j - (T_all-T_(j-1))/(P-j+1)].
```

Its conditional increment range has width at most `2` for `j<=s<P`.
The exponential Hoeffding bound therefore gives
`Pr[|M_s-M_0|>=u] <= 2 exp(-u^2/(2s))`.
For a complex deviation of size `s/4`, one real coordinate deviates
by at least `s/(4sqrt(2))`; the two-coordinate union bound gives the
claimed `4 exp(-s/64)`. No independence of the sampled coordinates is
assumed. Union over the `q-2` nontrivial characters succeeds if

```
4(q-2) exp(-s/64) < 1.
```

Every resulting `G` has bias at most `s/2`. The Cauchy subset-product
lemma then makes every element of `E*` an exact `r`-subset product if

```
(q-2)(s+1) exp(-theta(1-theta)s/2) < 1.
```

These conditions, `s<p-2`, and `2<=r<s` hold eventually for the stated
fixed `C,rho,d`. In particular the concentration argument is uniform
over *all* multiplicative characters, including small-order characters.

## Exact comparison and limitations

This achieves the inverse-logarithmic capacity margin together with
almost every native affine label and both far sources. Thus the stated
`1/(2n)` lower-bound probability in Krachun--Kazanin--Haboeck Appendix A
is not a ceiling of their quotient mechanism.

This coverage/margin combination is not a new existential guarantee.
The independent primary audit in
`CS_FULL_DOMAIN_EXACT_CA_SUBSUMPTION.md` shows that Crites--Stewart
Corollary 1 already gives **every** affine label at an inverse-logarithmic
margin on arbitrary domains, including `D=E=F_(p^5)`, with prescribed
direction `g=X^J`. Root counting and interpolation then give exactly
`agr(g)=CA(u,g)=J`, subsuming the older d5 theorem's existential native
profile asymptotically. That result makes the first source near. The
norm construction's distinct recorded feature is its two individually
far sources and transparent exact source/common profile; priority for
that feature has not been established. See also
`RANDOM_TAG_PRIOR_WORK_PARETO_AUDIT.md`.

The domain changes: `n=Theta(p^(d-1)log p)`, so

```
p = Theta((n/log n)^(1/(d-1)))
q = Theta((n/log n)^(d/(d-1))).
```

For degree five this is length `Theta(p^4 log p)`, not `p^5`.
The chosen domain need not be a subgroup and is not a prescribed domain.
The alphabet is an extension field and characteristic is below the code
dimension. These distinctions must accompany any comparison to prime-
alphabet results or to the prior full-domain five-dimensional theorem.
At 31-bit characteristic, norm fibers themselves are enormous for
`d>=2`; this does not solve the practical length-`2^18` target.

Padding this construction back to the full `p^d`-point field does not
preserve the inverse-logarithmic margin: the additive source gap remains
one norm fiber, `m`, so normalization by `p^d` returns a `Theta(1/p)`
gap. Thus this result does not settle almost-all coverage at an inverse-
logarithmic margin in the original matched full-domain `n=q=p^5` regime.
This last limitation concerns the norm mechanism alone; the cited
Crites--Stewart corollary already supplies the existential full-domain
guarantee with one far projective direction.
