# Contact resource at the actual binding cell

Status: exact necessary inequality and an irreducible, source-compatible countermodel to excluding the cell by scalar contact resource alone. This is not a bad-line construction or a counterexample to a potential geometry theorem with additional hypotheses.

## Framework boundary

At the pinned primary repository cdb451f13fdc6c84f5fe363e77ee13a89bd30974, `MovingFiberInitialBound6811.lean:initialA_universal_singleBound` passes factor divisibility, weighted/support caps, candidate agreement and no-large-pencil hypotheses to `MovingFiberSingletonGeometry6811.factor_count_of_cover`. The resulting sheet bound depends on the cumulative flag (r,v,z). `MovingFiberSingleCore6811.lean` defines `cap`, `choice`, and `Active` solely using these flags and stored phase/source data. There is no contact-profile or contact-excess coordinate in these receipt interfaces.

Adding the resource is therefore a new theorem/interface step, not a different numeric reading of an existing Own column. Moreover, a factor of ONE source is not automatically an `initialAUniversalFactor`, which divides EVERY source in the primary kernel. Any countermodel must preserve that distinction.

## A necessary inequality at the binding cell

Write n=262144, w=131071, A=181275, m=118. The total primary contact-excess resource is strictly below

    B=m(A-w)=5924072.

For a factor with exact jet degree y and R-degree r, some monomial of jet degree y has weight at least wy-r. Thus

    e(F)=wt(F)-(w/n)sum_x a_x >= wy-r-(w/n)sum_x a_x.

At (r,y,t)=(12,55,3261), wt(F)>=7208893. Any such primary factor must consequently satisfy

    average_x a_x > 1284821/131071.

In particular UNIFORM integer contact must be at least ten. This is a real restriction, but does not exclude the binding cell.

## Exact irreducible model satisfying the source and scalar-resource gates

Let Lambda be the squarefree locator of the n nodes, let the received affine word be w_x(Z)=Z, and put T=Y-Z. Define

    F=T^55 + R^12*T^10 + Lambda(X)^10*R*Z^3260.

Over k[X,Z,R], this monic polynomial in T is Eisenstein at the prime R: every nonleading coefficient is divisible by R, and the constant coefficient is divisible by R but not R^2. Hence F is irreducible. Changing T back to Y-Z preserves irreducibility. Also F_R is nonzero.

Its exact flags and weight are

    deg_R F=12, deg_(Y,R) F=55, deg_(Y,R,Z) F=3261,
    wt(F)=55w=7208905.

At each domain node, substituting X=x+t and Y=Z+tR+t^2 E gives exact contact ten: the order-ten coefficient is

    R^22 + Lambda'(x)^10*R*Z^3260,

a nonzero polynomial. Thus

    e(F)=45w=5898195 <5924072,

leaving 25877 of the strict primary resource. Define Q0=F*T^108. Its contact is exactly118 at every node, and

    wt(Q0)=163w=21364573 <118A=21390450.

Its R-degree is12, jet degree163, and total jet/challenge degree3369. Thus it satisfies the repaired primary-A support caps (s=36,Y=163,L=176421), as well as the actual weighted source cutoff. The contact-preserving graph factors consume zero charge. All these checks are symbolic; no numerical search is required.

This model establishes that one cannot delete the binding flag merely from primary-source membership, irreducibility, regular-carrier condition F_R!=0, and the nonnegative additive contact budget, even when all contacts are uniform. The regular-uniform gap is satisfied by a large margin.

## Limits and the actual missing global inequality

The model does not assert that F divides every member of the source kernel. Its received line is itself a codeword line, so it also does not satisfy the receipt's no-large-selected-pencil setup for that obvious solution family. It establishes scalar-resource compatibility, not realizability of the full worst-case regular-seed ledger.

The normal routing cost is an aggregate over first-tail components inside a carrier surface. The one charge e(F) belongs to the carrier factor, not separately to each such component. No repeated allocation of e(F) to these components follows from additivity under polynomial factorization.

A useful strengthening must prove a bound of the form

    aggregate active normal cost of F <= Phi(flags(F), e(F), source data),

using universal-kernel divisibility and/or actual selected-seed/no-pencil conditions, and prove the corresponding packing inequality over factors. The current resource supplies no such Phi. In particular, substituting e(F) for any one of r,y,t in `flagMixed` is not justified: the model above retains the exact binding flags while fitting the complete scalar resource.

No reduction of the 7.65% full-ledger deficit is claimed.
