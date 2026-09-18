# Independent audit of the Paley F29 norm-net filter

PASS, with strictly finite-field scope. The target excluded is a whole geometrically integral genus-zero curve whose parameter is in P2(F29). A reducible member is not being called a high-genus integral curve; it is simply not such a target. This is not a characteristic-zero or algebraically closed parameter-plane exclusion.

## Charts and absence of artificial boundary components

The four disjoint charts/point sets used by count.py are:

1. finite X,Y:29^2 points;
2. finite X,Y=infinity:29 points, equation v^10 H(X,1/v) at v=0;
3. X=infinity, finite Z=Y/X^3:29 points, equation t^34 H(1/t,Z/t^3) at t=0;
4. their corner:one point, equation t^34 v^10 H(1/t,1/(t^3v)).

These are exactly the900 F29 points of F3, with no overlap. The exponents34-k-3l are nonnegative by the source flags. Every nonzero member has Y-degree10 by the independently verified leading projection. Also the three infinity restrictions are

    23 Z^8+10Z, 15Z^9+7Z^2, 20Z^10+2Z^3.

Their supports are disjoint. Hence no nonzero parameter has lower coefficient excess than4: no artificial infinity-fiber component is introduced by homogenization to the common class. The negative section is not an artificial component either. This check is essential before interpreting the homogeneous curve point counts.

## Normalization point counts

A smooth rational point contributes exactly one point of the normalization over the same field. At an ordinary multiplicity-m point, the squarefree homogeneous tangent cone has m distinct geometric directions; its rational directions are precisely the rational normalization branches. The code tests squarefreeness both in the finite slope polynomial and at the infinity direction. A simple rational direction remains a unique smooth rational branch even when other tangent directions are repeated. Thus such simple directions can safely be counted as a lower bound at a nonordinary point.

Every rational normalization point maps to a rational image point. Consequently examining every rational point of F3 is sufficient: no rational normalization point is hidden over a nonrational image point. When all rational singularities encountered are ordinary, the resulting count is exact even if nonrational singularities exist. Otherwise ignoring unresolved branches gives a lower bound.

A smooth projective geometrically integral genus-zero curve over Fq has q+1 rational points. Therefore a lower bound exceeding q+1 excludes this target; an exact count different from q+1 also excludes it. No conclusion is drawn from an unresolved lower count.

## Independent replay

`independent_count.py` independently rebuilds the four chart equations from gate.json, enumerates all900 points and all871 projective parameters, and uses FLINT univariate gcd/derivative arithmetic for the tangent-cone test instead of the original handwritten polynomial Euclidean routine. It checks every smooth count, ordinary singularity record, unresolved count and classification against count.json.

Results agree exactly:

*828 members:known normalization count>30;
*14 members:exact count different from30;
*21 members:exact count30;
*8 members:nonordinary unresolved by that first pass.

The remaining28 nonsymmetric parameters are exactly the mu7 orbits of (1,1,17),(1,4,1),(1,8,15),(1,8,20), with action (1,a,b)->(1,a*zeta^(2j),b*zeta^(4j)). The additional unresolved point is the eigenmember(0,1,0), excluded by the independently audited Kummer genus bound. The replay completed in1.07seconds using35MiB.

## F841 checks and final nonordinary point

I inspected count2.cpp's arithmetic: it realizes F841=F29[s]/(s^2-2), valid since2 is nonsquare modulo29; the four surface chart loops are disjoint and complete. Hasse derivatives, inversion by exponent839, and homogeneous infinity-root accounting are consistent with the first pass. The saved counts for the four representatives are respectively844,974,841,930, with only the third having an unresolved point. These full F841 counts were code-audited, not independently recomputed in a second implementation here.

For the third representative, independent Taylor expansion at(1,1) gives multiplicity4 and cone

    14+3T+8T^2+26T^3+11T^4
      =11(T-9)^2(T^2-6T-9)  modulo29.

The quadratic discriminant is14, nonzero and nonsquare in F29. Its two distinct roots become rational in F841, remain distinct from9, and each gives a unique rational branch. Neither was counted in the old841 lower bound because that entire nonordinary point was omitted. Thus the valid lower bound is843>842. This excludes the last nonsymmetric orbit. The final partial-branch code update can record843 directly; the older count2.json value841 is a valid weaker lower bound and should not be silently described as an exact count.

Combining these checks excludes every P2(F29)-defined geometrically integral genus-zero member. It does not exclude members defined over extensions of F29 or prove a characteristic-zero no-go. A characteristic-zero rational member may have parameters specializing outside F29 or have bad reduction. No rental or rational parametrization task is warranted from these eliminated finite-field candidates alone.
