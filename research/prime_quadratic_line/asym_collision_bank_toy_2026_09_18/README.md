# Exact asymmetric collision-bank toy

September 18, 2026. **PASS.** This fixture checks the asymmetric core,
rich-bank label screening, filler exclusion, neutral padding, and exact
agreement profiles from `../asymmetric_collision_bank.tex`. It is separate
from both earlier translated-grid fixtures and does not modify them.

The parameters are deliberately small: `H=600`, `K=1500`, `t=2`, `s=4`,
and `p=10125000000029`. We override the gap with `d=1`, whereas
`floor(M/(64H))=0`. The asymptotic relation between H and K and the theorem's
field window are not met. This verifies the finite mechanism and curve
placement; it is not an asymptotic onset, constant exceptional fraction,
or practical benchmark certificate.

Run `python verify.py` with Python 3.10 or later. It uses only the standard
library and reconstructs `fixture.json` and `receipt.json`. The verifier
proves primality by trial division by every prime through `isqrt(p)`:
228976 trial primes through 3181980. All arithmetic and comparisons are exact.

## Asymmetric core

The construction uses disjoint prime intervals and a separate coherent
square-root reference in each component:

| Component | Numerator primes | Denominator primes | Reference |
| --- | --- | --- | --- |
| Rich K(2,2) | 307, 313 | 331, 349 | 307 |
| Filler K(4,4) | 757, 809, 823, 881 | 919, 937, 941, 953 | 757 |

Both selected quartic-character classes happen to have the value
1167152939837; their available sizes are 16 and 28. Within each component
the verifier chooses square factors `alpha_a^2=a/z`, `beta_b^2=b/z` and
sets `theta_ab=alpha_a/beta_b`. It verifies that every theta is a square,
that `theta^2=a/b`, and that the 20 bank parameters are distinct. The bank is

```
P_theta(X) = theta + X^2/theta.
```

Among products of distinct bank parameters, 116 have one unordered-pair
representation and 37 have two. The double products are precisely the
rectangle diagonals within one component: one rich rectangle and 36 filler
rectangles. Including repeated pairs gives 173 distinct products.

A singleton product receives both roots of `x^2=theta*phi`. At a double
product, the smaller root goes to the lexicographically first pair and
the other root to the other pair. The two assigned pair sums differ.
At every core node, the verifier evaluates all 20 bank polynomials and
checks that exactly the two assigned owners match.

Each rich word loses one of its 38 potential pair-intersection coordinates;
each filler loses nine. Thus the exact core profiles are

```
A       = 37, attained by all four rich words,
A_filler= 29, attained by all sixteen filler words,
N_core  = (4*37 + 16*29)/2 = 306.
```

## Grid, filler exclusion, and complete line profile

For `M=floor(20/8)=2`, the first translation from seed 2026091834 retains
two of the four grid pairs. The other two ratios are nonsquares. Both
retained ratios are distinct nonzero squares outside the core ratios.

The verifier checks all 40 native bank/grid identities

```
U*P_theta(x) - c0
  = theta*u0 + v0/theta + (a*u+b*v)/(b*theta) - c0.
```

Only rich-bank raw labels are screened. Their full integer-interval
supersets contain 2604 bank-label pairs, and their union also has size
2604. Thus there are no cross-rich-bank collisions, including among
unretained grid pairs. The shift is `c0=1`; endpoints 0 and 1 avoid the
rich raw-label union and the zero-polynomial exception at `p-1`.

Append 415 neutral coordinates with `g=0`, `f=x^3`, avoiding zero, old
coordinates, and every bank's cubic intersections. The verifier then
evaluates every bank at every one of the 723 domain coordinates.

Each bank has two different native grid labels, with one grid hit at
each. Hence every filler has maximum agreement `29+1=30` over the entire
line, strictly below `A=37`. This is an exact check of all possible filler
agreements; it does not require enumerating the field's labels.

| Quantity | Exact value |
| --- | ---: |
| Field | F_10125000000029 |
| RS dimension | 3 |
| Length | 723 |
| Core / grid / neutral sizes | 306 / 2 / 415 |
| Endpoint maximum agreements | 37, 37 |
| Common agreement | 37 |
| Rich threshold | 38 |
| Singleton threshold labels | 8 |
| Maximum filler agreement at any label | 30 |

All eight rich labels are distinct and avoid both endpoints and the
exceptional label. A nonbank quadratic has at most 20 core matches:
each matching core node counts against its two bank owners, while its
difference from each bank has at most two roots. It has at most `2M=4`
grid matches, except for the zero polynomial at the exceptional label,
and at most three neutral matches. Thus its bound is

```
L + 2M + 3 = 27 < A=37 < T=38.
```

The exceptional zero polynomial is checked directly and has only two
agreements. These bounds exclude all unenumerated quadratic codewords;
no enumeration of `p^3` polynomials is claimed. Consequently the complete
affine line has this exact profile:

- Exactly eight labels have maximum agreement 38 and singleton nearest lists.
- Every other label has maximum agreement 37.
- At threshold 37, the list consists of exactly the four rich bank words
  at every label.

For common agreement, a nonzero quadratic explaining direction has at
most two matches where `g=0` and at most `2M=4` grid matches, totaling six.
A zero direction restricts to core plus neutral coordinates, where rich
banks have exactly 37 matches, fillers have 29, and a nonbank has at most
`L+3=23`. Thus common agreement is exactly 37.

## Exact first-order and Johnson placement

The threshold is below the degree-two Johnson agreement because

```
T^2 = 38^2 = 1444 < 2n = 1446.
```

For the low-rate first-order curve, use

```
n*a1(3/n) <= sqrt(3n/2) + (3n/8)^(1/4).
```

The verifier checks the strict integer inequalities

```
3*n*50^2 < 2*1647^2,
3*n*50^4 < 8*203^4.
```

They imply

```
n*a1(3/n) < 1647/50 + 203/50 = 37 = A < T.
```

The narrow finite curve placement therefore holds exactly. The explicit
`d=1` override and unmet asymptotic prescriptions remain part of the fixture's
scope.
