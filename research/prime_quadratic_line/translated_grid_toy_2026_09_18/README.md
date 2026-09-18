# Exact translated-grid mechanism check

September 18, 2026. **PASS.** This is a finite sanity check for the mechanism
in `../TRANSLATED_GRID_POLYNOMIAL_GAP_INDEPENDENT_AUDIT.md`. It is not a
finite onset certificate for that asymptotic theorem, a novelty claim, or
an improvement to the practical fixed-domain benchmark.

The finite-field toy deliberately uses `d=1`, whereas its asymptotic
formula gives `floor(M/(64H))=0`. A separate integer-grid fixture exercises
the counting argument with its actual value `d=2`.

Run the dependency-free verifier with Python 3.10 or later:

```
python verify.py
```

It deterministically reconstructs `fixture.json` and `receipt.json`.
Primality is checked by trial division by all 228976 primes through
3181980; no probable-prime assertion is used. Every field calculation is
exact integer arithmetic modulo p.

## Finite-field parameters and results

| Quantity | Value |
| --- | ---: |
| H | 1500 |
| Prime p, with 2H^4 < p < 4H^4 and p=1 mod4 | 10125000000029 |
| Largest quartic prime class in [750,1500] | 28 primes |
| Disjoint numerator/denominator vertex sets | 9 primes each |
| F3 point/nonvertical-line incidence edges L | 27 |
| Pair-intersection core nodes | 702 |
| Core agreements per bank A | 52 |
| Translated-grid side M | 6 |
| Retained grid nodes | 18 |
| Neutral padding nodes | 685 |
| Total length n | 1405 |
| Ordinary RS dimension | 3 (degree at most2) |
| Toy agreement threshold T=A+1 | 53 |
| Distinct labels with singleton threshold lists | 486 |
| Exact agreement at each chosen endpoint | 52 |
| Exact common agreement of the endpoints | 52 |

The random seed is 2026091827; the first translation passes. Every
retained grid slope is a nonzero square, and all repeated slopes and core
slopes are checked before retention. Here the only deletions are eighteen
nonsquares. All 278517 labels in the **full integer-interval supersets**
are distinct across banks, so there are no cross-bank deletions. These
supersets include the labels of unretained grid pairs as well.

The exact point, line, prime, theta, core, grid, padding, and nearby-label
data are saved in `fixture.json`. The canonical file's SHA256 is recorded
in the receipt.

## What is checked exhaustively

The graph has no C4. Each bank parameter theta satisfies
`theta^2=a/b`, and theta itself is a square. All 378 unordered pair
products, including repeated pairs, are distinct. Thus the 351 distinct
bank pairs give exactly two different core nodes each.

At every core coordinate, the verifier evaluates all 27 quadratics

```
P_theta(X)=theta+X^2/theta
```

and confirms that precisely the two advertised owners match the core
word. Each bank has exactly52 core hits. All neutral coordinates are
distinct, nonzero, outside the old domain, and satisfy
`x^3 != P_theta(x)` for every bank.

On a retained grid coordinate associated with U=u0+u and V=v0+v,
`x^2=V/U`, and the words are `g=1/U`, `f=c0/U`, with c0=1. For every
one of the 486 bank/grid pairs the verifier checks the native quadratic
identity

```
U P_theta(x)-c0
 = theta*u0 + v0/theta + (a*u+b*v)/(b*theta) - c0.
```

Every bank is also evaluated at every domain coordinate. This classifies
its agreements for **every field label**: it has52 fixed core hits,
zero padding hits, and the saved finite map of grid-hit labels. Each of
the 486 counted labels has exactly one bank owner and exact bank
agreement53; all other banks have agreement52 there.

The endpoint labels0 and1 are checked to lie outside all translated raw
label supersets and outside the exceptional label `-c0=p-1`. Each bank
has exactly52 agreements with both endpoint words.

## Analytic certification of the unenumerated quadratics

The verifier does not enumerate all p^3 quadratics. The following exact
degree bounds complete the list and maximum-agreement claims.

If a quadratic Q is outside the bank, it meets each bank polynomial at
at most two points. Every core hit is counted twice, because every core
coordinate has two owners. Thus Q has at most L=27 core hits.

For a nonconstant Q and each fixed nonzero U, the equation
`Q(x)=(c0+lambda)/U` has at most two roots, hence at most2M=12 grid hits.
A nonzero constant has at most M grid hits. The zero polynomial has
zero grid hits unless `lambda=-c0`; this one label is excluded. On
padding, `Q(x)=x^3` has at most three roots. Therefore every nonbank
quadratic at a counted label or endpoint has at most

```
L+2M+3=27+12+3=42 < 52 < 53
```

agreements. This proves that all486 threshold lists are singleton and
that both endpoints have exact maximum agreement52.

For common agreement, transform the two endpoint witnesses to an
intercept F and direction G for the original pencil; the endpoint
labels0 and1 make this simply `G=P1-P0`, `F=P0`. If G is nonzero, it
can match the zero direction on at most two core-plus-padding nodes,
and has at most2M grid matches to g. Hence common agreement is at most
`2M+2=14<52`. If G=0, no grid coordinate can contribute. A nonbank
intercept has at most `L+3=30` core-plus-padding hits, and a bank
intercept has exactly52. The latter is attained. Thus common agreement
is exactly52.

Finally,

```
53^2=2809 < 2*1405=2810.
```

The toy threshold is strictly below the degree-two Johnson agreement.
This numerical check does not establish the asymptotic growth claims or
their finite onset.

## Independent integer-fiber check with d>1

Use `H=6`, primes `a=3,b=5`, and `M=1024`. Retain exactly the pairs
with `(u+v) mod4=0`. This leaves M^2/4=262144 pairs, and the prescribed
formula now gives `d=floor(M/(64H))=2`.

The verifier enumerates all full and retained fibers of `3u+5v`. It
independently checks every one of the 8193 indexed sums by solving the
Diophantine interval and congruence for u. The maximum full fiber is205;
the maximum retained fiber is103. There are30 points in fibers of size
less than2, and **4051 labels of multiplicity at least2**, exceeding
`HM/16=384`.

The raw interval has size8185, below `3HM=18432`, and the exact
light-point and maximum-fiber inequalities used in the proof pass.
This fixture checks the integer rich-fiber mechanism only; it is not a
second finite-field construction.
