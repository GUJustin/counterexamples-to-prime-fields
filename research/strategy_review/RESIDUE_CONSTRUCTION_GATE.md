# Bounded constructive check: residue moments and three value branches

September 17, 2026. Outcome: no new scalable construction. The constant
alphabet route is a reformulation of the missing nearest-list source;
the simplest challenge-dependent cubic alphabet has a sharp extension
obstruction. No numerical enumeration was launched.

## Exact residue representation

Let S={a_1,...,a_s}, R=product_a(X-a), and

    P_e(X)=sum_a e_a R(X)/(X-a).

Then P_e(a)=e_a R'(a), and deg P_e<=D iff

    sum_a e_a a^j=0 for j=0,...,s-D-2.           (1)

These are necessary AND sufficient, by expansion at infinity. Taking
s above about2.313D gives precisely the deep-moment regime needed to
evade the new fixed-singular-cover theorem near quarter-rate first-order
agreement. There is no free degree reduction from increasing s.

## Fixed alphabets: limitation and exact list-to-line reduction

Suppose on EVERY coordinate of the evaluation domain all candidate
values belong to a fixed set of size at most b. Then any full-support
bad witness must agree at a coordinate with g(x)!=0: if g vanished on
its whole support, G=0 would be a common direction. At a nonzero-g
coordinate the received value f(x)+zg(x) visits each candidate value
at at most one label. Therefore there are at most bn bad labels,
independently of the number of candidates or the moment equations.

The qualification EVERY coordinate is essential. A residue alphabet
controls values only on its root core S. Suppose a fixed word f on S
has L distinct degree-D candidates with at least A0>D agreements.
Add one fresh coordinate x0, set g=0 on S, g(x0)=1, f(x0)=0. At label
z=P(x0), candidate P has at least A0+1 agreements. A common direction
would vanish on more than D core points and hence identically, but it
must equal1 at x0; thus the witness is bad. If the P(x0) are distinct,
this gives L bad labels. The core's large list itself is the required
source; the residue representation has not supplied it.

For a finite list one can ensure distinct evaluations by choosing x0
outside the roots of all pairwise differences. At most D*binom(L,2)
coordinates are forbidden. This works in a sufficiently large field
without changing existing candidates. In an extension of the core field,
a coordinate of minimal-polynomial degree greater than D automatically
separates all distinct degree-D candidates. However, the resulting
labels generally lie in that extension, not in the prime scalar-label
set. This distinction matters for the intended target.

Thus a constant-alphabet residue construction has two outcomes: on its
root domain it is linearly bounded; after adding a separator coordinate,
it is exactly the existing missing large-nearest-list problem. This
branch is stopped until a scalable deep-moment identity is available.

## The simplest genuinely cubic challenge alphabet: {0,1,z}

Assume s>=D+2, as holds in the target deep-moment regime.
Partition S into disjoint B,C and the remaining roots, and take residues
1 on B, z on C, and0 elsewhere. The degree condition becomes

    U_j+z V_j=0,
    U_j=sum_{a in B}a^j, V_j=sum_{a in C}a^j,
    j=0,...,s-D-2.                              (2)

This is a concrete three-branch formulation rather than an unspecified
cubic equation. It could in principle exploit the interference window
2.313D<deg T<=3D that the monic quadratic theorem does not cover.

### Prime scalar labels, with s<p

The zeroth moment gives

    |B|+z|C|=0 in F_p.

For a nonzero candidate, C is nonempty, so
z=-|B|/|C| belongs to F_p. Only O(s^2) cardinality-ratio labels are
possible. This does not exclude a quadratic lower bound, but all the
remaining moments now require

    (1/|B|) sum_B a^j = (1/|C|) sum_C a^j

through linear depth s-D-2 (when B is nonempty). In particular an
arbitrary choice of B,C or a larger Sidon root set is insufficient.
The normalized empirical moment identities are the precise missing
constructive input. If the challenge label is0, B must be empty and
the resulting residue vector is zero, so it supplies no nonzero candidate.

### Extension labels over a prime-field root set

If S lies in F_p, s<p, and z lies outside F_p, then (2) implies U_j=V_j=0
separately. Already j=0 forces B=C=empty. Thus the proposed family has
NO nonzero off-prime-label candidates, irrespective of higher moments.
At the full prime domain s=p, the same count argument permits only an
empty set or the entire domain for B or C. Disjointness leaves the
constant/affine families P=R' or P=zR' (and zero); for R=X^p-X these are
constants -1 or -z. They do not create this superlinear mechanism.
This obstruction does not cover extension-field root sets with more
than p points; those are a different domain regime.

More generally, affine residue branches over F_p satisfy moment
conditions U_j+zV_j=0. At any z outside F_p the two coefficient families
must separately satisfy the degree condition. Each selected branch mask
then extends to an affine codeword pencil for all z, rather than being
an isolated polynomial solution at that label. On the full root domain,
any bad agreement must involve a nonpersistent branch/received-line
intersection, giving at most b*s labels across all masks. With both
branches and received line over F_p, those intersections lie in F_p,
so there are no off-prime full-support bad labels from these masks.

## Why a cubic residue condition is not yet a first-order family

At a root a of R, the three allowed values satisfy
P(P-R')(P-zR')=0. Hence this product is divisible by R for every such
candidate. It does NOT follow that

    R P' = P(P-R')(P-zR')

or any fixed first-order identity holds. The quotient of the cubic by
R is generally candidate-dependent and need not equal P'. Indeed

    P'(a)=e_a R''(a)/2
           +R'(a) sum_{b!=a} e_b/(a-b)

when characteristic is not2. Thus a proposed differential equation
adds nontrivial coupled conditions to (2), rather than following from
the rootwise value branches. Deep moments must be checked first, then
actual agreement, and only then a common differential identity.

## Decision

The concrete cubic test produced a precise distinction: a possible
O(s^2) prime scalar-label window remains, but it requires new deep
normalized-moment identities; the natural extension-label version is
impossible for a prime-field root set. The fixed-alphabet route adds
no source beyond the existing nearest-list problem. Stop this bounded
exploration here rather than enumerate masks or recycle cyclic seeds.
A restart requires an explicit family of disjoint B,C satisfying (2)
at linear moment depth, with enough distinct cardinality ratios and
an actual received-line agreement proof.
