# Priority correction: the curvature-one rank bound was already in the restored framework

The claim that CLOSED_CURVATURE_RANK.md supplied a new curvature-linear rank theorem was incorrect. The cached primary LowerGeometry.lean already contains `SecondJetCounts.rankBound` and `local_rank_le_count` for the SAME rectangular first-derivative/curvature support, not merely a related relaxed flag. Our formula is its curvature-cap-one specialization. The numerical implementations and elementary proof can remain useful verification artifacts, but are not a novel rank or grading result.

## Exact identification

The restored source is `tmp/current-lower-primary-cache/LowerGeometry.lean`, namespaces `SecondJetSpace`, `SecondJetRank`, and `SecondJetCounts` (the scalar rank definition appears near line18803). The source has rectangular caps s1 on first-derivative degree and s2 on curvature degree. Its kernel uses

    q=max(ceil((m−r)/2), m−r−(s2−h)).

Set s1=S, s2=1, and d=m−r. At curvature index h=1, q=d, exactly the ordinary first-jet kernel. At h=0, q=d−1 for d≥2, and q=1 when d=1. Therefore the rank differs from twice the first-jet rank only by the extra kernel boundary at d=b+1, b≥1.

For fixed b, the new kernel rectangle has dimensions

    A=r−b+1, B=S−b+1,

and homogeneous degree shift b. The former first-jet rectangle has dimensions A−1,B−1 and shift b+1. Their Hilbert-series difference is

    T^b[(1−T^A)(1−T^B)−T(1−T^(A−1))(1−T^(B−1))]/(1−T)²
      =T^b(1+T+...+T^(A+B−2)).

Since r=m−b−1, its dimension is

    q_b=A+B−1=m+S−3b.

Summing b=1,...,S (with the empty boundary contributing zero when m=2S) gives exactly

    sum q_b=S(2m−S−3)/2.

The degree moment is exactly sum_b sum_(ell=0)^(q_b−1)(b+ell), which is the grading correction in CLOSED_CURVATURE_RANK.md. Hence both the scalar and challenge-graded formulas were already contained in the restored result.

## What remains a current-session calculation

The bounded finite arithmetic evaluates these established formulas at the new agreement target181275 and compares selected source shapes. It produces valid source-existence certificates within the checked gates. It does not produce a new general interpolation theorem, a new asymptotic threshold, or a better.codes improvement.

The restored primary files also contain `SecondJetRelaxedInterpolation.Interpolant`, `SecondJetTotalAvoidance.helper_or_divisibility`, and `SecondJetAsymmetric.count_of_interpolant_total`, including the retained divisibility alternative. Our earlier discussion that generic second-jet routing was mathematically missing overlooked this restored material. The actual remaining issue is mapping the chosen source to those hypotheses and making the route activate cheaply enough at the repaired target.
