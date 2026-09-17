# Binomial sections as a possible short-domain character construction

September 17, 2026. Exploratory exact search; no growing-family result.

Choose p=2rk+1 prime, a section 0<=j<r, and e=rk+j. Define

    G(X)=sum_{i=0}^k binom(e,ri+j) X^i.

Its leading coefficient is1 and its linear coefficient is nonzero
modulo p, since e<p. For each h in H=mu_k, put P_h(X)=G(hX)-X^k.
These are exactly k distinct degree-<k polynomials: the leading terms
cancel and the linear coefficient distinguishes h.

On a coset aH, let v_a be a most frequent value of G, with frequency
m_a. Use the constant received value v_a-a^k on that coset. Multiplying
inputs by h permutes the coset, so every P_h has exactly m_a agreements
there. Choosing the c cosets with largest m_a gives length n=ck,
rate1/c, list size at least k, and agreement M=sum(top c frequencies).
This is the optimal agreement for this orbit among all H-invariant
words on c cosets. The received word generally has degree greater than
M, so the preceding low-degree boundary-word classification does not
exclude this route.

If c were fixed, r,k both grew, and M/k stayed above1+c*eta for a
fixed eta>0, this would give unbounded lists at fixed positive gap with
n/p approximately c/(2r) tending to zero. For fixed eta, strict Elias
would hold eventually. This conditional implication is the reason for
the search; none of its asymptotic hypotheses is established here.

## Exact search outcome

The initial section j=1 search covered184 admissible (r,k) pairs with
r=2,...,80 and k in {8,11,16,23,32,47,64,97,128}. Only r=2 had a
positive surplus on four cosets, reproducing the Dickson mechanism.

The extended scan covers726 cases using the distinct choices among
j=0,1,floor(r/2),r-1. It records every coset's exact mode, frequency,
and received symbol. Some higher sections give finite positive surplus,
but at rate1/4 none except the two r=2,j=1 cases is strictly below
the characteristic-based Elias bound.

At c=8,16,32 there are respectively30,143,240 below-Elias cases,
but their largest observed k values are only11,16,32. These are finite
lists, not evidence of unbounded k at fixed c. For example r78,j0,k8
gives p1249, n64, eight distinct candidates and16 agreements, at exact
rate and gap1/8. No proposed universal bound is refuted by that example.

## Verification and scope

The C++ census uses modular binomial recurrence, exact Horner evaluation
at every nonzero field point, and exact mode counts. Assertions remain
enabled. verify_binomial_sections.py independently uses integer binomial
coefficients and checks every coset and all candidate polynomials in
five fixtures, including the known full-length Dickson cases and a
shorter lower-rate case. It applies the exact integer Elias inequality
to every recorded c=4,8,16,32 construction.

The scan is not an impossibility proof for other section choices,
larger parameters, nonconstant words inside cosets, or different
hypergeometric families. It currently offers no fixed-gap asymptotic
improvement, no prescribed-code/better.codes improvement, and no new
manuscript claim.

## All section indices in an expanded fixed-k audit

The subsequent `all_sections.cpp` scan covers every j=0,...,r-1 for
r=2,...,48 and k in {16,32,64,128} whenever 2rk+1 is prime:989 cases.
At c=4 the only below-Elias case is the known r2,j1,k64,p257 example.
There are no c8 cases; c16 has6 cases with largestk16, and c32 has261
with largestk32. This does not reveal growing lists at fixed c.
The new j29/r38/k16 example is independently replayed along with three
other fixtures by `verify_all_sections.py`, including every candidate
polynomial and coset mode. The checker uses the exact characteristic
Elias inequality, which includes one extra c32 case compared with the
simpler sufficient entropy inequality used in the discovery summary.
The final summary is regenerated from the exact checker. No new
manuscript theorem or impossibility claim follows.

The later ORBIT_DOMAIN_OPTIMALITY.md removes the earlier invariant-word
qualification: for the full chosen subgroup orbit and lengths divisible
by its order, the modal coset construction maximizes minimum agreement
over ALL domains and received words, including domains containing zero.
It also records the independently checked4,326-case subgroup scan.
Arbitrary non-subgroup subsets of the candidate orbit remain outside
that optimization statement. No unbounded fixed-gap family was found.
