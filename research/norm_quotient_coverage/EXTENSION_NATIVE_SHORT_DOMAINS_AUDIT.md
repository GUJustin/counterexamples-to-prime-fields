# Four exact finite native-alphabet instances

September 18, 2026. **All four finite criteria pass.** Integration source:
`extension_native_short_domains.tex`. The exact replay is
`verify_extension_native_short_domains.py`; its complete integer receipt
is `extension_native_short_domains_verified.json`.

All instances have length 262144 and code dimension 131072. The domain
is an existentially chosen union of multiplicative fibers **inside the
prime field**, while code coefficients and affine labels use the full
stated extension field. No tag list was enumerated. These are not claims
about the prescribed NTT subgroup or its agreement target 139782.

## Uniform population bound

For `E=F_(p^d)`, take a full-degree element `b`, let
`H=(F_p*)^m`, and reserve `a0 in H`. The population is

```
A = {b-a : a in H minus {a0}}
P = (p-1)/m-1
M = p^d-1.
```

For every nontrivial character of E*, the twisted Katz bound on
`E x F_p` is `d sqrt(p)`, uniformly over the base-field twist.
Average over the `m` annihilator characters of H, then remove a0.
The resulting character mean is at most `(d sqrt(p)+1)/P`.
This is the already audited finite-etale estimate, not the unproved
moment hypothesis in the separate practical-subgroup gate.

The script replaces sqrt(p) by an exact integer upper bound:

| Field | Population P | Bias upper bound | Seed size/weight | Completion pairs |
| --- | ---: | --- | --- | ---: |
| Goldilocks degree 3 | 18014398505287679 | 12884901889/P | 247/125 | 4 |
| BabyBear degree 4 | 1966079 | 179481/P | 243/123 | 6 |
| BabyBear degree 5 | 1966079 | 224351/P | 211/107 | 22 |
| KoalaBear degree 6 | 4161535 | 276961/P | 511/257 | 0 |

The final tag counts and weights are `(s,r)=(255,129)` in the first
three cases and `(511,257)` in the last.

## Exact recurrence certificates

Use the proved finite seed/pair lemma with its upper seed polynomial
`(1+epsilon)^s0`. Initial distinctness is bounded by
`a=1-binom(s0,2)/P>0`. Round the initial missing-density bound and each
subsequent recurrence **upward** to denominator `2^512`. The recurrence
is increasing in the nonnegative density, so upward rounding preserves
a rigorous upper bound at every step. All comparisons use exact integers
and rational arithmetic.

The resulting certified bounds are:

| Field | Initial density bound | Final density bound | Final M h_t |
| --- | --- | --- | --- |
| Goldilocks degree 3 | `<2^-50` | `<2^-213` | `<2^-21` |
| BabyBear degree 4 | `<2^-84` | `<2^-125` | `<2^-2` |
| BabyBear degree 5 | `<2^-19` | `<2^-157` | `<2^-2` |
| KoalaBear degree 6 | `<2^-272` | `<2^-272` | `<2^-86` |

The full trace records every dyadic numerator and character-bias bound.
The strict inequality `M h_t<1` proves that no group element is missing.
It is not an estimate from sampled products or characters.

The primes also have exact Proth certificates. The odd factors and
two-adic exponents of `p-1` are `(2^32-1,32)`, `(15,27)`, and `(127,24)`;
bases 7, 11, and 3 respectively have half-power residue -1 modulo p.
In each case the odd factor is smaller than the power of two. For any
prime divisor l of p, that residue forces `2^a | l-1`; hence every
prime divisor exceeds sqrt(p), proving primality.

## Compiler and limits

With `w=m-1`, the exact quotient compiler yields:

| Field | m | Source and common agreement | Every nonzero native label |
| --- | ---: | ---: | ---: |
| Goldilocks degree 3 | 1024 | 132095 | 133119 |
| BabyBear degree 4 | 1024 | 132095 | 133119 |
| BabyBear degree 5 | 1024 | 132095 | 133119 |
| KoalaBear degree 6 | 512 | 131583 | 132095 |

The last column is exact agreement, proved by a monic cleared numerator,
and every witness has degree at most 131071. Both source agreements and
their ordinary common agreement are exact as well. The capacity margins
are `2047/262144` and `1023/262144`; source separations are `1/256` and
`1/512`, respectively.

No Elias comparison is asserted in this receipt: the alphabet is p^d,
and alphabet-q versus characteristic-p comparisons must be distinguished.
No novelty claim follows from the finite criterion alone. The result is
a finite existence theorem on selected domains, with full native label
coverage; it does not supply an explicit domain, the prescribed-domain
139782-agreement target, or a benchmark improvement.
