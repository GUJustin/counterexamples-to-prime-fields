# Entropy-threshold compiler and below-Elias comparison: independent addendum

2026-09-18. Mathematical compiler and comparison **PASS**. At the time of this read, `prime_random_fiber_log_gap.tex` still contained the old large-C concentration proof. Thus this receipt certifies the replacement's mathematics, not an unread future file revision.

## Exact profile survives the new coverage proof

The new seed/pair theorem changes only how G is obtained. For n=(s+1)m, J−1=(r−2)m+w,0≤w<m, R the reserved-fiber locator, and Y=X^m, set

    f=R(Y^r−b^r)/(Y−b), g=−R/(Y−b).

The pole is root-free. The first source is monic of degree A=J+m−1; subtracting any codeword of degree<J is nonzero of degree A. The g agreement numerator R+(Y−b)h is nonzero since deg R<m and, if h≠0, deg((Y−b)h)≥m. Its degree is at most A. These give the two upper bounds independently, without using coverage.

Interpolate the two quotient-variable sources on r−1 tags of G by degree≤r−2 polynomials, substitute Y and multiply R. Both witnesses then agree on the same r−1 full fibers plus the w reserved points. Therefore both individual agreements and ordinary common agreement are exactly A.

For each λ≠0 product coverage gives S⊂G,|S|=r,V_S(b)=−λ. The quotient witness has degree≤J−1 and residual R V_S(Y)/(Y−b), with exactly T=J+2m−1 canonical agreements. Since A<T, λ0 is far and the projective direction g is far. For t≠1,

    (1−t)f+tg=(1−t)(f+[t/(1−t)]g).

Nonzero scalar multiplication preserves distance to a linear code. Thus exactly the p−2 parameters t∉{0,1} give near normalized affine mixtures, while both endpoints have exact agreement A. The statement concerns existence of near witnesses, not uniqueness or exact maximum agreement of interior words.

## Exact dimension and s can both be retained

Fix C>1/h(ρ), and first choose a constant completion count t with positive exponent slack as in the independent seed/pair proof. If the theorem retains s=ceil(C log p) exactly, use seed size s0=s−2t, not s. Define J=floor(ρ(s+1)m), r=floor((J−1)/m)+2, and seedcard r0=r−t. Then r0=ρs0+O(1) and s0=C log p+O(1), so the entropy proof still applies. Every completed representation has exactly r elements from exactly s distinct tags. This removes any rounding/circularity concern.

## Elias comparison with signs explicit

For fixed ρ and p→∞, the q-ary entropy inverse at q=p gives Elias decoding radius

    R_E=1−ρ−h(ρ)/log p+o(1/log p).

Equivalently its agreement threshold is ρ+h(ρ)/log p+o(1/log p). Here

    T/n=ρ+2/(C log p)+o(1/log p).

Hence1/h(ρ)<C<2/h(ρ) places T/n strictly above the Elias AGREEMENT boundary, or the decoding radius1−T/n strictly below the Elias radius. C>1/h(ρ) is the seed-coverage entropy condition. The exact source-to-near gap is1/(C log p)+o(1/log p). This is a genuine below-Elias radius conclusion, but still below the fixed-rate DKT first-order AGREEMENT curve because the latter exceedsρ by a fixed positive amount.

## What KKH already proves

The actual Krachun–Kazanin–Haboeck primary text explicitly says immediately after Theorem1 that choosing β sufficiently large produces parameters below the Elias radius. Theorem1 has fixed rate, polynomial PRIME alphabet p=Θ(n^β), inverse-logarithmic gaps, and arbitrarily large polynomial exceptional counts. AppendixA already supplies the quotient-variable degree ledger. Primary: https://eprint.iacr.org/2026/782 ; cached `sources/actual_list_literature/kkh2026_782.txt`, lines118–149 and AppendixA.

Therefore the new construction must NOT be promoted as the first prime-alphabet below-Elias inverse-logarithmic counterexample. Nor does prime alphabet alone distinguish it from KKH. The potentially sharper profile is the conjunction of ALL nonzero pencil labels, TWO individually far endpoints, and exact individual/common agreement, on a chosen union of cosets rather than their subgroup domain. KKH's stated Proposition4 gives at least p/(2n) labels and only a far direction. The prior proof audit did not find the stronger endpoint conclusion implicit in CS/DG. This is a precise comparison of certified statements, not a priority claim.

CS's all-affine-near entropy-window corollary does not supply this below-Elias guarantee: its agreement excess has coefficient below h(ρ), whereas the new window has2/C>h(ρ). Its first source is also near. These differences are both worth stating, while retaining the known KKH below-Elias precedent.

## Stronger exact interior agreement (subsequent root observation: PASS)

The earlier limitation to certified lower agreement is unnecessary. For ANY polynomial h of degree<J and ANY λ,

    (Y−b)(f+λg−h)
       =R(Y^r−b^r−λ)−(Y−b)h.

The first summand is monic of degree w+rm=T. The second has degree at most m+J−1=A<T. Hence the numerator is a nonzero polynomial of exact degree T. The denominator is nowhere zero on D, so every witness has at most T agreements. For λ≠0 the product witnesses attain T, proving

    agr_J(f+λg)=T  for every λ≠0.

Together with the separate source proof, the complete projective agreement profile is exactly A at the two source points and exactly T at every other projective point. In normalized affine coordinates, t=0,1 have agreement A and all p−2 remaining parameters have agreement T. This strengthens the earlier 'at least T' language throughout the compiler family, including the finite fixtures; it does not assert uniqueness of a maximizing witness.

## Final actual-source acknowledgment

The updated `fixed_weight_completion.tex` and `prime_random_fiber_log_gap.tex` were read in full on 2026-09-18 after integration. **PASS.** The finite lemma includes the distinct-sampling conditioning and depleted-population correction; its entropy corollary uses a fixed completion count, with a valid geometric exponent bound. The prime theorem uses positive population/bias exponents, includes all completion pairs within its prescribed final s, preserves exact J through Euclidean division, proves exact interior agreement by the monic degree-T residual, and has the correct Elias-entropy sign. No mathematical correction is required for these sources. This receipt does not certify a later edit or typesetting/build output.

SHA256 of reviewed sources:

- `fixed_weight_completion.tex`: `421548ac04ffe17ce1db5481c18a69e6a9d07c74ce1919cf4792a8c81c8814d3`
- `prime_random_fiber_log_gap.tex`: `5b5cc10df2aa48ee766e1e38b4cf0a1c9809e2a70e1ed88fb498745c923b6685`

Final finite48 insertion and certificate-path audit: PASS, with coverage receipts now independently completed. Current `prime_random_fiber_log_gap.tex` SHA256: `9e43f03cc96e1fd2881b68e7da9abc60c41c6944f5ffd8c449396538af3854cd`. The earlier source hash is retained as historical evidence of the prior reviewed revision.

## Final integration check by the coordinating audit

The finite certificate and separately audited fixed-m corollary are now included.
All finite coverage counts were replayed by direct field multiplication, independently of discrete logarithms. The final mathematical source was read, the complete PDF rebuilt, and the new theorem/certificate pages visually checked. Final source hashes:

- `fixed_weight_completion.tex`: `421548ac04ffe17ce1db5481c18a69e6a9d07c74ce1919cf4792a8c81c8814d3`
- `fixed_m_corollary.tex`: `1d24ebdf18a27846b2e7037f2626d09629b0745a898593168afee09e9e6de520`
- `prime_random_fiber_log_gap.tex`: `4a65ab71be8de8037203c62fce4e50065cea39ee09964cd5e2217df55018dadc`
