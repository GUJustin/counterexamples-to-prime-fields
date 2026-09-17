# Prescribing every sufficiently small rational gap

September 17, 2026. Strengthening of the existing anchored-padding
theorem: the coefficient lower bound holds at every sufficiently small
rational gap, not only along a sequence. This does not improve its
asymptotic order or make the count superlinear at one fixed gap.

## Flexible finite padding

Retain the integer seed m,k,t,L and the common anchor from PROOF.md.
For any integers B,n,K with

    q=n-mB+1 >= 1,
    K >= B(k-1),
    K-1+q < Bt,

the same proof gives length n, dimension K, threshold Bt, and Lq
distinct nearby labels with no ordinary correlated agreement.
Candidates have degree at most B(k-1)-1. A zero direction gives at
most Bt-1 common agreements, and a nonzero direction gives at most
K-1+q. The latter inequality also implies K<Bt. Prime-size conditions
are unchanged after replacing the old dimension and padding count by
K and q. Arbitrarily large splitting primes give n=o(p) and strict
Elias. No prime-fiber rigidity hypothesis is needed.

## All small rational gaps at an exact rational rate

Fix rational 0<rho<1 and H=H_2(rho). For any sufficiently small rational
eta>0, put a=rho+eta and choose

    m=floor(H/(eta^2 log_2(1/eta))),
    t=ceil(a*m/(1-eta/2)),
    k=floor(rho*t/a),
    s=t-k.

Then m tends to infinity, eta*m tends to infinity, and

    t/m -> rho,  s=(1+o(1))*eta*m,
    a*m < t < a*m/(1-eta),
    1 <= k < t < m.

The rounding error in t is at most one, whereas the difference between
the two displayed upper targets is of order eta*m, which diverges.
All these conclusions hold as eta approaches zero through arbitrary
rationals; there is no denominator restriction.

Among the t-subsets of {1,...,m} containing 1, match the first s binomial
moments. Their ranges are bounded by t*binom(m,j)+1. The standard
factorial estimate gives

    log_2(number of moment vectors)
      <= (s^2/2)*log_2(m/s) + O(s^2+s*log m)
       = (H/2+o(1))*m.

Meanwhile log_2 binom(m-1,t-1)=(H+o(1))*m. Thus an anchored class has
L >= 2^{(H/2-o(1))*m} distinct supports, with common locator
coefficients in degrees t,...,k.

Let B grow through multiples making n=Bt/a and K=rho*n integers;
this is possible for every fixed rational eta, regardless of its
denominator. Set q=n-mB+1. Then

    K >= Bk >= B(k-1),
    q>0,
    K-1+q = B*((1+rho)*t/a-m) < Bt.

The final inequality is exactly t < a*m/(1-eta). Flexible padding
therefore gives exact rate rho and exact gap eta at all these lengths.
Its nearby-label count is

    Lq > C_rho(eta)*n,
    C_rho(eta)=(1-a*m/t)*L.

Since 1-a*m/t=(1+o(1))*eta/2, its logarithm costs only O(log(1/eta)).
Consequently, uniformly as rational eta tends to zero,

    log_2 C_rho(eta)
      >= (H^2/2-o_rho(1))/(eta^2 log_2(1/eta)).

This is an all-small-rational-gap theorem. Each eta has its own fixed
integer seed and its own unbounded sequence of B and splitting primes.
There is no uniform bound on the least length or field size.

## Checks and limits

verify_prescribed_gap.py checks the exact rational inequalities and
integer moment bounds for 15 parameter choices at rates 1/4,1/2,3/4.
Its two prime-field fixtures have (p,n,K,A)=(1009,21,5,10) and
(14449,42,10,20), exact rate and gap both 5/21, and 8 and 14 distinct
nearby labels. The global common-agreement bounds are 9 and 19.
These are mechanism checks; they do not demonstrate the asymptotic
coefficient or prove splitting-prime infinitude.

The whole construction remains linear in n at each fixed gap. It does
not control the global maximum list size and does not improve a
prescribed-code or better.codes benchmark.
