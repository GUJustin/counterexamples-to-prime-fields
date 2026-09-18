**Subsequent result:** `EQ63_GROUPED_POSITIVE_SORTING.md` resolves positive feasibility by allowing excess deletion and prefix trimming before grouped shifts. The counterexamples and elementary normalizations below remain valid; their formerly open question is answered by that broader operation.

# Two valid normalizations of a positive Eq63 certificate

These operations preserve positive feasibility, unlike arbitrary adjacent height sorting. They do not yet extend the fourth-power theorem to all Y0-downward supports.

Use saturated full derivative-weighted coefficient prefixes on a finite Y0-downward support S. Write

    d_q=G_q/n-R_q, P_j=sum_{q<=j}d_q,
    M_H=sum_q(H-q+1)_+ d_q=sum_{j=0}^H P_j.

Suppose M_H>0. Unsaturated final diagonals may first be deleted by the existing half-rank lemma, since their Eq63 contributions are nonpositive.

## Maximal-prefix truncation

Choose j in {0,...,H} maximizing P_j, and discard all jet monomials above total degree j. The resulting support is still Y0-downward, saturated, and has no larger declared caps. Its prefix surplus is unchanged up to j and equals P_j thereafter. Therefore its Eq63 margin is at least M_H, and its total unweighted surplus equals P_j>0.

The last strict inequality follows because the sum of the original prefixes is positive. This step is important: a positive weighted test alone does not require the untruncated total surplus to be positive.

## Translation of the derivative exponent

Apply the preceding truncation. Let d be the minimum occupied derivative exponent, and translate every jet monomial (u,v) to (u,v-d). All original degrees q satisfy q<=j<=H, so both original and translated challenge weights are active. Saturated local ranks depend only on the active u exponents within a diagonal; they shift from q to q-d without changing magnitude. The coefficient prefix of every jet monomial grows by (D-1)d.

Consequently the exact NORMALIZED margin change is

    M_H(translated S)-M_H(S)
      =d*(G/n-R)
       +(D-1)d/n * sum_{(u,v) in S}(H-u-v+1+d).

It is strictly positive when d>0. The translation preserves Y0-downward closure, saturation and positive coefficient lengths, and decreases both the total-degree and derivative caps. Thus every positive certificate in this class can be replaced at the same H by one with positive total surplus and minimum derivative exponent zero.

## Remaining obstruction

This removes a common derivative monomial factor but does not sort unequal heights. A grouped rearrangement can move some monomials right while moving others left, and positivity of the whole support does not give positivity of each moved block. The exact adjacent formula in EQ63_ADJACENT_SWAP_OBSTRUCTION.md identifies the remaining rank-marginal terms. Neither this lemma nor the negative-margin counterexamples settle whether complete decreasing height sorting preserves positive feasibility.
