# Independent complete census and good-reduction audit

**PASS.** The earlier condition that the full system enumeration had not been independently replayed is now discharged.

## Independent enumeration

`independent_census.cpp` is a separate implementation. It reads the node/word input reconstructed from the independently verified nine-quartic decoder, uses variable order C8,...,C0,B4,...,B0, visits base subsets by bit masks in descending node order, and solves by forward echelon elimination with backward substitution. The original generator instead uses B/C ascending order, recursive subsets, and full Gauss–Jordan elimination. The independent field inverse uses the quadratic norm formula rather than an exhaustive inverse-table search.

| full fibers f | all base subsets | refined systems on consistent bases | consistent final systems | unresolved families |
|---|---:|---:|---:|---:|
| 0 | 816 | 31 | 31 | 0 |
| 1 | 3,060 | 42,308 | 226 | 0 |
| 2 | 8,568 | 667,992 | 988 | 0 |
| 3 | 18,564 | 4,084,080 | 1,498 | 0 |

The union is literally equal, coefficient by coefficient, to the generator's set of 733 norms. The comparison is recorded in `independent_census.verified.json`; raw output is `independent_census.json`. The bounded replay completed in 1.09 seconds using 4,656 KiB peak RSS. For reproducible compilation on this machine, the system compiler required `-isysroot /Library/Developer/CommandLineTools/SDKs/MacOSX15.4.sdk` to avoid an unrelated newer-SDK linker mismatch.

Together with the separate Python classification replay, this is a complete fixed-residue certificate. There are 705 nonzero square norms and 28 with binary odd degree four, six, or eight; none has binary odd degree two or is zero.

## Enumeration coverage over the algebraic closure

For a non-descended section E4+ZO3 on a connected quadratic cover, at most three selected fibers are full, because O3 is nonzero and the selected fibers are unramified. If its total agreement is at least fifteen and its actual full-fiber count is f, then at least 15−f distinct fibers are hit. Choose a (15−f)-subset containing all f full fibers. The norm vanishes at those nodes, and its two partial derivatives vanish at each chosen full fiber. This is one of the enumerated systems.

The enumeration does not assume these equations are independent. It explicitly preserves affine solution directions, imposes the full-fiber conditions on that entire affine space, and reports every remaining family. All consistent final systems have dimension zero. Therefore their coefficients lie in F289 even when the putative section or its branch divisor is defined over a larger field. This justifies the algebraic-closure conclusion for the fixed residue word.

The binary squarefree test covers arbitrary degree-two P1 maps, including branch infinity: pi_*O=O plus O(−1), so pi_*pi*O(4)=O(4) plus O(3). A genuine non-descended norm has J8=B2 O3² with squarefree binary B2, hence exactly two odd-multiplicity branch points. No recorded norm has that property. Descended sections are covered by the complete threshold-eight quartic census, whose maximum residue agreement is nine rather than eight.

## Good-reduction lemma

The proposed lemma is correct under all of its explicit hypotheses, including arbitrary ramification of the mixed-characteristic valuation ring. One wording correction is needed: the affine chart with infinity away from the thirty-six marked nodes is a chart on the **cover parameter line**, not the base/source parameter line.

After a residue extension, choose this chart by a PGL2 transformation over the DVR. The thirty-six marked sections then have integral coordinates with unit pairwise differences. The good-reduction degree-two morphism identifies its pulled-back O(4) with O(8) over the DVR; the corresponding local evaluation frames at marked points differ only by units. Thus the received evaluations used for interpolation are integral. Nine actual agreements determine any degree-eight competitor with integral coefficients by a unit Vandermonde determinant.

Its reduction is therefore a degree-eight section with at least fifteen matches on the special-fiber quadratic cover. The fixed-residue theorem forces it to be the pullback of one known residue quartic. Let U be that residue candidate's agreement set on the cover: it has size at most eighteen. A set S of fifteen actual competitor agreements and the sixteen selected agreements T of the known lifted candidate both lie in U. Hence |S intersect T|≥15+16−18=13>8. The two generic-fiber sections coincide. This reasoning handles both residue candidates with accidental ninth base matches, and does not require characteristic-zero completeness of the source list.

The conclusion is only for degree-two maps with good reduction and unramified special fibers above the selected marked nodes, with all lifted marked points having distinct reductions. A bad-reduction map, specialization of branch points to source marks, or coalescing cover coordinates is outside the lemma. The finite result alone must not be promoted to an all-covers characteristic-zero exclusion.

No manuscript edits were made.
