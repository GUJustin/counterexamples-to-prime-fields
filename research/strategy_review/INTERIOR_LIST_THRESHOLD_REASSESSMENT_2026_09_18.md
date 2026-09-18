# A matched list bound in the interior of the low-rate first-order band

September 18, 2026. Bounded positive-route reassessment. The consequence below strengthens the threshold and onset of the existing extension-field list comparison; it is not a new prime-field construction. Independently checked in `../binary_characteristic_transfer/quadratic_frobenius_core/NORM_ONE_INTERIOR_THRESHOLD_INDEPENDENT_AUDIT.md`. No scan or rental was run.

## Concrete consequence

For every prime p>=53, retain the norm-one construction over E=F_(p^3):

    N=2(p^2+p+1), K=3, D={x in E*: Norm(x^2)=1},
    f(x)=x^(2p+2), T=ceil(19p/10).

Its complete threshold-T list consists of the N/2 quadratics

    Q_a(X)=aX^2-a^(p^2+1),  Norm(a)=-1.

Each bank member has exactly 2p+2 matches. Every outsider has at most p+1 matches, and p+1<T<=2p. Thus lowering the threshold preserves the exact list. At these SAME parameters, the archived finite DKT certificate bounds every received word's list, on every domain of length N, by 22N.

The fixed certificate has m=6, derivative cap 3, B=3T, coefficient count G=4B^2-2B, and local rank R=62. Even the stronger challenge certificate with H=40B remains valid:

    39G-40NR >= (2711/25)p^2-5428p-4960 >0  (p>=53).

For the fixed-word count put lambda=(N-2)/(T-2). The primary formulas (54),(56) and Lemma 5.11 in `../../tmp/eprint-2056/paper.txt` give

    list size <= floor[lambda(21T-12)+15T-9]
              = floor[21N+30lambda+15T-51] <=22N.

Here lambda<=2p, T<=2p, and N-90p+51>0 for p>=53. Reconstruction requires only p>3, not p>B. At p=53 the exact ledger is N=5726, T=101, exhibited list 2863, finite upper bound 123444<=125972=22N, and conservative graded surplus 29732888.

## Why the threshold change matters

The old threshold 2p-ceil(4sqrt(p))-4 approaches Johnson with absolute separation only Theta(N^(1/4)). The new threshold has

    T/sqrt(N) -> 19/(10sqrt(2)),
    [sqrt(2N)-T]/sqrt(N) -> 1/(10sqrt(2)).

The archived first-order estimate gives

    N a_1(3/N) <= sqrt(3N/2)+(3N/8)^(1/4)
                < 7p/4+sqrt(p) < T  (p>=53).

In particular the first-order separation is also Theta(sqrt(N)): its liminf after division by sqrt(N) is at least (19/10-sqrt(3))/sqrt(2)>0. The matched linear list comparison therefore holds at an interior point of the scaled low-rate band, with a fixed proportional separation from Johnson, rather than only approaching its boundary. Rate 3/N and normalized agreement/margins still vanish. The alphabet remains an extension field. This changes neither the far-input line theorem nor any prime-field claim.

## The same support gives an interval, without a challenge variable

For every fixed c with sqrt(31)/3<c<2, choose T_c=ceil(cp). For all sufficiently large p (depending on c), the same bank is exactly N/2 and the same codewide 22N upper bound holds. For a fixed received word the sufficient interpolation condition is simply

    G-NR = 36T_c^2-6T_c-124(p^2+p+1)>0,

whose leading coefficient is 36c^2-124>0. No H or challenge surplus is needed: apply the fixed-word interpolation kernel and the fixed-word part of Lemma 5.6. Since sqrt(31)/3>sqrt(3), this entire interval is eventually above the first-order curve and below Johnson. This statement is an implication of the existing support, not an optimization over all supports.

## Prime-field research decision

The requested fixed-positive-rate prime-field growing list, or superlinear far-source line above first order, remains unconstructed. This review found no additional splitting identity, modular incidence realization, or balanced common-remainder formula that would justify a bounded constructive computation. Low-monodromy/split-fiber language by itself supplies none of those objects. The archived rational-envelope and power-family analyses also prevent treating the familiar bounded families as a new route without checking their precise hypotheses; an unspecified growing-degree pencil supplies no positive mechanism. No new exclusion theorem is asserted.

Accordingly the useful action from this pass is the interior-threshold corollary above. Do not allocate another scan to the pencil suggestion or present the existing discriminant, moment, or higher-character necessary conditions as new construction progress.
