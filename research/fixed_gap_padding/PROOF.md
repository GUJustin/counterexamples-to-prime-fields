# Anchored padding: actual fixed-gap correlated-agreement failure

September 16, 2026. Self-reviewed proof with passing exact finite checks; no independent review or novelty claim. This strengthens
the earlier selected-witness fixed-gap construction. It does not establish
quadratic growth in block length at one fixed gap.

September 17 update: `PRESCRIBED_GAP.md` strengthens the sequence-of-gaps
quantifier below to every sufficiently small rational gap, with the same
leading coefficient and exact fixed rate. The manuscript uses that
stronger proof. The finite construction and earlier parametrization
recorded here remain valid.

## Finite integer seed

Let 1<=k<t<m and let L distinct t-subsets A_i of {1,...,m}, all containing
1, have the same first s=t-k elementary symmetric coefficients. Write

    F_i(X)=prod_{a in A_i}(X-a),
    W(X)=their common part in degrees t,...,k,
    G_i=W-F_i,    deg G_i<k.

All G_i(1)=W(1). The anchored moment pigeonhole gives

    L >= ceil[binom(m-1,t-1) / prod_{j=1}^s R_j],

with the same moment-range bounds R_j used in the manuscript. Restricting
to subsets containing 1 costs only the factor t/m in the numerator.

Choose an integer r with 1<=r<t-k. It will count the padding as a multiple
of the fiber size. Let B grow, and set

    n_B=B(m+r),     k_B=Bk,     A_B=Bt.

These have exactly fixed rate rho=k/(m+r), agreement a=t/(m+r), and gap
eta=(t-k)/(m+r)>0.

## Lift, remove one anchor point, and divide

As in the manuscript's Chebotarev lift, choose an arbitrarily large prime
p for which each X^B-a, 1<=a<=m, splits with distinct roots. Let D_old
be the mB-point union of these fibers with the point X=1 removed. Define

    F_old(X)=[W(X^B)-W(1)]/(X-1),
    P_i(X)=[G_i(X^B)-W(1)]/(X-1).

These are polynomials because every selected G_i has the same value at 1.
Their degrees satisfy

    deg F_old=Bt-1=A_B-1,
    deg P_i <= B(k-1)-1 < k_B,

where a zero numerator is harmless. On D_old, each P_i agrees with F_old
at exactly Bt-1=A_B-1 points: its difference is F_i(X^B)/(X-1).
Distinctness follows from the distinct selected fiber supports.

## Add Br+1 coordinates

Choose m_add=Br+1 new points x_j outside D_old and {1} such that the values
P_i(x_j) are pairwise distinct over i, for each j. There are enough points
when

    p > mB + (k_B-1) binom(L,2) + m_add.

Indeed each nonzero P_i-P_i' excludes at most k_B-1 points. Choose offsets
b_j successively so that the labels

    z_ij=P_i(x_j)-b_j

are all distinct over all i,j. Each prior label excludes at most L choices
of b_j, so p>(m_add-1)L^2 suffices. Define the received line by

    f(x)=F_old(x), g(x)=0                 on D_old,
    f(x_j)=b_j,    g(x_j)=1              on the added points.

At challenge z_ij, P_i agrees at its A_B-1 old points and at x_j. The
collision-free choice makes its agreement count exactly A_B. Hence there
are at least

    L(Br+1) > [rL/(m+r)] n_B

distinct nearby challenges. The direction is nonzero.

All field-size lower bounds can be imposed before using infinitude of
completely split primes. No bound on the least splitting prime is needed.
The coefficient and domain data may depend on B; all fields are prime.

## No correlated agreement, for any challenge

Suppose degree-<k_B polynomials F,G jointly agree with f,g on a set S.
If G=0, no added point lies in S, since g=1 there. The polynomial
F_old-F has degree A_B-1 (because k_B<A_B), so |S|<=A_B-1.

If G is nonzero, it has at most k_B-1 zeros on D_old, and there are only
Br+1 added coordinates. Therefore

    |S| <= k_B-1+Br+1 = B(k+r) < Bt=A_B.

Thus **no pair of codewords has A_B common agreements with f,g**. Every
nearby challenge above is a genuine correlated-agreement failure, as well
as a full-MCA failure. This conclusion does not refer to an arbitrary
selection among persistent good witness lines.

The radius theta=1-t/(m+r) is strictly below the characteristic-based
Elias radius after additionally imposing eta*log_2 p>1. The rate, gap,
and radius are all exactly fixed as B tends to infinity.

## Sharper finite dimension

For k>=2 the candidate degree bound already permits dimension B(k-1).
In that case one may allow 1<=r<=t-k: a nonzero G has common agreement
at most B(k-1+r)<=B(t-1)<Bt. All other steps and field-size conditions
use this smaller dimension without change. This sharpens the finite
coefficients below; the asymptotic statement retains dimension Bk.

## Quantitative coefficient as the gap shrinks

Fix any rational target rate rho in (0,1). Let the seed length m grow
through multiples of its denominator. Choose

    s=floor(c sqrt(m/log_2 m)),
    r=the largest denominator-multiple <=s/2,
    k=rho(m+r),     t=k+s,

where c>0 is fixed and c^2<4H_2(rho). For large m, 1<=r<s and t<m.
The source rate k/m=rho+O(s/m) tends to rho. The anchored moment count
has

    log_2 L >= [H_2(rho)-c^2/4-o(1)] m.

Put eta=s/(m+r). Taking c^2=2H_2(rho) and eliminating m gives, along a
sequence eta tending to zero,

    log_2 [rL/(m+r)] >=
        [H_2(rho)^2/2-o(1)] / [eta^2 log_2(1/eta)].

For each such eta separately, the lifted family has n_B tending to
infinity, exact rate rho, exact gap eta, and at least C_rho(eta)*n_B
nearby challenges with no correlated agreement, where C_rho has the
preceding lower bound. The factor r/(m+r) is asymptotic to eta/2 and
changes its logarithm only by O(log(1/eta)).

Consequently no bound of the form

    c1 * 2^(c2/eta) * n + o(n)

can bound the number of full-MCA exceptions uniformly over prime fields
and domains, even with the remainder specified separately at each fixed
gap. More generally, the logarithm of any universal linear coefficient
must be at least of order eta^-2/log(1/eta) along a sequence of gaps.

The lower-bound coefficient is fixed in B. This does not show Omega(n^2)
exceptions at one fixed gap, or contradict the supplied paper's
polynomial-in-n upper bounds at fixed derivative order.

## General nonzero integer domains and concrete seeds

The finite lemma also holds on any set of m distinct nonzero integers
containing 1: use the splitting field of the corresponding product of
X^B-a. From any integer moment class of L0 supports, averaging point
incidences gives an anchor in at least ceil(t*L0/m) supports. The integer
affine transformation x -> 2(x-anchor)+1 puts the anchor at 1 and avoids
zero everywhere. Scaling substituted locator polynomials by 2^t preserves
monicity and integer coefficients.

The published (64,32,34) class of size 5552914238035 gives an anchored
class of at least 2949985688957. With r=2 and dimension 31B, the fixed rate and gap are
31/66 and 1/22, with coefficient 2949985688957/33.

The integer class underlying the published (157,63,68) certificate has
size at least 28169451256663519418. It gives an anchored class of at least
12200781436007129430. With r=5 and dimension 62B, the rate and gap are 31/81 and 1/27,
and the linear coefficient is 10167317863339274525/27 > 3.76e17.
These coefficients count nearby challenges with no correlated agreement.
The resulting fields grow with B; the M31 alphabet is not retained.
