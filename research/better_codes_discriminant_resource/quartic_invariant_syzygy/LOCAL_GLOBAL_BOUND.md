# Quartic invariant derivative: a valid new resource, but this profile survives

Let G=Y^4+bY^3+cY²+dY+e, with coefficient degree bounds w,2w,3w,4w. Work over a field of characteristic different from two and three. Set

    I=c²-3bd+12e,
    J=72ce+9bcd-27d²-27b²e-2c³,
    Delta=4I³-J²=27 Disc(G),
    W=3I'J-2IJ'.

Equivalently, after depressing G=Y^4+pY²+qY+r, the invariants are I=p²+12r and J=72pr-27q²-2p³. The raw formulas show directly that deg I≤4w and deg J≤6w, independently of a local translation by the received word.

## Universal local lower bound

Assume I,J,Delta are nonzero and let their orders at a finite coordinate be alpha,beta,delta. Then

    ord W >= max(0,
       alpha+beta-1 + [3alpha=2beta],
       alpha+delta-beta-1 + [delta=3alpha],
       beta+delta-2alpha-1 + [delta=2beta]).

Here an equality in brackets is an equality of integers. Additional characteristic-dependent cancellation can only improve the bound. The proof consists of the three derivative identities

    W=3I'J-2IJ',
    J W=I Delta'-3I' Delta,
    4I² W=J Delta'-2J' Delta.

Their leading coefficients respectively contain 3alpha-2beta, delta-3alpha, and delta-2beta. When that integer is zero the nominal leading term cancels and the order improves by at least one. Regularity gives the extra lower bound zero, including the case where all three invariants are units.

In characteristic zero, or when the relevant order differences are nonzero modulo the characteristic, an unbalanced pair 3alpha≠2beta gives the exact value alpha+beta-1. In the balanced case alpha=2k,beta=3k and delta>6k, the exact value is delta-k-1 provided delta-6k is nonzero modulo the characteristic. For delta=6k only the universal bound5k follows without more coefficients.

## Global degree budget

If W is nonzero, its degree is at most10w-2, slightly better than the naive10w-1. If either I or J falls short of its cap this is immediate. If both attain their caps, their top derivative coefficient cancels because 3(4w)-2(6w)=0. Therefore the sum of the displayed local lower bounds over distinct nodes cannot exceed10w-2.

## Exact archived profile

`profile.py` reads the previously verified quartic remainder profile and computes generic invariant orders directly from the raw coefficient orders:

    alpha=min(2 ord c, ord b+ord d, ord e),
    beta=min(ord c+ord e, ord b+ord c+ord d,
             2 ord d, 2 ord b+ord e, 3 ord c).

These minima are exact on the generic local states specified by that profile; they are not asserted for arbitrary cancellations. The discriminant orders are the archived Newton-polygon orders. The resulting local triples and W costs are:

| (alpha,beta,delta) | W lower bound |
|---|---:|
| (0,0,0) | 0 |
| (1,2,3) | 2 |
| (2,2,4) | 3 |
| (2,3,7) | 5 |
| (3,4,8) | 6 |

At w=131071 the weighted sum is1135931, below the global bound1310708 by174777. Thus the invariant-derivative syzygy is a legitimate additional compatibility resource, but it does **not** exclude this surviving local profile. The generic local states also force W to be nonzero, because some have unbalanced invariant orders with nonvanishing leading coefficient. No new source search or linear program was used.

## The W=0 branch

In characteristic zero, W=0 implies (I³/J²)'=0 and hence I³/J² is constant. In characteristic p this conclusion needs a Frobenius guard: it holds if the rational function has height below p. The coefficient caps give height at most12w, so p>12w suffices here.

If I and J are both nonzero, unique factorization over an algebraic closure then gives

    I=a K², J=b K³,

with nonzero constants a,b and deg K≤2w. Thus Delta=(4a³-b²)K^6. If Delta is nonzero, all its finite zero orders are multiples of six. The cases I=0, J=0, or Delta=0 must be separated rather than divided through. In the separable, nonzero-discriminant setting this is constant quartic moduli (constant root cross-ratio up to permutation), not a proof that the roots form an affine polynomial pencil. Projective changes, algebraic extensions, and twists may still occur. No polynomial-section helper or routing improvement is claimed from this observation alone.
