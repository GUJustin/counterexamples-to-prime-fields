# Gold, elliptic quadratic forms, and the characteristic parameter

This is a quantitative reading of existing results, not a new construction theorem. The binary repository was read only. Sources are `sections/constructions/fullfield-elliptic.tex`, Theorem `thm:fullfield-elliptic` and Corollary `cor:elliptic-fixed-codimension`, and `sections/constructions/quadratic-near-johnson.tex`, Remark `rem:fixed-characteristic-all-rates`, in `/Users/jthaler/Documents/binary_field_counterexamples`.

Write b=ell for the varying odd prime characteristic. Using a prime power b instead is also valid. Agreement counts, common agreement CA, individual-source agreement, and the number of bad challenges are distinct quantities throughout.

## 1. The existing odd-characteristic replacement for Gold

The binary alternating-polar-form argument should not be transferred verbatim: in odd characteristic quadratic polar forms are symmetric. The existing elliptic trace-quadratic theorem supplies the correct replacement.

Let B=F_(b^m), m=2n, let D be B or an F_b-hyperplane, put d=dim_b D, h=m-d, N=b^d, and choose 2<=t<=n-h. Set

    M=b^(2t)(b^t-1) [n-h choose t]_(b²),
    delta=(b-1)N/b^(2t).

The two existing rows are

| row | dimension K | agreement T | ordinary list lower bound L |
|---|---:|---:|---:|
| low | N/b² | N/b-(b-1)N/b^(t+1) | M/(b-1) |
| high | (b-1)²N/b² | (b-1)N/b-N/b^(t+1) | M |

For every containing challenge field F of size q>N, the theorem constructs a pair with agr_K(g)=CA_K(f,g)=K and at least

    ceil( L(q-N)/(q-N+delta(L-1)) ) - 1

distinct nonzero bad challenges. This exact harmonic expression is preferable to assuming that an arbitrary desired real q is an available extension-field size.

Individual first-source bounds are, respectively,

    agr_K(f) <= (b+1)N/(2b²)-1,
    agr_K(f) <= floor(((b+1)K-2)/b)  (b>2).

The mechanism is an elliptic rank-2t trace-form population, translations modulo the radical, and the additive-locator differential identity. Its Frobenius compiler produces strict low-degree witnesses from level sets. These are characteristic-specific identities, not characteristic-zero deformation identities.

## 2. What degrades as b grows

The exact normalized common-source gaps T/N-K/N are

    low:  (b-1)/b² - (b-1)/b^(t+1),
    high: (b-1)/b² - 1/b^(t+1).

Both are asymptotic to 1/b when t grows. The rates tend to the endpoints: the low rate is b^-2 and the high rate is (1-1/b)². The high row's guaranteed gap above the *first individual source* is only of order b^-2, not b^-1; the low row's is of order (2b)^-1.

For the full-field domain and t near m/4, Gaussian-binomial estimates give

    log_b M = tm-2t²+3t+O(1),
    log L = (log N)²/(8 log b)+O(log N).

Thus the fixed-b quasipolynomial population becomes only a fixed polynomial in N if b=N^gamma and the extension degree m=1/gamma remains bounded. Integer constraints on m,t still apply. At t=m/4 exactly, delta=(b-1)sqrt(N). The harmonic count can retain a constant fraction of L when q-N is at least a constant multiple of delta L; its corresponding challenge-density scale is then 1/delta. This is not a uniform near-unit bad-density statement.

As a diagnostic, ideal balanced padding of the limiting low row to an intermediate rate rho gives agreement

    a = 1/b + (rho-1/b²)(1-1/b)
      = rho+(1-rho)/b-1/b²+1/b³.

Consequently its margin also vanishes as b grows. Fixed-characteristic all-rates and fixed-codimension corollaries explicitly allow their constants and onset to depend on b; they cannot be read as uniform growing-characteristic results.

## 3. Explicit codimension-two compiler: an existing corollary

The following displays the s=2 specialization of the existing fixed-characteristic locator compiler. It is useful because all dependence on b is visible.

Let D be F_b-linear of size N=b^d=b^4 K, d>=4. For every codimension-two subspace W, write its monic locator as

    L_W=X^(b²K)+a X^(bK)+c X^K+V,   deg V<=K/b.

