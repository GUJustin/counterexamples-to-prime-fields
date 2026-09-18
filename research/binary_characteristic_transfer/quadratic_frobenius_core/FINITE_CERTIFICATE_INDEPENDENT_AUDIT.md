# Independent finite DKT certificate audit

September 18, 2026. **PASS.** Directly read the archived primary DKT text `tmp/eprint-2056/paper.txt`, equations (60)–(64), Proposition 5.10 and its proof, and Lemma 5.9's reconstruction guard. This new support repairs the failed m=4 support; it does not retroactively validate the old support.

Use `n=9p²`, code dimension `k=3`, message degree `D=2`, agreement `A=T=4p`, multiplicity `m=6`, derivative cap `Bpartial=3`, total jet cap `B=12p`, and challenge height `H=40B`. The received curve is a line, so ell=1.

The derivative-weighted support is exactly

    x+2a+b < mA=24p,  b<=3,  a+b<=B.

Thus every candidate substitution has degree STRICTLY less than mA. Vanishing with multiplicity m at A distinct agreement coordinates forces the substituted polynomial to be zero. The choice B=mA/2 is compatible with the strict inequality: the terminal degree contributes only derivative-weighted columns with b>0. It does not require replacing the strict root-count argument by a non-strict one.

The primary Eq61 sum is

    G=sum_(t=0)^B sum_(b=0)^min(t,3) max(2B-2t+b,0)
     =4B²-2B=576p²-24p.

For Eq62, all potentially nonzero blocks have t<=s+3, s<=5; the cutoff s+t<24p is therefore harmless for p>=7. Summing its exact displayed rank upper bound gives the six s-block totals

    4, 8, 12, 15, 14, 9,

hence R=62. These are support-rank UPPER bounds as required by the proposition; no assertion of characteristic-independent exact local ranks is needed.

In particular `G-nR=18p²-24p>0`. Because H>=B, Eq63's source side is at least `(H-B+1)G`, and its target side is at most `(H+1)nR`. The difference is exactly

    B(144p²-936p)+18p²-24p.

This is positive for every integer p>=7: `144p²-936p=72p(2p-13)>0`, and the remaining term is positive. Therefore the STRICT graded row test holds, uniformly for every evaluation domain and every received line over the field. Proposition 5.10 produces a sound interpolant nonzero at every challenge specialization with the printed challenge/jet bounds.

Interpolation itself has no characteristic restriction. Lemma 5.9 separately permits reconstruction/counting under `p>max(D,Bpartial)=3`; in particular the construction's p>=41 suffices. The primary text explicitly does not require `p>Bjet`. Thus there is no conflict from B=12p exceeding the characteristic.

A separate direct-sum arithmetic replay at p=7,11,41,43,101 is saved in `finite_certificate_independent_replay.json`. It rebuilds Eq61 and Eq62 before comparing to the closed formulas and the surplus expression.

## Scope of this receipt

This certifies the finite first-order EXPLAINER and the reconstruction characteristic hypothesis. It does not by itself evaluate every downstream list/MCA incidence budget or certify a newly claimed numerical upper-bound constant. Any such constant requires applying the primary counting formulas with this m=6 support. Since the challenge field in the construction has size q=p⁴=n²/81, a coarse constant-times-n² count can still be larger than the field. No generic tightness or nontrivial failure-probability upper bound is asserted here.
