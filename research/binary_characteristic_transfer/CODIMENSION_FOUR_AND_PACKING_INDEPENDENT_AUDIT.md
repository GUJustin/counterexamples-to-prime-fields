# Codimension-four compiler and support-packing audit

September 18, 2026. Independently read the general locator elimination in the binary manuscript's `sections/constructions/quadratic-near-johnson.tex`, including its fixed-characteristic remark. The proposed s=4,d=7 specialization is a genuine scalar received line, but its enhanced-support route cannot improve the p^5 population exponent.

## Single-label compiler is valid

Let B=F_(p^7), and range over three-dimensional subspaces with locators

    L=X^(p³)+aX^(p²)+bX^p+cX.

Set b0=1 and

    b1=theta1-a^(p³),
    b2=theta2-b^(p³)-b1*a^(p²),
    b3=theta3-c^(p³)-b1*b^(p²)-b2*a^p.

Then L^(p³)+b1 L^(p²)+b2 L^p+b3 L has the four fixed high coefficients 1,theta1,theta2,theta3 at exponents p^6,p^5,p^4,p³. Its coefficient at X^(p²) is the single scalar

    z=b1*c^(p²)+b2*b^p+b3*a.

The remainder has degree at most p and zero constant term. Dividing by X and negating the remainder gives a strict degree-<p witness for the line with direction g=X^(p²-1). Thus there is no multihead-label defect.

With 1,theta1,theta2,theta3 independent over B, the triangular label coefficients recover the three locator coefficients, giving [7 choose4]_p~p^12 distinct labels. However the theta3 coefficient of the complete residual is L itself. Its roots on B are exactly W. This independent-parameter choice has no extra outer fibers: agreement remains p³-1, below first order for length p^7 and dimension p.

Specializing to dependent heads could create extra fibers but loses the automatic injectivity guarantee. Regardless of how that is addressed, the following packing bound controls distinct labels with enough canonical agreements.

## General packing lemma

Let D be any d-dimensional F_p-linear domain, not necessarily a field. Suppose distinct labels z_i have degree-<p designated witnesses h_i for a common received line f+z_i g, where g=X^(p²-1). Assume each designated support contains V_i minus zero for an F_p-subspace V_i of the domain. This holds for the canonical compiler: its multiplied residual is linearized, so its roots in D form a subspace. Whether zero also matches only strengthens the argument.

For distinct labels, (z_i-z_j)g-(h_i-h_j) is a nonzero polynomial of exact degree p²-1. It vanishes on (V_i intersect V_j) minus zero. Therefore

    dim_Fp(V_i intersect V_j)≤2.

This argument depends only on distinct scalar labels, the degree bounds, and inherited subspace supports. It does not require independent head coefficients or a subfield domain.

If each V_i has dimension at least r, select an r-dimensional subspace in each and pass to annihilators in the d-dimensional dual space.

* For d=2r-1, r≥3, the annihilators have dimension r-1 and pairwise intersection dimension at most one. Each two-plane belongs to at most one annihilator, so

      M≤[2r-1 choose2]_p / [r-1 choose2]_p =Theta_r(p^(2r)).

  In terms of N=p^d the exponent is 1+1/d, at most 6/5 for d≥5. At d=7 this is p^8=N^(8/7), strictly below the existing p^5 example's exponent 6/5.

* For d=2r, r≥2, if support dimensions are at least r+1, choose such subspaces. Their annihilators have dimension r-1 and pairwise trivial intersection. Packing one-dimensional spaces gives

      M≤[2r choose1]_p / [r-1 choose1]_p =Theta_r(p^(r+1)),

  with exponent (r+1)/(2r). In particular the even-dimensional route does not restore the desired improvement.

These are bounds on distinct qualifying labels, not on the number of original locators mapping to them.

## Why first order forces those dimensions

For code dimension p and length p^d, rho=p^(1-d). In the low-rate branch, the primary DKT curve satisfies

    N*a1(rho)>sqrt(N*p/2)=p^((d+1)/2)/sqrt(2).

For d≥4 and p≥3 this is in the low-rate branch. If d=2r-1, a subspace of dimension at most r-1 has fewer points than this threshold. If d=2r, a subspace of dimension at most r has fewer points than the threshold. Thus canonical supports above first order must satisfy exactly the dimensions used above. The argument does not rely on a large-p asymptotic threshold approximation.

## Scope and decision

The s4,d7 scalar compiler is valid, but independent parameters forbid the proposed outer fibers. Dependent parameters cannot yield more than O(p^8) distinct above-first-order canonical labels, by packing, even if they generate many enhanced locators before collisions. Consequently this route cannot improve the p^5 exponent 6/5. Solving the extra norm/image conditions is unnecessary for the proposed exponent-12/7 objective.

The lemma does not exclude new noncanonical witnesses whose agreement supports are not linear subspaces, other source-direction degrees, non-linear domains, or different code dimensions. It is a constructive-route stopping criterion, not a universal first-order bound.