Choose theta outside B. Define

    f=X^(b³K-1)+theta X^(b²K-1),
    g=X^(bK-1),
    z_W=c^b-a^(b+1)+theta a,
    H_W=-((theta-a^b)(cX^K+V)+V^b)/X.

The minus sign in H_W matters in odd characteristic. Direct expansion gives

    f+z_W g-H_W
      = L_W (L_W^(b-1)+theta-a^b)/X.

Here deg H_W<K. On D the second factor is nonzero, and the value at zero after cancelling X is nonzero, so the support is exactly W minus {0}: A=b²K-1.

The labels are injective. Their theta coordinate first recovers a, then their B coordinate recovers c. Two locators with the same a,c have difference of degree at most K/b but vanish on W intersect W', which has at least K points, so the locators coincide. The count is exactly

    [d choose 2]_b = (N-1)(N-b)/((b²-1)(b²-b)).

Moreover CA_K(f,g)=agr_K(g)=bK-1. For the lower bound choose a subspace U of size bK. Remainders of the three additive heads modulo L_U have degree at most K, and dividing them by X supplies simultaneous strict witnesses on U minus {0}. The upper bound follows from the degree of g minus any strict witness. If the containing field has dimension at least three over B, choose s outside B+B theta and replace f by f+s g. Projection to the s coordinate then also bounds its individual agreement by bK-1; common agreement supplies equality. This last exact two-source conclusion uses the stated extension hypothesis.

The resulting ledger is

    rho=b^-4,
    A/N=b^-2-1/N,
    CA/N=b^-3-1/N,
    (A-CA)/N=(b-1)/b³,
    bad-count=[d choose 2]_b ~ N²/b^4.

These are derived explicit parameters, not an improvement over the existing compiler. The actual agreement satisfies

    A²-N(K-1)=(b^4-2b²)K+1>0.

For K>=2 the lower advertised threshold b²(K-1) lies below sqrt(N(K-1)); it loses b²-1 matches from the actual support. This is a constant-coordinate loss for fixed b, but not uniformly as b varies.

## 4. The exact prime-field obstruction

The obstruction occurs before the collision analysis or challenge-field conversion. The elliptic construction requires an additive domain supporting rank at least four; the sparse specialization requires d>=4. Thus in characteristic ell these mechanisms require N>=ell^4 and a field containing a nontrivial extension of F_ell. A domain contained in the prime field F_ell has F_ell-linear dimension at most one. It cannot host the required subspace lattice or quadratic-rank population.

Allowing ell to vary does not remove this obstruction: within these constructions ell<=N^(1/4), whereas a prime-field realization would require N<=ell. These conditions are incompatible for ell>1. This is a barrier to this specific additive-subspace mechanism, not a theorem excluding other prime-field constructions.

The strongest transferable lesson is therefore structural: many low-rank forms or many codimension-two locators yield many distinct strict explanations, and an exact differential/compiler identity controls common-source agreement. What does not transfer is the required high-dimensional vector-space domain inside a prime field, nor a characteristic-uniform positive source margin.

## 5. Large-characteristic first-order frontier of the unpadded compiler

For the codimension-s compiler on n=p^d, the exact seed parameters are

    K=p^(d-s-2), D=K-1, A=p^(d-s)-1,
    M=[d choose s]_p ~ p^(s(d-s)).

Assume s>=1, d>=s+2, and p tends to infinity with s,d fixed. The guard p>D forces d<=s+3. The low-rate first-order threshold is asymptotic to sqrt(rho/2), whereas rho=K/n=p^(-s-2) and A/n~p^(-s). Their ratio is asymptotic to sqrt(2)*p^(1-s/2). Consequently s>=3 fails first order, even though its formal population exponent can exceed 6/5. For s=2 the largest allowable d is five, giving exponent 6/5. For s=1 the largest d is four, giving exponent 3/4. At d=s+2 the witnesses are constant and the population exponent is smaller. Thus the existing unpadded codimension compiler has no larger asymptotic exponent under these simultaneous conditions. This is a parameter frontier for this construction, not a universal upper bound.

The existing elliptic low row has K=p^(d-2), so p>D requires d<=3. Its quadratic-rank hypothesis t>=2 requires d>=4 for a full-field domain, and d>=5 for the hyperplane version. Hence it has no unshortened admissible instance under p>D. The high row and odd-norm rows likewise have dimension proportional to their extension-field domain and do not provide the requested regime directly.

