# Official centibit scoring and the first coordinate improvement

The pinned official interface takes `ProtocolClaim centiBits radiusNumerator radiusDenominator` with centiBits a natural number and error claim2^(−centiBits/100). The verifier adapter requires scale100 and exports score=value/scale. The repository README specifies maximizing that integer score. A better radius certified at the same6811centibits may be a valid mathematical improvement and may pass claim verification, but it is not a strict leaderboard-score improvement. Radius metadata does not create a hidden fractional-centibit score.

Primary pinned sources:
- [TargetLower](https://github.com/proximity-prize/proximity-prize/blob/cdb451f13fdc6c84f5fe363e77ee13a89bd30974/ProximityPrize/Benchmark/TargetLower.lean)
- [Official README](https://github.com/proximity-prize/proximity-prize/blob/cdb451f13fdc6c84f5fe363e77ee13a89bd30974/README.md)
- [Verifier score adapter](https://github.com/proximity-prize/proximity-prize/blob/cdb451f13fdc6c84f5fe363e77ee13a89bd30974/scripts/write-verifier-score.py)

## Exact cell boundary

An agreement target A corresponds to error cell e=n−A, whose radius satisfies e/n<=delta<(e+1)/n. Therefore its spot-score supremum is−128log2((A−1)/n), not attained at the excluded upper endpoint. A6812 score can occur inside the cell exactly when

    (A−1)^12800 * 2^6812 < n^12800.

The code performs this exact integer comparison. Decimal logarithms below are explanatory only.

| Agreement | Score supremum | Can reach68.12? |
|---:|---:|---|
|181284|68.1108331969|No|
|181283|68.1118518555|No|
|181282|68.1128705196|No|
|181281|68.1138891894|No|
|181280|68.1149078648|No|
|181279|68.1159265458|No|
|181278|68.1169452324|No|
|181277|68.1179639247|No|
|181276|68.1189826225|No|
|181275|68.1200013260|Yes|

Thus none of181283..181276 gives the next strict score under the current protocol route. Agreement181275 is the first integer cell capable of6812centibits; this does not itself prove its extractor-error condition.

## One-coordinate source diagnostic

At A181283, the unchanged primary A shape has gap−161757088035, but its L-slope remains positive1554840. Keeping multiplicity115,slope35,quotient159, increasing L274277 to378312 restores positive nullity. This preserves the narrow quotient/slope box but enlarges A's direct-helper cost.

TCap m226,s70 cannot keep total9275 under the exact common-divisor nullity gate. Its best nearby total cap is9318 (+43); bounded m210..250,s60..80 optimization does not improve that threshold. This is much smaller expansion than the +403 needed by the practical A181275 replacement.

All27 unchanged auxiliary sources fail even at181283. Optimizing multiplicity within the existing closed-count regime lets sources1,6,11,17 retain their old geometric caps; the other23 need L increases3..11. This is materially easier than the181275 replacements, but is still not a complete certificate and cannot produce a strict centibit gain by itself.

Files `score_cell_probe.py/json/resources` give exact gates and per-source details; `score_cell_sources.json` pins the official scoring files. The bounded run took7.38seconds, below22MiB. No submission or verifier run was performed.
