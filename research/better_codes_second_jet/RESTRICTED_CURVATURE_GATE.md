# Curvature-linear source: exact restricted local rank

This tests a genuinely different constraint relation: retain a first-derivative cap and introduce the second Hasse derivative with exponent at most one. The earlier dense second-jet experiment removed that cap and consequently paid a much larger ambient rank. This note derives an exact finite-field local rank computation rather than assuming independence of the constraints.

## Benchmark requirement

The fully repaired target ledger costs296022915414629475 against MCA allowance274980720453263170. It must lose at least21042194961366305, approximately7.65% of the allowance. The critical singleton costs288191873412750740. These are full downstream counting quantities. A percentage improvement in the interpolation rank cannot be subtracted directly from either ledger number.

## Independently checkable local-rank lemma

At a received coordinate put t=X−x. For an agreeing polynomial P, backward Taylor gives

`P(x+t)−P(x)=t P^[1](x+t)−t² P^[2](x+t)+t³ E(t)`.

Thus consider the exact linear substitution map over the pinned prime field

`Y -> tR−t²V+t³E`, modulo t^m,

on source monomials t^a Y^i R^j V^k with 0<=a<m, j<=S, k<=K, and i+j+k<=J. Here K=1 is the curvature-linear case. Its rank R_m,S,K,J is a uniform upper bound on the local constraint rank of the global weighted source. Translating a received value out of Y preserves these caps. Translating X merely changes coefficients within the ambient truncated t-space. We impose a sufficient identity for arbitrary formal E,R,V; no assumption is made that all such jets arise from an actual candidate.

The map decomposes into blocks indexed by

`ell=i+j+k`, `h=a+i−k`.

Indeed selecting b factors t³E and v factors −t²V from Y^i gives coefficient

`(−1)^v binom(i,b) binom(i−b,v)`

and output monomial

`t^(a+i+v+2b) E^b V^(v+k) R^(i−b−v+j)`.

Both ell and h are recoverable from the output: ell is total E,V,R degree, and h is t-degree minus V-degree minus twice E-degree. Outputs belonging to different blocks are disjoint. Consequently summing exact matrix ranks of these blocks gives the exact rank of the ambient map. Each block has at most (S+1)(K+1) columns, since i and a are fixed once ell,h,j,k are specified.

This is a proved block decomposition. The numerical matrix ranks below are exact arithmetic over the actual pinned prime p=2130706433, not floating-point or characteristic-zero generic ranks.

## Source count and challenge degree

For n=262144, w=131071, A=181275 and degree budget mA, the scalar weighted source count is

`C=Σ_(j<=S,k<=K,i+j+k<=J) max(mA−wi−(w−1)j−(w−2)k,0)`.

Thus C−nR>0 is a sufficient scalar source-existence gate. For line challenge Z and total degree i+j+k+z<=L, the coefficient count becomes

`C(L)=Σ (L+1−i−j−k) max(mA−wi−(w−1)j−(w−2)k,0)`.

After translating the affine received value f_x+Zg_x out of Y, the image is contained in the tensor product of the same local jet box and polynomials of Z-degree at most L. Hence n(L+1)R is a valid conservative global constraint bound. The large-L dimension slope is exactly C−nR for this sufficient bound. A positive slope would establish a line-source existence certificate for sufficiently large L, but still not a routing certificate or characteristic-valid full counting receipt.

## Bounded verification and interpretation

`restricted_curvature_rank.py/json` records the finite comparisons. Eight tiny cases compare the block calculation with a single unblocked matrix. Every K=0 case also reproduces the independent closed first-jet rank formula

`6R=(S+1)[3m²+3(1−S)m+S(2S+1)]`.

At m32,S10,J44, the first-jet source has R=4433,C=1146617615. The curvature-linear source has R=8611,C=2236636138, improving the ratio R/C by about0.4184%. Its dimension slope remains−20685846; lowering the local rank by79 would suffice for positivity at this particular shape. The computation demonstrates actual useful cross-jet dependencies, but not yet a positive global source gate at this shape.

The full data and watchdog report also include the parent-authorized m64 comparison. Their result must be read together with the downstream limitation below; no exact local-rank gain is itself a7.65% ledger repair.

## Remaining proof requirement

The existing helper/factor receipt is built for variables Y,R,Z. A V-dependent source has a new degree profile and its derivative geometry introduces the next derivative. Before propagating any candidate into the benchmark, one needs a valid counting/routing theorem for curvature-linear factors, including characteristic and all source/avoidance gates. The present result is the exact restricted rank lemma and its bounded finite verification. It neither supplies that missing theorem nor justifies substituting the rank gain into the old first-order ledger.
