# Independent audit: shared-pole subbank budget

Verdict: PASS. Reviewed `SHARED_POLE_SUBBANK_BUDGET_2026_09_18.md`, the bank definition, and the previously audited full-bank double-zero proof. No manuscript edits or finite-field scans. The small sign checks below are exhaustive algebraic truth-table checks, not domain searches.

## Uniform pair estimate

For four signs a,b,c,d in {−1,1}, the displayed indicator

 I=3/8+(ac+ad+bc+bd−ab−cd)/8+3abcd/8

is exactly 1_{a+b=c+d}. Independently checked all sixteen tuples. With precisely one zero and the other entries signs, its value lies between 0 and 1/2 (so the note's weaker bound [0,1] is safe).

Distinct nonzero labels modulo sign make all four shifts distinct. Each quadratic character sum for a pair of shifts is −1. Their signed aggregate contribution is −1/4. The quartic is squarefree and monic, giving two rational points at infinity on its smooth genus-one model. Thus its character sum C4 satisfies |C4+1|<=2sqrt(M); the shift by one is correct. The total lower bound is 3M/8−5/8−3sqrt(M)/4. Removing four exceptional shifts and zero loses at most five; replacing the resulting constant 45/8 by six is conservative.

The remaining equalities occur in ±pairs. Twice the number of equal poles is therefore at least 3M/8−3sqrt(M)/4−6. Every such pole supplies a double zero, so this is precisely the degree amount subtracted from M, with no extra or missing factor two. The stated Delta=5M/8+3sqrt(M)/4+6 is a valid pairwise offpole root bound.

Here the Hasse estimate is over the auxiliary label field F_{ell²}, not over the ambient coefficient field. The character values are integer signs. Ambient characteristic zero or p>5 preserves the distinct possible pole coefficients −2,−1,0,1,2; p!=ell preserves the bank's distinctness. These two uses of characteristic must remain separate.

## Pole buckets and spectral normalization

At the diagonal label S=±T, the formal zero-bucket indicator contributes 1/2 although the true value is ±1; the formal ±2 indicators contribute either 0 or 1/2. Thus subtracting the diagonal contributions can only lower those three ordinary buckets. The exceptional ±1 bucket has size at most one. For L>=2, one is at most L/2, so the stated bound

 r_T<=L/2+|B_T|/2+|A_T|/4

also covers the exceptional bucket, including the smallest allowed L=2. Independently checked the inequality on all abstract sign patterns, with zero or one diagonal, for L=2 through 7; its algebraic proof does not depend on that finite check.

Convolution by chi on the real vector space of functions on F_M satisfies C²=MI−J, since chi(−1)=1. Thus its real operator norm is sqrt(M). For the indicator of the L distinct squares S², full-field squared output norm is actually ML−L²; restricting to squared pole arguments gives <=ML. For the indicator of the 2L signed labels, full-field squared output norm is 2ML−4L². The output is even, so halving after removing zero gives <=ML on nonzero sign representatives. Both claimed spectral constants are valid (slightly conservative). This is a real spectral calculation, not a finite-characteristic positive-semidefinite assertion.

Applying Cauchy separately to A_T and B_T on any selected q poles yields exactly qL/2+(3/4)sqrt(qML), uniformly over both the subbank and the selected poles.

## Incidence inequality and arbitrarily slow growth

The offpole pair sum is at most binom(L,2)Delta. Cauchy gives S_off²<=m[S_off+L(L−1)Delta]. Solving for its positive root and adding the pole contribution gives the displayed finite inequality without a missing L factor.

Uniformity for slowly growing L can be made explicit. Put z=q/M in [0,1/2]. After division by M, the right side is at most

 z/2+sqrt((4−z)*5/8)
 +3/(4sqrt(2L))+2/L
 +(2/sqrt(35))*(4/L²+3/sqrt(M)+24/M).

Indeed one may drop the negative factor −1/L in the square-root term; its remaining radicand error is at most 4/L²+3/sqrt(M)+24/M. The base radicand is at least 35/16, and sqrt(a+e)<=sqrt(a)+e/(2sqrt(a)). This proves an absolute uniform error O(L^(−1/2)+M^(−1/2)) and requires no lower bound on the rate at which L tends to infinity.

The limiting function has derivative 1/2−(5/16)/sqrt((4−z)*5/8)>0 throughout [0,1/2]. Its maximum is (1+sqrt(35))/4. The normalized agreement fraction is consequently at most (1+sqrt(35))/16+o(1), strictly below (3+sqrt(133))/31. Discarding a possible zero-label member preserves the hypothesis L→infinity.

## Scope

This excludes every growing subbank of the fixed, unrenormalized Paley shared-pole bank at N=4M and code dimension M+1 (also the same limiting dimension ratio). It does not infer that each candidate retains exact degree M after arbitrary linear normalization, nor exclude subbanks under a substantially reduced degree normalization, other arrays, candidate-dependent scalars/shifts, or fixed-size lists. Those exclusions are correctly absent from the source note. No correction is needed.
