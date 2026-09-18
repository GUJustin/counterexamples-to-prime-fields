# Seven cubics on the Fano triples and their complements require characteristic two

## Statement

Let the seven Fano lines, in order, be

    L0=123, L1=145, L2=167, L3=246,
    L4=257, L5=347, L6=356.

There are no seven distinct degree-at-most-three polynomials over a field of characteristic different from two, on fourteen distinct nodes t_l,b_l, whose selected agreement sets have the following pattern: the candidates indexed by L_l agree with the received value at t_l, and the candidates indexed by the complement of L_l agree at b_l. Each candidate would have seven selected agreements. The theorem concerns this precise incidence design, not all seven-cubic half-agreement configurations.

## Saturation of the difference roots

Every pair of candidates belongs together to one Fano triple and to two complementary quadruples. Hence P_i−P_j, which is a nonzero cubic or lower-degree polynomial, has three prescribed distinct roots. It is a nonzero scalar multiple of their cubic locator.

Fix a Fano line {i,j,k}. The three differences P_i−P_j, P_i−P_k, P_j−P_k share the factor belonging to t_l. Dividing their identity by that factor shows that the following three binary quadratics are linearly dependent: for each pair, take the quadratic with roots at the two b-nodes whose Fano lines avoid both members of the pair. The triple-node locations have disappeared entirely.

Work projectively with binary cubics and quadratics. A projective coordinate change preserves the difference identities and their roots. Since the b-nodes are distinct, normalize

    b0=infinity, b1=0, b2=1, b3=u, b4=v, b5=w, b6=z.

The remaining u,v,w,z are finite, pairwise distinct, and different from0,1. A finite root pair r,s has coefficient row (1,−r−s,rs). A root pair infinity,s has row (0,1,−s). Linear dependence means the determinant of the corresponding three rows is zero.

## Three equations already contradict distinctness

For L2={1,6,7}, the three pair-avoidance root pairs are

    {b4,b5}, {b3,b6}, {b0,b1}.

Their determinant gives

    E2=−uz+vw=0.

For L3={2,4,6}, the pairs are

    {b2,b6}, {b1,b5}, {b0,b4},

and the determinant gives

    E3=vw−vz−v+z=0.

For L5={3,4,7}, the pairs are

    {b2,b4}, {b1,b3}, {b0,b6},

and the determinant gives

    E5=uz−vz+v−z=0.

(The pair order is inherited from increasing candidate indices.) Therefore

    E3−E5−E2=2(z−v)=0.

In characteristic different from two this forces b6=b4, contradicting node distinctness. This completes the proof without assuming that an abstract Fano matroid must be represented by the candidate coefficient vectors.

## Exact check and scope

`necessary.py` constructs all seven pair-avoidance determinants directly from the incidence sets, then factors them in four variables. The complete equations are in `necessary.json`. An additional rational Groebner computation returns u=z,v=z,w=z, but that stronger computational output is not needed: the displayed three-equation linear combination is the proof. The job completed in0.57seconds under the repository's384MiB/60second limits; `resources.json` records the run.

The argument remains valid over algebraic extensions and after any projective coordinate normalization. It does not prove that the incidence design exists in characteristic two, and it does not exclude other support patterns for seven cubics. In particular, it closes this specific proposed characteristic-zero construction and its power-pullback descendants; it is not a general seven-word list upper bound.
