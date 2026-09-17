# Independent audit of the gauge extension — September 17, 2026

Reviewed the proof sketch in BEYOND_MONIC_RICCATI.md. The algebraic gauge
identity is correct. For nonzero A and T, the substitution Y=AP transforms
T P' - A P^2 + R P - S=0 into

  T Y' - Y^2 + (R-T A_X/A)Y - AS=0.

Its coefficients are polynomial precisely when A divides T A_X. In that
case their challenge degrees remain bounded: z-degree is additive for
nonzero products in the integral domain F[X,z]. Let a=deg_X A and E=D+a.
The following extension is mathematically justified with one additional
characteristic hypothesis that the original sketch did not state:

  characteristic zero or characteristic > E=D+a.

The published monic proof needs distinct coefficient pivots through degree
E. The original characteristic>D is insufficient to reuse that proof
when a>0. This is a genuine additional scope restriction, not a numerical
technicality. The lower-degree case alone still only needs characteristic>D.

Assume agreement threshold H satisfies H>(5D+4a)/3+lambda*n. If deg_X T
is at most 2E, the original equation has a value-independent separant T.
Its persistent domain root set has size at most 2E; total singular
coordinate-label incidences outside that set are at most deg_z(T)*n.
The fixed-cover theorem for original degree-D messages gives the claimed
linear count, since (2*(2E)+D)/3=(5D+4a)/3.

If deg_X T>2E, use only the high-degree cases of the monic theorem on Y.
The received values for Y are polynomial curves A(x,z)(f(x)+zg(x)), not
an affine received line, so citing the monic theorem verbatim would be
incorrect. Its recurrence and plane-intersection proof nevertheless
continues to apply. Remove the at most a coordinates where A(x,z)
vanishes identically. Agreement equations on the remaining coordinates
retain bounded parameter degree and challenge degree O(E). A source curve
with at most D persistent remaining coordinates contributes at least
H-a-D nonpersistent incidences per candidate, with positive linear slack
under the displayed assumption. More than D persistent remaining
coordinates determine the original degree-D candidate P as an affine
pencil: fix D+1 of them and exclude roots of their nonzero A-values,
then divide at those coordinates and interpolate. This adds O_h(D)
exceptional labels per source component, still O(n). There are only a
bounded number of components in the high-degree proof. Individual labels
where A(X,z) vanishes identically are also explicitly excluded.

Hence bounded-a gaugeable coefficients are ruled out in large enough
characteristic and with the stated slack. This extension is now Corollary Q.3 in the paper, with a second
independent review of the final LaTeX. It is not a
construction, a universal first-order result, or a benchmark certificate.
