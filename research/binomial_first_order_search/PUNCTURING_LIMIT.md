# Puncturing the Dickson bank cannot reach the first-order regime

September 17, 2026. Restricted-family result, extending
`DICKSON_FIRST_ORDER_LIMIT.md`. This is not an upper bound for arbitrary
Reed--Solomon lists and supplies no intrinsic tightness lower bound.

## Arbitrary domains and candidate subsets

Let p=4k+1 be prime, k>=2, and use the polynomial G and the complete
2k-element binomial bank Q_a from the preceding note. Let D be ANY
n-element subset of F_p^*, with k<n<=4k, and let the received word on D
be arbitrary. For any L-element subset of either one of the two
k-element candidate orbits, its minimum agreement is at most

    B(n,k) + 4 Lambda + 8 Lambda sqrt(k/L) + 36k/L + 1,       (1)
    B(n,k)=min(n/2,n/4+k/2),  Lambda=8(sqrt(p)+3).

In particular, fewer than 2^23 members of the complete bank can all have
agreement greater than B(n,k)+k/4. The bound is uniform in the domain,
received word, prime, and candidate subset. The constant is deliberately
loose. It includes domains chosen after inspecting the candidates.

Proof. Let n_s and n_ns count the square and nonsquare coordinates of D.
The constant masks have densities 1/4 on square cosets and 1/2 on
nonsquare cosets. Thus their mean contribution to average agreement is

    n_s/4+n_ns/2 = n/4+n_ns/4 <= B(n,k),

because n_ns<=min(n,2k). On each H-coset the error in a mask mean is at
most Lambda/k. On square coordinates choose the larger of the two mask
counts: its mean is still at most L/4+L Lambda/k, with the sum of the
two absolute deviations added. Thus all mean errors contribute at most
n Lambda/k<=4 Lambda after dividing by L. The same Parseval estimate
as in the preceding note applies to an arbitrary subset of a coset:
restricting the sum of squared deviations can only decrease it. Summing
the two masks on each square coset and the single mask on each nonsquare
coset gives at most 6 Lambda sqrt(k/L), hence the stated bound of 8.
Residual fibers contribute at most 9n/L<=36k/L. The harmless extra 1
retains the normalization of the preceding note. This proves (1).

The change of variable and word that identifies the second orbit with
the first sends an arbitrary D to another arbitrary subset of F_p^*;
it does not require a full domain. In either orbit L<=k and
Lambda<42 sqrt(k), so the error in (1), divided by k, is at most

    504/sqrt(L)+37/L.

At L=2^22 this is strictly less than 1/4, and it decreases thereafter.
Any 2^23 candidates contain at least 2^22 from one orbit, proving the
claimed bound.

## Comparison with the audited first-order threshold at every rate

Write rho=k/n, so 1/4<=rho<1, and

    b(rho)=B(n,k)/n=min(1/2,1/4+rho/2).

The continuum first-order threshold a_*(rho) audited in the separate
support note satisfies

    a_*(rho)>b(rho)+rho/4.                               (2)

Here the threshold equals the positive root of

    F_rho(a)=(8-rho)a^2-6rho*a+rho*(4rho-5)

up to rho_*=8-3sqrt(6). For rates from 1/4 through 1/2 this also follows
directly from the audited cap-completion lemma: at the displayed root,
the cap surplus is -(2-rho)B(B-B_0)^2/6 with
B_0=3(1-a)/(2(2-rho))<=a/rho-1. Thus its maximum is zero and a
positive-area cap attains it. Above rho_* the optimized high-rate threshold
is strictly greater than (1+sqrt(2rho-1))/2, as proved in the high-rate
curve audit. Thus this comparison includes the high-rate refinement,
not only the older unrefined curve.

For 1/4<=rho<=1/2, substitute a=1/4+3rho/4:

    F_rho(a)=-(rho-1)*(9rho^2-49rho+8)/16<0.

The quadratic factor is decreasing and already negative at rho=1/4.
For 1/2<=rho<=rho_*, substitute a=1/2+rho/4:

    F_rho(a)=-(rho-2)*(rho^2-42rho+16)/16<0.

Again the quadratic factor is decreasing and negative at rho=1/2.
Since the constant coefficient of F_rho is negative, a positive input
with negative F_rho lies below its positive root. For rho>rho_*, use
rho_*>5/8 and

    2rho-1-rho^2/4>0  for 5/8<=rho<=1,

which implies (1+sqrt(2rho-1))/2>1/2+rho/4. This proves (2).

Consequently fewer than 2^23 complete-bank candidates can simultaneously
exceed the audited first-order threshold on ANY puncturing of the full
nonzero prime-field domain. Neither a specially chosen received word,
an arbitrary candidate subbank, nor arbitrary coordinate deletion makes
this particular bank witness growing lists in that regime.

This does not address other polynomial families, changing the evaluation
points rather than selecting a subset, or lists below the first-order
threshold. In particular it does not contradict the existing linear-size
quarter-rate list at agreement 3/8.

## Verification and scope

`verify_puncturing_limit.py` checks the polynomial factorizations,
the exact endpoint and monotonicity inequalities used above, and the
domain-size baseline. These checks do not substitute for the character-sum
estimate. That analytic input and the already checked branch identities
are those of the preceding audited note.
No independent human or separate-agent review, and no novelty claim.
