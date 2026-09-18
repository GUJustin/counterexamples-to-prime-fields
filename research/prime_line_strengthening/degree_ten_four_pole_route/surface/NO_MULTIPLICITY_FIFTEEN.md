# Exact global exclusion of multiplicity-fifteen points modulo29

Let H(a,b,c) be the reconstructed degree62 Gauss-image equation in
`gauss_image_interpolation.json`. The following proof is a polynomial
identity certificate over F29, hence applies over its algebraic closure.
It does not rely on checking only finite-field rational parameters.

## Affine chart a=1

Write h(b,c)=H(1,b,c). Form every Hasse derivative h^[i,j] with i+j<=14.
A point of multiplicity at least15 must annihilate all these polynomials.
Multiply each order-t derivative by each monomial b^u c^v with u+v<=t;
the resulting products have degree at most62. Since h has mu7 character5,
the constant-character products satisfy

    5-2i-4j+2u+4v =0 modulo7.

Their exact coefficient matrix has1113 nonzero rows and288 columns.
Its rank is287, and the constant polynomial1 lies in its row span.
`hasse_multiplicity_gate.json` records276 nonzero terms of an identity

    1 = sum c_(i,j,u,v) b^u c^v h^[i,j](b,c).

The script verifies the complete coefficient vector of this identity.
Thus there is no multiplicity-fifteen point in this affine chart.
The matrix need not have full column rank for this conclusion.

## Boundary a=0

In the chart c=1 form the a,b Hasse derivatives of H(a,b,1), then set a=0.
The gcd of these univariate polynomials for total orders through14 is1.
The saved boundary certificate expresses1 as a combination of seven
such polynomials, with derivative indices

    (0,0),(0,1),(1,0),(1,1),(2,0),(2,1),(3,0).

Every multiplier coefficient is recorded, and the script multiplies and
sums them back to1 exactly. This excludes every geometric point on the
boundary except [0:1:0]. The latter has exact multiplicity6 by the minimum
a+c exponent among monomials of H, and is excluded as well.

Consequently the projective multiplicity-at-least15 locus of H is empty.
All Hasse orders0 through14 were included; no homogeneous Euler shortcut
across characteristic29 was used.

## Receipt and scope

`hasse_multiplicity_gate.py/json/resources.json` record the exact input
hash, row provenance, coefficients, and successful0.59-second/14MiB run
under the60-second/384MiB watchdog. An independent replay can ignore the
linear-algebra search and simply verify the two displayed polynomial
identities and the endpoint support from the original H coefficients.

This is a completed modular algebraic-closure exclusion. Turning it into
a characteristic-zero no-rational-member statement additionally requires
the relative discriminant-cycle specialization argument. That geometric
transfer is separate from this certificate and is not assumed here.
