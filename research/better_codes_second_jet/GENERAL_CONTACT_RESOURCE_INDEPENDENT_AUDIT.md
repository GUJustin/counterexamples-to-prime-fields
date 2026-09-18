# Independent audit: the general contact resource and its equality case

Verdict: PASS. The leading R-coefficient argument proves the resource for arbitrary received words, without binomial-size, coprimality, or uniform-contact assumptions. The proof below independently obtains the required bound directly; it does not assume the stronger local weighted-valuation lemma.

Let k be a field, n distinct nodes x in k carry arbitrary symbols w_x, and w>=2 with n>=2w. For nonzero F in k[X,Y,R], let V be its weighted degree for weights (1,w,w-1). Let a_x be its actual formal contact, namely the t-adic order after

    X=x+t, Y=w_x+tR+t^2 E.

Put r=deg_R F, write A_r=[R^r]F, put q=deg_Y A_r, and let B=[Y^q]A_r, d=deg_X B.

## 1. The pointwise inequality

At a fixed node first translate Y by w_x. This preserves r,q,B. Select the homogeneous (Y,R)-degree q+r component G. Its coefficient of Y^q R^r is B(x+t). Since its R-degree is at most r, every term of G is divisible by Y^q. Write G=Y^q H, where H is homogeneous of degree r and H(t,0,1)=B(x+t).

Distinct homogeneous jet degrees remain distinct homogeneous degrees in (R,E) after substitution, so they cannot cancel. Therefore

    a_x(F) <= contact(G) = q+contact(H).

Dehomogenize h(t,Y)=H(t,Y,1), and expand

    h(t,Y)=sum_j c_j(t)*(Y-t)^j.

All c_j lie in k[t]. Substitution Y=t+t^2 E shows

    contact(H)=min_j(ord_t c_j+2j)=b.

On the other hand,

    B(x+t)=h(t,0)=sum_j c_j(t)*(-t)^j.

Since ord c_j>=0, each summand has order ord c_j+j >=ceil(b/2). Thus ord_x B>=ceil(b/2), proving

    a_x(F) <= q+2 ord_x B.                      (1)

This argument divides by no scalar and is valid in every characteristic. The homogeneous substitution is injective, so none of the contact orders of nonzero pieces is infinite.

## 2. Global resource and factor additivity

Summing (1) over the distinct nodes gives sum a_x<=nq+2d. Also

    V >= r(w-1)+qw+d.

Consequently

    e(F):=V-(w/n)sum a_x
         >=r(w-1)+(1-2w/n)d >=r(w-1)>=0.       (2)

For a factorization Q=c product F_i^m_i, weighted degree and local contact are additive, so the e-values are additive. A primary source of contact at least m at every node and V(Q)<mA therefore satisfies

    sum_i m_i e(F_i) = e(Q) <m(A-w).

This recovers the source resource without the previous combinatorial hypothesis. It also charges R-degree, but the resulting numerical R-degree total bound need not beat existing support caps.

## 3. Zero-charge classification

If e(F)=0, (2) and w>=2 force r=0. Now F is R-free. Taking the coefficient R^q E^0 after substitution gives the stronger inequality

    a_x(F)<=q+ord_x B.

Hence

    e(F)>=V-qw-(w/n)d >=(1-w/n)d.

Since n>w, equality forces d=0 and V=qw. Each a_x<=q and their average equals q, so all a_x=q. If q=0 this says F is a nonzero scalar in k.

Suppose q>=1 and char(k)=0 or char(k)>q. Write

    F=B Y^q+C(X)Y^(q-1)+lower terms,

where B is a nonzero scalar and deg C<=w. The coefficient of t^(q-1)R^(q-1) in the local contact identity is qB w_x+C(x); it must vanish. Thus P=-C/(qB) has degree at most w and P(x)=w_x at every node.

Translate Y by P(X). This preserves the weight cap and formal contact: locally the changes in R,E absorbing P(x+t)-P(x) form an invertible triangular polynomial substitution. The translated polynomial has zero-word contact q. If its coefficient of Y^j is C_j(X), the coefficient of R^j E^0 after local substitution shows

    (X-x)^(q-j) divides C_j for every node, j<q.

Therefore Lambda^(q-j) divides C_j, where Lambda is the squarefree domain locator. But deg C_j<=(q-j)w<(q-j)n, so C_j=0. This proves

    F=B*(Y-P(X))^q.

No hypothesis q<w, n>w+q, or gcd(n,w)=1 is needed. The sufficient characteristic condition may be weakened to q nonzero in k for this equality proof; the stated char>q condition is safe and matches the intended theorem.

For coefficients in k(Z), the same proof is valid over that field. If the received symbols are affine in Z and n>w, interpolation at w+1 nodes makes P affine in Z coefficientwise. Clearing scalar factors must be handled separately from this field-level statement.

## Scope

The argument concerns carrier factors and their R-degree. It does not assign independent charge to every first-tail component within a carrier. The previously constructed binding simple-tail model has e=45w and r12 and satisfies (2); it is not excluded. No improvement of the full benchmark ledger is claimed by this audit.

## 5. All-characteristic equality classification — independent extension audit

Verdict: PASS. The characteristic restriction in Section3 can be removed entirely, while retaining w>=2 and n>=2w. Here are the missing positive-characteristic steps.

From Section3, a zero-charge F is R-free, has weight qw, has constant nonzero leading Y-coefficient, and has actual contact q at every node. Suppose char(k)=p divides q.

First differentiate the local identity with respect to R. Since F is R-free, this gives t*(F_Y)_sub, so F_Y has contact at least q-1 at every node. If F_Y were nonzero, its weight would be at most (q-1)w. Nonnegativity of charge forces equality throughout: F_Y has zero charge, weight (q-1)w and uniform contact q-1. The characteristic-free part of Section3 says any R-free zero-charge polynomial has contact equal to its Y-degree. But the top Y^q term differentiates to zero, so deg_Y F_Y<=q-2, a contradiction. Thus F_Y=0.

Differentiating the local identity in t now shows that F_X has contact at least q-1, since the chain-rule term (R+2tE)F_Y vanishes. If F_X were nonzero, let j be its Y-degree and B_j(X) its leading coefficient. Every Y-exponent of F is divisible by p, and the leading coefficient of Y^q is constant. Hence j<=q-p. Set d=q-j>=p>=2. The R-free contact inequality gives

    ord_x B_j >= q-1-j=d-1

at every node. Therefore deg B_j>=n(d-1). But differentiation decreases weighted degree by at least one, so

    deg B_j <= (q-j)w-1=dw-1.

These are incompatible because n>=2w and d>=2 imply n(d-1)>=dw>dw-1. Thus F_X=0 as well.

Over the perfect closure of k, all coefficients have p-th roots, and F_X=F_Y=0 gives F=G^p. Polynomial evaluation commutes with p-th powers, so G has weight (q/p)w and contact exactly q/p at the same nodes and received symbols. It therefore has zero charge. Repeating this reduction eventually gives an exponent not divisible by p, where the coefficient argument of Section3 applies. Ascending the powers gives

    F=B*(Y-P(X))^q,   deg P<=w.

Finally P descends from the perfect closure to the original coefficient field: it agrees with the original symbols at n>w nodes, so interpolation at any w+1 of those original-field nodes uniquely reconstructs P over k. The scalar B is already the original leading Y-coefficient. The case q=0 remains a nonzero scalar.

Thus the full graph-power classification holds in every characteristic. No Frobenius exception survives under these weight/contact and n>=2w hypotheses. For k(Z)-coefficients and an affine received word, the same interpolation also gives the affine-in-Z refinement stated above.
