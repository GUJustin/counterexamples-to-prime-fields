# Complete unrestricted W12 census

For W=(X^12-1)^2/2 on the 48th roots of unity, seek degree-at-most-11 polynomials with at least16 agreements. The C++ search is complete over F1009, with primitive root13. It found exactly9 polynomials, in two rotation orbits of sizes6 and3, each with exactly16 agreements. Runtime6.003 seconds. The independent DFT replay confirms all degree bounds and supports; both orbits are compositions in X² (the second even in X⁴).

## Coverage

Partition the domain into four12-node cosets indexed by exponent modulo4; the word is constant on each. A constant polynomial has only12 matches. Otherwise each coset contributes at most11.

If a candidate has m≥5 matches on a coset, choose all m matching nodes there and factor P-v=G R. Then deg R≤d=11-m. The other36 nodes contain at least16-m matches. Split them into two18-node halves: one contains at least d matches. Enumerate its d-anchor subsets. Newton interpolation gives R=R0+tL, and each remaining node supplies one possible t. A bucket of size5 suffices and is necessary for this enumeration to retain the candidate. Enumerate m=5,...,11 and all four cosets. The m-anchor subsets may be quotiented by cyclic rotation of the12 nodes, because X→ζ⁴X preserves the word. There are66,80,66,43,19,6,1 anchor orbits. For d=0, use one empty-anchor pencil, not two identical halves. Total17,205,820 pencils.

Otherwise the candidate has exactly4 matches on each coset. Choose the four matches on the first coset, modulo rotation (43 choices), and the four on the second (495 choices). These8 anchors give P=P8+L8R with deg R≤3. Any4 matches on the third coset contain at least3 among its fixed first11 nodes. Enumerate those165 triples, interpolate an affine cubic pencil, and require a parameter bucket of size4 on the fourth coset plus at least1 further match on the third. Total3,512,025 pencils.

The combined20,717,845 pencils cover every candidate. Every retained polynomial is directly evaluated at all48 nodes before output. Rotations are expanded for the final list count. Parent's independent coverage receipt counts four additional duplicate empty-anchor pencils; this does not change coverage.

## Characteristic-zero transfer

Any characteristic-zero candidate with16 agreements has coefficients in Q(ζ48), determined by12 matching nodes. At the prime over1009 sending ζ48 to13, all node differences are units, so interpolation coefficients are integral and reduction preserves every match. Therefore its reduction is one of these nine candidates. Since every modular candidate has exactly16 matches, its complete modular support must equal the characteristic-zero support. Interpolating any12 points of that support over Q(ζ48), then checking all48 points, exhausts the possible lifts. The independent exact replay is owned by audit_random_directions; finite census alone is not substituted for that replay.

Files: search.cpp, search.raw, search.log, resources.json, survivors.json; independent output verification verify_survivors.py and survivors.verified.json. Root's independent mathematical coverage audit is ROOT_COVERAGE_AUDIT.md.
