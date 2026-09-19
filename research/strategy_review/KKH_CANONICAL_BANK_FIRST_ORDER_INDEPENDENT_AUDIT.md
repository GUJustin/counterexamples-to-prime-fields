# KKH canonical subset bank above first order: independent audit

September 18, 2026. **PASS**, including the arbitrary-integer strengthening.
This is a necessary parameter condition for the canonical bank, not a
classification of all witnesses or all exceptional labels on its line.
No other agent's files were edited.

The cached primary KKH Section 4/Appendix A was reread at
`/Users/jthaler/Dropbox/Documents-full-2026-09-16/Documents/stwo_audit_2026-09-15/sources/actual_list_literature/kkh2026_782.txt`,
lines 663--782. Its degree cap `(r−2)m` corresponds to strict code
dimension `k=(r−2)m+1`; the canonical agreement is `T=rm`, and its raw
subset bank has size `binom(s,r)`.

## Audited statement

Let `s>=16`, `m>=1`, and `2<=r<s` be integers, and put

```
n=sm,  k=(r−2)m+1,  rho=k/n,  a=T/n=r/s.
```

If `a>a1(rho)`, then

```
r is one of 2, s−2, s−1.
```

Moreover, `r=2` requires `m>s/8`, and `r=s−2` requires `m>s/7`.
Thus `binom(s,r)<4n` for arbitrary integer `s,m`. If both are powers
of two, each of the first two cases requires `m>=s/4`, giving
`binom(s,r)<2n`; the last case always has bank size `s<=n`.

These implications are not converses. They do not bound the number of
other codewords or labels that the same received line might possess.
They also do not automatically apply to compilers with altered dimension,
padding, agreement, or domain ledgers.

## Monotonicity and branch convention

The curve has transition `rho_c=11−3sqrt(13)<3/16` and is

```
low:  a1(rho)=sqrt(rho/2)(1+u),
      u>=0, u²(u+3)=sqrt(rho/2);
high: a1(rho)=[3rho+2sqrt(rho(5−rho)(2−rho))]/(8−rho).
```

The low expression is strictly increasing because both positive factors
increase. For the high expression, put `h=rho(5−rho)(2−rho)`. Its
derivative has positive denominator and numerator

```
24sqrt(h)+80−102rho+24rho²−rho³.
```

Writing `x=1−rho`, the polynomial part is
`1+57x+21x²+x³>0` on `[0,1]`. The two branches meet at the transition:
there `u=sqrt(rho_c/2)=(sqrt(13)−3)/2` and their common value is
`4−sqrt(13)`. Therefore lowering the actual rate to
`rho0=(r−2)/s` can only lower the first-order curve.

## Interior values on the high branch

Let `3<=r<=s−3`, `t=s−r`, and `a=r/s`. Direct expansion gives

```
s⁴{[a(8−rho0)−3rho0]²−4rho0(5−rho0)(2−rho0)}
 = −(7s+t+2) H_s(t),

H_s(t)=4s²(t−2)−3st²−16s−t³−2t².
```

This polynomial is strictly concave in `t`. For `s>=12`, its endpoint
values on `[3,s−3]` are positive; writing `y=s−12>=0`, they are

```
H_s(3)   =4y²+53y+15,
H_s(s−3)=5y²+62y+33.
```

Hence the displayed squared difference is negative. It follows that
`a` is strictly below the high-branch value at `rho0`, regardless of
the sign before squaring. Equivalently, the quadratic
`(8−rho0)a²−6rho0*a+rho0(4rho0−5)` is negative. This excludes every
interior value whose lowered rate is on the high branch.

## Interior values on the low branch

It suffices to prove `a<=sqrt(rho0/2)`, since the low curve is strictly
larger when `rho0>0`. This leading comparison is equivalent to
`2r²<=s(r−2)`.

For `r>=6`, the low-branch condition gives
`s>16(r−2)/3`. This is stronger than the needed bound because
`5r²−32r+32>0` for every `r>=6`. For `r=5`, it gives `s>=17`, hence
`50<3s`. For `r=4`, `32<=2s` holds already at `s=16`. For `r=3`,
`18<=s` handles all `s>=18`.

The two remaining cases are `(s,r)=(16,3),(17,3)`. Put
`b=1/sqrt(2s)` and `u*=6b−1>0`. Then

```
b−(u*)²(u*+3)=b(19−108/s)−2>0,
```

since `(19s−108)²−8s³` equals respectively `5648` and `6921`.
The increasing defining cubic therefore has its positive root above
`u*`, proving `a<a1(rho0)` in both cases. At `s=16` the same slack is
`−2+49sqrt(2)/32>0`, as in the proposed proof.

## Endpoint sizes

For `r=2`, the actual rate is `rho=1/(sm)`. The leading lower bound
on its low branch gives

```
2/s > sqrt(1/(2sm)),  hence m>s/8.
```

For `r=s−2`, the actual rate is on the high branch. Direct expansion
at `rho=((s−4)m+1)/(sm)` gives

```
[a(8−rho)−3rho]²−4rho(5−rho)(2−rho)
 = −4(7ms+4m−1) E/(m³s⁴),

E=ms²−7m²s+4ms−4m²+m−s
 =ms(s−7m)+(4m−1)(s−m).
```

If `1<=m<=s/7`, both terms in the latter expression are nonnegative
and the second is strictly positive. This contradicts being above the
positive high-branch root. Thus `m>s/7` is necessary.

The first endpoint gives
`binom(s,2)<s²/2<4sm`; the second gives the stronger bound
`binom(s,2)<(7/2)sm<4sm`. For powers of two, either necessary lower
bound on `m` forces `m>=s/4`, so `binom(s,2)<2sm`.
Finally `r=s−1` gives `binom(s,r)=s<=sm`.

The accompanying `verify_kkh_canonical_first_order_audit.py` checks both
polynomial identities by exact coefficient arithmetic and replays a
bounded integer census with exact branch comparisons. The proof above,
rather than the census, establishes the unbounded statement.
