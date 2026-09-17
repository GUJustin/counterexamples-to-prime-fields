# Prime-field lines at logarithmic block length

September 16, 2026. New consequence of the paper's existing moment and
rational-line lemmas. No novelty claim beyond this manuscript is made.

Fix rational 0<rho<1, put H=H_2(rho), and fix an integer r>=2.
For every sufficiently large prime p, let b=log_2 p, set

    a=(r-1)(r+2)/2,
    n=(b+(a+2)log_2 b)/H + O_rho(1),

rounding upward to a multiple of the denominator of rho. Put k=rho*n,
t=k+r, eta=r/n. There is a received line over F_p on the interval
{0,...,n-1}, with no correlated agreement at t, having at least

    (H/(rho(1-rho))-o(1)) * p/log_2 p

nearby labels for RS dimension k. Every parametrized codeword line
contains at most floor((n-k)/r) selected witnesses. The radius is
strictly below the characteristic-based Elias radius.

Consequently, for every c1,c2>0, choose integer r>max(1,c2). For every
sufficiently large prime p these length-Theta(log p) examples violate
c1*n*2^(c2*H/eta) as a finite selected-witness line threshold.
This is not a fixed-gap statement: eta=(rH+o(1))/log_2 p.

## 1. A bank larger than the field

Apply the finite-list lemma with source dimension k+1 and s=r-1.
Its t-subsets give distinct polynomials of degree <=k with exact
agreement size t. Each binomial-moment range satisfies R_j=O_r(n^(j+1)),
so product R_j=O_r(n^a). At fixed rho,r, the elementary entropy lower
bound binom(n,t)>=2^(n H_2(t/n))/(n+1) implies

    binom(n,t)>=c_(rho,r)*2^(Hn)/n.

Indeed t/n=rho+r/n and H_2 is continuously differentiable near rho.
Thus a common-prefix bank has

    N >= c'_(rho,r)*2^(Hn)/n^(a+1) >= c''_(rho,r)*p*b.

In particular N/p tends to infinity. All constructions remain valid
modulo p>n; no equality between integer classes and the entire modular
list is needed.

## 2. Subtract shared-support roots from collisions

Select exactly N members of such a bank. Let I_x be their support
incidences, so sum_x I_x=Nt. Each pair difference has degree at most k
and already has a root at each coordinate of the two supports'
intersection. Across admissible poles outside the domain, its total
root budget is at most k-|A intersection B|. Therefore the sum of
collision pairs over all Q=p-n admissible poles is at most

    B = k*binom(N,2)-sum_x binom(I_x,2)
      <= [N^2*(k-t^2/n)+N*(t-k)]/2.

The last inequality is Cauchy-Schwarz on the incidences. All these
counts concern actual distinct polynomials and supports, so no
negative root budget can occur. For our parameters k-t^2/n>0 eventually.

Some pole has at most B/Q collision pairs. Applying Cauchy-Schwarz
to its value multiplicities gives at least

    NQ / [Q + N*(k-t^2/n) + (t-k)]

values, each a distinct label on the rational received line. Here
k-t^2/n=rho(1-rho)n-2rho*r-r^2/n. Since N/p tends to infinity,
the label count is (1-o(1))*p/[rho(1-rho)n], as claimed.
The original rational-line lemma proves the absence of correlated
agreement and the stated concurrency bound.

## 3. Elias and the proposed threshold

eta*log_2 p = r*b/n tends to rH, whereas
H_2(1-rho-eta) tends to H. Since r>1, the sufficient strict Elias
inequality eta*log_2 p>H_2(1-rho-eta) holds eventually.

The logarithm of the proposed threshold is

    log_2(c1*n)+c2*H*n/r = (c2/r)*b+O_(rho,r,c1,c2)(log b).

The constructed count has logarithm b-log_2 b+O_rho(1). For r>c2
its excess tends to infinity linearly in b. The construction exists
for every sufficiently large prime, not just a selected prime sequence.

## Relation to earlier results

This corollary changes the field quantifier and the required block
length in the line result. It is obtained by holding the number of
canceled moments fixed, depending on the proposed c2, while choosing
n near log_2(p)/H. It neither improves the growing-moment asymptotic
list exponent nor establishes a fixed-gap superlinear exception count.
