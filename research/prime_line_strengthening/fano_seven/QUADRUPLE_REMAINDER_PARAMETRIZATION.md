# Exact three-amplitude parametrization of every incidence orbit

This is a reversible reduction, not an existence assertion or an obstruction.
It applies to all eight ordered designs, including non-Fano orbits 0–3.

Let b_1,...,b_7 be the seven distinct quadruple-node coordinates. The triple
C_l is the complement of the four candidates matching at b_l. Each candidate
index occurs in exactly three C_l, hence matches at precisely four b_l.
Put

    L_i(X) = product_{l: i not in C_l} (X-b_l).

For arbitrary received values at these seven nodes, interpolate the unique
polynomial W of degree at most six. Every candidate cubic is necessarily

    P_i = W mod L_i.

Conversely, these remainders satisfy every required quadruple-node incidence.
Thus this parametrization loses no solutions. Coincidences beyond the required
incidences, coincident candidates, or coincident nodes must still be excluded.

Common cubic addition changes neither any difference nor the incidence
geometry. Subtracting the degree-at-most-three part of W permits the exact
normalization

    W = a X^4 + b X^5 + c X^6.

The three amplitudes cannot all vanish in a distinct-candidate solution.
Writing L_i=X^4-s_1 X^3+s_2 X^2-s_3 X+s_4, ordinary monic division gives

    Q_i = c X^2 + (b+c s_1) X + a+b s_1+c(s_1^2-s_2),
    P_i = W-L_i Q_i.

In particular, the coefficients of P_i, from X^3 down to 1, are

    a s_1 + b(s_1^2-s_2) + c(s_1^3-2s_1 s_2+s_3),
    -a s_2 + b(-s_1 s_2+s_3)
       + c(-s_1^2 s_2+s_2^2+s_1 s_3-s_4),
    a s_3 + b(s_1 s_3-s_4)
       + c((s_1^2-s_2)s_3-s_1 s_4),
    -s_4(a+b s_1+c(s_1^2-s_2)).

All formulas are integral identities, with no characteristic restriction.

For each required triple {i,j,k}, divide P_i-P_j and P_i-P_k by their
known common factors at quadruple nodes, and require an additional common
root t_{ijk}. Merely setting a resultant to zero is insufficient unless its
root is outside all seven b_l and distinct from the six other triple nodes;
it may otherwise certify a forbidden existing-node collision or a degree
degeneration. Retaining t_{ijk} explicitly avoids that ambiguity.

In a genuine saturated seven-cubic configuration, pair differences have
exactly their three prescribed distinct roots. Accordingly all leading
cubic coefficients are distinct in a finite-coordinate model. This guard
can be imposed before any elimination.

There are seven b coordinates and three amplitudes. Common output scaling
projectivizes the amplitudes; the PGL2 action on the evaluation coordinate
removes three further dimensions on the open distinct-node locus. This gives
six parameters before imposing seven additional triple-common-root
conditions. The apparent deficit of one is only an expected-dimension count:
it is neither an impossibility proof nor evidence that those conditions are
independent. Working with a projective coordinate at infinity requires
homogeneous binary cubics instead of silently using the finite-coordinate
leading-coefficient guard.
