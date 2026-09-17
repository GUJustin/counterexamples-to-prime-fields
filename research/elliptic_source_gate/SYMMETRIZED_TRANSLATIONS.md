# Feasibility gate for a torsion-translation RS source

September 17, 2026. A symbolic check of one concrete new construction,
not an exclusion of elliptic or algebraic-geometric methods generally.
This route fails before a numerical search is warranted.

Let E/C have equation y^2=x^3+ax+b with nonzero discriminant. For a
finite nonidentity translation point A=(u,v), consider

  S_u(x(P)) = x(P+A)+x(P-A)
             = 2[u x^2+(u^2+a)x+au+2b]/(x-u)^2.

The addition law gives this identity directly. For v nonzero its pole
at x=u has order two, since the displayed numerator takes value 4v^2
there. For a nonidentity two-torsion translation its reduced rational
degree is one; otherwise it is two. It is always nonconstant. The
common denominator for L distinct non-two-torsion x-coordinates u has
degree 2L. Clearing it produces ordinary polynomials of degree at most
2L, but does not increase their agreements away from excluded poles.
Thus even a large torsion translation group is not a free supply of
low-degree RS candidates.

## Stronger failure on the full torsion domain

Take the distinct finite x-coordinates of E[m], omitting undefined
received or candidate poles. Let h>=1 divide m, and take the received
word to be x([h]P). This is well-defined as a function of x(P), since
negating P negates [h]P and leaves its x-coordinate unchanged.
Write R_h(x)=x([h]P), a rational map of degree h^2.

The equality S_u(x)=R_h(x) has at most h^2+2 finite roots unless the
rational functions are identical. They are not: for h>=2 their degrees
differ, and for h=1 the function R_1=x has a pole at infinity whereas
S_u is finite at infinity. Clearing the two denominators proves the
root bound, with cancellations only decreasing the degree.

There is a second, complementary bound. The multiplication map sends
E[m] into E[m/h], so the received word has at most (m/h)^2 distinct
finite values. A nonconstant rational map of degree at most two takes
each value at at most two x-coordinates. Consequently every candidate has

  A <= min(h^2+2, 2(m/h)^2).

Put z=h^2. The two terms cross at z=-1+sqrt(1+2m^2); hence

  A <= 1+sqrt(1+2m^2) = O(m).

The full finite x-domain has (m^2+t-2)/2 points, where t=|E[m][2]| is
one for odd m and four for even m. For h>=2, removing the preimages of
the received pole at infinity leaves Theta(m^2) points whenever m/h>=2;
indeed h<=m/2 then removes at most about m^2/8 x-coordinates. Removing
candidate poles can only reduce agreement. If h=m, every received value
is undefined and no source exists. For h=1 there is no additional pole
removal and the stronger constant root bound applies.

Thus on the full torsion domain (or after only a fixed-fraction deletion),
these candidates have O(sqrt(N)) agreement, not a positive agreement
fraction. Clearing their common denominator does not change this fact.
The proposal cannot supply fixed-positive-rate, fixed-gap nearest banks.
If one instead selects only O(m) nodes, the domain is a different sparse
construction; the argument does not rule it out, but a shared high-
agreement domain must then be supplied and its polynomial degree budget
checked separately.

## Scope and decision

Do not run a torsion enumeration for this particular symmetrized-
translation/isogeny-word proposal. The failure is quantified already.
This says nothing about other elliptic functions, higher-degree
translation combinations, non-isogeny received words, or a new shared-
pole identity. Reopen this route only with a concrete identity escaping
both the degree and finite-image bounds.
