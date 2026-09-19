# Composition refinement: a linear characteristic condition for exact sources

2026-09-19. Independent audit: **PASS**. The sufficient characteristic
condition for exact source agreement improves from `p>=h²` to
`p>=3h−1`. The refinement treats every degree-`h` polynomial, including
ones with several intermediate exponents, and permits arbitrary
puncturing for the noncanonical upper bound.

## Exact lemma and branch audit

Let `p` be an odd prime and let odd `h>1` divide `p²+1`. Work over
`B=F_(p²) subset E=F_(p⁴)` with the primitive-scale two-block domain
of `HIGHER_POWER_FULL_FIBER_LIFT.md`. Assume `p>=3h−1`.
For any noncanonical polynomial `q` of degree at most `h`, define

\[
 \delta=\gcd\bigl(h,\{j:0<j<h,\ q_j\ne0\}\bigr),
 \qquad H=h/\delta.
\]

The set of intermediate exponents is nonempty. Thus `delta` is a
proper divisor of odd `h`, and `H>=3` is odd. Every exponent of `q`,
including zero and the possible leading exponent `h`, is divisible
by `delta`. Hence `q(X)=q_0(X^delta)` with `deg q_0<=H`.

The primitive-scale branch separation is valid here: the required
guard `h−1<(p²+1)/h` follows from `p>=3h−1>h`. Within a block, the
difference of two coefficientwise-`B` branch indices must belong to
the simultaneous kernels of multiplication by every intermediate
exponent on `Z/hZ`. This common kernel has exactly `delta` elements.
There are consequently at most `delta` good branches in that block,
and the scale-separation congruence prevents good branches in both
blocks at once. The constant coefficient and challenge can only
remove compatible branches; they do not enlarge this bound.

On every normalized branch, the matching equation has the form

\[
 z^{hp}=\widetilde P(z^\delta),\qquad \deg\widetilde P\le H.
\]

Since odd `delta | h | p²+1`, one has
`gcd(delta,p²−1)=1`. Substituting `u=z^delta` is therefore a
**bijection on B**, not a map with `delta` preimages. On a good
branch the equation becomes `u^(Hp)=P(u)` over `B`. A nonzero
intermediate coefficient survives normalization and division of
exponents, so this remains noncanonical at exponent `H`. The local
Kummer classification in `ODD_POWER_KUMMER_NONCANONICAL_BOUND.md`
gives at most `max(p,H²)` matches.

On a bad branch, the nonzero projection killing `B` is also a
polynomial in `z^delta`; as a polynomial in `u`, its degree is at
most `H`. It therefore gives at most `H` matches. Using at most
`delta` good branches among all `2h` branches is legitimate because
`max(p,H²)>=H`. Thus uniformly in the challenge,

\[
 \operatorname{agr}(f+\lambda g,q)
 \le U_\delta
 :=\delta\bigl(\max(p,H^2)+(2H-1)H\bigr).
\tag{1}
\]

This verifies both possible sources of a hidden multiplicity error:
the simultaneous good-branch count is `delta`, whereas the
`delta`-power substitution within a branch has multiplicity one.

## Both characteristic cases give strict inequality

If `p>=H²`, then

\[
 hp-U_\delta
 =\delta\bigl((H-1)p-(2H-1)H\bigr)
 \ge\delta H(H^2-3H+1)>0,
\]

since `H>=3`.

If `p<H²`, then instead

\[
 U_\delta=\delta(3H^2-H)=h(3H-1).
\]

Here `p>=3h−1>=3H−1`. Equality with `3H−1` is impossible because
`H` is odd, so `3H−1` is even and at least eight, whereas `p` is an
odd prime. Therefore `p>3H−1`, again giving `U_delta<hp`.
These two cases cover every possible composition divisor.

If the complete first block is retained, a canonical nonzero core
fiber attains `hp` at every challenge. Outside the union of canonical
label planes, canonical polynomials have at most `hp` matches, and
(1) puts every noncanonical polynomial strictly below `hp`. Hence

\[
 A(f+\lambda g)=hp
\]

for **every** parameter outside that union. Ordinary common agreement
is also exactly `hp` by the indicator-polynomial argument. The exact
threshold-list profile follows whenever `T>hp` and the retained fresh
domain gives every doubly canonical polynomial at least `T` matches.
There is no assumption that all codewords are compositions; each
noncanonical codeword is assigned its own `delta` and bounded above.

## Finite application: p=307, h=65

The exact standard-library certificate
`verify_composition_p307_h65.py` and its JSON receipt use

\[
 p=307,\quad h=65,\quad L=p^2-1=94248,\quad
 N=hL=6126120,\quad m=\lfloor17N/20\rfloor=5207202.
\]

Here `p` is prime by trial division through 17,
`h | p²+1`, and `p>=3h−1=194`, although `p<h²=4225`.
The possible proper composition divisors are exactly

| delta | H | case | bound U_delta |
|---:|---:|---|---:|
| 1 | 65 | p < H² | 12610 |
| 5 | 13 | p >= H² | 3160 |
| 13 | 5 | p >= H² | 4576 |

All noncanonical witnesses therefore have at most `12610` matches,
strictly below the exact source and common agreement `hp=19955`.

For the deterministic domain, choose a primitive `s in E`, put
`z=s^(p²+1)` and `alpha_j=s^((p²+1)j/h)`. Retain all `h` core
branches, then `r=55` complete fresh branches and the first `d=23562`
points of the next branch in the order `s*alpha_r*z^t`, `0<=t<d`.
Indeed `m=rL+d`. The resulting exact ledger is

| Quantity | Value |
|---|---:|
| Length n | 11333322 |
| Dimension k | 66 |
| Exact endpoint and common agreement | 19955 |
| Threshold T=floor(sqrt(hn−1)) | 27141 |
| Minimum canonical agreement (h+r)(p−1) | 36720 |
| Certified first-order agreement upper bound | 19802 |
| Johnson squared slack hn−T² | 32049 |
| Singleton labels | 29028384 |
| Additional zero-label list size | 308 |

The first-order bound is certified by separate exact ceilings of
`sqrt(kn/2)` and `(k³n/72)^(1/4)`, namely `19340` and `462`.
The rate is below `1/100`, within the low-rate branch. Thus

\[
 n a_1(k/n)<19802<19955<27141<\sqrt{hn}.
\]

The first inequality is strict because the radical sum is strictly
below the sum of its integer ceilings. Both `(T+1)²>=hn` and
`T<=36720` are checked exactly. Even the older stronger threshold
guard `hp+h²<T` happens to hold; the new lemma is needed for the
**exact** source value under the weaker characteristic hypothesis.
The exact source loss as a fraction of the capacity margin is

\[
 \frac{T-hp}{T-k}=\frac{7186}{27075}>0.265.
\]

This is a finite parameter certificate for an algebraically specified
domain over `F_(307^4)`, after a primitive element is fixed. It does
not enumerate the domain, claim a prescribed short evaluation set,
or assert a new asymptotic rate. The finite label population exceeds
the length, but one finite instance is not itself a superlinear
asymptotic statement. No manuscript edit or broad parameter search
was performed.
