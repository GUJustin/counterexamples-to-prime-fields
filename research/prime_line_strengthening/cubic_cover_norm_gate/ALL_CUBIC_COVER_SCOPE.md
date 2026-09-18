# Closing the double-plus-simple denominator case

Work in characteristic zero. The same local arguments hold in sufficiently large characteristic with the indicated tame expansions. Fibers above the fourteen selected finite base nodes are assumed separable, with all three distinct preimages in the domain. The extra linear denominator is proper.

The existing cubic pattern proof covers squarefree binary S. A triple root of S is the polynomial-cover case after a source Möbius change, including a pole at infinity. The remaining ramification type of psi above infinity is (2,1). This note closes that type.

## Local singularity bound

An irreducible plane branch with local coordinate orders (2,m), m>0, has delta at least floor(m/2). For odd m this is the usual first characteristic-pair bound (2,m). For even m, subtract powers of the first coordinate to remove the even leading terms from the second: primitivity forces an odd exponent at least m+1, giving delta at least m/2. An infinite sequence of only even terms would contradict primitivity. This argument may be made after a formal change giving the first coordinate exactly t^2.

Two distinct branches of orders (e_1,m_1),(e_2,m_2) have intersection multiplicity at least min(e_1 m_2,e_2 m_1). Delta of their union is the sum of individual deltas plus their intersection multiplicity. We apply these bounds at the image (infinity,infinity); a branch whose second coordinate has no pole is omitted, equivalently assigned zero contribution in the bounds below.

## Uniform computation for original and two-full-fiber residual maps

Write k=3 for the original function v=N/(ell S^3), or k=1 after subtracting the linear interpolant through two full fibers and dividing by their base locator. In the second case the function is M4/(ell S). In both cases the degree is at most 3k+1 before cancellations, and the image of (psi,v) has arithmetic genus at most 2(3k)=6k.

At the double and simple S roots, the baseline pole orders are 2k and k. Let v_1,v_2 be their cancelled orders, capped at these baseline orders. The map is birational: an off-S proper simple pole cannot be a pullback from a degree-three map; at the double S root the proper order 2k+1 is not divisible by two; at the simple root the proper order k+1 would demand order 2k+2 at the double root, exceeding its available order. Subtracting a function of psi and dividing by one preserves the generated function field, so this remains true after full-fiber removal.

If the extra pole is off S, the finite singularity budget is at most

    6k - 2(v_1+v_2)
       - floor((2k-v_1)/2)
       - min(2k-v_1, 2(k-v_2)) <= 3k.

The inequality follows by separating v_1 even and odd, or directly comparing the two terms in the minimum. This allows arbitrary numerator cancellation at S.

If the extra pole is at the double S root, properness leaves order 2k+1 there. The other pole has order k-v_2. The infinity delta is at least k+2(k-v_2), so the finite budget is at most 3k.

If the extra pole is at the simple S root, its order is k+1 and the double-root order is 2k-v_1. Infinity delta is at least floor((2k-v_1)/2)+(2k-v_1). The remaining budget is at most

    3k - floor(v_1/2) <= 3k.

Therefore the original map has at most nine units of finite double-point budget. A double fiber consumes at least one, and a full three-preimage fiber at least three. Thus d+3f<=9. The homogeneous binary-cubic decomposition proving f<=2 uses only coprimality of R,S, not squarefreeness of S, so is unchanged. With two full fibers, the residual k=1 calculation gives d<=3. The already established incidence argument consequently leaves exactly the same f0/f1 patterns.

Together with the squarefree and polynomial cases, the cubic norm matrices therefore exclude proper one-pole augmentation for **every rational cubic cover** of the fixed Paley bank, subject to the required fourteen separable fibers. The same conclusion holds for the fixed archived orbit2 bank, using its own two-pattern incidence classification.

## Orbit2 exact gate

`orbit2_gate.py/json` uses the independently verified F83 reduction in `../quadratic_one_pole_route/orbit2_bank83.json`. The no-full-fiber matrix has rank26; the sole one-full-fiber pattern (triple index2, empty quadruple index4) has rank20. `orbit2_verify.py` rebuilds the entries and uses integer Bareiss determinants. The maximal minors reduce to 38 and 1 modulo83. The unit-specialization argument in PROOF.md gives the corresponding characteristic-zero exclusion.

## Seven-bank classification scope

The archived exhaustive combinatorial enumeration and six geometric exclusions prove that any characteristic-zero seven-cubic bank on fourteen nodes has incidence type orbit2 or orbit7. The orbit7 realization is classified up to the stated transformations and conjugation. The universal max-seven proof needs only that classification, because any eight-bank contains an orbit7 seven-subbank.

That proof does **not** classify all geometric realizations of orbit2 as the one constructed number-field bank. Hence the two successful norm gates exclude the fixed orbit7 and fixed orbit2 constructions, not automatically every possible orbit2 realization. A complete orbit2 realization classification, or a parameter-uniform norm-rank proof, would be required for that stronger conclusion.
