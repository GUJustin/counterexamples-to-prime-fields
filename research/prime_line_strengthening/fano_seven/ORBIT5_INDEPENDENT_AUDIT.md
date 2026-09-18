# Independent audit of the global orbit5 obstruction

Verdict: PASS in characteristic different from two, including characteristic zero. The proof in `ORBIT5_OBSTRUCTION.md` excludes the whole ordered incidence design, not merely the sampled rational-node specialization.

## Normalization and necessary node equations

The seven b-nodes are distinct, so a projective coordinate change can put their first three at infinity,0,1. Candidates must be transformed as degree-three binary forms, with the corresponding common value multiplier. This preserves incidence; evaluation at infinity means the leading affine cubic coefficient. Subtracting the transformed P1 is legitimate.

Every pair has exactly three prescribed common nodes. A nonzero binary cubic cannot have an additional root or extra multiplicity at one of these nodes. Therefore each difference is a nonzero scalar times its prescribed binary cubic locator. Dividing the three differences on a T-line by their shared triple-node linear form gives a linear dependence of their quadratic b-locators. The determinant computation in `relative_fano.py` uses coefficient vectors (1,-a-b,ab) for two finite roots and (0,1,-a) for infinity and a finite root. These conventions are correct.

The three displayed equations imply u=w/s,v=z/s,s=w+z-1. The eliminated factors w,z,z-v,z-w are nonzero by the node-distinctness guards. The equation v*s=z also proves s nonzero. No potentially admissible locus is discarded.

## Completeness of the candidate family

Each Pi with i>1 vanishes at its two prescribed b-nodes shared with P1. It is therefore its displayed quadratic times a linear polynomial, allowing degree drop at this stage.

At infinity, P4,P5,P6,P7 have equal leading coefficient l. At0 the products zu and wv agree, so equality of P6,P7 there identifies their quotient-linears' constant coefficients. Thus their quotient linears are identical. At1, (1-z)(1-v)=(1-w)(1-u), so the same reasoning identifies those of P4,P5. For P2,P3 the ratios of the two quadratic prefactors are s^2 at BOTH0 and1; equality of their values at these two distinct points therefore makes their quotient linears differ by precisely s^2. The remaining equalities give the claimed L1,L2 constants. This proves the three-parameter family is exhaustive; it is not a generic-nullspace assertion requiring an unproved rank condition.

Because P1(infinity)=0 and P2(infinity)=p lie outside the selected quadruple, no-extra-agreement forces l!=0 and p-l!=0. The latter also ensures the two residual quadratics used in the resultants have genuine degree two. No division by l or p is needed in constructing the family.

## Excluded factors and the contradiction

Expanding the four recorded evaluations verifies the factors A,B,C_z,C_w exactly. At0 the selected group is2367, while4,5 are outside it. At1 the selected group is2345, while6,7 are outside it. An outsider agreeing there creates a fourth root for a nonzero pair difference. Hence all four factors are nonzero, as are their scalar multipliers z/s,w/s,(z-1)/s,(w-1)/s.

The first two factors in `orbit5_explicit.json` match the note after replacing w+z-1 by s. In particular their unexcluded factors are precisely

    F_+=(z-w)l+s(s+1)p+2s^2q,
    F_-=(w-z)l+s(s+1)p+2s^2q.

Each prescribed triple has a distinct finite node beyond its known b-node, so its divided pair of differences has a common root. The appropriate resultant must vanish. Its other factors have all been proved nonzero, forcing F_+=F_-=0. Subtracting gives2(z-w)l=0, impossible in odd characteristic under z!=w and l!=0.

The second two resultants, any projective-solution enumeration at fixed w,z, and the timed-out generic-nullspace computation are unnecessary. The argument does not claim an obstruction in characteristic two or for any of the other six unclosed ordered designs. No additional numerical job was run for this audit.
