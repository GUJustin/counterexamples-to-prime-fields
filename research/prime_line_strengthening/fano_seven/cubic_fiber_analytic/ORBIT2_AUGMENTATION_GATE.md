# Orbit-2 seven-cubic bank: complete cubic-cover support reduction

The positive number-field bank is `../orbit2_number_field.json`, over q³−10q²+3q+1. Its independently verified affine chart, word, and seven cubic coefficient arrays are in `../orbit2_independent_field_audit.json`. Use this affine chart before composing with a cubic. The first seven nodes are quad nodes and the last seven are triple nodes, in the original design order.

Consider a separable three-point cover ψ(U)=U³+aU+γ of all fourteen nodes, and a proper witness N(U)/(U-b) with deg N≤10 and b outside the domain. All arguments and the degree-nine norm in `FIBER_PATTERNS_AND_LINEAR_GATE.md` apply unchanged: properness implies C≠0, f≤2, d+3f≤9, and f=2 implies d≤3. Pair intersections force exactly21 agreements, with at least14 on triple fibers.

## Only two patterns survive

Let M and Q be the seven-by-seven incidence matrices whose columns are respectively `T` and `Q` in `orbit2_patterns.json`. These are the actual, non-Fano orbit-2 matrices. Direct integer arithmetic gives det M=−6, det Q=8; both row sums are respectively3 and4.

* If f=2, the same counting as before forces two full and three double triple fibers and all quad fibers single. The extra triple multiplicity vector v has entries 2,2,1,1,1,0,0, but pair saturation forces Mv=3·1. Invertibility forces v=1, contradiction.
* If f=0, all triple fibers are double. Pair saturation Qb=4·1 forces every quad fiber single.
* If f=1, the full fiber is triple. No triple fiber is empty and at most one is single. If all six other triple fibers are double, there is one empty quad fiber. Its incidence block must contain the full triple block. The only such containment is T[2]={1,5,6} inside Q[4]={1,3,5,6}, with indices starting at zero.
* If one triple fiber is single, either every quad fiber is single, contradicting M(e_i−e_k)=0, or one quad is double and one empty. The latter requires M(e_i−e_k)=Q(e_l−e_j). The two sets of 42 nonzero column differences are disjoint, as can be checked directly from the displayed integer incidence columns. Thus this case is impossible.

Consequently the complete patterns are:

1. Triple multiplicities (2,2,2,2,2,2,2); quad multiplicities (1,1,1,1,1,1,1).
2. Triple multiplicities (2,2,3,2,2,2,2); quad multiplicities (1,1,1,1,0,1,1).

`orbit2_patterns.py` independently enumerates every seven-tuple of multiplicities in {0,1,2,3} for each bucket, then applies the total agreement, full/double-fiber norm, and all seven pair bounds. Its exact output is precisely these two patterns. Unlike the aligned Paley pattern, only one full/empty pair is possible. This does not establish existence or nonexistence of a rational witness.

## Generic word: still a five-by-three gate

Let x_0,...,x_6 be the affine triple nodes and W the degree≤6 polynomial interpolating their received values. At each triple fiber choose an omitted root t_i of ψ(U)=x_i; at a full fiber choose any root. For C=c_0+c_1X+c_2X², interpolate T(x_i)=C(x_i)t_i and R(x_i)=C(x_i)t_i², with deg T,R≤6. Then

    B=W+T,  A=R+aC−bW.

The three equations T_l=−W_l, l=4,5,6 enforce deg B≤3. The other three equations R_l=bW_l enforce deg A≤3. In this bank at least one W_k, k∈{4,5,6}, is nonzero: otherwise W itself would be the excluded eighth cubic matching all seven triple nodes (verified independently in `orbit2_independent_field_audit.json`). Choose such k and eliminate the pole:

    b=R_k/W_k,
    W_k R_l−W_l R_k=0  for l∈{4,5,6}\{k}.

This gives five affine linear equations in the three coefficients of C, exactly as in the Paley gate, with different constants. For pattern2 impose additionally C(x_2)=0 and omit quad index4 from required matching. Pattern1 requires one match on every quad fiber. Singular systems must be preserved as affine solution spaces. Reconstruct N=A(ψ)+UB(ψ)+U²C(ψ), then test N(b)≠0, pole exclusion, and actual agreements. A candidate for pattern2 can also arise in the unrestricted gate because changing the omitted root on its full fiber has no effect.

For a completely general base word whose three high W coefficients all vanish, retain the six equations with b free; do not divide by a zero pivot. That exceptional branch does not occur for the archived orbit-2 bank.

## Constructive scope

This bank supplies genuinely different affine nodes and word coefficients, so its five-by-three systems are a new augmentation family. The combinatorial possibility of two full fibers, however, is closed by its invertible triple incidence matrix; the new opportunity is algebraic, not a larger class of multiplicity patterns. No shift-zero rank classification has yet been performed for this bank, and the Paley cyclotomic no-go does not transfer to it.
