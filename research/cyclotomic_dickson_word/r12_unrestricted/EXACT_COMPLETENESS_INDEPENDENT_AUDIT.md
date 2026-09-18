# Independent exact lifting and coverage audit for W12

Status: PASS. The unrestricted modular gate, together with the exact replay, proves that over characteristic zero the word W12=(1+X^24)/2-X^12 on mu48 has maximum agreement 16 among polynomials of degree below 12, and exactly nine polynomials attain it. They are precisely the archived composition bank, in rotation orbits of sizes six and three.

## Coverage and implementation

I read `search.cpp` and independently checked both branches against `ROOT_COVERAGE_AUDIT.md`. A nonconstant degree-at-most-11 polynomial has at most 11 hits in a single constant-word coset. If one coset has m>=5 hits, use its full hit subset and canonicalize it by mu12 rotation. Its locator factors P-c, leaving degree d=11-m. Among the 36 other coordinates, one of the two 18-point halves contains at least d of the remaining 16-m hits. Interpolation on d such anchors leaves a one-dimensional affine pencil. At least five additional hits have the same pencil parameter, exactly the histogram threshold used in the code. All divisions outside the chosen coset and at nonanchor nodes have nonzero denominators.

Otherwise any qualifying polynomial has exactly four hits in each coset. The code interpolates on four coset-0 and four coset-1 nodes, then three coset-2 anchors from an eleven-point prefix. Every four-subset contains at least three points in that prefix. These eleven conditions leave a degree-11 pencil. Four hits in coset 3 and one additional hit in coset 2 certify sixteen total, as implemented. Canonicalizing the coset-0 subset does not invalidate this universal prefix property. Constant polynomials have only twelve matches and need not be separately searched.

An independent orbit census, deleting rotation orbits from the full combination sets rather than canonical-minimum collection, gives counts 43,66,80,66,43,19,6,1 for subset sizes 4 through 11. The total is 20,717,845 pencils. The difference of four from the initial unoptimized coverage count is exactly the four duplicated empty-anchor half cases when m=11. Saved in `coverage.independent.json`. This independently checks the complete count and implementation coverage; it is not a second execution of the exhaustive C++ search.

## Independent characteristic-zero replay

`exact_replay.py` uses FLINT rational-polynomial arithmetic in Q[z]/(z^16-z^8+1), with z a primitive 48th root. For each modular representative it interpolates on the reversed last twelve support nodes, evaluates at all 48 nodes, and expands all twelve rotations. Both representatives have exactly sixteen exact matches and orbit sizes six and three. Their full union has nine distinct polynomials, all identical to the independently reconstructed archived composition bank. `exact_replay.json` records every exact coefficient in ascending powers of z, every support, and the complete rotation closure. Exact replay took about 0.02 seconds.

## Transfer of completeness

Choose the prime above 1009 sending z to the recorded root 13. All 48 nodes have distinct residues. Any characteristic-zero polynomial with at least sixteen matches is uniquely interpolated by twelve matching nodes, hence has coefficients in Q(z), integral at this prime. Its reduction is one of the nine modular survivors. Every modular survivor has exactly sixteen matches, so all actual matching indices are precisely that survivor's support. Interpolation on any twelve of them therefore identifies the original polynomial with the exact lift verified above. A polynomial with more than sixteen matches would reduce to a modular polynomial with more than sixteen matches, which the complete gate excludes. This argument applies over arbitrary characteristic-zero coefficient extensions and uses crucially that every modular survivor has exactly sixteen matches.

The result is a complete fixed-source census, not an unbounded construction or a statement about all received words.
