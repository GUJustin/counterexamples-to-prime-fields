# Independent audit: all connected quadratic covers of the fixed rational source

**PASS.** The statement is that no *fresh* section of the pulled-back degree-three line bundle has thirteen or more agreements on the thirty-two points of a connected degree-two cover of P1 with all sixteen selected fibers separable, over characteristic zero or its algebraic closure. The eight pulled-back source cubics remain allowed and have fourteen matches. The received values must be the pullback of the fixed rational source sections, with the corresponding common line-bundle trivialization. This is not an obstruction for changing the source, allowing repeated selected points, or arbitrary unrelated received words.

## Independent exact replay

`verify_exact_general_quadratic_thirteen.py` assembles the equations in the different unknown order C6,...,C0,B3,...,B0 and reproduces the full rational norm set. It uses FLINT rational linear algebra, independently assembled derivative rows, and an independent coefficient-recursion square test rather than the generator's polynomial factorization.

* Eleven-subsets: 4,368 total; five inconsistent, 4,363 unique; none positive-dimensional.
* Twelve-subsets: 1,820 total; 1,801 inconsistent, nineteen unique; none positive-dimensional.
* After the required two-full-fiber test for eleven-subsets and deduplication: exactly thirty norms, equal to the generator's exact rational set.
* Every J=E²−C is nonzero and is an exact rational scalar times a polynomial square. Its degree is even and its infinity order 6−deg J is even.

The receipt `exact_general_quadratic_thirteen.verified.json` records each scalar, monic polynomial square root, and infinity order. Thus no factorization oracle is needed for the final parity certificate. Runtime was below one second, without a scan over covers.

## Exhaustiveness and boundary cases

Over an algebraically closed characteristic-zero field, a connected degree-two map P1→P1 has two distinct branch points. Its finite flat algebra is O⊕O(−1), with multiplication specified by a squarefree nonzero binary quadratic B. A section of the pulled-back O(3) is uniquely E+ZO, where E is a binary cubic and O is a binary quadratic. This covers arbitrary rational quadratic maps, including branching at base infinity; it does not require a polynomial square map.

If O=0, a thirteen-match section must match at least seven complete base fibers, and source completeness forces one of the original eight cubics. If O is nonzero, at most two selected full fibers are possible: at an unramified selected fiber the two values of Z are distinct and nonzero in a local frame, so matching both forces O=0 and E=w. A nonzero binary quadratic has at most two distinct such zeros. All selected base nodes are finite in the certified U chart, but a zero of O at infinity can only decrease this count.

Let M be the number of distinct hit fibers and f the number of full fibers. The total match count is M+f, so thirteen matches imply M≥11. If M≥12, one of the enumerated twelve-subsets applies. If M=11, necessarily f=2, and both full fibers belong to that eleven-subset. At a full fiber the norm H=(w−E)²−BO² satisfies H=H_w=H_U=0, with w held fixed in the last derivative. All three conditions are linear in the coefficients of H=w²+B3w+C6. The exact enumeration retains every possible pair when an affine family occurs; the independent replay establishes that no such family actually occurs in this source. No extension-field coefficient solutions are hidden, since every consistent system used here is uniquely solved over Q.

A nonzero B O² has odd vanishing order at exactly the two branch points. This is incompatible with every recorded J, whose vanishing orders are even at all finite points and at infinity. The generator's convention assigning degree zero to J=0 would need a separate explanation in a general instance: J=0 is also impossible with B and O nonzero. In this instance all thirty J are nonzero, as independently verified, so that degenerate case never arises. A drop in affine degree is accounted for by the explicitly verified infinity order; it is not discarded.

There is no scope correction needed to the stated connected-cover/separable-fiber theorem. The above clarifies the line-bundle interpretation and closes the potentially ambiguous zero-J and infinity cases.
