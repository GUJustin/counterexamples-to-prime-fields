# Higher-power blocks at minimal dimension: positive-regime audit

2026-09-18. Independent verdict: **PASS** for the asymptotic construction below, subject to the explicit finite conditions stated here. This is distinct from the earlier D=Theta(p) enlargement: here the message dimension is k=h+1. No manuscript edits or scans were made.

## Finite algebra and retained-domain conditions

Use the primitive-scale setup of HIGHER_POWER_FROBENIUS_BRANCH_AUDIT.md: B=F_(p²), E=F_(p⁴), M=p²+1, a proper divisor h of M, and primitive s in E*. Set eta=s^h, which is outside B. The disjoint full blocks D0 and D1=sD0 each have

    N1=h(p²-1)

coordinates. The received sources before reparametrization are f=x^(hp), g=0 on D0 and f=s^(h-hp)x^(hp), g=1 on D1. Take the strict code dimension k=h+1.

Fix 0<c<1, retain all D0 and an m=floor(c*N1) subset D1' of D1, and put

    n=N1+m,  T=floor(sqrt(h*n-1)).

Thus T is exactly the largest integer strictly below the Johnson agreement sqrt((k-1)n).

Every noncanonical polynomial (not of the form aX^h+b) has at most hp+h² matches, provided

    h-1<M/h,  h<hp.

These are the previous branch guards at D=h. Every canonical polynomial not rich on both full blocks has at most hp matches: a coefficient a outside B gives at most one y=x^h solution per block; a in B with norm different from one also gives at most one; a of norm one gives a full affine p-fiber or no solutions. Thus the non-double canonical bound is max(hp,2h)=hp.

The canonical family rich on both blocks is exactly

    Q_(a,b)=aX^h+b,
    a^(p+1)=1, b,v in I_a=image(y^p-a*y on B),
    lambda=b-eta*v.

Its first-block supports have hp coordinates if b!=0 and h(p-1) if b=0. Fresh supports similarly have hp or h(p-1) coordinates according to v. This follows because x -> x^h maps each full block onto the corresponding B* coset, with exactly h preimages per nonzero value. There are p(p+1) different fresh supports.

For an exact finite retention criterion, let

    L=T-h(p-1),  delta=m/N1,
    gamma=delta-(L-1)/(h(p-1)).

If gamma>0 and p(p+1)*exp[-2h(p-1)gamma²]<1, a uniformly sampled m-subset has positive probability of meeting every fresh support in at least L points. This is the sampling-without-replacement Hoeffding inequality, applied to each fixed support; the zero fiber gives the worst support size. Provided also hp+h²<T, every qualifying word is doubly canonical and every doubly canonical word qualifies.

For a simpler sufficient asymptotic check, suppose c>=1/2 and N1>=4/c. The retained proportion is at least 3c/4. Hoeffding shows that every fresh support retains at least c/2 times its size with positive probability whenever

    p(p+1)*exp[-c²*h(p-1)/8]<1.

The resulting canonical agreement is at least (1+c/2)h(p-1). For fixed c>=1/2 and sufficiently large p this exceeds hp*sqrt(1+c)>=T, since (1+c/2)²-(1+c)=c²/4. This sufficient argument is uniform as c approaches one.

## Exact label profile and source/common agreement

The p+1 planes I_a+eta I_a have dimension two over F_p and intersect pairwise only at zero. Indeed, 1 and eta are linearly independent over B, so a common representation forces both B-components to lie in the intersection of two distinct F_p-lines I_a. Each plane has p²-1 nonzero elements. Consequently, under the retention and threshold conditions above, the finite affine pencil f+lambda*g has exactly

    B_count=(p+1)(p²-1)

singleton-list parameters, one parameter lambda=0 with list size p+1, and empty threshold lists elsewhere. There is no support-pair overcount.

Choose distinct alpha,beta outside the union of these planes and define r=f+alpha*g, s0=f+beta*g. They exist since the union has only 1+B_count<p⁴-1 elements. Each source's maximum agreement lies in

    [hp, hp+h²].

