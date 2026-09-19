# Arbitrary-label linear bound for the torsion-multiple quintic family

September 19, 2026. Root proof; independently checked by Audit and Practical. The independent proof and the degenerate syndrome-line case are recorded in [TORSION_LIFT_DISJOINT_EXTRAS_LINEAR_BOUND.md](TORSION_LIFT_DISJOINT_EXTRAS_LINEAR_BOUND.md).

**Result.** The 3/7-fiber construction with extras at multipliers 1,2,4,5,6 supplies exactly ell*n distinct supports, but at most **2n distinct exceptional projective challenges** on a genuine received syndrome line with a far endpoint. This holds for arbitrary challenge labels and arbitrary error values. Thus this particular moving-quintic construction cannot give the desired superlinear counterexample. It does not close the general norm-quintic family.

## A support lemma

Let C be a linear code of minimum distance d. Write S(A) for the syndrome image of vectors supported on a coordinate set A. Fix a core B and pairwise disjoint petals J_i, all disjoint from B. Suppose

    |B| + |J_i| + |J_j| + |J_l| < d

for any three distinct petals. Let L be a two-dimensional syndrome space. Suppose L is not contained in any S(B union J_i), and is not contained in S(B).

Then at most two distinct projective points of L belong to the union of the spaces S(B union J_i).

Proof: each individual support space contains at most one projective point of L, since two distinct points span L. If three distinct points existed, choose representing errors e_i,e_j,e_l on three distinct supports. In a two-dimensional space their syndromes have a dependence with all three coefficients nonzero. The corresponding combination of errors is a codeword supported on B union J_i union J_j union J_l. Its weight is less than d, so it is zero. On each petal only one error contributes, forcing that error to vanish on its entire petal. All three syndromes therefore lie in S(B). Two distinct ones span L, a contradiction.

This argument uses no assumption that errors are nonzero throughout their allowed support.

## Application to the torsion construction

Let ell>14 be prime, in odd characteristic different from ell, and assume E[ell] is rational. Take the domain of nonzero torsion x-coordinates,

    n=(ell^2-1)/2,   k=n-4ell+1,   d=n-k+1=4ell,
    T=n-2ell-5.

For each order-ell subgroup H and each nonzero signed quotient class {q,-q} in E[ell]/H, fix one sign q. There are ell lifts P of q. The common core B is the union of the two paired fibers tagged by 3q and 7q, of size 2ell. The petal attached to a lift P is

    J_P = {x(jP): j in {1,2,4,5,6}},

of size five. These petals avoid B. They are pairwise disjoint as P ranges over the ell lifts: equality x(jP)=x(j'P') implies j q = +/- j' q. The five multipliers are distinct modulo sign, so j=j' and the sign is positive; multiplication by j is invertible on E[ell], giving P=P'.

Three supports in this bank have union size 2ell+15, which is less than d=4ell for ell>14. The support lemma applies.

In detail, let received words f,g define a genuine two-dimensional syndrome space L. Assume some word on this line has agreement strictly less than T with C. If L were contained in S(B union J_P), every word on the line would be equivalent modulo C to an error on at most 2ell+5 coordinates, hence would have agreement at least T. If L were contained in S(B), the agreement would be at least T+5. Both contradict the far-word assumption. Thus this bank supports at most two distinct projective challenges.

There are ell+1 choices of H and (ell-1)/2 signed nonzero quotient classes per H. The number of banks is exactly n. Taking the union of their challenge sets gives

    number of distinct exceptional challenges <= 2n.

Possible collisions between different banks only reduce this upper bound. No challenge injectivity is assumed. At ell=23 the construction has 6072 distinct supports but at most 528 distinct challenges under the stated far-word hypothesis.

## Scope and consequence

The bound applies to every subbank of the proposed torsion-multiple family, every assignment of labels, and every choice of error amplitudes. It is stronger than the finite norm-label rank certificate, which tested one labeling on one curve. There is no need to run the proposed larger Plucker calculation for this family.

The argument does not exclude arbitrary moving quintics, different parameter families with overlapping petals, or a larger number of quotient-class banks. It identifies the obstruction precisely: within each fixed quotient class, the varying extra supports are disjoint, and their three-support union is smaller than the code's minimum distance.


## Independent actual-text signoff

Audit read the complete saved proof and checked the strict minimum-distance inequality, the three nonzero dependence coefficients, disjointness of the lift petals modulo sign, the far-word implication for both support-space exclusions, and the exact n-bank count: PASS. The bound allows arbitrary partial errors and arbitrary subbanks. It is scoped to this torsion-multiple family and does not exclude general moving norm quintics. The independent derivation is also recorded in `TORSION_LIFT_DISJOINT_EXTRAS_LINEAR_BOUND.md`. No Plücker computation is needed or claimed.
