# Constant relative loss in the translated-grid mechanism

September 18, 2026. A scoped obstruction, with a matching small-label
tradeoff. No manuscript changes accompany this note.

Increasing the grid side from L/4 to cL for any fixed c<1/2 changes
constants only. A positive fraction of the capacity margin **is**
possible by adding one bounded-height bank, but it then supplies only
Theta(L)=Theta(sqrt(n)) labels. A single translated grid cannot retain
the much larger label population at that loss scale.

## 1. A height bound that does not assume rational input slopes

Let p be odd, M>=2, and p>2(M-1)^2. On any retained subset of the
translated M-by-M grid, the bank parameter theta specifies labels

    lambda = theta*u + v/theta + constant_theta,
    1<=u,v<=M.

The translations and the common shift affect only the constant. Suppose
one label has d>=2 distinct grid points. Then theta² has a reduced
integer representation a/b modulo p with

    0<|a|<=K,  1<=b<=K,  gcd(a,b)=1,
    K=floor((M-1)/(d-1)).

Proof: every difference vector (h,k) of two points in the fiber obeys
theta²*h+k=0 modp. Neither component can vanish unless both do. For
two such vectors, their determinant vanishes modp and has absolute
value at most 2(M-1)^2<p. It therefore vanishes as an integer. All
fiber points lie on one rational line with a primitive direction
(b,-a). Their integer line parameters are distinct, so the extreme
ones differ by at least d-1. The width M-1 in each coordinate gives
the displayed bounds. This proves the assertion even if theta was
initially chosen as an arbitrary element of Fp rather than from small
rational coefficients.

There are at most 2K² signed reduced ratios of the displayed height,
and each has at most two square roots theta. Consequently at most

    R_d <= 4K²

distinct banks can have even one d-rich fiber. If B labels each have
one qualifying bank witness, the bank-label incidence budget now gives

    B <= R_d * M²/d
      <= 4M²/d * floor((M-1)/(d-1))².                 (1)

One may add one to (1) for the exceptional zero-polynomial label in
the audited construction. Deleting grid points, keeping one square
root of each ratio, and excluding core coordinates only shrink fibers,
so none of these operations weakens the bound. Sidonicity is not needed.

For M=O(L) and d=Theta(L), (1) is O(L). More quantitatively, for
d tending to infinity and B/L tending to infinity it forces

    d/L = O((L/B)^(1/3)) = o(1).

Thus no change of rational slopes, nor arbitrary finite-field slopes,
can give both a constant relative gap and a superlinear-in-L number of
labels within this single dense grid. If a positive fraction of all L
banks must have a d-rich fiber, the sharper intermediate count gives
d=O(M/sqrt(L)), hence d=O(sqrt(L)) for M=O(L).

The field-size hypothesis is automatic in the originally requested
M=cL, c<1/2 regime: the distinct quadratic core already needs
p>=L(L-1), which eventually exceeds 2(M-1)^2. Modular wraparound
therefore does not evade the line-direction argument in that regime.

## 2. Why changing rows, neutral padding, or bounded height does not help

The existing deterministic exclusion of nonbank quadratics is

    nonbank agreement <= L+2M+3 < A=2L-2.

It holds, for example, for M<=floor((L-6)/2), so every fixed c<1/2
is available. With the original prime-ratio bank, every slope has
height at least H/2, so every fresh fiber has at most 1+2M/H points.
Hence d/A=O(1/H)+O(1/L), independently of the choice of c.

For code dimension three, the tested capacity margin and source loss
are respectively

    eta=(T-3)/n,    epsilon=(T-A)/n=d/n,
    epsilon/eta=d/(A+d-3).                           (2)

Neutral padding changes n in both quantities and leaves their ratio
exactly unchanged. With A=Theta(L), a positive limiting ratio requires
d=Theta(L), which invokes the O(L) label bound above.

Bounded rational height cannot support a growing bank: at height H
there are at most 4H² possible theta, even before imposing Sidon
constraints. In the disjoint-prime/C4-free realization there are only
O((H/log H)^(3/2)) edges. Indeed, if the graph has v vertices per side,
counting pairs of neighbors gives sum_b binom(deg(b),2)<=binom(v,2),
whence its edge count is at most v^(3/2)+v. This explains the stronger
height growth in the actual proof. A different Sidon construction may
improve that exponent; it cannot bypass (1).

These statements do not rule out a different received-word ratio,
multiple unrelated grids, sparse retention from a much larger grid,
or a new core whose actual common agreement has a different scale.
If both above-first-order agreement and n=Theta(L²) are retained,
however, the common agreement must remain Omega(L), so merely lowering
its advertised core count is not enough.

## 3. A matching positive constant-loss tradeoff with fewer labels

Adjoin theta_0=1 to the existing prime-ratio Sidon bank. This preserves
the multiplicative Sidon property. An equality theta_i*theta_j=theta_k
or theta_i*theta_j=1, after squaring, would equate products containing
different numbers of numerator primes from one disjoint prime set and
denominator primes from the other. Unique factorization excludes it;
p>H^4 prevents modular aliases. Equalities involving only the old
parameters were already excluded.

Let L denote the enlarged bank size. Keep M=floor(L/4), but set

    d=floor(M/16),   A=2L-2,   T=A+d,
    n=floor(T²/2)+1.

The square-retention argument still supplies X>=M²/4 valid fresh
coordinates. For the special bank theta_0=1, a label depends only on
u+v. It therefore has at most 2M-1 possible labels, and each fiber
has at most M points. Fibers smaller than d account for at most
2M*d<=M²/8 points. At least M/8 labels consequently have at least d
fresh matches.

Every old bank has at most 1+2M/H=o(d) fresh matches at any label,
so none reaches T. Thus cross-bank label collisions do not affect
singleton lists at this threshold. Remove at most the single
zero-polynomial label. Choose the common shift c0 outside the old and
new raw bank-label unions and their unit translates, and outside
{0,-1}; these unions still have size o(p). The original endpoint and
common-agreement proof, and the same neutral padding, apply unchanged.
There are at least floor(M/8)-1 singleton labels, exact endpoint and
common agreement A, and source gap d. The total number of threshold
labels is O(M), because only the special bank and the zero exception
can qualify.

In this concrete parameter choice,

    d/L -> 1/64,
    epsilon/eta -> 1/129,
    number of singleton labels = Theta(L)=Theta(sqrt(n)).

The threshold is strictly below Johnson by the exact choice of n.
The common agreement remains above first order: A/sqrt(n) tends to
128*sqrt(2)/129, which exceeds sqrt(3/2). All codewords still have
degree at most two and all values lie in the prime field.

This realizes the O(L) label-count scale permitted by (1) for a
constant fraction of capacity margin. It does not improve the large
exceptional-population theorem or supply Omega(p) labels. The useful
gate is therefore a tradeoff, not an impossibility of any constant
relative gap.
