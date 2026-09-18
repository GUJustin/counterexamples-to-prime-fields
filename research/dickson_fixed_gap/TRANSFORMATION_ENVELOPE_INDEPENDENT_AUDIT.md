# Independent audit and puncturing repair

The inequalities and first-order comparison in `TRANSFORMATION_ENVELOPE.md` are correct for its three explicitly listed operations. They do not, by direct invariant preservation, prove a statement allowing later puncturing: deleting an unmatched point lowers `(N−A)−5(N−D)/6` by 1/6. The following ancestry argument supplies that missing extension under the inherited-match hypotheses.

## Uniform error with arbitrary interleaving, including puncturing

Fix the final carried subbank, and select a single original Dickson orbit containing at least half its members. Write L for this orbit subbank size. The archived Fourier proof bounds its **average** agreement, not merely its minimum, on any retained original-coordinate domain and arbitrary word, by

    B(n,k)+epsilon_L k,
    B(n,k)=min(n/2,n/4+k/2), epsilon_L=O(L^(−1/2)).

The proof of that estimate applies also to domains of size at most k: its mask means, restricted Parseval bound, and residual-fiber bound have no lower restriction on n. This observation, or an explicit extension of the cited lemma's statement, is needed when using layers below. Empty layers may be assigned zero contribution.

Let P be the product of all pullback degrees, however many operations occur. Classify final retained coordinates by their ancestry. Let N0 count descendants of the original Dickson domain, Z count descendants of inserted common-zero coordinates, and V count the remaining inserted coordinates on which no carried matches are claimed. Then N=N0+Z+V. Each original coordinate has at most P descendants. Layer its multiplicity into P ordinary subsets of the original domain. A layer may carry a different received word; the uniform average bound allows this. Summing average bounds, and using the two linear upper bounds defining B, gives

    A <= B(N0,Pk)+Z+P epsilon_L k,    N0<=4Pk.

Here A is the minimum agreement of the carried final subbank and is at most its average. It is essential to sum the average bounds; summing unrelated per-layer minimum bounds would be invalid. The construction normally inherits the same received value on a fiber, but the average argument even allows different such values without changing the bound.

The degree bookkeeping gives

    D >= P(k−1)+Z.

Indeed each common-zero insertion contributes its degree multiplied by the product of subsequent pullback degrees, and at most that many of its coordinate descendants survive. Puncturing does not reduce polynomial degree. This concerns the stated polynomial/section pullback and common-multiplier construction; an additional unproved re-embedding or degree cancellation operation is not silently allowed.

The elementary bounds on B are

    B(N0,Pk)<=3Pk/2,
    B(N0,Pk)<=(N0+5Pk)/6.

Consequently

    A <= 3D/2 + P(epsilon_L k+3/2),
    A <= (N+5D)/6 + P(epsilon_L k+5/6).

At nontrivial code rates D<N, the inequality D>=P(k−1) implies P/N<=1/(k−1). Since a growing carried list forces L and k to infinity, both normalized errors are uniformly o(1). There is no sum of fresh errors over operations, and no restriction on their number or degree scales is needed. All match creation except inherited matches and common zeros remains outside this argument. Non-inherited additional candidates are also outside its list statement.

## Actual first-order comparison

The piecewise comparison in the source note is sound. Below r=2/9 use a1(r)>=sqrt(r/2), with strictness at the endpoint from the positive-root formula. The intervals [2/9,1/4] and [1/4,8−3sqrt6] lie in the branch where the positive root of F_r(a)=(8−r)a²−6ra+r(4r−5) is the relevant threshold. The two displayed substitutions and their negative signs are correct. Above 8−3sqrt6 the stated refined high-rate lower bound dominates (1+5r)/6 by the displayed factorization. Passing from effective degree rate D/N to dimension rate (D+1)/N cannot lower the nondecreasing target. Even if rates approach zero or one, a uniform o(1) envelope error cannot give a fixed positive margin over the dominating curve.

“Exact extremal envelope” refers to the limiting normalized resource point (4,1,3/2), and continuous padding proportions; it is not an exact finite-integer optimum.

## Block localization qualifications

The block degree inequality is valid for the actual localized Cartesian family: varying one block multiplies a nonzero degree-D_i difference by the full other-block locator, forcing degree N_total−N_i+D_i. The resulting agreement upper bound is the sum of block minima because all block choices are independent. Its error sum must be o(N_total). Uniformly growing subbank sizes in every block suffice, even with a growing number of blocks, because the supremum of their normalized errors tends to zero. Merely having a growing product list while some positive-length blocks have fixed subbanks is not the stated hypothesis and is not certified by this proof. The more general sufficient condition is the weighted error sum o(N_total).

Subsequent pullback/common-zero insertion preserve the A−D bound; puncturing cannot increase A−D either. Uniform normalization after arbitrarily severe final puncturing follows from the initial localization cost D>=N_total/2 for at least two nonempty blocks, together with D_final<N_final. This prevents an initially negligible error from becoming macroscopic after deleting coordinates.

No main manuscript changes were made. The ancestry repair makes a genuine later-puncturing extension precise while keeping new-coincidence padding and new polynomial families outside the theorem.
