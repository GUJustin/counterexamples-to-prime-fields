# Finite gap-three audit and transfer scope

The independent arithmetic replay `finite_random_gap_small_replay.py` verifies the stronger small certificate from `finite_gap3/certificate.py/json`. All exact rational moment values agree. The finite parameters are

    p=18,120,497, L=1500, d=3, n=4,503,001,
    A=2998, T=3001,
    at least 4,680,342 singleton bad challenges including infinity.

The excess over n is 177,341. No received word is enumerated; this is finite probabilistic existence.

The strengthened upper moment is valid. At each coordinate, the actual probabilities for k specified incumbent categories are at most Q=1/(p−2L). Their categorical outcome can be coupled to one having probability exactly Q in each category by assigning some residual outcomes to the deficits. The total deficit fits because kQ≤1. This simultaneously increases all k category counts.

For the resulting multinomial law, compare counts d+s_i to the all-d term. The additional falling factorial is at most t^(Σs_i), and each factorial ratio d!/(d+s_i)! is at most (d+1)^(−s_i). Extending the sum to all nonnegative s_i gives the claimed geometric factor [1−tQ/((1−kQ)(d+1))]^(−k). The odd/even binomial truncations used for the no-hit factor are exact Bonferroni bounds. The independent replay evaluates them by a recurrence instead of binomial coefficients. The Sidon guard p−1>4max b_i is sufficient; its margin of eight is small but strictly positive. Both first-order and Johnson comparisons are checked with rational inequalities.

## Relation to existing list-to-line conversions

The current manuscript already contains an anchored list-to-line padding lemma and a list-to-quotient transfer. The conversion mechanism should not be described as new in isolation.

For a classical Reed–Solomon quotient, take b outside a domain and define f=w/(X−b), g=−1/(X−b). A quadratic witness h on f+zg corresponds exactly to the cubic Q=z+(X−b)h on w, with Q(b)=z. Thus the threshold ordinary cubic list is partitioned into line lists by its evaluations at b. Singleton lists require evaluation separation; a pair of source words with agreement at most A additionally requires labels avoiding the entire ordinary list at threshold A+1, rather than just the smaller list at T=A+d.

The archived near-capacity moment constructions use growing polynomial degree. This quotient decreases degree by one, so those constructions do not directly give the present fixed-dimension-three theorem. Reproducing its parameters by this route would require a suitable large ordinary cubic list, controlled evaluations over the same small prime field, and the lower-threshold endpoint avoidance. This audit supplies no impossibility theorem for such a route and makes no exhaustive literature novelty claim. The established distinction is the explicit fixed-quadratic parameter regime, growing absolute source gap, and positive density of singleton bad challenges.
