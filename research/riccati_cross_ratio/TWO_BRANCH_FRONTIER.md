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
More generally, a branch of degree at most D is excluded as a useful
nontrivial-witness route by the elementary high-agreement lemma below.

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

The independent exhaustive check `verify_zero_branch.py` verifies all
586 nonzero supported-root candidates and 151,605 pairs for (p,n,D)
=(7,5,1),(11,9,2), including repeated roots. All 2,040 detected
collinearity checks have proportional witnesses and a common agreement
set of size at least n-D. The field-independent proof above, not these
finite checks, establishes the theorem.

## A low-degree moving branch also forces high agreement

The following is an elementary rigidity observation, not a claimed new
general proximity-gap theorem. It does not use differential equations.

Let r_z=f+zg be any received line on n distinct coordinates, with
n>4D. Suppose distinct labels z have chosen degree-at-most-D witnesses
P_z, each agreeing with r_z on at least n-D coordinates. If there are
at least three labels, all P_z lie on one parametrized polynomial line
A+zB with deg A,deg B<=D. Indeed, fix two labels and their interpolated
polynomial line. Every third witness has more than D common agreement
coordinates with the first two, since n-3D>D, forcing polynomial
equality to the interpolated member at that third label.

The received coefficients f,g and the polynomial coefficients A,B
agree together on a fixed set C of at least n-2D coordinates: use the
intersection of the first two witness supports. Outside C, the residual
(f-A)+z(g-B) vanishes for at most one label per coordinate. Thus at most
n-|C|<=2D labels have any selected-witness agreement outside C. At all
other labels the full agreement set is C and has a correlated
explanation. Families of at most two labels are bounded separately.
No characteristic assumption is needed for this lemma.

Apply it to T P_z'=(P_z-F_z)(P_z-G_z), where F_z,G_z are affine in z
and deg F_z<=D. For any witness P_z!=F_z, the equality at each domain
coordinate implies P_z=G_z except possibly at the at most D roots of
P_z-F_z. Thus this witness is within D errors of G_z. The lemma applies
to all such labels, giving a common correlated set of size >=n-2D and
at most max(2,2D) selected full-set failures in this nontrivial family.
Witnesses P_z=F_z already belong to the prescribed codeword branch;
their agreement with G_z need not be rich, so do not silently include
them in the rich-witness conclusion.

At quarter rate, n=4k and D=k-1, the common set has size at least
n/2+2, above the sought agreement 0.49n. Thus a two-branch construction
aimed at that target cannot rely on one branch being a codeword and the
other being the received line. Both branches must evade this reduction,
or the construction must use a different mechanism.
