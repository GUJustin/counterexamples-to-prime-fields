# The cubic correction does not rescue the three-double-fiber pattern

## Scope

Enlarge the preceding second-step ansatz to

    A(y)=G_i(y)+h L3(y), B(y)=lambda L3(y),
    L3(y)=(y−a0)(y−r)(y−s), lambda!=0,

where a0 is the first rational witness's pole and r,s are two base matches of H_i. This allows a new cubic polynomial part rather than insisting on A=G_i. Even this family fails for every admissible four-parameter reciprocal-quadratic seed. The result does not exclude a general second one-pole witness with different double fibers or fewer double fibers.

On each of the six nonmatching base coordinates, let z=(y−r)(y−s)/(w−H_i). The single-match condition becomes

    y=c0+[b0+lambda z/(1−h z)]².

Thus y must be a rational function of z with numerator and denominator degrees at most two, with a denominator that does not vanish at the six tested coordinates. We prove that even an unrestricted degree-(2,2) rational map cannot work, so the perfect-square denominator and other pole guards need not be tested.

## Fixed cyclotomic verification

`../second_step_mobius.py` tests all sixty old-candidate/root-pair choices in exact Q(zeta_12) arithmetic using rows

    (1,z,z²,−y,−yz,−yz²).

Forty-eight matrices have trivial kernel. The other twelve have opposite correction roots r=−s. In these cases z has the same value at y and −y, making a defined rational map impossible. Their two-dimensional kernels consist of common-vanishing numerator/denominator polynomials, not valid maps. This bounded computation completed in under one second.

## Exact generic obstruction

Write the four nonzero seed parameters as a,b,c,d, with distinct squares. Fix H_a; its nonmatching nodes are ±bc,±bd,±cd. Opposite correction roots fail for the same parity reason. Otherwise signs and relabeling reduce to r=ab,s=ac.

For an edge uv among bc,bd,cd set

    t=uv,
    C=−(a²−u²)(a²−v²),
    U=a²(t²+a²bc), V=−a³(b+c)t.

Then z at y=±t is (U±V)/C. Clearing C² in the interpolation rows and taking half-sum and half-difference of the two rows produces

    (C², UC, U²+V², 0, −tVC, −2tUV),
    (0, VC, 2UV, −tC², −tUC, −t(U²+V²)).

Stacking these two rows for the three edges gives a six-by-six matrix. Its exact determinant is

    −a^20 b^4 c^4 d²
     * (a²−b²)^3 (a²−c²)^3 (a²−d²)^4
     * (b−c)² (b+c)^6 (b²−d²)² (c²−d²)².

Every factor is nonzero under the seed hypotheses. Thus there is no nonzero numerator/denominator coefficient vector, even before imposing a square denominator. The factorization is a polynomial identity certified by `second_step_mobius_symbolic.py` using exact polynomial-domain determinant arithmetic; its output is saved in the adjacent JSON file. The watchdog reports completion in 2.77 seconds with a 384-MiB/60-second cap and about 66 MiB peak RSS.

The old pole a0 cancels before this computation. Therefore choosing a different first one-pole witness, varying the quadratic critical value, or strategically moving the two fresh coordinates cannot evade the obstruction within this ansatz.

## What remains different

A successful second witness must leave this particular three-double-fiber pattern: it may use a double-match set not consisting of the first pole fiber and two matches of one old polynomial, or have fewer double matches and more single matches with a genuinely different cubic polynomial part. No conclusion about those cases is established here. The generic positive first-step identity remains valid.
