# Arbitrary fresh words for the conic quadratic bank

2026-09-19. Bounded reassessment of the actual prime-field target.
No field scan, new construction, or universal prime-field obstruction.

**Conclusion.** Changing the fresh grid, even to arbitrary received values,
cannot give superlinear labels at a constant loss-to-capacity-margin ratio
while retaining the existing `Theta(sqrt(n))` bank. Dropping singleton lists
does not change this. Enlarging the same conic bank also cannot retain
`Omega(sqrt(n))` common-core agreement for all its members: every core point
has at most two owners. Arbitrary fresh values lead to point-plane or
point-parabola incidences, so the stronger planar point-line restriction
does not automatically extend to them.

## 1. What was already known, and what is checked here

The bank is

    P_theta(X) = theta + X^2/theta,       theta in Theta subset Fp*,
    L = |Theta|.

The existing [bank budget](SOURCE_GAP_BANK_LIMIT.md),
[proportional-word incidence gate](PLANAR_PROPORTIONAL_PADDING_INCIDENCE_GATE.md),
and [three-dimensional box note](THREE_DIMENSIONAL_BOX_ROUTE_GATE.md) already
record the fresh-incidence budget, the proportional special case, and the
three-coordinate incidence equation, respectively. They are not new results
of this note. The reassessment below makes the broader common-core ceiling
explicit, identifies the exact arbitrary-value geometry, and relates its
collinearity parameter to ordinary common agreement.

Let `D subset Fp` have `n` distinct coordinates, let `f,g` be arbitrary
received words, and set

    A = CA_3(f,g),       T>A,       d=T-A,
    E = {x in D : g(x) != 0},      e=|E|.

Select one bank witness for each of `B` distinct labels whose word
`f+lambda g` has agreement at least `T`. The known exact budget is

    B d <= L e <= L n.                                      (1)

It requires neither proportional words, a grid, singleton lists, nor a
regular core. Matches on `g=0` give a simultaneous explanation `(P_theta,0)`
and hence contribute at most `A`. On `E`, each fixed `(theta,x)` determines
one label. This is the complete reason for (1).

In the dimension-three first-order/Johnson window, `T-3=Theta(sqrt(n))`.
A positive constant loss/capacity ratio therefore means
`d/(T-3)>=c>0`, so `d=Omega(sqrt(n))`. With the existing retained
`L=O(sqrt(n))` bank, (1) gives `B=O(n)` in every characteristic.
This also bounds an asserted individual-source separation: if the chosen
endpoints have agreement at most `A_src<T`, then `CA<=A_src` and
`d=T-CA>=T-A_src`. Thus a gap-scale individual-source loss implies the
gap hypothesis used in (1), even without exact equality of these profiles.

## 2. The bank size is not merely an outsider-list convenience

For any coordinate `x` and any assigned value `v`, bank owners solve

    theta^2-v theta+x^2=0.                                 (2)

There are at most two distinct owners. Therefore on any common graph
with `n_0` coordinates, if `L_0` bank members each have at least `a` matches,

    L_0 a <= 2 n_0.                                        (3)

In particular a gap-scale common core, `a>=c sqrt(n)` with `n_0<=n`, forces
`L_0=O_c(sqrt(n))` for this entire conic bank, regardless of its arithmetic
parameterization. Arbitrary core multiplicities cannot be introduced while
retaining this coefficient conic.

The actual translated and collision cores already have `n_0=Theta(L^2)`
and largest core agreement `Theta(L)`. In the asymmetric construction,
`L=t^2+s^2`, while `A=t^2+2s^2+2t-3=Theta(L)` and `n=Theta(s^4)`.
These geometric and source-agreement constraints precede the exclusion of
nonbank witnesses. Allowing larger lists does not shrink those cores or
permit `L/sqrt(n)` to grow.

Equation (3) is a restriction on a *shared core*, not on every possible
received pencil using a large conic bank. A larger bank can avoid it only
if most relevant witnesses have `o(sqrt(n))` matches on that common graph
and obtain their threshold agreements on label-dependent fresh supports.

## 3. The exact arbitrary-value incidence mapping

For `x in E`, define

    (U_x,V_x,W_x) = (1/g(x), x^2/g(x), f(x)/g(x)).

Then agreement is exactly

    theta^2 U_x + V_x - theta W_x = theta lambda.            (4)

Thus coordinates are points in `Fp^3`, and selected bank-label pairs are
planes with normals on the conic `(theta^2,1,-theta)`. Distinct pairs give
distinct planes, since the coefficient of `V` is normalized to one.
A spatial point represents at most two coordinates: `V/U=x^2` determines
`x` up to sign, and `U != 0`. Consequently the geometric incidence count
is at least `B d/2`.

