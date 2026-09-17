# Dense nearby-parameter sets by choosing the padding direction

September 17, 2026. Self-audited proof with passing exact finite check; extends AVERAGED_PADDING.md.

## Removing the padding-size restriction

Keep the core assumptions and image bound M of the averaged-padding
lemma, but drop K-1+q<A. Let n=N+q and require

    binom(n,A)*p^q < p^(A-K)*(p-1)^q.                 (1)

For ANY fixed q distinct padding points, there are nonzero direction
values g_j such that every nonzero polynomial G of degree<K agrees
with g (zero on the core) on fewer than A coordinates.

Proof: choose the g_j independently uniformly in F_p^*. Fix an A-subset
S with r old and u=A-r new coordinates. A nonzero G vanishing on r>=K
old points is impossible. If r<K, the vector space of G vanishing on
those points has dimension K-r. Its evaluations on the u new points
occupy at most p^(K-r) vectors. Thus the probability of a matching G
is at most

    p^(K-r)/(p-1)^u
      =p^(K-A)*(p/(p-1))^u
      <=p^(K-A)*(p/(p-1))^q.

A union bound over at most binom(n,A) supports gives probability<1
by (1). Supports with u=0 cannot have a nonzero G since A>K.
No independence between different supports is used.

Now choose padding coordinates with largest candidate evaluation images,
fix any such good g, and independently choose uniform offsets f_j.
For each coordinate, labels (P_i(x_j)-f_j)/g_j are uniform translates
of a scaled image, with the same cardinality s_x. The averaged union
bound J>=ceil(p*(1-(1-M/p)^q)) is unchanged. Every label in this union
is nearby. Joint witnesses with nonzero G have fewer than A agreements
by construction; G=0 has no new agreements (g_j nonzero), and w-F has
degree A-1 on the core. Thus there is no ordinary correlated agreement
at threshold A. Multiple nearby candidates are allowed.

## A constant fraction of all parameters

Fix rational rho<beta<1. Put alpha=rho/beta, H=H_2(beta), b=log_2 p.
Choose n through common denominator multiples with n~2b/(alpha*H),
m=alpha*n, K=rho*n, k=K+1, and

    s=floor(2*(1-epsilon_b)*sqrt(b/log_2 b)), t=k+s,
    N=m-1, A=t, q=n-m+1, d=K-1,

where epsilon_b=sqrt(log_2(log_2 b)/log_2 b), for large b.
The anchored integer moment count gives

    log_2 L >= m*H_2(t/m) -(s^2/2)*log_2(m/s)
                    -O_rho,beta(s^2+s*log m+log m)
             >= b+Omega(epsilon_b*b),

so L/p tends to infinity. All parameters satisfy 1<=k<t<m<p for
large p. The balanced old-support savings give

    2T/L^2 = (rho*(1-beta)+o(1))*n,
    M/p = (1+o(1))/(rho*(1-beta)*n).

Also log_2 binom(n,A)<=n=O(b), whereas (A-K)*log_2 p=(s+1)b
is Theta(b^(3/2)/sqrt(log b)); hence (1) holds eventually.
It follows that

    n = (2*beta/(rho*H_2(beta))+o(1))*log_2 p,
    eta = (rho*H_2(beta)/beta+o(1))/sqrt(b*log_2 b),
    J/p >= 1-exp(-(beta-rho)/(rho*beta*(1-beta)))-o(1).

Rate rho is exact; n=o(p); strict Elias holds since eta*b tends to
infinity. The selected evaluation domain is a punctured integer core
plus added points, not a prescribed subgroup. Every nearby parameter
has no ordinary correlated agreement, because no common pair exists
at all at the threshold.

In particular, for every fixed rational rho in (0,1) and every fixed
delta>0, choose rational beta sufficiently close to 1 that
exp(-(beta-rho)/(rho*beta*(1-beta)))<delta. For every sufficiently large
prime p, some logarithmic-length code and line then have at least
(1-delta)*p nearby parameters, at gap Theta_rho,delta(1/sqrt(b log b)),
with no ordinary correlated agreement. This is a shrinking-gap theorem;
it does not resolve the fixed-gap superlinear target. The constants
in length/gap deteriorate as delta tends to zero.

Finite check: F17,N6,K2,A4,q4,n10. The direction union bound is
30345/32768<1; direction(1,1,1,2) succeeds. All83521 offset tuples
and all83521 codeword pairs are exhausted. Union bound guarantees10
nearby labels; maximal selected union has12. Maximum joint agreement3.
