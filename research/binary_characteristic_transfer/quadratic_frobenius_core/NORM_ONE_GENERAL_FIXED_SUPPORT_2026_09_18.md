# Fixed supports give linear lists for every c greater than sqrt(2)

September 18, 2026. Explicit finite-certificate derivation from the cached primary DKT paper, Proposition 5.10 / Eqs. (60)--(63), and Lemma 5.6 / Eqs. (54),(56). This is a consequence of the existing support machinery for degree-two messages, not a new construction or a claim that the published asymptotic first-order curve has changed. Integrated as Corollary N.27 after an independent audit.

## Result

Fix sqrt(2)<c<2. For all sufficiently large primes p depending on c, put

    N=2(p²+p+1), T=ceil(cp).

Every received word on every length-N, dimension-three Reed--Solomon domain in characteristic p has at most C_c N threshold-T witnesses, with C_c=O((c²-2)^(-3)). On the existing norm-one domain over F_(p³), the received word X^(2p+2) has its exact N/2-element list at T. Thus the maximum list is Theta_c(N).

Only when c>sqrt(3) is this eventually above the specific curve N*a1(3/N), whose leading term is sqrt(3)p. The interval sqrt(2)<c≤sqrt(3) is an additional finite-degree consequence of the same support; do not label it the strict first-order-to-Johnson interval. The alphabet remains an extension field and the rate tends to zero.

## Exact support counts

Choose integers h≥1 and s≥h. Use multiplicity m=2h, derivative cap s, joint cap B=hT. Assume B≥2h+s; this convenient sufficient condition makes every nonzero local block active and implies s≤B. The coefficient count is exactly

    G=(s+1)B(B+1-s/2).

Indeed, for a fixed derivative exponent b, summing the strict X-degree allowance 2B-2t+b over b≤t≤B gives B(B-b+1). Summing b=0,...,s gives G.

For local index a=0,...,2h-1, the count of source coefficients as t varies is the convolution of intervals of lengths a+1 and s+1. Truncating the overlap at 2h-a gives total

    R_a=q(a+s+2-q), q=min(a+1,2h-a,s+1).

Because s≥h, q=a+1 for a<h and q=2h-a for a≥h. Summation yields the exact integer

    R=h(h+1)(6s+2h+7)/6.

The strict specialization cutoff a+t<2B also holds: a+t≤4h+s-2<2B under the assumed B bound. These are original coefficient/local-rank sums, not asymptotic substitutes.

As p grows, G>NR has leading condition

    c² > ccrit²(h,s)
       = 2R/((s+1)h²)
       = 2 + 2/h + (h+1)(2h+1)/(3h(s+1)).

For s=h this is (8h+7)/(3h). Hence h=7 gives critical value 3 exactly, while h=8 gives 71/24<3. Increasing s beyond h is valid in Proposition 5.10: there is no cap s≤m/2. First increasing h and then s makes ccrit² approach 2 from above. We have not claimed optimality over all possible supports.

## Explicit parameters and an actual finite onset

Set delta=c²-2 in (0,2), and choose

    h=ceil(8/delta), s=ceil(8h/delta),
    kappa=ceil(4c²/delta), H=kappa B.

Then s≥h and

    2/h≤delta/4,
    (h+1)(2h+1)/(3h(s+1))≤2h/(s+1)≤delta/4,

so ccrit²≤2+delta/2<c². The middle inequality holds for every h≥1.

To make “sufficiently large” an explicit finite test, define

    g2=(s+1)h²c²,
    g1=(s+1)h(s/2-1)c,
    a2=(kappa-1)g2-2kappa R,
    a1=(kappa-1)g1+2kappa R,
    a0=2kappa R.

Here h≥4 and s≥4, so g1≥0. Moreover a2>0: divided by (s+1)h² it equals kappa(c²-ccrit²)-c²≥kappa*delta/2-c²≥c².

Choose a prime p satisfying

    p>max{s, 3/(c-1), (2h+s)/(hc), 1, (a1+a0)/a2}.

Then B≥2h+s and the quadratic formula for G is increasing throughout T≥cp, giving G≥g2 p²-g1 p. Consequently

    (kappa-1)G-kappa NR ≥ a2 p²-a1 p-a0 >0.

In particular G>NR, and the conservative graded certificate is strictly positive:

    (H-B+1)G-(H+1)NR
       =B[(kappa-1)G-kappa NR]+(G-NR)>0.

This verifies the full Proposition 5.10 certificate even with a challenge variable. For the fixed-word application that variable is unnecessary, but retaining it avoids any ambiguity about the support hypotheses. Reconstruction uses only p>max(2,s), already enforced. There is no requirement p>B, p>mT, or p>N.

For an arbitrary fixed real c the bounds above are real inequalities specifying an onset; for a rational c they are exact arithmetic tests apart from the explicit ceilings in the chosen fixed integers. One can also choose any rational c0 strictly between sqrt(2) and c, build the certificate at ceil(c0 p), and use monotonicity of lists to obtain the threshold-c result.

## Uniform list bound

For degree two, Eq. (54) gives, once B≥2h+s,

    Freg=(2s+1)B-s(s+1),
    S=(2s-1)B-s².

The max with B in the definition of S selects this expression because s≥4 and B≥s+1. Write lambda=(N-2)/(T-2), C=h(2s+1), and d0=2C-s(s+1). Equation (56) is exactly

    list≤lambda Freg+S
        =C N+d0 lambda+h(2s-1)T-2C-s².

Our onset gives T≥p+3, so lambda≤2p. Since c<2, ceil(cp)≤2p. Thus with

    Kcorr=2 max(d0,0)+2h(2s-1),

we have list≤C N+Kcorr p. Requiring also p≥Kcorr/2 gives list≤(C+1)N, since N≥2p². This is an explicit C_c=C+1, independent of p. The choices h=O(delta^-1), s=O(delta^-2) give C_c=O(delta^-3).

Finally T>p+1 and T≤2p<2p+2, so the previously proved complete norm-one list remains exactly N/2 throughout these parameters. The lower bound needs no new witness or decoding calculation.

## Optimization scope: sqrt(2) is the infimum for this particular ledger

For arbitrary fixed multiplicity m and derivative cap s, with joint cap floor(mT/2) and all local blocks active, write q_a=min(a+1,m-a,s+1). The same interval-convolution count gives

    R_a=q_a(a+s+2-q_a).

For each a, R_a/(s+1)≥min(a+1,m-a). If s+1 is the minimum then the left side equals a+1; otherwise it equals q_a+q_a(a+1-q_a)/(s+1) with q_a=min(a+1,m-a). Therefore

    R/(s+1)≥sum_(a=0..m-1) min(a+1,m-a)
              =floor((m+1)²/4).

The leading coefficient condition for this support and this rank upper bound is c²>8R/((s+1)m²). Its critical squared constant is consequently strictly greater than 2 for every fixed m,s. The preceding even-m family approaches 2, so sqrt(2) is the exact infimum WITHIN this fixed rectangular derivative-cap / joint-cap ledger. This is not an impossibility theorem for actual interpolation kernels, different supports, or other list-counting arguments. In particular an upper bound on local rank need not be an exact global constraint rank.

## Relation to the safe finite corollary

The separately audited p≥401, m=16, s=8, H=100B result gives a clean numerical 137N bound throughout ceil(sqrt(3)p)≤T≤2p+2. It is already suitable for manuscript integration. The present result is a separate general-parameter strengthening; its large c-dependent onset is not a replacement for that useful finite constant.
