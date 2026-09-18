# Finite Eq63 transfer for graded translation-stable jet spaces

This is an Eq63-only finite coefficient-prefix theorem for a restricted nonmonomial class. No nonmonomial Eq64 extension is asserted. It does not follow for arbitrary filtered jet spaces merely from the existing saturated monomial-domination theorem.

## Source class

Let W=direct_sum W_q be a finite-dimensional TOTAL-JET-DEGREE-GRADED subspace of k[Y0,Y1], stable under Y0 translation. Let its maximum degree be d, with characteristic zero or greater than d. Use the global source

    U(W)=k[X]W intersect {derivative weight <mA},

where wt(X,Y0,Y1)=(1,D,D-1). Thus the coefficient cutoff is imposed on the actual polynomials, not on an arbitrary chosen basis. Let G_q be its dimension in total jet degree q and R_q the rank of its finite local image at that degree. Suppose its affine-line row test sum_q(H-q+1)_+(G_q-nR_q)>0.

Then there is a Y0-downward monomial full-prefix source with exactly the same G_q, no larger R_q in every degree, and no larger total-jet or derivative cap. Therefore the Eq63 fourth-power declared-ledger necessity transfers to this graded nonmonomial class.

## Exact finite degeneration

Within W_q, perform echelon reduction in increasing Y1 exponent v. The pivot exponents are distinct; a pivot vector has form

    f_v=Y0^(q-v)Y1^v + sum_{j>v} c_j Y0^(q-j)Y1^j.

Its derivative weight is Dq-v. These pivot weights are distinct, and any nonzero linear combination has the weight of its smallest surviving pivot. Hence the vectors X^x f_v with

    0<=x<mA-Dq+v

are a basis for the degree-q portion of U(W). In particular its full coefficient-prefix lengths are determined by the pivots.

Apply Y1->tY1 and rescale each vector by t^(-v), giving the polynomial family

    f_v(t)=Y0^(q-v)Y1^v+sum_{j>v}c_j t^(j-v)Y0^(q-j)Y1^j.

Every basis vector retains the same highest-weight pivot and the same X-prefix length for all t, including t=0. The limiting global space is EXACTLY U(S), the full-prefix source of the pivot monomials. This equality, not merely containment in U(S), is the necessary finite-cutoff point.

On the local target extend the action by X->t^(-1)X. Then E=Y0-XY1 is fixed and the contact ideal (monomials X^i E^j with i+2j>=m) is preserved. For t nonzero the actual finite local matrix has the same rank: source and target actions are invertible diagonal changes. At t=0 its rank cannot increase. Total jet degree is preserved by the action, so this holds separately for every q and gives R_q(S)<=R_q(W). No saturated-coefficient assumption is required for this step.

Y0-derivative stability persists in the flat limit. Since every exponent is below the characteristic, the monomial limit is Y0-downward. All pivots were already monomials present in the source, so total-degree, Y0-degree and derivative-degree caps cannot increase. The source G_q are unchanged, completing the row-test transfer and the application of the full downward-support theorem.

## Why arbitrary filtered spaces are not yet included

The existing monomial-domination proof first replaces a nonhomogeneous W by its highest total-degree parts. This preserves filtered total-degree multiplicities and saturated rank inequalities, but need not preserve the derivative-weight filtration or finite X-prefix dimensions.

For example, with D=2 the translation-stable space

    W=span{1,Y0,Y0^2+Y1^3}

has total-degree multiplicities at 0,1,3. The last generator has derivative weight4; its highest total-degree part Y1^3 has weight3. For a sufficiently large cutoff, taking highest parts therefore creates an EXTRA permitted X coefficient in the full-prefix source. Semicontinuity bounds the rank of the actual flat limit of the original finite source, not the rank of that larger full-prefix source. Adding the extra coefficient can also add local constraints, so positivity does not follow simply by inclusion.

In addition, for a nonhomogeneous source the degree-by-degree local rank bookkeeping behind Eq63 requires an explicitly compatible filtration/row selection; a saturated total-rank inequality is not by itself that statement. A broader extension needs a degeneration preserving the relevant finite coefficient and challenge filtrations together, or a separate direct filtered kernel theorem. Neither is assumed here.
