# The degree-21 square branch survives the present scalar resources

Consider A=G^2 H, with deg_Y G=21, deg_Y H=1, G squarefree. At the binding weight, wt(G)<=21w+6 and wt(H)<=w+12. The exact Newton support bound for contact a is

  NP_A(j)>=g_a(j)=max(0,(a-j)/2,a-12-j).

## Safe integrated allocation

Let b_H be the valuation of the leading coefficient of H. Selecting the doubled roots of G among the roots of A gives

  NP_A(2j+1)<=2 NP_G(j)+b_H.

Thus

  ord Disc(G)>=sum_{j=1}^{20} g_a(2j+1)-20 b_H.

This is an integrated polygon statement, not a pointwise root-slope inference. At a=40 its continuous right side is205, not the tempting approximation Phi_A/4=225. The single H root absorbs an endpoint of the root list.

Coefficient integrality can strengthen that bound. The following exact local models show what is actually attainable at the two relevant contact orders.

## Explicit realizable local polygons

Work over an algebraically closed residue field of characteristic greater than43 and formal parameter t. Choose all constants below nonzero and generically distinct, avoiding the finitely many coincidences of leading root coefficients.

For contact39 take

  G=(Y-c1)(Y-c2) product_{i=1}^6(Y^2-alpha_i t)
                       product_{j=1}^7(Y-beta_j t),
  H=Y-gamma t.

The G root valuations are 0 twice, 1/2 twelve times, and1 seven times. H has root valuation1. Therefore A=G^2H has root valuations 0 four times, 1/2 twenty-four times, and1 fifteen times. Its Newton polygon is exactly g_39: slope1 for fifteen roots, slope1/2 for twenty-four, and slope0 for four. All coefficients satisfy the exact integral Newton support inequalities. Distinct leading coefficients make

  ord Disc(G)=192,
  ord Res(G,H)=13.

For contact40 take

  G=(Y-c) product_{i=1}^6(Y^2-alpha_i t)
                  product_{j=1}^8(Y-beta_j t),
  H=Y-d,

with d distinct from c. The G root valuations are 0 once, 1/2 twelve times, and1 eight times; H has root valuation0. A has valuations 0 three times, 1/2 twenty-four times, and1 sixteen times. Its polygon is exactly g_40, and

  ord Disc(G)=218,
  ord Res(G,H)=0.

These are genuine polynomials over the power-series ring, with monic leading coefficients and nonzero G-discriminant. They independently verify coefficient-level realizability, including the half-integral slopes; no invalid root-count shortcut is used.

## A compatible abstract global profile

Take114187 coordinates of the first local type and147957 of the second. The independently audited rank table gives

  sum R(a)=6802317277834 >= C-1=6802316684344.

The total required G-discriminant order is

  114187*192+147957*218=54178530.

Even with wt(G)=21w exactly, its global degree upper bound is

  21*20*w=55049820,

leaving871290. The required resultant order is1484431, below the bound21w=2752491 for wt(H)=w. The radical GH-discriminant lower order is57147392, below22*21*w=60554802. Thus adding the ordinary pair-resultant and radical-discriminant scalar budgets still does not exclude this profile.

H matches the received symbol at only114187 coordinates in these local models, fewer than w. The high-multiplicity linear-factor pencil argument is therefore not forced by this resource profile.

This is NOT a global construction of A, F, or a universal primary factor. It demonstrates a sharply scoped limitation: the present own-rank inequality plus exact local Newton polygons, individual discriminants, and pair-resultant degree budgets admit this abstract profile. A contradiction must use additional global compatibility or a stronger routing theorem. It cannot follow merely by replacing the repeated discriminant with the discriminant of G and summing these local lower bounds.
