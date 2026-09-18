# Exact quotient reduction for non-Fano orbits0 and1

This is a proved reduction, not an obstruction or a constructed solution.
It applies to the first two ordered incidence orbits in design_orbits.jsonl.

Both have triple block345 and complementary triple block345. Let t be the
coordinate for the former, and u the coordinate for the quadruple1267.
Subtract P1 from every candidate and the received word. At u, the four
candidates indexed by I={1,2,6,7} now vanish. Consequently

    H_i=(P_i-P1)/(X-u),  i in I,

are four distinct polynomials of degree at most two. For j in J={3,4,5},
put

    R_j=(P_j-P1)/(X-u).

These are proper one-pole functions with numerator degree at most three.
Indeed P_j(u) cannot equal P1(u): the saturated global incidence count says
exactly the four candidates in I match the received symbol at u.

Remove the two nodes t,u. On each of the remaining12 nodes, divide the
translated received value by X-u. Directly from either orbit's incidence
blocks, exactly two members of I match at each remaining node. Each H_i
has exactly six matches, since it loses its match at u and had no match at t.
Each R_j has exactly six matches, since it loses its match at t and had no
match at u. In addition,

    R_3(t)=R_4(t)=R_5(t).

Thus either orbit would produce a four-quadratic12-point bank together with
THREE distinct proper degree-three/linear rational witnesses sharing the SAME
pole, each with six matches, and sharing one further off-domain value.

This reduction is reversible at the level of degrees and displayed incidences
if such a bank and three witnesses with the specified supports are provided:
multiply by X-u, restore the common polynomial P1, and add the u and t nodes.

The four-quadratic bank here is GENERAL. It need not be projectively equivalent
to H_i=X^2/a_i^2+a_i^2, and its paired roots need not be signs of common base
coordinates. Therefore the earlier balanced/antibalanced support classification
and the observed distinct poles in that special family cannot be applied to
exclude this configuration. A valid general same-pole three-witness theorem
would close orbits0 and1, but no such theorem is proved here.

For orbits2 and3, the same quadruple1267 is present, so division at its node
still produces four quadratics and three proper rational functions. However
there is no complementary triple345 among T, so the remaining incidence
pattern does not collapse to the same exact12-point bank. The preceding
three-witness reduction must not be silently extended to those orbits.
