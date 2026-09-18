# Exact all-label counting frontier of the reserved-fiber compiler

September 18, 2026. Exact necessary counting bounds. This is a ceiling
for the stated compiler, not a universal Reed--Solomon obstruction.

At `n=262144`, `J=131072`, the largest counting-permitted fiber size is
**m=1024 for all four native alphabets**. Goldilocks degree three and
BabyBear degrees four and five already have finite certificates at this
model's maximal capacity margin, `2047/262144`. KoalaBear degree six
has a certificate at `1023/262144`; counting permits at most
`2047/262144`, but does not prove coverage there.

## Model and optimization over r,w

Use the selected domain `D=(X^m)^-1(G union {a0})`, with one reserved
full fiber, `|G|=s`, and

```
n=(s+1)m,
0<=w<m,
2<=r<=s,
w+(r-2)m <= J-1.
```

An r-subset S supplies exactly one label, `lambda=-V_S(b)`. Therefore
covering every nonzero native label requires

```
q-1 <= binom(s,r),                  q=p^d.
```

This is necessary even if all subset products were optimally distributed.
Changing r or w means choosing another fixed compiler; it does not permit
summing label banks belonging to different received lines.

The agreement is `T=rm+w`, so the degree constraint gives

```
T <= J+2m-1,
eta=(T-J)/n <= (2m-1)/n.
```

The verifier optimizes all r,w, including unsaturated degree choices.
For fixed m and r, choose
`w=min(m-1,J-1-(r-2)m)`. Agreement increases with r, so the largest
counting-permitted r gives the optimum. At the maximizing m=1024,
the optimum is `s=255,r=129,w=1023`, and `T=133119`.

## Exact discrete obstruction at the next fiber size

Every divisor of n is a power of two, and every such divisor also divides
each of the three primes minus one. Thus there are no intermediate
compatible fiber sizes between 1024 and 2048.

At `m=2048`, only `s=127` nonreserved tags remain. Even the largest
binomial coefficient fails for the smallest native alphabet:

```
binom(127,63) < 2013265921^4-1.
```

The right side is BabyBear degree four; all three other q-1 values are
larger. Larger m only reduce s and its central binomial coefficient.
Consequently no r,w can satisfy the necessary count for m>=2048.
Conversely, `binom(255,129)>=q-1` holds in all four cases, so m=1024
is genuinely permitted by counting (not automatically by distribution).

| Native alphabet | Current certified margin | Counting ceiling | Remaining possible numerator gain |
| --- | --- | --- | ---: |
| Goldilocks degree 3 | 2047/262144 | 2047/262144 | 0 |
| BabyBear degree 4 | 2047/262144 | 2047/262144 | 0 |
| BabyBear degree 5 | 2047/262144 | 2047/262144 | 0 |
| KoalaBear degree 6 | 1023/262144 | 2047/262144 | 1024 |

For BabyBear degree four, the next central binomial is about 0.72894
times q-1; the exact integer comparison is recorded. This small margin
is why using the full binomial, rather than just `2^s`, matters here.

## Analytical ceiling

The elementary necessary count implies

```
q-1 <= binom(s,r) <= 2^s,
eta <= (2m-1)/n < 2/(s+1)
    <= 2/[1+log2(q-1)].
```

The last direction follows from `s>=log2(q-1)`.
More sharply, with `theta=r/s` and natural-log binary entropy h,
`log binom(s,r)<=s h(theta)` gives the exact bound

```
eta < 2 h(theta)/log(q-1).
```

At fixed rate rho with positive capacity margin, the degree and agreement
bounds force `r/s=rho+O(1/s)`. Therefore

```
eta <= [2 h(rho)+o(1)]/log q.
```

In particular this all-label one-pole parametrization cannot yield an
asymptotically larger-than-inverse-logarithmic capacity margin when the
native alphabet is polynomial in n. This statement relies on one label
per r-subset; it does not bound different parametrizations or compilers.

## Scope edge: zero core with no reserved tag

If w=0, one may change the model by omitting the reserved tag entirely.
Then `n=sm` instead of `(s+1)m`. For BabyBear degree four, the parameters

```
m=2048, s=128, r=65, w=0
binom(128,65) >= p^4-1
witness degree <=129024 <131072
T=133120, capacity margin=2048/262144
```

pass the necessary count. No coverage proof is supplied for them.
This is only one coordinate above the reserved-fiber margin. The source
f and common agreement are J, while the root-count upper bound for g is
`J+m-1`, so the guaranteed separation of both endpoints is only one
coordinate. This edge case is why the preceding 2047 ceiling must retain
its reserved-full-fiber qualification.

The separately audited M31 degree-five circle compiler has effective
fiber size F=2m and an analogous fixed-core ledger. Its current F=1024
also reaches its counting frontier: even permitting 128 complete fibers
at F=2048 gives at most `2^128<(2^31-1)^5-1` subsets. This comparison
does not identify its symmetric Laurent code with ordinary RS.

`verify_one_pole_counting_ceiling.py` checks all compatible divisors,
optimizes r,w, and saves exact results in
`one_pole_counting_ceiling_verified.json`. Large unnecessary binomial
integers are avoided by stopping a monotone product once it exceeds q-1.
