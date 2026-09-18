# Exact two-biclique collision-bank toy

September 18, 2026. **PASS.** This separately checks the coherent
two-K(4,4) core and the translated-grid/neutral-padding mechanism. It
does not overwrite the earlier C4-free toy.

This is **not** a finite onset or constant-fraction certificate for the
asymptotic theorem. We deliberately choose t=4, reuse H=1500 and
p=10125000000029, and set d=1 although `floor(M/(64H))=0`. This p is
outside the theorem's prescribed `(4096LHM,8192LHM)` window. No practical
benchmark improvement or novelty claim is made.

Run `python verify.py` with Python 3.10 or later. It uses only the standard
library and reconstructs the exact `fixture.json` and `receipt.json`.
Primality is proved by trial division by all 228976 primes through
3181980. All checks use exact finite-field arithmetic.

## Core construction and exhaustive checks

Among the 107 primes in [750,1500], the chosen quartic-character class
has28 members. The two components use these disjoint vertex sets:

| Component | Numerator primes | Denominator primes |
| --- | --- | --- |
| 0 | 757,809,823,881 | 919,937,941,953 |
| 1 | 971,1061,1109,1117 | 1171,1187,1213,1231 |

Using reference prime z=757, choose square roots alpha_a and beta_b of
a/z and b/z that are themselves squares, and set
`theta_ab=alpha_a/beta_b`. The verifier checks all these identities and
that every theta is a square and satisfies theta^2=a/b.

There are L=32 distinct bank polynomials

```
P_theta(X)=theta+X^2/theta.
```

Among products of **distinct** bank parameters, 352 products have one
unordered pair representation, and72 have two. Every double product
comes from the two diagonals of a rectangle in one component; the
coherent alpha/beta choice makes those products exactly equal. Products
of repeated parameters have no other representation.

For a singleton product assign both roots of x^2=theta*phi to its pair.
For a double product assign the smaller root to the lexicographically
first pair and the other root to the other pair. The two pair sums are
checked to differ. At an assigned node the word is the assigned sum.

The verifier evaluates **all32 bank polynomials at every core node**.
Precisely the assigned two owners match at each node. Each bank loses
exactly `(t-1)^2=9` of its62 potential pair-intersection coordinates and
has exactly

```
A=62-9=53=3t^2+2t-3
```

matches. The domain core has exactly `LA/2=t^2 A=848` distinct nodes.
Thus regularity and the assignment of the two signs are checked
directly, not inferred merely from the graph formula.

## Grid, padding, and complete finite profile

The first translation from seed2026091832 retains8 of the16 grid pairs
with M=4. All retained ratios are nonzero squares and distinct from
each other and every core ratio; the eight deleted pairs are nonsquares.
All256 bank/grid quadratic label identities are checked exactly.

The **full raw integer-interval supersets**, including unretained
pairs, contain192992 bank-label pairs. Their union has the same size:
there are no cross-bank collisions. The shift c0=1 makes labels0 and1
far and avoids the zero-polynomial exception at label p-1.

Appending603 neutral coordinates with `g=0,f=x^3`, excluding zero,
old coordinates, and every bank's cubic intersections, gives:

| Quantity | Exact value |
| --- | ---: |
| Field | F_10125000000029 |
| RS dimension | 3 |
| Length | 1459 |
| Core/grid/neutral sizes | 848 / 8 / 603 |
| Both endpoint maximum agreements | 53 |
| Common agreement | 53 |
| Nearby threshold | 54 |
| Singleton threshold labels | 256 |

Every bank is evaluated at every coordinate, so its complete agreement
profile is known:53 fixed core hits, no neutral hits, and one grid hit
at each of its eight labels. The256 such labels are all distinct.

The remaining quadratic words are certified analytically. A nonbank
quadratic has at most L=32 core matches, since each match has two bank
owners and each bank difference has at most two roots. Fixing U gives
at most two grid roots per row, hence at most2M=8 grid matches, apart
from the usual zero-polynomial exception. Neutral padding supplies at
most three more. Thus the nonbank bound is

```
L+2M+3=43 < A=53 < T=54.
```

At the exceptional label, the zero polynomial is checked directly to
have only8 agreements, also below A. Consequently the **entire line**
has this exact profile:256 labels have maximum agreement54 and a
singleton nearest list; every other label has maximum agreement53.
At the relaxed threshold53 the list consists of exactly the32 bank
words at every label. No enumeration of p^3 quadratics is claimed;
the root bounds prove exclusion of all unenumerated candidates.

For common agreement of the endpoints, a nonzero quadratic direction
has at most2 zero-direction matches and2M grid matches, totaling10.
A zero direction restricts the intercept to core plus neutral points;
a nonbank has at most L+3=35 matches there, whereas a bank has exactly53.
Thus common agreement is exactly53.

## Exact first-order and Johnson placement

The finite comparisons are also certified:

```
T^2=54^2=2916 < 2n=2918,
3n < 2*47^2,             3n < 8*5^4.
```

The low-rate first-order bound therefore gives

```
n*a1(3/n) <= sqrt(3n/2)+(3n/8)^(1/4) < 47+5=52 < A=53.
```

Both source and threshold lie above that curve, and the threshold lies
below the degree-two Johnson agreement. This finite placement is fully
consistent with the stated d=1 mechanism scope; it does not verify the
asymptotic theorem's growing d or constant exceptional fraction.
