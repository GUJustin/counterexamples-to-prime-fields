# One-anchor RS dimension-three list bound: finite norm-one constants

2026-09-19. Independent exact arithmetic audit. This improves uniform
fixed-word list upper bounds for the existing norm-one example; it is
not a new construction or a practical benchmark claim.

## Universal anchor bound

Let an RS code evaluate polynomials of degree at most two at `N>=3`
distinct field elements. Fix any received word and an integer agreement
threshold `3<=T<=N`. Suppose `(T-1)^2>N-1`. Then its list size is at most

    U(N,T) = N(N-1)(T-2) / [T((T-1)^2-(N-1))].             (1)

Indeed, fix an evaluation coordinate `x0`. Every listed polynomial
matching the word at `x0` has the form

    Q(X)=f(x0)+(X-x0)L(X), deg L<=1.

On the other `N-1` coordinates, these distinct linear polynomials match
the transformed word `(f(x)-f(x0))/(x-x0)` at least `T-1` times.
Truncate their supports to exactly `T-1` matches. Any pair shares at
most one coordinate. If there are `m` of them, Cauchy's inequality and
pair counting give

    m^2(T-1)^2 <= (N-1)[m(T-1)+m(m-1)],

hence `m<=(N-1)(T-2)/((T-1)^2-(N-1))`. Summing this bound over anchors,
each member of the original list is counted at least `T` times, proving
(1). The argument is valid over every field and for arbitrary received
words and evaluation domains. No characteristic guard is needed.

Write `M=N-1` and `z=T-1`. Exact differentiation gives

    d(U/N)/dz = -2M[(z-1)^2(z+1)+M-1]
                /[(z+1)^2(z^2-M)^2] < 0                 (2)

when `M>=2` and `z>sqrt(M)`. Therefore replacing an integer threshold
by a smaller real threshold in this range only increases the bound.

## Finite norm-one constants

The domain in `norm_one_direct_list.tex` has

    N=2(p^2+p+1), M=2p^2+2p+1.

For a proposed constant `A/B`, define the exact slack

    H = A*T0*((T0-1)^2-M) - B*M*(T0-2).                  (3)

Positivity of both `(T0-1)^2-M` and `H`, together with (2), proves
`U(N,T)<(A/B)N` for every integer `T>=T0` up to `N`. The following
three certificates use only polynomial coefficient positivity.

| Threshold lower bound `T0` | Onset | Uniform bound |
| --- | --- | --- |
| `19p/10` | `p>=53` | `U<(4/3)N` |
| `sqrt(3)p` | `p>=401` | `U<(21/10)N` |
| `sqrt(3)p` | `p>=53` | `U<(9/4)N` |

For the first row,

    H=(209p^3-10870p^2+1575p+1500)/250.

After `p=53+v`, its ascending coefficients are

    333219/125, 305299/125, 22361/250, 209/250.

The denominator gap similarly has positive shifted coefficients
`421509/100, 8243/50, 161/100`.

For the second row,

    H=sqrt(3)p^3-(86+62sqrt(3))p^2+(40-10sqrt(3))p+20.

After `p=401+v`, its ascending coefficients are

    -13812826+54507529sqrt(3),
    -68932+432669sqrt(3), -86+1141sqrt(3), sqrt(3).

For the stronger-onset third row,

    H=sqrt(3)p^3-(38+26sqrt(3))p^2+(16-4sqrt(3))p+8.

After `p=53+v`, its ascending coefficients are

    -105886+75631sqrt(3),
    -4012+5667sqrt(3), -38+133sqrt(3), sqrt(3).

All displayed coefficients are strictly positive. The verifier checks
their signs by rational squaring in `Q(sqrt(3))`, without floating point.
It also verifies denominator positivity after the same shifts.
These certificates hold for all real `p` at or above their onsets;
restricting to primes supplies the norm-one construction.

The existing exhibited list has exactly `N/2` members at all thresholds
in the two requested bands. Consequently the finite matched ratios are
at most `8/3` at `ceil(19p/10)` and at most `9/2` throughout
`ceil(sqrt(3)p)<=T<=2p+2` already for `p>=53`. At `p>=401`, the latter
ratio improves to `21/5`. This audit does not change the separately
proved first-order and Johnson placement conditions.

## Fixed normalized threshold

Fix `sqrt(2)<c<2`, and write `T=ceil(cp)=cp+epsilon`,
`0<=epsilon<1`. The numerator and denominator of `U/N` have leading
coefficients `2c` and `c(c^2-2)` as polynomials in `p`, independently
of the bounded rounding variable. Therefore

    U(N,ceil(cp))/N -> 2/(c^2-2).

For completeness the denominator gap is at least

    (c^2-2)p^2-(2c+2)p-1,

which is positive whenever `p>=1` and `p>(2c+3)/(c^2-2)`.
The exhibited `N/2` list remains present for all sufficiently large
`p`; its upper-to-lower ratio consequently has upper limit at most
`4/(c^2-2)`. This replaces the older cubic dependence on
`(c^2-2)^(-1)` by a linear dependence for this codewide comparison.

## Reproduction and scope

Run `verify.py` with the existing research-toolchain Python. It checks
the derivative identity, each cross-multiplied polynomial, every
shifted coefficient sign, and the rounded-threshold leading coefficients.
It writes `receipt.json` with the script hash. No parameter sweep,
codeword enumeration, manuscript edit, or field computation is used.

## Superseded comparisons and practical scope

The dated norm-one audits and September 18 strategy notes retain the
older valid 22N/137N upper bounds and factor-44/274 comparisons as
historical records. The constants above supersede those comparisons;
the archived certificates have not been rewritten.
[The active-text audit](LOCAL_PRIOR_AND_ACTIVE_TEXT_AUDIT.md) records
the manuscript checks and identifies the older records.

[The general-shortening audit](GENERAL_SHORTENING_PRACTICAL_AUDIT.md)
extends the argument to arbitrary message degree and checks two frozen
practical benchmark cells. Every resulting numerical upper-bound
expression exceeds 2^24400 there. This is a limitation of this proof,
not a lower bound on the actual list size or a live better.codes claim.
