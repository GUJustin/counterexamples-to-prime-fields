# Complete second tier on the fixed rational cubic cover

**PASS.** For the fixed cover U=(11−T³)/3 of the explicit rational sixteen-node source, the complete degree-nine agreement profile above fourteen is exactly eight inherited cubics with twenty-one matches and eight further descended cubics with fifteen. Every other polynomial has at most fourteen agreements. This holds in characteristic zero over the algebraic closure, and at all sufficiently good completely split primes of a fixed number field containing the domain.

## Independent finite enumeration and interpolation obstruction

`independent15.cpp` uses alternating base-fiber halves, the opposite cube root, Newton interpolation, and only C3 deck symmetry. It detects seven-fold concurrence in the eight-anchor parameter planes by slope histograms from the first thirty-four of forty residual lines. Any seven-fold concurrence contains one of those references. This differs from the original pair-intersection histogram and Frobenius quotient. The exact search produces seven representatives; their deck/Frobenius closure is literally equal to the nine candidates obtained from the original three canonical hits. As before, any fifteen-match algebraic-closure candidate has F289 coefficients by ten-point interpolation.

`verify_lift15.py` independently brute-forces the unique root lift among all 289 first-digit corrections for each of the forty-eight marked roots modulo17². It checks the exact rational source gauge, then interpolates the LAST ten nodes of every fifteen-node support using Newton divided differences over (Z/289)[theta]/(theta²−7). The original script instead uses the FIRST ten nodes and Gaussian elimination. All nine candidates have nonzero residuals at remaining support points. All supports, orbit equality, normalized coefficient reductions, and residual divisibility by17 are checked exactly. The receipt is `lift15.independent.json`.

This is not merely a failed unramified deformation search. The fixed-cover nodes and rational word values lie in the fixed unramified local extension. Their unit-separated ten-node Vandermonde matrix determines a unique integral interpolant already over that ring. Any candidate over any ramified or residue-field extension matching those ten points must be exactly that polynomial. Its nonzero modulo17² residual cannot be removed by passing to a larger field. Every non-descended residue candidate has exactly fifteen matches, so a candidate with fifteen actual matches must lift its entire residue support. Thus all nine are excluded without a ramification loophole.

## Descended residue cases and exact second tier

After removing the nine non-descended residue possibilities, a characteristic-zero Q with fifteen matches reduces to a cubic in T³. It can match at most seven residue base fibers. If it matches seven, the residue base cubic is known. Its characteristic-zero inherited lift matches all twenty-one corresponding coordinates, so Q and that lift agree at the fifteen actual matching points; degree nine forces equality.

Otherwise all actual matches lie over at most six base fibers. Fifteen points force at least three complete three-point fibers, since partial fibers contribute at most two. In Q=E(T³)+T O(T³)+T²V(T³), deg O,deg V≤2, each full fiber forces O=V=0 at its distinct base value. Three full fibers force both polynomials identically zero. Thus Q is a descended cubic with at least five rational source matches.

The independently enumerated exact rational source has 1,516 four-point interpolants, exactly sixteen with at least five matches: eight have seven and eight have five, with no six-match source polynomial. Hence their distinct pullbacks are exactly the sixteen claimed candidates, with agreement counts21 and15. Every algebraic candidate is covered because four rational source matches determine the descended cubic over Q.

For split-prime specialization, keep the nonzero evaluation differences of every ten-point degree-nine interpolant, as well as all coordinate and denominator guards. This finite guard set preserves the complete two-tier profile; every candidate with fifteen matches is a ten-point interpolant. The eight fifteen-match witnesses themselves are descended rational polynomials, so the tier is attained after specialization.

## Moving-cover scope

The fixed-cover assertion above does not use the moving-cover modulo17³ obstruction or any unproved tangent-gauge identification. Those computations remain separate research evidence. In particular, this audit does not promote the varying-cover claim to arbitrary ramification, other residue points, or bad-reduction covers.

The manuscript fragment `../cubic_pullback_completeness.tex` has been upgraded in place, preserving its label and first-order comparison. No main manuscript file was edited.
