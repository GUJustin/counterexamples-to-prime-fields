# Independent audit: delete two endpoint supports in the Fp3 construction

PASS for the guaranteed population and far-source conclusion below. One counting caveat: p³−p² is the exact size of the retained parameter region, not necessarily the total number of qualifying or singleton labels after puncturing.

Use `fp3_common_agreement.tex` with p≥4099, N=2p²−p−1, A=2p−ceil(4sqrt(p))−2. For a direction u, write P_u=I_u+eta I_u. Every P_u is a two-dimensional F_p-plane containing the common exceptional line Lambda0. Choose distinct alpha,beta in P_u\Lambda0. Their unique high witnesses Q_alpha,Q_beta have the same quadratic leading coefficient a_u, and each has a full matching support of size at most 2p+4sqrt(p).

Delete the union R=S_alpha union S_beta of those supports. Then

    |R| <=4p+8sqrt(p),
    N'=N−|R| >=2p²−5p−8sqrt(p)−1,
    T=A−8=2p−ceil(4sqrt(p))−10.

At alpha the unique high witness now has zero matches. Every other quadratic had at most C=max(16,p+2sqrt(p)) matches before deletion, by the original exhaustive classification, and deletion cannot increase them. The same holds at beta. Thus both restricted endpoint words have agreement at most p+2sqrt(p)<T. Ordinary common agreement is also at most p+2sqrt(p), because restriction cannot increase it and invertible changes of the source pair preserve it.

## All labels outside P_u retain singleton lists

There are exactly p³−p² such labels. None lies in Lambda0, so it originally had exactly one high canonical witness Q_lambda, of slope different from a_u. At a removed point in S_alpha where Q_lambda also matches its own word,

    Q_lambda−Q_alpha=(lambda−alpha)g.

On each of the two blocks g is constant zero or one. The polynomial on the left minus that constant has nonzero quadratic leading coefficient, because the slopes differ. Hence it has at most two roots on each block. At most four Q_lambda matches are lost to S_alpha, and at most four to S_beta. Thus Q_lambda retains at least A−8=T matches.

Every other word at lambda had at most C matches originally and still does. Since T>C, its new list is exactly the singleton Q_lambda. The retained p³−p² labels therefore certify population Theta(p³) and singleton fraction at least 1−1/p in the raw affine parameterization. Parameters inside P_u may also remain close. In particular, the multiple witnesses at Lambda0 need not disappear. Do not claim an exact total count after puncturing.

For the two far sources F=f+alpha*g and G=f+beta*g, their affine mixtures correspond bijectively to raw labels lambda=alpha+t(beta−alpha). For the alternate pencil F+tG, the non-infinite parameters satisfy lambda=(alpha+t beta)/(1+t); all retained labels map to distinct nonzero finite t. Its extra t=−1 direction has the two constant witnesses, as in the unpunctured step-direction discussion, since each remaining block is still much larger than T. This distinction does not affect the guaranteed singleton population.

## Thresholds and finite certificate survive

For p≥4099, sqrt(p)≥64 and

    T >=2p−5sqrt(p),
    N' <=N.

The same low-rate bound used in the original proof gives N'*a1(3/N')<7p/4+sqrt(p)<T. For the Johnson inequality, N'>=2p²−6p and T<=2p−sqrt(p), so

    2N'−T² >=4p*sqrt(p)−13p >0.

The code dimension remains three and the characteristic guard remains p>3.

For the exact derivative-weighted certificate choose m=6, derivative cap3, B=3T, H=40B. The original rank calculation remains R=62 and G=4B²−2B. Moreover

    B >=6p−12sqrt(p)−33 >=29p/5,
    B <=6p.

The second inequality in the first line follows since p/5−12sqrt(p)−33 is positive at p=4096 and increasing thereafter. Therefore the original coarse margin remains valid, now with the smaller N':

    39G−40*62*N' >=(7196/25)p²−468p >0.

It follows that G>62N' and (H−B+1)G−(H+1)62N'>0. This is a uniform finite first-order certificate with reconstruction guard p>max(2,3). No asymptotic-only substitution or stronger characteristic assumption is needed.

The resulting two endpoint agreements and common agreement are bounded above by p+2sqrt(p), while T differs by Theta(p). No exact agreement equality is asserted. The parameter and length asymptotics remain q=p³, N'~2p², with at least p³−p² singleton qualifying labels. No manuscript edits or numerical search were used for this audit.

## Sharper shared-witness choice (independently checked)

The following strengthens the deletion and loss constants without changing the basic proof. Take u1=eta*u0∈W. Since I_u1=(delta/u1)F_p,

    eta I_u1=(delta/u0)F_p=Lambda0.

The line I_u1 is distinct from Lambda0. Therefore, for every nonzero b∈I_u1, all p labels b−eta*v, v∈I_u1, lie outside Lambda0 and share the same unique high witness Q=a_u1 X²+b.

The nonzero core fibers for this direction partition D0 minus its zero fiber. Their total physical size is (p²−1)−(p−1)=p²−p, over p−1 choices of b. Choose a nonzero b whose core fiber has size at most p. On the fresh block, the p fibers indexed by v∈I_u1 partition the trimmed D1 of size p²−p. Choose two distinct v1,v2 with the two smallest fiber sizes; their sum is at most twice the mean, 2p−2. These choices are independent of b. Both endpoint labels are generic by the preceding coset calculation.

Deleting their full matching supports therefore removes just one core fiber and two distinct fresh fibers, with

    |R|<=3p−2,  N'>=2p²−4p+1.

For a retained witness of any other direction, comparison with Q on the deleted core fiber gives at most two lost matches. Comparison on each of the two fresh fibers gives at most two more, for total loss at most six. Thus take T=A−6. At the endpoints Q is erased entirely and every other word remains below p+2sqrt(p). All p³−p² labels outside P_u1 retain singleton lists as before; the same exact-total caveat applies.

The earlier threshold and finite-certificate proof already works for the weaker bounds N'>=N−4p−8sqrt(p) and T=A−8, so it immediately applies to this stronger choice (or use B=3(A−6), with the same lower and upper bounds 29p/5≤B≤6p). This sharper construction also keeps both source agreements and common agreement bounded by p+2sqrt(p), without asserting exact equality.
