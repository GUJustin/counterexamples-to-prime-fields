# A planar-incidence gate for proportional fresh words

September 18, 2026. This is a scoped consequence of a primary incidence
theorem. It applies to arbitrary fresh point sets, not only translated
integer grids, but still requires the fixed conic quadratic bank and a
constant received-word ratio on the informative coordinates.

For this model over a prime field, Omega(n) qualifying labels force
d=O(n^(7/15)). More strongly, d>=delta*sqrt(n), for a fixed delta>0,
allows only O_delta(n^(7/8)) labels. Thus a positive constant fraction
of a prime alphabet cannot coexist with a loss comparable to the
capacity margin when that margin is Theta(n^(-1/2)).

## Primary theorem inspected

Sophie Stevens and Frank de Zeeuw, *An Improved Point-Line Incidence
Bound Over Arbitrary Fields*, Theorem 3, page 2 of
[arXiv:1609.06284v4](https://arxiv.org/pdf/1609.06284), published in
*Bulletin of the London Mathematical Society* 49 (2017), 842--858,
[doi:10.1112/blms.12077](https://doi.org/10.1112/blms.12077).

For m points and k lines, with m^(7/8)<k<m^(8/7), their theorem gives

    I(points,lines) = O(m^(11/15) k^(11/15)),

provided m^(-2)k^13 is at most a suitable constant times p^15 in
positive characteristic p. In particular m=k=N gives O(N^(22/15))
incidences when N is sufficiently smaller than p^(15/11). The
applications below have N<=p, so the characteristic condition has
substantial slack. These are the only external incidence facts used.

## Exact coding-to-plane reduction, including multiplicities

Let D be n distinct coordinates in Fp, so n<=p, with p odd. Consider
the fixed bank

    P_theta(X)=theta+X²/theta,   theta in S subset Fp*.

Let E={x in D:g(x)!=0}, and suppose f(x)=c0*g(x) throughout E.
On E put

    U_x=1/g(x),    V_x=x²/g(x).

Agreement with bank theta at label lambda is exactly the point-line
incidence

    (U_x,V_x) lies on l_(theta,lambda),
    l_(theta,lambda): V=-theta² U+theta(lambda+c0).       (1)

A point (U,V) comes from at most two coordinates: U!=0 and V/U=x²
determine x up to sign. Also a geometric line comes from at most two
bank-label pairs. Equal slopes force theta'=theta or theta'=-theta;
within a fixed theta the intercept determines lambda uniquely.
No assumption that S excludes opposite parameters is needed.

Suppose B distinct labels are each supplied with one bank witness
having at least d matches in E. The selected pairs define at least
B/2 distinct lines, each containing at least d/2 distinct plane
points. The plane point set has at most n members. The possible
factors of two are harmless but must not be omitted.

This applies to a proximity gap d=T-A whenever A is the actual
ordinary common agreement of f,g. For any bank word, its matches on
D\E are common matches explained by (P_theta,0), so there are at
most A. A bank witnessing total agreement at least T therefore has
at least d informative matches. No exact core regularity is required
for this implication.

## Omega(n) labels imply a sub-square-root gap

Fix alpha>0 and assume B>=alpha*n. Select a constant multiple of n
distinct geometric lines among those above (at most n of them), each
d/2-rich. Enlarge the plane point set to exactly n distinct points;
doing so cannot destroy incidences. There are enough points in Fp².
The point and line counts are comparable, and the primary theorem
applies because its characteristic expression is O(n^11)<=O(p^11),
whereas p^15 is larger by an unbounded factor.

The lower incidence bound is Omega_alpha(n*d), and the upper bound
is O_alpha(n^(22/15)). Hence

    d=O_alpha(n^(7/15)).                              (2)

In the above-first-order dimension-three regime where
T-3=Theta(sqrt(n)), the source-loss/capacity-margin ratio satisfies

    (d/n)/((T-3)/n)=d/(T-3)=O_alpha(n^(-1/30)).         (3)

This does not approach a positive constant.

## A stronger count when d is a fixed fraction of sqrt(n)

Fix delta>0 and suppose d>=delta*sqrt(n). Let k be the number of
distinct selected geometric lines, so k>=B/2. If k>=n, selecting
n of them would give Omega_delta(n^(3/2)) incidences, contradicting
the balanced O(n^(22/15)) bound for all sufficiently large n.
Therefore k<n eventually.

If k<=n^(7/8), then B<=2n^(7/8) already. Otherwise apply Theorem 3
to the enlarged n-point set and these k lines. Its size conditions
hold, and n^(-2)k^13<=n^11<=p^11 again verifies the characteristic
condition. Since every selected line is at least d/2-rich,

    k*d/2 <= C n^(11/15) k^(11/15),
    k <= C' n^(11/4)/d^(15/4)
      <= C_delta n^(7/8).

Thus in both cases

    B=O_delta(n^(7/8)).                               (4)

The constants depend on delta, not on the bank size, field size, or
the geometry of the fresh set. In particular B=Omega(p), with n<=p,
is impossible under these hypotheses at a constant relative loss.

## Scope and remaining escape conditions

- This is a bound on labels witnessed by the specified conic bank.
  It does not count arbitrary new degree-two witnesses outside it.
- Proportionality must hold on every informative coordinate used to
  infer d matches. A statement about only one small block does not
  control matches supplied on other blocks.
- Any fixed number of blocks with separate constant values of f/g
  has the same asymptotic obstruction, after assigning each witness
  to a block containing a fixed fraction of its informative matches.
- For nonconstant f/g, the incidence equation naturally uses three
  coordinates (1/g,x²/g,f/g) and planes. The planar theorem does not
  apply. Likewise a general quadratic bank with a varying linear
  coefficient introduces another coordinate. Those are concrete
  changes not excluded by this gate.
- The use of n<=p is specific to a prime-field coordinate domain.
  Extension-field domains can violate the characteristic-size
  hypothesis of the primary theorem. No universal binary-versus-prime
  impossibility statement is inferred.

The regular collision-bank theorem has d=Theta(n^(1/4)/log n), well
below (2), so this gate does not contradict it or establish its
optimality. It does identify a mathematical obstruction to reaching
constant relative loss merely by replacing its integer grid with a
different planar fresh set while retaining proportional fresh words.
