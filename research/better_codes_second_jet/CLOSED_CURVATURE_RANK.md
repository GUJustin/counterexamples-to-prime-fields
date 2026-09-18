# Curvature-linear rank saving: recovered specialization

**Priority correction.** This rank bound and its challenge grading are already contained in the restored `SecondJetCounts.rankBound` / `local_rank_le_count` framework in `tmp/current-lower-primary-cache/LowerGeometry.lean`. The derivation below is a simpler specialization to curvature cap one, not a new rank theorem. See `RESTORED_FRAMEWORK_PRIORITY.md` for the exact algebraic identification. The restored files also contain general second-jet routing with a retained divisibility alternative; applying it at the new target still requires the correct support, reserve, activation, and numerical gates.

Fix integers m>=2S and a field of arbitrary characteristic. Write t for the local coordinate and use source variables Y,R,V. Enlarge the source to all monomials t^a Y^i R^j V^k with 0<=a,i<m, 0<=j<=S and k<=1. Terms with i>=m would map to zero anyway. Restricting this source by a jet-degree or weighted-degree cap can only lower rank.

Consider the map Y -> tR−t²V+t³E modulo t^m. Its rank satisfies

    R <= 2R0 − S(2m−S−3)/2,
    R0 = (S+1)[3m²+3(1−S)m+S(2S+1)]/6.

This is a sufficient upper bound, not a conjecture based on the numerical ranks. PRIORITY CORRECTION: subsequent inspection of the restored primary LowerGeometry.lean located the same rectangular rank and graded count in SecondJetCounts. This proof is a recovered specialization and independent verification, not a new mathematical rank theorem.

## Baseline and additional kernel vectors

The first-jet substitution Y -> tR+t²E has rank R0. In its block of t-degree r before the final contact substitution, the source is the rectangle of monomials u^i R^j with i<=r,j<=S. The kernel consists exactly of multiples of (u−R)^h, h=m−r. Its dimension is (r−h+1)(S−h+1) when h<=min(r,S), and zero otherwise. Summing source dimensions minus these kernel dimensions gives R0. The divisibility and degree argument works in every characteristic.

Write a curvature-linear source as A+VB. The direct sum of the two first-jet kernels lies inside the second-jet kernel: substitute E_first=−V+tE. Hence the baseline rank is at most 2R0.

Put z=Y−tR (this z is not the challenge variable). For b=1,...,S choose

    0<=i<=m−1−2b,  0<=j<=S−b,
    l=i+j,  a=m−1−i−2b,
    Q_(b,l)=t^a Y^i R^j z^(b−1)(z+t²V).

Choose one representation (i,j) for each l. The possible l are exactly 0,...,m+S−1−3b. If m=2S and b=S this interval is empty and contributes zero.

The second-jet substitution gives t-order at least

    a+i+2(b−1)+3=m,

so every Q is a kernel vector. Its slope degree is at most j+b<=S, curvature degree at most one, and total jet degree is l+b<=m+S−3. Every expanded source t and Y exponent is below m.

Under the direct pair of first-jet maps on (A,B), its image is

    t^(m−1) R^l (E^b, E^(b−1)).

These vectors are independent already in their first components. Thus their classes are independent modulo the embedded pair of first-jet kernels. Their number is

    sum_(b=1)^S (m+S−3b) = S(2m−S−3)/2,

proving the rank bound. No assumption that the actual global extraction fills the local ambient box is used.

## Exact source count and finite comparison

For n=262144, w=131071, target agreement A=181275, source contact budget mA, slope cap S and curvature cap K in {0,1}, set J=floor((mA+S+2K−1)/w). For each j<=S,k<=K put

    B=mA−(w−1)j−(w−2)k,
    q=min(J−j−k,floor((B−1)/w)).

If q>=0 its coefficient contribution is (q+1)B−wq(q+1)/2. The jet-degree moment contribution is

    Bq(q+1)/2−wq(q+1)(2q+1)/6
      +(j+k)[(q+1)B−wq(q+1)/2].

