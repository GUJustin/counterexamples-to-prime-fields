# Cyclic two-coset banks: construction, complete list, and search coverage

Let q be an odd integer at least3, r=(q-1)/2, and let k contain a primitive q-th root
zeta, with characteristic not dividing q. Let r<h<q. Suppose
P in k[X], degree at most r, satisfies

1. P(zeta^s)=zeta^(hs) at exactly r+1 indices s;
2. alpha is nonzero and alpha^q!=1;
3. P(alpha*zeta^s)=c*zeta^(hs) at at least r indices s.

Define the domain mu_q union alpha*mu_q and the received word

    w(zeta^s)=zeta^(hs),
    w(alpha*zeta^s)=c*zeta^(hs).

For j=0,...,q-1 set

    P_j(X)=zeta^(-hj) P(zeta^j X).

These are q distinct polynomials of degree at most r. Indeed a nontrivial
stabilizer rotation would preserve the first matching set of size(q+1)/2.
Every orbit of that rotation has a common length greater than1 dividing q,
which cannot divide(q+1)/2. Thus the stabilizer is trivial, even when q is
composite. P is nonzero by condition1. An equivalent coefficient check is
gcd(q,{d-h: coefficient of X^d in P is nonzero})=1.
Every P_j has at least q agreements; each first-coset coordinate has exactly
r+1 matching candidates, and each second-coset coordinate has at least r.

Pair counting forces the second multiplicity to be exactly r. The q
candidates allow at most r*binom(q,2)=q*r^2 pair incidences. The first coset
already contributes q*binom(r+1,2), and a second multiplicity r contributes
the complementary q*binom(r,2). Any larger multiplicity is impossible.
Thus every candidate has exactly q agreements and every pair shares exactly
r distinct domain nodes. In particular every pair difference has degree r.

## Complete list, not merely q exhibited candidates

Let H of degree at most r be distinct from the displayed q candidates and
have at least q agreements. Counting its intersections with the bank gives
at most qr. Every agreement in the first coset contributes r+1 intersections,
and every agreement in the second contributes r. Therefore H must agree
at exactly all q second-coset points and at no first-coset point.

On alpha*mu_q the received values have unique interpolant of degree below q

    c*alpha^(-h) X^h.

If c!=0, its degree h exceeds r, so no such H exists. The complete list at
agreement q therefore has exactly q members, and the nearest agreement is q.
If c=0, H=0 is the unique additional candidate, distinct from the bank.
Then the complete list has exactly q+1 members, still with nearest agreement q.
A zero-valued bucket should therefore be retained, not rejected as degenerate.

The code operates over prime F_p with q dividing p-1. Its primes necessarily
have characteristic greater than q, and all interpolation denominators are
nonzero. For number-field constructions the same argument is valid directly;
finite-field hits alone are not evidence of a characteristic-zero lift.

## Independent verification of the q7,p113 witnesses

`independent_verify.py/json` fully reconstructs both emitted witnesses,
the fourteen domain points, received values, seven coefficient vectors,
all masks, and all21 pair agreement counts. Both pass: agreement7 per
candidate, pair agreement3, first-coset masks4, second-coset masks3,
and nonzero bucket value. Their complete lists therefore have exactly7
members. This verification does not call the C++ interpolation or counting
functions.

## What search.cpp covers

The original audited prime-q program enumerates all supports of size r+1 on the first coset, up to
cyclic rotation; all exponents r<h<q; and all distinct nonidentity cosets
alpha*mu_q. For each support the unique degree-r interpolant is computed,
and each equal-value bucket of P(alpha*zeta^s)*zeta^(-hs) is tested.

Rotation canonicalization is sound: rotating the support by j replaces P
by zeta^(hj)P(zeta^(-j)X), preserving bucket multiplicities. Changing alpha
to another representative of the same coset only permutes the bucket
indices and rescales all bucket values by a nonzero scalar.
Exponents h<=r give P=X^h by interpolation on r+1 nodes and thus a collapsed
single-candidate orbit; their omission is justified for this ansatz.

This is exhaustive only for the specified split cyclic two-coset ansatz at
one fixed(q,p), when the emitted status says exhaustive=true. It omits
nonsplit cyclic actions (q dividing p+1), non-semi-invariant received words,
more than two orbits, other degrees, and other incidence families. A stop
after a hit is intentionally not an exhaustive negative result. The q<=25
bitmask guard excludes the larger Singer tests unless a separate fixed-support
mode is added; a fixed-support search is not exhaustive over all supports.

## Practical protocol before a larger scan

For q=11,19,23 the numbers of canonical supports are respectively
42,4862,58786. With m=(p-1)/q, the unpruned coset tests per prime are

    [binom(q,r+1)/q] * r * (m-1).

Each current test uses q degree-r evaluations and a sort of q values.
Thus raising p raises runtime linearly; q23 is substantially more expensive
than q11. Start with the smallest admissible primes p=1 mod q, record every
(q,p), support count, tests, wall time, stop reason and positive hit, and
schedule independent pairs on separate CPU workers. Dozens of primes can
be useful finite exploration, but cannot certify a characteristic-zero
family or asymptotic growth without a separate identity or lifting proof.

The reciprocal transformation P*(X)=X^r P(1/X) pairs exponents
h and q+r-h, and sends alpha to alpha^(-1). It could almost halve the h
range after a separate implementation check; the current full range is safer.

Two engineering bounds should be explicit: reject p<2; and use a widened
addition (or restrict p<2^30), since `(a+b)%p` uses signed int addition.
The requested small and moderate prime scans are below this overflow range.
For bounded jobs, flushed hit output or a hit-limit of1 prevents a timeout
from losing buffered positive results. Keep the exact source version with
each result. Independently reconstruct every positive bank before assigning
mathematical significance.

## Composite Singer manifests

The independently verified generator in singer/generate.py now also includes
q15 and q63 using x^4+x+1 and x^6+x+1. Powers of X enumerate every nonzero
residue, proving the supplied quotients are fields and the elements primitive.
Only unit multipliers modulo q are included. There are2 and6 multiplier
classes modulo rotations, respectively; their trace-zero difference-set
multiplicities are3 and15. Natural twists h=(3q-1)/4 are11 and47, coprime
to q. A composite-q search must verify the full order of zeta explicitly;
the original prime-q shortcut is not sufficient.
