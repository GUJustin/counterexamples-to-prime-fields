# Slowly vanishing separation at nearby density tending to one

September 17. Proof audit of a new parameter choice for the existing
multi-match padding lemma. Not a new padding mechanism.

Fix rational rho in (0,1), c>H_2(rho), and write b=log_2 p. Let s=s(b)
be integer valued with s→infinity and s^(5/3) log_2 b=o(b). Put

    n=s*b/c+O(1), through denominator multiples for rho,
    K=rho*n, r=floor(s^(1/3)),
    h=ceil(3(r+1)b/log_2 s), D=K+s,
    t=D+1, m=t+h, N=m-1=D+h, q=n-N.

All asymptotics below hold along every function satisfying those conditions.
We claim the multi-match lemma yields

    eta=(s+r)/n~c/b,
    J/p >= 1 - (3c/(1-rho)+o(1))/log_2 s,
    exact outside separation = r/n = kappa*eta,
    kappa=r/(s+r)~s^(-2/3), r→infinity.

## Support and moment count

Here h/n=O(s^(-2/3)/log s)→0, and

    log_2(N/h)=(2/3)log_2 s+log_2 log_2 s+O_(rho,c)(1).

Hence log_2 binom(N,h)>=h log_2(N/h)>=(2-o(1))*r*b.
More precisely the lower bound is 2(r+1)b plus a term eventually
positive of order (r+1)b loglog s/log s.
The first s integer binomial moment ranges have total logarithm at most
O(s^2 log m)=O(s^2 log b)=o(r*b), since s^(5/3)log b=o(b).
Thus an anchored common-moment class has

    log_2 L >= (2-o(1))*r*b,
    (p-1)^r/L <= 2^(-(1-o(1))*r*b).

The rough moment bound suffices; no growing-dimensional concentration
estimate is used. The schedule condition implies s=o(b^(3/5)), so
log m=O(log b) and n is polynomial in b.

## Pair collisions and nearby count

Since h=o(n), eventually 2D>N and the uniform outside pair cap is

    e=(K-1)-(2D-N)=h-s-1~h.

The last equivalence follows from b/(s^(2/3)log s)→infinity, which is
implied by the schedule condition. Also q~(1-rho)n. Therefore

    r^2 e/(q-r+1) = (3c/(1-rho)+o(1))/log_2 s.

The finite-field correction ((p-1)/(p-N-r+1))^r is
1+o(1/log s), since n,r are polynomial in b and p=2^b.
Substitution in the already proved multi-match second-moment bound gives
E[X^2]/E[X]^2 <= exp((3c/(1-rho)+o(1))/log_2 s).
Inversion, averaging over p-1 labels, and exp(-x)>=1-x give the stated
nearby fraction. The degree-D global word has exact maximum agreement
D, so the far point is r coordinates outside and no correlated agreement
exists at threshold A=D+r. Elias follows from eta*b→c>H_2(rho).
If c>c2*H_2(rho) as well, the numerical prescription is o(p).
Every affine codeword graph contains at most floor((n-A+r)/r)=o(n)
selected witnesses, by the quantitative incidence lemma.

## Consequence for any prescribed vanishing buffer

Given any epsilon(p)>0 tending to zero, take

    s=floor(min(epsilon(p)^(-3/4), b^(1/4))).

Then s→infinity and s^(5/3)log b=o(b). Moreover
kappa~s^(-2/3)>epsilon(p) eventually, while J/p→1.
Thus requiring a far point at least epsilon(p)*eta outside does not
prevent the near-total failure, for ANY prescribed vanishing epsilon.
This parameter choice uses a vanishing epsilon. The later cubic-domain
construction in ../cubic_domain_warp/ closes the fixed-positive-relative-
buffer question, with every nonzero parameter nearby at fixed rate.
For an explicit uncomplicated choice, s=floor(log_2 b) gives
n~b log_2 b/c, kappa~(log_2 b)^(-2/3), and
J/p>=1-O(1/log_2 log_2 b), with r~(log_2 b)^(1/3).

These are a quantitative parameter consequence of existing lemmas.
The arbitrary-buffer qualitative consequence could also be obtained
by a careful diagonal argument from fixed-fraction families; the new
formulas make lengths, number of missing coordinates, and convergence
explicit. Finite computation cannot prove these asymptotics.

## Actual global lists remain large

On the same core N=D+h, take A=D+r subsets and match s+r integer
moments. The complement size is h-r~h; its support logarithm remains
(2-o(1))*r*b. The moment cost O((s+r)^2 log b)=o(rb). Subtracting each
monic locator from the common degree-A received polynomial leaves a
candidate of degree below K. Thus the actual global maximum list is
at least p^((2-o(1))*r)>p, after extending the received word over the
padding. The slow-separation result is not an actual-list-size
separation. The parameter checker also verifies sufficient support
versus moment bit inequalities for these off-line lists.

## Faster density when one missing coordinate suffices

If s^2 log_2 b=o(b), keep n=sb/c+O(1), take r=1 and
h=ceil(2b/log_2 s). The support log is >=(2-o(1))b and moment cost
o(b), so L/p→infinity. The collision residual is asymptotic to h,
thus M/p~1/h. Far-point padding gives

    J/p >=1-exp(-((1-rho)/(2c)-o(1))*s*log_2 s),
    kappa=1/(s+1).

The 1/p loss is negligible because s log s=o(b). This is also a
parameter consequence of the existing lemma, complementary to r→infinity.
The exact parameter audit checks support/moment separation and q/h
scaling for this variant on the same slowly growing schedules.