Equivalently, map a selected pair to the point `(z,w)=(theta,theta lambda)`.
Each coordinate gives the genuine parabola

    w = U_x z^2 - W_x z + V_x,       U_x != 0.               (5)

Identical parabolas have multiplicity at most two. The selected point set
has exactly `B` points, with distinct ratios `w/z=lambda`. These
realizability and distinct-label conditions are part of the problem; an
arbitrary multiset of curves and points is not automatically an RS example.

If `W_x` is constant, (4) restricts to the old planar line problem. More
generally a relation `W=aU+bV+c` corresponds to
`f=a+bX^2+c g` on this block; subtracting the even quadratic explains the
same planar reduction. No such relation is supplied by arbitrary `f/g`.
Equation (5) is quadratic, so a planar point-line theorem cannot simply be
applied to it as if the extra received-value coordinate disappeared.

## 4. Common agreement controls the spatial collinearity parameter

Consider a spatial line

    (U,V,W)=(u_0,v_0,w_0)+z(a,b,c),
    Delta = a v_0-b u_0.

If `Delta=0`, the ratio `V/U` is constant on its points with `U!=0`.
At most two distinct RS coordinates map there. If `Delta!=0`, substituting
`V=x^2 U` gives the simultaneous explanations

    g(x) = (a x^2-b)/Delta,
    f(x) = ((a w_0-c u_0)x^2+c v_0-b w_0)/Delta.             (6)

Both are even quadratics. Hence at most `A` coordinates lie on this
spatial line. Since `A>=3` when `n>=3`, the maximum number of distinct
collinear spatial points is at most `A` in all cases.

Rudnev's primary point-plane theorem, by duality, gives

    I(P,Pi) = O(|Pi| sqrt(|P|) + k_col |Pi|)

when `|P|<=|Pi|`, `|P|=O(p^2)`, and the characteristic is odd.
Here `|P|<=n<=p`, `k_col<=A`, and `|Pi|=B`. Thus for `B>=n`, (4) yields
only

    d = O(sqrt(n)+A).                                     (7)

This bound allows the desired `d=Theta(sqrt(n))` when `A=Theta(sqrt(n))`.
It does not give the planar power saving or exclude superlinear labels
for a genuinely larger, differently used bank.
[Rudnev, Theorem 3, arXiv:1407.0426v5](https://arxiv.org/pdf/1407.0426v5).

The primary point-parabola theorem also applies to (5), since `B<=p`
verifies its condition `B << p^(15/13)`. It gives

    B d << B^(15/19) n^(15/19) + B^(23/19) n^(4/19) + n.

At `B=Theta(n)` its leading upper bound has order `n^(30/19)`, larger
than the required `n^(3/2)`. Therefore this application does not close
the target either. This is an applicability check, not a claim that the
inspected theorem is an optimal bound for the special configuration (5).
[Mohammadi–Pham–Warren, Theorem 1.3, arXiv:2111.04072v2](https://arxiv.org/html/2111.04072v2).

For comparison, the existing proportional-word result uses
`I(P,L)<<m^(11/15)r^(11/15)` for
`m^(7/8)<r<m^(8/7)` and `m^(-2)r^13<<p^15`. In the balanced prime-field
range `m,r=Theta(n)<=O(p)`, its hypotheses hold and its exponent is below
`3/2`. This explains precisely why that planar argument is stronger than
(7), and why its dimensional hypothesis matters.
[Stevens–de Zeeuw, Theorem 3, arXiv:1609.06284v4](https://arxiv.org/pdf/1609.06284v4).

## 5. Constructive decision

No new fresh-grid search is justified for the current retained bank.
Two mathematically different changes remain:

* Keep the conic family but abandon a gap-scale common core for most
  witnesses. A candidate must produce many rich planes in (4), retain
  `V/U=x^2` with at most two coordinates per ratio, use distinct labels,
  and separately bound both endpoint agreement and ordinary CA.
* Change the coefficient family so that common-core nodes can have growing
  bank multiplicity. The [existing quadratic-rich-core audit](PRIME_QUADRATIC_RICH_CORE_INCIDENCE_GATE.md)
  leaves a finite-field incidence window for larger banks, but does not
  supply an actual prime-field construction in that window.

Dropping singleton-list requirements is compatible with either route,
but alone accomplishes neither. No explicit two-parameter prime-field
geometry with `L/sqrt(n)->infinity` and gap-scale common-core agreement
was obtained in this reassessment, so no bank scan or computational job
was started.
