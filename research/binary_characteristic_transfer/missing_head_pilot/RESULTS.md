# Missing-head pilot: exact correlated parameters

Target: N=p^7, degree cap p-1, direction X^(p^3-1), and residual

    X^(p^6)+theta1 X^(p^5)+theta2 X^(p^4)+z X^(p^3)-alpha X^p-beta X.

For a four-space locator J=X^(p^4)+A X^(p^3)+B X^(p^2)+C X^p+EX, right division gives residual J^(p^2)+tJ^p+vJ, with

    t=theta1-A^(p^2),
    v=theta2-B^(p^2)-t A^p.

The missing X^(p^2) coefficient is the affine linear constraint

    (C^p-B A^p) theta1+B theta2
      +E^(p^2)-A^(p^2)C^p-B^(p^2+1)+B A^(p^2+p)=0.

Thus grouping locators by this line gives an exhaustive check of correlated heads with at least one head outside the locator coefficient field. Distinct affine lines cannot share a point outside that coefficient field. Two independent extension heads give no solution (the three coefficient equations would force B=C=E=0). Heads both in the coefficient field are not screened here.

## Exact p=2 results

`p2.py` enumerates all 11,811 four-subspaces of F_128, using unique reduced-row-echelon bases and additive-locator recursion. Every missing-head constraint is nonzero. There are 127 lines with 15 distinct labels, 889 with two, and 8,128 with one. `verify_pencils.py/json` checks that every maximal group is exactly the 15 four-spaces containing one common three-space. Their union is the entire domain and their pairwise intersections equal the common three-space.

`p2_nonfield.py` instead uses the seven-dimensional polynomial-basis hyperplane in F_256 (modulus X^8+X^4+X^3+X+1). It enumerates the same number of subspaces. There are two lines with 16 labels, 60 with 15, one with four, 20 with three, 515 with two, and 9,784 with one; one locator has inconsistent missing-head constraint. There are no universal constraints. The best group consists of a 15-member constant-B pencil and one extra locator with a different B. This is a genuine non-field effect, not an asymptotic construction.

`check_best.py/json` reconstructs both coefficient components of all residuals for one best head line, evaluates on all 128 domain points, and verifies 16 distinct labels, degree-at-most-one witnesses, and exactly 15 agreements each. Theta can be any element outside F_256. No assertion about common agreement or first-order proximity at this small p is inferred solely from this pilot.

The main enumerations take about 0.07 and 0.13 seconds respectively on the local Python environment. Their arithmetic is elementary binary polynomial-field arithmetic; no large matrix or extension-parameter grid is formed. The receipt checks are internal exact checks, not yet an independent implementation audit.

The observed larger groups are support pencils plus isolated exceptions. A positive growing-characteristic result still requires an explicit family whose distinct-label population grows faster than N^(6/5); the small pilot does not provide one.

## Exhaustive characteristic-three comparison

`p3.cpp` enumerates all 925,771 four-subspaces of F_(3^7), using modulus X^7+X^2+2 and generator -X. The correlated-head census has 856,912 lines: 68,859 with two distinct labels and 788,053 with one. There are no universal or inconsistent constraints. In particular, no 40-member analogue of the characteristic-two pencils appears.

The bounded run completed in 0.91 seconds with sampled peak RSS 33.4 MB (rusage peak 35.1 MB), below the authorized 60 seconds/384 MiB. See `p3.resources.json`. Compilation used the installed MacOSX15.4 SDK because the default SDK/linker combination rejected newer architecture tags; this did not change source arithmetic.

`verify_p3.py` independently checks all six locators saved in the three representative maximal groups, using polynomial convolution rather than logarithm tables. Each has exactly 81 roots, its head constraint normalizes correctly, and the two labels on each line are distinct. This is a selected-output replay, not a second exhaustive implementation. See `p3.selected_verified.json`.

The algebra agent independently identifies why the observed constant-coefficient pencil is characteristic-two-specific: a sparse three-space locator J=X^(p^3)+B X^p+CX splitting inside F_(p^7), together with Q composed with J = X^(p^7)-X, forces a coefficient equation -2 C^(p^5+p^4+p^2+p)=0. Since C is nonzero, this mechanism requires characteristic two. This does not exclude other odd-characteristic nonconstant-coefficient families. No F_(3^8) expansion was launched after this decisive comparison.
