# Independent audit: norm-bank trace pullback degree gate

September 19, 2026. **PASS**, with the scope explicitly stated in the audited note. This is an algebraic audit; no finite search is needed.

## Inherited-word identity and degree

With base-field input nodes, coefficientwise Frobenius computes Frobenius of evaluated values. Thus the inherited word equals H plus the three cyclic terms A_i A_(i+1)/B_(i+1). Clearing the norm of B gives denominator degree at most 3d and numerator degree at most 4d. Subtracting a degree-at-most-d candidate retains the 4d bound. B is assumed nonzero on the domain, so no undefined or pole coordinates enter the root count. At more than 4d matches the candidate must be the single rational identity H+R. This counts distinct polynomials, not bank parameters.

The base-field input hypothesis is essential: at arbitrary extension-field inputs coefficient twisting alone does not compute value Frobenius. Native evaluation-domain membership is also correctly retained as a separate guard. A separately chosen traced received word need not have this rational identity.

The fixed witness-span citation applies to the affine space H+U, with dim U≤6. Adding 1 to U if necessary yields dimension at most seven and no common evaluation zero. Subtracting H invokes the affine version of the archived lemma, so there is no extra dimension charge for H. At fixed positive rate and a fixed positive gap above d/n, that lemma bounds the fixed-word list by a constant.

## Degree forcing and evaluations

The seven character exponents 0, ±1, ±Q, ±Q² are distinct modulo Q²+Q+1 for every Q≥2. The resulting polynomial of degree less than Q²+Q+1 cannot vanish on all roots of unity unless every coefficient vanishes. This proves full affine span of the bank, including characteristic two.

In Moore coordinates, clearing Norm(z) makes an affine functional a homogeneous ternary cubic. The full affine span supplies a rational point outside its zero set. Every line through that point has a nonzero cubic restriction and hence at most three projective roots, including infinity. The Q+1 lines partition the remaining projective points, giving the claimed bound 3(Q+1). This proof also covers characteristic three; it does not assume Tr(1) is nonzero.

Applying this bound separately to every high-degree output coefficient forces the actual A,B,H to degree at most e when more than 3(Q+1) bank parameters have outputs of degree at most e. For the whole bank, affine span suffices even when the numerical threshold is vacuous. The evaluation-level statement is valid: reduction modulo the base-field domain locator commutes with coefficient trace, preserves all evaluated data, and converts low-degree representability into the required formal coefficient statement. This avoids assuming that a high-degree chosen representative is the canonical codeword polynomial.

The threshold is a count of distinct parameters and itself grows with Q. It does not rule out every growing subbank of size O(Q). Nor does the cubic bound automatically pass to a further trace to a proper subfield. These limitations are explicit in the final note.

## Growing extension degree

For Q=p^r and prime-field inputs, the cyclic trace has 3r terms with index increment r. Norm-denominator degree is at most 3rd, while the residual numerator degree is at most (3r+1)d. Therefore increasing r weakens this test, as stated; it is not excluded by the fixed-r argument.

Before final trace, the native matching condition is exactly A A^[sigma^r]−a A B^[sigma^r]−b B B^[sigma^r]=0, of degree at most 2d independently of r. Since B is not the zero polynomial, subtracting two identity conditions gives (a−a')A+(b−b')B=0. Nonconstant A/B permits at most one identity pair. Constant A/B can give several parameters but their identity outputs coincide. Other inherited native matches are bounded by 2d. Any larger trace list would therefore require new trace-kernel coincidences, which this note does not claim to exclude or construct.

The final scope is accurate: this rules out the specified bounded-degree inherited-word compiler in the stated agreement regimes, not arbitrary trace-based constructions, arbitrary linear coefficient maps with new words, or all growing-extension-degree routes. It yields no new proximity-gap counterexample or certified benchmark gain.

## Audited artifact SHA-256

- `NORM_BANK_TRACE_PULLBACK_DEGREE_GATE_2026_09_19.md`: `91688f715d20d8ab11b39395423c64e01af8bbe4952d672c53fad70cb0b7d394`
- `research/strategy_review/fixed_witness_span_gate/INDEPENDENT_AUDIT.md`: `6a1c5aa81afba6bb9846eeadfd715358e8f5156e6e3e100ef150fcb7b3fd7e2d`
