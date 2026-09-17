# Several-coordinate far points by a second moment

This strengthens the distance of the far point, at the cost of a weaker
convergence estimate for the nearby fraction. Pure mathematical construction;
no prescribed-domain or fixed-gap claim.

Let w have degree D >= K and let L distinct polynomials of degree <K each
agree with w at exactly D points of a core of size N. Put R=p-N, U=p-1,
d=K-1. Every difference P_i-w is nonzero outside the core. Write c_ij for
the number of outside roots of P_i-P_j, and

    T=d*binom(L,2)-pairs(L*D,N),

where pairs is the balanced minimum sum of pair collisions. Then
sum_{i<j} c_ij <= T and c_ij <= d.

Choose q distinct outside points uniformly and independently choose nonzero
padding directions there. Set f=w globally, g=0 on the core. For fixed z!=0,
let X count pairs (i,S), |S|=r, such that P_i matches f+zg on all padding
positions in S. Then X>0 implies agreement at least A=D+r. Using falling
factorials (x)_a, put

    v_a=binom(r,a)*binom(q-r,r-a)/binom(q,r).

The exact second-moment ratio, averaged over domains and directions, is

    E[X²]/E[X]² = sum_{a=0}^r v_a U^a *
        [1/L + (1/L²) sum_{i!=j} (c_ij)_a/(R)_a].

The a=0 term is v_0. For a>=1 and d>=1, use
(c_ij)_a <= c_ij*(d-1)_{a-1}. Thus the ratio is at most

    B = v_0 + sum_{a=1}^r v_a U^a *
        [1/L + 2T*(d-1)_{a-1}/(L²*(R)_a)].

A falling factorial vanishes when its order exceeds a nonnegative integer.
The d=0 case has all c_ij=0 and the pair term is zero. Paley-Zygmund at
zero gives Pr(X>0)>=1/B. Averaging over all nonzero z yields one choice
of domain and directions with at least ceil(U/B) nearby parameters.
The zero word has exact maximum agreement D: degree bounds the maximum,
and the selected candidates attain D on the core. Consequently it is r/n
outside the nearby radius, and no correlated agreement at A is possible.

## Fixed r asymptotic consequence

Fix rational rho in (0,1), c>H2(rho), and a positive integer r. Write
b=log2 p, ell=log2 b, epsilon=sqrt(log2 ell/ell), and choose

    n ~ sqrt(2)/c * b^(3/2)/sqrt(ell), K=rho*n,
    s=floor(c*n/b), h=ceil((2r+2+epsilon)*b/ell),
    k=K+1, t=k+s, m=t+h, N=m-1, D=t-1, q=n-N.

The anchored binomial-moment construction gives
log2 L >= r*b+Omega(epsilon*b), hence U^r/L ->0. The threshold is
A=D+r=K+s+r, so eta=(s+r)/n~c/b and the zero word is exactly r/n farther.
The balanced core-collision estimate gives 2T/L²=O(h), while d=O(n),
q=Theta(n), and U/(R-r+1)=1+o(1). For fixed r and each a>=1,
v_a=O_r(q^-a), so

    B <= 1 + U^r/L + O_{rho,r}(h/n) = 1+o(1).

Thus J/p ->1 with a far point r coordinates outside, at exact rate rho,
on a polylogarithmic short domain and strictly below Elias. Choosing
c>max(H2(rho),c2*H2(rho)) still makes the numerical prescription o(p).
This proves arbitrarily large FIXED coordinate separation, not constant
relative separation, and does not preserve the earlier exponential
convergence estimate. Growing r requires a separate uniform audit.

## Growing r (audited uniform estimate)

Put a²=(1-rho)*ln(2)/(4rho), r=floor(a*sqrt(ell)), epsilon=ell^-1/4,
and keep h=ceil((2r+2+epsilon)*b/ell). Now log2((m-1)/h)=ell/2+O(1),
so log2 L >= r*b+Omega(epsilon*b). Set tau=2T/L². Then tau/d=O(b^-1/2).
For Z the intersection size of two uniform r-subsets of a q-set,
E[d^Z]=sum_j (d-1)^j*binom(r,j)*(r)_j/(q)_j
<=exp(r²*d/(q-r+1)). Therefore

    B <= 1+U^r/L + (tau/d)*(U/(R-r+1))^r*exp(r²*d/(q-r+1))
      <= 1+b^(-1/4+o(1)).

The exponential is b^(1/4+o(1)), the field-ratio factor tends to one,
and U^r/L is exponentially small. This proves J/p>=1-b^(-1/4+o(1))
with r->infinity and the same leading n and eta. Relative far-point
separation still vanishes. The earlier fixed-r discussion's restriction
on growing r is resolved by this uniform estimate, not by extrapolation.

## Stronger uniform pair cap: final manuscript version

Each two D-element core supports intersect in at least max(0,2D-N).
Consequently c_ij <= e=d-max(0,2D-N), much smaller than d in this regime.
Using that cap directly gives the simpler ratio bound

    E[X²]/E[X]² <= U^r/L + (U/(R-r+1))^r * exp(r²e/(q-r+1)).

The hypergeometric factorial-moment identity proves the last exponential
bound. Now choose r=floor(b^(1/6)), epsilon=ell^-1/4,
h=ceil((3+epsilon)*(r+1)*b/ell). Then
log2((m-1)/h)=ell/3+(log2 ell)/2+O(1), so L>=p^r*2^Omega(epsilon*r*b).
Here e=h-s-1~h, r²e/q=O(ell^-1/2), and the field-ratio factor is
1+o(ell^-1/2). Hence J/p>=1-O(ell^-1/2), with the same leading length,
rate and gap and r coordinate separation. This supersedes the weaker
sqrt(ell) coordinate-separation corollary above. Neither asserts constant
relative separation or a fixed positive gap.
