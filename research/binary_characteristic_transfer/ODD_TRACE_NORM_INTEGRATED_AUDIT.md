# Odd trace–norm integrated independent audit

Verdict: PASS. Read the complete frozen `odd_trace_norm_refinement.tex` and compared its statement and proof with the independently derived compiler/source audit and the exact finite receipt. No manuscript edits were made.

Checked the following substantive points:

- The polynomial trace normalization makes F and G have the same leading coefficient; P is monic, its correction has degree exactly k, and its displayed witness has strict degree below k and exactly T matches.
- All nonzero trace–Hermitian differences split over B, including the zero-level center of multiplicity Q+1. This gives injection at every exterior pole and exactly n(Q−1) distinct certified labels.
- The c_* normalization is defined by c_*^p=Lambda(beta)^(p−1). The Omega argument is nonzero at beta, and its double-root factor proves multiplicity at least p at every native agreement coordinate, including multiple roots of the residual. Its degree bound and the resulting U are correct.
- The endpoints r0=f+c_*g and r1=c_*g have source bounds U and k, with exact common agreement k. The map t=1−c_*/lambda loses no bank label and places every one in the affine interior.
- The finite Johnson slack and full high-branch first-order factor are correct for every odd p and s>=2. The smallest rate is 34/81, safely in that branch. Positivity of the quadratic sign places the positive agreement on the upper side of its unique positive root; it is not an ambiguous sign test.
- The p=3,s=2 paragraph agrees with the fixture receipt: n81,k34,T51,U45,648 distinct interior parameters, Johnson slack72, first-order sign1496/59049. The receipt's numerator13464 over81^3 is the same sign. Its verifier hash matches the actual script. This review inspected the receipt and did not repeat the producer's field enumeration or claim a codeword enumeration.
- The final comparison explicitly attributes the fixed-rate, constant-margin, superlinear-count regime to the inherited construction. It correctly distinguishes finite correction-degree/injectivity refinements, growing prime-field extension degree4s, and characteristic smaller than code dimension. No complete label classification, nearest-agreement equality, singleton claim, or prime-alphabet claim is introduced.

The proof is self-contained relative to the manuscript's definition of the first-order curve and ordinary Reed–Solomon/common agreement. The independent algebra is recorded in `ODD_TRACE_NORM_COMPILER_INDEPENDENT_AUDIT.md`.

## Reviewed file hashes

- `odd_trace_norm_refinement.tex`: `14a7d3e01e32bc7f05fed410b3a4376df757f5f7c13d140b5de262bbe510b03f`
- `ODD_TRACE_NORM_EXACT_COMPILER.md`: `7e28d64ce4fd1548a4b21150e4570bf4337b6d87ae88fcd272ccd4464796f71e`
- `norm_trace_p3_s2_fixture/verify.py`: `eb06422d9a3d4fa89eeca7a4377383a874826ab3e9cb8c5ad6a1bb793f4c2e5d`
- `norm_trace_p3_s2_fixture/receipt.json`: `c3d77107a91bdafa8a7238b51ece8c3d8ccdf45b5d2cd93d0cbc56edd8436758`
