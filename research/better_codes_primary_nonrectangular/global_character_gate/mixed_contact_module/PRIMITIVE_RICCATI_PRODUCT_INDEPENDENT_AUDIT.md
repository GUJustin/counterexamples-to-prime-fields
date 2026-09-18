# Independent audit: actual-weight obstruction for primitive Riccati products

Status: PASS. This stronger argument supersedes the nominal-only limitation for the specified multiplicative construction. It does not apply to sums of products or general Y/R-dependent multipliers.

Let Q=a2(X)Y^2+a1(X)Y+a0(X)+d(X)R, with d nonzero and gcd(a2,a1,a0,d)=1. Define contact at a by substituting X=a+t, Y=f_a+tR+t^2E, with R,E free, and taking t-order. Work with distinct nodes over any field; the following coefficient argument does not need a characteristic-zero assumption.

If contact were at least three, the coefficient of t^2 R^2 would force a2(a)=0. The coefficient of t^2 E is then a1(a), so a1(a)=0. The coefficient of R at t^0 forces d(a)=0, and the remaining constant term forces a0(a)=0. This contradicts primitivity, including after extending the field to contain the node. Hence contact is always at most two. If contact is positive, already the t^0 R coefficient gives d(a)=0. Therefore the sum of factor contacts over all selected nodes is at most twice the number of distinct roots of d, hence at most 2 deg d.

For original weights (1,w,w-1), write W=wt(Q). The term dR gives deg d<=W-w+1, so total contact<=2(W-w+1). This is an actual bound on the fully primitive polynomial, not a nominal estimate from its unnormalized determinant formula.

Now take Z primitive factors Q_t, each with W_t<=4w-1, and an arbitrary nonzero scalar polynomial H(X). Assume their product has contact at least m at each of n selected nodes and m>2Z. Contact orders add exactly: the substituted leading coefficients lie in the integral domain k[R,E]. Thus at every node

    ord_a H >= m-sum_t contact_a(Q_t) > 0.

Summing yields deg H>=mn-sum_(a,t) contact_a(Q_t). Weighted degrees also add exactly under multiplication: the highest-weight forms multiply nontrivially in a polynomial domain. Consequently the actual product weight satisfies

    wt(H product Q_t)
      >= mn + sum_t W_t - 2 sum_t deg d_t
      >= mn - sum_t W_t + 2(w-1)Z
      >= mn - (2w+1)Z.

There is no hidden top-degree cancellation in this product, and its R-degree is exactly Z because its R-leading coefficient is H*product d_t, nonzero. Thus the cap Z<=35 is valid without a genericity assumption. Other source caps can only restrict this family further.

For m=115,n=262144,A=181275,w=131071 and Z<=35,

    wt(H product Q_t)-mA
      >= 115*(262144-181275)-35*(2*131071+1)
      = 124930 > 0.

Therefore no such product is an admissible helper of weight below mA. This includes arbitrary primitive Riccati factors within the stated weight bound, not merely triple determinants. It survives additional individual polynomial content, because one first divides out the full content and then uses the primitive factor's actual weight and actual contact. Higher tangencies cannot create contact above two without violating primitivity. Any polynomial-in-X factors removed or inserted are absorbed into H.

For triple determinants, raw weighted degree is at most 4w-1, so their primitive quotients meet the factor weight assumption. Their nonzero R coefficient follows from the product of the three nonzero pair differences. The raw contact-at-least-two/pair and at-least-four/triple statements and the squarefree triple-coincidence content divisor are consistent with this stronger primitive bound; after full normalization the residual contact is necessarily at most two.

Remaining escapes include sums or other linear combinations of these products, factors with higher Y/R structure, and multipliers depending on Y or R. The argument does not rule out a general list-conditioned interpolation kernel and does not show a benchmark improvement. It rigorously excludes this multiplicative Riccati construction at the frozen caps.
