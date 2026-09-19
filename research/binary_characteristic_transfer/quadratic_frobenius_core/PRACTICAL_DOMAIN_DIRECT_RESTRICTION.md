# Direct restriction of the two-block Frobenius sources to practical domains

2026-09-18. Independent algebraic check and root proof review: **PASS**. No scan or manuscript edit. These are restrictions on the unchanged piecewise X^(2p) received sources, not impossibility results for arbitrary words, alternative compilers, or every code on these domains.

## Setup

Let p be odd, E=F_(p^m), and D=D0 disjoint-union D1 a domain of n distinct coordinates. Consider the received pencil

    w_lambda(x)=A_b*x^(2p)+B_b(lambda),  x in D_b, b=0,1,

where A_b are fixed field scalars and B_b(lambda) are affine functions of lambda. The ordinary RS code has strict message dimension k>=3: polynomials of degree less than k. The multiplicative-domain argument permits zero A_b; the norm-circle upper bound requires BOTH A_b nonzero. The original two-block sources with coefficients1,c in E* and a block-indicator direction meet these assumptions.

The finite Johnson agreement used here is sqrt(n*(k-1)). Every assertion is about actual retained coordinates, so arbitrary puncturing and an arbitrary partition into the two blocks are allowed.

## Multiplicative two-power cosets

Assume p≡1 mod4. Let H be a multiplicative subgroup of E* of order s=2^a, and suppose D is any subset of gamma*H, gamma nonzero. On this coset the ratio

    x^(2p)/x²=x^(2(p-1))

has exactly

    r=s/gcd(s,2(p-1))

possible values. Partitioning by this ratio and by the source block gives at most 2r pieces. On each piece w_lambda is a quadratic polynomial A_b*rho*x²+B_b(lambda). Therefore, for EVERY native label lambda,

    agr_D(w_lambda,RS_k) >= ceil(n/(2r)).

Since s divides p^m-1 and p≡1 mod4, the elementary lifting-the-exponent identity gives

    v2(p^m-1)=v2(p-1)+v2(m).

Consequently

    r <= 2^max(v2(m)-1,0).

If n>4r²(k-1), then n/(2r)>sqrt(n*(k-1)). Thus every pencil word already has agreement above Johnson; no two far endpoints at a below-Johnson tested agreement can exist for these sources. This conclusion does not require the whole subgroup to be retained.

## Affine translations: still a bounded number of quadratic pieces

Allow D to be any subset of a+gamma*H. The preceding ratio for x itself need not retain its smaller r-value count. Instead put z=x-a. The ratio z^p/z has

    R=s/gcd(s,p-1) <= 2^v2(m)

values on gamma*H. On a fixed ratio class, z^p=tau*z, and hence

    x^p=a^p+tau*(x-a).

Its square is a quadratic polynomial in x. Refining by the two source blocks again gives

    agr_D(w_lambda,RS_k) >= ceil(n/(2R)).

Thus n>4R²(k-1) rules out far endpoints below Johnson even after arbitrary affine translation and nonzero scaling of the domain. This is a direct calculation for the UNCHANGED formula x^(2p), not merely an invariance assertion. The bound can be weaker than the untranslated one by a factor of two in the number of pieces.

## Named fields

Goldilocks p=2^64-2^32+1 and BabyBear p=2^31-2^27+1 both satisfy p≡1 mod4. For arbitrary two-power subgroup cosets in the indicated extension, the uniform bounds are:

| Field | m | Untranslated r bound | Translated R bound | For k=3, sufficient n cutoff: untranslated / translated |
|---|---:|---:|---:|---:|
| Goldilocks squared | 2 | 1 | 2 | n>8 / n>32 |
| Goldilocks cubed | 3 | 1 | 1 | n>8 / n>8 |
| BabyBear degree four | 4 | 2 | 4 | n>32 / n>128 |
| BabyBear degree five | 5 | 1 | 1 | n>8 / n>8 |

The exact subgroup order may make r or R smaller. These statements concern ordinary polynomial RS and the displayed source functions; they do not assert anything about a full proof system's received words or constraints.

## Norm-one circle cosets and their affine translates

Now let E=F_(p²), and let D be any subset of a norm-circle coset

    x^(p+1)=u,  u in F_p*,

including any subgroup subset or arbitrary puncture of that circle. Then x^p=u/x, so x^(2p)=u²/x². For a quadratic Q, its matches on block b satisfy

    x²*Q(x)-B_b(lambda)*x²-A_b*u²=0.

This polynomial has degree at most four and is nonzero because its constant coefficient is -A_b*u². Under the explicit assumption A_0,A_1 nonzero, every quadratic therefore has at most four matches on either block and at most eight overall:

    agr_D(w_lambda,RS_3) <= 8  for every lambda.

Thus this direct restriction supplies no near labels at a tested agreement T>8. This is a different failure from the multiplicative-coset case: here all words are too far to furnish the desired rich witnesses.

Affine translation does not evade this upper bound. On Norm(x-a)=u, put z=x-a, so

    x^p=a^p+u/z.

Multiplying a matching equation by z² again gives a polynomial of degree at most four whose value at z=0 is -A_b*u², nonzero. Arbitrary affine images of a norm-one circle are of this form. Thus the same eight-match cap holds on them for the unchanged two-block x^(2p) sources.

For larger k, the identical argument gives at most k+1 matches per block, hence at most 2(k+1) overall; the eight-match assertion specifically uses k=3. If a block multiplier is zero, its word is constant and this upper bound can fail completely.

## What a GRS or projective change does and does not alter

A common nonzero coordinate multiplier v sends a received word w to v*w and the code C to v*C. At each coordinate, w=Q if and only if v*w=v*Q. Therefore all individual agreements, threshold lists, and ordinary common agreements are preserved exactly. Changing both code and words into an equivalent GRS instance cannot defeat either obstruction. Multiplying only the received words while keeping ordinary RS fixed is a different source family, not covered by this invariance or by the formulas above.

The standard projective RS change is similarly exact. Let R(z)=(a*z+b)/(c*z+d) have nonzero determinant and no pole on the retained domain. Pull back words and multiply by (c*z+d)^(k-1). A degree-less-than-k polynomial Q transforms to

    (c*z+d)^(k-1)*Q(R(z)),

again of degree less than k; this operation is invertible on the k-dimensional polynomial space. It preserves every coordinate equality. Hence applying this coherent transformation to an already excluded instance cannot create the missing proximity profile. If a pole is discarded, apply the corresponding statement to the remaining punctured instance.

An arbitrary transformation of evaluation nodes followed by reusing the original monomial source formula is not in general this coherent GRS transformation. The affine case was checked directly above; no universal assertion about all such nonlinear redefinitions is made.

## Scope

These calculations close direct puncturing of the specified two-block Frobenius sources onto two-power multiplicative cosets and norm circles, including the stated affine translates. They do not exclude counterexamples with new source formulas, more general directions, a different witness code, or arbitrary short domains. No generic prime-field or extension-field impossibility claim follows.
