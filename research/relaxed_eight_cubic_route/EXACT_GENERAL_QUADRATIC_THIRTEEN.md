# Exact obstruction to a thirteen-match quadratic-cover augmentation

For the exact rational eight-cubic received word in `rational_seed.json`, no connected degree-two map from a projective line, with all sixteen selected fibers separable, admits a fresh degree-six section agreeing at thirteen or more of the thirty-two pulled-back coordinates. This includes arbitrary branch points, not just the square map. The statement is over characteristic zero and its algebraic closure. It concerns this fixed source; it does not exclude changing the source or a different degree cover.

Write the double cover in binary form as `Z²=B₂(X,V)`, where B₂ is squarefree of degree two. A section of the pulled-back O(3) has a unique form `E₃(X,V)+Z O₂(X,V)`. A section with O₂=0 is a pulled-back cubic. Source completeness gives only the original eight cubics with seven or more base matches, and hence only those eight pulled-back sections with thirteen or more matches.

Suppose O₂ is nonzero. At most two selected base fibers can have both preimages match, since such a full fiber requires O₂=0. Define the monic norm

`H(X,w)=w²+B₃(X)w+C₆(X)=(w−E₃)²−B₂ O₂²`.

Thirteen matches therefore require at least eleven distinct norm-hit fibers. If there are twelve or more norm-hit fibers, one of the 1,820 twelve-subsets is a set of norm zeros. Otherwise there are exactly eleven norm-hit fibers and two full fibers. At each full fiber, `H=H_w=H_X=0`: explicitly O₂ vanishes and the received value equals E₃. These are linear equations in the eleven unknown coefficients of B₃ and C₆.

The executable `exact_general_quadratic_thirteen.py` reconstructs these systems from the exact affine rational table U=1/(X−3). It examines all 4,368 eleven-subsets and all 1,820 twelve-subsets. For an eleven-subset with a unique norm, it checks every node for the two derivative conditions. For a positive-dimensional solution space it adds those conditions for every pair of nodes and solves again. No consistent positive-dimensional refined spaces remain. All surviving systems give exactly thirty distinct rational norms, recorded in `exact_general_quadratic_thirteen.json`.

For every one of those thirty norms, the binary sextic `J=E₃²−C₆`, with E₃=−B₃/2, has squarefree part of degree zero. The certificate records its exact rational factorization, with the infinity valuation obtained from `6−deg(J)`. In contrast, a nonzero expression `B₂ O₂²` with squarefree binary B₂ has squarefree part of degree exactly two, including the possible infinity root. This contradiction excludes every non-even candidate over the algebraic closure. Scalar square roots do not change this parity argument.

The computation uses exact FLINT rational row reduction and factorization, takes about 0.27 seconds, and does not infer characteristic-zero inconsistency from modular specialization. The complete subset census also avoids identifying potentially different rational norms merely because their reductions modulo 17 coincide. Independent replay should be retained alongside this generator before manuscript use.
