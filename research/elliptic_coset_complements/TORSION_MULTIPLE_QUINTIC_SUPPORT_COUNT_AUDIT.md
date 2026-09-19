# Exact support count for the torsion-multiple quintic candidate

Independent audit: PASS. Let ell>14 be prime, different from the odd characteristic, and let E[ell] be rational. Write
`S={1,2,4,5,6}`, `W=±S` in F_ell*, and
`J_P=product_{j in S}(X-x([j]P))` for P!=O.
The domain consists of the n=(ell^2-1)/2 nonzero torsion x-coordinates.

## Quintics: precisely the ±P ambiguity

The ten elements of W are distinct. If J_P=J_Q, then some nonzero multiple of P equals a signed nonzero multiple of Q, so Q=[u]P for u in F_ell*. Equality is then equivalent to uW=W. Conversely this condition plainly suffices.

The multiplicative stabilizer K of W acts freely on W, so |K| divides10. It contains ±1 and therefore has order2 or10. Since1 belongs to W, order10 would imply W=K. In particular2,5 would both belong to this order-ten group, forcing ell to divide both2^10−1 and5^10−1. Their gcd is33, impossible for ell>14. Thus K={±1} for every prime ell>14, not only asymptotically or outside an unspecified exceptional set.

It follows that the number of distinct J_P is exactly n globally, and exactly ell(ell−1)/2 when P is restricted to E[ell] outside a specified order-ell subgroup H. The latter restriction is stable under sign.

The five signed points P,2P,6P,−4P,−5P sum to O. They therefore form a principal degree-five divisor after subtracting5O. A function in L(5O) representing it has the form a(X)+Yb(X), deg a<=2 and deg b<=1. Its conjugate norm is a nonzero scalar times J_P. Its pole has order exactly5, since all five zeros are finite; hence this is genuinely a quintic, not a lower-degree norm with an unaccounted pole. This checks the stated norm-quintic membership without asserting any received pencil.

## The two fibers and five extras are disjoint

For P outside H, its quotient image barP in E[ell]/H is nonzero. The two chosen x-fibers correspond to the signed quotient classes ±3barP and ±7barP. These are nonzero and distinct: neither3 nor7 is zero, and3±7 is nonzero modulo ell.

An extra x(jP) lies in one of these fibers exactly when j is congruent to ±3 or ±7 modulo ell. For j in S, all nonzero integer differences and sums at issue have absolute value at most13. Thus the exclusions hold for every ell>14. The five extras also have pairwise different signed quotient classes. Each selected fiber has ell distinct x-coordinates, so the entire support

`U_(H,P)=D_(H,3P) union D_(H,7P) union Z(J_P)`

has exactly2ell+5 coordinates.

## Complete supports within a subgroup

For fixed H, its nonkernel x-fibers are disjoint. In U_(H,P), precisely two such fibers are present in full; each other fiber contains at most one of the five extra points. Since ell>5, the full fibers can be recovered from the support itself. If U_(H,P)=U_(H,Q), the two full fibers agree as an unordered pair. Removing them recovers J_P=J_Q, so Q=±P. Hence fixed H supplies exactly ell(ell−1)/2 distinct complete supports.

## Complete supports across different subgroups

Suppose H!=K. The x-fiber D_(H,A) lifts to the disjoint pair of affine cosets (A+H) union (−A+H). Similarly D_(K,B) lifts to two K-cosets. Every H-coset meets every K-coset in exactly one torsion point, since H and K are complementary one-dimensional subspaces of E[ell]. Thus the intersection upstairs has at most four points. It is invariant under negation and contains no O, so its x-image has at most two points.

The unions of two full fibers for H and K therefore intersect in at most8 x-coordinates. If their complete supports U_(H,P),U_(K,Q) were equal, all2ell points in the first full-fiber union would lie in the other full-fiber union plus its five extras. This would imply2ell<=8+5, impossible for ell>14.

There are ell+1 subgroups H. Consequently the exact number of distinct complete supports is

`(ell+1)*ell*(ell−1)/2 = ell*n`.

For ell=23 this is24*253=6072, on n264 coordinates. The quintics themselves number only264 globally, or253 per H; their repeated use across subgroups is not being counted as new quintics.

## Scope

This certifies an explicit superlinear number Theta(n^(3/2)) of distinct admissible support sets. It does not certify syndromes on one common affine line, distinct challenge labels, nearby codewords, or far endpoints. In the particular F_1657 fixture,6072 distinct field labels are impossible simply because the field has only1657 elements. No parameter or matrix scan was used for this count.
