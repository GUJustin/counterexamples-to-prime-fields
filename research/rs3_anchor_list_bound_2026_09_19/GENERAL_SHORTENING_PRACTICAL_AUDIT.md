# General shortening bound and two frozen practical cells

2026-09-19. Independent algebra and integer-arithmetic audit. The inputs
below are saved research parameters, not a statement about a live website.

**Outcome.** The one-anchor dimension-three bound extends to arbitrary
degree by anchoring `j` matching coordinates. At the two specified
half-rate benchmark cells, it requires more than 48,000 anchors before
the residual Johnson denominator becomes positive. Every resulting
displayed bound exceeds `2^24400`. This direct extension therefore
does not supply a useful benchmark improvement.

## Exact formula

Consider degree-at-most-`D` polynomials evaluated on `n` distinct field
elements, and fix an integer agreement threshold `D<T<=n`. For any
integer `0<=j<=D` with

    Delta_j=(T-j)^2-(D-j)(n-j)>0,

the list size of every received word obeys

    L <= [binom(n,j)/binom(T,j)]
         * (n-j)(T-D) / Delta_j.                         (1)

Here `D` is the degree bound, so the code dimension is `D+1`.
For an anchor set `A` of size `j`, let `I_A` be the degree-less-than-`j`
interpolant of the received values there and let
`h_A=prod_(a in A)(X-a)`. Every listed polynomial matching on `A` has
the unique form

    Q=I_A+h_A R, deg R<=D-j.

On the remaining `n-j` coordinates it matches the transformed received
word at least `T-j` times. Truncating each support to exactly `T-j`
points, distinct residual polynomials share at most `D-j` matches.
The standard second-moment count therefore bounds this anchored list by

    (n-j)((T-j)-(D-j)) / [(T-j)^2-(D-j)(n-j)].

Count pairs consisting of a listed polynomial and a size-`j` subset of
its agreement coordinates. Each polynomial contributes at least
`binom(T,j)`, while each of the `binom(n,j)` anchor sets contributes at
most the preceding quantity. This proves (1). The case `j=0` is the
ordinary Johnson count, with the zero interpolant and `h_A=1`.

The denominator is exactly affine in the anchor size:

    Delta_j=T^2-Dn+j(n+D-2T).                            (2)

## Exact frozen-cell arithmetic

Both cells have `n=262144` and `D=131071` (dimension `131072`).
The slope in (2) is positive in each case. Thus the least admissible
integer anchor size is

    j_min=floor((Dn-T^2)/(n+D-2T))+1.

| Saved agreement `T` | `Dn-T^2` | Slope | `j_min` | `Delta_(j_min-1)` | `Delta_(j_min)` |
| --- | --- | --- | --- | --- | --- |
| 181275 | 1498850599 | 30665 | 48879 | -6729 | 23936 |
| 181284 | 1495587568 | 30647 | 48801 | -13968 | 16679 |

The previous and first denominator values certify minimality directly;
there is no scan over possible anchor counts.

For any admissible `j`, the residual Johnson factor in (1) is at least
one, because

    (n-j)(T-D)-Delta_j=(T-j)(n-T)>=0.                    (3)

Also,

    binom(n,j)/binom(T,j)
       = prod_(i=0)^(j-1) (n-i)/(T-i)
       >= (n/T)^j.

The exact comparisons

    n^2-2*(181275)^2=2998225486>0,
    n^2-2*(181284)^2=2991699424>0

give `n/T>sqrt(2)`. Consequently the right side of (1), for **every**
admissible anchor size, is strictly greater than `2^(j/2)`, hence greater
than `2^(48879/2)` and `2^(48801/2)` respectively. Minimizing this
particular family of bounds cannot change that conclusion.

This lower bound is on the numerical *upper-bound expression*, not on
the actual list size. It does not rule out smaller lists or better
upper bounds from other arguments, nor improvements that exploit
additional information about the anchored residual lists.

## Reproduction

`verify_general_shortening.py` checks the two symbolic identities (2)
and (3), recovers the dimension-three one-anchor formula, and checks
the two exact integer cells. It writes
`general_shortening_receipt.json`. No website access, large binomial
evaluation, parameter sweep, codeword enumeration, or manuscript edit
is involved.

Saved context for the two thresholds is in
[`LOCAL_SINGLETON_SOURCE_AUDIT.md`](../better_codes_current_lower_2026_09_17/LOCAL_SINGLETON_SOURCE_AUDIT.md)
and the
[`analytic revisit README`](../better_codes_analytic_revisit_2026_09_17/README.md).
