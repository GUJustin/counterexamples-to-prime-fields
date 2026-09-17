# Padding with collisions: a finite-field lower bound

September 17, 2026. Mathematical existence bound. This replaces the
requirement that all labels be distinct by averaging their union.
No claim of whole-line uniqueness or explicit offsets is made.

## General finite lemma

Let D_old subset F_p have N points. Let w be a polynomial of degree A-1,
and let P_1,...,P_L be distinct polynomials of degree<K<A, each agreeing
with w at exactly A-1 old points. Let D bound every nonzero pairwise
difference degree (one may use D=K-1). For q<=p-N with

    K-1+q < A,

one can add q distinct coordinates and choose a received line equal to
w on old coordinates, with direction 0 there and 1 on new coordinates.
No pair of degree<K codewords has A common agreements with its two
coefficient words. Put R=p-N. Define pairs(h,N) as the minimum of
sum_x binom(h_x,2) over N nonnegative integer occupancies summing to h.
With h=aN+b, 0<=b<N, it equals N*binom(a,2)+b*a. Put

    T = D*binom(L,2) - pairs(L*(A-1),N),
    M = L^2*R/(L*R+2*T).

Then T>=0, and some such line has at least

    ceil( p * (1 - (1-M/p)^q) )

nearby labels at threshold A. This includes all candidates sharing a
label or one candidate agreeing on multiple new points.

Proof: for each available x, let r_{x,v} count candidates with value v,
and let s_x be the number of distinct values. Each pair has at most D
roots of its difference; their old common agreements account for at
least the displayed balanced-pair count. Thus

    sum_available_x sum_v r_{x,v}^2 <= L*R+2*T.

Cauchy--Schwarz first at each x and then across x gives average s_x>=M.
Choose the q available points with largest s_x. Their average is >=M.
Choose each padding offset b_j independently uniformly in F_p. The
image at that point, translated by -b_j, hits any fixed label with
probability s_x/p. Hence the expected size of the union of labels is

    p * (1-product_j(1-s_{x_j}/p))
      >= p * (1-(1-M/p)^q)

by arithmetic-geometric mean. Some choice attains its ceiling.
At every label in this union, one P_i has its A-1 core agreements
and at least one new agreement. If a common direction polynomial is
zero, joint agreement is at most A-1 by the degree of w-F; if it is
nonzero, it is at most K-1+q<A. This proves actual ordinary correlated-
agreement failure for every nearby label, not just selected-witness
inconsistency. T>=0 follows by counting actual pair roots; M<=p follows
from the actual evaluation images.

Dropping the old-incidence savings gives the simpler valid choice
M=L*R/(R+(L-1)*D). Thus p on the order of L*D, rather than L^2*D,
already allows a constant fraction of qL distinct labels whenever
qL is at most a constant times p. No actual image or offset search
is required for an existence certificate.

## Interval seed specialization (B=1)

An integer moment class of L0 t-subsets of m consecutive points,
matching moments1..s=t-k, has degree<k candidates. Some anchor lies
in at least L=ceil(t*L0/m) supports. Remove that coordinate and divide
by its linear factor, giving

    N=m-1, K=k-1, A=t, D=k-2.

Take q=s+1. Then n=m+s and exact gap q/n, while K-1+q=A-1.
The Gram ellipsoid count already audited in the manuscript supplies L0.
The seed nodes remain distinct for p>m; integer polynomial identities
survive reduction, and distinct supports imply distinct candidates.
The bound is independent of finding or enumerating the selected class.

## Stronger short-domain asymptotic

Fix rational rho in (0,1), H=H_2(rho), and b=log_2 p. For every large
prime p choose n a denominator multiple with n=(2/H+o(1))*b, and put

    s=floor(2*(1-epsilon_b)*sqrt(b/log_2 b)),
    m=n-s, k=rho*n+1, t=k+s,

where epsilon_b tends to zero slowly enough, for example
sqrt(log_2(log_2 b)/log_2 b) for sufficiently large b. The anchored
integer moment bound gives

    log_2 L >= m*H_2(t/m) - (s^2/2)*log_2(m/s)
                 - O_rho(s^2+s*log m+log m)
            >= b + Omega(epsilon_b*b).

The rounding and entropy corrections are absorbed by epsilon_b*b.
Thus L/p tends to infinity. Apply the finite lemma at B=1 with
N=m-1, K=rho*n, A=t, q=s+1, D=K-1. The old-incidence savings yield

    2T/L^2 = D-(A-1)^2/N+o(1)
            = (rho*(1-rho)+o(1))*n.

Since R/p tends to one and R/L tends to zero,
M/p=(1+o(1))/(rho*(1-rho)*n). Also q/n tends to zero, so expansion of
the exact union bound proves

    eta=(A-K)/n=(H+o(1))/sqrt(b*log_2 b),
    J >= (H/(rho*(1-rho))-o(1))*p/sqrt(b*log_2 b).

The rate is exact, n=(2/H+o(1))*b=o(p), and every nearby parameter
has no ordinary correlated agreement at threshold A. Strict Elias
holds since eta*log_2 p tends to infinity. Whole-line uniqueness is
not asserted. This improves both the gap and the bad-label count over
the existing fixed-r construction with gap Theta(1/log p) and count
Omega(p/log p). The gap still shrinks; no fixed-gap superlinear
result follows.

## Exact finite certificates

verify_average_padding.py uses the existing exact Gram ellipsoid bound,
anchor averaging, balanced pair arithmetic, the rational union formula,
Lucas--Lehmer primality and integer strict-Elias checks. Outward rational
logarithm intervals certify the following lower bounds on
log_2(J/[n*2^(H_2(K/n)/eta)]) at c1=c2=1:

  prime          n     K     A       excess bits greater than
  2^31-1         72    12    15       6.73559
  2^61-1         155   35    40       27.01590
  2^127-1        273   70    76       78.16602
  2^521-1        1065  381   393      422.98809

These are existence certificates on padded interval domains, not
prescribed subgroups or protocol-security estimates. Finite discovery
scanned 5,404,578 parameter triples; it is not a global optimality proof.
Two F17 fixtures exhaust all 5,202 padding-offset tuples and 167,042
codeword pairs, independently checking union expectations and no
correlated agreement. All pass under the 384 MiB watchdog.
