# Independent d=5 trace-dual and actual-locator audit

September 18, 2026. **PASS.** The trace-Hodge signs and native label formula are correct. A direct enumeration of three-dimensional subspaces, constructing their actual monic locators, reproduces the full p=3 and p=5 label counts and fiber histograms in `check_d5_theta_one.json`.

## Exact coefficient and label identities

Let E=F_(p^5), let W be a three-dimensional Fp-subspace with basis w1,w2,w3, and let U=W-perp for the trace pairing, with basis x,y. Write

    Pij=x^(p^i)y^(p^j)-x^(p^j)y^(p^i),
    L_W=X^(p^3)+a1 X^(p^2)+a2 X^p+a3 X.

Let Delta_ijk be the indicated three-column minor of the Moore matrix of W, with columns 0,...,4. The Moore rows of W and U are orthogonal because their dot products are Trace(w*x) and Trace(w*y). Complementary minors therefore agree up to a common nonzero scalar c and the complementary-column permutation signs:

    Delta_012= c P34,
    Delta_013=-c P24,
    Delta_023= c P14,
    Delta_123=-c P04.

Expanding the monic subspace-polynomial determinant along its X row gives

    a1=-Delta_013/Delta_012=P24/P34,
    a2= Delta_023/Delta_012=P14/P34,
    a3=-Delta_123/Delta_012=P04/P34.

The denominator is nonzero for an independent pair x,y. Frobenius with indices modulo five gives

    a2^p=P02/P04,
    a1^p=P03/P04.

Using P02 P34-P03 P24+P04 P23=0, the original locator label becomes exactly

    z_W(theta)=theta*a1+a2^p-a1^(p+1)
              =(theta P24-P23)/P34.

In particular the signs in the bounded two-space checker are correct; changing trace-dual basis does not change the label.

## Independent finite-field receipt

The new verifier enumerates RREF three-spaces directly, independently of the existing two-space enumerator. Starting with L_0=X, adjoining an independent vector v uses

    L_(V+Fp*v)=L_V^p-L_V(v)^(p-1)*L_V.

This constructs the actual monic locator, since its roots are exactly the vectors whose L_V value lies in Fp*L_V(v). For every resulting three-space the verifier checks that the polynomial has degree p^3, has nonzero X coefficient, and vanishes on its three basis vectors. Its p-linearity and separability then certify the exact root space. It evaluates z from the locator coefficients first.

Only afterward, the verifier computes W-perp using the independently constructed 5-by-5 trace Gram matrix, checks all six trace orthogonalities, and checks all three Hodge ratios and the Plucker label against the locator result. The Gram matrix is checked nondegenerate also at p=5; Trace(1)=0 there causes no problem.

| p | actual three-spaces and locators checked | native labels | missing labels |
|---|---:|---:|---|
|3|1210|243 of 243|none|
|5|20306|3124 of 3125|scalar 3 only|

The total subspace count is checked against

    [5 choose 3]_p=(p^5-1)(p^4-1)/((p^2-1)(p-1)).

The complete fiber histograms also match the archived receipt. This audit does not repeat its p=7 or p=11 census. The bounded direct p=3,5 check takes approximately 2.4 seconds locally.

Replayable artifacts:

* `verify_d5_locator_labels_independent.py`
* `verify_d5_locator_labels_independent.json`

Run with the research Python environment containing python-flint. The receipt records the concrete extension-field polynomials, counts, timings, and assertion results.

## Brief rejection of the preliminary quadratic guess

The suggested missing-label equation z^2-z-1=0 does not fit: in characteristic 11 the locator

    L=X^(11^3)+8X^(11^2)+5X^11+8X

has exactly a three-dimensional root space in F_(11^5), since

    (T^2+3T+4)(T^3+8T^2+5T+8)=T^5-1 in F11[T]

gives the corresponding p-polynomial composition identity, and L is separable. Its label is 8+5-8^2=4, although 4^2-4-1=0 modulo 11. This exact countercertificate is included in the receipt. It is only a check of the discarded guess, not a classification of the remaining scalar fibers.
