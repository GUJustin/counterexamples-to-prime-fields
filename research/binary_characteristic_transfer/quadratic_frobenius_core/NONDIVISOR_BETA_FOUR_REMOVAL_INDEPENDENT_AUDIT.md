# Independent audit: remove the excluded beta=4 character spike

Verdict: PASS. This sharpens the previously audited coprime-chart moment screen; it does not assert a construction or a low-energy theorem. Read the current `NONDIVISOR_DISCRIMINANT_GATE.md` and its independent audit. No verifier edits or duplicate field enumeration.

Assume p odd, n|p−1, 3<=e<=n−1, gcd(e−1,n)=1. Retain the note's notation m', E_*, C_*, K, and nonzero fibers M_v.

## Parity is essential and sufficient

For every t in mu_n\{1},

 4−v_t=4 t^(e−2) ((t−1)/(t^(e−1)−1))².

All displayed factors are nonzero. If n is even, coprimality forces e−1 odd, hence e even, making t^(e−2) a square. If n is odd, mu_n lies in the square subgroup of F_p*, so t is a square regardless of e. Thus 4−v_t is always a nonzero square. This covers every parity case; without the coprime-chart hypothesis, the first case would fail.

In particular no v_t equals four, and every retained nonzero fiber contributes +M_v to H_*(4). Since chi(4)=1,

 J(4)=H_*(4)=m'.

This is an exact identity, including multiplicities and zero-fiber deletion, not an equidistribution estimate.

## Remaining moments

On B=F_p\{0,4}, of size N=p−2, remove J(0)=0 and J(4)=m' from the earlier full-field moments. The result is

 S1=sum_B J=−2m',
 S2=sum_B J²=p E_*−2m'²−C_*².

In particular S2 is nonnegative and N S2>=4m'² by Cauchy. The assumptions e>=3,e<=n−1 imply p>=5, so N is positive. If m'=0, all these quantities vanish and no K>0 shape qualifies; no division-by-zero exception is hidden.

For K>0 and c>=0, the count of beta in B with J(beta)>=K is at most

 (S2−4m'c+N c²)/(K+c)².

The nonnegative minimizer is c=(S2+2Km')/(NK+2m'). Substitution gives exactly

 count <= (N S2−4m'²)/(S2+N K²+4Km').

The denominator is positive for K>0. In the zero-variance case all remaining J equal their nonpositive mean and the count is zero, consistent with this formula. The earlier stronger necessary threshold J(beta)>=K+M_beta can only reduce the count further.

If any admissible shape qualifies, its square alone contributes at least K² to S2. Thus necessarily

 p E_* >=2m'²+C_*²+K².

This necessary inequality is valid whether or not the one-sided bound is evaluated or rounded. It removes an artificial favorable spike at the excluded discriminant-zero coefficient shape beta=4. The quantity E_* itself has not been bounded here.

## Scope

Both beta=0 (nonzero coefficients) and beta=4 (the separately treated square family) are genuinely excluded in the surviving problem. The refinement is therefore legitimate for exactly that problem; it must not be used to bound a family that intentionally restores beta=4. Passing this remaining-shape screen does not prove roots occur in the evaluation subgroup or furnish a high-agreement candidate.
