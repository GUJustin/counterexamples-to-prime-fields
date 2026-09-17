# Improved local-rank bound for an explicit YS source cap

The explicit source cap survives localization and gives a valid smaller local target. This yields an improved rank formula rather than only reusing the original unconstrained bound.

## Translated coefficient space

Pinned `LowerFoundation.lean`, namespaceRCN119, uses local variables(X0,X1,X2) and `slopeDifference=X0−X1`. At blockr, `blockEntry` is a sum of terms

 seedAffine(u0,u1)^(i−f) · X0^f X1^j X2^z,

withf≤r, where the global source monomial has original exponentsi,j,z and i+j≤Y. The polynomialseedAffine is a constant plus a multiple ofX2. Consequently every local monomial satisfies

 a≤M=min(r,L), b≤S, a+b≤Y, a+b+c≤L.

The addedYS inequality follows froma=f≤i andb=j; the seed expansion affects onlyc. This is uniform over nodes and received-word values.

Define the capped local coefficient box E(M,L,S,Y) by these four inequalities, and its dimension

 B(M,L,S,Y)=Σ_{a=0}^{min(M,Y,L)}Σ_{b=0}^{min(S,Y−a,L−a)}(L+1−a−b).

## Exact rank of the enclosing block jet

The existing `contactJet_eq_zero_iff` says its h-jet vanishes precisely when(X0−X1)^h divides the polynomial. Multiplication by this nonzero polynomial injects

 E(M−h,L−h,S−h,Y−h) into E(M,L,S,Y)

wheneverh≤min(M,L,S,Y), and its image is exactly the jet kernel on E.

For the converse, if nonzeroP=(X0−X1)^h Q is inE, each relevant degree is additive under multiplication over a field: ordinary degree inX0, degree inX1, weighted degreea+b, and totaldegreea+b+c. The factor has degreeh for all four degrees. ThereforeQ obeys precisely the four reduced caps. This remains true in small characteristic: the pureX0^h andX1^h coefficients remain nonzero. Ifh exceeds any cap, there is no nonzero kernel element. The zero polynomial is handled separately.

Thus the enclosing block rank is exactly

 B(M,L,S,Y)−B(M−h,L−h,S−h,Y−h)

whenh≤min(M,L,S,Y), and equalsB(M,L,S,Y) otherwise.

For the source interpolation map takeh=m−r and sum this quantity overr=0..m−1. This sum is a **valid upper bound on the actual local source rank**. It is exact for the direct sum of the enclosing block maps; we do not claim the restricted source extraction fills those blocks independently. That distinction does not affect the kernel-dimension lower bound obtained by subtractingn times this rank bound from the exact source coefficient count.

No new field-size or characteristic requirement is used by this rank argument. Existing vanishing/source hypotheses still apply separately.

## Constant-time block dimension

Let K=min(Y,L), and define

 F(K,L)=(K+1)(K+2)(3(L+1)−2K)/6 forK≥0,

withF=0 forK<0. Every nonzero call below satisfiesL≥K. Inclusion-exclusion gives

 B(M,L,S,Y)=F(K,L)
  −F(K−M−1,L−M−1)
  −F(K−S−1,L−S−1)
  +F(K−M−S−2,L−M−S−2).

This makes the complete rank boundO(m), with exact integer arithmetic. TheYS cap begins removing possible local rows whenY<m−1+S, not only whenY<m.

## Formal port and numerical status

Add the four-cap local box, its basis/cardinality lemma, multiplication and quotient-degree lemmas, and the restricted block-entry membership statement. Build the local target from the ranges of these restricted jet maps, then repeat the current product-target rank bound and rank-nullity proof. The existing original constraint map can alternatively be factored through this smaller target on the explicitly restricted source domain.

Frontier implemented this formula in `restricted_rank_probe.py`. It reports2401 brute block-count checks and agreement with the old local rank when theYS cap is inactive. For the single tested Source00 shape, kernel nullity was already negative at the first cap reduction producing a rank gain, and remained negative at the lower sampled caps. The bounded probe stopped there; this is not a global exclusion of different source shapes.

Status: mathematical derivation and implementation design, not a compiled Lean theorem.
