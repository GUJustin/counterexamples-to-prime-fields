# Nonprimitive norm-power audit: PASS with explicit elimination scope

The independent stdlib verifier reconstructs every Hasse entry from the
fourteen original nodes and word values, derives the support and jet
labels independently, and takes exact integer Bareiss determinants of
the selected ORIGINAL rows. It does not import the generator or reuse
its modular row elimination. The results are

    t=2: 63 columns,63 rows, determinant27 modulo29;
    t=5: 12 columns,28 rows, selected determinant27;
    t=10: 5 columns,14 rows, selected determinant8.

All three column spaces have trivial interpolation kernel. The replay
took0.027seconds; `nonprimitive_norm_gate.verified.json` and the watchdog
receipt are saved. This confirms the supplementary LaTeX paragraph's
pure-power exclusion.

## Precise norm-to-power lemma

Work in characteristic zero, algebraically closing constants if desired.
Let X=psi(U) have degree10, let v(U) be a rational function, and put
L=k(X,v) inside k(U). Then

    t=[k(U):L] divides10,
    Norm_(k(U)/k(X))(Y-v)=m(Y)^t,

where m is the monic minimal polynomial of v over k(X), of degree10/t.
This follows directly by norm transitivity. On clearing denominators and
taking the primitive part in k[X,Y], Gauss's lemma gives a nonzero scalar
multiple of G^t, where G is the primitive irreducible equation of the
image. For t>1 the only possibilities are2,5,10. This also covers a
constant v in k(X), where t=10.

If the primitive polynomial G^t belongs to the stated uniform net, its
weight, Y degree and local multiplicities immediately give

    wdeg(G)<=floor(34/t), deg_Y(G)<=10/t,
    mult_Q(G)>=ceil(4/t), mult_T(G)>=ceil(6/t).

Weighted degree and maximal-ideal order are additive for products over a
field, because their associated graded polynomial rings are domains.
The verified minors exclude every such G over characteristic zero: the
same square minors are integral at the chosen prime and remain nonzero.

## When contacts survive primitive-part extraction

Removing an arbitrary vertical factor from an arbitrary resultant can
destroy its prescribed contacts. That step cannot be implicit.

A sufficient hypothesis, met by the intended proper augmentation setup,
is that every selected fiber of psi consists of distinct points and v
is regular at all of them, with the claimed received values. Over the
completed base DVR each branch v is then integral. The field norm of
Y-v is a monic integral polynomial, and every agreeing branch contributes
one factor in the maximal ideal (X-x,Y-w). Thus its order is at least
the number of agreeing branches. Its monic leading coefficient is a
unit, so passing to a primitive cleared polynomial changes it by a unit
at every selected base coordinate. The prescribed contacts therefore
survive. Removing polynomial vertical content cannot increase weighted
degree.

For the binary resultant of coprime cover forms R,S and a proper rational
witness N/D, selected fibers being off D and S makes this local assertion
explicit. Indeed at a selected base value the denominator D*S^3 is
nonzero at every fiber point, so the resultant's leading coefficient in
Y is a unit. One must still supply the weighted-box bound from the
applicable norm construction; it is not a consequence of field degree
alone.

The manuscript's conditional wording, requiring an eliminated norm that
is a scalar pure power in the uniform net, is safe as written. For an
unconditional augmentation application, state the separable selected
fibers, absence of poles there, and the weighted-box bound explicitly.
No assertion about arbitrary reducible polynomials in the net follows
from these three power tests.
