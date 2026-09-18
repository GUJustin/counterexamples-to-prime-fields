# Exact support ledger for a possible second one-pole step

**Conclusion:** the proposed twelve-singleton-transversal obstruction is valid,
but degree/incidence counting does NOT exclude all possible14-match supports.
Several explicit support patterns satisfy every intersection bound, including
the even-core parity bound. They are only combinatorial possibilities, not
constructed rational witnesses.

## Setup and notation

The first extension has26 paired-core points: two lifts of each of the12
old base nodes, plus the two-point pole fiber. Each base node is indexed by
an edge ij of K4 and a sign. Exactly the two old lifted words G_i,G_j match
there. The first rational witness picks one sign on every edge; call these
the positive edges for this ledger. G5 matches both lifts of those six
positive base nodes and none of the six negative ones. At the pole fiber,
all four old words match and G5 does not. At each of the two fresh points,
only G5 matches.

The last claim holds for the explicit lift: N-DH_i has already exhausted
its three roots at old agreement nodes, so a fresh point whose base image
is outside the old domain cannot be an additional G5/G_i intersection.

For a prospective proper degree-at-most-seven numerator over T-beta, its
difference from any of these five degree-at-most-six polynomials is a
nonzero numerator of degree at most seven. Each old-word intersection
therefore has at most seven points.

Choose a14-element proposed agreement support. Let f be its number of fresh
points and p its number of pole-fiber points. Put x_ij^+,x_ij^- in{0,1,2}
for the number of lifts chosen at each of the12 base nodes. Write

    b=sum x_ij^sign =14-f-p,
    k=sum x_ij^+.

The necessary intersection conditions are

    sum_(j!=i)(x_ij^+ + x_ij^-) + p <=7   (each old word),
    k+f<=7                               (G5),
    0<=f,p<=2.

Summing the four old-word inequalities gives b+2p<=14, or p<=f.

## Valid obstruction for the proposed transversal

If both fresh points are used, exactly12 core points remain. A transversal
choosing one point over EACH of the12 old base nodes, with no pole points,
has k=6. Together with the fresh points this makes eight intersections with
G5, impossible for a nonzero degree-seven difference numerator. This proves
the root's proposed obstruction to that specific support.

## A further parity restriction

On the paired core the received values are even in T. Write a candidate
numerator as N_e(T^2)+T N_o(T^2), with degrees at most three, and normalize
its denominator to T-beta. Matching both signs above a base value z forces

    N_e(z)+beta*N_o(z)=0.

This polynomial has degree at most three and is nonzero: an identity would
make N=(T-beta)N_o(T^2), contradicting properness. Hence at most THREE
paired-core fibers can be selected in full. The pole fiber counts as one
such fiber. This argument assumes characteristic different from two, as in
the characteristic-zero construction.

## Explicit feasible support patterns

Label one edge12 and its complementary edge34. In the following, a singleton
means either one of the two lifts; the choice is not yet constrained.

* f=2,p=0: omit the positive12 base fiber; take both lifts of the negative12
  base fiber; take one lift of every other base fiber. There are12 core points,
  k=5, and each old word has six core intersections. Adding the fresh points
  makes seven G5 intersections. Only one paired fiber is doubled.

* f=1,p=1: take one lift over every old base node, one pole point, and one
  fresh point. Every old word has exactly seven intersections, G5 has seven,
  and no paired-core fiber is doubled.

* f=0,p=0: start with one lift over every old base node and add the second
  lift at positive12 and negative34. There are14 core points. Each old word
  has exactly seven intersections, G5 has seven, and exactly two fibers are
  doubled.

All these patterns satisfy the degree-seven bounds and the at-most-three-
full-fibers parity condition. In particular there is no combinatorial no-go
for all12-point core supports when both fresh points are selected.

The second pattern has a useful saturation feature: all FIVE old-candidate
intersection budgets are exactly seven. That may impose further polynomial
identities worth studying, but this ledger does not solve them. No existence
of a degree-seven one-pole witness follows from support feasibility alone.
