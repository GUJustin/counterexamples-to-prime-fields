# A rational envelope gives linear full-support MCA

September 17, 2026. New proof under local audit. Elementary incidence
argument extending the polynomial residual cluster lemma already in
`research/bounded_root_mca/appendix.tex`. No novelty claim.

## Statement

Let F be any field, D a nonnegative integer, and X a set of n distinct
F-points. Fix polynomials S,R in F[X], with R nonzero. Let h count zeros
of R on the evaluation domain. Fix r>=0 and consider any family of
polynomials P of degree at most D such that

    (P-S)/R = a_P/b_P,  deg a_P <= r, deg b_P <= r,

as rational functions, with b_P nonzero. No bound is imposed on the size
of the family or the coefficients/degrees of S,R. Let f+zg be any received
line, and require agreement at least an integer 1<=A<=n. A candidate is full-support bad
when g has no degree-at-most-D interpolant on its entire agreement set.

Suppose A-h >= beta*n for some 0<beta<=1, and

    n >= 48*r/beta^3.

Then the number of distinct bad labels witnessed by this family is at
most 16*(n-A+1)/beta^3. There is no characteristic restriction, field-size
assumption, or bound on how many candidates occur at one label.

## Proof

Select one bad candidate P_z at each distinct bad label under consideration.
For infinite fields select any finite set; the same bound then applies.
Write W_z=(P_z-S)/R in reduced form. At every domain point where R is
nonzero, W_z is regular, since it equals (P_z-S)/R. Divide the received
line by R after subtracting S at these points. Each selected pair has
at least beta*n agreements on these retained coordinates.

Consider ordered triples of distinct graph points (z,W_z) in F(X)^2.
If a triple is not collinear, its affine-incidence determinant is a
nonzero rational function. Clearing the three reduced denominators gives
a nonzero polynomial of degree at most 3r. Thus the triple has at most
3r common retained agreement coordinates.

A line in this graph through two selected points corresponds, after
multiplication by R and addition of S, to a polynomial pencil U+zV with
deg U,deg V<=D: interpolate the two actual polynomials at their distinct
scalar labels. Every selected point on this graph line is on that pencil.
There are at most M=n-A+1 selected bad labels on any such line. To see
this sharp pencil bound, let c count persistent coordinates where
(f,g)=(U,V). Every other coordinate can agree at at most one scalar label.
If c<A, each nearby label uses at least A-c nonpersistent agreements, so
there are at most floor((n-c)/(A-c))<=n-A+1 nearby labels. If c>=A,
a full-support bad label must have an additional nonpersistent agreement,
or U,V explain its entire support. There are at most n-c<=n-A such labels.
This proves the claimed bound in both cases.

Let L be the number of selected labels. On each retained coordinate x let
b_x count their agreements; extend by b_x=0 on deleted coordinates.
Then sum b_x >= beta*n*L. The ordered triple-incidence count satisfies

    sum_x b_x(b_x-1)(b_x-2)
      >= sum_x (b_x-2)_+^3
      >= n*(beta*L-2)_+^3.

For L>=4/beta this is at least beta^3*n*L^3/8. Noncollinear triples
contribute at most 3r*L^3. Each ordered pair determines one graph line,
with at most M possible selected third labels; hence there are at most
M*L^2 collinear ordered triples. Each contributes at most n coordinates.
Consequently

    beta^3*n*L^3/8 <= 3r*L^3+n*M*L^2.

Since 3r<=beta^3*n/16, rearranging gives L<=16*M/beta^3. The case
L<4/beta also satisfies that bound. This proves the theorem.

## Consequences and exact limits

If deg R<=D+c and A-D>=eta*n, then h<=D+c and beta can be eta-c/n
when positive. For fixed c,r, every sufficiently large length therefore
has O_eta(n) bad labels. The theorem even allows r to grow linearly with
n provided r<=beta^3*n/48.

For logarithmic derivatives P=R H'/H with deg H<=r and deg R=D+1,
use S=0, a=H', b=H. This gives a uniform linear full-support bound without
restricting the roots or multiplicities of H, and in all characteristics.
The earlier isolated-family theorem gives a stronger constant bound for
its particular finite residue alphabet. The new envelope result permits
arbitrary residues and affine pencils, for which a linear bound is natural.

A union of M such envelopes, each with the same beta,r bounds, has at
most 16*M*(n-A+1)/beta^3 bad labels. M must be fixed to infer linear growth.

This theorem does NOT cover arbitrary polynomial candidates by taking
R=1: the resulting r is D, and its size hypothesis fails at the usual
positive-rate, small-gap parameters. Nor does an arbitrary high-degree
R help if it vanishes on too many evaluation points. It does not prove
an unrestricted linear prime-field proximity theorem.

This is a limitation of potential lower-bound mechanisms, not evidence
that the upper theorem is intrinsically tight. Its role is to show why
large bounded-residual algebraic families still fail to supply many
unexplained nearby labels on the same received line.
