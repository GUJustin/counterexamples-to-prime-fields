# Independent check of the conditional practical moment gate

September 18, 2026. **PASS for the conditional implication and integer
tests only.** Neither moment hypothesis has been proved or numerically
tested. No literature claim or coding transfer is audited here.

Let `p=2130706433`, `N=262144`, `I=8128`, `q=p^6`, and `r=139782`.
Then `p-1=NI`. Let `D=mu_N`, and let `b` have degree six over F_p.
For a nontrivial character `chi` of `F_q*`, define

```
M_chi(psi) = sum_{a in F_p*} chi(b-a) psi(a)
A_(2k)(chi) = [1/(p-1)] sum_psi |M_chi(psi)/sqrt(p)|^(2k).
```

All factors `b-a` are distinct and nonzero. The moment sum is over
**all** `p-1` base-field multiplicative characters, including the
trivial twist.

## Hölder normalization and exact powers

Orthogonality over the `I` characters trivial on `D` gives
`S_chi=(1/I) sum_{psi in D^perp} M_chi(psi)`. Hölder and positivity
give, with no randomness or equidistribution assumption,

```
|S_chi|^(2k)
 <= (1/I) sum_{psi in D^perp} |M_chi(psi)|^(2k)
 <= [(p-1)/I] p^k A_(2k)(chi)
  = N p^k A_(2k)(chi).
```

An independent integer verifier confirms both strict inequalities

```
130  N p^5 < (N-570)^10,
4182 N p^6 < (N-570)^12.
```

Thus either uniform assumption `A_10(chi)<=130` for every nontrivial
`chi`, or `A_12(chi)<=4182` for every such `chi`, gives the uniform
character bound `|S_chi|<261574=N-570`. The inclusive assumed moment
bounds correctly produce a **strict** character bound.

## Fixed-cardinality coverage

Put `theta=r/N`. For the elementary symmetric character coefficient
`e_r(chi(b-a):a in D)`, the audited Cauchy-circle argument gives

```
|e_r| / binom(N,r)
 <= (N+1) exp[-theta(1-theta)(N-B)].
```

The target group has order `q-1` and exactly `q-2` nontrivial
characters. Fourier inversion therefore gives, for every `z in F_q*`,

```
# {S subset D : |S|=r, product_{a in S}(b-a)=z}
 >= binom(N,r)/(q-1)
    * [1-(q-2)(N+1) exp(-theta(1-theta)*570)].
```

There is no missing factor of `I`, `p-1`, or `q-1` in either step.
The prefactor is exactly `(p^6-2)(N+1)`.

For a separate exponential certificate, the independent verifier uses

```
u=570 r(N-r)/N^2 = 1218660362235/8589934592 > 283/2.
```

It forms the degree-160 Taylor polynomial at the **smaller** argument
`283/2` entirely with integers, using denominator `2^160 * 160!`.
The numerator minus `(q-2)(N+1)` times that denominator is strictly
positive. Hence

```
exp(u) > exp(283/2) > sum_{j=0}^{160} (283/2)^j/j!
       > (q-2)(N+1).
```

The bracket in the count bound is positive. Each target consequently
has at least one product representation by exactly 139782 distinct
factors.

The verifier imports neither the original script nor its receipt and
does not use floating-point transcendental functions. Exact positive
differences and the Taylor certificate are saved in
`practical_subgroup_amplification_independent.json` by
`verify_practical_subgroup_amplification_independent.py`.

This verifies a useful **conditional analytic ingredient**. It does
not establish either uniform moment bound, construct admissible
degree-below-131072 witnesses, or imply a new benchmark result.
