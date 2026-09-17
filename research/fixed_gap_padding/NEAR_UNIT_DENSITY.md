# Nearby density tending to one at reciprocal-logarithmic gap

September 17, 2026. Uses the final far-point construction in FAR_POINT_PADDING.md.

Fix rational rho in (0,1) and a real C>H_2(rho). Write b=log_2 p,
ell=log_2 b. For every sufficiently large prime p, choose n a denominator
multiple for rho with

    n=(sqrt(2)/C)*b^(3/2)/sqrt(ell)+O(1), K=rho*n,
    s=floor(C*n/b), h=ceil((4+epsilon_b)*b/ell),
    k=K+1, t=k+s, m=t+h, N=m-1, q=n-N,

where epsilon_b=sqrt(log_2 ell/ell). All dimensions and support sizes
are integral; eventually 1<=k<t<m<n<p and q>0. The seed uses the
m-point integer interval and t-subsets containing a common anchor.

## The seed list exceeds the field size

Counting missing h-subsets, the number of anchored supports is
binom(m-1,h). Since m~rho*sqrt(2)/C * b^(3/2)/sqrt(ell),

    log_2((m-1)/h) = ell/2 + (log_2 ell)/2 + O_rho,C(1).

The elementary bound binom(u,h)>=(u/h)^h gives

    log_2 binom(m-1,h) >= (2+epsilon_b/2)*b-O_rho,C(b/ell).

Matching s binomial moments uses at most a product of ranges whose
logarithm is

    (s^2/2)*log_2(m/s)+O(s^2+s*log m)
      = b+O_rho,C(b/ell+sqrt(b*ell)).

Here s=(sqrt(2)+o(1))*sqrt(b/ell), and m/s=(rho/C+o(1))*b.
The error is o(epsilon_b*b). Therefore some anchored moment class
has log_2 L >= b+Omega(epsilon_b*b), and L/p tends to infinity.
Remove its anchor and divide by the corresponding linear factor.
The resulting L polynomials have degree<K and exactly A-1 old
agreements, for A=t.

## Images and a far point

Put d=K-1 and T=d*binom(L,2)-pairs(L*(A-1),N). Since A-1=K+s
and N=K+s+h,

    d-(A-1)^2/N = h-s-1-h^2/(K+s+h) = (1+o(1))*h.

Balanced occupancies imply 2T/L^2=(1+o(1))*h, and the image bound
M=L^2(p-N)/(L(p-N)+2T) satisfies M/p=(1+o(1))/h.
Apply the far-point padding lemma with f=w globally and independent
nonzero direction values on the padding. No direction union bound is
needed. The parameter-zero word has exact distance (n-A+1)/n. The
strict Elias condition follows from eta*b->C>H_2(rho).

## Result

Choose a direction by multiplicative averaging of the difference images
in F_p^*. No pair of degree<K codewords has A joint agreements because
even f=w alone has at most A-1 agreements with every such codeword.
Moreover 1-x<=exp(-x) gives

    J >= (p-1)*(1-exp(-q*M/(p-1))),
    q*M/(p-1) = ((1-rho)/(2*sqrt(2)*C)+o(1))*sqrt(b*ell).

Thus every sufficiently large prime admits exact-rate-rho codes with

    n=(sqrt(2)/C+o(1))*b^(3/2)/sqrt(log_2 b),
    eta=(C+o(1))/b,
    J/p >= 1-exp(-((1-rho)/(2*sqrt(2)*C)-o(1))*sqrt(b*log_2 b)),

strictly below Elias and with no ordinary correlated agreement.
The loss (p-1)/p is absorbed in the o(1) exponent since 1/p is much
smaller than exp(-Theta(sqrt(b*ell))). The nearby fraction tends to one;
this is stronger than merely
choosing an arbitrarily high fixed fraction. It does not say that all
p parameters are nearby. Length is polylogarithmic in p, hence n=o(p).
The gap still shrinks, so the fixed-gap superlinear target remains open.

For fixed c1,c2 and C>max(H_2(rho),c2*H_2(rho)), the proposed bound is
c1*n*2^(c2*H_2(rho)/eta)=p^(c2*H_2(rho)/C+o(1))=o(p), whereas J/p->1.

Exact finite checks: verify_near_unit_density.py passes five Mersenne
prime fixtures at rate1/2, with b521,1279,2203,3217,4423. The first
three have (n,K,A)=(2800,1400,1411),(10068,5034,5050),(21940,10970,10990)
and nearby-density lower bounds0.99485642,0.99987751,0.99999545.
Finite checks use max(box anchored count, anchored Gram count), exact
direction and Elias inequalities, Lucas-Lehmer primality and a dyadic
downward image bound with a32-term positive binomial sum. The raw box
bound alone does not exceed p in the b521/1279 fixtures; this is why
the verified Gram refinement is used. No such finite threshold is
needed for the all-sufficiently-large-prime asymptotic proof.
