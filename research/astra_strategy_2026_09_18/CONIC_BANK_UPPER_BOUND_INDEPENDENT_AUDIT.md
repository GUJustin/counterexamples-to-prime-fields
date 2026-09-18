# Independent audit of the conic-bank lifting obstruction

Reviewed `fixed_rate_lift_finish.answer.md`. Result: **PASS**, including zero-direction coordinates, constant graphs, duplicate bank witnesses, and the inherited-witness scope.

Use the standard RS convention 1≤k≤N and distinct evaluation nodes. Thresholds T>N have no qualifying labels and can be dismissed. Interpolating both source words on any k nodes proves their actual common agreement A≥k. Therefore T>A implies T>b and T−k+1>0; all displayed denominators are positive. This convention should be stated if the theorem is extracted from the answer.

## Independent incidence proof

Let Q_theta=H+theta U+theta^(-1)V, with U,V not both zero and degrees<k. Let b count the common zeros of U,V, so b≤k−1. Count qualifying parameter pairs (theta,lambda), which upper-bounds the number of qualifying labels even if different parameters give identical bank polynomials.

At a node with G≠0, agreement is the Laurent graph
lambda=(U/G)theta+(V/G)theta^(-1)+(H−F)/G.
Two distinct graphs have at most two intersections for theta≠0, since multiplication by theta gives a nonzero quadratic. This remains valid in small characteristic.

Remove Z={U=V=G=0,F=H}, with z=|Z|. These nodes agree at every parameter pair. For one qualifying pair, group its remaining matches as follows:
- one group containing all G=0 matches;
- one group for each identical nonconstant graph;
- one group of constant-graph matches, of size h.
All matching constant graphs have the same value lambda. Their nodes satisfy U=V=0, so z+h≤b.

Every group of the first two kinds, of size m_i, has m_i+z≤A. For G=0, the simultaneous witness pair is (Q_theta,0). For a nonconstant graph with U/G=a≠0, it is (H−cU/a,U/a), where c=(H−F)/G is the common graph constant. If a=0, use V/beta instead. These are valid degree<k polynomials and also explain Z. Thus sum m_i²≤(A−z)sum m_i.

Write w=sum m_i and s=z+h+w≥T. Counting pairs in different groups, but not pairs within the constant group, gives
h w+(w²−sum m_i²)/2 ≥ w(s+h−A)/2 ≥ (T−b)(T−A)/2.

Each unordered coordinate pair contributes at most twice over all qualifying parameter pairs. Distinct G≠0 graphs intersect at most twice. For a G=0/G≠0 pair, the former's equation is
U theta²+(H−F)theta+V=0.
It is nonzero after removing Z: if all three coefficients vanished, that node would lie in Z. Thus it has at most two theta roots, and the other node determines lambda. Two G=0 nodes are never paired in this count; neither are two constant graphs. This accounts for all degeneracies.

The total pair budget is at most2 binom(N,2)=N(N−1). Consequently the number of qualifying pairs, and hence labels, is at most
2N(N−1)/[(T−b)(T−A)].
Using b≤k−1 proves the second bound in the answer. In particular if T−k≥epsilon N, the bound is at most2N/(epsilon(T−A)).

## Transformation scope

A common field-affine-linear map on the witness space preserves H+theta U+theta^(-1)V. Polynomial pullbacks and common multipliers are examples once the resulting witnesses lie in the stated RS code. Puncturing changes only the evaluation domain. For ordinary coordinate shortening, three surviving distinct parameters force the shortening equation's quadratic in theta to vanish identically, so the common shortening factor divides U,V and H minus the prescribed polynomial. Dividing retains the conic form. If fewer parameters survive, there are at most two inherited bank members.

Thus the theorem excludes superlinear bank-witnessed populations after these uniform transformations at fixed positive capacity margin. It does not restrict genuinely new witnesses, nonlinear transformations that do not preserve the conic span, or growing unions of independently transformed banks beyond the stated union bound. The actual post-transformation common agreement A must be used; carrying an old value through a transformation without proving it would not be valid.

The obstruction is compatible with the new growing-gap construction: there K=3 but T/N→0, so there is no fixed positive capacity margin. It is also independent of whether threshold lists are singleton.
