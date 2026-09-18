# Seven verified reducible parameter lines

The exact computation `old_graph_lines.py` reconstructs each old cubic from
four of its seven matching nodes, verifies its complete fourteen-node
incidence mask, and substitutes it into all three norm-net basis members.
The result is always a scalar times the degree34 locator whose exponents
are4 at matched quad points and6 at matched triple points. The seven
normalized scalar functionals, in the archived basis coordinates `(a,b,c)`,
are

    a+24b+23c, a+25b+24c, a+20b+20c, a+16b+7c,
    a+7b+c, a+23b+25c, a+b+16c                 (mod29).

Each is nonzero, and the seven lines are distinct. On each line the script
constructs two spanning parameter vectors and verifies coefficient by
coefficient the division by `Y-P_i(X)`. Thus these are exactly the parameter
lines where the corresponding old cubic graph divides the member.

On the first line, write the generic member as `F_left+z F_right` and divide
out its old graph. FLINT factors the resulting primitive polynomial over
F29[X,Y,z] as a single irreducible factor, of degrees `(30,9,1)`. This is
irreducibility over the stated finite coefficient field, not a claim of
geometric irreducibility over its algebraic closure. The complete job took
0.54 seconds under the60-second/384MiB watchdog.

These lines must be retained as known reducible strata during any global
parameter analysis. They are not automatically components of the
degree-at-least15 discriminant-gcd locus. Indeed, on the fourteen-point
blowup the old graph C has C²=-4 and D.C=0; hence
`C.(D-C)=4`. Its generic intersections with the residual component therefore
account for four extra singularity-index units. This is consistent with
the independently observed specialized gcd degree4 and does not by itself
explain a gcd of degree15.

The restriction argument works in characteristic zero as well, but the
displayed seven numerical linear forms are modular. A characteristic-zero
parameter or component cannot be discarded merely because its reduction
lies on one of these lines.
