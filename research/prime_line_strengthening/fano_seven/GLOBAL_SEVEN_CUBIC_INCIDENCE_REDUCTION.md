# Exact incidence reduction for any seven cubics on fourteen points

**Proved necessary condition.** Let seven DISTINCT polynomials of degree at most
three each agree with a received word on at least seven of fourteen distinct
coordinates. Then every word has exactly seven agreements; exactly seven
coordinates have three agreeing words and seven have four; and every pair of
words shares exactly three agreement coordinates.

Indeed, let s_x be the number of agreeing words at a node and M=sum s_x.
We have M>=49. Pairwise root counting gives

    sum_x binom(s_x,2)<=binom(7,2)*3=63.

Among fourteen nonnegative integer column sizes with sum49, convexity gives
minimum63, attained only by seven3's and seven4's. At sum50 the minimum is
66. Thus M=49, every column has one of the indicated two sizes, each row has
exactly seven incidences, and every pair saturates its three-root budget.
In particular every pair difference has degree EXACTLY three and three simple
domain roots; all leading cubic coefficients of the seven words are distinct.

Let T be the multiset of seven triple supports. Let C be the multiset of
complements of the seven quadruple supports, so C also has seven triples.
Write r_T(i),r_C(i) for point degrees and lambda_T(i,j),lambda_C(i,j) for
pair degrees. Row degree seven gives r_T(i)=r_C(i)=r_i. Pair degree three gives

    lambda_T(i,j)+lambda_C(i,j)=r_i+r_j-4.

Summing over j!=i gives

    4r_i=5r_i-3,

because sum_i r_i=21. Therefore r_i=3 for every point and

    lambda_T(i,j)+lambda_C(i,j)=2.

Thus T union C is a twofold triple system, a2-(7,3,2) MULTIDESIGN, partitioned
into two3-regular multisets of seven triples. This is not automatically two
Fano planes. Repeated incidence blocks are allowed: distinct coordinate values
do not prevent identical subsets of candidates from agreeing there. Every
triple has multiplicity at most two in the combined multiset, because any
pair within it has total multiplicity exactly two. Repetitions within T or
within C must therefore be retained in any exhaustive classification.

The separate Fano difference-factor obstruction handles the special case in
which T and C are the same Fano plane. Excluding or constructing all remaining
multidesigns requires additional algebraic work; the incidence count alone
proves neither a global odd-characteristic upper bound of six nor a seventh
word construction.
