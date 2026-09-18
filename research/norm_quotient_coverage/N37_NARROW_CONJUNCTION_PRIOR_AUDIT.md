# N37 narrow conjunction: strengthened prior comparison

2026-09-18. Bounded audit of primary arguments and obvious transformations. **Candidate distinction, not a priority claim:** prime-field RS codes at fixed rate, polynomial alphabet size, strictly below-Elias radius, inverse-logarithmic gaps, and an exact projective distance profile with two far points and every other point near.

## Important correction: KKH's mechanism already gives two far endpoints

The strongest comparison should not rely on the fact that KKH's headline theorem mentions only one far direction. Its Appendix A quotient construction can immediately be shifted to obtain both endpoints far.

Write Y=X^m and take its root-free pole b outside the tag image. At strict code dimension J=(r−2)m+1, start with

    f0=Y^r/(Y−b), g=−1/(Y−b).

Shift the affine origin to

    f=f0+b^r g=(Y^r−b^r)/(Y−b).

This f is monic degree A=(r−1)m. For any degree<J codeword h, f−h is nonzero degree A, while the g residual numerator1+(Y−b)h is nonzero degree≤A. Interpolation in Y on r−1 domain tags attains A simultaneously. Thus both endpoint agreements and ordinary common agreement are exactly A.

If S is an r-subset of domain tags, its original represented parameter P_S(b) becomes λ=P_S(b)−b^r=−V_S(b), which is nonzero because b is outside the tag set. The shift is injective on the label set, so no exceptional count is lost. The quotient witness has exactly T=rm agreements, and the cleared residual is monic degree T for every codeword, giving exact maximum agreement T for every represented label. The source gap is m/n; capacity margin is (2m−1)/n, with ratio m/(2m−1)→1/2. These are exactly the endpoint scales relevant to N37.

Therefore KKH already yields polynomial prime alphabets, fixed rate, below-Elias inverse-logarithmic gaps AND two far endpoints after a simple origin shift. The difference left by its actual proved bounds is coverage: Theorem1 gives a large polynomial number of labels and Proposition4 gives at least p/(2n), not all p−1 nonzero labels. An invertible parameter change preserves the number of nearby projective points; it cannot upgrade this guaranteed count to p−1. The theorem may have more labels than its lower bound, but its proof does not establish saturation.

Primary: Krachun–Kazanin–Haboeck, https://eprint.iacr.org/2026/782 , AppendixA quotient construction and Propositions3–4; Theorem1's following paragraph explicitly notes below-Elias instances for sufficiently large β. This correction supersedes any earlier suggestion that two-farness alone distinguishes N37 from the KKH mechanism.

## Why CS and DG do not give the full conjunction immediately

CS Corollary1 proves all affine labels near with a prescribed far direction, but its entropy window places the radius above the q-ary Elias limit. Its center is near. Its projective line has one far point, so reparametrization cannot make two. The same primary paper's quotient/list conversion can be origin-shifted only when the requisite polynomial degree structure is supplied; its random-center theorem does not supply that structure. Restricting its random center to be far is not justified by the unconditional expectation.

DG Theorem2.5 fixes a deep-hole center and chooses a direction from all ambient projective directions. There is no formula or degree restriction on that direction. The explicit direction-count audit shows that restricting its pigeonhole argument to far directions leaves only one aggregate near incidence guaranteed, not almost-all coverage. Thus neither the opposite orientation nor a scalar change proves the full conjunction.

A direct sum of differently oriented one-far examples does not by itself solve this: a direct-sum code is not the same RS code, the source/near distance inequalities need fresh estimates, and exact threshold equality is not preserved automatically. No such transformation was found in the inspected proofs.

Primaries: CS https://eprint.iacr.org/2025/2046 , Theorems1–3 and Corollary1; DG https://eprint.iacr.org/2025/2010 , Theorem2.5 and its proof. Local PDFs/texts are cached in `tmp/cs_novelty_audit/`.

## Active paired completion baseline

The active paired-domain construction already gives all nonzero labels and a two-far corollary below Elias, but its length constraint is n≈(2k+4/5)log p/h(ρ), with k log log p=o(log p). It therefore has n=o((log p)^2/log log p), not polynomial alphabet in n. To force p polynomial in n would require k≈n/log n, outside the proved hypothesis. This is a parameter failure of that theorem, not a universal barrier to adapting its method.

The new fixed-cardinality completion proof is itself a refinement of this classical seed-energy/random-translate mechanism. N37 should be described as assembling/refining known methods to saturate the label image in the polynomial-prime-alphabet quotient setting, not as inventing the two-far pattern or completion principle.

## Defensible claim and remaining uncertainty

A defensible theorem-level claim is the precise conjunction of polynomial prime alphabet, fixed rate, below-Elias inverse-logarithmic margins, exact source gap asymptotic to half the capacity margin, and ALL p−2 normalized interior affine mixtures at one exact distance. Among the primary statements and their immediate algebraic consequences checked here, none establishes that entire conjunction. KKH supplies every listed item except proved all-interior saturation; CS supplies all-label coverage in the other entropy regime and with a near center.

This does not establish historical priority. The work uses standard ingredients, and the relevant completion argument already appears in the project's paired construction. A bounded web search for later all-but-two RS statements did not yield a verified additional primary theorem; absence of such a search result is not evidence of novelty. Stronger claims require a wider expert literature check. Nor does the conjunction establish first-order DKT tightness: at fixed rate its agreement still tends to the code rate.
