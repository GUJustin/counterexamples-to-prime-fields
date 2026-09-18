# Independent audit of the revised ten/eleven-source quadratic-cover screens

**PASS for the revised rank-exception-complete certificates.** Over characteristic zero and its algebraic closure, neither fixed source admits a fresh degree-six section with at least thirteen matches on the full selected fibers of a connected degree-two cover, assuming all selected fibers are separable. The ten/eleven inherited source cubics remain permitted and have fourteen matches. This concerns the fixed received words and the pulled-back O(3) line bundle, not an arbitrary change of received values or source.

## Independent replay

`verify_padded_quadratic_norms.py` independently assembles every modular system in reversed C/B coefficient order, computes all coefficient-rank exceptions regardless of augmented consistency, and replays the retained systems over Q(sqrt(d)) in the square-root basis rather than the generator's theta basis. Exact linear algebra uses doubled rational matrices. Binary squarefree degrees are checked by a separate Euclidean/Yun squarefree algorithm over the quadratic field, rather than the generator's SymPy algebraic squarefree factorization.

| source | prime | all 11/12-subsets | deficient coefficient-rank bases | full-rank retained bases | exact norms | binary odd-degree counts |
|---|---:|---:|---:|---:|---:|---|
| ten | 47 | 50,388 | 588 | 412 | 48 | all 48 degree zero |
| eleven | 61 | 125,970 | 1,154 | 444 | 61 | all 61 degree zero |

For each source exactly one retained eleven-subset requires all 55 possible full-pair refinements over the exact field. None remains a positive-dimensional consistent family. The field embeddings are independently checked coefficientwise: sqrt(17) maps to 8 modulo47 and sqrt(39) maps to51 modulo61. Source coordinates remain distinct, and the independently constructed node/word residues agree with the screening input.

Receipts are `ten_quadratic_norm_independent.json` and `eleven_quadratic_norm_independent.json`. The joint bounded job completed in 5.42 seconds at 34,864 KiB peak RSS. The earlier uncorrected 113/70 norm counts are not the audited final census; after exact full-fiber conditions and complete exceptional-system replay, the counts are 48/61.

## Why the modular exclusions are valid

The eleven unknown norm coefficients satisfy linear equations with integral source coefficients at the chosen place. If the coefficient matrix has rank eleven modulo p, an eleven-row minor is a unit. Any exact solution is unique and integral at that place, even if the cover initially lives over an extension. Modular inconsistency then excludes an exact solution, and a rejected modular norm is the genuine reduction of any exact solution.

If coefficient rank drops modulo p, neither modular inconsistency nor a modular parity failure is safe by itself. A characteristic-zero solution can have denominators divisible by p. The revised screen therefore retains EVERY deficient-coefficient-rank base system, including those with an inconsistent augmented modular system. Independent enumeration confirms the complete 588/1,154 exception lists. They are solved over the exact quadratic field; every exact affine family on an eleven-subset is refined by both derivative conditions at every possible pair. Any remaining family on a twelve-subset would be unresolved and prohibit the conclusion, but there is none.

For an integral norm, the rejection test uses a closed degeneration condition, not the open condition of having two distinct branch points. The map

    P² × P² -> P⁶, (B2,O2) -> B2 O2²

is a projective morphism, and its image is closed. Its affine cone also contains zero. Over an algebraic closure, a nonzero binary sextic belongs to this image exactly when its binary squarefree part has degree at most two: the remaining even multiplicities contain a degree-two square divisor. Thus a genuine characteristic-zero B2 O2² can reduce to a square or zero, and these possibilities MUST be retained. The code does retain them. Infinity multiplicity is included as 6−deg(J), so affine degree drops are not silently discarded. Unit normalization or extension of the valuation ring gives the same closed-image specialization argument when B2 and O2 themselves have denominators.

## Geometric completeness

On a connected quadratic P1-cover in characteristic zero, write a section as E3+Z O2 with Z²=B2 squarefree binary quadratic. If O2=0, thirteen matches require seven base matches, so source completeness gives an inherited candidate. If O2 is nonzero, at most two selected fibers are full. Thirteen matches require at least eleven distinct norm-hit fibers. Twelve or more hits are covered by a twelve-subset. Exactly eleven hits force two full fibers, where H=H_w=H_X=0. Those are precisely the linear equations used in the exact pair refinement.

Every surviving exact norm has binary squarefree degree zero, incompatible with B2 O2² having two distinct odd-multiplicity branch points. If J were identically zero, it would also be impossible with B2 and O2 nonzero. All conditions include branching at infinity and arbitrary projective coordinates on the cover; selected fibers are required to remain separable so they give the advertised full set of distinct coordinates.

No manuscript changes were made. The rank-drop correction is essential to this proof and must accompany any use of the result.