### A specific possible escape: affine locator fibers

Affine codimension-two flats offer p^2 cosets per linear W, but one must not count them as extra labels without checking the compiler. Before division by X, for L_W additive the relevant composition is

    P_W(X)=L_W(X)^p+(theta-a_W^p)L_W(X).

Replacing the zero fiber by L_W(X)=v changes the constant by

    v^p+(theta-a_W^p)v.

To retain a polynomial degree-(p-1) witness after division by X, this constant must vanish. For the field-domain seed with theta outside its coefficient field B, v in B forces v=0. Without division by X the witnesses have degree p, missing p>D by one. Thus the naive affine-flat enlargement is invalid.

These affine fibers have the SAME label for a fixed W; they increase agreement, not label population. For s=2 this alone cannot improve the 6/5 exponent.

A sharper noninherited target uses s=3,d=6,K=p. Its existing formal population is [6 choose 3]_p~p^9=n^(3/2), but its single-flat agreement p^3 is below first order, whose absolute scale is p^(7/2)/sqrt(2). The outer compiler is an additive polynomial of degree p^2 in L_W. If its kernel intersects L_W(D) in at least p elements for many W, each witness would agree on at least p^4-1 points (a union of at least p cosets), more than enough. One could then advertise a below-Johnson threshold near p^(7/2), while retaining p>D. Thus a potential 3/2-exponent candidate is precisely a common source-head choice producing such a kernel intersection for a p^9-scale family, with distinct labels.

No such family is established. If the domain is an entire field B and all head parameters lie in B, the labels lie in B and number at most n; independent extension head parameters instead prevent the desired additional kernel fibers. A possible escape would require a non-field six-dimensional additive domain in a larger coefficient field, or a carefully dependent extension-head choice. The decisive missing object is simultaneous outer-kernel intersections AND enough distinct labels, not merely a larger count of affine flats.

### Outer-fiber target resolved by support packing

The proposed s=3 target is excluded by an elementary absorption bound. Put d0=p^2-1. Distinct labels give distinct ordinary codewords H_z-zg of degree d0. An extra outer-kernel dimension gives at least A=p^4-1 agreements on N=p^6 points. Since A^2-N*d0=p^6-2p^4+1>0, pair counting bounds the population by

    N(A-d0)/(A^2-N*d0) = O(p^4).

The parity-correct s=4,d=7 alternative has nominal population p^12 and would clear first order after one extra fiber, but a stronger packing argument also excludes an improvement. This argument works for arbitrary additive domains and dependent head choices.

Suppose the canonical residual multiplied by X is F_p-linearized on a d-dimensional domain. Its roots form a subspace; zero itself can change the agreement count by at most one. For two distinct labels, the witness difference after absorbing the direction has exact degree p^2-1. Their root subspaces therefore intersect in dimension at most two: an intersection of dimension three would supply p^3-1 common nonzero agreements.

For d=7, first-order agreement requires at least a four-dimensional root subspace for all sufficiently large p. Choose one such subspace for each retained label. Their annihilators are three-dimensional subspaces of the dual seven-space, intersecting pairwise in dimension at most one. Counting two-dimensional subspaces yields

    M <= [7 choose 2]_p / [3 choose 2]_p = O(p^8)=O(N^(8/7)).

Thus this extra-fiber variant cannot improve the existing N^(6/5) lower bound, regardless of whether the outer-kernel and collision conditions can be solved.

More generally, keep K=p, direction degree p^2-1, and a fixed additive dimension d. The first-order absolute threshold is asymptotic to p^((d+1)/2)/sqrt(2). If d=2r-1>=5, qualifying canonical root subspaces have dimension at least r. Their annihilators have dimension r-1 and pairwise intersection at most one, giving

    M <= [d choose 2]_p / [r-1 choose 2]_p
      = O(p^(2r)) = O(N^(1+1/d)).

If d=2r>=6, qualifying subspaces have dimension at least r+1. Their annihilators have dimension r-1 and pairwise zero intersection, giving

    M <= (p^d-1)/(p^(r-1)-1)=O(p^(r+1)).

The largest odd-dimensional exponent is 6/5 at d=5, attained in scale by the existing seed. These bounds concern canonical witnesses with linearized residuals and this direction degree; they do not exclude different source degree profiles or nonadditive agreement supports. They settle the proposed extra-outer-fiber route without a finite search.