Write their sums as C and M. With challenge degree constrained jointly by jet degree plus challenge degree <=L, the source dimension is exactly (L+1)C−M. The conservative constraint bound n(L+1)R therefore gives a sufficient source gate. It is not the tighter degree-graded constraint count.

The reproducible script curvature_upper_gate.py checks the formula against all twelve existing exact matrix ranks and tests the single shape S=max(1,round(.31m)), m=2,...,512. The first positive first-jet slope is m117, S36, J161, contact budget21209175 and C−nR=1029969. The first positive curvature-linear slope is m72, S22, J99, contact budget13051800 and C−nR=312222. Thus this particular sufficient gate becomes positive at smaller finite multiplicity; first-jet existence itself was already possible.

At m96 the first-jet slope is −32862387, while the curvature-linear slope is80969070 and the conservative sufficient challenge cap is37350. At m128 both slopes are positive; conservative sufficient challenge caps are166523 and28741 respectively. These challenge caps deliberately use the loose n(L+1)R bound and are not optimized.

## Scope

The repaired full benchmark ledger still costs296022915414629475 against allowance274980720453263170: the needed reduction is21042194961366305, approximately7.65 percent of the allowance. A rank percentage cannot be subtracted from that ledger. This result establishes a useful finite source-existence improvement. It does not by itself supply a complete characteristic-valid benchmark receipt. A general second-jet helper/counting theorem already exists in the restored framework; its target-A port and activation conditions must be checked. It does not establish a new capacity threshold or a better.codes score.

## Graded challenge bound

The contact map preserves total jet degree ell (total degree in E,R,V), and received-value translation preserves the filtration ell+challenge degree<=L. The preceding proof is homogeneous in ell. It therefore gives a stronger challenge rank bound without any new numerical rank computation.

For the first-jet block r let h=m−r, d_r=(r+1)(S+1), and subtract k_r=(r−h+1)(S−h+1) if h<=min(r,S), otherwise k_r=0. Both the rectangle and the shifted kernel rectangle have mean jet degree (r+S)/2. Consequently

    T0=sum_(r=0)^(m−1) (d_r−k_r)(r+S)/2

is the first-jet rank's degree moment. The pair A+VB has baseline rank2R0 and moment2T0+R0. Its additional kernel vectors have ell=l+b, so their degree moment is

    Tsave=sum_(b=1)^S [b q_b+q_b(q_b−1)/2],
    q_b=m+S−3b.

Put R=2R0−sum q_b and T=2T0+R0−Tsave. For L>=m+S the enlarged source's challenge rank is at most

    (L+1)R−T.

This follows degree by degree from subtracting the independent homogeneous kernel classes; it does not require the ungraded bound to be exact. All enlarged nonzero image degrees are at most m+S, so each weight L+1−ell is positive. Restricting the original source by J can only reduce rank, even if J does not contain the entire enlarged rectangle.

The resulting global source-dimension lower bound is

    (L+1)(C−nR)−M+nT.

For the first-jet comparison use R0,T0. The exact arithmetic implementation graded_curvature_gate.py gives: m96 curvature L7109; m117 first-jet L613675 and curvature L5625; m128 first-jet L31890 and curvature L5515. The last curvature gate has kernel dimension at least53746080. At the first positive curvature multiplicity m72, the improved sufficient L is578963. These are source-existence certificates only; the routing and full benchmark limitations above remain in force.

The first-jet graded refinement is already present in the pinned benchmark local-rank formula; it is not a new first-jet optimization. For example its m117,S36,L613675 value matches the independently repaired primary-A source. The curvature-linear graded kernel saving was initially thought new, but is also a specialization of the restored SecondJetCounts formula; that novelty claim is withdrawn. Here T denotes the moment of an upper-rank profile; it is not asserted to be an independent lower bound on the actual rank moment.
