# Primary B and derivative-chain target repair

Two explicit B replacements pass the current interpolation gate and all checked characteristic conditions at A181275. The existing nine-trillion tail/free allowance remains sufficient for both. These facts supply arithmetic inputs for a target proof port; they do not establish a final receipt.

| B choice | m | slope | Y cap | L | weighted D | kernel nullity |
|---|---:|---:|---:|---:|---:|---:|
|Preserve Y/slope|134|40|185|22192|24290850|28698360|
|Reduce L|137|42|189|18812|24834675|40328453|

The first follows the least-L repair in the earlier fixed-cap search. The second is an already identified nearby tradeoff, not a new broad search. Both obey D=mA and D+s<=w(Y+1). A's universal-factor caps163/36 remain tighter than either B cap, so changing between these two B choices does not enlarge the narrow phase box. It does change the wide complement box and derivative-chain budget.

## Residual pair

For left caps B=(Y,R,L) and right TCap=(312,70,9682), the mixed vector is

    (R*9682+L*70, Y*9682+L*312, Y*70+R*312).

The agreement vector is the coordinatewise maximum of the left and right vectors (1+2wy,w(2r−1),1+2wt). This maximum is essential: the residual pair is not a left-only helper.

Its regular bound is floor(((n−w)*dot(agreement,mixed)+(errors+1)*gap*mixed.z)/gap). The two candidates give respectively1215189223289491 and1073295356313793. The exact baseline formula reproduces1057030663884726. All mixed coordinates are below characteristic2130706433; the maximum across the two candidates is8715074.

## Tail and free factors

`TightParameters` uses (n,w,A,D_B,L_B,1), so implicitY=floor((D_B−1)/w), algebraicCap=L_B. Its exact count cap is

    floor(((n−w)*[(1+2wY)L+w(2YL)+(1+2wL)Y]
           +(errors+1)*gap*Y+2L²*gap)/gap).

This is8430483280653 for the first candidate and7300835672419 for the second, both below9000000000000. Therefore the tail floor in every derivative chain and the two final free-part allowances can retain nine trillion. The characteristic gate2YL<p also passes, as do positive D,w,L and the field-size degree gates.

## Derivative chain

For chain degree d, retain the generic stage caps(leftY,leftR,leftZ)=(y,d−j,z) and right caps(y,d,z). With target gap50204 and errors+1=80870, define

    K=131073*(z+y+524284*y*z)+50204*80870*y,
    M=131073*131071*y*z.

The exact sum identity is

    2*sum_{j=1}^{d−1} stageNumerator(j)
       =(d−1)*(3d*K+4M*(d−1)).

The existing endpoint-convexity proof then applies with the same positive quadratic coefficients. `repaired_primary_chain.py` implements the target unitSlope/unitConstant and max-with-nine-trillion exactly, including natural-number behavior at d=0. The summed identity was independently checked against explicit stage numerators through d42, which covers both B candidates. The existing Lean lemma artificially enumerates d<=40; choosing slope42 requires extending that finite arithmetic wrapper to42 or proving the elementary sum formula generically. This is an explicit port obligation, not an unverified new mathematical assumption.

Uniform chain characteristic checks use mixed-coordinate bounds2RL,2YL,2YR, all belowp for both candidates. Actual derivative degrees are at mostR, also belowp. Other hypotheses retain1<=w<A<=n and nonzero multiplicity/weighted bounds.

## Coupling into the final ledger

For aggregate(r,y,t), use the repaired A helper potential computed on the wide B caps(Y,R,total9678). Add its greedy complement to

    r*unit(y,t,r)+(R−r)*unit(Y−y,L−t,R−r)
      +2*9000000000000+residualPairCap.

`ledger_overhead` implements this entire non-phase part. At aggregate(35,159,9249), it is6294952113262627 for the first B choice and6248687056498801 for the second. At(36,163,9678), it is6681884339081191 versus6557990472105493. This favors the second choice at these locations, but full ledger propagation determines the actual winner.

Files `primary_B_chain_repair.json` and `repaired_primary_chain.py` supply all exact inputs and callable formulas. No shared primary Lean file was changed or rebuilt.