The lower bound is attained by a canonical first-block fiber with nonzero b. Ordinary common agreement is EXACTLY hp. To verify the upper bound directly for (f,g), a nonconstant degree-at-most-h polynomial explaining g has at most h roots at each of the levels zero and one, so contributes at most 2h common matches. A constant explanation confines common matches to one block, where f minus any degree-at-most-h polynomial is nonzero of degree hp and has at most hp roots. The lower bound uses the same hp-point core fiber and the zero polynomial for g. Invertible linear changes of the pair preserve ordinary common agreement, so CA(r,s0)=hp as well.

The normalized affine interpolation (1-z)r+z*s0 corresponds to lambda=alpha+z(beta-alpha), a bijection on E. Thus it retains the complete list profile and has both individually far endpoints. No infinite parameter or omitted label must be added to this count.

## The minimal-dimension positive regime

Let h tend to infinity slowly, set

    c=1-2/sqrt(h),  k=h+1,

and choose p much larger than h^4, with h dividing p²+1. Eventually c>=1/2, all finite branch/retention conditions hold, and hp+h²<T. The parameters satisfy

    n=(2-2/sqrt(h)+o(1))*h*p²,
    CA=hp,
    hp <= agr(r),agr(s0) <= hp+h²,
    T=(sqrt(2)+o(1))*hp.

This regime remains ABOVE first order. The actual low-rate first-order bound used in projective_quadratic_line.tex is

    sqrt(rho/2) < a1(rho)
       <= sqrt(rho/2)+(rho/2)^(3/4)/sqrt(3).

At rho=k/n this gives

    n*a1(k/n) <= sqrt(k*n/2)+(k³*n/8)^(1/4)/sqrt(3).

The correction is O(h*sqrt(p)), not a dimension-three specialization. For h>=25, using n<=h(2-2/sqrt(h))*p²,

    sqrt(k*n/2) <= hp*sqrt((1+1/h)(1-1/sqrt(h)))
                  <= hp-(2/5)*p*sqrt(h).

The O(h*sqrt(p)) correction is smaller than this deficit when p/h tends to infinity; the stipulated p>>h^4 is more than sufficient. Hence

    n*a1(k/n) < hp = CA <= agr(r),agr(s0) < T < sqrt(h*n).

Moreover all these agreements divided by hp converge to one at the source end, while T/(sqrt(h*n)) tends to one. In particular

    CA/[n*a1(k/n)] -> 1,
    agr(r)/[n*a1(k/n)] -> 1,
    agr(s0)/[n*a1(k/n)] -> 1,
    T/Johnson -> 1.

Thus the source-to-test agreement loss asymptotically spans the first-order-to-Johnson interval in this extension-field, vanishing-rate regime. This is an endpoint-location statement, not a claim that the exceptional count meets a general upper bound.

The loss divided by the capacity agreement surplus has the same limit for common agreement and either individual source:

    (T-CA)/(T-k) -> 1-1/sqrt(2),
    (T-agr(r))/(T-k), (T-agr(s0))/(T-k) -> 1-1/sqrt(2).

The h² uncertainty in individual agreements is negligible because h/p -> 0. The limit is approximately0.292893, rather than the fixed-quadratic h=2 density limit. Message dimension is growing, so this is not a stronger dimension-three assertion.

## Prime sequence and population exponent

An explicit existence schedule is h_a=5^a, a>=2. The congruence u²=-1 modulo5 has a simple root, which lifts modulo5^a because its derivative2u is a unit. Fix such a root u_a. Dirichlet's theorem supplies arbitrarily large primes p congruent to u_a modulo h_a. Choose one with

    p > h_a^(a+4).

Then h_a divides p²+1, is a proper divisor, satisfies p/h_a^4 -> infinity, and log(h_a)/log(p) -> 0. No effective least-prime estimate or prescribed practical prime is asserted.

Along this sequence,

    h=p^o(1),   n=p^(2+o(1)),   k=h+1=n^o(1),
    rho=k/n=(1+o(1))/(2p²)=n^(-1+o(1)),
    |E|=p⁴=n^(2-o(1)),
    B_count=(1+o(1))*p³=n^(3/2-o(1)).

The selected domain lies in F_(p⁴); the characteristic exceeds k, but the alphabet is not prime and the domain is not a prescribed NTT/circle domain. The retained subset is supplied probabilistically with a uniform finite criterion, not by an enumerated practical fixture. This positive minimal-dimension regime does not contradict the earlier negative rate ledger for D=Theta(p): the two choices of message dimension are different.
