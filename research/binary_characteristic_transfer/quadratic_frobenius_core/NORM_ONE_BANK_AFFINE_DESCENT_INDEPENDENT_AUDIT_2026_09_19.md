# Independent audit: three-point norm-bank affine descent

September 19, 2026. **PASS.** Independently checked the final proof and replayed the finite checker. The theorem applies to all prime powers Q, including characteristics two and three; the separate evaluation-domain construction retains its odd-characteristic restriction.

## Uniform geometry

The parameterization p(d)=(-d^(Q²)/d,-d^Q/d), modulo F_Q*, is correct and bijective onto the bank. Its Moore determinant detects exactly F_Q-independence of three parameters. For a triple that is not E-collinear, uniqueness of E-barycentric coordinates and the requirement that those coordinates lie in F_Q force every bank point in its affine F_Q-plane to be a vertex. Ratios of two nonzero barycentric coordinates would otherwise force two basis parameters to be F_Q-proportional.

When the intersection is E-collinear, its parameters lie in an F_Q-subspace of dimension two by the same Moore criterion. The first-coordinate map on this projective line is a nonconstant Möbius function with a pole of exact degree three. Projecting any affine F_Q-plane to E yields a subspace of dimension at most two, hence a nontrivial trace equation. The three coefficient-conjugate Möbius summands have distinct simple poles and nonzero residues. Their sum cannot vanish identically, including in characteristic three. Clearing the norm denominator gives a nonzero homogeneous cubic. The denominator has no F_Q-projective zero, and the homogeneous root count includes infinity. Thus at most three bank points survive. A Moore-independent triple proves sharpness.

The optional earlier six-point argument is also consistent: anisotropy makes the binary cubic leading form irreducible over F_Q, hence the affine norm cubic irreducible over that field. An F_Q-defined quadratic cannot share a geometric component with it, because the normalized common divisor descends under Frobenius. The sharp proof does not rely on this auxiliary argument.

## Descent interface and limitations

For finite E and K, writing k=E∩K, the compositum/intersection degree formulas establish linear disjointness over k. Consequently any k-independent vectors in K^N remain E-independent, by expanding relation coefficients in a k-basis of E. This proves dim_k(W∩K^N)≤dim_E W even when W is an arbitrary E-linear subspace of a larger ambient field. No assumption that an embedding matrix is defined over E or K is necessary.

After subtracting one selected image, an injective E-linear embedding of the coefficient pair therefore pulls all selected differences into a k-space of dimension at most two. If k⊂F_Q, its F_Q-span is at most a plane, so the sharp intersection theorem gives at most three selected witnesses. Arbitrary common translation is harmless. The valuation condition v_3(m)≤v_3(r) is equivalent to gcd(3r,m) dividing r.

The rational-function extension is valid: a k-basis of E remains independent over K(X) by clearing denominators and comparing coefficients. Nonconstant phi ensures the common map (a,b)↦M(a phi²+b) is injective in every characteristic, including two. Thus arbitrary common rational pullbacks, common nonzero multipliers, and common translations are covered. Parameter-dependent transformations, nonlinear coefficient maps, traces, changed characteristic, and reconstruction of a different witness bank are not covered. No preservation of distance or agreement is inferred from coefficient descent alone.

## Replay

The standard-library checker passed for Q=3,5,7, covering respectively 286, 4495, and 29260 triple spans. All tested bank triples are F_Q-affinely independent; each resulting plane meets the bank in exactly three points. Together with explicit checking of collinear spans, this covers every possible plane intersection of size greater than three in those fixtures. The uniform assertion rests on the proof, not these examples.

This is a sharp obstruction to transferring a growing subset of this particular coefficient bank. It is not a new proximity-gap lower bound or a certified benchmark improvement.

## Audited artifact SHA-256

- `NORM_ONE_BANK_THREE_POINT_AFFINE_DESCENT_2026_09_19.md`: `d471364e5e83b56e9b6957f8988a72935c31ba2ca979addee6e40ff27013c630`
- `verify_norm_bank_affine_planes.py`: `81b584ffb6d5489c90f1d4c0b40c325e71471e52b5e8d233b9bd0dba9766efe1`
- `verify_norm_bank_affine_planes.json`: `865825ee5511d14617c536c96082f8f8e01890311546dde44d1ee679961ccdb9`
