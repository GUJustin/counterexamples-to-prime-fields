# Full-block trajectory resource ceiling

2026-09-18. Independent audit: PASS, with a sharper uniform ratio. This is a coverage hypothesis on successful witnesses, not a theorem for all received lines.

Let a length-n received pencil be w_lambda=f+lambda g. Suppose disjoint nonempty blocks E_j have f=F_j and g=G_j, with F_j,G_j in the message polynomial space (degree<k). Assume ordinary common agreement is at most A<n, and test T=A+d≤n with d>0. A success is covered by this argument when some qualifying witness is exactly the polynomial Q_j(lambda)=F_j+lambda G_j for some j.

For each DISTINCT ordered pair (F_j,G_j), merge all its assigned blocks and let w_j denote their total size. Define its full persistent set

    C_j={x : F_j(x)=f(x) and G_j(x)=g(x)}, c_j=|C_j|.

Then w_j≤c_j≤A and Σ_j w_j≤n. Duplicate trajectories must be merged for a sharp count, but counting them separately also gives a valid weaker upper bound. Equality as polynomial trajectories is equality of both coefficient polynomials; trajectories meeting at an isolated parameter need not be merged.

At every coordinate outside C_j, the affine equation

    F_j(x)+lambda G_j(x)=f(x)+lambda g(x)

has at most one solution lambda. (It can have none when the slope difference vanishes and the intercept difference does not.) Hence the total number of nonpersistent match incidences, summed over all parameters, is at most n−c_j. Every qualifying parameter needs at least T−c_j such matches. Therefore

    B_j≤floor((n−c_j)/(T−c_j)).

The ratio R(c)=(n−c)/(T−c) has derivative (n−T)/(T−c)^2≥0. Since c_j≤A,

    B_j≤(n−A)/d.

Thus the sharper uniform numerator is n−A, not merely n. If every block has size at least D, the number m of distinct trajectories is at most floor(n/D), giving

    B_covered≤Σ_j B_j≤floor(n/D) floor((n−A)/d)
             ≤n(n−A)/(Dd).

In particular D,d=Omega(sqrt(n)) imply B_covered=O(n), with no restriction to pure quadratics. For T>n there are no successes. For T=n, the exact ratio is1; for d>A or other parameter ranges the same proof still holds provided A<n and T≤n. Parameters are affine/native field parameters; adding the projective point at infinity contributes at most one label.

## Weighted versions and limits

The informative weighted version, when the persistent sets are known, is

    B_covered≤Σ_distinct trajectories floor((n−c_j)/(A+d−c_j)).

A disjoint-block-only version is obtained by weighting each trajectory by its assigned block mass. Since w_j≥D,

    D B_covered≤Σ_j w_j B_j≤(n−A)/d ·Σ_j w_j≤n(n−A)/d.

More generally, if each successful label is covered by trajectories whose total assigned mass is at least W, then

    B_covered≤(n−A)·(Σ_j w_j)/(d W).

This includes the previous bound with W=D and improves it when successful labels have many distinct block-identity witnesses. It does not count a repeated representation of the same trajectory twice after merging.

Block sizes alone do not justify replacing c_j by w_j in the upper bound: R is increasing, so knowledge c_j≥w_j provides a LOWER bound on the ratio, not an upper bound. Persistent sets of distinct trajectories may overlap outside their assigned blocks; no bound Σc_j≤n is assumed. Such overlap or polynomial-degree constraints might provide a separate improvement, but the displayed weighted bounds require neither.

## Exact scope

The premise is polynomial identity with a trajectory, not merely a witness matching a few coordinates in a block. If a witness agrees with w_lambda on at least k distinct coordinates inside a block, degree<k root counting does imply this identity, so that is a sufficient way to verify coverage. Otherwise a witness may accumulate sub-k matches across many blocks, and it lies outside this gate. Therefore the route to superlinear populations must either use smaller blocks than the loss scale or make successful witnesses avoid every block identity; enlarging from scalar quadratics to arbitrary low-degree block trajectories alone does not evade the bound.
