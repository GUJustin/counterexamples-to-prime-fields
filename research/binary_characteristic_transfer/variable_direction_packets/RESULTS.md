# Variable-direction affine-line packets: exact head conditions

Read-only sources: binary repository `research/frontier/characteristic-and-domains.md`, section “Incomplete Artin–Schreier packets”, its AGENTS/current-status/strategy, and this repository's LOCATORS_TREES_NORMS_TRANSFER.md and GOLD_AND_NEAR_JOHNSON_LEDGER.md. No binary files changed. This is a bounded structural check, not a new fixed-rate counterexample.

Let E=F_(p²), p odd. A normalized affine F_p-line locator is X^p−aX−b, where a^(p+1)=1 and b lies in the image of X^p−aX. Distinct directions intersect once. Parallel distinct lines are disjoint.

## Product versus squarefree support

For r lines the raw product has degree rp. Selecting u slope terms and v intercept terms gives degree loss u(p−1)+vp. For u+v<p these losses uniquely determine (u,v). Thus matching a head through successive layers requires mixed elementary-symmetric conditions, not merely a single direction-sum condition. The first two are fixed sums of a_i and b_i, at losses p−1 and p.

More importantly, let m_x be the number of selected lines through x. The true locator is the raw product divided by D(X)=product_x (X−x)^(m_x−1). Its degree is rp−sum_x(m_x−1). For p>2 the raw product has zero coefficient immediately below its leading term; hence the true locator's first subleading coefficient is sum_x(m_x−1)x. Up to loss p−2 its normalized head is the reciprocal formal series of the normalized head of D. Common long heads therefore also constrain intersection moments. Ignoring this division does not certify agreements of size rp.

## Exact concurrent cancellation and its population

Fix center zero and r distinct directions S in the norm-one circle C (size p+1). The radical locator is

    R_S(X)=X product_(a in S)(X^(p−1)−a)
          =sum_(j=0)^r (−1)^j e_j(S) X^((r−j)(p−1)+1).

Its support has r(p−1)+1 points. Frobenius sends every a to a^−1, giving the exact identity

    e_(r−j)=e_r e_j^p.

Consequently fixing the first k elementary coefficients, with 2k<r, leaves at most (p+1)*p^(2(r−2k−1)) direction sets: choose e_r in the norm-one circle and the remaining middle coefficients. This is an upper bound, not a realization claim. For larger k there are at most p+1 choices. If the first k coefficients vanish and 2k>=r−1, all intermediate coefficients vanish. Such sets are precisely multiplicative cosets of the r-th roots of unity, requiring r | p+1. There are (p+1)/r of them, and

    R_S(X)=X^(r(p−1)+1)−a^r X.

For r=2 this gives (p+1)/2 supports with common head gap 2p−2. An arbitrary pair of nonparallel affine lines has a unique intersection c, and its radical has first subleading coefficient c. Thus varying c already loses this long common head; fixing c reduces to the displayed concurrent calculation after translation.

These are binomial/multiplicative-coset supports, not a new additive population mechanism. Apart from zero the supports partition E*. A domain retaining h of them has at least 1+h*r(p−1) points. In particular a domain of size O(p) retains only O(1) complete supports. This does not deliver the desired growing family at fixed positive rate with p>K.

More generally, if a domain of n<p² points contains R distinct complete affine lines, their incidence counts m_x satisfy sum m_x=Rp and sum m_x²<=Rp+R(R−1). Cauchy–Schwarz yields

    R <= n(p−1)/(p²−n).

Thus n=O(p) permits only O(1) complete lines, regardless of direction, and therefore only O(1) subsets of those lines. At fixed rate K/n bounded below and p>K, n=O(p). This closes the proposed complete-line-packet transfer in that contract; it does not exclude partial lines, higher-dimensional ambient domains, or unrelated locators.

## Exact small check

`check.py` uses independent tuple arithmetic in F_3² and F_5². It enumerates only subsets of their 4/6 direction parameters, verifies every Frobenius coefficient identity, reconstructs every concurrent support and evaluates its radical at all roots. `check.json` records the results. For p=3, the two opposite pairs have vanishing first coefficient, while no three-direction set does. For p=5, exactly three pairs and two triples have vanishing first coefficient; each exceptional triple also has vanishing second coefficient and is a cubic-root coset. No received-word search or large job was run.

Conclusion: direction cancellation is real and can multiply the head gap, but its maximally cancelled concurrent cases are familiar binomial cosets. The complete-line incidence bound prevents this route from retaining a growing support population in the requested fixed-rate p>K regime. Stop this route rather than extending the small census.
