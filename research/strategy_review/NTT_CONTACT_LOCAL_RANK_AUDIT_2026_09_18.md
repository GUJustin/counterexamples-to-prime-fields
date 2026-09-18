# Independent local-rank audit of the cyclic contact test

September 18, 2026. PASS: the proposed injectivity test at monomial exponent 181275 cannot work. This is not a new uniform rank saving.

For m=115, joint degree cap Q=159, and R cap s=35, fix homogeneous joint degree d and put l=max(0,d-s). After translating the received value, the allowed coefficient module has basis Y^i R^(d-i), l<=i<=d. Translation preserves both caps. A unit triangular change over the truncated local coefficient ring replaces this basis by

    Y^l (Y-tR)^k R^(d-l-k), 0<=k<=min(d,s).

Under the full contact substitution Y=tR+t^2 E, these become

    t^(l+2k) (R+tE)^l E^k R^(d-l-k).

Multiplication by the common monic polynomial (R+tE)^l is injective over the truncated coefficient ring: its leading coefficient in R is 1. Before this multiplication the distinct k have distinct monomials in R,E. Hence the image dimension for this homogeneous component is exactly

    sum_(k=0)^min(d,s) max(m-l-2k,0).

Different d remain homogeneous of different degree and do not mix. Every original X coefficient prefix has length at least 6336, greater than m, so there is no local coefficient truncation beyond t^m. Summing over d=0,...,159 gives exactly 182580.

A character subspace on the cyclic domain maps, after invertible coordinate and unit changes, into this same one-node image. Therefore its image dimension is at most 182580. Each of the 48 maximal supports in the compression note has 182584--182687 columns, proving a kernel in each. No dense matrix or conjectural determinant identity is needed.

## Cross-check against the frozen source ledger

Write r(q) for the same local dimension with joint cap q. Including all Z coefficients, with L=274277 and n=262144, the full local row bound is

    n * ((L-Q+1)*r(Q) + sum_(q=0)^(Q-1) r(q))
      = 13125118926520320.

This is exactly the PRE-EXISTING frozen row count. The original column count is 13123663101701085, smaller by 1455824819235. Consequently this calculation supplies no new uniform cokernel saving and no better.codes improvement. The special word's extra kernel does not establish the needed all-word assertion.

The useful change in next action is to cancel the 48-profile injectivity test and any associated matrix allocation. A different exponent must first pass the dimension ceiling; a perturbation must first supply a justified map between the old kernel and cokernel. Neither condition alone proves injectivity or repairs the benchmark.

## Independent check of the elementary exponent restriction

For a received word X^a with 0<=a<n and second row zero, the polynomial (Y-X^a)^115 is a nonzero contact helper. Its weight is 115*max(w,a), hence strictly below W=115*181275 whenever a<181275. Its joint degree is115 and its R degree is zero, so both other caps hold.

For a>211940=n+w-181275, use (X^(n-a)Y-1)^115 instead. The inner polynomial vanishes at all prescribed domain values because X^n=1 there, giving contact order at least115 after taking the power. Its weight115*(n-a+w) is strictly below W. The other caps again hold.

Thus only the inclusive30666-element interval181275<=a<=211940 can possibly give an injective monomial-word map. Endpoint equality is correctly retained because the source weight bound is strict. This restriction is algebraic, independent of a rank computation, and applies only to the monomial received pair (X^a,0).
