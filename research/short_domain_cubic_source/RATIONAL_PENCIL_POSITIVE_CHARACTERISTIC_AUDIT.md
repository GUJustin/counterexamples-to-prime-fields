# Independent audit: positive-characteristic quadratic/linear pencil

Verdict: PASS under the stated hypotheses p>2 and p>6D, algebraically closed constants during the proof, and coprime numerator/denominator of exact u-degrees two and one. No changes to the source note are required.

Audited source: RATIONAL_PENCIL_POSITIVE_CHARACTERISTIC.md. Primary theorem independently reopened: Pasten–Wang, *Extensions of Büchi's Higher Powers Problem to Positive Characteristic*, author PDF https://people.math.harvard.edu/~hpasten/preprints/PWposIMRN.pdf, Theorem 3, printed pp.4–5.

1. The primary theorem permits arbitrary distinct constant labels. For degree two and genus zero its strict threshold M>19 gives twenty. It removes constant polynomial factors first; the remaining factors must be separable and outside K^p[C]. The note correctly checks these extra assumptions rather than using the unrelated consecutive-label theorem.

2. Four distinct labels yield four distinct sections. A candidate denominator cannot vanish identically at a section, since numerator and denominator are coprime. The cross-difference argument proves rank four: a second kernel vector gives a degree-at-most-three polynomial vanishing at four distinct K-elements, hence zero. Coprimality and degree caps force proportionality, including kernel vectors with a vanishing numerator or denominator. Maximal minors therefore produce a nonzero representative with the claimed columnwise bounds (2D,3D,4D,3D,4D).

3. The three homogeneous coefficients of the normalized discriminant have polynomial representatives of degree at most 6D. Their projective height is at most 6D, even with a common polynomial factor: removing that factor only decreases the height bound. For monic factors, local Gauss valuation is additive, and each local height contribution is nonnegative because the leading coefficient is one. Thus every factor has height less than p. A nonconstant monic factor in K^p[C] has a coefficient which is a nonconstant p-th power, whose rational-function height is at least p. The factor height bounds the height of each coefficient. This excludes exactly the Frobenius factors prohibited by the primary theorem.

4. All irreducible factors have degree at most two; p>2 makes them separable. If the discriminant has nonconstant coefficients, at least one remaining factor exists after removing constant factors. The theorem forces every such factor to have multiplicity two. Degree two then forces a single nonconstant linear factor squared, leaving no constant factor of positive degree. Thus the handling of constant factors introduces no gap.

5. The claimed discriminant-in-C formula is correct and is nonzero: its parenthesized term is d1²*N(−d0/d1), nonzero by coprimality. Therefore the squared-polynomial alternative is impossible. Constant coefficients are the only remaining outcome.

6. The quadratic formula puts every section on a rational affine line with scalar parameter in the algebraically closed constant field. Two distinct degree-at-most-D polynomial sections generate the same line, with polynomial generators of degree at most D. Over a nonclosed base field choose two base-field sections; every other base-field section has a base-field affine scalar, as seen by comparing any nonzero coefficient of their polynomial difference. Extending constants therefore does not weaken the claimed prime-field consequence.

7. Fewer than twenty labels supply at most 38 sections. Otherwise the affine-line agreement count gives L(a−D)≤n. The resulting bound max(38,floor(1/eta)) at surplus eta*n is valid for every received word. D=0 causes no exception because p>2 is separately assumed.

This audit confirms a restriction on a particular rational-pencil class. It does not establish a new lower bound, a general rational-fibration classification, or a bound for every Reed–Solomon list.
