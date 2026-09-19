# Quadratic-extension centers: dense conic unions do not supply rich lines

2026-09-18. One bounded candidate assessment; no scan or manuscript edit. The exact fixed-angle center reduction is in FP2_PARTITIONED_TWO_BLOCK_REDUCTION.md. This note tests a growing union of complete circles/conics, rather than another Cartesian grid or Fermat orbit. It proves a scoped obstruction; no positive short-domain family was found.

## Model and required richness

Write E=F_(p²) as the prime affine plane. For disjoint physical coordinate blocks D0,D1, each squared-coordinate set S_i={x²:x in D_i} carries actual multiplicity at most two. Their total retained coordinate count is n. In the norm-one, nontrivial-coefficient reduction, a successful canonical witness at center z matches two lines through z, with directions u and eta*u.

If its agreement exceeds the common block maximum U by at least c*sqrt(n), then EACH of the two lines has at least c*sqrt(n) physical matches. The conclusion below rules this out when a block is a union of complete nonsingular conics, or a union of uniformly dense retained pieces of such conics, and n=o(p²). No condition on the fixed angle is needed: the individual rich lines already fail to exist.

## Exact bound for growing complete-conic unions

Let S be the union of h distinct nonsingular conics' complete affine F_p-point sets, with m=|S|. Components without points may be discarded. A nonsingular projective conic with a rational point has exactly p+1 rational points: projection from that point parametrizes it by P¹(F_p), including the tangent direction. Removing the line at infinity deletes at most two points. Hence every component has between p-1 and p+1 affine points. Distinct nonsingular conics have no common component and meet in at most four geometric points. Every affine line meets each in at most two points.

For each point x, let v(x) count its incident conics. Cauchy-Schwarz and these intersection bounds give

    [h(p-1)]² <= (sum_x v(x))²
                 <= m sum_x v(x)²
                 <= m [h(p+1)+4h(h-1)].

Thus

    m >= h(p-1)²/(p-3+4h).

Whenever (p-1)²>4m this rearranges to the exact resource bound

    h <= m(p-3)/[(p-1)²-4m].

A line has at most 2h distinct points of S and hence at most 4h physical square-root coordinates. Since m<=n, for sufficiently large p with n=o(p²), its weighted richness is at most

    4n(p-3)/[(p-1)²-4n] = O(n/p) = o(sqrt(n)).

Therefore a growing number of overlapping COMPLETE conics cannot evade the short-domain requirement. Heavy overlap does not help: the second-moment bound already accounts for every pairwise intersection. This is stronger than only excluding a fixed number of bounded-degree components.

## Actual square filtering and dense partial components

The square map reaches only half of E*. One must not apply the preceding full-conic point count to a conic whose nonsquare points have been discarded without checking the remaining population.

The same argument has a precise robust version. Suppose S is the union of h retained subsets S_j, each lying on a distinct nonsingular conic and satisfying |S_j|>=delta*p for a fixed delta>0. Each still has at most p+1 points, pairs overlap at most four, and every line intersects each in at most two. Therefore

    m >= h*delta²*p²/(p-3+4h),
    h <= m(p-3)/(delta²*p²-4m)  when the denominator is positive.

The weighted line bound is again O_delta(n/p)=o(sqrt(n)). This covers arbitrary square filtering or subsequent puncturing PROVIDED every retained component still has the stated fixed positive density. That density is an explicit hypothesis, not a character-sum assertion proved here.

There is an exact square-compatible complete-circle family. For the norm circles

    C_r={y in E: Norm_(E/F_p)(y)=r},  r in F_p*,

each has p+1 points. Since chi_E(y)=chi_p(Norm(y)), if r is a nonzero square then every point of C_r has two square roots in E. If r is nonsquare it supplies no square-root coordinates. For h selected square radii these circles are disjoint, so m=h(p+1), and every line has at most 2h points and 4h physical matches. The ratio of this maximum to sqrt(2h(p+1)) tends to zero whenever h=o(p). Thus the natural complete norm-circle union fails the target with exact counts and no density assumption.

Translated norm circles of nonzero radius also intersect pairwise in at most two points, since subtracting their norm equations gives a line when their centers differ. Complete such circles satisfy the stronger bound m>=h(p+1)²/(p-1+2h). Their square-filtered versions still need a retained-density check before using it.

## Comparison and what is not closed

PUNCTURING_ASSESSMENT.md already excludes balanced Cartesian grids, bounded unions of their projective images, and the specified complete Fermat-orbit mechanism. The argument above is different: it allows an unbounded number of distinct full conics and uses their linear-in-p population against bounded pair overlap. It shows that the proposed dense conic/circle population never produces even ONE required square-root-rich line on a short domain, so it cannot produce superlinearly many fixed-angle rich centers.

The point-parabola bounds in PRIME_QUADRATIC_RICH_CORE_INCIDENCE_GATE.md concern a different graph-of-a-word model. Their nontrivial exponents are not an existence result for the present center geometry, and no real-plane incidence bound has been transferred to F_p here.

Sparse torsion-projected pieces, sparse angular pieces of circles, or other components with o(p) retained points are not excluded by this proof. If h such pieces each have v points with negligible overlaps, m is about hv, while the elementary line cap is 2h. Square-root richness can then first become possible around h>=constant*v. This is only a necessary resource ledger: it gives no compatible line directions, centers, labels, or far endpoints. In particular, replacing complete circles by sparse pieces would require an explicit modular incidence identity, not just counting many supports or components.

No positive family meeting the actual line-richness and far-endpoint requirements was established in this bounded assessment. The surviving sparse-component problem is narrower than a union of complete conics, and this note makes no universal obstruction claim for short prime-plane point sets.

### Dense bounded-degree torsion projections obey the same resource gate

The same proof also applies to a specified bounded-degree projected-torsion model. Suppose each retained piece has at least delta*p distinct points on one of h distinct absolutely irreducible plane curves of degree at most D, with D and delta fixed. Assume no component is a line. Distinct curves meet in at most D² points, a line meets each in at most D points, and each curve has at most D*p affine points by the elementary polynomial zero bound. Consequently

    m >= h*delta²*p²/[D*p+D²(h-1)].

For m=o(p²), this forces h=O_(D,delta)(m/p), and square-root-weighted line richness is at most 2D*h=o(sqrt(n)) when m<=n=o(p²). For example, torsion subsets of size comparable to p lying on distinct elliptic plane cubics satisfy these premises; bounded-degree injective projections preserve the conclusion when their image curves and retained populations satisfy the stated bounds. Repeating a curve does not help and should first be merged into one retained piece.

This does NOT apply to torsion sets of size o(p), projections collapsing a large fraction of their points, growing-degree image curves, or line components. Those are exact failures of the premises, not evidence of a positive incidence construction.
