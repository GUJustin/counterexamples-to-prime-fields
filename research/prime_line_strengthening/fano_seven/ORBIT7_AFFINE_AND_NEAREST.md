# Affine conversion and a true-nearest certificate for the orbit7 bank

This note assumes the exact seven-polynomial incidence certificate in
orbit7_number_field.json, independently checked separately. Its implications
below do not require another search.

Let K=Q(w), where w^3+2w^2-w-1=0. The cubic is irreducible: its only possible
rational roots are ±1, and neither is a root. Every listed finite evaluation
node is either0,1 or a nonconstant polynomial in w of degree at most two.
Consequently none equals2. Apply the projective coordinate transformation

    t=1/(X-2),       X=2+1/t.

For each cubic P_i put

    Ptilde_i(t)=t^3 P_i(2+1/t).

This is a polynomial of degree at most three. Send an old finite received
value y at node x to t^3 y at t=1/(x-2), and send the old infinity value to
the received value at t=0. The latter is the leading coefficient of a matching
old cubic. This produces14 distinct finite evaluation points and preserves
all incidences, so it is an ordinary affine Reed–Solomon construction rather
than merely an extended-code construction.

The maximum agreement of ANY cubic is exactly seven. Each of the fourteen
received positions is matched by three or four of the seven certified bank
members. If a new cubic P has A matches, counting intersections with all
seven bank members gives at least3A. Each distinct bank member has at most
three common projective evaluation points with P, counting infinity by the
binary-cubic convention. Therefore3A<=21, hence A<=7. A cubic equal to a
bank member already has exactly seven certified matches, so cannot be an
exception to this argument. The same reasoning works after affine conversion.

Moreover, a new seven-match cubic must use only the seven triple positions:
a single quadruple position would force at least22 pair intersections.
Its support must therefore be exactly the set of all seven triple positions.
There is at most one such polynomial, determined already by any four of those
distinct points. Thus the full nearest list has size either seven or eight;
four-point interpolation and checking the remaining three values decides it.
This note does not assert the outcome of that final interpolation check.

The construction has length14, polynomial degree cap3, agreement7, and at
least seven genuine nearest codewords. These finite parameters alone do not
give an unbounded-list family or a superlinear prime-field proximity-gap
counterexample.
