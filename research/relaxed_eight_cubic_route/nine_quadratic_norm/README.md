# Complete fixed-residue quadratic polynomial-cover pilot

Input: the independently verified nine-quartic word on18 nodes over F17(theta), theta²=7, encoded a+17b, in `../nine_complete_decode.json`. Its maximum degree-four agreement is9: two known quartics have9 matches and seven have8. Its complete list at threshold8 consists of these9 quartics.

Question: can a polynomial of degree at most8, fresh relative to the nine pullbacks, have at least15 matches after a simple quadratic polynomial cover Y=T²+c? The branch c must avoid all18 base nodes. Coefficients and c may lie in the algebraic closure of F289.

Write the candidate E(Y)+T O(Y), deg E<=4, deg O<=3. If O=0, a fresh candidate descends to a fresh base quartic and has at most14 matches, by completeness at threshold8. Thus O is nonzero. It can vanish at at most3 base nodes, so the number f of fully matched two-point fibers is at most3. Choosing15 matches gives at least15-f distinct hit fibers. Its norm is

    w²+B(Y)w+C(Y), B=-2E, C=E²-(Y-c)O²,

with5+9=14 unknown coefficients. At a hit fiber x require w²+B(x)w+C(x)=0. At a full fiber also require B(x)=-2w and wB'(x)+C'(x)=0. These are linear equations over F289.

For f=0,1,2,3 enumerate every(15-f)-subset of the18 base nodes and every f-subset of those selected nodes as full fibers. This covers any candidate with at least15 matches; selecting fewer than all matches cannot invalidate the equations. Solve the base affine system once and restrict the full-fiber equations to its affine solution space. Every consistent final system is uniquely solved: there are no underdetermined survivors, so no algebraic-closure solutions are missed by collecting F289 vectors.

`search.cpp` completes4,794,411 refined systems on consistent base subsets in1.53seconds. The base subsets themselves are all enumerated, including inconsistent ones; the printed f=0 system count31 counts only consistent base systems, not all816 tested subsets. Consistent refined counts by f are31,226,988,1498. Deduplication gives733 norms. A necessary binary odd-factor degree<=2 test retains705 norms.

Independent Python polynomial arithmetic in `classify.py` decomposes these705 norms. Every J=E²-C is a NONZERO SQUARE:658 have degree8,44 degree6,2 degree4,1 degree2. Therefore none can equal(Y-c)O² with O nonzero, over any algebraic extension. There is no proper fresh candidate in this fixed-source pilot.

This is a finite-characteristic fixed-residue exclusion, not a characteristic-zero exclusion for the moving implicit source. A characteristic-zero family may have nonintegral normalized norm coefficients or specializations in omitted projective charts. No inference excluding that family is claimed. The C++ system enumeration has not yet received a separate implementation replay; Python independently reclassifies the saved norms, not the entire coverage computation.

Files: `input.hpp`, `search.cpp`, `screen.json`, `resources.json`, `classify.py`, `classified.json`. The supplied source/word encoding is the same as the independently audited decoder.
