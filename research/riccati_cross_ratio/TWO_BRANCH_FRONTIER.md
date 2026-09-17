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
This normalized special case is now CLOSED at rate at most 1/4:
the agreement it forces is too large, and three labels already force
a proportional family with a common correlated agreement set. See the
proof below. It must not be pursued as a candidate for the quarter-rate
fixed-gap lower bound. The unnormalized two-branch equation remains open.

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

## Closure of the zero-branch normalization (September 17)

Let T be the squarefree locator of n distinct coordinates. Suppose
char(F)=0 or char(F)=p>D, n>4D, and R_z=R_0+z R_1 with R_1 nonzero.
Consider nonzero polynomials P_z of degree at most D satisfying

    R_z = P_z - T P_z'/P_z.

Every root of P_z lies among the roots of T: a root outside T would
give a nonzero logarithmic-derivative residue, since its multiplicity
is between 1 and D<p. Thus P_z agrees with R_z at every domain point
outside its roots, at least n-D coordinates.

Take three distinct labels z_1,z_2,z_3 and write z_3=c z_1+(1-c)z_2,
where c is neither 0 nor 1. Outside the union of the three root sets,
the line relation gives P_3=cP_1+(1-c)P_2. There are at least n-3D>D
such coordinates, so this is a polynomial identity. Substituting into
the R identities yields

    P_3'/P_3 = c P_1'/P_1 + (1-c) P_2'/P_2.

Clearing denominators and expanding gives

    c(1-c)(P_1-P_2)(P_1' P_2-P_1 P_2') = 0.

Distinct labels give distinct P's, because R_z is an injective
polynomial line. Hence P_1/P_2 has zero derivative. After cancellation
its numerator and denominator have degree at most D<p, so the ratio
is constant (also in characteristic zero). All three P's are proportional.
Every further label, paired with the first two, has the same property.

Consequently any family with at least three labels has P_z=b_z Q for
one polynomial Q, and R_z=b_z Q-T Q'/Q. The scalars b_z vary affinely
with z. On the common set where Q does not vanish, of size at least
n-D, the whole received line is explained by the affine codeword line
b_z Q. In fact these are the full agreement sets: at a root x of Q
of multiplicity e, (T Q'/Q)(x)=e T'(x) is nonzero.

Thus this special route has at most two labels unless it has a common
correlated explanation at agreement at least (n-D)/n. The quarter-rate
message convention D=k-1, n=4k satisfies n>4D. This proof does not
cover general F_z,G_z, nor any arbitrary first-order differential
equation. It corrects the earlier exploratory optimism about F_z=0.
