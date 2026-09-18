# Independent audit: uniform first-jet equality rigidity

Verdict: PASS for UNIFORM_CONTACT_EQUALITY_RIGIDITY.md under its exact hypotheses.
No characteristic bound p>w is necessary; p>a is used only to divide by a when
recovering the received polynomial. The endpoint is degree <=w.

## Independent local-coordinate proof of the missing lower-degree exclusion

This verifies root's alternative argument and does not depend on the subset-pencil
proof in the main note. Work over the coefficient field, which may be k(Z), and
put Lambda(X)=product_x(X-x). Let F_k be the top homogeneous (Y,R) part of a
nonzero source, of total degree k. Taking the highest homogeneous degree in
(R,E) in each local contact identity shows

    F_k(x+t,tR+t^2 E,R)=0 mod t^a.

Make the global polynomial substitution

    Y=Lambda U,   R=Lambda' U+Lambda V.

At a node x, writing Lambda=ell*t+O(t^2), this corresponds to the regular local
change

    R=Lambda' U+Lambda V,
    E=((Lambda-tLambda')/t^2)U-(Lambda/t)V.

All coefficients are regular power series, and its determinant at t=0 is
-ell^2 !=0. Thus the transformed F_k is divisible by t^a coefficientwise at
every node. Because the nodes are distinct, it is globally divisible by
Lambda^a coefficientwise in U,V.

Write

    F_k=sum_{j=0}^k A_j(X)Y^(k-j)R^j,
    deg A_j <= (a-k)w+j.

If k<a, the coefficient of V^k after transformation is Lambda^k A_k.
Hence Lambda^(a-k) divides A_k. But

    deg A_k <= (a-k)w+k < (a-k)n,

since n-w>a>k and a-k>=1. Therefore A_k=0. Descending j, after the higher
coefficients have vanished, the coefficient of U^(k-j)V^j is Lambda^k A_j,
and the same divisibility and strict degree inequality force A_j=0. This
contradicts nonzero F_k. It proves the missing lower-total-jet-degree exclusion
in every characteristic, provided the nodes are distinct.

## Cross-checks of the main proof

* The weight bound and a<w-1 imply total jet degree at most a.
* Formal source contact implies contact along an actual polynomial arc: after
  R=P', the residual E=(P-w_x-tP')/t^2 is polynomial whenever P(x)=w_x.
* In the subset-pencil proof, the X^(aw) coefficient depends only on the weighted
  leading terms and the pencil coefficient c, not on the selected w-subset.
  This remains valid when the integer w vanishes in the coefficient field.
* Varying the extra node over n-w+1>a distinct values proves the polynomial
  identity in that node parameter, without an infinite-field assumption.
* H_T'/H_T=H_B'/H_B+1/(X-z) is transcendental as a rational function in the
  indeterminate z, even in positive characteristic. Hence the top piece is cY^a.
* The next homogeneous piece has coefficients B_j of degree <=w+j<n; its
  descending contact equations kill j>=1 and give a*c*w_x+B_0(x)=0.
* The residual after subtracting c(Y-P)^a still has weight <=aw and contact a,
  and the independently verified exclusion forces it to vanish.

## Affine received-line refinement

If the received symbols are w_x(Z)=f_x+Zg_x over the original field k, the
conclusion obtained over k(Z) can be stated without rational challenge poles.
Choose any w+1 of the n nodes. The degree<=w interpolant through their values is

    P(X,Z)=P_0(X)+Z P_1(X),   P_0,P_1 in k[X], deg_X<=w.

Uniqueness of interpolation identifies it with the P obtained over k(Z).
Thus the entire received line is a codeword pencil, not merely a rational
challenge family. If the original source belongs to k[X,Y,R,Z], its coefficient
c of Y^a lies in k[Z], and the identity F=c(Z)(Y-P_0-ZP_1)^a holds in the
polynomial ring. No exceptional challenge labels or denominator exclusions are
needed for this identity.

This refinement does not extend the theorem to nonuniform contact or positive
weight excess; those are distinct unresolved resource cases.
