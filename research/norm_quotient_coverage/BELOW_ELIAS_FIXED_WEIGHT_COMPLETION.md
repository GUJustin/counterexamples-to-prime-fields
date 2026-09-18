# Fixed-cardinality completion closes the below-Elias transfer

September 18, 2026. Independent audit passed;
integration source: `fixed_weight_completion.tex`.

The useful literature mechanism is the already cited Erdős--Rényi
random-translate completion, not a stronger direct Cauchy bound and
not an assumption that all fixed-weight subset products are independent.
The paper's existing paired-domain completion already preserves
cardinality by selecting one member from each added pair. Combining
that mechanism with the following scalar second-moment seed reaches
the leading entropy threshold even for our nonuniform population.

## Exact finite lemma

Let `Gamma` be any finite abelian group of order `M`, and let the
uniform distribution on a `P`-element subset `A` have every nontrivial
Fourier coefficient of modulus at most `epsilon`. Choose a seed size
`s0`, seed weight `r0`, and a number `t` of completion pairs. Put

```
L0 = binom(s0,r0)
a = 1-binom(s0,2)/P > 0
F = sum_u binom(r0,u)binom(s0-r0,u)epsilon^(2u)
h0 = (M-1) F/(a L0) <= (M-1)(1+epsilon)^s0/(a L0)
Pj = P-s0-2j
gamma_j = (P epsilon+s0+2j)/Pj
h_(j+1) = (h_j^2+gamma_j^2 h_j)/(1-1/Pj).
```

Assume `0<r0<s0` and `s0+2t<=P`. If `M h_t<1`, there is a set of
exactly `s0+2t` distinct population elements whose products of exactly
`r0+t` elements cover all of `Gamma`.

Seed proof: draw `s0` elements independently, allowing repetitions.
For two `r0`-subsets with `u` indices on each side of their symmetric
difference, collision probability is

```
(1/M) sum_chi |mu_hat(chi)|^(2u)
 <= 1/M + (1-1/M)epsilon^(2u).
```

This only factors over the independent **seed draws** after common
indices cancel. It makes no independence claim for the subset products.
There are `binom(r0,u)binom(s0-r0,u)` partners of each type for each
support. The normalized energy excess
`Delta=M*energy/L0^2-1` is nonnegative pointwise and has expectation
at most `(M-1)F/L0`. Conditioning distinct draws therefore costs only
division by `a`, with **no additive conditioning error**. Cauchy--Schwarz
then gives a distinct seed with missing fraction at most `h0`.

Completion proof: after any history, deletion of `s0+2j` values gives
the uniform bound `gamma_j` on the remaining distribution. If the
current missing set is `B` of density `h`, two independent new values
`u,v` satisfy

```
E[|Bu intersection Bv|/M]
 = sum_chi |hat(1_B)(chi)|^2 |hat(mu_remaining)(chi)|^2
 <= h^2 + gamma_j^2(h-h^2).
```

Conditioning `u!=v` costs `1/(1-1/Pj)`. A pair attaining the average
exists. Union the two translated represented sets, choosing exactly
one value from the pair. This preserves fixed cardinality and yields
the recurrence. Integer missing count turns `M h_t<1` into full coverage.

## Asymptotic threshold and prime transfer

If `P>=M^alpha`, `epsilon<=M^-kappa` for fixed positive `alpha,kappa`,
then for every fixed `rho in (0,1)` and every

```
C > 1/h(rho), h(rho)=-rho log rho-(1-rho)log(1-rho),
```

one can take any integer total size `s=C log M+O(1)` and any `r/s->rho`.
Choose a constant `t`, seed size `s0=s-2t`, and seed weight `r0=r-t`.
Stirling gives `L0=M^(C h(rho)+o(1))`, so `h0` is polynomially small.
The remaining Fourier bias remains polynomially small after deleting
`O(log M)` elements. A sufficiently large **constant** number of
completion pairs makes the missing fraction below `1/M`.
The `.tex` file supplies explicit choices of exponent and constant `t`.
The necessary counting bound `binom(s,r)>=M` gives `C>=1/h(rho)`,
so the leading constant is optimal for the stated populations.

For the prime-field population already audited,

```
M=p-1
H=(F_p*)^m, p=Theta(m^beta), beta>12/5
A={b-a:a in H\{a0}}, b in F_p*\H
P=(p-1)/m-1 = p^(1-1/beta+o(1))
epsilon <= (sqrt(p)+1)/P = p^(-(1/2-1/beta)+o(1)).
```

Both required exponents are positive. Thus the exact-rate prime
compiler can replace its old `C>64` restriction by **any**
`C>1/h(rho)`, after reserving a constant number of paired alternatives
inside the same total `s` tags. Nothing else in its degree, domain,
source/common agreement, or challenge-count ledger changes.

Choose

```
1/h(rho) < C < 2/h(rho).
```

With `n=(s+1)m`, `J=floor(rho n)`, the exact sources/common agreement
remain `J+m-1`, and every nonzero label has agreement exactly
`T=J+2m-1`.
Now the capacity margin satisfies `eta log p -> 2/C > h(rho)`.
Consequently the tested radius is **strictly below Elias**.
The alphabet remains prime and polynomial in length:
`p=Theta((n/log n)^beta)`, with `p/J->infinity`.

The audited lemma is now included before the prime-fiber theorem in
`prime_random_fiber_log_gap.tex`; that theorem uses `C>1/h(rho)` and
states the strict below-Elias range. Its separate finite Cauchy route
and existing 1420-tag fixture remain valid sufficient constructions.
That fixture is above Elias; this asymptotic argument alone certifies
no finite below-Elias instance.

For the exact upper bound, use `Y=X^m`, the monic core locator `R`
of degree `w`, and `J-1=(r-2)m+w`. For any `deg h<J`,

```
(Y-b)(f+lambda g-h)
  = R(Y^r-b^r-lambda) - (Y-b)h.
```

The first term is monic of degree `w+rm=T`; the second has degree at
most `J+m-1<T`. Since `Y-b` has no domain root, every agreement is
at most `T`. The existing witnesses attain `T` for each nonzero
`lambda`. This also upgrades the existing finite fixture's nonzero
agreement claim from a lower bound to equality.

## Primary literature checked

* Erdős--Rényi, *Probabilistic methods in group theory* (1965),
  Theorem 2, [primary PDF](https://renyi.hu/~p_erdos/1965-15.pdf).
  It completes dense random subset-sum images by extra translates;
  its stated theorem allows all cardinalities. The fixed-weight paired
  alternative modification is already used in this manuscript's
  `paired_domain_warp/completion.tex`.
* Ma--Tang, *An Erdős problem on random subset sums in finite abelian
  groups* (2026), [primary text](https://arxiv.org/html/2602.05768v1).
  It concerns the second-order unrestricted-subset coverage threshold.
  It does not directly give the required fixed-cardinality or nonuniform
  population statement. No such direct application is asserted here.

The present proof avoids both that mismatch and the fourth-moment
rank/Boolean-parallelogram issues by completing a dense seed image.
