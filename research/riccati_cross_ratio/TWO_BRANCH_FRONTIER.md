# Two-branch singular-coordinate route: exploratory status

The main fixed-positive-gap quadratic target is still unresolved.
The following is an attempted route, not a theorem or counterexample.

Take a domain locator T of degree n and a Riccati equation

    T P' = (P-F_z)(P-G_z),

with F_z,G_z affine in z. At every domain coordinate a polynomial
solution matches one of the two branches. For D<n/2, this could force
nearby candidates at a fixed gap if one branch is matched sufficiently
often. Polynomial identities, rather than coordinate constraints alone,
remain the obstruction to constructing many labels.

The special case F_z=0, G_z=R_z becomes

    R_z = P - T P'/P

for nonzero P. All roots of P must be roots of T under p>D. Outside
those roots, P agrees with R_z, hence on at least n-D coordinates.
Thus a large nonaffine labeled family for which the displayed rational
logarithmic-derivative expression lies on one affine polynomial line
would be a promising candidate. Merely finding many factors of T is
insufficient: their expressions R_P must share that same line.

Some immediate restrictions:

- The leading coefficient of R_P in degree n-1 is -deg(P). If that
  coefficient varies nontrivially with z, at most D distinct labels
  are possible for nonconstant candidates. A serious construction must
  therefore fix the candidate degree (or avoid this normalization).
- High coefficients of T P'/P encode root power sums. Because n>2D
  at a fixed positive gap in this special route, there are more high
  coefficients than the candidate degree; these impose substantial
  compatibility conditions beyond local residue equations.
- With T squarefree, a root x of P of multiplicity e forces
  R_z(x)=-e T'(x). If the z-direction at x is nonzero, it supplies at
  most D labels. Repeated roots and coordinates with zero direction
  prevent this observation alone from proving an O(n) count.
- Existing spectral_riccati results cover a different normalized
  family with bounded X-degree challenge weight. They do not close this
  unrestricted route. No claim of a general first-order proof follows.

A related attempted escape through common polynomial composition led
instead to the separate upper-bound note in ../composed_bounded_root_mca/.
That proof does not by itself resolve this two-branch route.
