# Integrated norm-one shortening audit

PASS, 2026-09-19. Actual revised norm_one_direct_list.tex and paper.tex introductory comparison inspected. No manuscript edits.

## Universal shortening lemma

For any nonempty list, T≤N and N≥3. Anchoring a chosen agreement point leaves T−1 element sets with pairwise intersections at most one on N−1 coordinates. Cauchy–Schwarz gives the displayed local Johnson count; summing r_x gives precisely U(N,T). If T>N the list is empty and the bound is trivial, so the proof need only treat the nonempty case. No characteristic, prime-alphabet, or finite-field assumption enters this lemma. The derivative has the stated sign (up to a positive factor) for N≥3, hence the real-threshold monotonicity used later is valid.

## Finite constants and profile

The full norm-one list classification remains internally consistent: the even bank has N/2 witnesses with 2p+2 matches; the squared-linear bank has 2L witnesses with p+1 matches; all other quadratics have at most four. The semilinear identity, quartic test and sign recovery correctly distinguish these banks. The threshold ceil(19p/10) lies strictly above p+1 and below 2p+2 for p≥53, so the displayed list there is exactly N/2.

Substituting N=2(p²+p+1), t=19p/10 into U≤4N/3 gives exactly 209p³−10870p²+1575p+1500≥0 after multiplication by a positive constant. The stated expansion at p=53 is correct and all coefficients are positive. Independent rational spot checks at p=53,59,61,97 also satisfy the integer-threshold bound. The first-order estimates √(3N/2)<7p/4 and (3N/8)^(1/4)<√p hold for p≥53; √p>20/3 then gives the required strict gap below T. The upper Johnson comparison T<2p<√(2N) is valid. Thus the advertised finite ratio at most 8/3 between universal maximum and exhibited N/2 list is correct.

For the entire integer band beginning at ceil(√3 p), substitution into U≤9N/4 gives the exact radical polynomial in the proof. At p≥53, √3(p−26)−38≥27√3−38>0 and the remaining linear and constant terms are positive. All thresholds in the band remain in the exact N/2 classification range. The manuscript correctly warns that the whole finite band need not lie between first order and Johnson; this placement is only claimed eventually for each fixed c in (√3,2).

## General range and scope

At T=cp+O(1), U/N=2/(c²−2)+O_c(1/p), with positive denominator eventually for c>√2. The same lower bank remains exactly N/2 for each fixed c<2. Thus the upper-to-exhibited ratio tends to 4/(c²−2), between two and four for √3<c<2. This is a limiting comparison, not an assertion of optimal dependence on c or a finite uniform onset independent of c. The upper bound applies to every domain over every field of the specified length, while the lower example requires the stated extension-field norm-one domain.

The intro accurately describes a codewide ordinary-list comparison, not an exceptional-label bound, fixed-rate result, or prime-alphabet assertion. Its finite 4N/3 and 9N/4 statements and asymptotic ratio language agree with the theorem. Research interpolation certificates may remain archived; none is needed for the new upper proof.

## Frozen hashes

- `research/binary_characteristic_transfer/quadratic_frobenius_core/norm_one_direct_list.tex`: `5ae6570f715de3f18019d2cac265af6bb2d4a59a81bce9487e7215b00821f269`
- `paper.tex`: `a61806c33064a73cd03e1df6f825788501a15fa41b7d0f099a540b8fb44912cd`
