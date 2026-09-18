# Exact interpolation can certify the whole Gauss image

## Geometric hypotheses and scope

The archived affine ramification residual Gamma is irreducible over F29.
The point(1,10) is a smooth F29 point, with gradient(27,14). These facts
prove absolute irreducibility: otherwise Frobenius transitively permutes
its geometric components, and a rational point lies on every conjugate
component and is singular. A nonconstant rational Gauss map from Gamma
therefore has an absolutely irreducible image C, defined over F29.

The audited effective residual discriminant cycle has degree62. The
Gauss image is one of its components, so deg C<=62, regardless of whether
isolated rank-one jet points contribute other parameter lines, or whether
the map Gamma->C has degree greater than one. Interpolating C does not
automatically reconstruct that whole residual cycle or its multiplicities.

The sampler must certify every projective image point by an actual source
point on Gamma where the jet matrix has rank exactly two. Its Gauss
parameter is the one-dimensional kernel. Point counts alone, or only
checking the three jet equations without excluding rank one, would not
certify that the samples lie on this particular image curve.

## Bezout certificate, including the extra-factor issue

Let S contain more than3844 distinct geometric points of C. Any nonzero
homogeneous degree62 polynomial vanishing on S must contain C, since
otherwise Bezout bounds its intersections with C by62*deg C<=3844.
Thus the degree62 vanishing space of S is exactly

    I(S)_62 = G * k[a,b,c]_(62-d),

where G is the irreducible equation of C and d=deg C. This proves that
the gcd of a full basis of that space is G, up to a scalar. A single
interpolant need not be irreducible and need not equal G; taking the full
basis avoids assuming its extra factors away. Its dimension must be
binomial(64-d,2), providing a consistency check.

## Exact symmetry reduction

The action on parameter coordinates is

    [a:b:c] -> [a:zeta^(-2)b:zeta^(-4)c], zeta=16 in F29.

For homogeneous degree62, divide the2016 monomials into the seven
characters2*deg_b+4*deg_c modulo7. Frobenius and this action preserve C.
The script checks that the input sample set is a union of full orbits of
the generated21-element group, with projective normalization and exact
deduplication. It then chooses one representative per orbit.

Within a character space, mu7 translates multiply every evaluation by
the same nonzero scalar. With coefficients in F29, Frobenius translates
conjugate the evaluation. Thus a representative over F29³ supplies exactly
the three base-field coordinate equations needed for its entire orbit.
Solving all seven character blocks recovers the FULL degree62 vanishing
space, not just one selected character. The invariant kernel decomposes
as a direct sum because7 is invertible and zeta belongs to F29.

`interpolate_gauss_image.py` uses independent tuple arithmetic modulo the
sampler's irreducible cubic, checks field and projective normalization,
computes all seven nullspaces over F29, forms their polynomial gcd, checks
the dimension formula, and evaluates the resulting equation directly on
every supplied point. The input file's SHA256 is recorded.

The completed run used4018 distinct points in192 symmetry orbits. All
seven blocks have288 columns and576 rows; characters0,1,2,3,4,6 have
full rank288, while character5 has rank287. The full degree62 kernel is
one-dimensional. Its gcd has degree62 and271 nonzero terms. The equation
was directly verified on all4018 points. The run took4.82seconds and53MiB
under the60-second/384MiB watchdog; exact data and receipts are
`gauss_image_interpolation.json/resources.json`.

Given the certified source witnesses, absolute irreducibility and cycle
degree bound above, Bezout proves this is the exact image equation over
the algebraic closure. Its degree62 exhausts the residual discriminant
cycle, so its cycle multiplicity is one and no other positive-degree
parameter components remain. In particular the Gauss map has degree one.
This does not rule out incidence components contracted to parameter points.
No characteristic-zero equation or rational member is asserted here.

## Consequence for the next bounded target

A rational integral member must be a point of multiplicity at least15
on this residual curve, by the separately audited local smoothing
argument. A reduced plane singularity of multiplicity15 has delta at
least105. The arithmetic genus of a degree62 plane curve is1830, hence
there are at most17 such geometric points. The three mu7-fixed parameter
axes have exact multiplicities3,6,3, read directly from the coefficient
support, so none qualifies. All remaining orbits have size seven.
Consequently the modular multiplicity-at-least15 locus has at most14
geometric points, in at most two mu7 orbits.

An exact Hasse-jet computation must include all local orders0 through14.
In characteristic29, using only the top order and recovering lower orders
by homogeneous Euler identities is unsafe because those identities cross
a factor divisible by29.
