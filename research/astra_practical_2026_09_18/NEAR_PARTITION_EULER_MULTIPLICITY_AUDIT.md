# Almost-full polynomial fiber pools: Euler multiplicity audit

September 18, 2026. **PASS.** This proves the proposed near-partition
exclusion from `NEAR_POWER_PACKET_MAP_AUDIT.md`. It is a scoped polynomial
map obstruction, not an improvement to the practical agreement/count
benchmark.

**Lemma.** Let `F` have characteristic `p>n`, and suppose

```
X^n−1 = U(X) W(H(X)),
deg U=u,  deg H=e,  deg W=d>=2.
```

Then `0<u<e` is impossible. All factors may be nonmonic. The assertion
holds over the algebraic closure as well as over `F`.

**Proof.** Degree comparison gives `n=u+de`. The polynomial `X^n−1`
is squarefree. Thus `W` is squarefree: a repeated root of `W` would
give repeated roots of `W(H)` over the algebraic closure. Since
`2<=d<n<p`, its derivative has degree `d−1>=1`. Choose a root `beta`
of `W'`, of multiplicity `a>=1`. Squarefreeness gives
`v=W(beta)!=0`. Because all relevant exponents are less than `p`,
`W(Y)−v` has a zero of order exactly `a+1` at `beta`.

Set

```
Q=X^n−1−vU=U(W(H)−v),
E=nQ−XQ'=−n+v(XU'−nU).
```

The leading coefficient of `E` is `v(u−n)lc(U)`, which is nonzero.
Consequently `E` has degree exactly `u`. This resolves the possible
cancellation of its constant term; no claim that the constant term is
nonzero is needed.

Let `xi` be a root of `H−beta` of multiplicity `m_xi`. Then

```
ord_xi Q >= (a+1)m_xi.
```

Any root of `U` there only increases this order. At `xi!=0`, the Euler
expression has order at least `(a+1)m_xi−1`; at `xi=0`, multiplication
of `Q'` by `X` restores the lost order, so the lower bound is
`(a+1)m_xi`. If `H−beta` has `r` distinct roots and `z` of them equal
zero (`z` is zero or one), the sum of these forced multiplicities is

```
(a+1)e−(r−z) >= ae >= e.
```

The nonzero degree-`u` polynomial `E` cannot have this many roots
counted with multiplicity when `u<e`. This proves the lemma.

## Direct NTT-domain consequence

Let `D=mu_n`, and let a degree-`e` polynomial have `M>=2` distinct tags
whose fibers each contain `e` distinct points of `D`. Their fibers are
disjoint. Multiplying their locators and the locator of the remaining
points gives the lemma's identity with `u=n−Me`. Thus

```
0<n−Me<e  is impossible.
```

In particular, if `e` does not divide `n` and `floor(n/e)>=2`, the number
of complete degree-`e` fibers is at most `floor(n/e)−1`.

For the prescribed KoalaBear domain, `n=262144`, `p=2130706433>n`, and
`e=512+s`, `1<=s<=7`, the maximal putative pool has `M=512−s` and
leftover `u=s²<e`. Hence every such degree has at most `511−s` complete
fibers, regardless of the tag set. This excludes the maximal pools for
degrees 513 through 519. It does not exclude the next-smaller pools,
prove concentration bounds for their coefficient signatures, or address
rational maps with denominators.

The strict condition on the leftover is necessary. When `u=0`, ordinary
power maps supply examples. When `u=e`, the factorization
`X^((d+1)e)−1=(X^e−1)(1+X^e+...+X^(de))` supplies examples as well.
