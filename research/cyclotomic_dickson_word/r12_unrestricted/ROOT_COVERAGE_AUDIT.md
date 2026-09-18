# Independent coverage reduction for the unrestricted r=12 gate

Target: degree at most11, at least16matches on the48th roots, with four twelve-node constant-word cosets. A constant matches only12; every nonconstant has at most11matches in any one coset.

If some coset has m>=5 matches, enumerate its complete m-subset up to the exact mu12 rotation symmetry. Write P=c+L_m R, deg R<=d=11-m. Outside that coset are36points with at least16-m matches. One of two eighteen-point halves has at leastceil((16-m)/2)>=d matches. Enumerate d anchors there; every residual polynomial is q+tL_d. At least(16-m)-d=5 remaining outside points determine the same t. This covers every candidate in this case. Search output must still be evaluated on all48points to certify counts and duplicates.

Otherwise sixteen matches force exactly four in each coset. Enumerate four roots in coset0 up to mu12, four anchors in coset1, and three anchors in a fixed eleven-node subset of coset2. Every four-subset of coset2 has at least three in that prefix. After factoring the first locator these seven anchors give a residual degree7 pencil. A valid candidate supplies at least one further coset2 match and four coset3 matches at the same parameter. This covers the remaining case.

The canonical rotation acts on polynomials and all nodes; it preserves all four word cosets. The prefix condition applies to the transformed candidate as to every candidate, so it is compatible with canonicalizing the first support. Canonical output is not itself the full list: recover the rotation orbit and remove duplicates.

Exact independent orbit counts and resulting pencil totals are in root_coverage_counts.json. Prime1009 is1mod48 and keeps spurious modular supports much rarer than97. Any characteristic-zero candidate has integral coefficients at this split prime by twelve-point interpolation on unit-separated roots; a modular exclusion therefore transfers. Modular survivors require exact cyclotomic replay, including every matching support and full orbit.

Implementation count clarification: at m=11 the residual degree is zero and each half supplies the same empty anchor set. Skipping the duplicate half removes exactly one pencil per coset, four total. Thus the complete implementation visits20,717,845 pencils, four below the undeduplicated coverage count20,717,849. This changes no covered candidate.
