# Complete cubic pullback: independent finite gate and characteristic-zero transfer

## Independent residue replay: PASS

The independent executable `independent.cpp` differs from the generator in its partition, symmetry, and interpolation algorithm. Its two halves contain alternating base fibers rather than the first and last eight fibers. It uses the opposite primitive cube root, Newton divided differences instead of Lagrange interpolation, and only the order-three deck rotations; it does not use Frobenius to identify subsets. It enumerates 2,615,008 nine-anchor subsets and 871,744 canonical pencils, finding no non-descended degree-nine polynomial with seventeen matches. Runtime 2.70 seconds, peak RSS 4,336 KiB. Receipt: `independent.json`.

Every seventeen-match candidate has at least nine matches in one of the two twenty-four-node halves. For nine anchors, all degree-at-most-nine interpolants form the affine pencil q+lambda L, where q has degree at most eight and L is the monic nine-anchor locator. At each remaining node x, the required parameter is (w−q(x))/L(x); the denominator is nonzero. A candidate has seventeen matches exactly when one parameter occurs at least eight times. The exhaustive parameter histogram thus avoids iterating over every polynomial. Deck rotation preserves each half and its word, and preserves degree and the property of descending through T³. Retaining the smallest subset in each rotation orbit loses no possible non-descended hit.

All forty-eight nodes and word values lie in F289. Any polynomial over its algebraic closure with at least ten matches is the unique degree-nine interpolant on ten of these points, so its coefficients already lie in F289. The finite gate therefore excludes non-descended seventeen-match candidates over the algebraic closure, not merely over the base coefficient field. This is stronger than the earlier F17-only Frobenius-pair gate.

Descended residue candidates can have eighteen matches, coming from six-match residue cubics. The gate does not discard this case in the characteristic-zero transfer.

## Exact rational cubic cover and transfer

Use the explicit rational source in the U-chart and the degree-three cover

    U=(11−T³)/3,    T³=11−3u_j.

The sixteen radicands reduce to 1,...,16 modulo17. Their forty-eight cube roots are distinct and lie in the unramified quadratic residue extension F289. The eight lifted degree-nine polynomials reduce, after common polynomial subtraction and a nonzero scalar, to the original P_i(T³) residue seed.

Suppose a characteristic-zero degree-nine Q has at least seventeen matches. Interpolating ten actual matches on unit-separated nodes makes its coefficients integral at the place above17. The residue gate forces its reduction to descend through T³. Its base cubic matches at most seven residue fibers, by the original complete cubic census. Thus all actual matches of Q lie over at most seven labeled generic base fibers.

If f of those fibers are fully matched, the total agreement is at most 2*7+f. Seventeen matches imply f>=3. Write Q(T)=E(T³)+T O(T³)+T²V(T³), with degrees at most 3,2,2. Full agreement with the same received value at all three distinct roots of a fiber forces O and V to vanish at its base coordinate. Three distinct full fibers force O=V=0. Therefore Q itself descends to a cubic on the rational source, with at least six source matches. The exact rational four-point interpolation census has only the eight known cubics at threshold six: eight have seven matches, eight fresh cubics have five, and all remaining interpolants have four. Hence Q is one of the eight inherited polynomials.

The cubic pullback consequently has complete nearest list eight, maximum agreement twenty-one, and every fresh degree-nine polynomial has at most sixteen matches, over characteristic zero and its algebraic closure. This argument explicitly handles reduction to a fresh six-match residue cubic; it does not assume residue completeness at threshold seventeen consists only of the original eight.

## Prime-field specialization

Take a finite Galois number field containing all forty-eight roots. There are finitely many ten-point degree-nine interpolants on the fixed domain. Exclude denominators and the norms of every nonzero evaluation difference for these interpolants, together with node separation guards. At every remaining completely split rational prime, the same agreement counts persist. Every candidate with at least seventeen matches is among the ten-point interpolants, so both completeness and the fresh-agreement bound sixteen persist. Arbitrarily large such primes exist.

## Stronger threshold sixteen: independently replayed

`independent16.cpp/json` checks a different exact parameter-plane algorithm from the root's pair-intersection count. It uses alternating base-fiber halves, the opposite primitive cube root, Newton interpolation, and only C3 symmetry. All 1,470,942 eight-anchor subsets give 490,314 canonical planes q7+L8(a+bT). The forty other points impose forty lines a+b*x=t. Any eight-fold concurrence includes a reference among the first thirty-three lines. For each such reference, the verifier counts equal slopes to the other thirty-nine lines: seven equal slopes certify the concurrence. There are no non-descended candidates with sixteen matches. Runtime 2.23 seconds and 4,608 KiB peak RSS. The algebraic-closure coefficient argument remains valid by ten-point interpolation.

The characteristic-zero consequence improves to every fresh candidate having at most FIFTEEN matches. If the descended residue base cubic has seven matches, it is known; all sixteen actual match indices then lie in its twenty-one-point residue support, and the known lift agrees at all these indices. Sixteen common points force equality of degree-nine polynomials. If the residue base cubic has six matches, sixteen actual matches confined to six fibers force at least four full fibers. Their O2,V2 vanish, so the candidate descends; exact rational source completeness at threshold six again makes it known.

The fresh bound fifteen is attained by composing any exact fresh-five-match rational source cubic with the cover. Thus the nearest agreement is twenty-one, the complete nearest list has eight elements, and the next-best agreement is exactly fifteen. Good split-prime specialization preserves this gap by the finite ten-point-interpolant guard argument. The manuscript-ready separate fragment is `../cubic_pullback_completeness.tex`; no main manuscript file was edited.
