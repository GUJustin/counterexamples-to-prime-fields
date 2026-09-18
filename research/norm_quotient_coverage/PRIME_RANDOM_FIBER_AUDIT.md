# Prime-alphabet transfer of the random-fiber compiler

**Update: the Cauchy-only parameter restriction below is superseded.**
The independently audited seed-and-pair completion in
`fixed_weight_completion.tex` permits every C>1/h(rho). For
1/h(rho)<C<2/h(rho), the strengthened theorem is strictly below Elias.
The Jacobi population estimate and exact compiler audited here are
unchanged. The cleared residual has degree T=J+2m-1 for every witness,
so every nonzero pencil label has exactly T agreements. See
`ENTROPY_COMPILER_ELIAS_PRIOR_ADDENDUM.md` for the exact comparison,
including KKH's existing below-Elias result. The finite Cauchy criteria
and the published F65537 fixture remain valid independent sufficient
certificates; they are not finite below-Elias certificates.

September 18, 2026. **PASS.** Integration candidate:
`prime_random_fiber_log_gap.tex`. This uses the prime-progression input
already used in Krachun--Kazanin--Haboeck and otherwise reuses the
audited random-tag and quotient arguments. No novelty claim is made.

## Character estimate

Let `p` be prime, `m>=2` divide `p-1`, `H=(F_p*)^m`, and
`L=|H|=(p-1)/m`. Choose `b in F_p* \ H`. For every nontrivial
multiplicative character `chi` of `F_p*`,

```
sum_(a in H) chi(b-a)
  = (1/m) sum_(psi trivial on H) chi(b) psi(b) J(psi,chi).
```

There are exactly `m` twists. All characters, including the trivial
character, are extended by zero at zero. If `psi=1`, the Jacobi sum
is `-1`. If `psi chi=1`, its modulus is `1`. Otherwise its modulus
is `sqrt(p)`. Therefore the whole subgroup sum has modulus at most
`sqrt(p)`; no nontrivial `chi` is excepted.

Reserve `a0 in H`. The remaining population has size `L-1` and
character-mean modulus at most `(sqrt(p)+1)/(L-1)`.
The no-replacement concentration **argument** from the existing lemma
applies to this arbitrary bounded population. Its literal statement,
which assumes an extension field and tags from `F_p` minus a small
excluded set, is not the statement being invoked here.

## Exact finite compiler

Choose a uniform `s`-subset `G` of `H \ {a0}`. Put

```
D = {x in F_p : x^m in G union {a0}}
n = (s+1)m
J = floor(rho n)
J-1 = (r-2)m+w, 0<=w<m
theta = r/s.
```

The finite conditions

```
s < L-1, 2 <= r < s
(sqrt(p)+1)/(L-1) <= 1/4
4(p-2) exp(-s/64) < 1
(p-2)(s+1) exp(-theta(1-theta)s/2) < 1
```

guarantee some single `G` for which all `r`-subset products of
`{b-a : a in G}` cover `F_p*`. The first exponential condition gives
the simultaneous character bound `s/2`; the second is the Cauchy
fixed-cardinality criterion.

Take a core of `w` points in `x^m=a0`, with locator `R`, and define

```
Y=X^m
f=R (Y^r-b^r)/(Y-b)
g=-R/(Y-b).
```

All coefficients and all values lie in the **prime field**. The
denominator is root-free on the entire prime field: its nonzero image
is `H`, while zero maps to zero and `b` lies in neither.
The same polynomial degree and interpolation arguments prove

```
agr_J(f)=agr_J(g)=CA_J(f,g)=J+m-1
agr_J(f+lambda g)>=J+2m-1 for every lambda in F_p*.
```

Zero is a far affine label, and the projective direction is also far.
The affine line through `f,g` has exactly `p-2` nearby mixtures.
No distinct-witness claim is used.

## Prime sequence and parameter ledger

Fix `beta>12/5`. The prime-selection input in Krachun--Kazanin--Haboeck,
Theorem 1 / Appendix A, gives infinitely many powers of two `m` and
primes `p=1 mod m`, `p=Theta(m^beta)`. The label-injection restriction
`beta>tau+1` from their different counting argument is not needed;
alternatively invoke their stated theorem with `tau=1`, which already
permits every `beta>12/5` and supplies the desired prime sequence.

Then

```
L/sqrt(p) = Theta(m^(beta/2-1)) -> infinity.
```

The character mean tends to zero because `beta>2`. For fixed rate
`rho`, choose `C>max(64,4/[rho(1-rho)])` and `s=ceil(C log p)`.
All finite conditions hold eventually, with `theta->rho`. Consequently

```
n = Theta(m log m)
p = Theta((n/log n)^beta)
p/J -> infinity
capacity margin = (2m-1)/n = 2/(s+1)-1/n = Theta(1/log n)
source gap = m/n = 1/(s+1) = Theta(1/log n).
```

Thus the extension-alphabet and small-characteristic restrictions of
the norm specialization are removed. The remaining domain restriction
is substantive: this is a chosen union of `m`-point multiplicative
cosets, usually not one subgroup and not a prescribed domain. It also
does not obtain a fixed positive gap at fixed rate.

Crites--Stewart already supplies all nearby affine labels with one far
projective direction for arbitrary eligible domains in this regime.
The recorded feature here is a structured two-far construction with
the exact individual/common agreement profile. Its priority is not
established by this audit.

## Comparison correction after checking the active paired theorem

The existing manuscript already proves the two-far pattern in
`pd:two-far-inputs`; this is not a new feature within the paper.
`PAIRED_DOMAIN_COMPARISON.md` gives the exact ledger and a replacement
related-work paragraph. The random-fiber result changes the alphabet/
length relation to polynomial size and gives inverse-logarithmic gaps
in block length. However, its current constant `C` forces the tested
radius above Elias, whereas the existing paired construction is strictly
below Elias and has a stronger exact affine-space profile. These are
distinct tradeoffs, not a componentwise improvement.
