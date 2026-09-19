# Torsion lifts with disjoint extras: a linear label bound

Independent audit of the root argument: PASS. This closes the specified3/7 torsion-multiple support family, independently of the proposed kappa labels. It is not a bound for arbitrary moving quintics.

Use ell>14 prime, n=(ell^2−1)/2, k=n−4ell+1, T=n−2ell−5, with the full rational ell-torsion x-domain and strict RS dimension k. Let the parity-check map be Hcal, with redundancy r=4ell−1. Every set of at most r parity columns is independent.

Consider a genuine two-dimensional syndrome space L for a received affine line. Assume at least one of its endpoints has nearest agreement strictly less than T. We count distinct projective syndrome points in L that have an error representative supported in one of

`U_(H,P)=D_(H,3P) union D_(H,7P) union {x(jP):j=1,2,4,5,6}`,

where H is an order-ell subgroup and P is outside H. On a genuine two-dimensional affine syndrome line, distinct affine parameters give distinct projective syndrome points, so the same upper bound applies to affine exceptional labels.

## Banks with a common base and disjoint extras

Fix H and one nonzero quotient class q in E[ell]/H, modulo sign. Choose a sign representative q. Its ell lifts P=P0+T, T in H, parametrize precisely the ell support descriptions in this bank; changing the representative sign does not change the bank.

The two full fibers form one fixed base B_q of size2ell, because their tags are the classes±3q and±7q. Every lift has five extras J_P outside B_q.

The extra sets for different lifts are disjoint. Indeed an equality x(jP)=x(j'P') implies jq=±j'q. The multipliers1,2,4,5,6 are distinct up to sign modulo ell, so j=j'. The negative sign is then impossible because q is nonzero and ell is odd. Thus jP=jP', whence P=P'. This also verifies that no hidden choice of sign causes an overlap.

## Three distinct labels are impossible in one bank

First, one fixed support U cannot contain error representatives for two distinct projective points of L: their syndromes would span L inside the support space S_U. Every word on the received line would then have an error representative on at most2ell+5 coordinates, and hence agreement at least T, contradicting the far endpoint. Thus three distinct labels require three distinct lifts.

Suppose three such labels have representatives e1,e2,e3 on B_q union J1,J2,J3. Their nonzero syndromes lie in L and are pairwise projectively distinct. Consequently they have a linear dependence

`a1 Hcal(e1)+a2 Hcal(e2)+a3 Hcal(e3)=0`

with all ai nonzero. The combined error is supported on a union of size at most2ell+15. Since

`2ell+15 <= 4ell−1 = r`

for ell>14, parity-check injectivity on that union forces
`a1e1+a2e2+a3e3=0` as vectors. Restricting to each disjoint Ji forces the corresponding ei to vanish there. All three syndromes therefore lie in S_(B_q). Two distinct ones span L, so every word on the line has an error representative on at most2ell coordinates. Its agreement is at least n−2ell=T+5, again contradicting the far endpoint.

Thus every fixed(H,±q) bank contributes at most two distinct labels. The argument permits arbitrary values and partial support inside all fibers and extras; it does not assume the canonical quotient witnesses, nonzero errors on every extra point, or a formula for the labels.

## Total count and finite instance

There are ell+1 subgroups and (ell−1)/2 nonzero signed quotient classes per subgroup. Hence there are exactly n banks, and the union of their qualifying label sets has size at most

`2n = ell^2−1`.

Labels represented in multiple banks only decrease the union count. At ell23 this is at most528 distinct labels, despite the6072 distinct complete support sets. The count thus cannot provide a superlinear-label counterexample with a far endpoint.

The statement assumes a genuine two-dimensional syndrome line. If an affine received line has syndrome span of dimension at most one, all its nonzero syndromes are scalar multiples and have equal nearest agreement. A far endpoint then rules out all nonzero near syndromes; at most the single zero-syndrome parameter can remain. This degenerate case does not evade the linear conclusion.

The bound does not apply to unrelated quintics, supports with overlapping moving extras that do not admit this bank partition, changed code parameters invalidating the short-union injectivity, or lines without a far endpoint. It excludes the specific torsion-multiple family as a superlinear-label mechanism; it does not exclude a common pencil with only linearly many useful parameters.
