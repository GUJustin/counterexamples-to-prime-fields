# Independent audit: pure-character Wronskian closure

Verdict: PASS. Read the entire `PURE_CHARACTER_WRONSKIAN_CLOSURE.md` and the independence/ideal proof in `research/power_family_mca/PROOF.md`, rather than treating the latter as a black-box theorem with automatically inherited hypotheses. No scans or manuscript edits.

## Paired-root reduction

For h>=3 the elementary bounds A<=h and A<=2r are valid. In a branch with two distinct roots, the sum K=−b/a is nonzero. With z=x/(K−x), equality of hth powers gives z^h=1, and substitution gives exactly [c(1+z)^2−aK²z](1+z)^(h−2)=K^h. Distinct paired roots yield distinct z-values, and the map x→z is injective away from K. Zero and −1 cannot be relevant z-values. Thus 2d2<=k and A<=r+k/2 without any hidden assumption that all branches are double or all gcd roots arise from branches.

## Independence and coordinate changes

The three homogeneous forms have pairwise disjoint supports: F0 only at infinity, F1 only at zero, and F2 at −1 and at up to two roots of q, neither zero, infinity nor −1. The assumptions c!=0 and aK²!=0 are exactly what guarantee this. A double root of q causes no problem. There are at most five root points.

Over an algebraic closure one may choose the new infinity outside these points and the common roots. Homogeneous pullback keeps the three forms degree h, their differences as the same homogeneous linear combinations, and their degree-four monomials degree exactly 4h. It preserves valuations and rational degrees. This coordinate change need not be defined over the original finite field, which is harmless for a geometric common-root bound.

Distinct degree-four monomials have nonconstant ratio with degree at least h−2: a changed F1 exponent gives a nonzero valuation of magnitude at least h at its unique root; otherwise the F2 exponent changes and its −1 valuation has magnitude at least h−2. These observations replace the archived common-power multiplicative-independence hypothesis; that theorem is not being applied outside its stated form.

In a minimal relation of q<=15 terms, q−1 terms have a nonzero ordinary Wronskian. The finite-characteristic justification is degrees <=4h<p: row reduction to distinct leading degrees makes its leading coefficient a nonzero Vandermonde product modulo p. No characteristic-zero assertion is silently reused. Omitting a minimum-order term at each root and comparing divisor degree gives

 4h−deg(gcd of relation terms)<=(|S|−1)binom(q−1,2)<=364.

Every monomial ratio has degree at most the left side but at least h−2. Thus h>=367 gives the required strict contradiction. This remains valid for a two-term relation (already ruled out by nonconstant ratios).

## Ideal Wronskian ledger

The degree-four component of the two-linear-generator homogeneous ideal has codimension one among 15 monomials, hence dimension 14. Independence makes evaluation injective. The ordinary Wronskian is nonzero under the same p>4h guard and has degree at most 56h−91.

The codimension-one filtration estimate loses at most the maximum monomial valuation at a point. Summing all monomial valuations over S gives 60h. Since supports of the forms are disjoint, the sum of the maximum valuations is exactly 4*(3h)=12h. Differentiation loses at most 91 at each of at most five points, yielding at least 48h−455 zeros on S. Local basis changes are constant invertible matrices, so these valuation bounds legitimately concern one Wronskian.

The two evaluated generators have no common root on S. Their degree-k gcd divides every evaluated ideal element, so the identity Wr(Tf1,...,Tf14)=T^14 Wr(f1,...,f14) supplies 14k additional zeros off S. Thus

 14k<=8h+364,  or k<=4h/7+26.

No repeated-root or projective-infinity multiplicity is lost. The original Z^h−1 is squarefree, since h<p; after the chosen coordinate change all its relevant common roots are finite.

## Constants and full ratio range

Outside 3/8<sigma=r/h<2/3, the elementary bounds already imply A<=sqrt(3hr/2). Inside that interval, n=hr>(3/8)h² and n divides p−1, so p>n>4h for h>=367. The finite-characteristic hypothesis is automatic exactly where the Wronskian estimate is used.

The resulting A<=r+2h/7+13 is below sqrt(3hr/2), because the concave function sqrt(3sigma/2)−sigma−2/7 has endpoint values 5/56 and 1/21. Its minimum on the closed interval is 1/21. The slack h/21−13 is positive at h=367 and increases thereafter. Both boundary ratios themselves are covered by the elementary bounds.

For h<367, the ordinary residual degree bounds A by 366 when h>=3; for h=1,2 its degree is at most two and it cannot be the zero polynomial under abc!=0. Thus the bounded-h exception cannot produce growing agreement either. The primary low-rate curve in Eq. (31) of `tmp/eprint-2056/paper.txt` is strictly larger than sqrt(rho/2), so at dimension three the proved bound is below its leading threshold sqrt(3n/2).

## Scope

This closes precisely x^h against quadratics with all three coefficients nonzero on mu_n, with h|n|p−1, for the proposed growing-agreement target. The finite-characteristic algebraic gcd lemma itself has the separately stated guard p>4h. It says nothing about arbitrary exponents not dividing the domain order, received words outside this family, or quadratic banks in general. The local archived mechanism is correctly acknowledged; no new literature-priority claim is implied.
