# Arbitrary retained higher-power blocks: exact canonical moments

2026-09-18. Independent resource calculation. This is not a universal short-domain impossibility theorem or a construction of a partial bank.

Use the normalized y-coordinates in B=F_(p²) for the two higher-power blocks. Retained physical coordinates give weights w_i(y) in {0,...,h}, with w_i(0)=0. Put n_i=sum_y w_i(y), n=n_0+n_1, and S_i=sum_y w_i(y)²<=h*n_i. For each norm-one slope a, let r_i(a,b) be the retained weight of its affine fiber y^p-a*y=b. There are p fibers per slope and p+1 slopes. Canonical witness instances are indexed by (a,b,v), and their agreement is

    A_(a,b,v)=r_0(a,b)+r_1(a,v).

Nonzero challenge labels have unique such instances; zero has p+1 instances. Thus the number of qualifying distinct labels is at most the number of qualifying instances. All statements below allow arbitrary puncturing and nonuniform lift weights.

## Exact first and second moments

Across the (p+1)p² canonical instances,

    sum A = p(p+1)*n,             mean A = n/p.

For each block, distinct y-points share exactly one affine prime-plane line, while a repeated point is on p+1 lines. Therefore

    sum_(a,b) r_i(a,b)² = n_i²+p*S_i.

Expanding the paired sum gives the exact centered identity

    sum_(a,b,v) (A_(a,b,v)-n/p)²
       = p²(S_0+S_1)-n_0²-n_1².

The cross term is 2(p+1)n_0*n_1; it is essential to retain this factor. In particular, if T>n/p and B_T counts qualifying distinct labels, then

    B_T <= [p²(S_0+S_1)-n_0²-n_1²]/(T-n/p)²
         <= p²*h*n/(T-n/p)².

This is a finite exact bound before the last inequality. Requiring EVERY canonical instance to qualify gives the simpler necessary condition T<=n/p directly from the first moment.

## A positive fraction of the canonical bank still forces long domains

Suppose B_T>=delta*(p+1)(p²-1), where delta>0 is fixed, and T>=a*sqrt(h*n). If T<=n/p then n>=a²*h*p² already. Otherwise the variance bound yields

    a <= sqrt(n/(h*p²)) + p/sqrt(delta*(p+1)*(p²-1)).

Consequently

    n >= h*p² * [a-p/sqrt(delta*(p+1)*(p²-1))]_+².

For fixed delta and a this is n>=(a²-o(1))*h*p². Thus retaining a fixed positive fraction of all canonical labels is almost as restrictive, to leading order, as retaining them all. In particular, a Johnson-scale threshold with a approaching one cannot preserve a positive canonical-bank fraction at n=o(h*p²).

This does NOT exclude a smaller superlinear bank. When T=Theta(sqrt(h*n)) and n=o(h*p²), the variance bound gives only B_T=O(p²), which can exceed n. A vanishing fraction of the original roughly p³ instances remains possible.

## Stronger partial-bank ledger when a source gap is required

Let U bound every individual canonical block weight, for example the maximum source agreement of either endpoint: any one-block canonical fiber can be explained at any label by adjusting its intercept. Suppose T-U>=g>0. Every qualifying pair must then use a g-rich fiber from EACH block. Write R_i(a) for the number of these fibers at slope a. Necessarily

    B_T <= sum_a R_0(a)R_1(a),
    R_i(a) <= floor(n_i/g).

The exact one-block centered variance is

    V_i=sum_(a,b)(r_i(a,b)-n_i/p)²=p*S_i-n_i²/p.

When g>n_i/p, summing rich fibers gives sum_a R_i(a)<=V_i/(g-n_i/p)². Hence

    B_T <= min{
       floor(n_0/g)*V_1/(g-n_1/p)²,
       floor(n_1/g)*V_0/(g-n_0/p)²
    }.

In the regime n=o(h*p²), g>=c*sqrt(h*n) for fixed c>0, this is O_c(p*sqrt(n/h)). Therefore a superlinear count B_T/n -> infinity requires n=o(p²/h) within these assumptions. The broad intermediate range is excluded by this resource inequality, but the much shorter regime is not. It still needs an actual rich-line construction and source/label control.

The source-gap ledger was also derived independently by the short-domain agent. These inequalities concern only the full higher-power canonical family and its arbitrary retained weighted y-sets. They do not constrain unrelated witness families or received sources, and no count upper bound here is a positive existence result.
