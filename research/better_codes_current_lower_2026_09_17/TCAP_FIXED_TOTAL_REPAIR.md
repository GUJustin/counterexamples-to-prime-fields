# TCap: exact common-divisor total-cap repair audit

At target A=181275, the fixed total cap9275 is not recovered by any shape in the bounded grids below. A valid nearby replacement preserves m226,s70 and quotient312 but needs L9682 and total cap9678. This is an arithmetic source gate, not a completed benchmark certificate.

## Actual proof obligation

The pinned `MovingFiberSelection6811.lean`, `common_TCap_total_le`, argues by contradiction: a common divisor of total degree at least T+1 leaves every kernel quotient in the coefficient box of total degree L−T−1. Injectivity of division would imply

    kernel nullity <= C(D,L−T−1,s).

Consequently the sufficient numerical gate is

    C(D,L,s) − n R(m,L,s) > C(D,L−T−1,s),

with D=mA, n262144, w131071. Strict inequality matters. This is stronger than positive nullity. If L<=T, positive nullity already bounds the divisor by T directly; the code handles that case separately.

## Exact optimization in L

For L>=max(m+s−1,q), q=floor(D/w), and one-residue condition (D mod w)+s<=w, the source surplus G(L)=C(D,L,s)−nR(m,L,s) is affine. The rank uses the general rectangular sum; no assumption 2s<=m is imposed.

For a small quotient degree u, the coefficient count is evaluated exactly, without applying a large-L formula outside its hypotheses. For each j<=min(s,u), put v=D−(w−1)j and k=min(u−j,floor((v−1)/w)); discard k<0. Its contribution is

    (k+1)(u+1−j)v − ((u+1−j)w+v)k(k+1)/2
      + w k(k+1)(2k+1)/6.

The increment C(u+1)−C(u) is nondecreasing, since it sums nonnegative weighted coefficients over increasing diagonals. Thus G(T+1+u)−C(u) is concave. Binary search finds the exact maximum: its forward difference is slope(G)−[C(u+1)−C(u)]. For u>=q+2 all relevant diagonals are included; thereafter the difference is negative. No large L can escape this finite maximum. Direct nested sums and independent first differences check the small-box formula.

For these tested shapes T9275 exceeds the affine-regime lower endpoint. The optimizer u does not depend on T, and the optimum increases by slope(G) for each extra unit of T. This gives the nearby total-cap thresholds analytically. The two reported replacement witnesses were checked directly at their claimed total cap and at the preceding cap.

## Results

The first grid covers 19044 legitimate one-residue shapes: m1..226,s0..90 and m227..260,s50..90, subject to s<=q. None satisfies the total9275 gate for any L in the stated affine regime.

Original m226,s70 has slope909424303 and optimum L9281 at T9275, but its strong surplus is −365685676234.

| m | s | quotient | proved total cap | least L at that cap | nullity | quotient count |
|---:|---:|---:|---:|---:|---:|---:|
|226|70|312|9678|9682|1269335799|815430885|
|229|71|316|9673|9678|1525346346|1443744190|

For the first row, optimized L cannot prove total9677; for the second, it cannot prove9672. Within the first grid, the first row gives the smallest threshold retaining quotient<=312 and s<=70; the second gives the smallest strong-gate threshold overall. These statements concern the listed coefficient supports and numeric sufficient condition, not the true common-divisor degree.

A separate coarse wider grid checks2592 shapes: m270..2000 in steps of10 and s=floor(pm/100)+d, p29..33,d in{-1,0,1}, with the same legitimacy conditions. All fail total9275. The best nearby threshold in that grid is9859 at m270,s84,quotient373. This is a bounded search, not a global exclusion of larger multiplicity or other supports.

## Consequence for certificate rebuilding

The q312,s70 replacement increases TCap.L by401 and the aggregate total cap by403. These affect the residual pair bound, the wide and narrow aggregate boxes, helper majorants, phase thresholds, and base receipts. A phase ledger verified only through total9275 does not complete this repair. Using m229 instead reduces the total cap by five but increases the TCap quotient and slope caps, so it is not coordinatewise better.

Files: `tcap_fixed_total_repair.py/json`, `tcap_minimum_total_witnesses.json`, `tcap_wider_probe.py/json`, and corresponding watchdog records. Both searches completed in about five seconds, below31 MiB, within the384 MiB/60 second guard. No Lean port/build or improved score is asserted.
